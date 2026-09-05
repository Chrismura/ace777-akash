#!/usr/bin/env python3
"""Compare converted ACE observation CSVs without network or execution."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def summarize(path: Path) -> dict:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    decisions = Counter(row.get("decision", "") for row in rows)
    reasons = Counter(row.get("reason", "").split(";", 1)[0] for row in rows)
    fills = [row for row in rows if row.get("decision") == "ALLOW"]
    return {
        "file": path.name,
        "rows": len(rows),
        "skips": decisions.get("SKIP", 0),
        "allows": decisions.get("ALLOW", 0),
        "unit": sorted({row.get("unit", "") for row in rows}),
        "run_ids": sorted({row.get("run_id", "") for row in rows}),
        "top_reasons": reasons.most_common(5),
        "filled_with_mid": sum(bool(row.get("mid")) for row in fills),
        "filled": len(fills),
    }


def report(paths: list[Path], output: Path) -> None:
    summaries = [summarize(path) for path in paths]
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# ACE observation comparison",
        "",
        "> Local projection of existing CSVs; no market data or Binance reconciliation is implied.",
        f"> Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "",
        "## Runs",
        "",
        "| File | Unit | Rows | SKIP | ALLOW | ALLOW with entry price | run_id |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for item in summaries:
        lines.append(
            f"| `{item['file']}` | {','.join(item['unit'])} | {item['rows']} | "
            f"{item['skips']} | {item['allows']} | {item['filled_with_mid']} | "
            f"{','.join(item['run_ids'])} |"
        )
    lines += ["", "## Top decision reasons", ""]
    for item in summaries:
        lines.append(f"### `{item['file']}`")
        for reason, count in item["top_reasons"]:
            lines.append(f"- `{reason}` — {count}")
        lines.append("")
    lines += [
        "## Interpretation limits",
        "",
        "- This report describes recorded engine decisions only.",
        "- Missing bid/ask/order-book values remain missing.",
        "- It does not establish profitability, slippage, or Binance fee reconciliation.",
        "- It must not be used as permission to launch ACE or LIVE trading.",
        "",
    ]
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare local ACE observation CSVs")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    report(args.inputs, args.output)
    print(f"OBSERVATION_COMPARISON_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
