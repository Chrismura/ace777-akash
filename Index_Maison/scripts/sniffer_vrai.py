#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sniffer_vrai.py — SNIFFER DU VRAI (19/08/2026).

Pour un sujet (crypto) : tire le BRUT (source primaire = marché réel CoinGecko +
onchain « poussière » live.json) et le NARRATIF (ce qu'on dit = description
projet + résumé DuckDuckGo), puis soumet les deux à la famille avec le prompt
DIVERGENCE (identity/prompts/divergence.json).

Théorie (Christophe, validée) : le narratif = « ce qu'on veut que tu saches »,
le brut = la vérité. Le signal = la DIVERGENCE entre les deux.

Usage : python3 sniffer_vrai.py [bitcoin | ethereum | ...]   (défaut: bitcoin)
Stdlib uniquement · lecture seule · réutilise recherche_web.py.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recherche_web import chercher_coin, donnees_coin, chercher_web, normaliser

INDEX = Path.home() / "ace777-test-day1" / "Index_Maison"
DIVERGENCE = INDEX / "identity" / "prompts" / "divergence.json"
LIVE = INDEX / "thermo" / "live.json"
HUB = "http://127.0.0.1:11435/v1/chat/completions"


def brut_onchain():
    """La poussière : dust, CPFP, blocs privatisés, whales (source primaire mempool)."""
    try:
        onch = json.loads(LIVE.read_text(encoding="utf-8"))["onchain"]
        return {
            "poussiere_dust": onch.get("cpfpDustDetail"),
            "poussiere_score": onch.get("cpfpDustScore"),
            "cpfp_mode": onch.get("cpfpMode"),
            "blocs_privatises_pct_fantome": onch.get("blocPrivatiseTauxFantome"),
            "blocs_caches_nb": onch.get("blocPrivatiseNbCachees"),
            "whale_dir": onch.get("whaleDir"),
            "whale_alerte": onch.get("whaleAlerteTexte"),
            "synthese": onch.get("synthèse"),
        }
    except Exception as e:
        return {"erreur": str(e)}


# Registre de la BONNE source par actif (règle « toujours chercher la source »).
CHAINE = {
    "bitcoin": "bitcoin", "btc": "bitcoin",
    "ethereum": "ethereum", "eth": "ethereum",
    "xrp": "ripple", "ripple": "ripple",
    "solana": "solana", "sol": "solana",
    "cardano": "cardano", "ada": "cardano",
    "dogecoin": "dogecoin", "doge": "dogecoin",
    "litecoin": "litecoin", "ltc": "litecoin",
}


def blockchair_stats(chain):
    """Statistiques natives d'une chaîne (blockchair, gratuit sans clé)."""
    url = "https://api.blockchair.com/%s/stats" % chain
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ACE777-sniffer/1.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=12).read().decode()).get("data", {})
        return {
            "blocs_hauteur": data.get("best_block_height") or data.get("best_ledger_height"),
            "mempool_tx": data.get("mempool_transactions"),
            "mempool_total": data.get("mempool_total"),
            "market_price_usd": data.get("market_price_usd"),
            "dominance_pct": data.get("market_dominance_percentage"),
            "dernier_bloc": data.get("best_block_time") or data.get("best_ledger_time"),
            "source": "blockchair %s (natif)" % chain,
        }
    except Exception as e:
        return {"erreur": str(e)[:60]}


def xrpscan_ledger():
    """XRP Ledger natif : dernier ledger, tx count, total coins (XRPScan, gratuit)."""
    try:
        req = urllib.request.Request("https://api.xrpscan.com/api/v1/ledger",
                                     headers={"User-Agent": "ACE777-sniffer/1.0"})
        d = json.loads(urllib.request.urlopen(req, timeout=12).read().decode())
        led = (d.get("ledgers") or [{}])[0]
        return {
            "current_ledger": d.get("current_ledger"),
            "tx_count_bloc": led.get("tx_count"),
            "total_coins": led.get("total_coins"),
            "close_time": led.get("close_time_human"),
            "source": "XRPScan (XRP Ledger natif)",
        }
    except Exception as e:
        return {"erreur": str(e)[:60]}


def brut_chaine(q):
    """La BONNE source primaire par actif."""
    chain = CHAINE.get(normaliser(q).lower())
    if chain == "bitcoin":
        return {"type": "mempool_btc", "poussiere": brut_onchain()}
    if chain == "ripple":
        return {"type": "xrp_ledger",
                "blockchair": blockchair_stats("ripple"),
                "xrpscan": xrpscan_ledger()}
    if chain:
        return {"type": "blockchair", "blockchair": blockchair_stats(chain)}
    return {"type": "aucune_source_native",
            "note": "pas de source onchain branchée pour cet actif"}


