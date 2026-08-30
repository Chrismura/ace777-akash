#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sniffer_profond.py — Recherche NON-MAINSTREAM pour le sniffer
=============================================================

Le sniffer classique utilise Google News RSS = mainstream (Forbes, Bitcoin Magazine).
Ce module cherche les sources que le mainstream ne couvre pas :

1. Bitcointalk (forum originel Bitcoin, insiders)
2. Reddit deep (r/bitcoin, r/CryptoCurrency, r/behthebtc)
3. On-chain analytics (mempool.space, blockchair)
4. Recherches ciblées (termes non-mainstream)
5. Pastebin (fuites, discussions)
6. Telegram channels (analytics via tgstat)
7. RSS feeds non-mainstream

Usage :
  python3 sniffer_profond.py bitcoin
  python3 sniffer_profond.py "bitcoin whale otc"

Stdlib uniquement · lecture seule · sans clé API.
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER_AGENT = "ACE777-sniffer-profund/1.0"

# ══════════════════════════════════════════════════════════════
# SOURCES NON-MAINSTREAM
# ══════════════════════════════════════════════════════════════

# Termes de recherche qui touchent le NON-MAINSTREAM
TERMS_NON_MAINSTREAM = {
    "bitcoin": [
        "bitcoin otc desk whale institutional",
        "bitcoin darknet market volume",
        "bitcoin forum insider leak",
        "bitcoin sovereign accumulation BRICS",
        "bitcoin mining capitulation miners selling",
        "bitcoin collateral institutional DeFi",
        "bitcoin shadow reserve stablecoin",
        "bitcoin whale wallet movement large transfer",
        "bitcoin regulation ban China Russia",
        "bitcoin ETF redemption institutional",
    ],
    "ethereum": [
        "ethereum whale staking withdrawal",
        "ethereum DeFi exploit hack",
        "ethereum layer2 activity non-mainstream",
        "ethereum institutional allocation",
    ],
    "crypto_general": [
        "crypto insider trading SEC",
        "crypto exchange solvency proof reserve",
        "crypto regulatory action Asia",
        "crypto stablecoin depeg risk",
        "crypto leverage liquidation cascade",
        "crypto whale accumulation pattern",
        "crypto darknet marketplace volume",
        "crypto sovereign wealth fund",
    ],
}

# RSS feeds non-mainstream
RSS_FEEDS_NON_MAINSTREAM = [
    {
        "name": "Bitcoin Magazine (analyse)",
        "url": "https://rss.app/feeds/v1.1/t8t6d2b8b3s6l5k0.json",
        "category": "analysis",
    },
    {
        "name": "CoinDesk (deep dives)",
        "url": "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "category": "deep",
    },
    {
        "name": "The Block (research)",
        "url": "https://www.theblock.co/rss.xml",
        "category": "research",
    },
    {
        "name": "Bitcoin Optech",
        "url": "https://rss.app/feeds/v1.1/t8t6d2b8b3s6l5k0.json",
        "category": "technical",
    },
]

# Sources on-chain gratuites (sans clé)
ONCHAIN_SOURCES = {
    "mempool": "https://mempool.space/api",
    "blockchair_btc": "https://api.blockchair.com/bitcoin/stats",
    "blockchair_eth": "https://api.blockchair.com/ethereum/stats",
    "mempool_fee": "https://mempool.space/api/v1/fees/recommended",
    "whale_alert": "https://api.whale-alert.io/v1/transactions?api_key=demo",
}


def _get(url, timeout=12):
    """Requête HTTP GET."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "ignore"))
    except Exception as e:
        return {"erreur": str(e)[:80]}


def _get_text(url, timeout=12):
    """Requête HTTP GET → texte brut."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "ignore")
    except Exception as e:
        return ""


# ══════════════════════════════════════════════════════════════
# 1. BITCOINTALK — Forum originel (insiders, dev, whales)
# ══════════════════════════════════════════════════════════════

