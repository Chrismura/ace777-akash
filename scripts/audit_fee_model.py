#!/usr/bin/env python3
"""Read-only audit of ACE CSV fee calculations."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def audit(runs: Path, tag: str) -> dict:
    meta_files = sorted(runs.glob(f"{tag}_*_session.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    meta = json.loads(meta_files[0].read_text()) if meta_files else {}
    expected_round_trip = float(meta.get("fee_round_trip_bps", 8))
    rows = []
    for role, suffix in (("BETA", "BETA_X5"), ("ALPHA", "ALPHA_X13_BURST13")):
        path = runs / f"{tag}_{suffix}.csv"
        if not path.exists():
            continue
        with path.open(newline="") as handle:
            for row in csv.DictReader(handle):
                if row.get("status") != "FILLED":
                    continue
                entry = float(row.get("entryPrice") or 0)
                exit_price = float(row.get("exitPrice") or 0)
                qty = abs(float(row.get("qty") or 0))
                fee = float(row.get("feeUsdt") or 0)
                notional = (entry + exit_price) * qty
                bps = fee / notional * 10000 if notional else 0
                rows.append({"role": role, "cycle": row.get("cycle"), "notional": notional, "fee": fee, "fee_bps": bps})
    total_notional = sum(r["notional"] for r in rows)
    total_fee = sum(r["fee"] for r in rows)
    actual = total_fee / total_notional * 10000 if total_notional else 0
    return {"tag": tag, "expected_round_trip_bps": expected_round_trip, "actual_fee_bps": round(actual, 6), "rows": rows, "ok": abs(actual - expected_round_trip / 2) < 0.01}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--runs", default="runs")
    args = ap.parse_args()
    result = audit(Path(args.runs), args.tag)
    print(json.dumps(result, indent=2))
    print("FEE_MODEL_AUDIT_OK" if result["ok"] else "FEE_MODEL_AUDIT_FAIL")
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
