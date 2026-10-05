#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""generer_fiches_projet.py — Fiche ÉTUDE PROJET par actif (06/09/2026).

Complète la FICHE_SETUP (technique) : ici on étudie le PROJET derrière le token.
Sources : verdicts deepdive famille (paires_croisement.json), thèses enregistrées
(CONNAISSANCE_PROJETS.json), données live DefiLlama (TVL) + CoinGecko (market cap).

Deuxième fiche par actif (consigne Christophe 06/09) :
- FICHE_SETUP  = technique (fenêtres, déclencheurs, rôle dans le groupe)
- FICHE_PROJET = étude projet (catégorie, thèse, verdict famille, données live, sources de vérité)

Usage : python3 scripts/generer_fiches_projet.py [PAIRE1 ...]   (défaut : CORE-20)
"""
import datetime
import json
import os
import sys
import urllib.parse
import urllib.request

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
STRAT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "strategie")
CRYPTO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                      "Index_Maison", "OUTBOX_OBSIDIAN", "Crypto_Projet")
os.makedirs(CRYPTO, exist_ok=True)

CORE_PAIRS = [
    "BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT",
    "WUSDT", "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT",
    "TELUSDT", "CHIPUSDT", "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT",
    "RWAUSDT", "MNSRYUSDT",
]

NOMS = {
    "BTCUSDT": "Bitcoin", "ETHUSDT": "Ethereum", "XRPUSDT": "XRP (Ripple)",
    "HBARUSDT": "Hedera", "CCUSDT": "CC (Canton Network)", "REDUSDT": "RedStone (oracle)",
    "CHIPUSDT": "CHIP (USD.AI, compute)", "EDELUSDT": "EDEL", "PYTHUSDT": "Pyth (oracle)",
    "RIZEUSDT": "RIZE (T-RIZE, RWA)", "ZBCNUSDT": "Zebec", "WUSDT": "W (Wormhole)",
    "BIOUSDT": "BIO (Bioprotocol)", "KITEUSDT": "KITE", "TELUSDT": "Telos",
    "RWAINCUSDT": "RWA Inc.", "RWAUSDT": "Allo (RWA, ex-Xend)", "QNTUSDT": "Quant",
    "FLUIDUSDT": "Fluid (Instadapp)", "MNSRYUSDT": "Mansory Token",
    # 05/10/2026 (GO Christophe) : paires en OBSERVATION (cueillette avant intégration)
    "IOTAUSDT": "IOTA", "LAUSDT": "Lagrange",
    "WAXLUSDT": "Axelar (WAXL, wrapped — AXLUSDT absent de MEXC)",
}

CATEGORIE = {
    "BTCUSDT": "Socle / réserve de valeur", "ETHUSDT": "Socle / smart contracts",
    "XRPUSDT": "Paiements / majeure manipulée", "HBARUSDT": "Socle institutionnel L1",
    "CCUSDT": "RWA / privacy institutionnel", "REDUSDT": "Oracle",
    "CHIPUSDT": "RWA compute (USD.AI)", "EDELUSDT": "Agent IA (loterie)",
    "PYTHUSDT": "Oracle (moteur portefeuille)", "RIZEUSDT": "RWA institutionnel (T-RIZE)",
    "ZBCNUSDT": "Paiements / streaming", "WUSDT": "Interoperabilité (bridge)",
    "BIOUSDT": "DeSci / biotech", "KITEUSDT": "à vérifier (exclue prudence)",
    "TELUSDT": "L1 (exclue prudence)", "RWAINCUSDT": "RWA Inc. (exclue prudence)",
    "RWAUSDT": "RWA (Xend rebrand — NON famille)", "QNTUSDT": "Interoperabilité institutionnelle (CBDC/ISO 20022)",
    "FLUIDUSDT": "DeFi (hub unifié Instadapp)", "MNSRYUSDT": "Memecoin (usurpation — NON famille)",
    "IOTAUSDT": "L1 / IoT (ancien projet réactivé)",
    "LAUSDT": "Infrastructure crypto (Lagrange — ZK/provisioning)",
    "WAXLUSDT": "Interop (Axelar wrapped — en observation, liquidité faible)",
}

# Slugs DefiLlama (repris de digest_watch.py) + CoinGecko ids pour les majeures
DEFILLAMA_SLUGS = {
    "W": "wormhole", "ZBCN": "zebec-protocol", "RED": "redstone-oracles",
    "HBAR": "hedera", "XRP": "ripple", "PYTH": "pyth-network", "BIO": "bioprotocol",
    "QNT": "quant-network", "FLUID": "fluid",
}
COINGECKO_IDS = {
    "BTC": "bitcoin", "ETH": "ethereum", "XRP": "ripple", "HBAR": "hedera",
    "W": "wormhole", "PYTH": "pyth-network", "QNT": "quant-network", "ZBCN": "zebec-network",
    "RED": "redstone-oracles", "BIO": "bio-protocol", "FLUID": "fluid-2",
    "IOTA": "iota", "LA": "lagrange", "WAXL": "axelar",
}


def gj(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def tvl_defillama(pair):
    slug = DEFILLAMA_SLUGS.get(pair.replace("USDT", ""))
    if not slug:
        return None, "pas de mapping DefiLlama"
    try:
        j = gj(f"https://api.llama.fi/protocol/{slug}")
        tvl = j.get("currentChainTvls") or j.get("tvl")
        if isinstance(tvl, dict):
            v = sum(float(x) for x in tvl.values() if isinstance(x, (int, float)))
        elif isinstance(tvl, (int, float)):
            v = float(tvl)
        else:
            v = None
        return v, "ok"
    except Exception as e:
        return None, f"miss ({type(e).__name__})"


def coingecko(pair):
    cid = COINGECKO_IDS.get(pair.replace("USDT", ""))
    if not cid:
        return None
    try:
        j = gj(f"https://api.coingecko.com/api/v3/coins/{cid}"
               f"?localization=false&tickers=false&community_data=false&developer_data=false")
        md = j.get("market_data") or {}
        return {"mcap_usd": md.get("market_cap", {}).get("usd"),
                "mcap_rank": md.get("market_cap_rank"),
                "fdv_usd": md.get("fully_diluted_valuation", {}).get("usd"),
                "circ_vs_max": (
                    (md.get("circulating_supply") or 0) / (md.get("total_supply") or 1) * 100
                    if md.get("total_supply") else None)}
    except Exception:
        return None


def charger_statuts():
    fn = os.path.join(STRAT, "paires_croisement.json")
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for grp, label in (("deepdive_validees", "DEEPDIVE VALIDÉE"),
                       ("observation_setup", "OBSERVATION"),
                       ("exclues_prudence", "EXCLUE (prudence)"),
                       ("ejectees", "ÉJECTÉE")):
        for pair, note in (d.get(grp) or {}).items():
            out[pair] = (label, note or "")
    return out


def charger_these(pair):
    fn = os.path.join(STRAT, "CONNAISSANCE_PROJETS.json")
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        return None
    proj = (d.get("projets") or {}).get(pair)
    if not proj:
        return None
    verif = proj.get("statut_verification") or {}
    return {
        "these": proj.get("these"),
        "classe_hulk": proj.get("classe_hulk"),
        "horizon": proj.get("horizon_bag"),
        "capital": proj.get("capital_alloue_max"),
        "verdict": verif.get("verdict"), "score": verif.get("score"), "reserve": verif.get("reserve"),
        "lecons": [l.get("texte") for l in (proj.get("lecons") or [])][:4],
        "faits": [f.get("texte") for f in (proj.get("faits") or [])][:4],
        "updated": proj.get("updated"),
    }


def render(pair, date_str, date_tag, statut, these, tvl, tvl_note, cg):
    nom = NOMS.get(pair, pair.replace("USDT", ""))
    cat = CATEGORIE.get(pair, "—")
    st = statut[0] if statut else "—"
    note = statut[1] if statut else ""

    th = these or {}
    bloc_these = ""
    if th:
        lecons = "\n".join(f"- {x}" for x in (th.get("lecons") or [])) or "- (aucune leçon enregistrée)"
        faits = "\n".join(f"- {x}" for x in (th.get("faits") or [])) or "- (aucun fait vérifié)"
        bloc_these = f"""### Thèse enregistrée ({(th.get('updated') or '?')[:10]})
{th.get('these') or '—'}

