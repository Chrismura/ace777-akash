#!/usr/bin/env python3
"""
reconcilier_binance.py — Réconcilie le CSV du moteur avec l'historique réel Binance.

But : prouver l'écart et calculer le VRAI PnL (pas celui du CSV).

Usage:
  python3 reconcilier_binance.py                  # aujourd'hui
  python3 reconcilier_binance.py --date 2026-08-20  # une date précise
  python3 reconcilier_binance.py --days 7          # 7 derniers jours
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1/Index_Maison")
RUNS = ROOT.parent / "runs"
ENV = Path.home() / ".binance_testnet.env"
BASE_DEFAULT = "https://testnet.binancefuture.com"

ALPHA_CSV = RUNS / "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"
BETA_CSV = RUNS / "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"


def load_env():
    if not ENV.exists():
        raise SystemExit("FAIL: ~/.binance_testnet.env manquant")
    for line in ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("export "):
            line = line[7:]
        if "=" in line:
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip().strip('"').strip("'")


def signed(path: str, params: dict | None = None) -> dict | list:
    key = os.environ["BINANCE_API_KEY"]
    sec = os.environ["BINANCE_API_SECRET"]
    base = os.environ.get("BASE_URL", BASE_DEFAULT).rstrip("/")
    p = dict(params or {})
    p["timestamp"] = int(time.time() * 1000)
    p["recvWindow"] = 60000
    q = urllib.parse.urlencode(p)
    sig = hmac.new(sec.encode(), q.encode(), hashlib.sha256).hexdigest()
    url = f"{base}{path}?{q}&signature={sig}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": key})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode() or "null")


def day_start_ms(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int(time.mktime(dt.timetuple())) * 1000


def fetch_binance_trades(date_str: str) -> list:
    start_ms = day_start_ms(date_str)
    end_ms = start_ms + 86400 * 1000
    all_trades = []
    start = start_ms
    while start < end_ms:
        tr = signed("/fapi/v1/userTrades", {"startTime": start, "endTime": end_ms, "limit": 1000})
        if not tr:
            break
        all_trades.extend(tr)
        start = tr[-1].get("time", end_ms) + 1
        if len(tr) < 1000:
            break
    return all_trades


def load_csv_trades(date_str: str) -> list:
    trades = []
    for name, path in [("ALPHA", ALPHA_CSV), ("BETA", BETA_CSV)]:
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                st = (row.get("status") or "").upper()
                if st == "SKIPPED":
                    continue
                ts = row.get("ts", "")
                if not ts or ts[:10] != date_str:
                    continue
                try:
                    dt = time.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S")
                    unix = int(time.mktime(dt))
                except Exception:
                    continue
                trades.append({
                    "source": name,
                    "ts": ts[:19],
                    "unix": unix,
                    "side": (row.get("side") or "").upper(),
                    "entry": float(row.get("entryPrice", 0) or 0),
                    "exit": float(row.get("exitPrice", 0) or 0),
                    "qty": float(row.get("qty", 0) or 0),
                    "pnl": float(row.get("pnl", 0) or 0),
                })
    return trades


def reconcile(csv_trades: list, binance_trades: list) -> dict:
    """Match CSV trades with Binance trades by time (±60s) and qty."""
    matched = []
    unmatched_csv = []
    csv_ids = set()

    for ct in csv_trades:
        found = False
        for bt in binance_trades:
            bt_unix = bt.get("time", 0) // 1000
            if abs(bt_unix - ct["unix"]) <= 60:
                bt_qty = abs(float(bt.get("qty", 0)))
                if abs(bt_qty - ct["qty"]) < 0.0001:
                    matched.append({"csv": ct, "binance": bt})
                    csv_ids.add(bt.get("id"))
                    found = True
                    break
        if not found:
            unmatched_csv.append(ct)

    unmatched_binance = [t for t in binance_trades if t.get("id") not in csv_ids]

    return {
        "matched": matched,
        "unmatched_csv": unmatched_csv,
        "unmatched_binance": unmatched_binance,
        "csv_count": len(csv_trades),
        "binance_count": len(binance_trades),
        "matched_count": len(matched),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--days", type=int, default=1)
    args = ap.parse_args()

    load_env()

    dates = []
    dt = datetime.strptime(args.date, "%Y-%m-%d")
    for i in range(args.days):
        d = dt
        dates.append(d.strftime("%Y-%m-%d"))
        dt = __import__("datetime").datetime(d.year, d.month, d.day) - __import__("datetime").timedelta(days=1)

    for date_str in dates:
        print(f"\n{'='*60}")
        print(f"  RÉCONCILIATION — {date_str}")
        print(f"{'='*60}")

        csv_trades = load_csv_trades(date_str)
        binance_trades = fetch_binance_trades(date_str)

        if not csv_trades and not binance_trades:
            print(f"  Aucune donnée pour {date_str}")
            continue

        result = reconcile(csv_trades, binance_trades)

        print(f"\n  CSV:      {result['csv_count']:>5} fills")
        print(f"  Binance:  {result['binance_count']:>5} trades")
        print(f"  Matchés:  {result['matched_count']:>5} ({result['matched_count']/max(result['csv_count'],1)*100:.0f}% du CSV)")
        print(f"  Phantoms: {len(result['unmatched_binance']):>5} trades Binance non dans CSV")

        # CSV PnL
        csv_pnl = sum(t["pnl"] for t in csv_trades)
        print(f"\n  CSV PnL brut:     {csv_pnl:+.4f}$")

        # Binance PnL
        binance_pnl = sum(float(t.get("realizedPnl", 0)) for t in binance_trades)
        binance_comm = sum(float(t.get("commission", 0)) for t in binance_trades)
        print(f"  Binance realized: {binance_pnl:+.4f}$")
        print(f"  Binance commission: {binance_comm:+.4f}$")
        print(f"  Binance net:      {binance_pnl + binance_comm:+.4f}$")

        # Phantom PnL
        phantom_pnl = sum(float(t.get("realizedPnl", 0)) for t in result["unmatched_binance"])
        phantom_comm = sum(float(t.get("commission", 0)) for t in result["unmatched_binance"])
        print(f"\n  Phantoms PnL:     {phantom_pnl:+.4f}$")
        print(f"  Phantoms commission: {phantom_comm:+.4f}$")

        # Volume
        phantom_vol = sum(abs(float(t.get("qty", 0)) * float(t.get("price", 0))) for t in result["unmatched_binance"])
        csv_vol = sum(abs(ct["qty"] * ct["entry"]) for ct in csv_trades)
        print(f"\n  CSV volume:       {csv_vol:>10,.0f}$")
        print(f"  Phantom volume:   {phantom_vol:>10,.0f}$")
        print(f"  Ratio:            {phantom_vol/max(csv_vol,1):.1f}x")

        # Top 5 phantom losses
        if result["unmatched_binance"]:
            print(f"\n  Top 5 phantom losses:")
            sorted_ph = sorted(result["unmatched_binance"], key=lambda t: float(t.get("realizedPnl", 0)))
            for t in sorted_ph[:5]:
                ts = time.strftime("%H:%M:%S", time.gmtime(t["time"] / 1000))
                pnl = float(t.get("realizedPnl", 0))
                qty = float(t.get("qty", 0))
                print(f"    {ts}Z qty={qty:.6f} pnl={pnl:+.4f}$")


if __name__ == "__main__":
    sys.exit(main() or 0)
