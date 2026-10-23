#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_seuils_tempete.py — MESURER le gate seuils-par-paire AVANT câblage (règle #8).

Question : bloquer les ENTREES quand dd (creux depuis pic) >= seuil_interrupt
(2x range_med_7j, seuils_paires_live.json) évite-t-il de mauvais trades
sans tuer l'amplitude (le joker + compounding) ?

Méthode (replay_cache 45j, bougies 1h, walk-forward strict) :
- pic15 = plus-haut des 360 dernières clôtures (== peak15 live du moteur) ;
- pic30 = plus-haut des 720 dernières clôtures (spec POINT_GO « pic 30j ») ;
- storm15/storm30 = dd >= seuil_interrupt de LA paire ;
- métriques par paire : % barres en storm, rendement forward +24h/+7j des
  barres storm vs non-storm, chevauchement avec PLANCHER (25 %).
Sortie : table + verdict par paire (CÂBLER / TROP FREQ / INUTILE).
Lecture seule, 0 ordre, 0 écriture moteur.
"""
import json
import statistics as st
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "runs" / "replay_cache"
SEUILS = RACINE / "runs" / "seuils_paires_live.json"
PLANCHER_DD = 25.0

seuils = json.load(open(SEUILS, encoding="utf-8"))["paires"]


def fwd_ret(closes, i, h):
    if i + h >= len(closes) or closes[i] <= 0:
        return None
    return (closes[i + h] - closes[i]) / closes[i] * 100.0


print(f"{'paire':12s} {'seuil':>6s} {'storm15':>7s} {'storm30':>7s} "
      f"{'fwd24h storm':>12s} {'fwd24h calm':>11s} {'fwd7j storm':>11s} {'fwd7j calm':>10s} verdict")
for pair in sorted(seuils):
    f = CACHE / f"{pair}_1h_45j.json"
    if not f.exists():
        print(f"{pair:12s} PAS DE CACHE -> SKIP (fail-open au runtime)")
        continue
    kl = json.load(open(f, encoding="utf-8"))
    closes = [float(b["c"]) for b in kl]
    seuil = float(seuils[pair]["seuil_interrupt_pct"])
    n = len(closes)
    s15 = s30 = 0
    r24_s, r24_c, r7_s, r7_c = [], [], [], []
    for i in range(720, n):
        pic15 = max(closes[i - 360:i])
        pic30 = max(closes[i - 720:i])
        if pic15 <= 0 or pic30 <= 0:
            continue
        dd15 = (1 - closes[i] / pic15) * 100.0
        dd30 = (1 - closes[i] / pic30) * 100.0
        in15 = dd15 >= seuil
        in30 = dd30 >= seuil
        s15 += in15
        s30 += in30
        r24 = fwd_ret(closes, i, 24)
        r7 = fwd_ret(closes, i, 168)
        (r24_s if in15 else r24_c).append(r24) if r24 is not None else None
        (r7_s if in15 else r7_c).append(r7) if r7 is not None else None
    tot = max(1, n - 720)
    f15, f30 = 100.0 * s15 / tot, 100.0 * s30 / tot
    m = lambda xs: round(st.median(xs), 2) if xs else float("nan")
    m24s, m24c, m7s, m7c = m(r24_s), m(r24_c), m(r7_s), m(r7_c)
    # Verdict : le gate a un edge si storm-forward < calm-forward (on évite du mauvais),
    # et il ne tue pas l'amplitude si storm < 15 % du temps.
    edge24 = (m24c - m24s) if r24_s and r24_c else float("nan")
    if f15 > 15.0:
        verdict = "TROP FREQ (>15% temps -> tue amplitude)"
    elif r24_s and r24_c and edge24 > 0.5:
        verdict = "CABLER (storm fwd pire de %.1fpp/24h)" % edge24
    elif f15 < 0.5:
        verdict = "INUTILE (jamais en storm sur 45j)"
    else:
        verdict = "NEUTRE (rare, edge faible -> cabler ss risque)"
    print(f"{pair:12s} {seuil:6.2f} {f15:6.2f}% {f30:6.2f}% "
          f"{m24s:>7.2f}/{len(r24_s):<4d} {m24c:>7.2f}/{len(r24_c):<4d} "
          f"{m7s:>7.2f} {m7c:>7.2f}  {verdict}")
