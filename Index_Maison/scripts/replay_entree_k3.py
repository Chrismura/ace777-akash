#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REPLAY — FILTRE D'ENTRÉE K=3 (seuil sismique A1 appliqué à l'ENTRÉE, levier R33).
Lecture seule : klines 1m publiques Binance (même source que le shadow) + cache 4 fenêtres.
Zéro ordre, zéro contact moteur/champion. Aucune donnée future (causal strict).

Question (R33) : le problème est l'ENTRÉE (fréquence) + les FRAIS. Le shadow scénario C entre
à CHAQUE slot 5-min quand H=1 — en chop plat, ça paie le péage 1,76 $ en boucle pour des
micro-bruts < péage. Candidat : n'entrer que si la dernière minute fermée est SISMIQUE :
    amplitude 1m (high-low) > k × médiane des amplitudes des 120 min précédentes, k=3 (gelé A1/R30).
Le k=3 n'est PAS tuné ici : constante déjà validée A1/R30, appliquée à un nouvel usage (entrée).

Mécanique sortie = moteur shadow GELÉ inchangé (trailing 30 % + plancher breakeven,
cap gain +50 USDT, sortie h_gate_off aux bornes 5-min, frais 1,76 $/trade aller-retour).
QTY = 0.10593 BTC (gelé R24). Gate H : somme des bruts des trades clôturés (2h glissantes) > 0.

