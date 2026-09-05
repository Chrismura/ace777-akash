#!/usr/bin/env python3
"""Estimate fee-adjusted results for historical ACE CSVs without network."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def summarize(path: Path, fee_bps: float):
    with path.open(newline="", errors="ignore") as f:
        rows = [r for r in csv.DictReader(f) if r.get("status") == "FILLED"]
    gross = sum(float(r.get("pnl") or 0) for r in rows)
    notional = sum((float(r.get("entryPrice") or 0) + float(r.get("exitPrice") or 0)) * abs(float(r.get("qty") or 0)) for r in rows)
    fees = notional * fee_bps / 10000.0
    return len(rows), gross, fees, gross - fees


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--fee-bps", type=float, default=4.0, help="rate on entry+exit notional")
    args = ap.parse_args()
    for path in args.paths:
        if not path.exists():
            continue
        n, gross, fees, net = summarize(path, args.fee_bps)
        print(f"{path}: fills={n} gross={gross:+.4f} fees={fees:+.4f} net={net:+.4f}")


if __name__ == "__main__":
    main()
