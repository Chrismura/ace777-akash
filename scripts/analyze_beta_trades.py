#!/usr/bin/env python3
"""Analyze Beta trade economics from local CSVs only."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def load(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row.get("status") == "FILLED"]


def f(row: dict, key: str) -> float:
    try:
        return float(row.get(key) or 0)
    except ValueError:
        return 0.0


def analyze(paths: list[Path]) -> dict:
    by_exit = defaultdict(lambda: {"count": 0, "gross": 0.0, "fees": 0.0, "net": 0.0})
    trades = []
    for path in paths:
        for row in load(path):
            reason = row.get("exitReason") or "unknown"
            item = by_exit[reason]
            item["count"] += 1
            item["gross"] += f(row, "pnl")
            item["fees"] += f(row, "feeUsdt")
            item["net"] += f(row, "pnlNet")
            trades.append((path.name, row))
    return {"by_exit": by_exit, "trades": trades}


def write_report(data: dict, output: Path) -> None:
    lines = [
        "# ACE Beta trade economics",
        "",
        "> Read-only analysis of local Beta CSV fills; no strategy or engine change was applied.",
        "",
        "| Exit reason | Trades | Gross | Fees | Net |",
        "|---|---:|---:|---:|---:|",
    ]
    for reason, item in sorted(data["by_exit"].items()):
        lines.append(f"| `{reason}` | {item['count']} | {item['gross']:+.4f} | {item['fees']:+.4f} | {item['net']:+.4f} |")
    lines += ["", "## Individual fills", "", "| Source | Cycle | Entry | Exit | Qty | Gross | Fees | Net | Exit |", "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for source, row in data["trades"]:
        lines.append(f"| `{source}` | {row.get('cycle', '')} | {row.get('entryPrice', '')} | {row.get('exitPrice', '')} | {row.get('qty', '')} | {f(row, 'pnl'):+.4f} | {f(row, 'feeUsdt'):+.4f} | {f(row, 'pnlNet'):+.4f} | {row.get('exitReason', '')} |")
    lines += [
        "",
        "## Strict verdict",
        "",
        "- Beta must not be changed based on a small sample alone.",
        "- A stop-loss loss and its fee are separate effects and must remain separate in diagnosis.",
        "- The next safe improvement is richer entry telemetry and replay, not a live parameter change.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze local ACE Beta trades")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    write_report(analyze(args.inputs), args.output)
    print(f"BETA_ANALYSIS_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
