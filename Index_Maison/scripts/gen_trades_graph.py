#!/usr/bin/env python3
"""Génère les données du graphique trades pour le panneau cockpit.

Lit les CSV du run MASTER_VORTEX_V2_COLLAB_4H (append-only), filtre sur la
session EN COURS (depuis --since, défaut : dernier démarrage GO_VORTEX),
récupère les klines testnet, écrit Index_Maison/data/trades_graph.json.

Usage:
  python3 Index_Maison/scripts/gen_trades_graph.py [--since 2026-08-14T21:44:00]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
DATA = ROOT / "Index_Maison" / "data"
KLINE_URL = "https://testnet.binancefuture.com/fapi/v1/klines"
MAX_KLINES = 240  # 4h de bougies 1m max pour le panneau

CSVS = [
    ("ALPHA", ROOT / "runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"),
    ("BETA", ROOT / "runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"),
]


def fetch_klines(start_ms: int, end_ms: int) -> list[list]:
    out: list[list] = []
    cur = start_ms
    while cur < end_ms and len(out) < MAX_KLINES:
        url = f"{KLINE_URL}?symbol=BTCUSDT&interval=1m&startTime={cur}&endTime={end_ms}&limit=1000"
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                batch = json.loads(r.read().decode())
        except Exception:
            break
        if not batch:
            break
        out.extend(batch)
        nxt = batch[-1][6] + 1
        if nxt <= cur:
            break
        cur = nxt
    return out[:MAX_KLINES]


def load_trades(csv_path: Path, since_dt) -> list[dict]:
    trades = []
    try:
        f = open(csv_path, encoding="utf-8")
    except FileNotFoundError:
        return trades
    with f:
        for row in csv.DictReader(f):
            if row.get("status") != "FILLED":
                continue
            try:
                ts = dt.datetime.strptime(row["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=dt.timezone.utc)
                if since_dt and ts < since_dt:
                    continue
                trades.append({
                    "ts_ms": int(ts.timestamp() * 1000),
                    "ts": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "side": row["side"],
                    "entry": float(row["entryPrice"]),
                    "exit": float(row["exitPrice"]),
                    "pnl": float(row["pnl"]),
                    "reason": row.get("exitReason", ""),
                })
            except (ValueError, KeyError):
                continue
    return trades


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default=None, help="UTC, ex: 2026-08-14T21:44:00 (défaut: début du run actif détecté)")
    args = ap.parse_args()

    since_dt = None
    if args.since:
        since_dt = dt.datetime.strptime(args.since, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=dt.timezone.utc)
    else:
        # source de vérité = CSV : le démarrage du run = la ligne cycle=1 la plus
        # récente (le CSV est append-only depuis juillet, mais le cycle repart à 1
        # à chaque session du lanceur).
        try:
            p = ROOT / "runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"
            rows = list(csv.DictReader(open(p, encoding="utf-8")))
            cyc1 = [r for r in rows if r.get("cycle") == "1" and r.get("ts", "").startswith("2026-08-14T2")]
            if cyc1:
                since_dt = dt.datetime.strptime(cyc1[-1]["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=dt.timezone.utc)
        except Exception:
            pass

    all_trades: dict[str, list] = {}
    t_all = []
    for unit, path in CSVS:
        trades = load_trades(path, since_dt)
        all_trades[unit] = trades
        t_all.extend(trades)
    t_all.sort(key=lambda t: t["ts_ms"])

    klines = []
    if t_all:
        t0 = t_all[0]["ts_ms"] - 10 * 60_000
        t1 = t_all[-1]["ts_ms"] + 5 * 60_000
        klines = fetch_klines(t0, t1)

    payload = {
        "_meta": {
            "generated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "since": since_dt.strftime("%Y-%m-%dT%H:%M:%SZ") if since_dt else None,
            "nb_trades": len(t_all),
            "nb_klines": len(klines),
        },
        "klines": {"t": [k[0] for k in klines], "c": [float(k[4]) for k in klines]},
        "trades": all_trades,
    }
    DATA.mkdir(exist_ok=True)
    out = DATA / "trades_graph.json"
    out.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(f"OK: {out} — since={payload['_meta']['since']} trades={len(t_all)} klines={len(klines)}")
    for unit, tr in all_trades.items():
        pnl = sum(t["pnl"] for t in tr)
        print(f"  {unit}: {len(tr)} trades, PNL {pnl:+.2f} $")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
