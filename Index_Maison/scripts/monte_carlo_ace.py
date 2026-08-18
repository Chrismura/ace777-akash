#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MONTE CARLO ACE — Test de résistance du champion (lecture seule)
================================================================
Source : signets X (Lummox/antpalkin = méthode, 0x_Punisher = leçon P(fill))
Doctrine : S9 « Monte Carlo sur l'ordre des trades → Max DD / ruine »
(brief_ia_sniff + audit_survie_frais)

Ce que ça fait :
  1. Lit les trades RÉELS remplis d'ACE (BETA + ALPHA) depuis runs/*.csv
  2. Mélange l'ordre des trades N fois (les marchés n'arrivent jamais 2× pareil)
  3. Recalcule la courbe d'équité à chaque mélange → distribution de :
       - PnL final
       - Max drawdown (le pire creux)
       - Probabilité de ruine (drawdown < -25 % du capital, doctrine S9)
       - Probabilité de finir en vert
  4. Applique la leçon 0x_Punisher : « Real EV = EV modélisé × P(fill) »
       - P(fill) réel = fills / cycles (mesuré dans le CSV)
       - Montre le PnL par cycle RÉEL vs PnL par trade (le rêve vs la réalité)

100 % lecture seule. Rien ne se supprime, rien ne touche au moteur.
Sortie : rapport markdown dans Index_Maison/ + résumé console.

Usage :
  python3 Index_Maison/scripts/monte_carlo_ace.py [--sims 5000] [--capital 20.0]
