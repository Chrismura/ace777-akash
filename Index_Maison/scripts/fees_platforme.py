#!/usr/bin/env python3
"""
Frais de plateforme (Binance FUTURES TESTNET) — lecture seule, sans ordre.

Interroge /fapi/v1/income et agrège par type (COMMISSION, REALIZED_PNL,
FUNDING_FEE, TRANSFER) depuis le début du run courant (premier timestamp du
CSV BETA) et sur 24h. Écrit Index_Maison/thermo/fees_platforme.json.

Usage:
  python3 fees_platforme.py
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
RUNS = ROOT / "runs"
OUT = ROOT / "Index_Maison" / "thermo" / "fees_platforme.json"
ENV = Path.home() / ".binance_testnet.env"
BASE_DEFAULT = "https://testnet.binancefuture.com"

BETA_CSV = RUNS / "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"
ALPHA_CSV = RUNS / "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"


def load_env() -> None:
    if not ENV.exists():
        raise SystemExit("FAIL: ~/.binance_testnet.env manquant")
    for line in ENV.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[7:]
        k, v = line.split("=", 1)
        os.environ[k.strip()] = v.strip().strip('"').strip("'")


def signed(path: str, params: dict | None = None):
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
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode() or "null")


def today_start_ms() -> int:
    """Début du jour UTC (00:00) en ms."""
    now = time.gmtime()
    return int(time.mktime(time.struct_time((now.tm_year, now.tm_mon, now.tm_mday, 0, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))) * 1000)


def aggregate_since(start_ms: int) -> dict:
    """Pagine /fapi/v1/income en remontant dans le temps (du plus récent au plus ancien)."""
    tot: defaultdict[str, float] = defaultdict(float)
    cnt: defaultdict[str, int] = defaultdict(int)
    end_ms = int(time.time() * 1000) + 60000  # maintenant + marge
    pages = 0
    while pages < 60:
        params: dict = {"startTime": start_ms, "limit": 1000}
        if end_ms:
            params["endTime"] = end_ms
        inc = signed("/fapi/v1/income", params)
        if not inc:
            break
        for i in inc:
            t = i.get("incomeType", "?")
            tot[t] += float(i.get("income", 0) or 0)
            cnt[t] += 1
        pages += 1
        if len(inc) < 1000:
            break
        oldest = inc[-1].get("time") or 0
        if oldest <= start_ms:
            break
        end_ms = oldest - 1
    return {"totals": dict(tot), "counts": dict(cnt)}


def main() -> int:
    load_env()
    now = time.time()

    # aujourd'hui (00:00 UTC) — fiable, sans ambiguité de run
    rt = aggregate_since(today_start_ms())
    t = rt["totals"]

    # 24h glissantes
    r24 = aggregate_since(int((now - 24 * 3600) * 1000))
    t24 = r24["totals"]

    def pack(totals, counts):
        return {
            "commission": round(totals.get("COMMISSION", 0.0), 4),
            "realized_pnl": round(totals.get("REALIZED_PNL", 0.0), 4),
            "funding_fee": round(totals.get("FUNDING_FEE", 0.0), 4),
            "net_trading": round(
                totals.get("COMMISSION", 0.0)
                + totals.get("REALIZED_PNL", 0.0)
                + totals.get("FUNDING_FEE", 0.0),
                4,
            ),
            "counts": counts,
        }

    out = {
        "ts": int(now),
        "ts_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
        "today": pack(t, rt["counts"]),
        "h24": pack(t24, r24["counts"]),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(OUT)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
