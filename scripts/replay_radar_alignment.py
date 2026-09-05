#!/usr/bin/env python3
"""Replay: what if Beta had entered in the radar direction instead of fixed SELL?

Pure local computation on existing CSV data. No network, no orders.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

RADAR = re.compile(r"radar=(long|short)")
TOKEN = re.compile(r"(?P<key>conf|tension|pct)=(?P<value>-?\d+(?:\.\d+)?)")
FEE_BPS = 4.0  # per side, 8 bps round trip


def parse_msg(msg: str) -> dict:
    values = {m.group("key"): float(m.group("value")) for m in TOKEN.finditer(msg)}
    radar_match = RADAR.search(msg)
    values["radar"] = radar_match.group(1) if radar_match else ""
    return values


def load_beta(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("status") != "FILLED":
                continue
            msg = parse_msg(row.get("msg", ""))
            rows.append({
                "source": path.name,
                "cycle": row.get("cycle", ""),
                "ts": row.get("ts", ""),
                "side": row.get("side", ""),
                "entry": float(row.get("entryPrice") or 0),
                "exit": float(row.get("exitPrice") or 0),
                "qty": float(row.get("qty") or 0),
                "pnl": float(row.get("pnl") or 0),
                "fees": float(row.get("feeUsdt") or 0),
                "net": float(row.get("pnlNet") or 0),
                "exitReason": row.get("exitReason", ""),
                "holdSec": float(row.get("holdSec") or 0),
                "radar": msg.get("radar", ""),
                "conf": msg.get("conf", 0),
                "tension": msg.get("tension", 0),
            })
    return rows


def replay_beta(trades: list[dict]) -> dict:
    """If entry had been in radar direction, PnL sign flips for misaligned trades."""
    aligned = []
    misaligned = []
    for t in trades:
        radar = t["radar"]
        side = t["side"]
        is_long_entry = side == "BUY"
        radar_long = radar == "long"
        # aligned: (BUY + radar=long) or (SELL + radar=short)
        if (is_long_entry and radar_long) or (not is_long_entry and not radar_long):
            aligned.append(t)
        else:
            # misaligned: flip the PnL sign (entry was opposite to radar)
            flipped = dict(t)
            flipped["pnl_flipped"] = -t["pnl"]
            flipped["net_flipped"] = -t["pnl"] - t["fees"]
            misaligned.append(flipped)
    return {"aligned": aligned, "misaligned": misaligned}


def write_report(data: dict, output: Path) -> None:
    aligned = data["aligned"]
    misaligned = data["misaligned"]

    real_net = sum(t["net"] for t in aligned) + sum(t["net"] for t in misaligned)
    hypo_net = sum(t["net"] for t in aligned) + sum(t.get("net_flipped", t["net"]) for t in misaligned)
    real_gross = sum(t["pnl"] for t in aligned) + sum(t["pnl"] for t in misaligned)
    hypo_gross = sum(t["pnl"] for t in aligned) + sum(t.get("pnl_flipped", t["pnl"]) for t in misaligned)

    lines = [
        "# Beta radar alignment replay",
        "",
        "> Local hypothetical: what if Beta had entered in the radar direction?",
        "",
        "## Summary",
        "",
        f"- Aligned trades: {len(aligned)}",
        f"- Misaligned trades: {len(misaligned)}",
        f"- Real gross: {real_gross:+.4f}",
        f"- Hypothetical gross (radar-aligned): {hypo_gross:+.4f}",
        f"- Real net: {real_net:+.4f}",
        f"- Hypothetical net: {hypo_net:+.4f}",
        f"- Delta: {hypo_net - real_net:+.4f}",
        "",
        "## Misaligned trades (would flip PnL)",
        "",
        "| Source | Cycle | Side | Radar | Entry | Exit | Real PnL | Hyp PnL | Exit |",
        "|---|---|---|---|---:|---:|---:|---:|---|",
    ]
    for t in misaligned:
        lines.append(
            f"| `{t['source'][:20]}` | {t['cycle']} | {t['side']} | {t['radar']} "
            f"| {t['entry']:.1f} | {t['exit']:.1f} "
            f"| {t['net']:+.4f} | {t.get('net_flipped', t['net']):+.4f} | {t['exitReason']} |"
        )
    lines += [
        "",
        "## Verdict",
        "",
        "- This is a local simulation, not proof of profitability.",
        "- It assumes identical exit timing and fees in both scenarios.",
        "- A positive delta does not mean the engine would have been profitable overall.",
        "- ACE LIVE remains NO-GO.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Replay Beta radar alignment")
    parser.add_argument("output", type=Path)
    parser.add_argument("inputs", nargs="+", type=Path)
    args = parser.parse_args()
    trades = []
    for p in args.inputs:
        trades.extend(load_beta(p))
    write_report(replay_beta(trades), args.output)
    print(f"RADAR_REPLAY_OK trades={len(trades)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