"""

import argparse
import csv
import json
import random
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "runs"
OUT_DIR = ROOT / "Index_Maison"

CSV_UNITS = [
    ("BETA", RUNS / "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"),
    ("ALPHA", RUNS / "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"),
]

RUIN_DD = 0.25  # doctrine S9 : drawdown < -25 % = trop risqué


def lire_trades(path, depuis=None):
    """Lit un CSV de run. Retourne (fills, cycles, skips) avec les pnl des fills.

    depuis : date ISO 'YYYY-MM-DD' — ne garde que les lignes à partir de ce jour
    (pour isoler une période propre, ex: nouvelle base scellée).
    """
    fills, skips, cycles = [], 0, 0
    if not path.exists():
        return fills, 0, 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = (row.get("ts") or "").strip()
            if depuis and ts[:10] < depuis:
                continue  # hors fenêtre → ignoré (ni cycle ni fill)
            status = (row.get("status") or "").strip().upper()
            cycles += 1
            if status == "SKIPPED" or (row.get("side") or "").strip().upper() == "SKIP":
                skips += 1
                continue
            if status == "FILLED":
                try:
                    pnl = float(row["pnl"])
                except (ValueError, KeyError, TypeError):
                    continue
                fills.append(pnl)
    return fills, cycles, skips


def simuler(fills, n_sims, seed, capital):
    """Monte Carlo : mélange l'ordre des trades N fois, retourne les métriques."""
    rng = random.Random(seed)
    n = len(fills)
    nets, max_dds, ruins, greens = [], [], 0, 0

    for _ in range(n_sims):
        shuffled = fills[:]
        rng.shuffle(shuffled)
        eq = capital
        peak = capital
        max_dd = 0.0
        for pnl in shuffled:
            eq += pnl
            peak = max(peak, eq)
            dd = (peak - eq) / peak if peak > 0 else 0.0
            max_dd = max(max_dd, dd)
        nets.append(eq - capital)
        max_dds.append(max_dd)
        if max_dd >= RUIN_DD:
            ruins += 1
        if eq > capital:
            greens += 1

    nets.sort()
    max_dds.sort()

    def pct(arr, p):
        return arr[min(len(arr) - 1, int(p * len(arr)))]

    # NB : la somme finale est INVARIANTE (mélanger l'ordre ne change pas le total).
    # Ce qui varie d'un monde à l'autre, c'est le CHEMIN → le drawdown.
    return {
        "n_sims": n_sims,
        "sum_pnl": sum(fills),
        "median_dd": pct(max_dds, 0.50),
        "p95_dd": pct(max_dds, 0.95),    # pire creux probable (95e percentile)
        "worst_dd": max_dds[-1],         # pire creux observé sur tous les mondes
        "ruin_prob": ruins / n_sims,
        "green_prob": greens / n_sims,
        "win_rate": sum(1 for p in fills if p > 0) / n if n else 0.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sims", type=int, default=5000)
    ap.add_argument("--capital", type=float, default=20.0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--depuis", type=str, default=None,
                    help="ne garder que les trades à partir de cette date ISO (YYYY-MM-DD)")
    args = ap.parse_args()

    lines = []
    lines.append(f"# MONTE CARLO ACE — Test de résistance — {__import__('datetime').date.today()}")
    lines.append("")
    lines.append(f"**Méthode** : doctrine S9 + signets (Lummox/antpalkin = méthode, "
                 f"0x_Punisher = leçon P(fill)). Lecture seule, rien ne touche le moteur.")
    fenetre = f" · depuis {args.depuis}" if args.depuis else " · toutes les données"
    lines.append(f"**Paramètres** : {args.sims} simulations · capital ${args.capital:.2f} · "
                 f"seuil de ruine drawdown ≥ {RUIN_DD*100:.0f} % (S9) · graine {args.seed}{fenetre}")
    lines.append("")

    all_fills = []
    total_cycles = 0
    total_fills = 0
    total_skips = 0
    per_unit = {}

    for unit, path in CSV_UNITS:
        fills, cycles, skips = lire_trades(path, depuis=args.depuis)
        per_unit[unit] = {"fills": fills, "cycles": cycles, "skips": skips,
                          "p_fill": (fills and cycles) and len(fills) / cycles or 0.0}
        all_fills.extend(fills)
        total_cycles += cycles
        total_fills += len(fills)
        total_skips += skips

    # ---- 1. Le rêve vs la réalité (leçon 0x_Punisher) ----
    p_fill_total = total_fills / total_cycles if total_cycles else 0.0
    avg_pnl_fill = statistics.mean(all_fills) if all_fills else 0.0
    # Real EV par cycle = EV par trade × P(fill)  (signet 0x_Punisher)
    ev_par_cycle_reel = avg_pnl_fill * p_fill_total
    ev_par_trade = avg_pnl_fill

    lines.append("## 1. Le rêve vs la réalité (leçon 0x_Punisher)")
    lines.append("")
    lines.append("> *« Real EV = EV modélisé × P(fill). Un backtest qui suppose que tu es rempli "
                 "à chaque fois n'est pas un backtest, c'est un vœu pieux. »* — @0x_Punisher")
    lines.append("")
    lines.append("| Unité | Fills | Skips | Cycles | **P(fill) réel** | PnL moyen / trade | PnL moyen / cycle réel |")
    lines.append("|---|---|---|---|---|---|---|")
    for unit, d in per_unit.items():
        n = len(d["fills"])
        avg = statistics.mean(d["fills"]) if n else 0.0
        lines.append(f"| {unit} | {n} | {d['skips']} | {d['cycles']} | "
                     f"**{d['p_fill']*100:.2f} %** | {avg:+.4f} $ | {avg * d['p_fill']:+.4f} $ |")
    lines.append(f"| **TOTAL** | {total_fills} | {total_skips} | {total_cycles} | "
                 f"**{p_fill_total*100:.2f} %** | {ev_par_trade:+.4f} $ | **{ev_par_cycle_reel:+.4f} $** |")
    lines.append("")
    lines.append(f"**Lecture** : ACE n'est rempli qu'à **{p_fill_total*100:.1f} %** des cycles. "
                 f"Le PnL moyen par trade ({ev_par_trade:+.4f} $) n'est pas le vrai rendement : "
                 f"par cycle réel, c'est **{ev_par_cycle_reel:+.4f} $**.")
    lines.append("")

    # ---- 2. Monte Carlo global ----
    if all_fills:
        res = simuler(all_fills, args.sims, args.seed, args.capital)
        lines.append("## 2. Monte Carlo — {:,} chemins mélangés".format(args.sims))
        lines.append("")
        lines.append("> Les marchés n'arrivent jamais deux fois dans le même ordre. "
                     "On mélange l'ordre des trades réels et on regarde ce qui survit.")
        lines.append("")
        lines.append("| Métrique | Valeur | Lecture |")
        lines.append("|---|---|---|")
        lines.append(f"| Trades réels analysés | {len(all_fills)} | {res['win_rate']*100:.1f} % de trades gagnants |")
        lines.append(f"| Somme des PnL réels | {res['sum_pnl']:+.2f} $ | invariant : mélanger l'ordre ne change pas le total |")
        lines.append(f"| Max drawdown **médian** (50 % des mondes) | {res['median_dd']*100:.1f} % | le creux typique |")
        lines.append(f"| Max drawdown **pire cas** (5 % des mondes) | {res['p95_dd']*100:.1f} % | le creux rare |")
        lines.append(f"| Pire drawdown observé | {res['worst_dd']*100:.1f} % | le pire de tous les {args.sims} mondes |")
        lines.append(f"| **Probabilité de ruine** (DD ≥ {RUIN_DD*100:.0f} %) | **{res['ruin_prob']*100:.1f} %** | {res['ruin_prob']*100:.1f} % des {args.sims} mondes meurent |")
        lines.append(f"| Probabilité de finir en vert | {res['green_prob']*100:.1f} % | {res['green_prob']*100:.1f} % des mondes finissent + |")
        lines.append("")
        lines.append("## 3. Verdict")
        lines.append("")
        if res["ruin_prob"] < 0.01:
            verdict = "🟢 **RÉSISTANT** — la ruine est quasi impossible sur ces données réelles."
        elif res["ruin_prob"] < 0.05:
            verdict = "🟡 **FRAGILE** — la ruine arrive dans quelques mondes sur 100. À surveiller."
        else:
            verdict = "🔴 **À RISQUE** — la ruine est fréquente dans les mondes mélangés. Le champion dépend de l'ordre des trades."
        lines.append(f"{verdict}")
        lines.append("")
        if res["sum_pnl"] < 0:
            lines.append("⚠️ La somme des PnL réels est **négative** : le champion perd avec ses propres trades, même bien ordonnés.")
        else:
            lines.append(f"✅ La somme des PnL réels est **positive** ({res['sum_pnl']:+.2f} $) : le champion gagne dans l'ordre vécu. "
                         f"La question est la profondeur des creux en cours de route.")
        lines.append("")
        lines.append("## 4. Les données")
        lines.append("")
        lines.append("| Unité | Fichier | Fills |")
        lines.append("|---|---|---|")
        for unit, path in CSV_UNITS:
            n = len(per_unit[unit]["fills"])
            lines.append(f"| {unit} | `{path.name}` | {n} |")
        lines.append("")

    else:
        lines.append("⚠️ Aucun trade rempli trouvé — vérifier les CSV de runs.")
        lines.append("")

    # Écriture du rapport
    from datetime import date
    suffixe = f"_depuis_{args.depuis}" if args.depuis else ""
    out_file = OUT_DIR / f"MONTE_CARLO_ACE_{date.today().isoformat()}{suffixe}.md"
    out_file.write_text("\n".join(lines), encoding="utf-8")

    # Résumé console
    print(f"=== MONTE CARLO ACE — {date.today().isoformat()} ===")
    print(f"Trades réels : {total_fills} fills / {total_cycles} cycles "
          f"(P(fill) réel {p_fill_total*100:.2f} %)")
    if all_fills:
        print(f"PnL/trade {ev_par_trade:+.4f} $ → PnL/cycle réel {ev_par_cycle_reel:+.4f} $")
        print(f"MC {args.sims} chemins : DD médian {res['median_dd']*100:.1f} % | "
              f"DD pire {res['p95_dd']*100:.1f} % | pire DD {res['worst_dd']*100:.1f} % | "
              f"ruine {res['ruin_prob']*100:.1f} % | vert {res['green_prob']*100:.1f} % | "
              f"total réel {res['sum_pnl']:+.2f} $")
        print(f"Rapport : {out_file.relative_to(ROOT)}")
    print(f"P(fill) par unité : " + ", ".join(
        f"{u}={d['p_fill']*100:.1f}%" for u, d in per_unit.items()))


if __name__ == "__main__":
    sys.exit(main())
