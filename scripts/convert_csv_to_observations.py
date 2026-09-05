#!/usr/bin/env python3
"""Convert existing ACE CSV decisions into local observation records.

This is a lossless-ish projection of fields that actually exist in the CSV.
Missing order-book fields remain empty; no market data is invented.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import tempfile
from pathlib import Path

from observation_recorder import ObservationRecorder


def number(value: str):
    if value in (None, ""):
        return ""
    try:
        return float(value)
    except (TypeError, ValueError):
        return ""


def reason_fields(message: str) -> dict:
    values = {}
    for token in (message or "").split():
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        if key in {"conf", "spread_bps", "raw_mom_bps", "tension"}:
            values[key] = number(value)
    return values


def unit_from_source(source: Path) -> str:
    match = re.search(r"_(ALPHA|BETA)(?:_|\.)", source.name)
    return match.group(1) if match else "UNKNOWN"


def convert(source: Path, destination: Path, *, run_id: str) -> int:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", dir=str(destination.parent)
    )
    os.close(fd)
    temporary = Path(temporary_name)
    recorder = ObservationRecorder(temporary, enabled=True)
    unit = unit_from_source(source)
    count = 0
    try:
        with source.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                message = row.get("msg", "")
                parsed = reason_fields(message)
                status = row.get("status", "")
                filled = status == "FILLED"
                reason_name = row.get("exitReason", "") or (message.split(",", 1)[0].split("=", 1)[-1] if message else "unknown")
                observation = {
                    "ts": row.get("ts", ""),
                    "run_id": run_id,
                    "unit": unit,
                    "cycle": row.get("cycle", ""),
                    "symbol": "BTCUSDT",
                    "mid": number(row.get("entryPrice", "")) if filled else "",
                    "spread_bps": parsed.get("spread_bps", ""),
                    "momentum_bps": parsed.get("raw_mom_bps", ""),
                    "regime": "FILLED" if filled else "DECISION_LOG",
                    "decision": "ALLOW" if filled else "SKIP",
                    "side": row.get("side", "") if filled else "",
                    "confidence": parsed.get("conf", ""),
                    "reason": f"csv_engine:{reason_name};source={source.name}",
                }
                if recorder.record(observation):
                    count += 1
        os.replace(temporary, destination)
        return count
    except Exception:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert ACE CSV to local observations")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    count = convert(args.source, args.destination, run_id=args.run_id)
    print(json.dumps({"status": "CSV_OBSERVATION_OK", "rows": count, "output": str(args.destination)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
