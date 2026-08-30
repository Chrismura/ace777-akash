#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation CORTANA — RED vs BTC/ETH (dé-corrélation) — 30/08/2026.

Souscription Christophe : « oui soumettre à cortana » (la découverte que RED est
dé-corrélé de BTC/ETH, avec le pattern horaire et le set-up). ADVISORY : Cortana
propose, ne touche à rien.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_CORTANA_RED_DECORR_20260830")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es CORTANA, l'analyste-maîtresse de la famille ACE777 (contrat : ADVISORY — "
    "tu PROPOSES, tu n'appliques JAMAIS rien ; mode appliqué seulement si justesse ≥60%). "
    "Tu connais HULK (paper dip&rip MEXC small caps), nos indices maison (poussière, murs, "
    "régimes) et le pattern V8 d'ACE. Avis franc, chiffré, GO-sized."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

CONTEXTE = """\
RED vs BTC/ETH — découverte de dé-corrélation + set-up — avis de Cortana (30/08/2026)

================
LE FAIT (nos données, jamais inventé)
================
RED = RedStone, token oracle blockchain (infra DeFi, rival Chainlink). Market cap ~44,9 M$.
Prix actuel 0.11076 (30/08 14:06Z). Portefeuille paper Hulk : seedée 10$, non tradée.
Analyse de 2238 points REDUSDT sur 3 jours (27→30/08) dans croisement_contexte.jsonl.

================
LES 2 DÉCOUVERTES À VALIDER
================
D1 — PATTERN INTRAday net (3 jours, répété) :
- CREUX moyen 14h-19h UTC, pire ~15-16h (prix moyen 0.1062-0.1068 ; min absolu 0.10200).
- PIC moyen 21h-05h UTC, meilleurs ~01h et 04h (0.1096-0.1105 ; max absolu 0.11434).
- Écart jour→nuit ~2,4-2,8% ; range 24h constaté 3,0-10,0%.
- Ultra-volatile PAR RAFALES : dd15 moyen 22,86% (max 27,8%). Régime IMPULSE concentré
  13h-17h UTC (15h=30 points, 16h=40) = c'est là que ça déprime.
- Mur bid max ~45 240$ constant, spoof faible (1,67%) → mur réel. Poussière 17,8% nuit / 20,2% jour.

D2 — DÉ-CORRÉLATION RED vs BTC/ETH (corrélations horaires des prix moyens, 3 jours) :
- RED~BTC = +0.07 ; RED~ETH = −0.01 ; BTC~ETH = +0.98 → RED quasi indépendant du marché.
- Par phase : MATIN 08-13h RED~BTC = −0.85 / RED~ETH = −0.89 (INVERSEMENT corrélé) ;
  CREUX 14-17h = +0.10 / −0.01 (dé-corrélé, creux EN SOLO) ; NUIT 21-05h = +0.60 / +0.59.
- Niveaux relatifs (100=base) : MATIN RED 100.5 vs BTC 99.9 ; CREUX RED 98.0 vs BTC 99.7
  (BTC/ETH restent stables pendant que RED plonge en solo) ; NUIT RED 100.5 vs BTC 100.1.
- Signal précurseur (divergence rejouée 14:11Z) : RED +0.14 → 🟡 léger achat, sous le seuil
  LEADER (0.15). Timing corr 0.63 lag +4h → RED SUIT le panier (pas un leader).
- Historique : RED est passé POMPE-PIÈGE (29/08, −0.15) → LEADER (29-30/08, +0.16-0.20) →
  NEUTRE/léger achat (30/08) : signal précurseur INSTABLE.

================
LE SET-UP PROPOSÉ (à évaluer)
================
Cadre famille (ULTRA+JUGE+codeur validé) : fenêtre temporelle + déclencheur de micro-
structure, JAMAIS l'heure seule.
- Entrée : fenêtre 14h-17h UTC UNIQUEMENT + poussière <15% + mur 45K testé et tenu
  + garde-fou volume 15min < 3× moyenne 24h + entrée en 3 tranches (−1/−2/−3%)
  + stop dynamique 1,5× range bougie 15min.
- Sortie : scaling out au pic de nuit 01h-05h (0.110-0.112+), reste derrière le trailing Hulk.
- Invalidation : casse < 0.103-0.104 hors fenêtre ; arrêt si frais réels > 1% (marge 2,4%).
- État : RED reste en seed, RIEN n'est câblé. Observation 7 jours avant activation.

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur D1 (pattern horaire) et D2 (dé-corrélation) : GO / GO AVEC RESERVES / NON
   + raison courte et nette. La dé-corrélation RED vs BTC/ETH (0.07 / −0.01, matin à −0.85)
   est-elle crédible ou artefact de nos 3 jours de données ?
2. Que changerait cette dé-corrélation au set-up (diversification, gestion du matin anti-
   corrélé, couplage avec le reste du portefeuille) ?
3. UNE amélioration concrète GO-sized (pas cosmétique).
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
    with open(os.path.join(OUT, "AVIS_CORTANA_RED.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AVIS CORTANA — RED vs BTC/ETH (provider {provider})\n\n{content}\n")
    print(f"[OK] CORTANA ({provider})")


if __name__ == "__main__":
    main()