#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""price_source.py — SOURCE DE PRIX BTC (juge indépendant du verdicteur).

prix_btc() → (float | None, source : str) — MEXC public sans clé, repli
CoinGecko, fail-open (None si tout échoue — le verdicteur saute le passage).
Jamais de clé, jamais d'ordre, lecture seule.
"""
import json
import urllib.request

UA = {"User-Agent": "ACE777-price/1.0"}


def _mexc():
    with urllib.request.urlopen("https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT",
                                timeout=5) as r:
        return float(json.loads(r.read().decode())["price"])


def _coingecko():
    req = urllib.request.Request("https://api.coingecko.com/api/v3/simple/price"
                                 "?ids=bitcoin&vs_currencies=usd", headers=UA)
    with urllib.request.urlopen(req, timeout=5) as r:
        return float(json.loads(r.read().decode())["bitcoin"]["usd"])


def prix_btc():
    for fn, nom in ((_mexc, "mexc"), (_coingecko, "coingecko")):
        try:
            p = fn()
            if p and p > 0:
                return p, nom
        except Exception:
            continue
    return None, "indisponible"


if __name__ == "__main__":
    p, s = prix_btc()
    print(f"{p} ({s})")