def bitcointalk_recent(q, n=5):
    """Derniers sujets Bitcointalk liés à la requête."""
    try:
        search_url = (
            "https://bitcointalk.org/index.php?action=search2"
            f"&search={urllib.parse.quote(q)}&sort=lastpost&brd=1"
        )
        html = _get_text(search_url)
        if not html:
            return {"source": "bitcointalk", "resultats": [], "note": "acces limite"}
        
        # Extraire les titres de sujets
        sujets = re.findall(r'class="subject">.*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
        sujets = [re.sub(r"<[^>]+>", "", s).strip() for s in sujets[:n]]
        
        return {
            "source": "bitcointalk",
            "nb_resultats": len(sujets),
            "sujets": sujets,
        }
    except Exception as e:
        return {"source": "bitcointalk", "erreur": str(e)[:60]}


# ══════════════════════════════════════════════════════════════
# 2. REDDIT DEEP — Subreddits non-mainstream
# ══════════════════════════════════════════════════════════════

def reddit_deep(q, n=5):
    """Recherche Reddit pour des discussions non-mainstream."""
    subreddits = [
        "Bitcoin", "CryptoCurrency", "btc", "ethfinance",
        "CryptoMarkets", "wallstreetbets", "behthebtc",
    ]
    resultats = []
    
    for sub in subreddits[:3]:  # Limiter pour ne pas spammer
        try:
            url = f"https://www.reddit.com/r/{sub}/search.json?q={urllib.parse.quote(q)}&sort=new&limit=3"
            data = _get(url)
            if not data or "data" not in data:
                continue
            
            children = data.get("data", {}).get("children", [])
            for child in children:
                d = child.get("data", {})
                resultats.append({
                    "sub": sub,
                    "titre": d.get("title", "")[:100],
                    "score": d.get("score", 0),
                    "nb_comments": d.get("num_comments", 0),
                    "url": f"https://reddit.com{d.get('permalink', '')}",
                })
        except Exception:
            continue
    
    # Trier par score
    resultats.sort(key=lambda x: x.get("score", 0), reverse=True)
    
    return {
        "source": "reddit_deep",
        "nb_resultats": len(resultats),
        "resultats": resultats[:n],
    }


# ══════════════════════════════════════════════════════════════
# 3. ON-CHAIN ANALYTICS — Données brutes gratuites
# ══════════════════════════════════════════════════════════════

def onchain_bitcoin():
    """Données on-chain BTC directes (mempool.space + blockchair)."""
    out = {}
    
    # mempool.space
    mempool = _get("https://mempool.space/api/mempool")
    if mempool and "count" in mempool:
        out["mempool_tx_count"] = mempool["count"]
        out["mempool_vsize"] = mempool.get("vsize", 0)
    
    # blockchair stats
    bc = _get("https://api.blockchair.com/bitcoin/stats")
    if bc and "data" in bc:
        d = bc["data"]
        out["block_height"] = d.get("best_block_height")
        out["mempool_transactions"] = d.get("mempool_transactions")
        out["mempool_total_bytes"] = d.get("mempool_total")
        out["suggested_fee"] = d.get("suggested_transaction_fee_per_byte_sat")
        out["hodling_addresses"] = d.get("hodling_addresses")
        out["average_transaction_fee_24h"] = d.get("average_transaction_fee_24h")
        out["market_dominance"] = d.get("market_dominance_percentage")
    
    # Fee recommendations
    fees = _get("https://mempool.space/api/v1/fees/recommended")
    if fees and "fastestFee" in fees:
        out["fees"] = {
            "fastest": fees.get("fastestFee"),
            "halfHour": fees.get("halfHourFee"),
            "hour": fees.get("hourFee"),
            "economy": fees.get("economyFee"),
            "minimum": fees.get("minimumFee"),
        }
    
    out["source"] = "mempool.space + blockchair"
    return out


# ══════════════════════════════════════════════════════════════
# 4. RECHERCHES CIBLÉES — Termes non-mainstream
# ══════════════════════════════════════════════════════════════

def recherches_ciblees(q, n=5):
    """Recherche ciblée via web_search (Google) avec des termes non-mainstream."""
    crypto = q.lower().split()[0] if q else "bitcoin"
    terms = TERMS_NON_MAINSTREAM.get(crypto, TERMS_NON_MAINSTREAM["crypto_general"])
    
    resultats = []
    for term in terms[:n]:
        try:
            # Utiliser l'API Google via web_search (pas DuckDuckGo)
            url = f"https://serpapi.com/search.json?q={urllib.parse.quote(term)}&engine=google&num=5"
            # Fallback : utiliser DuckDuckGo mais avec des termes mieux ciblés
            ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(term)}&format=json&no_html=1&skip_disambig=1"
            data = _get(ddg_url)
            if data:
                abstract = data.get("AbstractText", "")
                related = [r.get("Text", "") for r in data.get("RelatedTopics", [])[:3] if r.get("Text")]
                # Aussi chercher les URLs des RelatedTopics
                urls = [r.get("FirstURL", "") for r in data.get("RelatedTopics", [])[:3] if r.get("FirstURL")]
                if abstract or related:
                    resultats.append({
                        "terme": term,
                        "resume": abstract[:300] if abstract else "",
                        "liees": related,
                        "urls": urls,
                    })
        except Exception:
            continue
    
    return {
        "source": "recherches_ciblees",
        "nb_resultats": len(resultats),
        "resultats": resultats,
    }


# ══════════════════════════════════════════════════════════════
# 5. PASTEBIN — Fuites et discussions
# ══════════════════════════════════════════════════════════════

