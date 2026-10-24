#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONDE NADO — lecture seule, 0 clé, 0 ordre.
R21 NOIR SUR BLANC :
  rôle : vérifier que Nado est vivant et que BTC-PERP est tradable + spread sain
  lecteur : superviseur / cockpit (fraîcheur), Hulk paper plus tard (porte d'entrée)
  preuve : à accumuler 15j avant tout réel — spread, depth, statut live
Interdit : signer, déposer, trader. Queries publiques uniquement.
"""
import json, time, urllib.request, urllib.parse, gzip
from pathlib import Path

BASE = "https://api.prod.nado.xyz/gateway/v1"
OUT = Path(__file__).resolve().parent.parent / "thermo" / "nado_live.json"

def get(path, params):
    qs = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{BASE}{path}?{qs}", headers={"Accept-Encoding": "gzip", "User-Agent": "Mozilla/5.0 (Macintosh; ACE777-sonde-lecture-seule)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
        try:
            data = gzip.decompress(data)
        except Exception:
            pass
        return json.loads(data.decode("utf-8", "ignore"))

def main():
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    # 1. symbols perp : BTC présent + live ?
    syms = get("/query", {"type": "symbols", "product_type": "perp"})
    all_syms = (syms.get("data", {}) or {}).get("symbols", {})
    btc = all_syms.get("BTC-PERP", {})
    xlm = [k for k in all_syms if "XLM" in k.upper()]
    shx = [k for k in all_syms if any(x in k.upper() for x in ("SHX", "STRONG", "HOLD"))]

    # 2. carnet BTC id 2 profondeur 10
    book = get("/query", {"type": "market_liquidity", "product_id": 2, "depth": 10})
    bids = (book.get("data", {}) or {}).get("bids", [])
    asks = (book.get("data", {}) or {}).get("asks", [])
    spread_bps = None
    bid_px = ask_px = None
    bid5 = ask5 = 0.0
    if bids and asks:
        bid_px = int(bids[0][0]) / 1e18
        ask_px = int(asks[0][0]) / 1e18
        spread_bps = (ask_px - bid_px) / bid_px * 1e4 if bid_px else None
        bid5 = sum(int(x[1]) / 1e18 for x in bids[:5])
        ask5 = sum(int(x[1]) / 1e18 for x in asks[:5])

    payload = {
        "ts_utc": now,
        "source": "sonde_nado_lecture_seule",
        "total_perp": len(all_syms),
        "btc_perp": {"present": bool(btc), "status": btc.get("trading_status"), "product_id": btc.get("product_id")},
        "xlm_found": xlm,
        "shx_found": shx,
        "btc_book": {"bid": bid_px, "ask": ask_px, "spread_bps": round(spread_bps, 3) if spread_bps is not None else None,
                      "bid5_btc": round(bid5, 4), "ask5_btc": round(ask5, 4)},
        "verdict": "OK" if (btc.get("trading_status") == "live" and spread_bps is not None and spread_bps < 5) else "A_SURVEILLER",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
