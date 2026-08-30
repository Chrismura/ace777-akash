#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alerter_cortana_mouvements_20260830.py — ALERTE CORTANA « mouvements BTC » (2e).

Souscription Christophe : « cortana autre alerte mouvement ». Suite de la 1re
alerte (vieux BTC) : on soumet à Cortana le bilan complet des mouvements du jour
(87 344 BTC internes Binance/Bitbank/OKEx), la poussière qui a franchi le seuil
ce soir, la correction CAPITALE du label (3LYJfcf = BTCB Binance, pas IBIT/Coinbase)
et le constat structurel Coinbase (fonds éclatés, pas de gros wallet).
ADVISORY : elle propose, ne touche à rien.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_CORTANA_MOUVEMENTS_20260830")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es CORTANA, l'analyste-maîtresse de la famille ACE777 (contrat : ADVISORY — "
    "tu PROPOSES, tu n'appliques JAMAIS rien ; mode appliqué seulement si justesse ≥60%). "
    "Tu connais HULK (paper dip&rip MEXC small caps), nos indices maison (poussière, murs, "
    "régimes, indice onchain, veille baleines) et la thèse Christophe (BTC = VALEUR, socle). "
    "Avis franc, chiffré, GO-sized."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
ALERTE N°2 — BILAN DES MOUVEMENTS BTC (30/08/2026) + CORRECTION CAPITALE

================
1) LES 87 344 BTC D'AUJOURD'HUI (scan baleines 22:37Z, 15 gros blocs)
================
Tracé à la source (mempool.space, adresses étiquetées) :
- 62,6% (54 675 BTC) = Binance Hot #2 → Binance Cold #2 (11 transferts internes)
- 23,8% (20 755 BTC) = Bitbank Cold → adresse bc1q (le gros arbre vu par la poussière)
- 4,3% (3 742 BTC) = OKEx Cold → 2 adresses bc1q
- 5,3% (4 609 BTC) = Binance Cold #6 → 2 adresses
- 4,1% (3 564 BTC) = entrée vers Binance Cold #6
→ ~87% = mouvements INTERNES d'exchanges (hot→cold = ils RANGENT au froid).
→ Vue 24h : net +2 652 BTC = ACCUMULATION. Aucune destination = exchange de vente.

================
2) POUSSIÈRE (signal maison)
================
- Score passé de ~0 (06:00Z) à 5 (13:50Z) puis pic 50/50 (22:02Z, alerte émise),
  retombé à 35 (22:36Z). Cumul 48h a franchi le seuil de 1000 tx poussière.
- Carte1 (arbre de montants) déclenchée TOUTE la journée (z=3.59, max 20 755 BTC
  = le transfert Bitbank). Carte2 (CPFP complet) NON déclenchée (conf 0) →
  alerte rouge pas émise. C'est l'écho des flux d'exchange, pas un camouflage CPFP.

================
3) 🚨 CORRECTION CAPITALE (découverte du jour)
================
Notre base whales.json étiquetait 3LYJfcf…zexb comme « BlackRock IBIT Custodian
(Coinbase) » depuis le 24/08. **C'était FAUX** : c'est la **réserve BTCB de Binance**
(wrapped BTC sur BNB Chain) — preuve : tweet officiel Binance
(x.com/binance/status/1140602413243674624) + Bitcoin.com 05/07/2026 (Arkham top-12).
CORRIGÉ. Conséquence : on ne surveille en réalité AUCUNE vraie adresse Coinbase.

================
4) COINBASE — LE CONSTAT STRUCTUREL (Arkham, article officiel 19/06/2026)
================
- Coinbase détient ~970K BTC (2e entité mondiale après Satoshi) vs Binance 665K BTC.
- MAIS : Coinbase éclate ses fonds en MILLIERS de petites adresses (ségrégation
  par client, norme custody institutionnelle) — contrairement à Binance (peu de
  gros wallets identifiables). 98% des fonds clients en cold storage.
- 8 des 11 spot BTC ETF US utilisent Coinbase comme custodian (84,5% de l'AUM ETF).
- L'essentiel du BTC Coinbase est en custody pour IBIT (BlackRock).
- Arkham identifie « des milliers d'adresses Coinbase » + « Coinbase Hot Wallet ».
- Conséquence pratique : impossible de tracker Coinbase avec 2-3 adresses comme
  Binance. Notre base n'a aucune vraie adresse Coinbase (le label était faux).

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur le bilan : les 87 344 BTC internes + poussière qui monte + vieux
   wallets 2011-2014 réveillés (553 BTC, alerte n°1) — quelle est LA lecture
   synthétique du marché BTC en ce moment (accumulation ? distribution ? neutre) ?
2. COINBASE : étant donné l'éclatement structurel de ses adresses, est-il
   pertinent de vouloir la tracker adresse par adresse, ou vaut-il mieux
   surveiller autre chose (flux ETF IBIT onchain, Coinbase Prime, Whale Alert) ?
   Et comment intégrer ça SANS alourdir Hulk ?
3. UNE amélioration concrète GO-sized pour notre veille baleines (les 2 alertes
   d'aujourd'hui ont révélé : label faux + sonde aveugle aux vieux coins +
   Coinbase introuvable).
Réponds en français, format court et net, sans blabla. ADVISORY : tu ne modifies rien.
"""


def main():
    payload = {
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": SYSTEM + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1800,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=400) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    content = d["choices"][0]["message"]["content"].strip()
    provider = d.get("provider", "?")
    with open(os.path.join(OUT, "AVIS_CORTANA_MOUVEMENTS.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AVIS CORTANA — mouvements BTC + correction label (provider {provider})\n\n{content}\n")
    print(f"[OK] CORTANA ({provider})")
    print(content)


if __name__ == "__main__":
    main()
