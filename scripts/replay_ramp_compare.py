#!/usr/bin/env python3
"""Compare historical leverage profiles without changing trade direction.

This is a sensitivity/replay report, not a backtest: it reuses observed gross
returns and applies a conservative size multiplier for the leverage profile.
No network, orders, or engine execution.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def fills(path: Path):
    with path.open(newline="") as f:
        return [r for r in csv.DictReader(f) if r.get("status") == "FILLED"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="ACE_DUO_CLEAN_V3_15M")
    ap.add_argument("--runs", default="runs")
    args = ap.parse_args()
    root = Path(args.runs)
    all_rows = []
    for role, suffix in (("BETA", "BETA_X5"), ("ALPHA", "ALPHA_X13_BURST13")):
        p = root / f"{args.tag}_{suffix}.csv"
        if p.exists():
            all_rows.extend((role, r) for r in fills(p))
    print(f"REPLAY_RAMP_COMPARE tag={args.tag} fills={len(all_rows)}")
    for name, multiplier in (("x13_fixed", 1.0), ("ramp_5_to_13", 0.6923076923)):
        gross = sum(float(r.get("pnl") or 0) * multiplier for _, r in all_rows)
        fee = sum(float(r.get("feeUsdt") or 0) * multiplier for _, r in all_rows)
        net = gross - fee
        print(f"{name}: gross={gross:.4f} fees={fee:.4f} net={net:.4f}")
    print("NOTE: sensitivity only; leverage cannot be reconstructed exactly from exit prices.")


if __name__ == "__main__":
    main()
