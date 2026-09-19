#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test B — le signal (tension/confiance) prédit-il les gains ?
Période au choix (défaut 2026-08-09 → 2026-08-20).
Reconstruit le signal d'entrée de chaque trade FILLED depuis la dernière ligne
SKIP (conf=/tension=) avant l'entrée — c'est ce que le moteur voyait à l'instant T.
"""
import csv, re, sys, bisect
from datetime import datetime

CSV = "/Users/christophe/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"
DEBUT = sys.argv[1] if len(sys.argv) > 1 else "2026-08-09"
FIN = sys.argv[2] if len(sys.argv) > 2 else "2026-08-20"


def epoch(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


rows = list(csv.DictReader(open(CSV)))
sel = [r for r in rows if DEBUT <= (r["ts"] or "")[:10] <= FIN]

# Séries de signal (SKIP avec conf=/tension=) triées par temps
signaux = []  # (ts_epoch, conf, tension)
for r in sel:
    msg = r.get("msg") or ""
    if "conf=" not in msg and "tension=" not in msg:
        continue
    t = epoch(r["ts"])
    if t is None:
        continue
    def fld(k):
        m = re.search(k + r"=([0-9.]+)", msg)
        return float(m.group(1)) if m else None
    conf, tens = fld("conf"), fld("tension")
    if conf is None and tens is None:
        continue
    signaux.append((t, conf if conf is not None else 0.0,
                    tens if tens is not None else 0.0))
signaux.sort()
tsig = [s[0] for s in signaux]

trades = [r for r in sel if r.get("pnl") not in (None, "") and float(r["pnl"] or 0) != 0]
print(f"=== TEST B — période {DEBUT} → {FIN} ===")
print(f"trades fermés (pnl≠0): {len(trades)} | lignes signal: {len(signaux)}")

# Pour chaque trade : dernier signal ≤ entrée, à moins de 60 s
couples = []  # (signal, pnl)
for r in trades:
    t = epoch(r["ts"])
    if t is None:
        continue
    i = bisect.bisect_right(tsig, t) - 1
    if i < 0 or (t - tsig[i]) > 60:
        continue
    couples.append((signaux[i][1], signaux[i][2], float(r["pnl"])))

if len(couples) < 50:
    print("échantillon trop petit:", len(couples))
    sys.exit(0)

def quartiles(vals, pnl, nom):
    qs = sorted(vals)
    n = len(qs)
    bornes = [qs[int(n * f)] for f in (0.25, 0.5, 0.75)]
    print(f"\n--- {nom} (par quartile) ---")
    print(f"{'Q':<4}{'borne':<10}{'n':<6}{'win%':<8}{'pnl moyen':<12}{'pnl total':<10}")
    for k, (lo, hi) in enumerate([(0, bornes[0]), (bornes[0], bornes[1]),
                                  (bornes[1], bornes[2]), (bornes[2], 1e18)]):
        idx = [i for i, v in enumerate(vals) if lo <= v < hi]
        if not idx:
            continue
        ps = [pnl[i] for i in idx]
        wins = [p for p in ps if p > 0]
        print(f"Q{k+1:<3}{lo:.4f}-{hi:.4f}  {len(ps):<6}"
              f"{100*len(wins)/len(ps):<8.1f}{sum(ps)/len(ps):<12.3f}{sum(ps):<10.2f}")

conf_vals, tens_vals, pnls = zip(*couples)
quartiles(conf_vals, pnls, "CONFIANCE (conf)")
quartiles(tens_vals, pnls, "TENSION")

# Corrélation simple
import statistics
def corr(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a, b in zip(x, y))
    den = (sum((a-mx)**2 for a in x) * sum((b-my)**2 for b in y)) ** 0.5
    return num/den if den else 0.0

print("\ncorrélation conf vs pnl : %.3f" % corr(list(conf_vals), list(pnls)))
print("corrélation tension vs pnl : %.3f" % corr(list(tens_vals), list(pnls)))
