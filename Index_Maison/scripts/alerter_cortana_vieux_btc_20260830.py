#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alerter_cortana_vieux_btc_20260830.py — ALERTE CORTANA « vieux BTC qui bougent ».

Souscription Christophe : « ah tu peux snifer des vieux btc bouje, cortana averti ».
Le sniff a détecté 553,59 BTC (40,15 M$) de wallets 2011-2014 réveillés entre le
16 et le 26/08 (Galaxy Research) + confirmation que notre sonde maison rate ce
signal. On ALERTE Cortana avec le contexte complet et on lui demande sa lecture
(ADVISORY : elle propose, ne touche à rien).
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_CORTANA_VIEUX_BTC_20260830")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es CORTANA, l'analyste-maîtresse de la famille ACE777 (contrat : ADVISORY — "
    "tu PROPOSES, tu n'appliques JAMAIS rien ; mode appliqué seulement si justesse ≥60%). "
    "Tu connais HULK (paper dip&rip MEXC small caps), nos indices maison (poussière, murs, "
    "régimes, indice onchain) et la thèse Christophe (BTC = l'arbre qui cache la forêt, "
    "or/Bâle 3, 2e degré). Avis franc, chiffré, GO-sized."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
ALERTE — VIEUX BTC QUI BOUGENT (réveil de baleines dormantes) — 30/08/2026

================
CE QU'ON A DÉTECTÉ (brut, jamais inventé)
================
Entre le 16 et le 26/08, SIX wallets BTC dormants depuis 2011-2014 ont transféré
553,59 BTC ≈ 40,15 M$ (données Galaxy Research, recoupées crypto.news / CoinDesk /
KuCoin / CoinMarketCap) :

| Date | Bloc | BTC | Dormance | Destination |
|---|---|---|---|---|
| 16/08 | 962770 | 8,54 | depuis 13/06/2011 | adresse sans label |
| 18/08 | — | 212,00 | depuis 10/08/2012 | label « Noah Doe #1396 · Salomon Client Dusted » (procès NY) |
| 18/08 | — | 10,74 | depuis 17/06/2011 | sans label |
| 22/08 | 963519 | 132,31 (3 adresses 2011) | ~15 ans | sans label exchange |
| 22/08 | — | 150,00 | depuis 26/12/2014 | label « Noah Doe #1680 » (procès NY) |
| 26/08 | 964127 | 40,00 | depuis 28/05/2012 | Boerse Stuttgart Digital (custody allemand) |

FAITS CLÉS :
- 5/6 transferts → adresses SANS lien exchange : aucune preuve onchain de vente.
- 1 seul vers entité connue (Boerse Stuttgart Digital = custody, pas exchange spot).
- Le 20/08 : 28 wallets dormants → 1 314 BTC (94 M$), dont 1 214 BTC d'adresses 2014
  (21 tx de 50 BTC exactement, même format → 1-2 holders, réorganisation).
- Contexte : 5 908 BTC (383 M$) bougés en juillet après 8,5 ans de dormance.
- ACTIVITÉ DORMANTE AU PLUS BAS DEPUIS 2022 (Galaxy) → événement ponctuel, pas une vague.

================
LES 2 EXPLICATIONS NON-MARKET À GARDER EN TÊTE
================
1) PROCÈS NY « Noah Doe » : plainte sur 39 069 adresses dormantes (~3,7 M BTC visés,
   y compris wallets Satoshi et Mt.Gox) en « abandoned property ». Les plaignants
   envoient des tx dust de notification (labels « Salomon-dusted »). Les adresses qui
   BOUGENT sont retirées de la plainte (44 wallets déjà retirés en juillet).
   → Les holders bougent pour SORTIR de la plainte, pas pour vendre.
2) SÉCURITÉ Coldcard : faille firmware (mars 2021) → 4 vagues de drain ≈ 1 816 BTC
   retirés de 5 294 adresses depuis fin juillet. Vieux holders peuvent bouger par
   sécurité (migration de clés).

================
SCAN DIRECT (mempool.space, 30/08 22:07Z, 4 derniers blocs, seuil 50 BTC)
================
35 grosses tx · 0 vieux coin ≥ 2 ans dans la dernière heure. Les gros mouvements
récents (2 440 BTC ×3, 835, 657 ×4…) sont des flux d'exchange frais.
→ FAILLE DE NOTRE SONDE : surveiller_whales.py ne surveille que les adresses
étiquetées (Binance Cold/Hot, Bitbank) → il RATE les vieux coins vers adresses muettes.

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur l'événement : ce réveil de 553 BTC (2011-2014) est-il un signal de
   marché (distribution) ou de la réorganisation de holders (procès NY + sécurité
   Coldcard) ? Argumente avec les faits ci-dessus.
2. QUELLE LECTURE pour HULK / notre portefeuille : est-ce que ça change quelque
   chose à la thèse BTC (VALEUR, socle) et au set-up des positions ?
3. UNE amélioration concrète GO-sized : comment brancher la détection « vieux coins »
   dans notre veille (proposition de sonde, seuils, croisement) SANS alourdir Hulk ?
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
    with open(os.path.join(OUT, "AVIS_CORTANA_VIEUX_BTC.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AVIS CORTANA — vieux BTC qui bougent (provider {provider})\n\n{content}\n")
    print(f"[OK] CORTANA ({provider})")
    print(content)


if __name__ == "__main__":
    main()
