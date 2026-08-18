#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recherche_web.py — Recherche web à la demande pour Cortana (ACE777)
====================================================================
Rôle : chercher sur le net une crypto (ou un sujet) à la demande de Christophe.
Gratuit, SANS clé, SANS dépendance (stdlib uniquement) — respecte C5/C9.

Sources :
  1. CoinGecko  : données de marché (prix, cap, volume, ATH, variation 24h)
                  + description du projet + catégories (relations avec de gros
                  acteurs : portfolios, écosystèmes) + liens (site/twitter/github).
  2. DuckDuckGo : résumé web général (instant answer, type Wikipedia).

Sortie : JSON structuré {query, coin, web} consommé par le bridge, qui le passe
au hub (task cortana.analyse) pour la synthèse d'analyse.

Usage :
  python3 recherche_web.py bitcoin
  python3 recherche_web.py "ethereum"
Lecture seule — jamais d'ordre.
"""

import json
import re
import sys
import urllib.parse
import urllib.request

USER_AGENT = "ACE777-recherche/1.0"
CG_SEARCH = "https://api.coingecko.com/api/v3/search?query={q}"
CG_COIN = ("https://api.coingecko.com/api/v3/coins/{cid}"
           "?localization=false&tickers=false&community_data=false&developer_data=false")
DDG = "https://api.duckduckgo.com/?q={q}&format=json&no_html=1&skip_disambig=1"


def _get(url, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:
        return None


def normaliser(q):
    q = (q or "").strip()
    q = re.sub(r"[?!.]+$", "", q).strip()
    return q


def chercher_coin(q):
    """CoinGecko : renvoie l'id du coin le mieux classé (market_cap_rank le plus petit)."""
    d = _get(CG_SEARCH.format(q=urllib.parse.quote(q)))
    if not d or not isinstance(d, dict):
        return None
    coins = d.get("coins") or []
    if not coins:
        return None

    def rank(c):
        r = c.get("market_cap_rank")
        return r if isinstance(r, int) else 10 ** 9
    top = sorted(coins, key=rank)[0]
    return top.get("id")


def donnees_coin(cid):
    d = _get(CG_COIN.format(cid=urllib.parse.quote(cid)))
    if not d or not isinstance(d, dict):
        return None
    md = d.get("market_data") or {}
    liens = d.get("links") or {}
    home = (liens.get("homepage") or [])
    repos = (liens.get("repos_url") or {}).get("github") or []
    desc = (d.get("description") or {}).get("fr") or (d.get("description") or {}).get("en") or ""
    desc = re.sub(r"<[^>]+>", " ", desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    return {
        "id": d.get("id"),
        "name": d.get("name"),
        "symbol": (d.get("symbol") or "").upper(),
        "prix_usd": (md.get("current_price") or {}).get("usd"),
        "market_cap_usd": (md.get("market_cap") or {}).get("usd"),
        "volume_24h_usd": (md.get("total_volume") or {}).get("usd"),
        "variation_24h_pct": md.get("price_change_percentage_24h"),
        "ath_usd": (md.get("ath") or {}).get("usd"),
        "ath_change_pct": md.get("ath_change_percentage"),
        "rang_market_cap": d.get("market_cap_rank"),
        "description": desc[:900],
        "categories": (d.get("categories") or [])[:10],
        "liens": {
            "homepage": home[0] if home else None,
            "twitter": liens.get("twitter_screen_name"),
            "github": repos[:3],
        },
    }


def chercher_web(q):
    d = _get(DDG.format(q=urllib.parse.quote(q)))
    if not d or not isinstance(d, dict):
        return None
    out = {
        "resume": (d.get("AbstractText") or "").strip()[:600],
        "source": d.get("AbstractURL"),
        "titre": d.get("Heading"),
        "sujets_lies": [],
    }
    for t in (d.get("RelatedTopics") or []):
        if isinstance(t, dict) and t.get("Text"):
            out["sujets_lies"].append(t["Text"][:120])
            if len(out["sujets_lies"]) >= 5:
                break
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(json.dumps({"erreur": "requête vide"}, ensure_ascii=False))
        return 2
    q = normaliser(" ".join(args))
    coin_id = chercher_coin(q)
    coin = donnees_coin(coin_id) if coin_id else None
    web = chercher_web(q)
    out = {"query": q, "coin": coin, "web": web}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
