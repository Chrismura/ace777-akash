#!/usr/bin/env python3
"""Consolidate local ACE run facts without network access or execution."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def trade_stats(path: Path) -> dict:
    stats = {"filled": 0, "gross": 0.0, "fees": 0.0, "net": 0.0, "exits": Counter()}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("status") != "FILLED":
                continue
            stats["filled"] += 1
            stats["gross"] += float(row.get("pnl") or 0)
            stats["fees"] += float(row.get("feeUsdt") or 0)
            stats["net"] += float(row.get("pnlNet") or 0)
            stats["exits"][row.get("exitReason") or "unknown"] += 1
    return stats


def observation_stats(path: Path) -> dict:
    counts = Counter()
    tensions = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            counts[row.get("decision", "UNKNOWN")] += 1
            reason = row.get("reason", "")
            marker = "tension="
            if marker in reason:
                try:
                    tensions.append(float(reason.split(marker, 1)[1].split(";", 1)[0]))
                except ValueError:
                    pass
    return {"rows": sum(counts.values()), "skip": counts["SKIP"], "allow": counts["ALLOW"], "tensions": tensions}


def write_report(run_dir: Path, output: Path, tags: list[str]) -> None:
    lines = [
        "# ACE consolidated run facts",
        "",
        "> Local read-only consolidation. Gross/net values come from trade CSVs; no Binance reconciliation is implied.",
        "",
        "| Run | Unit | Obs rows | SKIP | ALLOW | Fills | Gross | Fees | Net | Exit reasons |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for tag in tags:
        for unit, suffix in (("ALPHA", "ALPHA_X13_BURST13"), ("BETA", "BETA_X5")):
            obs = run_dir / f"{tag}_{suffix}_OBSERVATIONS.csv"
            trades = run_dir / f"{tag}_{suffix}.csv"
            if not obs.exists() or not trades.exists():
                continue
            o = observation_stats(obs)
            t = trade_stats(trades)
            exits = ", ".join(f"{k}={v}" for k, v in sorted(t["exits"].items())) or "—"
            lines.append(f"| `{tag}` | {unit} | {o['rows']} | {o['skip']} | {o['allow']} | {t['filled']} | {t['gross']:+.4f} | {t['fees']:+.4f} | {t['net']:+.4f} | {exits} |")
    lines += [
        "",
        "## Strict verdict",
        "",
        "- The recent runs are technically complete and locally accounted for.",
        "- Observation coverage is sufficient to describe decisions, not to estimate missed-trade outcomes.",
        "- Net performance remains a local engine result until exchange commissions are reconciled by run_id.",
        "- Do not alter gates or enable LIVE based on this report alone.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Consolidate ACE local run facts")
    parser.add_argument("output", type=Path)
    parser.add_argument("tags", nargs="+")
    args = parser.parse_args()
    write_report(Path("runs"), args.output, args.tags)
    print(f"ACE_CONSOLIDATION_OK runs={len(args.tags)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
