#!/usr/bin/env python3
"""Analyze extracted tension by run/unit without changing ACE."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

TENSION = re.compile(r"tension=(-?\d+(?:\.\d+)?)")


def percentile(values: list[float], fraction: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, int((len(ordered) - 1) * fraction))
    return ordered[index]


def analyze(paths: list[Path]) -> dict:
    groups = defaultdict(list)
    decisions = Counter()
    for path in paths:
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                match = TENSION.search(row.get("reason", ""))
                if not match:
                    continue
                key = (row.get("run_id", ""), row.get("unit", "UNKNOWN"))
                groups[key].append(float(match.group(1)))
                decisions[(key, row.get("decision", ""))] += 1
    return {"groups": groups, "decisions": decisions}


def write_report(data: dict, output: Path) -> None:
    lines = [
        "# ACE tension by unit",
        "",
        "> Read-only analysis of tension embedded in engine logs.",
        "",
        "| Run | Unit | N | Min | P50 | P90 | Max | Decisions |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for (run_id, unit), values in sorted(data["groups"].items()):
        decision_text = ", ".join(f"{decision}={count}" for (key, decision), count in sorted(data["decisions"].items()) if key == (run_id, unit))
        lines.append(f"| `{run_id}` | {unit} | {len(values)} | {min(values):.3f} | {percentile(values, .50):.3f} | {percentile(values, .90):.3f} | {max(values):.3f} | {decision_text} |")
    lines += [
        "",
        "## Verdict",
        "",
        "- Tension is now measurable from the historical logs.",
        "- The available logs contain SKIP decisions only; they do not prove what would have happened after allowing a blocked cycle.",
        "- No gate threshold change is justified without complete structured observations and replay data.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze ACE tension by unit")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    write_report(analyze(args.inputs), args.output)
    print(f"TENSION_ANALYSIS_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
