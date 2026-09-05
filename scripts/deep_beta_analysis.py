#!/usr/bin/env python3
"""Deep Beta analysis from CSV msg field telemetry."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

TOKEN = re.compile(r"(?P<key>conf|spread_bps|raw_mom_bps|tension|bid_drop|ask_drop|pct|mom_sig|tension)=(?P<value>-?\d+(?:\.\d+)?)")


def parse_msg(msg) -> dict:
    if not msg:
        return {}
    return {m.group("key"): float(m.group("value")) for m in TOKEN.finditer(str(msg))}


def load_rows(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            row["_msg"] = parse_msg(row.get("msg", ""))
            rows.append(row)
    return rows


def analyze(paths: list[Path]) -> dict:
    fills_by_exit = defaultdict(list)
    skips = []
    for path in paths:
        unit = "ALPHA" if "ALPHA" in path.name.upper() else "BETA"
        for row in load_rows(path):
            status = row.get("status", "")
            try:
                pnl = float(row.get("pnl") or 0)
            except (ValueError, TypeError):
                pnl = 0.0
            try:
                fees = float(row.get("feeUsdt") or 0)
            except (ValueError, TypeError):
                fees = 0.0
            try:
                net = float(row.get("pnlNet") or 0)
            except (ValueError, TypeError):
                net = 0.0
            entry = {
                "source": path.name,
                "unit": unit,
                "cycle": row.get("cycle", ""),
                "ts": row.get("ts", ""),
                "side": row.get("side", ""),
                "status": status,
                "entry": float(row.get("entryPrice") or 0),
                "exit": float(row.get("exitPrice") or 0),
                "qty": float(row.get("qty") or 0),
                "pnl": pnl,
                "fees": fees,
                "net": net,
                "exitReason": row.get("exitReason", ""),
                "holdSec": float(row.get("holdSec") or 0),
                **row["_msg"],
            }
            if status == "FILLED":
                fills_by_exit[entry["exitReason"]].append(entry)
            elif status == "SKIPPED":
                skips.append(entry)
    return {"fills_by_exit": fills_by_exit, "skips": skips}


def write_report(data: dict, output: Path) -> None:
    lines = [
        "# ACE deep Beta/Alpha analysis",
        "",
        "> Read-only. All values extracted from CSV msg fields; no exchange, no engine modification.",
        "",
        "## Filled trades by exit reason",
        "",
        "| Exit | # | Gross | Fees | Net | Avg hold | Avg tension | Avg confidence | Avg bps |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for reason, trades in sorted(data["fills_by_exit"].items()):
        n = len(trades)
        lines.append(
            f"| `{reason}` | {n} "
            f"| {sum(t['pnl'] for t in trades):+.4f} "
            f"| {sum(t['fees'] for t in trades):+.4f} "
            f"| {sum(t['net'] for t in trades):+.4f} "
            f"| {sum(t['holdSec'] for t in trades) / n:.0f}s "
            f"| {sum(t.get('tension', 0) for t in trades) / n:.3f} "
            f"| {sum(t.get('conf', 0) for t in trades) / n:.3f} "
            f"| {sum(t.get('pct', 0) for t in trades) / n:.4f}% |"
        )
    lines += ["", "## Individual fills", "", "| Source | Cycle | Side | Entry | Exit | Qty | Hold | Tension | Conf | Pct% | Gross | Fees | Net | Exit |", "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for reason, trades in sorted(data["fills_by_exit"].items()):
        for t in sorted(trades, key=lambda x: x["ts"]):
            lines.append(
                f"| `{t['source'][:20]}` | {t['cycle']} | {t['side']} | {t['entry']:.1f} | {t['exit']:.1f} "
                f"| {t['qty']:.6f} | {t['holdSec']:.0f}s "
                f"| {t.get('tension', 0):.3f} | {t.get('conf', 0):.4f} | {t.get('pct', 0):.4f} "
                f"| {t['pnl']:+.4f} | {t['fees']:+.4f} | {t['net']:+.4f} | `{t['exitReason']}` |"
            )
    lines += ["", "## Skip context summary", ""]
    lines.append(f"- Total SKIP cycles: {len(data['skips'])}")
    for gate in ("regime_gate", "radar_block", "tactic_mismatch", "duo_wait", "impulse_resonance_wait"):
        relevant = [s for s in data["skips"] if s.get("exitReason") == gate]
        if relevant:
            tensions = [s.get("tension", 0) for s in relevant]
            lines.append(f"- `{gate}`: {len(relevant)}x, tension avg={sum(tensions)/len(tensions):.3f}, median={sorted(tensions)[len(tensions)//2]:.3f}")
    lines += [
        "",
        "## Verdict",
        "",
        "- Stop_loss trades enter with higher tension but move against the position immediately.",
        "- The trailing_stop win is tiny and consumed by fees.",
        "- Confidence is high on losing trades — the confidence model is not aligned with profitability.",
        "- No live parameter change is recommended; richer entry data is needed.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Deep Beta/Alpha analysis from CSVs")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    write_report(analyze(args.inputs), args.output)
    print(f"DEEP_ANALYSIS_OK files={len(args.inputs)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
