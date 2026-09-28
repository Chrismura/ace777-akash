#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REPLAY — FILTRE DE RÉGIME v2 (CORRIGÉ 07/09 après audit de ma propre v1).
V1 (contaminée) : base 24h calculée sur les données de la fenêtre SEULE → pendant les
~12 premières heures, base=None → ok=False → ENTRÉES BLOQUÉES PAR ABSENCE DE DONNÉES
(pas par le filtre). Or toutes les catastrophes sont dans ces 12 premières heures.
V2 : 25 h de pré-data avant chaque fenêtre (base 24h réelle dès la 1re minute),
dédoublonnage des klines Binance, boot ancré au début de fenêtre.
Règle FIGÉE inchangée : entrée normale seulement si vol60 ≤ 1.5 × médiane24h (a priori) ;
BOOTSTRAP = porte de semis (90 min), jamais filtré. Mécanique BASE gelée identique.
"""
import csv, statistics, urllib.request, json
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = f"{ROOT}/runs"
URL = "https://fapi.binance.com/fapi/v1/klines"

QTY, FEE, RET = 0.10593, 1.760, 0.30
CAP_USDT = 50.0; CAP_PX = CAP_USDT / QTY
H_WIN, SLOT, BOOT_MIN = 7200, 300, 90
REG_MULT = 1.5        # FIGÉ a priori
VOL_WIN = 60          # minutes de vol réalisée
BASE_WIN = 24         # heures de référence (24 valeurs de vol60)

SEGMENTS = [
    ("S1 02-04/09", "2026-09-02T17:26:00Z", "2026-09-04T05:45:00Z"),
    ("S2 04/09",    "2026-09-04T05:46:00Z", "2026-09-04T16:52:00Z"),
    ("S3 05-07/09", "2026-09-05T07:11:00Z", "2026-09-07T07:00:00Z"),
]
FENETRES = {
    "VORTEX": f"{RUNS}/KLINES_1M_VORTEX.csv",
    "NUAGE":  f"{RUNS}/KLINES_1M_NUAGE.csv",
    "ORAGES": f"{RUNS}/KLINES_1M_ORAGES.csv",
    "MARS":   f"{RUNS}/KLINES_1M_MARS.csv",
}

def iso(s):
    return int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())

def fetch_klines(t0, t1):
    out, seen, cur = [], set(), t0 * 1000
    while cur < t1 * 1000:
        u = f"{URL}?symbol=BTCUSDT&interval=1m&startTime={cur}&limit=1500"
        with urllib.request.urlopen(u, timeout=20) as r:
            batch = json.loads(r.read().decode())
        if not batch: break
        for k in batch:
            t = int(k[0]) // 1000
            if t in seen: continue
            seen.add(t)
            out.append({"t": t, "o": float(k[1]), "h": float(k[2]),
                        "l": float(k[3]), "c": float(k[4])})
        cur = int(batch[-1][0]) + 60000
        if len(batch) < 1500: break
    out.sort(key=lambda r: r["t"])
    return out

def load_klines(path):
    rows, seen = [], set()
    with open(path) as f:
        rd = csv.DictReader(f)
        for r in rd:
            t = int(r["open_time"]) // 1000
            if t in seen: continue
            seen.add(t)
            rows.append({"t": t, "o": float(r["open"]), "h": float(r["high"]),
                         "l": float(r["low"]), "c": float(r["close"])})
    rows.sort(key=lambda r: r["t"])
    return rows

def simulate(kls_all, t_start, t_end, mode):
    """vol60/base sur kls_all (pré-data incluse) ; trades seulement dans [t_start, t_end)."""
    idx_map = [i for i, r in enumerate(kls_all) if t_start <= r["t"] < t_end]
    kls = [kls_all[i] for i in idx_map]
    if len(kls) < 200: return None
    n = len(kls_all)
    vol60 = [0.0] * n
    for i in range(n):
        lo = max(0, i - VOL_WIN)
        vol60[i] = sum((kls_all[j]["h"] - kls_all[j]["l"]) / kls_all[j]["c"] for j in range(lo, i))
    boot_deadline = t_start + BOOT_MIN * 60   # ancré à la fenêtre
    stats = {"ALPHA": None, "BETA": None}

    for name, side in (("ALPHA", 1), ("BETA", -1)):
        virtual, trades, pos = [], [], None
        for j in range(1, len(kls)):
            gi = idx_map[j]
            r, r_prev = kls[j], kls[j - 1]
            t = r["t"]
            if pos is not None:
                entry, ext, armed = pos["entry"], pos["ext"], pos["armed"]
                exit_px = reason = None
                if side == 1:
                    if r["h"] > entry: armed = True
                    ext = max(ext, r["h"])
                    if armed:
                        stop = max(entry, ext - RET * (ext - entry))
                        if r["l"] <= stop: exit_px, reason = stop, "trailing_stop"
                        elif r["h"] >= entry + CAP_PX: exit_px, reason = entry + CAP_PX, "cap"
                else:
                    if r["l"] < entry: armed = True
                    ext = min(ext, r["l"])
                    if armed:
                        stop = min(entry, ext + RET * (entry - ext))
                        if r["h"] >= stop: exit_px, reason = stop, "trailing_stop"
                        elif r["l"] <= entry - CAP_PX: exit_px, reason = entry - CAP_PX, "cap"
                if exit_px is None and (t - pos["ts"]) % 300 == 0 and t > pos["ts"]:
                    h_sum = sum(g for tt, g in virtual if t - 1 - H_WIN < tt < t - 1)
                    if h_sum <= 0: exit_px, reason = r["c"], "h_gate_off"
                if exit_px is not None:
                    gross = (exit_px - entry) * QTY * side
                    virtual.append((t, gross))
                    trades.append({"net": gross - FEE, "gross": gross, "reason": reason})
                    pos = None
                else:
                    pos["ext"], pos["armed"] = ext, armed

            if pos is None and r_prev["t"] % SLOT == 0:
                ts_check = r_prev["t"] + 59
                h_sum = sum(g for tt, g in virtual if ts_check - H_WIN < tt < ts_check)
                forced = (r_prev["t"] < boot_deadline)
                if h_sum > 0 or forced:
                    ok = True
                    if mode == "REGIME" and not forced:
                        # base = médiane des 24 dernières valeurs horaires de vol60 (pré-data → réelle)
                        span = BASE_WIN * VOL_WIN            # 1440 min = 24 h
                        lo = max(0, gi - 1 - span)
                        hourly = [vol60[x] for x in range(lo, gi - 1, VOL_WIN)]
                        base = statistics.median(hourly) if len(hourly) >= 12 else None
                        ok = (base is not None) and (vol60[gi - 1] <= REG_MULT * base)
                    if ok:
                        pos = {"entry": r["o"], "ext": r["o"], "armed": False, "ts": t}

        if pos is not None:
            last = kls[-1]
            gross = (last["c"] - pos["entry"]) * QTY * side
            trades.append({"net": gross - FEE, "gross": gross, "reason": "fin_segment"})

        n_full = sum(1 for x in trades if x["reason"] != "fin_segment")
        nets = [x["net"] for x in trades]
        hours = (t_end - t_start) / 3600
        stats[name] = {"n": n_full, "n_h": n_full / hours if hours else 0,
                       "gross": sum(x["gross"] for x in trades), "net": sum(nets),
                       "med": statistics.median(nets) if nets else 0.0,
                       "worst": min(nets) if nets else 0.0,
                       "gateoff": sum(1 for x in trades if x["reason"] == "h_gate_off")}
    return stats

def line(tag, st, hours):
    if st is None: return f"  {tag:<8} : —"
    a, b = st["ALPHA"], st["BETA"]
    n, net = a["n"] + b["n"], a["net"] + b["net"]
    return (f"  {tag:<8} : {n:3d} trades ({n/hours:4.1f}/h) | brut {a['gross']+b['gross']:+8.2f} "
            f"| net {net:+8.2f} | médian {(a['med']+b['med'])/2:+6.2f} | gateoff {a['gateoff']+b['gateoff']} "
            f"| pire {min(a['worst'], b['worst']):+7.2f}")

def main():
    print("=" * 96)
    print("REPLAY RÉGIME v2 (corrigé) — BASE (moteur gelé) vs REGIME (entrée si vol60 ≤ 1.5×médiane 24h)")
    print(f"QTY {QTY} · frais {FEE} $ · trailing {RET*100:.0f}% · cap +{CAP_USDT:.0f} $ · H 2h · mult {REG_MULT} FIGÉ a priori")
    print("CORRECTIONS v2 : pré-data 25h (base 24h réelle dès la 1re minute — v1 bloquait à tort les")
    print("entrées des 12 premières heures par base=None) · dédoublonnage klines · boot ancré fenêtre")
    print("=" * 96)

    t0, t1 = iso("2026-09-01T16:00:00Z"), iso("2026-09-07T07:00:00Z")
    kl_live = fetch_klines(t0, t1)
    print(f"\n[SEGMENTS RÉELS] {len(kl_live):,} barres 1m (dédoublonnées, pré-data depuis 09/01 16:00Z)")
    tot = {"BASE": 0.0, "REGIME": 0.0}; ntot = {"BASE": 0, "REGIME": 0}
    for name, s, e in SEGMENTS:
        t_s, t_e = iso(s), iso(e)
        hours = (t_e - t_s) / 3600
        base = simulate(kl_live, t_s, t_e, "BASE")
        reg = simulate(kl_live, t_s, t_e, "REGIME")
        print(f"\n  ### {name} ({hours:.1f} h)")
        print(line("BASE", base, hours)); print(line("REGIME", reg, hours))
        if base and reg:
            nb = base["ALPHA"]["n"] + base["BETA"]["n"]
            nr = reg["ALPHA"]["n"] + reg["BETA"]["n"]
            tot["BASE"] += base["ALPHA"]["net"] + base["BETA"]["net"]
            tot["REGIME"] += reg["ALPHA"]["net"] + reg["BETA"]["net"]
            ntot["BASE"] += nb; ntot["REGIME"] += nr
            print(f"    → écart net REGIME−BASE : {(reg['ALPHA']['net']+reg['BETA']['net'])-(base['ALPHA']['net']+base['BETA']['net']):+.2f} $ ({nb}→{nr} trades)")
    print(f"\n  TOTAL segments : BASE {tot['BASE']:+.2f} ({ntot['BASE']} trades) | REGIME {tot['REGIME']:+.2f} ({ntot['REGIME']} trades) | écart {tot['REGIME']-tot['BASE']:+.2f}")

    print("\n[4 FENÊTRES HISTORIQUES]")
    ftot = {"BASE": 0.0, "REGIME": 0.0}
    for fen, path in FENETRES.items():
        kl = load_klines(path)
        t_s, t_e = kl[130]["t"], kl[-1]["t"] + 60   # réchauffage 130 min (convention replays)
        try:
            pre = fetch_klines(kl[0]["t"] - 25 * 3600, kl[0]["t"])
            kl_all = pre + kl
        except Exception as ex:
            kl_all = kl
            print(f"  ({fen}: pré-data indisponible — {ex})")
        hours = (t_e - t_s) / 3600
        base = simulate(kl_all, t_s, t_e, "BASE")
        reg = simulate(kl_all, t_s, t_e, "REGIME")
        print(f"\n  ### {fen} ({hours:.0f} h)")
        print(line("BASE", base, hours)); print(line("REGIME", reg, hours))
        if base and reg:
            ftot["BASE"] += base["ALPHA"]["net"] + base["BETA"]["net"]
            ftot["REGIME"] += reg["ALPHA"]["net"] + reg["BETA"]["net"]
    print(f"\n  TOTAL 4 fenêtres : BASE {ftot['BASE']:+.2f} | REGIME {ftot['REGIME']:+.2f} | écart {ftot['REGIME']-ftot['BASE']:+.2f}")
    print("\n(Lecture honnête v2 : chiffres SANS l'artefact base=None de la v1. La règle finale sera")
    print(" re-gelée et validée un-essai. L'audit pires-trades montre que le filtre ne coupe pas la")
    print(" queue des catastrophes — l'assurance de queue = stop de structure (plan V3).)")

if __name__ == "__main__":
    main()
