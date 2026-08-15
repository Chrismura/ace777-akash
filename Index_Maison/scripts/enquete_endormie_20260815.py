#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enquête « endormie » v2 — lecture seule.
Gère les 2 formats CSV : pré-fix (11 champs, payload en col 11) et post-fix (12 champs).
Compare l'activité 12/13/14/08 vs 15/08.
"""
import csv, re
from collections import defaultdict, Counter
from datetime import datetime

BASE = "/Users/christophe/ace777-test-day1/runs"
FILES = {
    "ALPHA": f"{BASE}/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv",
    "BETA":  f"{BASE}/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv",
}
TEN = re.compile(r"tension=([0-9.]+)")
CONF = re.compile(r"conf=([0-9.]+)")
REASON = re.compile(r"reason=([A-Za-z_0-9]+)")
STALE = re.compile(r"tension_stale")

def parse(path):
    days = defaultdict(lambda: {
        "lines": 0, "filled": 0, "skip": 0, "other": 0,
        "pnl": 0.0, "bps_sum": 0.0, "bps_n": 0,
        "ten_sum": 0.0, "ten_n": 0, "ten_max": 0.0,
        "conf_sum": 0.0, "conf_n": 0,
        "first": None, "last": None,
        "reasons": Counter(), "exits": Counter(), "stale_skip": 0,
    })
    with open(path, newline="") as f:
        rd = csv.reader(f)
        header = next(rd)
        ncols = len(header)  # 12 post-fix, 11 pré-fix
        for row in rd:
            if not row:
                continue
            ts = row[0].strip()
            if not ts or "T" not in ts:
                continue
            day = ts[:10]
            d = days[day]
            d["lines"] += 1
            if d["first"] is None or ts < d["first"]:
                d["first"] = ts
            if d["last"] is None or ts > d["last"]:
                d["last"] = ts
            # payload = dernier champ (msg post-fix, ou col 11 pré-fix)
            payload = row[-1].strip() if len(row) > 10 else ""
            status = row[3].strip() if len(row) > 3 else ""
            side = row[2].strip() if len(row) > 2 else ""
            if status == "FILLED":
                d["filled"] += 1
                try:
                    d["pnl"] += float(row[8]) if row[8] else 0.0
                except (ValueError, IndexError):
                    pass
                try:
                    d["bps_sum"] += float(row[7]) if row[7] else 0.0
                    d["bps_n"] += 1
                except (ValueError, IndexError):
                    pass
                ex = row[9].strip() if len(row) > 9 else "?"
                d["exits"][ex] += 1
            elif status in ("SKIP", "SKIPPED"):
                d["skip"] += 1
                rm = REASON.search(payload)
                d["reasons"][rm.group(1) if rm else ("?" if payload else "vide")] += 1
                if STALE.search(payload):
                    d["stale_skip"] += 1
            else:
                d["other"] += 1
            tm = TEN.search(payload)
            if tm:
                v = float(tm.group(1))
                d["ten_sum"] += v
                d["ten_n"] += 1
                d["ten_max"] = max(d["ten_max"], v)
            cm = CONF.search(payload)
            if cm:
                d["conf_sum"] += float(cm.group(1))
                d["conf_n"] += 1
    return days

def span(d):
    try:
        a = datetime.strptime(d["first"][:19], "%Y-%m-%dT%H:%M:%S")
        b = datetime.strptime(d["last"][:19], "%Y-%m-%dT%H:%M:%S")
        return max((b - a).total_seconds() / 3600, 0.0)
    except Exception:
        return 0.0

DAYS = ["2026-08-12", "2026-08-13", "2026-08-14", "2026-08-15"]

for name, path in FILES.items():
    print("=" * 92)
    print(f"### {name}")
    print("=" * 92)
    days = parse(path)
    for day in DAYS:
        d = days.get(day)
        if not d:
            print(f"\n[{day}] aucune donnée")
            continue
        sp = span(d)
        lph = d["lines"] / sp if sp else 0
        fph = d["filled"] / sp if sp else 0
        ten = d["ten_sum"] / d["ten_n"] if d["ten_n"] else 0
        conf = d["conf_sum"] / d["conf_n"] if d["conf_n"] else 0
        skip_pct = 100 * d["skip"] / d["lines"] if d["lines"] else 0
        stale_pct = 100 * d["stale_skip"] / d["skip"] if d["skip"] else 0
        top = ", ".join(f"{k}={v}" for k, v in d["reasons"].most_common(4))
        exits = ", ".join(f"{k}={v}" for k, v in d["exits"].most_common(5))
        print(f"\n[{day}] couvert={sp:.1f}h ({d['first'][11:19]}→{d['last'][11:19]})")
        print(f"  cycles={d['lines']:5d} ({lph:5.1f}/h) | FILLED={d['filled']:4d} ({fph:4.1f}/h) | SKIP={d['skip']:5d} ({skip_pct:4.1f}%)")
        print(f"  pnl={d['pnl']:+9.4f} | bps_moy={d['bps_sum']/d['bps_n'] if d['bps_n'] else 0:+8.4f} | tension moy={ten:.4f} max={d['ten_max']:.4f} | conf_moy={conf:.3f}")
        print(f"  skip_stale_tension={stale_pct:.1f}% | reasons: {top}")
        print(f"  exits: {exits}")
