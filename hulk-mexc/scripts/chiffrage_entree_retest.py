#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_entree_retest.py — §28 (28/10/2026, ORDRE Christophe : attaquer le point d'entrée).
============================================================================================
Constat mesuré (journal 366 bookings) : les entrées GBAG au signal (cassure >
SMA24 + plus-haut 24 + SMA240) achètent le haut — 61 % plongent -6 %+ sous 7 j,
moyenne -5,76 % au creux 7 j. Le compounding amplifie l'entrée, il ne la corrige
pas (§26 : EDEL).

Ce replay oppose, sur les VRAIES entrées GBAG du journal (rejeu pur, 0 ordre) :
  A (actuel) : achat au signal, sortie à +30 j.
  B (retest) : ordre limite au prix du signal, valable 5 j — servi si le marché
     revient (le creux), sinon PAS d'entrée (on laisse passer).
Métrique : rendement à 30 j, taux de service, n. Limites R8 : prix = marks du
journal (pas des fills), n petit (~18), sans frais — directionnel, pas un PnL.
Un câblage éventuel exigera le replay sur klines 1 h + frais + GO (protocole).
"""
from __future__ import annotations

import csv
import glob
import os
from datetime import datetime, timedelta

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def main() -> int:
    csvs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)
    rows = list(csv.DictReader(open(csvs[-1], encoding="utf-8", errors="replace")))
    px: dict[str, list] = {}
    for r in rows:
        p = _f(r.get("price"))
        if p > 0:
            px.setdefault(r["pair"], []).append((r["ts"], p))

    def after(pair, ts, h):
        t0 = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return [(t, p) for t, p in px.get(pair, [])
                if t0 < datetime.fromisoformat(t.replace("Z", "+00:00")) <= t0 + timedelta(hours=h)]

    n = na = 0
    tot_r = tot_b = 0.0
    for r in rows:
        if "gbag_entree_sgn" not in (r.get("reason") or "") or r["event"] != "BUY":
            continue
        e = _f(r.get("price"))
        if e <= 0:
            continue
        w5, w30 = after(r["pair"], r["ts"], 120), after(r["pair"], r["ts"], 720)
        if not w5 or not w30:
            continue
        px30 = w30[-1][1]
        rr = (px30 / e - 1) * 100
        n += 1
        tot_r += rr
        if min(p for _, p in w5) <= e:  # le marché revient au prix du signal : servi
            na += 1
            tot_b += (px30 / e - 1) * 100
    print("=== REPLAY entrée retest vs breakout (§28) ===")
    print(f"journal : {os.path.basename(csvs[-1])}")
    print(f"entrées GBAG testables : {n}")
    print(f"  A breakout (actuel) : {tot_r / n:+.2f} % à 30 j en moyenne")
    if na:
        print(f"  B retest (limite 5 j) : servi {na}/{n} ({100 * na / n:.0f} %), "
              f"{tot_b / na:+.2f} % à 30 j en moyenne")
        print(f"  verdict : {'retest MEILLEUR' if tot_b / na > tot_r / n else 'breakout MEILLEUR'} "
              f"(Δ {tot_b / na - tot_r / n:+.2f} pts, n={n} — R8 : petit échantillon)")
    else:
        print("  B retest : jamais servi — le marché ne revient pas, on ne trade pas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
