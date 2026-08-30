#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation MÉTHODE — meilleure façon d'analyser le comportement des actifs (30/08/2026).

Souscription Christophe (GO) : « nous voulons » la MEILLEURE méthode de référence pour
analyser le comportement d'un actif pour SON set-up. On ne donne PAS notre méthode —
ils partent de zéro. Clause permanente gravée (14/08 + 16/08) DANS le prompt.

2 membres famille (DEEPSEEK critique factuel + ULTRA robustesse) + codeur. ADVISORY.
"""
import json
import os
import time
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_MEILLEURE_METHODE_20260830")
os.makedirs(OUT, exist_ok=True)

# Clause permanente (gravée 14/08 + 16/08 par Christophe — DANS le prompt, visible).
CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 14/08 + 16/08) : Prouve la meilleure logique et applique-la "
    "dans la correction et l'amélioration si possible. Ne te contente PAS de corriger ou de "
    "valider : si tu proposes AUTRE CHOSE (approche différente, autre architecture, autre "
    "unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. Corriger n'est pas "
    "suffisant : proposer est attendu. Donne ton avis strict."
)

MEMBRES = [
    ("DEEPSEEK", "deepseek.analyse",
     "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu "
     "donnes des contre-exemples, tu refuses les conclusions non étayées. Tu compares à la "
     "meilleure pratique professionnelle."),
    ("ULTRA", "inferx.analyse",
     "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : "
     "ce qui casse en prod, ce qui tient sur le long terme, ce qui est scalable."),
]

CONTEXTE = """\
MEILLEURE MÉTHODE D'ANALYSE DU COMPORTEMENT D'UN ACTIF — consultation (30/08/2026)

================
LA DEMANDE (Christophe)
================
Nous voulons établir la MEILLEURE méthode de référence (niveau quant desk / market maker
professionnel) pour analyser le comportement d'un actif en vue de SON SET-UP : décider
entrer / tenir / sortir.

Contexte : portefeuille de ~20 actifs, petites caps, échanges centralisés type MEXC,
micro-caps incluses. Objectif : une méthode rigoureuse, mesurable, exploitable en pratique
pour adapter le set-up de chaque actif à son comportement réel (qui change avec le marché).

================
TES 3 MISSIONS
================
1. Quelle est la MEILLEURE MÉTHODE (norme professionnelle) pour analyser le comportement
   d'un actif en vue de son set-up ? Donne le cadre complet : dimensions à mesurer,
   métriques clés par dimension, fréquence d'échantillonnage, sources de données.
2. Quelles métriques sont RÉELLEMENT DISCRIMINANTES sur des actifs peu liquides, vs celles
   qui sont du bruit ? Distingue clairement.
3. Quelle ARCHITECTURE DE COLLECTE recommandes-tu pour ~20 paires (fréquence, stockage,
   calcul) sans exploser les limites d'API ?

Réponds en français, concret, chiffré, sans blabla. NE PRÉSUPPOSE AUCUNE méthode existante
de notre côté : pars de zéro, donne la meilleure pratique. ADVISORY : tu ne modifies rien."""


def ask_hub(payload):
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=400) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def main():
    for nom, task, system in MEMBRES:
        for attempt in (1, 2):
            try:
                payload = {
                    "task": task,
                    "messages": [
                        {"role": "system", "content": system + "\n\n" + CLAUSE},
                        {"role": "user", "content": CONTEXTE + "\n\n" + CLAUSE},
                    ],
                    "max_tokens": 2000, "temperature": 0.3,
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

    # codeur
    for attempt in (1, 2):
        try:
            payload = {
                "task": "code.ia",
                "messages": [
                    {"role": "system",
                     "content": "Tu es le CODEUR de la famille ACE777. Avis factuel sur "
                                "l'implémentation et la validité technique d'une méthode "
                                "d'analyse. Tu ne modifies rien, tu DONNES UN AVIS." + "\n\n" + CLAUSE},
                    {"role": "user", "content": CONTEXTE + "\n\n" + CLAUSE},
                ],
                "max_tokens": 2000, "temperature": 0.3,
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