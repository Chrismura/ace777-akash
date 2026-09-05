#!/usr/bin/env python3
"""Read-only ACE Duo audit: Alpha/Beta CSV contract and session alignment."""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = {"ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty", "bps", "pnl"}
OPTIONAL_NET_FIELDS = {"feeUsdt", "pnlNet"}


def parse_ts(value: str):
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def inspect(path: Path, start: datetime | None):
    result = {
        "file": path.name,
        "exists": path.exists(),
        "fields": [],
        "rows": 0,
        "fills": 0,
        "skips": 0,
        "pnlGross": 0.0,
        "fees": 0.0,
        "pnlNet": 0.0,
        "netFieldsOk": False,
        "netRows": 0,
        "netConsistent": True,
        "firstTs": None,
        "lastTs": None,
        "schemaOk": False,
        "rowsBeforeSession": 0,
        "sessionRows": 0,
    }
    if not path.exists():
        return result
    with path.open(newline="", encoding="utf-8", errors="ignore") as handle:
        reader = csv.DictReader(handle)
        result["fields"] = reader.fieldnames or []
        result["schemaOk"] = REQUIRED.issubset(result["fields"])
        result["netFieldsOk"] = OPTIONAL_NET_FIELDS.issubset(result["fields"])
        for row in reader:
            result["rows"] += 1
            ts = parse_ts(row.get("ts"))
            if ts:
                result["firstTs"] = result["firstTs"] or ts.isoformat()
                result["lastTs"] = ts.isoformat()
                if start and ts < start:
                    result["rowsBeforeSession"] += 1
                    continue
                result["sessionRows"] += 1
            status = (row.get("status") or "").upper()
            if status == "SKIPPED" or (row.get("side") or "").upper() == "SKIP":
                result["skips"] += 1
                continue
            if status == "FILLED":
                result["fills"] += 1
                try:
                    gross = float(row.get("pnl") or 0)
                    result["pnlGross"] += gross
                    has_net = bool((row.get("feeUsdt") or "").strip()) and bool((row.get("pnlNet") or "").strip())
                    if has_net:
                        fee = float(row["feeUsdt"])
                        net = float(row["pnlNet"])
                        result["netRows"] += 1
                        result["fees"] += fee
                        result["pnlNet"] += net
                        if abs((gross - fee) - net) > 1e-6:
                            result["netConsistent"] = False
                except ValueError:
                    pass
    result["pnlGross"] = round(result["pnlGross"], 6)
    result["fees"] = round(result["fees"], 6)
    result["pnlNet"] = round(result["pnlNet"], 6)
    result["fees"] = round(result["fees"], 6)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", default="runs")
    parser.add_argument("--tag", default="MASTER_VORTEX_V2_COLLAB_4H")
    parser.add_argument("--meta")
    args = parser.parse_args()
    runs = Path(args.runs)
    meta_path = Path(args.meta) if args.meta else runs / f"{args.tag}_run_meta.json"
    start = None
    meta = {}
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        start = parse_ts(meta.get("start_utc"))
    alpha = inspect(runs / f"{args.tag}_ALPHA_X13_BURST13.csv", start)
    beta = inspect(runs / f"{args.tag}_BETA_X5.csv", start)
    sidecars = sorted(runs.glob(f"{args.tag}_*_session.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    sidecar = None
    if sidecars:
        try:
            sidecar = json.loads(sidecars[0].read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            sidecar = {"invalid": sidecars[0].name}
    out = {
        "tag": args.tag,
        "meta": meta,
        "sessionStart": start.isoformat() if start else None,
        "alpha": alpha,
        "beta": beta,
        "combinedGross": round(alpha["pnlGross"] + beta["pnlGross"], 6),
        "schemaCompatible": alpha["schemaOk"] and beta["schemaOk"],
        "sessionAligned": alpha["sessionRows"] > 0 and beta["sessionRows"] > 0,
        "readOnly": True,
        "sidecar": sidecar,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["schemaCompatible"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