- **Classe Hulk** : {th.get('classe_hulk') or '—'} · **Horizon** : {th.get('horizon') or '—'} · **Capital max** : {th.get('capital') or '—'}
- **Vérification** : {th.get('verdict') or '—'} (score {th.get('score') or '—'}) — {th.get('reserve') or ''}

**Faits vérifiés**
{faits}

**Leçons gravées**
{lecons}
"""
    else:
        bloc_these = "_Pas de thèse enregistrée dans CONNAISSANCE_PROJETS.json — à construire au prochain deepdive._\n"

    mcap = f"{cg['mcap_usd']:,.0f}$ (rang {cg['mcap_rank']})" if cg and cg.get("mcap_usd") else "—"
    fdv = f"{cg['fdv_usd']:,.0f}$" if cg and cg.get("fdv_usd") else "—"
    circ = f"{cg['circ_vs_max']:.0f}%" if cg and cg.get("circ_vs_max") else "—"
    tvl_txt = f"{tvl:,.0f}$ ({tvl_note})" if tvl else f"— ({tvl_note})"

    return f"""# 🏗️ FICHE ÉTUDE PROJET — {pair} ({nom}) — {date_str}

> **2ᵉ fiche de l'actif** (consigne Christophe 06/09) : ici on étudie le PROJET, pas le chart.
> Compagne de : `FICHE_SETUP_{pair}_{date_tag}.md` (technique — fenêtres, déclencheurs, rôle dans le groupe).

