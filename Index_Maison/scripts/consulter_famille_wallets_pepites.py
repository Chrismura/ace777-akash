#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consulter_famille_wallets_pepites.py — Pépites wallets baleines BTC (24/08, Buffy).

Question posée à la famille (via le hub, même circuit que sniffer_vrai.py) :
quelles ENTITÉS / ADRESSES de baleines BTC ajouter à la surveillance pour que
l'indice reflète au mieux la DYNAMIQUE RÉELLE des portefeuilles baleines.

Contexte injecté (réel) : la base actuelle (whales.json : 4 coffres exchanges
vérifiés + seuils) + le dernier scan (whales_scan_latest.json).

Règle d'or conservée (anti-hallucination, validée 15/08) : la famille PROPOSE,
on VÉRIFIE chaque adresse (double check mempool.space) avant de la brancher.

Usage : python3 consulter_famille_wallets_pepites.py
Stdlib uniquement · 1 appel hub · écriture dans
  scripts/CONSULTATION_FAMILLE_WALLETS_PEPITES_20260824/
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1/Index_Maison")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT_DIR = Path(__file__).resolve().parent / "CONSULTATION_FAMILLE_WALLETS_PEPITES_20260824"

SYSTEM = (
    "Tu es le CHASSEUR DE PÉPITES WALLETS du projet ACE777 (surveillance baleines BTC).\n"
    "Contexte : le projet surveille des portefeuilles pour capter la DYNAMIQUE RÉELLE des "
    "baleines (accumulation / distribution / mouvements entre exchanges). Règle d'or absolue : "
    "AUCUNE adresse sans source publique vérifiable (mempool.space, clusters publics Arkham, "
    "bitinfocharts, Etherscan de l'écosystème BTC…). Tu ne proposes jamais d'adresse inventée : "
    "si tu ne connais pas d'adresse exacte pour une entité, tu dis « adresse à retrouver » et tu "
    "donnes la piste de vérification. Ta valeur : la PERTINENCE pour la dynamique baleine, pas la "
    "quantité. Tu réponds en français, format structuré, factuel."
)

USER = """Contexte RÉEL actuel (à améliorer) :

BASE ACTUELLE (whales.json — 4 adresses, double-vérifiées mempool.space) :
{base}

DERNIER SCAN (whales_scan_latest.json) :
{scan}

SEUILS ACTUELS : gros bloc >= 1000 BTC · fragmentation >= 500 BTC sur 3 blocs.

PROBLÈME : 4 adresses (surtout des coffres d'exchanges) ne reflètent pas la dynamique
réelle des portefeuilles baleines sur BTC — l'échantillon est minuscule et biaisé.

TA MISSION — PROPOSE DES PÉPITES À BRANCHER (sans créer d'infra lourde) :

1. TOP 8 entités/adresses baleines BTC à ajouter à la surveillance, classées par
   pertinence pour la DYNAMIQUE baleine (accumulation/distribution). Pour chacune :
   - nom de l'entité + type (exchange hot/cold, fonds/ETF custodian, mineur, whale historique, market maker)
   - adresse EXACTE si tu la connais (sinon « à retrouver » + piste de vérification)
   - source publique vérifiable (mempool.space / Arkham / bitinfocharts / autre)
   - POURQUOI c'est un signal de dynamique (ex : outflows massifs = distribution vers le marché)
2. LES 3 INDICATEURS de dynamique de portefeuilles baleines les plus rentables à suivre
   (ex : outflows exchange vs inflows, âge des UTXO, concentration par cohorte) — avec la
   source gratuite qui permet de les calculer sans payer (mempool.space API, blockchain.com…).
3. LE PIÈGE À ÉVITER : quelles « fausses baleines » ne PAS suivre (adresses connues pour des
   mouvements internes qui n'ont pas de sens marché).

RÈGLES :
- Factuel, pas de storytelling. Si tu n'es pas sûr d'une adresse : « à retrouver », jamais inventée.
- Priorité au RENTABLE : les 5 meilleures propositions suffisent si elles sont bonnes.
- Format : listes nettes, prêtes à être vérifiées une par une."""

def lire(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception:
        return "(absent)"

def main() -> int:
    base = lire(ROOT / "data" / "whales.json")
    scan = lire(ROOT / "data" / "whales_scan_latest.json")
    user = USER.format(base=base[:1800], scan=scan[:800])

    payload = json.dumps({
        "task": "analyse.profonde",
        "model": "nvidia",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        "max_tokens": 3000,
        "temperature": 0.2,
    }).encode()

    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print("[consultation] soumission à la famille (analyse.profonde)…", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    secs = round(time.time() - t0, 1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    rep = OUT_DIR / "REPONSE.md"
    rep.write_text(
        f"# PÉPITES WALLETS BALEINES BTC — {now}\n"
        f"> provider : {provider} · {secs}s\n\n{content}\n",
        encoding="utf-8")
    (OUT_DIR / "contexte.json").write_text(
        json.dumps({"base": base, "scan": scan, "prompt_user": user},
                   ensure_ascii=False, indent=1),
        encoding="utf-8")
    print(f"[OK] provider={provider} ({secs}s) → {rep}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
