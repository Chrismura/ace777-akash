#!/usr/bin/env python3
"""Generate deterministic local observation fixtures.

These fixtures are for pipeline validation only and are explicitly marked
synthetic so they cannot be mistaken for exchange or engine observations.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate(path: Path, *, run_id: str, rows: int = 12) -> int:
    if rows < 1:
        raise ValueError("rows must be positive")
    start = datetime(2026, 9, 1, tzinfo=timezone.utc)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for cycle in range(1, rows + 1):
            decision = "SKIP" if cycle % 3 else "ALLOW"
            snapshot = {
                "ts": (start + timedelta(seconds=cycle)).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "run_id": run_id,
                "unit": "BETA" if cycle % 2 else "ALPHA",
                "cycle": cycle,
                "symbol": "BTCUSDT",
                "bid": 70000 + cycle,
                "ask": 70001 + cycle,
                "mid": 70000.5 + cycle,
                "spread_bps": 0.1428,
                "momentum_bps": 0.25 if decision == "ALLOW" else 0.02,
                "regime": "SYNTHETIC_FIXTURE",
                "decision": decision,
                "side": "BUY" if decision == "ALLOW" else "",
                "confidence": 0.72 if decision == "ALLOW" else 0.18,
                "reason": "synthetic_fixture",
            }
            handle.write(json.dumps(snapshot, ensure_ascii=False) + "\n")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate local synthetic observation snapshots")
    parser.add_argument("output", type=Path)
    parser.add_argument("--run-id", default="ACE_SYNTHETIC_FIXTURE")
    parser.add_argument("--rows", type=int, default=12)
    args = parser.parse_args()
    count = generate(args.output, run_id=args.run_id, rows=args.rows)
    print(f"SYNTHETIC_FIXTURE_OK rows={count} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
