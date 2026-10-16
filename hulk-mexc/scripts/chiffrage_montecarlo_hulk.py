#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_montecarlo_hulk.py — GO montecarlo 16/10/2026 (Christophe : « go »).

QUESTION : les trois réglages de taille sont au jugement (FRAC 0,5 · MAX_MULT 3 ·
GLOBAL_CAP 600). Avec CET edge et CES coûts, quelle taille survit, laquelle se ruine ?
MÉTHODE (doctrine S9, même que monte_carlo_ace.py) : on mélange l'ordre des 337
sorties RÉELLES du run 10/10 (NETTES de coûts : pnl − coût moyen/exit, mesuré
18,80 $ au journal) et on rejoue la courbe d'équité avec la VRAIE règle de mise :
  mise = min(max(base + FRAC×max(0,cumPnl), base×0,5), base×MULT)   (miroir fidèle
  de current_notional : plancher 0,5×, plafond MULT× — même formule, mêmes bornes)
  gain_monde = outcome_net × (mise / 30)   (mises live ≈ base 30 $)
Ruine = drawdown ≥ 25 % (S9). Grille FRAC × MULT × 2 moitiés chronologiques :
on ne câble que le gagnant des DEUX moitiés.
Le CAP GLOBAL (600) n'est PAS calibré ici : contrainte simultanée (22 poches),
pas séquentielle — il reste au jugement déclaré.
Lecture seule, 0 ordre, 0 €.
"""
from __future__ import annotations

import csv
import random
import statistics
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
JOURNAL = RACINE / "runs" / "PAPER_V1_20261010_074520.csv"
BASE = 30.0
C0 = 660.0            # enveloppe 22 paires × 30 $
RUIN_DD = 0.25        # doctrine S9
SIMS = 5000
SEED = 42
FRACS = (0.0, 0.25, 0.5, 0.75, 1.0)
MULTS = (2.0, 3.0, 4.0)


def charger():
    outs = []
    cout_exit = cout_buy = 0.0
    nbuy = 0
    for r in csv.DictReader(open(JOURNAL, encoding="utf-8")):
        ev = r.get("event")
        if ev in ("SELL", "SELL_PARTIAL", "BAG_SELL"):
            try:
                outs.append(float(r.get("pnl_usdt") or 0))
                cout_exit += float(r.get("cout_estime_usdt") or 0)
            except (TypeError, ValueError):
                pass
        elif ev == "BUY":
            nbuy += 1
            try:
                cout_buy += float(r.get("cout_estime_usdt") or 0)
            except (TypeError, ValueError):
                pass
    flat = (cout_exit + cout_buy) / max(1, len(outs))
    return [x - flat for x in outs], flat


def simuler(outs, frac, mult, seed):
    rng = random.Random(seed)
    ruins = 0
    dds, ends, greens = [], [], 0
    for _ in range(SIMS):
        sh = outs[:]
        rng.shuffle(sh)
        eq, peak, cum = C0, C0, 0.0
        max_dd = 0.0
        for x in sh:
            mise = min(max(BASE + frac * max(0.0, cum), BASE * 0.5), BASE * mult)
            g = x * (mise / BASE)
            eq += g
            cum += g
            peak = max(peak, eq)
            dd = (peak - eq) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)
        dds.append(max_dd)
        ends.append(eq - C0)
        if max_dd >= RUIN_DD:
            ruins += 1
        if eq > C0:
            greens += 1
    dds.sort()
    ends.sort()

    def pct(a, p):
        return a[min(len(a) - 1, int(p * len(a)))]

    return {"ruin": ruins / SIMS, "medDD": pct(dds, 0.50), "p95DD": pct(dds, 0.95),
            "medEnd": pct(ends, 0.50), "green": greens / SIMS}


def main():
    outs, flat = charger()
    print(f"MONTE CARLO HULK — {len(outs)} sorties réelles NETTES (coût/exit {flat:.4f} $) · "
          f"{SIMS} mondes · C0 {C0:.0f} $ · ruine DD≥25 % (S9) · graine {SEED}")
    print(f"Edge brut : moyen {statistics.mean([x + flat for x in outs]):+.4f} $ · "
          f"net {statistics.mean(outs):+.4f} $ · winrate "
          f"{100 * sum(1 for x in outs if x > 0) / len(outs):.1f} %")
    h = len(outs) // 2
    for nom, sub in (("FULL", outs), ("h1", outs[:h]), ("h2", outs[h:])):
        print(f"── {nom} ({len(sub)} trades)")
        for mult in MULTS:
            lig = []
            for frac in FRACS:
                m = simuler(sub, frac, mult, SEED)
                lig.append(f"F{frac:g}: ruine {m['ruin'] * 100:4.1f}% DDmed {m['medDD'] * 100:4.1f}% "
                           f"finmed {m['medEnd']:+7.2f}$ vert {m['green'] * 100:4.1f}%")
            print(f"  ×{mult:g} : " + " · ".join(lig))
    print("LIMITES (R8) : sorties mélangées (corrélations intra-position cassées, comme ACE) · "
          "mises live ≈ base (mults murs/fusibles ignorés) · CAP global non modélisé · "
          "1 run, 1 régime · ÉTUDE, pas preuve hors échantillon.")


if __name__ == "__main__":
    main()
