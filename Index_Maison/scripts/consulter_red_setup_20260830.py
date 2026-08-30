#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation ciblée RED — 30/08/2026.

Souscription Christophe : « oui mais aux 6 → 2 plus le codeur, toi et moi, suffisent. GO »
= consulter 2 membres de la famille + le codeur sur le PATTERN & SET-UP RED (oracle,
creux 15-16h UTC → pic 01-05h UTC), avec contexte complet. Ne modifie rien.

Membres choisis : JUGE (tranche formellement) + ULTRA (robustesse/long terme).
Codeur : task code.ia via le hub.
"""
import json
import os
import sys
import time
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_RED_SETUP_20260830")
os.makedirs(OUT, exist_ok=True)

# CLAUSE PERMANENTE (gravée 16/08 par Christophe — applicable à TOUS les prompts).
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

# 2 membres famille ciblés (pas les 6 — consigne Christophe).
MEMBRES = [
    ("ULTRA", "inferx.analyse",
     "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : "
     "ce qui casse en prod, en tempête, sur du long terme. Tu exiges du chiffré et tu "
     "donnes les limites du set-up proposé."),
    ("JUGE", "juge.tranche",
     "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC "
     "RESERVES / NON. Exigeant, raison courte et nette."),
]

CONTEXTE = """\
PATTERN & SET-UP RED (RedStone) — consultation ciblée famille (2) + codeur (30/08/2026)

================
LE FAIT (nostre BUFFER, jamais inventé)
================
RED = RedStone, token oracle blockchain (infra DeFi, rival de Chainlink). Market cap
~44,9 M$, prix 0.10741 USDT (30/08 13:48Z). Seedé 10$ dans le portefeuille paper Hulk.
Analyse de 2238 points REDUSDT sur 3 jours (27→30/08) dans croisement_contexte.jsonl.

================
LE PATTERN DÉCOUVERT (notre donnée, granulométrie ~1 pt/min)
================
1. Cycle intraday net répété chaque jour : CREUX en pleine journée, PIC soirée/nuit.
   - CREUX moyen 14h-19h UTC, pire ~15-16h (prix moyen 0.1062-0.1068 ; min absolu 0.10200).
   - PIC moyen 21h-05h UTC, meilleurs ~01h et 04h (0.1096-0.1105 ; max absolu 0.11434).
   - Écart jour→nuit ~2,4-2,8%, range 24h constaté 3,0-10,0% sur 3 jours.
2. Ultra-volatile PAR RAFALES : dd15 moyen 22,86% (max 27,8%) — en 15 min RED bouge
   souvent >= 20%. move6h moyen 3,8%. Régimes : surtout COOLING (1501) mais 93 IMPULSE
   concentrés 13h-17h UTC (15h=30, 16h=40) = c'est là que la paire déprime.
3. Murs & poussière : mur bid max ~45 240$ constant, spoof faible (1,67%) → mur RÉEL.
   Poussière (tx fantômes) 17,8% nuit / 20,2% jour (légèrement + pendant le creux).
   Integer wall 0,97-0,99.

================
LE SET-UP PROPOSÉ (à évaluer)
================
A. Entrée/accumulation FAVORABLE zone creux 15-16h UTC (prix 0.106-0.107, mur qui tient,
   poussière stable) → marge avant rebond de nuit.
B. Sortie/prise de profit FAVORABLE zone pic 01h-05h UTC (0.110-0.112+).
C. Prudence : RED ultra-volatile 15 min → Hulk DOIT garder stops serrés ; scaling out
   (dégager une partie au pic, garder le reste).
D. Comparaison : QAIT avait son creux 10-13h ; RED l'a 15-16h → même logique, autre heure.
E. Réserve : 3 jours de données = validation PRÉCOCE. Pattern net mais pas vérifié sur un mois.

================
TA MISSION (3 coups une pierre)
================
1. VERDICT sur le set-up A+B+C (+ éventuellement D/E) : GO / GO AVEC RESERVES / NON
   + raison courte et nette (le JUGE tranche formellement).
2. Le(s) ANGLE(S) MORT(S) : ce qui manque ou est mal borné dans ce set-up (validation
   trop courte ? mur 45K$ fragile en vrai ? fenêtre 15-16h pas reconductible ? ...).
3. UNE AMÉLIORATION concrète GO-sized pour fiabiliser l'exploitation de ce pattern.
Réponds en français, format court et net, sans blabla. Ne touche à rien.
"""


def ask_hub(payload):
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def main():
    # 1) 2 membres famille
    for nom, task, system in MEMBRES:
        for attempt in (1, 2):
            try:
                payload = {
                    "task": task,
                    "messages": [
                        {"role": "system", "content": system + "\n\n" + CLAUSE},
                        {"role": "user", "content": CONTEXTE},
                    ],
                    "max_tokens": 1400, "temperature": 0.3,
                }
                content, provider = ask_hub(payload)
                with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {nom} (provider {provider})\n\n{content}\n")
                print(f"[OK] famille {nom} ({provider})")
                break
            except Exception as e:
                print(f"[ERR] famille {nom} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)

    # 2) codeur (task code.ia)
    for attempt in (1, 2):
        try:
            payload = {
                "task": "code.ia",
                "messages": [
                    {"role": "system",
                     "content": "Tu es le CODEUR de la famille ACE777. Avis factuel sur "
                                "l'implémentation/la validité technique. Tu ne modifies rien, "
                                "tu DONNES UN AVIS." + "\n\n" + CLAUSE},
                    {"role": "user", "content": CONTEXTE + "\n\nLe set-up n'est PAS encore "
                     "câblé dans Hulk : c'est une proposition. Est-elle implémentable "
                     "proprement (fenêtre horaire entrée/sortie), quelles garde-fous faut-il, "
                     "et est-elle fiable sur 15 paires MEXC ?"},
                ],
                "max_tokens": 1400, "temperature": 0.3,
            }
            content, provider = ask_hub(payload)
            with open(os.path.join(OUT, "AVIS_CODEUR.md"), "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS CODEUR (provider {provider})\n\n{content}\n")
            print(f"[OK] codeur ({provider})")
            break
        except Exception as e:
            print(f"[ERR] codeur (tentative {attempt}): {e}")
            time.sleep(3)


if __name__ == "__main__":
    main()