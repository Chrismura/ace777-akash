#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation MÉTHODE — meilleure façon d'analyser le comportement des actifs (30/08/2026).

Souscription Christophe : « envoie quelqu'un pour qu'il m'amène la meilleure méthode pour
analyser le comportement des actifs / ce dont nous avons besoin pour l'évaluation, et tu me
dis — on va voir si ce qu'on fait c'est valable ou pas. GO »

2 membres famille (DEEPSEEK critique factuel + ULTRA robustesse) + codeur. ADVISORY : ne
modifient rien, ils DONNENT la méthode.
"""
import json
import os
import time
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_MEILLEURE_METHODE_20260830")
os.makedirs(OUT, exist_ok=True)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : Ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (approche différente, autre architecture, "
    "autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu. Une réponse qui ne fait "
    "que « c'est bon » ou « corrige X » est incomplète."
)

MEMBRES = [
    ("DEEPSEEK", "deepseek.analyse",
     "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu "
     "donnes des contre-exemples, tu refuses les conclusions non étayées. Tu compares "
     "notre méthode à la meilleure pratique professionnelle."),
    ("ULTRA", "inferx.analyse",
     "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : "
     "ce qui casse en prod, ce qui tient sur le long terme, ce qui est scalable sur un "
     "portefeuille entier."),
]

CONTEXTE = """\
MEILLEURE MÉTHODE D'ANALYSE DE COMPORTEMENT D'ACTIFS — consultation méthode (30/08/2026)

================
LE CONTEXTE (qui nous sommes)
================
Nous gérons un portefeuille paper de ~20 actifs (petites caps MEXC, dont des micro-caps)
via un moteur de trading (Hulk) qui fait du dip&rip. Notre doctrine (gravée 30/08) :
TOUS les actifs sont SOUS OBSERVATION en permanence — on trade, on observe, on modifie
les set-ups au fur et à mesure. Le set-up d'un actif n'est JAMAIS statique (le marché
change, les actifs changent de comportement). Chaque actif a sa fiche d'étude de cas.
Les données complètes de qualité sont notre arme principale.

================
CE QUE NOUS MESURONS AUJOURD'HUI (notre méthode actuelle)
================
Pour chaque actif, toutes les ~1 min, nous capturons dans croisement_contexte.jsonl :
1. PRIX + régime (COOLING / IMPULSE_WAIT / IMPULSE) + move 6h (m6_pct) + drawdown 15 min (dd15_pct)
2. MURS du carnet d'ordres : mur bid max/moy ($), spoofing (mur_spoof_pct), force du mur (wall_strength)
3. POUSSIÈRE (onchain) : tx fantômes (poussiere_taux_fantome, poussiere_nb_cachees) — activité cachée
4. INDICES onchain : SDI (pression vendeuse), IPT (micro-tx/entropie), RBF (double dépense),
   fee_pressure (frais réseau), pipeline_score
5. ANALYSES AGGREGÉES :
   - Pattern intraday par heure UTC (creux/pic de la journée, ex : RED creux 15-16h → pic 01-05h)
   - Corrélations au panier + vs BTC/ETH (par phase : matin/nuit, ex : RED matin anti-corrélé BTC -0.85)
   - Divergence : qui précède le panier (leader) / qui pompe-piège (précède baisse), timing lag
   - Gating temporel : signal jour vs nuit (thèse : la nuit = bruit thermique)
6. SUIVI QUOTIDIEN par actif : mesure à heure fixe (même heure = comparable), ligne par jour,
   comparaison jour après jour (ex : RED, script suivi_setup_red.py + plist 14:30 UTC)

================
LA DEMANDE (Christophe)
================
« Envoie quelqu'un pour qu'il m'amène LA MEILLEURE MÉTHODE pour analyser le comportement
des actifs / ce dont nous avons besoin pour l'évaluation. On va voir si ce qu'on fait
c'est valable ou pas. »

================
TES 3 MISSIONS
================
1. LA MEILLEURE MÉTHODE (norme professionnelle) : quelle est la méthode de référence pour
   analyser le comportement d'un actif en vue de son évaluation (entrer/tenir/sortir) ?
   Donne le cadre complet : les dimensions à mesurer (microstructure, momentum, cycle,
   liquidité, risque), la fréquence, les métriques clés par dimension.
2. VERDICT SUR NOTRE MÉTHODE : notre approche (1-6 ci-dessus) est-elle VALABLE / INSUFFISANTE
   / SURVEILLÉE PAR DES FAUSSES PISTES ? Qu'est-ce qui manque, qu'est-ce qui est du bruit,
   qu'est-ce qu'on mesure en trop, qu'est-ce qu'on devrait mesurer à la place ?
3. UNE AMÉLIORATION CONCRÈTE GO-sized pour passer au niveau pro (pas cosmétique).
Réponds en français, format court et net, sans blabla. ADVISORY : tu ne modifies rien."""


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
                        {"role": "user", "content": CONTEXTE},
                    ],
                    "max_tokens": 1800, "temperature": 0.3,
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
                    {"role": "user", "content": CONTEXTE + "\n\nEn tant que codeur : notre "
                     "méthode est-elle implémentable proprement à l'échelle de 20 paires ? "
                     "Quelles sont les failles techniques (biais, coûts API, fiabilité des "
                     "proxies onchain) ? Quelle architecture de suivi recommandes-tu ?"},
                ],
                "max_tokens": 1800, "temperature": 0.3,
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