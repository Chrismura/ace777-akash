#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_edge_criteria.py — assertion automatique du critère d'edge (chantier ace-lab).

Implémente les 3 conditions du §4 de Index_Maison/CHANTIER_ACE_LAB_20260901.md :
  1. PnL net par trade > frais moyen par trade
  2. Win rate net > 50 % (trades FILLED avec pnlNet > 0)
  3. Aucune raison de sortie ne porte plus de 40 % des pertes nettes totales
     (garde-fou anti-dépendance aux stop_loss)

+ garde-fou famille (DeepSeek/Gemini) : refuse de conclure si < MIN_TRADES.

Usage :
  python3 check_edge_criteria.py --tag ACE_RADAR_ALIGNED_V3_15M [--run-dir runs]
  python3 check_edge_criteria.py --beta runs/X_BETA_X5.csv --alpha runs/X_ALPHA_X13_BURST13.csv

Sortie : verdict EDGE_REEL / PAS_D_EDGE / DONNEES_INSUFFISANTES (exit 0/1/2).
Zéro ordre, zéro réseau, lecture seule.
"""
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

MIN_TRADES = 30          # pépite #3 : minimum pour conclure
MIN_NET_PER_TRADE_RATIO = 1.0   # net/trade doit dépasser frais/trade
MIN_WINRATE = 0.50
MAX_LOSS_SHARE = 0.40    # part max des pertes pour une seule raison de sortie


def read_trades(path):
    """Retourne les lignes FILLED d'un CSV moteur (ts, ..., pnlNet, exitReason...)."""
    trades = []
    p = Path(path)
    if not p.is_file():
        return trades
    with p.open(newline="", encoding="utf-8", errors="replace") as fh:
        for row in csv.DictReader(fh):
            if (row.get("status") or "").strip().upper() != "FILLED":
                continue
            try:
                net = float(row.get("pnlNet") or row.get("pnl") or 0.0)
            except ValueError:
                continue
            trades.append({
                "net": net,
                "fee": _f(row.get("feeUsdt")),
                "reason": (row.get("exitReason") or row.get("msg") or "unknown").split(",")[0].strip() or "unknown",
            })
    return trades


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def evaluate(trades):
    """Évalue les critères d'edge sur une liste de trades. Retourne (verdict, details)."""
    n = len(trades)
    total_net = sum(t["net"] for t in trades)
    total_fee = sum(t["fee"] for t in trades)
    wins = sum(1 for t in trades if t["net"] > 0)
    losses_net = -sum(t["net"] for t in trades if t["net"] < 0)

    by_reason = defaultdict(float)
    for t in trades:
        if t["net"] < 0:
            by_reason[t["reason"]] += -t["net"]
    worst_reason, worst_loss = (max(by_reason.items(), key=lambda kv: kv[1]) if by_reason else ("—", 0.0))

    details = {
        "trades": n,
        "total_net": round(total_net, 4),
        "total_fees": round(total_fee, 4),
        "net_per_trade": round(total_net / n, 4) if n else 0.0,
        "fee_per_trade": round(total_fee / n, 4) if n else 0.0,
        "winrate": round(wins / n, 4) if n else 0.0,
        "worst_exit_reason": worst_reason,
        "worst_exit_loss_share": round(worst_loss / losses_net, 4) if losses_net > 0 else 0.0,
    }

    if n < MIN_TRADES:
        return "DONNEES_INSUFFISANTES", details

    checks = {
        "c1_net_vs_frais": details["net_per_trade"] > details["fee_per_trade"] * MIN_NET_PER_TRADE_RATIO
                           and total_net > 0,
        "c2_winrate": details["winrate"] > MIN_WINRATE,
        "c3_loss_concentration": (losses_net <= 0
                                 or details["worst_exit_loss_share"] <= MAX_LOSS_SHARE),
    }
    details["checks"] = checks
    verdict = "EDGE_REEL" if all(checks.values()) else "PAS_D_EDGE"
    return verdict, details


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", help="tag de run (déduit les chemins CSV dans --run-dir)")
    ap.add_argument("--beta", help="CSV BETA explicite")
    ap.add_argument("--alpha", help="CSV ALPHA explicite")
    ap.add_argument("--run-dir", default="runs")
    args = ap.parse_args()

    if args.beta and args.alpha:
        beta_csv, alpha_csv = Path(args.beta), Path(args.alpha)
    elif args.tag:
        rd = Path(args.run_dir)
        beta_csv = rd / f"{args.tag}_BETA_X5.csv"
        alpha_csv = rd / f"{args.tag}_ALPHA_X13_BURST13.csv"
    else:
        print("Fournir --tag ou --beta/--alpha.")
        return 2

    trades = read_trades(beta_csv) + read_trades(alpha_csv)
    verdict, details = evaluate(trades)
    print(f"=== CRITERE D'EDGE ({beta_csv.name} + {alpha_csv.name}) ===")
    for k, v in details.items():
        print(f"{k}: {v}")
    print(f"VERDICT: {verdict}")
    return {"EDGE_REEL": 0, "PAS_D_EDGE": 1, "DONNEES_INSUFFISANTES": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
