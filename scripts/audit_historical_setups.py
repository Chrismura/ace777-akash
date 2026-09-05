#!/usr/bin/env python3
"""Read-only comparison of ACE historical setup reports from 2026-07-09 onward."""
from __future__ import annotations

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPORT_RE = re.compile(r"RAPPORT_PNL_AUTO_(202607(?:09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))_\d+\.md$")
DATE_RE = re.compile(r"\*\*Période:\*\* ([^ ]+) → ([^ ]+)")
SETUP_RE = re.compile(r"\*\*Setup:\*\* `([^`]+)` v`([^`]+)`")
TOTAL_RE = re.compile(r"\| (?:\*\*PNL SESSION TOTAL\*\*|PNL SESSION TOTAL) \| (?:\*\*)?([+-]?[0-9.]+)")
NET_RE = re.compile(r"\| \*\*PNL net\*\* \| \*\*([+-]?[0-9.]+)")


def parse(path: Path):
    if not REPORT_RE.search(path.name):
        return None
    text = path.read_text(errors="replace")
    period, setup, total = DATE_RE.search(text), SETUP_RE.search(text), TOTAL_RE.search(text)
    if not (period and setup and total):
        return None
    try:
        start = datetime.fromisoformat(period.group(1).replace("Z", "+00:00"))
        end = datetime.fromisoformat(period.group(2).replace("Z", "+00:00"))
    except ValueError:
        return None
    nets = [float(x) for x in NET_RE.findall(text)]
    return {"path": str(path), "start": start, "end": end, "setup": setup.group(1),
            "version": setup.group(2), "total": float(total.group(1)),
            "has_net_detail": bool(nets)}


def main():
    parsed = [x for x in (parse(p) for p in Path("runs").glob("RAPPORT_PNL_AUTO_*.md")) if x]
    unique = {}
    for item in parsed:
        key = (item["start"], item["end"], item["setup"], item["version"], item["total"])
        unique[key] = item
    groups = defaultdict(list)
    for item in unique.values():
        groups[(item["setup"], item["version"])].append(item)
    print("ACE HISTORICAL SETUP AUDIT — depuis 2026-07-09")
    print(f"reports={len(parsed)} unique_intervals={len(unique)}")
    for (setup, version), items in sorted(groups.items()):
        total = sum(x["total"] for x in items)
        avg = total / len(items)
        net = all(x["has_net_detail"] for x in items)
        print(f"{setup} v{version}: unique_runs={len(items)} sum={total:.4f} avg={avg:.4f} net_detail={'yes' if net else 'no'}")
        for x in sorted(items, key=lambda y: y["start"], reverse=True)[:3]:
            print(f"  {x['start'].isoformat()}..{x['end'].isoformat()} total={x['total']:+.4f}")


if __name__ == "__main__":
    main()