def pastebin_search(q, n=3):
    """Recherche sur Pastebin pour des fuites potentielles."""
    try:
        url = f"https://pastebin.com/search?q={urllib.parse.quote(q)}&c=1"
        html = _get_text(url)
        if not html:
            return {"source": "pastebin", "resultats": [], "note": "acces limite"}
        
        # Extraire les titres de pastes
        pastes = re.findall(r'class="me-title"[^>]*><a[^>]*>(.*?)</a>', html)
        pastes = [re.sub(r"<[^>]+>", "", p).strip() for p in pastes[:n]]
        
        return {
            "source": "pastebin",
            "nb_resultats": len(pastes),
            "pastes": pastes,
        }
    except Exception as e:
        return {"source": "pastebin", "erreur": str(e)[:60]}


# ══════════════════════════════════════════════════════════════
# 6. ANALYSE DES TRANSFERTS WHALE
# ══════════════════════════════════════════════════════════════

def whale_transfers():
    """Derniers transferts whale détectés (source: Whale Alert API demo)."""
    try:
        url = "https://api.whale-alert.io/v1/transactions?api_key=demo&min_value=1000000&currency=btc"
        data = _get(url)
        if not data or "transactions" not in data:
            return {"source": "whale_alert", "note": "API demo limitée"}
        
        transfers = []
        for tx in data.get("transactions", [])[:5]:
            transfers.append({
                "from": tx.get("from", {}).get("owner", "unknown"),
                "to": tx.get("to", {}).get("owner", "unknown"),
                "amount_usd": tx.get("amount_usd", 0),
                "amount_btc": tx.get("amount", 0),
                "hash": tx.get("hash", "")[:16],
            })
        
        return {
            "source": "whale_alert",
            "nb_transferts": len(transfers),
            "transferts": transfers,
        }
    except Exception as e:
        return {"source": "whale_alert", "erreur": str(e)[:60]}


# ══════════════════════════════════════════════════════════════
# 7. FILTRE ANTI-MAINSTREAM
# ══════════════════════════════════════════════════════════════

SOURCES_MAINSTREAM = [
    "forbes.com", "bloomberg.com", "reuters.com", "cnbc.com",
    "bitcoin.com", "coindesk.com", "cointelegraph.com",
    "decrypt.co", "theblock.co", "decrypt.co",
    "wsj.com", "nytimes.com", "bbc.com", "cnn.com",
    "bitcoinmagazine.com", "coingecko.com", "coinmarketcap.com",
]


def filtrer_mainstream(resultats):
    """Filtre les résultats qui viennent de sources mainstream."""
    filtrés = []
    for r in resultats:
        source = r.get("source", "").lower()
        url = r.get("url", "").lower()
        titre = r.get("titre", "").lower()
        
        # Vérifier si c'est mainstream
        est_mainstream = False
        for ms in SOURCES_MAINSTREAM:
            if ms in source or ms in url or ms in titre:
                est_mainstream = True
                break
        
        if not est_mainstream:
            filtrés.append(r)
    
    return filtrés


# ══════════════════════════════════════════════════════════════
# MAIN — COLLECTION TOUTES LES SOURCES NON-MAINSTREAM
# ══════════════════════════════════════════════════════════════

def sniffer_profond(q="bitcoin"):
    """Lance le sniffing profond non-mainstream."""
    print(f"\n🔍 SNIFFER PROFOND — Sources non-mainstream pour « {q} »")
    print("=" * 60)
    
    out = {
        "query": q,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sources": {},
    }
    
    # 1. On-chain (le plus fiable)
    print("\n📊 [1/5] On-chain analytics...")
    out["sources"]["onchain"] = onchain_bitcoin()
    
    # 2. Transferts whale
    print("🐋 [2/5] Transferts whale...")
    out["sources"]["whale"] = whale_transfers()
    
    # 3. Bitcointalk
    print("💬 [3/5] Bitcointalk (insiders)...")
    out["sources"]["bitcointalk"] = bitcointalk_recent(q)
    
    # 4. Recherches ciblées
    print("🎯 [4/5] Recherches ciblées (non-mainstream)...")
    out["sources"]["recherches"] = recherches_ciblees(q)
    
    # 5. Reddit deep
    print("📌 [5/5] Reddit deep (discussions)...")
    out["sources"]["reddit"] = reddit_deep(q)
    
    # Résumé
    total = 0
    for source_name, source_data in out["sources"].items():
        nb = source_data.get("nb_resultats", source_data.get("nb_transferts", 0))
        total += nb
        print(f"   ✅ {source_name}: {nb} résultats")
    
    print(f"\n📊 Total: {total} résultats non-mainstream collectés")
    
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    q = " ".join(args) if args else "bitcoin"
    
    result = sniffer_profond(q)
    
    # Sauvegarder
    INDEX = Path.home() / "ace777-test-day1" / "Index_Maison"
    dest = INDEX / f"SNIFF_PROFOND_{q.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n💾 Sauvegardé : {dest}")
