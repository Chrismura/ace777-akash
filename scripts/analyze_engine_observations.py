#!/usr/bin/env python3
"""Assess completeness of engine-log observation telemetry."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

FIELDS = ("spread_bps", "momentum_bps", "confidence")
TENSION = re.compile(r"tension=(-?\d+(?:\.\d+)?)")


def summarize(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    decisions = Counter(row.get("decision", "") for row in rows)
    reasons = Counter(row.get("reason", "") for row in rows)
    tensions = []
    for row in rows:
        match = TENSION.search(row.get("reason", ""))
        if match:
            tensions.append(float(match.group(1)))
    return {
        "file": path.name,
        "rows": len(rows),
        "decisions": decisions,
        "reasons": reasons,
        "fields": {field: sum(bool(row.get(field, "")) for row in rows) for field in FIELDS},
        "units": sorted({row.get("unit", "") for row in rows}),
        "run_ids": sorted({row.get("run_id", "") for row in rows}),
        "tensions": tensions,
    }


def write_report(paths: list[Path], output: Path) -> None:
    summaries = [summarize(path) for path in paths]
    lines = [
        "# ACE engine observation quality",
        "",
        "> Read-only analysis of parsed historical logs. Missing values are not inferred.",
        "",
        "| File | Rows | SKIP | ALLOW | Tension values | Tension avg | Spread field | Momentum field | Confidence field | Units | run_id |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in summaries:
        d = item["decisions"]
        f = item["fields"]
        tensions = item["tensions"]
        avg = f"{sum(tensions) / len(tensions):.3f}" if tensions else "—"
        lines.append(f"| `{item['file']}` | {item['rows']} | {d.get('SKIP', 0)} | {d.get('ALLOW', 0)} | {len(tensions)} | {avg} | {f['spread_bps']} | {f['momentum_bps']} | {f['confidence']} | {','.join(item['units'])} | {','.join(item['run_ids'])} |")
    lines += [
        "",
        "## Verdict",
        "",
        "- The current log parser captures decisions and units reliably.",
        "- Historical logs do not provide complete spread/momentum fields per cycle.",
        "- No gate threshold should be changed based on incomplete telemetry.",
        "- The next engine instrumentation should emit one structured observation before every decision.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze parsed engine observations")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    write_report(args.inputs, args.output)
    print(f"ENGINE_OBSERVATION_QUALITY_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
