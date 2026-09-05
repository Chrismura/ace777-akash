#!/usr/bin/env python3
"""Parse telemetry embedded in ACE text logs into observation CSV rows."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from observation_recorder import ObservationRecorder

ANSI = re.compile("\\x1b\\[[0-9;]*m")
TOKEN = re.compile(r"(?P<key>conf|spread_bps|raw_mom_bps|tension|mom_sig)=?(?P<value>-?\d+(?:\.\d+)?)")
HEADER = re.compile(r"\[(?P<unit>[^]]+)\]\s+(?P<clock>\d\d:\d\d:\d\d)\s+(?P<x>[^#]+)#(?P<cycle>\d+)\s+(?P<decision>SKIP|FILLED)\b")


def parse_line(line: str, *, run_id: str, source: str) -> dict | None:
    line = ANSI.sub("", line)
    match = HEADER.search(line)
    if not match:
        return None
    values = {m.group("key"): float(m.group("value")) for m in TOKEN.finditer(line)}
    tension_match = re.search(r"tension[=\\s]+(-?\\d+(?:\\.\\d+)?)", line)
    if tension_match:
        values["tension"] = float(tension_match.group(1))
    decision = match.group("decision")
    return {
        "ts": match.group("clock"),
        "run_id": run_id,
        "unit": "ALPHA" if "ALPHA" in match.group("unit") else "BETA" if "BETA" in match.group("unit") else "UNKNOWN",
        "cycle": match.group("cycle"),
        "symbol": "BTCUSDT",
        "spread_bps": values.get("spread_bps", ""),
        "momentum_bps": values.get("raw_mom_bps", ""),
        "regime": "ENGINE_LOG",
        "decision": "ALLOW" if decision == "FILLED" else "SKIP",
        "confidence": values.get("conf", ""),
        "reason": f"engine_log:{source};tension={values.get('tension', '')}",
    }


def parse(source: Path, destination: Path, *, run_id: str) -> int:
    recorder = ObservationRecorder(destination, enabled=True)
    count = 0
    with source.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            observation = parse_line(line, run_id=run_id, source=source.name)
            if observation and recorder.record(observation):
                count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse local ACE engine log telemetry")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    print(f"ENGINE_LOG_OBSERVATIONS_OK rows={parse(args.source, args.destination, run_id=args.run_id)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
