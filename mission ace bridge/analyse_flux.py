#!/usr/bin/env python3
"""Analyse le dernier CSV de runs et resume le flux."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

TENSION_RE = re.compile(r"tension=([-+]?\d*\.?\d+)")
HOLD_RE = re.compile(r"hold=([-+]?\d*\.?\d+)s?")
KEYVAL_RE = re.compile(r"(?:^|[,\s])([A-Za-z_][A-Za-z0-9_]*)=([^,\s]+)")


def to_float(value: Any) -> float | None:
    try:
        if value is None:
            return None
        text = str(value).strip()
        if text == "":
            return None
        return float(text)
    except ValueError:
        return None


def parse_keyvals(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in KEYVAL_RE.finditer(text or ""):
        out[m.group(1)] = m.group(2)
    return out


def extract_tension(row: dict[str, str], msg: str) -> float | None:
    direct = to_float(row.get("tension"))
    if direct is not None:
        return direct
    kv = parse_keyvals(msg)
    if "tension" in kv:
        return to_float(kv["tension"])
    m = TENSION_RE.search(msg or "")
    if m:
        return to_float(m.group(1))
    return None


def extract_hold(row: dict[str, str], msg: str) -> float | None:
    for key in ("hold", "holdSec"):
        v = to_float(row.get(key))
        if v is not None:
            return v
    kv = parse_keyvals(msg)
    if "hold" in kv:
        return to_float(kv["hold"])
    m = HOLD_RE.search(msg or "")
    if m:
        return to_float(m.group(1))
    return None


def extract_reason(row: dict[str, str], msg: str) -> str:
    reason = (row.get("reason") or row.get("exitReason") or "").strip()
    if reason:
        return reason
    kv = parse_keyvals(msg)
    return kv.get("reason", "")


def extract_msg(row: dict[str, str]) -> str:
    for key in ("msg", "message", "details", "extra"):
        if key in row and row[key]:
            return row[key]
    return ""


def latest_csv(runs_dir: Path) -> Path:
    files = [p for p in runs_dir.glob("*.csv") if p.is_file()]
    if not files:
        raise FileNotFoundError(f"Aucun CSV trouve dans: {runs_dir}")
    return max(files, key=lambda p: p.stat().st_mtime)


def load_rows(csv_path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            msg = extract_msg(row)
            out.append(
                {
                    "ts": row.get("ts", ""),
                    "tension": extract_tension(row, msg),
                    "pnl": to_float(row.get("pnl")),
                    "reason": extract_reason(row, msg),
                    "hold": extract_hold(row, msg),
                }
            )
    return out


def summarize(rows: list[dict[str, Any]], tail_count: int) -> dict[str, Any]:
    last = rows[-tail_count:] if tail_count > 0 else []
    tensions = [r["tension"] for r in rows if isinstance(r.get("tension"), (int, float))]
    avg_tension = sum(tensions) / len(tensions) if tensions else None
    return {
        "total_rows": len(rows),
        "last_rows": last,
        "avg_tension": avg_tension,
        "tension_count": len(tensions),
    }


def print_human(csv_file: Path, report: dict[str, Any]) -> None:
    print(f"Fichier analyse: {csv_file}")
    print(f"Lignes lues: {report['total_rows']}")
    print(f"Tensions detectees: {report['tension_count']}")
    avg = report["avg_tension"]
    print(f"Moyenne tension: {avg:.6f}" if avg is not None else "Moyenne tension: n/a")
    print("")
    print("5 dernieres lignes (tension, pnl, reason, hold):")
    for r in report["last_rows"]:
        t = "n/a" if r["tension"] is None else f"{r['tension']:.6f}"
        p = "n/a" if r["pnl"] is None else f"{r['pnl']:.6f}"
        h = "n/a" if r["hold"] is None else f"{r['hold']:.2f}"
        print(f"- {r.get('ts','')} | tension={t} pnl={p} reason={r.get('reason','')} hold={h}")


def default_runs_dir() -> Path:
    # .../ace777-test-day1/mission ace bridge/analyse_flux.py -> .../ace777-test-day1/runs
    project_root = Path(__file__).resolve().parents[1]
    return project_root / "runs"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Analyse le CSV le plus recent du dossier runs/")
    p.add_argument("--runs-dir", type=Path, default=default_runs_dir(), help="Dossier contenant les CSV")
    p.add_argument("--tail", type=int, default=5, help="Nombre de dernieres lignes a afficher")
    p.add_argument("--json", action="store_true", help="Sortie JSON (integration application)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        csv_file = latest_csv(args.runs_dir)
        rows = load_rows(csv_file)
        report = summarize(rows, args.tail)
        if args.json:
            payload = {
                "csv_file": str(csv_file),
                **report,
            }
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print_human(csv_file, report)
        return 0
    except Exception as exc:  # pylint: disable=broad-except
        print(f"ERREUR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
