#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT DES PIRES TRADES — vrai marché ou artefact de données ? (lecture seule)
Contexte (décision famille 07/09) : les fenêtres de test contiennent des interruptions/
redémarrages ; les grosses pertes peuvent être des TROUS DE DONNÉES et non du marché.
On audite donc les pires trades de chaque fenêtre/segment.

Règles FIGÉES avant l'analyse :
  • PERTURBATION  : minutes manquantes pendant la détention ≥ 20 % de la durée,
                    OU un trou unique ≥ 3 min à l'intérieur,
                    OU entrée collée à un trou (trou ≥ 3 min dans les 5 min avant).
  • MARCHE        : sinon (données continues → la perte est réelle).
  • Croix régime  : ratio = vol60(entrée) / médiane24h ; bloqué_par_régime si ratio > 1.5
                    (même règle figée que replay_regime.py, mult 1.5 a priori).
Mécanique moteur = BASE gelée (slot 5-min × gate H 2h, trailing 30 %, breakeven,
cap +50 $, frais 1,76 $, QTY 0,10593) — identique aux replays k=3 et régime.
"""
import csv, statistics, urllib.request, json
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = f"{ROOT}/runs"
URL = "https://fapi.binance.com/fapi/v1/klines"

QTY, FEE, RET = 0.10593, 1.760, 0.30
CAP_USDT = 50.0; CAP_PX = CAP_USDT / QTY
H_WIN, SLOT, BOOT_MIN = 7200, 300, 90
REG_MULT, VOL_WIN, BASE_WIN = 1.5, 60, 24
TOP_N = 5

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

def hms(t):
    return datetime.fromtimestamp(t, tz=timezone.utc).strftime("%m/%d %H:%M")

def fetch_klines(t0, t1):
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

def gap_stats(kls, t_s, t_e):
    """Trous de données dans la fenêtre : liste des (début, minutes manquantes)."""
    gaps, times = [], [r["t"] for r in kls if t_s <= r["t"] < t_e]
    for a, b in zip(times, times[1:]):
        d = b - a
        if d > 60:
            gaps.append((a, (d // 60) - 1))
    return gaps, times

def simulate_base(kls_all, t_start, t_end):
    """Replay BASE gelé. vol60/base calculés sur kls_all (pré-fenêtre incluse) ;
    les trades ne sont simulés que dans [t_start, t_end). Retourne (trades, kls_fenêtre)."""
    idx_map = [i for i, r in enumerate(kls_all) if t_start <= r["t"] < t_end]
    kls = [kls_all[i] for i in idx_map]
    if len(kls) < 200: return None, None
    n = len(kls_all)
    vol60 = [0.0] * n
    for i in range(n):
        lo = max(0, i - VOL_WIN)
        vol60[i] = sum((kls_all[j]["h"] - kls_all[j]["l"]) / kls_all[j]["c"] for j in range(lo, i))
    boot_deadline = t_start + BOOT_MIN * 60   # ancré à la fenêtre, pas au pré-data
    all_trades = []
    for name, side in (("ALPHA", 1), ("BETA", -1)):
        virtual, trades, pos = [], [], None
        for j in range(1, len(kls)):
            gi = idx_map[j]          # index global (pour vol60)
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
                    trades.append({"side": name, "entry_ts": pos["ts"], "exit_ts": t,
                                   "entry_px": entry, "exit_px": exit_px, "gross": gross,
                                   "net": gross - FEE, "reason": reason, "j_entry": pos["j"]})
                    pos = None
                else:
                    pos["ext"], pos["armed"] = ext, armed
            if pos is None and r_prev["t"] % SLOT == 0:
                ts_check = r_prev["t"] + 59
                h_sum = sum(g for tt, g in virtual if ts_check - H_WIN < tt < ts_check)
                forced = (r_prev["t"] < boot_deadline)
                if h_sum > 0 or forced:
                    pos = {"entry": r["o"], "ext": r["o"], "armed": False, "ts": t, "j": j}
        if pos is not None:
            last = kls[-1]
            gross = (last["c"] - pos["entry"]) * QTY * side
            trades.append({"side": name, "entry_ts": pos["ts"], "exit_ts": last["t"],
                           "entry_px": pos["entry"], "exit_px": last["c"], "gross": gross,
                           "net": gross - FEE, "reason": "fin_segment", "j_entry": pos["j"]})
        all_trades.extend(trades)
    # ratio de régime à l'entrée de chaque trade
    for tr in all_trades:
        gi = idx_map[tr["j_entry"]]   # index global de la barre d'entrée
        span = BASE_WIN * VOL_WIN
        lo = max(0, gi - 1 - span)
        hourly = [vol60[x] for x in range(lo, gi - 1, VOL_WIN)]
        base = statistics.median(hourly) if len(hourly) >= 12 else None
        tr["ratio"] = (vol60[gi - 1] / base) if (base and base > 0) else None
    return all_trades, kls

def classify(tr, times_set, kls):
    """PERTURBATION vs MARCHE — règles figées (voir docstring)."""
    e, x = tr["entry_ts"], tr["exit_ts"]
    dur_min = max(1, (x - e) // 60)
    present = sum(1 for tt in times_set if e <= tt <= x)
    missing = max(0, (dur_min + 1) - present)
    # plus grand trou interne
    inside = [t for t in times_set if e <= t <= x]
    biggest_inside = 0
    for a, b in zip(inside, inside[1:]):
        if b - a > 60: biggest_inside = max(biggest_inside, (b - a) // 60 - 1)
    # trou juste avant l'entrée ?
    idx = tr["j_entry"]
    pre_hole = 0
    if idx >= 2 and kls[idx - 1]["t"] - kls[idx - 2]["t"] > 60:
        pre_hole = (kls[idx - 1]["t"] - kls[idx - 2]["t"]) // 60 - 1
    if missing >= 0.20 * dur_min or biggest_inside >= 3 or pre_hole >= 3:
        why = []
        if missing >= 0.20 * dur_min: why.append(f"{missing}/{dur_min}min manquantes")
        if biggest_inside >= 3: why.append(f"trou interne {biggest_inside}min")
        if pre_hole >= 3: why.append(f"trou {pre_hole}min avant entrée")
        return "PERTURBATION", "; ".join(why)
    return "MARCHE", ""

def report(tag, kls, t_s, t_e):
    gaps, times = gap_stats(kls, t_s, t_e)
    times_set = set(times)
    miss_total = sum(m for _, m in gaps)
    span_min = (t_e - t_s) // 60
    trades, kl_win = simulate_base(kls, t_s, t_e)
    if trades is None:
        print(f"\n### {tag} : pas assez de données"); return
    hours = (t_e - t_s) / 3600
    net = sum(t["net"] for t in trades)
    print(f"\n### {tag} ({hours:.1f} h · {len(kl_win):,} barres · net BASE {net:+.2f} $)")
    if gaps:
        big = max(gaps, key=lambda g: g[1])
        print(f"  Données : {len(gaps)} trous, {miss_total} min manquantes "
              f"({100*miss_total/span_min:.1f} %) · pire trou {big[1]} min à {hms(big[0])}")
    else:
        print(f"  Données : continues (0 trou)")
    worst = sorted(trades, key=lambda t: t["net"])[:TOP_N]
    print(f"  {'net':>8}  {'entrée':>12}  {'sortie':>12}  {'durée':>6}  raison          régime   verdict")
    n_pert, pert_net, blocked_net = 0, 0.0, 0.0
    for tr in worst:
        dur = (tr["exit_ts"] - tr["entry_ts"]) // 60
        verdict, why = classify(tr, times_set, kl_win)
        ratio_s = f"{tr['ratio']:5.2f}x" if tr["ratio"] else "   — "
        blocked = tr["ratio"] is not None and tr["ratio"] > REG_MULT
        if blocked: blocked_net += tr["net"]
        if verdict == "PERTURBATION":
            n_pert += 1; pert_net += tr["net"]
            verdict_s = f"PERTURBATION ({why})"
        else:
            verdict_s = "MARCHE"
        b = " [bloqué par régime]" if blocked else ""
        print(f"  {tr['net']:+8.2f}  {hms(tr['entry_ts']):>12}  {hms(tr['exit_ts']):>12}  {dur:4d}m  "
              f"{tr['reason']:<14}  {ratio_s}  {verdict_s}{b}")
    print(f"  → pires {TOP_N} : {n_pert} perturbation(s) ({pert_net:+.2f} $) · "
          f"{TOP_N-n_pert} vrai marché · le régime en aurait bloqué {sum(1 for t in worst if t['ratio'] and t['ratio']>REG_MULT)} "
          f"({blocked_net:+.2f} $)")

def main():
    print("=" * 96)
    print("AUDIT PIRES TRADES — vrai marché vs trou de données (règles figées : trou≥3min interne,")
    print("≥20% manquant en détention, ou trou≥3min <5min avant entrée · régime : vol60 > 1.5×médiane24h)")
    print("=" * 96)

    # pré-data : 25 h avant le début de chaque fenêtre (pour la base 24 h du ratio régime)
    t0, t1 = iso("2026-09-01T16:00:00Z"), iso("2026-09-07T07:00:00Z")
    kl_live = fetch_klines(t0, t1)
    print(f"\n[SEGMENTS RÉELS SHADOW] {len(kl_live):,} barres 1m chargées (pré-data depuis 09/01 16:00Z)")
    for name, s, e in SEGMENTS:
        report(f"{name}", kl_live, iso(s), iso(e))

    print("\n[4 FENÊTRES HISTORIQUES]")
    for fen, path in FENETRES.items():
        kl = load_klines(path)
        t_s, t_e = kl[130]["t"], kl[-1]["t"] + 60   # réchauffage 130 min (convention replays)
        try:
            pre = fetch_klines(kl[0]["t"] - 25 * 3600, kl[0]["t"])
            kl_all = pre + kl
            print(f"  ({fen}: +{len(pre)} barres pré-fenêtre pour la base 24h)")
        except Exception as ex:
            kl_all = kl
            print(f"  ({fen}: pré-data indisponible — {ex})")
        report(f"{fen}", kl_all, t_s, t_e)

if __name__ == "__main__":
    main()
