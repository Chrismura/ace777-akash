#!/usr/bin/env python3
"""Analyze ACE observation gates without changing or running the engine."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


def analyze(paths: list[Path]) -> dict:
    result = {"files": [], "totals": Counter(), "units": defaultdict(Counter), "reasons": Counter()}
    for path in paths:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        unit = next(iter({row.get("unit", "UNKNOWN") for row in rows}), "UNKNOWN")
        counts = Counter(row.get("decision", "UNKNOWN") for row in rows)
        reasons = Counter(row.get("reason", "").split(";", 1)[0] for row in rows)
        populated = Counter(
            field for row in rows for field in ("mid", "spread_bps", "momentum_bps", "confidence") if row.get(field, "") != ""
        )
        result["files"].append({"path": path.name, "unit": unit, "rows": len(rows), "counts": counts, "reasons": reasons, "populated": populated})
        result["totals"].update(counts)
        result["units"][unit].update(counts)
        result["reasons"].update(reasons)
    return result


def write_report(data: dict, output: Path) -> None:
    total = sum(data["totals"].values())
    skips = data["totals"].get("SKIP", 0)
    allows = data["totals"].get("ALLOW", 0)
    lines = [
        "# ACE gate analysis",
        "",
        "> Read-only analysis of converted CSV observations. No execution or exchange reconciliation.",
        "",
        "## Global result",
        "",
        f"- Rows: **{total}**",
        f"- SKIP: **{skips}** ({(skips / total * 100 if total else 0):.1f}%)",
        f"- ALLOW/FILLED projection: **{allows}** ({(allows / total * 100 if total else 0):.1f}%)",
        "",
        "## By unit/file",
        "",
        "| File | Unit | Rows | SKIP | ALLOW | Mid available | Spread available | Momentum available | Confidence available |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in data["files"]:
        p = item["populated"]
        lines.append(f"| `{item['path']}` | {item['unit']} | {item['rows']} | {item['counts'].get('SKIP', 0)} | {item['counts'].get('ALLOW', 0)} | {p.get('mid', 0)} | {p.get('spread_bps', 0)} | {p.get('momentum_bps', 0)} | {p.get('confidence', 0)} |")
    lines += ["", "## Most frequent recorded reasons", ""]
    for reason, count in data["reasons"].most_common(10):
        lines.append(f"- `{reason}` — {count}")
    lines += [
        "",
        "## Strict interpretation",
        "",
        "- A high SKIP rate is an observation, not proof that a gate is wrong.",
        "- This projection lacks complete bid/ask history and cannot estimate missed-trade PnL.",
        "- No threshold change is recommended from this report alone.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze local ACE observation gates")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    write_report(analyze(args.inputs), args.output)
    print(f"GATE_ANALYSIS_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
