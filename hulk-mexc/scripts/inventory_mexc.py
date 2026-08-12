#!/usr/bin/env python3
"""Inventaire Hulk × MEXC spot USDT — volume 24h + spread approx → tiers A/B/C."""
from __future__ import annotations

import csv
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "data" / "universe_hulk_seed.csv"
OUT = ROOT / "data" / "universe_mexc_inventory.csv"
CFG = ROOT / "config" / "defaults.env"


def load_env(path: Path) -> dict:
    d = {}
    if not path.exists():
        return d
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        d[k.strip()] = v.strip()
    return d


def http_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "hulk-mexc-inventory/0.1"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main() -> int:
    cfg = load_env(CFG)
    min_vol = float(cfg.get("MIN_QUOTE_VOL_USDT", "50000"))
    max_spread = float(cfg.get("MAX_SPREAD_BPS", "80"))
    quote = cfg.get("QUOTE", "USDT")

    seeds = list(csv.DictReader(SEED.open()))
    symbols = [r["symbol"].strip().upper() for r in seeds if r.get("symbol")]

    print(f"seed={len(symbols)} min_vol={min_vol} max_spread_bps={max_spread}")

    info = http_json("https://api.mexc.com/api/v3/exchangeInfo")
    usdt_bases = {}
    for s in info.get("symbols", []):
        if s.get("quoteAsset") == quote:
            usdt_bases[s["baseAsset"].upper()] = s["symbol"]

    tickers = http_json("https://api.mexc.com/api/v3/ticker/24hr")
    if isinstance(tickers, dict):
        tickers = [tickers]
    tmap = {t["symbol"]: t for t in tickers if "symbol" in t}

    rows = []
    counts = {"A": 0, "B": 0, "C": 0}
    for sym in symbols:
        pair = usdt_bases.get(sym)
        if not pair:
            rows.append(
                {
                    "symbol": sym,
                    "pair": "",
                    "on_mexc": "0",
                    "quote_vol_usdt": "0",
                    "spread_bps": "",
                    "last": "",
                    "tier": "C",
                    "note": "no_USDT_pair",
                }
            )
            counts["C"] += 1
            continue

        t = tmap.get(pair, {})
        qvol = float(t.get("quoteVolume") or t.get("quote_volume") or 0)
        last = float(t.get("lastPrice") or 0)
        bid = float(t.get("bidPrice") or 0)
        ask = float(t.get("askPrice") or 0)
        spread_bps = ""
        if bid > 0 and ask > 0:
            mid = (bid + ask) / 2
            spread_bps = round((ask - bid) / mid * 10000, 2)

        note = "ok"
        if qvol >= min_vol and (spread_bps == "" or spread_bps <= max_spread):
            tier = "A"
        elif qvol > 0:
            tier = "B"
            note = "low_liq_or_wide_spread_spike_candidate"
        else:
            tier = "C"
            note = "zero_volume"

        # si spread connu et énorme → plutôt B même si vol ok
        if isinstance(spread_bps, (int, float)) and spread_bps > max_spread and tier == "A":
            tier = "B"
            note = "wide_spread"

        counts[tier] += 1
        rows.append(
            {
                "symbol": sym,
                "pair": pair,
                "on_mexc": "1",
                "quote_vol_usdt": round(qvol, 2),
                "spread_bps": spread_bps,
                "last": last,
                "tier": tier,
                "note": note,
            }
        )

    rows.sort(key=lambda r: (-float(r["quote_vol_usdt"] or 0), r["symbol"]))
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "symbol",
                "pair",
                "on_mexc",
                "quote_vol_usdt",
                "spread_bps",
                "last",
                "tier",
                "note",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {OUT}")
    print(f"tiers A={counts['A']} B={counts['B']} C={counts['C']}")
    print("--- top A ---")
    for r in [x for x in rows if x["tier"] == "A"][:12]:
        print(
            f"  {r['pair']:12} vol={float(r['quote_vol_usdt']):>12,.0f} "
            f"spread={r['spread_bps']} last={r['last']}"
        )
    print("--- sample B (spike / illiquide) ---")
    for r in [x for x in rows if x["tier"] == "B"][:8]:
        print(
            f"  {r['pair']:12} vol={float(r['quote_vol_usdt']):>12,.0f} "
            f"spread={r['spread_bps']} {r['note']}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
