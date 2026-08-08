#!/usr/bin/env python3
"""Binance FUTURES TESTNET — flatten positions (hedge) + solde + rappel faucet.

Usage:
  python3 scripts/binance_testnet_flatten_recharge.py

Lit ~/.binance_testnet.env (ne print jamais les secrets).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_DEFAULT = "https://testnet.binancefuture.com"
FAUCET_UI = "https://testnet.binancefuture.com/en/futures/BTCUSDT"


def load_env() -> None:
    path = Path.home() / ".binance_testnet.env"
    if not path.exists():
        sys.exit("FAIL: ~/.binance_testnet.env manquant")
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[7:]
        k, v = line.split("=", 1)
        os.environ[k.strip()] = v.strip().strip('"').strip("'")


def signed(method: str, path: str, params: dict | None = None):
    key = os.environ["BINANCE_API_KEY"]
    sec = os.environ["BINANCE_API_SECRET"]
    base = os.environ.get("BASE_URL", BASE_DEFAULT).rstrip("/")
    params = dict(params or {})
    params["timestamp"] = int(time.time() * 1000)
    params["recvWindow"] = 60000
    q = urllib.parse.urlencode(params)
    sig = hmac.new(sec.encode(), q.encode(), hashlib.sha256).hexdigest()
    url = f"{base}{path}?{q}&signature={sig}"
    req = urllib.request.Request(url, method=method, headers={"X-MBX-APIKEY": key})
    if method in ("POST", "DELETE"):
        req.data = b""
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read().decode() or "null"
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        try:
            return json.loads(body)
        except Exception:
            return {"code": e.code, "msg": body}


def usdt_available(bal) -> float | None:
    if isinstance(bal, dict) and bal.get("code"):
        return None
    u = next((x for x in bal if x.get("asset") == "USDT"), None)
    if not u:
        return None
    return float(u.get("availableBalance") or u.get("balance") or 0)


def main() -> int:
    load_env()
    base = os.environ.get("BASE_URL", BASE_DEFAULT).rstrip("/")
    print(f"BASE={base}")
    with urllib.request.urlopen(base + "/fapi/v1/ping", timeout=10) as r:
        print("PING OK")

    dual = signed("GET", "/fapi/v1/positionSide/dual")
    print("dualSidePosition:", dual)

    bal = signed("GET", "/fapi/v2/balance")
    before = usdt_available(bal)
    print(f"BEFORE available USDT={before}")

    pos = signed("GET", "/fapi/v2/positionRisk")
    if isinstance(pos, dict) and pos.get("code"):
        print("POSITIONS ERR", pos)
        return 1

    open_pos = [p for p in pos if abs(float(p.get("positionAmt") or 0)) > 0]
    print(f"OPEN positions={len(open_pos)}")
    for p in open_pos:
        print(
            f"  {p.get('symbol')} side={p.get('positionSide')} "
            f"amt={p.get('positionAmt')} upnl={p.get('unRealizedProfit')}"
        )

    for p in open_pos:
        sym = p["symbol"]
        amt = float(p["positionAmt"])
        ps = p.get("positionSide") or ""
        if ps not in ("LONG", "SHORT"):
            ps = "LONG" if amt > 0 else "SHORT"
        side = "SELL" if ps == "LONG" else "BUY"
        qty = ("%f" % abs(amt)).rstrip("0").rstrip(".")
        params = {
            "symbol": sym,
            "side": side,
            "type": "MARKET",
            "quantity": qty,
            "positionSide": ps,
        }
        # reduceOnly optional in hedge; omit if API complains
        r = signed("POST", "/fapi/v1/order", params)
        print("CLOSE", sym, ps, side, qty, "->", r.get("status") or r.get("msg") or r)

        # if still error about reduceOnly, retry without
        if isinstance(r, dict) and r.get("code") and "reduce" in str(r.get("msg", "")).lower():
            r2 = signed("POST", "/fapi/v1/order", params)
            print("RETRY", sym, "->", r2.get("status") or r2.get("msg") or r2)

    # cancel leftovers
    for sym in sorted({p["symbol"] for p in open_pos}):
        r = signed("DELETE", "/fapi/v1/allOpenOrders", {"symbol": sym})
        print("CANCEL", sym, "->", r)

    time.sleep(1.2)
    bal2 = signed("GET", "/fapi/v2/balance")
    after = usdt_available(bal2)
    print(f"AFTER available USDT={after}")
    left = [
        p
        for p in signed("GET", "/fapi/v2/positionRisk")
        if abs(float(p.get("positionAmt") or 0)) > 0
    ]
    print(f"AFTER open positions={len(left)}")
    for p in left:
        print(" STILL", p.get("symbol"), p.get("positionSide"), p.get("positionAmt"))

    need = float(os.environ.get("PREFLIGHT_MIN_USDT", "1000"))
    if after is not None and after >= need:
        print(f"WALLET OK for preflight (min={need})")
    else:
        print(f"WALLET SHORT for preflight (have={after} need>={need})")
        print("FAUCET: ouvre le testnet et clique Get funds / faucet :")
        print(f"  {FAUCET_UI}")
        print("Puis relance ce script pour vérifier le solde.")

    return 0 if not left else 2


if __name__ == "__main__":
    raise SystemExit(main())