Étendue : 3 segments shadow réels (02-07/09, découpe des redémarrages) + les 4 fenêtres
historiques (VORTEX/NUAGE/ORAGES/MARS) — l'essai un-essai du candidat se lit sur les 4 fenêtres.
"""
import csv, glob, statistics, urllib.request, json, os
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = f"{ROOT}/runs"
URL = "https://fapi.binance.com/fapi/v1/klines"

# ---- constantes GELÉES (shadow R24 + A1/R30) ----
QTY      = 0.10593
FEE      = 1.760          # USDT par trade aller-retour, imputé à la clôture
RET      = 0.30           # trailing rend 30 % de l'excursion
CAP_USDT = 50.0
CAP_PX   = CAP_USDT / QTY
H_WIN    = 7200           # 2h
SLOT     = 300            # slot d'entrée toutes les 5 min
BOOT_MIN = 90             # porte bootstrap au démarrage de chaque segment
K_SEISM  = 3.0            # seuil sismique k×médiane (A1/R30, GELÉ — aucun tuning ici)
SEISM_WIN = 120           # fenêtre glissante de la médiane (120 min, convention essai)

SEGMENTS = [  # (nom, début ISO UTC, fin ISO UTC) — découpe des redémarrages réels
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
    """1m BTCUSDT publiques, 1500/call, causal : seulement le passé."""
    out, cur = [], t0 * 1000
    while cur < t1 * 1000:
        u = f"{URL}?symbol=BTCUSDT&interval=1m&startTime={cur}&limit=1500"
        with urllib.request.urlopen(u, timeout=20) as r:
            batch = json.loads(r.read().decode())
        if not batch: break
        for k in batch:
            out.append({"t": int(k[0]) // 1000, "o": float(k[1]), "h": float(k[2]),
                        "l": float(k[3]), "c": float(k[4])})
        cur = int(batch[-1][0]) + 60000
        if len(batch) < 1500: break
    out.sort(key=lambda r: r["t"])
    return out

def load_klines(path):
    rows = []
    with open(path) as f:
        rd = csv.DictReader(f)
        for r in rd:
            rows.append({"t": int(r["open_time"]) // 1000, "o": float(r["open"]),
                         "h": float(r["high"]), "l": float(r["low"]), "c": float(r["close"])})
    rows.sort(key=lambda r: r["t"])
    return rows

def simulate(kl, t_start, t_end, mode):
    """Replay d'un segment. mode='BASE' (entrée slot×H=1) ou 'K3' (slot×H=1×sismique).
    Streams ALPHA (LONG) et BETA (SHORT) simulés séparément comme le shadow."""
    kls = [r for r in kl if t_start <= r["t"] < t_end]
    if len(kls) < 130: return None
    amps = [r["h"] - r["l"] for r in kls]
    boot_deadline = kls[0]["t"] + BOOT_MIN * 60
    stats = {"ALPHA": None, "BETA": None}

    for name, side in (("ALPHA", 1), ("BETA", -1)):
        virtual = []            # (ts_clôture, brut) pour le gate H
        trades = []             # nets
        pos = None
        for i in range(1, len(kls)):
            r, r_prev = kls[i], kls[i - 1]
            t = r["t"]

            # ---- 1. gestion position (ordre du shadow : trailing puis cap ; h_gate_off aux bornes 5-min)
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

            # ---- 2. slot 5-min : entrée à l'open de la barre SUIVANTE si H=1 (ou bootstrap) [+ sismique si K3]
            if pos is None and r_prev["t"] % SLOT == 0:
                ts_check = r_prev["t"] + 59          # H évalué à la clôture du slot (causal)
                h_sum = sum(g for tt, g in virtual if ts_check - H_WIN < tt < ts_check)
                forced = (r_prev["t"] < boot_deadline)
                if h_sum > 0 or forced:
                    ok = True
                    if mode == "K3":
                        lo = max(0, i - 1 - SEISM_WIN)
                        win = amps[lo:i - 1]
                        med = statistics.median(win) if win else 1e-9
                        ok = amps[i - 1] > K_SEISM * med          # sismique sur la DERNIÈRE minute fermée
                    if ok:
                        pos = {"entry": r["o"], "ext": r["o"], "armed": False, "ts": t,
                               "boot": forced and h_sum <= 0}

        # positions flottantes en fin de segment : clôture forcée au dernier close (marquée)
        if pos is not None:
            last = kls[-1]
            gross = (last["c"] - pos["entry"]) * QTY * side
            trades.append({"net": gross - FEE, "gross": gross, "reason": "fin_segment"})

        n_full = sum(1 for x in trades if x["reason"] != "fin_segment")
        nets = [x["net"] for x in trades]
        hours = (t_end - t_start) / 3600
        stats[name] = {
            "n": n_full, "n_h": n_full / hours if hours else 0,
            "gross": sum(x["gross"] for x in trades),
            "net": sum(nets), "med": statistics.median(nets) if nets else 0.0,
            "worst": min(nets) if nets else 0.0,
            "gateoff": sum(1 for x in trades if x["reason"] == "h_gate_off"),
        }
    return stats

def line(tag, st, hours):
    if st is None: return f"  {tag:<10} : —"
    a, b = st["ALPHA"], st["BETA"]
    n, net = a["n"] + b["n"], a["net"] + b["net"]
    return (f"  {tag:<10} : {n:3d} trades ({n/hours:4.1f}/h) | brut {a['gross']+b['gross']:+8.2f} "
            f"| net {net:+8.2f} | médian {(a['med']+b['med'])/2:+6.2f} | gateoff {a['gateoff']+b['gateoff']} "
            f"| pire {min(a['worst'], b['worst']):+7.2f}")

def main():
    print("=" * 82)
    print("REPLAY ENTRÉE K=3 — BASE (slot×H=1, moteur gelé) vs K3 (slot×H=1×sismique k=3)")
    print(f"QTY {QTY} BTC · frais {FEE} $/trade · trailing {RET*100:.0f}% · cap +{CAP_USDT:.0f} $ · H 2h · k={K_SEISM}×médiane 120min (GELÉ)")
    print("=" * 82)

    print("\n[1] Récupération klines 1m publiques (02/09 17:00 → maintenant)...")
    t0, t1 = iso("2026-09-02T17:00:00Z"), int(datetime.now(timezone.utc).timestamp())
    kl_live = fetch_klines(t0, t1)
    print(f"    {len(kl_live):,} barres 1m récupérées (source publique, zéro clé).")

    print("\n[2] SEGMENTS SHADOW RÉELS (bootstrap 90 min par segment, comme le moteur)")
    tot = {"BASE": 0.0, "K3": 0.0}; ntot = {"BASE": 0, "K3": 0}
    for name, s, e in SEGMENTS:
        t_s, t_e = iso(s), iso(e)
        hours = (t_e - t_s) / 3600
        base = simulate(kl_live, t_s, t_e, "BASE")
        k3 = simulate(kl_live, t_s, t_e, "K3")
        print(f"\n  ### {name} ({hours:.1f} h)")
        print(line("BASE", base, hours)); print(line("K3", k3, hours))
        if base and k3:
            nb, nk = base["ALPHA"]["n"] + base["BETA"]["n"], k3["ALPHA"]["n"] + k3["BETA"]["n"]
            tot["BASE"] += base["ALPHA"]["net"] + base["BETA"]["net"]
            tot["K3"] += k3["ALPHA"]["net"] + k3["BETA"]["net"]
            ntot["BASE"] += nb; ntot["K3"] += nk
            print(f"    → écart net K3−BASE : {(k3['ALPHA']['net']+k3['BETA']['net'])-(base['ALPHA']['net']+base['BETA']['net']):+.2f} $ "
                  f"| péage évité : {FEE*(nb-nk):.2f} $ ({nb}→{nk} trades)")
    print(f"\n  TOTAL segments réels : BASE {tot['BASE']:+.2f} $ ({ntot['BASE']} trades) "
          f"| K3 {tot['K3']:+.2f} $ ({ntot['K3']} trades) | écart {tot['K3']-tot['BASE']:+.2f} $")

    print("\n[3] LES 4 FENÊTRES HISTORIQUES — l'essai du candidat (k gelé, un seul passage)")
    print("     (réchauffage 120 min + bootstrap 90 min, convention essai 3 bras)")
    ftot = {"BASE": 0.0, "K3": 0.0}
    for fen, path in FENETRES.items():
        kl = load_klines(path)
        t_s, t_e = kl[130]["t"], kl[-1]["t"] + 60
        hours = (t_e - t_s) / 3600
        base = simulate(kl, t_s, t_e, "BASE")
        k3 = simulate(kl, t_s, t_e, "K3")
        print(f"\n  ### {fen} ({hours:.0f} h, {len(kl)} barres)")
        print(line("BASE", base, hours)); print(line("K3", k3, hours))
        if base and k3:
            ftot["BASE"] += base["ALPHA"]["net"] + base["BETA"]["net"]
            ftot["K3"] += k3["ALPHA"]["net"] + k3["BETA"]["net"]
    print(f"\n  TOTAL 4 fenêtres : BASE {ftot['BASE']:+.2f} $ | K3 {ftot['K3']:+.2f} $ | écart {ftot['K3']-ftot['BASE']:+.2f} $")
    print("\n(Règle d'or : le candidat ne vit que s'il améliore TOUTES les époques — sinon il meurt,")
    print(" et aucun paramètre n'a été touché ici. Confrontation famille avant toute décision.)")

if __name__ == "__main__":
    main()
