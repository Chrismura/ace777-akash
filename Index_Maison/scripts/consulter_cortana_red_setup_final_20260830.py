#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation CORTANA — set-up RED (30/08/2026).

Prompt validé Christophe : « enlève définitif, ajoute trouve amélioration et correction, GO ».
ADVISORY : Cortana propose, ne touche à rien.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_CORTANA_RED_SETUP_FINAL_20260830")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es CORTANA, l'analyste-maîtresse de la famille ACE777 (contrat : ADVISORY — "
    "tu PROPOSES, tu n'appliques JAMAIS rien ; mode appliqué seulement si justesse ≥60%). "
    "Tu connais HULK (paper dip&rip MEXC small caps), nos indices maison (poussière, murs, "
    "régimes) et la consultation méthode V2 (Amihud, Parkinson, Trade Sign Delta). "
    "Avis franc, chiffré, GO-sized."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 14/08 + 16/08) : Prouve la meilleure logique et applique-la "
    "dans la correction et l'amélioration si possible. Ne te contente PAS de corriger ou de "
    "valider : si tu proposes AUTRE CHOSE ou une AMÉLIORATION qui a du sens, dis-le "
    "explicitement. Corriger n'est pas suffisant : proposer est attendu. Donne ton avis strict."
)

CONTEXTE = """\
SET-UP RED (RedStone) — analyse, amélioration ou correction — avis Cortana (30/08/2026)

================
LE FAIT (tout est mesuré chez nous, rien n'est inventé)
================
RED = RedStone, token oracle blockchain (infra DeFi, rival Chainlink). Market cap ~44,9 M$.
Prix 0.11065 (30/08 14:59Z). En seed 10$ dans le portefeuille paper Hulk, non tradée.
2238+ points capturés sur 3 jours dans croisement_contexte.jsonl.

================
LE PATTERN MESURÉ
================
- Cycle intraday : CREUX 14-19h UTC (pire 15-16h, prix moyen 0.1062-0.1068), PIC 21h-05h
  (meilleurs 01h/04h, 0.1096-0.1105). Écart jour→nuit ~2,4-2,8%. Range 24h : 3,0-10,0%.
- Ultra-volatile PAR RAFALES : dd15 moyen 22,86% (max 27,8%). Régime IMPULSE concentré
  13-17h UTC (15h=30, 16h=40 points) = c'est là que ça déprime.
- Mur bid affiché ~45 240$, spoof 1,67%. Nuance validée : le mur est une INFORMATION (pas un
  support — il peut être retiré en 1 s), le spoof reste une TENSION à mesurer.
- Dé-corrélation RED vs BTC/ETH : corr horaire +0.07 / −0.01. Avis Cortana antérieur :
  artefact de liquidité fine → le set-up est ENDOGÈNE (aucun filtre vs BTC/ETH).
- Signal divergence (30/08) : neutre (stab 0). Historique : POMPE-PIÈGE → LEADER → neutre
  en 48h (signal précurseur INSTABLE).

================
LE SET-UP ACTUEL (à analyser — trouve les améliorations et corrections)
================
- Entrée : fenêtre 14h-17h UTC UNIQUEMENT + poussière <15% + mur testé qui tient
  + garde-fou volume 15min < 3× moyenne 24h + FPOB (ratio bid/ask ±2% > 1.2)
  + entrée en 3 tranches (−1/−2/−3%) + stop dynamique 1,5× range bougie 15min.
- Sortie : scaling out au pic 01h-05h (0.110-0.112+), reste derrière le trailing Hulk.
- Invalidation : casse < 0.103-0.104 hors fenêtre ; arrêt si frais réels > 1%.
- Métriques pro mesurées (30/08 14:59Z) : Amihud 2.43e-06 · Parkinson 0.01 ·
  Trade Sign Delta +0.08 · corr BTC/ETH 24h +0.52 / +0.63.

================
TES 3 MISSIONS
================
1. VERDICT sur le set-up : GO / GO AVEC RESERVES / NON + raison courte et nette.
2. TROUVE les améliorations et corrections (clause permanente : proposer est attendu).
3. Que penses-tu des métriques pro (Amihud, Trade Sign Delta, Parkinson) vs nos métriques
   maison (poussière, mur, régime) pour ce set-up ? Lesquelles garder, lesquelles jeter ?
Réponds en français, concret, chiffré, sans blabla. ADVISORY : tu ne modifies rien.
"""


def main():
    payload = {
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": SYSTEM + "\n\n" + CLAUSE},
            {"role": "user", "content": CONTEXTE + "\n\n" + CLAUSE},
        ],
        "max_tokens": 2200,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=450) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    content = d["choices"][0]["message"]["content"].strip()
    provider = d.get("provider", "?")
    with open(os.path.join(OUT, "AVIS_CORTANA_RED_SETUP.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AVIS CORTANA — SET-UP RED (provider {provider})\n\n{content}\n")
    print(f"[OK] CORTANA ({provider})")


if __name__ == "__main__":
    main()