---

## 🏛️ STATUT FAMILLE (paires_croisement.json)

**{st}** — {note or "pas de statut enregistré"}

---

## 🧭 CATÉGORIE & DONNÉES LIVE

| Élément | Valeur | Source |
|---|---|---|
| **Catégorie** | {cat} | classification maison |
| **Market cap** | {mcap} | CoinGecko (live) |
| **FDV** | {fdv} | CoinGecko |
| **Supply en circulation** | {circ} | CoinGecko |
| **TVL DeFi** | {tvl_txt} | DefiLlama |

---

## 📖 ÉTUDE PROJET

{bloc_these}
## 🔎 SOURCES DE VÉRITÉ (pour check-up de temps en temps)

- DefiLlama : https://defillama.com/protocol/{DEFILLAMA_SLUGS.get(pair.replace('USDT','')) or '—'}
- CoinGecko : https://www.coingecko.com/en/coins/{COINGECKO_IDS.get(pair.replace('USDT','')) or '—'}
- MEXC : https://www.mexc.com/exchange/{pair.replace('USDT','_USDT')}
- Annonces MEXC (delisting) : https://www.mexc.com/support/categories/6001c5f6dc1c9c3fd0b8f4af
- Dossier deepdive : voir `Index_Maison` (recherche `deepdive {pair.replace('USDT','')}`)

**Check-up recommandé** : toutes les 2-4 semaines ou à chaque alerte delisting/news —
vérifier TVL, adoption annoncée (communiqués officiels, pas marketing), supply, annonces MEXC.

---

## ⏱️ ÉTAT ACTUEL
- Cette fiche est **l'étude projet** : elle évolue aux deepdives et aux check-ups, pas au rythme du chart.
- Verdicts NON famille = **jamais de position** ; prix croisé SEUL pour l'observation.

## Archives
- Version 06/09/2026 (1ʳᵉ génération des fiches projet — consigne Christophe).
- Thèses : `hulk-mexc/strategie/CONNAISSANCE_PROJETS.json`
"""


def main():
    today = datetime.date.today()
    date_str = today.strftime("%d/%m/%Y")
    date_tag = today.strftime("%Y%m%d")
    statuts = charger_statuts()
    pairs = sys.argv[1:] or CORE_PAIRS
    n = 0
    for pair in pairs:
        statut = statuts.get(pair)
        these = charger_these(pair)
        tvl, tvl_note = tvl_defillama(pair)
        cg = coingecko(pair)
        fn = os.path.join(CRYPTO, f"FICHE_PROJET_{pair}_{date_tag}.md")
        with open(fn, "w", encoding="utf-8") as fh:
            fh.write(render(pair, date_str, date_tag, statut, these, tvl, tvl_note, cg))
        print(f"[OK] {pair}: TVL {tvl or '—'} · mcap {(cg or {}).get('mcap_usd') or '—'} · {statut[0] if statut else '—'}")
        n += 1
    print(f"== {n} fiches projet générées dans Crypto_Projet/")


if __name__ == "__main__":
    main()
