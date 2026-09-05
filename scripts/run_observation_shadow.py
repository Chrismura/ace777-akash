#!/usr/bin/env python3
"""Replay local observation snapshots into the stable observation CSV.

Input is newline-delimited JSON. This process is deliberately local-only:
network-looking input is rejected and no exchange client or order function is
available. It is safe to run while ACE is stopped.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from observation_recorder import ObservationRecorder


FORBIDDEN_KEYS = {"api_key", "api_secret", "signature", "order", "quantity", "symbol_order"}
FORBIDDEN_URL_PREFIXES = ("http://", "https://", "ws://", "wss://")


def load_snapshot(line: str) -> dict:
    value = json.loads(line)
    if not isinstance(value, dict):
        raise ValueError("snapshot must be a JSON object")
    lowered = {str(key).lower() for key in value}
    if lowered & FORBIDDEN_KEYS:
        raise ValueError("snapshot contains forbidden trading/auth fields")
    for item in value.values():
        if isinstance(item, str) and item.lower().startswith(FORBIDDEN_URL_PREFIXES):
            raise ValueError("network URLs are not allowed")
    return value


def run(input_path: Path, output_path: Path, *, run_id: str) -> int:
    recorder = ObservationRecorder(output_path, enabled=True)
    written = 0
    with input_path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                snapshot = load_snapshot(line)
            except (ValueError, json.JSONDecodeError) as exc:
                print(f"ERROR line {line_number}: {exc}", file=sys.stderr)
                return 2
            snapshot.setdefault("run_id", run_id)
            if recorder.record(snapshot):
                written += 1
    print(f"OBSERVATION_SHADOW_OK rows={written} output={output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Local ACE observation shadow replay")
    parser.add_argument("input", type=Path, help="newline-delimited JSON snapshots")
    parser.add_argument("output", type=Path, help="observation CSV output")
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    return run(args.input, args.output, run_id=args.run_id)


if __name__ == "__main__":
    raise SystemExit(main())