def brut_marche(q):
    """Marché réel : chiffres uniquement (pas de narratif)."""
    cid = chercher_coin(q)
    if not cid:
        return None
    c = donnees_coin(cid)
    if not c:
        return None
    return {k: c.get(k) for k in (
        "name", "symbol", "prix_usd", "market_cap_usd", "volume_24h_usd",
        "variation_24h_pct", "ath_usd", "rang_market_cap")}


def titres_news(q, n=8):
    """Titres d'actualité (Google News RSS, gratuit sans clé) = ce qu'on RACONTE en ce moment."""
    url = ("https://news.google.com/rss/search?q=%s&hl=fr&gl=FR&ceid=FR:fr"
           % urllib.parse.quote(q))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ACE777-sniffer/1.0"})
        raw = urllib.request.urlopen(req, timeout=12).read().decode("utf-8", "ignore")
        titres = re.findall(r"<title>(.*?)</title>", raw, re.DOTALL)
        titres = [re.sub(r"<[^>]+>", "", t).strip() for t in titres[1:]]
        return [t for t in titres if t][:n]
    except Exception as e:
        return ["ERR: " + str(e)[:60]]


def fear_greed():
    """Sentiment de la foule (Fear & Greed, alternative.me, gratuit sans clé)."""
    try:
        req = urllib.request.Request("https://api.alternative.me/fng/?limit=1",
                                     headers={"User-Agent": "ACE777-sniffer/1.0"})
        d = json.loads(urllib.request.urlopen(req, timeout=12).read().decode())
        data = d["data"][0]
        return {"valeur": data["value"], "sentiment": data["value_classification"]}
    except Exception as e:
        return {"erreur": str(e)[:60]}


def trending(n=6):
    """Attention de la foule (CoinGecko trending, gratuit sans clé)."""
    try:
        req = urllib.request.Request("https://api.coingecko.com/api/v3/search/trending",
                                     headers={"User-Agent": "ACE777-sniffer/1.0"})
        d = json.loads(urllib.request.urlopen(req, timeout=12).read().decode())
        return [c["item"].get("name") for c in d.get("coins", [])[:n]]
    except Exception as e:
        return ["ERR: " + str(e)[:60]]


def narratif(q, coin):
    """Ce qu'on DIT / RESSENT / RACONTE : sentiment + titres + attention (pas Wikipédia)."""
    out = {"fear_greed": fear_greed(), "titres_news": titres_news(q), "trending": trending()}
    if coin:
        out["description_projet"] = (coin.get("description") or "")[:400]
    return out


def ask_divergence(system, user):
    # Cerveau FORT sur le rôle sniffer : analyse.profonde -> NVIDIA (DeepSeek V4).
    payload = json.dumps({
        "task": "analyse.profonde",
        "model": "nvidia",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "max_tokens": 1400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=200) as r:
        d = json.loads(r.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    q = normaliser(" ".join(args)) or "bitcoin"
    prompt = json.loads(DIVERGENCE.read_text(encoding="utf-8"))["prompt"]

    print(f"[sniffer] brut marché + onchain poussière pour « {q} »…", flush=True)
    coin = donnees_coin(chercher_coin(q))
    brut = {"marche": brut_marche(q), "source_native": brut_chaine(q)}
    nar = narratif(q, coin)
    brut_txt = json.dumps(brut, ensure_ascii=False, indent=1)
    nar_txt = json.dumps(nar, ensure_ascii=False, indent=1)

    user = (f"SUJET : {q}\n\n"
            f"[BRUT]\n{brut_txt}\n\n"
            f"[NARRATIF]\n{nar_txt}\n\n"
            f"Analyse la DIVERGENCE entre le brut et le narratif.")

    print(f"[sniffer] soumission à la famille (divergence)…", flush=True)
    txt, prov = ask_divergence(prompt, user)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    out = (f"# SNIFFER DU VRAI — {q} — {now}\n"
           f"> provider : {prov}\n\n{txt}\n\n"
           f"---\n## BRUT reçu\n```json\n{brut_txt}\n```\n\n"
           f"## NARRATIF reçu\n```json\n{nar_txt}\n```\n")
    print("\n" + "=" * 70 + "\n" + out)

    dest = INDEX / f"SNIFF_{q.replace(' ', '_')}_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.md"
    dest.write_text(out, encoding="utf-8")
    print(f"[sniffer] sauvegardé : {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
