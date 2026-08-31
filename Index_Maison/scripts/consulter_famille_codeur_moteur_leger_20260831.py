#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_codeur_moteur_leger_20260831.py — Plan « moteur léger et
costaud » soumis à la FAMILLE (6 membres) ET au CODEUR (GO Christophe, 31/08).

Sujet : rendre Hulk (moteur paper MEXC) plus léger (moins d'appels réseau, moins
de charge) ET plus costaud (robuste aux timeouts / rate-limit / changements).
Buffy (chef scientifique) a mesuré le coût réel et propose un plan priorisé.
On demande un AVIS STRICT + UNE amélioration prouvée chacun + les dangers non vus.

Résultat : dossier CONSULTATION_FAMILLE_CODEUR_MOTEUR_LEGER_20260831/AVIS_*.md
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CODEUR_MOTEUR_LEGER_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — PLAN « MOTEUR LÉGER ET COSTAUD » À VALIDER

=== 1. LE MOTEUR HULK (paper MEXC) ===
Hulk est un bot de trading PAPER (argent fictif) qui tourne en continu sur un
MacBook. Boucle toutes les 20 s, ~21 paires suivies (BTC, ETH, XRP, EDEL, CC…).
À chaque cycle il : lit ses positions, décide d'acheter/vendre, et écrit un
fichier de contexte (croisement_contexte.jsonl, 1 point/pair/minute) qui sert à
tous les outils satellites (protocole divergence, short BTC, murs, etc.).

=== 2. LE DIAGNOSTIC MESURÉ (Buffy, pas une hypothèse) ===
Par cycle de 20 s (21 paires), le moteur fait :
- tick_pair × 21 → last_price(pair) : 1 appel API par paire = 21 appels
- sense_ok × 21 → book_sense (carnet d'ordres) : ~21 appels
- probe_aspiration : jusqu'à 5 appels profondeur
- refresh_scores (tous les 3 cycles) → klines 360 bougies + ticker_24h : +42 appels
Total ≈ 60-90 appels / cycle ≈ 200-270 appels / minute.
Limite MEXC annoncée ≈ 200 req/min/IP → le moteur est EN PERMANENCE au bord du
rate-limit. C'est probablement la cause racine des timeouts, retries lents
(timeout 40 s × 4 tentatives), cycles étirés, et des états « bizarres » qu'on
corrige en boucle depuis plusieurs jours.

FAIT VÉRIFIÉ : MEXC renvoie les 2076 paires en 1 SEUL appel
(GET /api/v3/ticker/price sans symbole, testé à l'instant). Le moteur fait 21
appels pour ce qu'1 appel suffit à fournir.

=== 3. LE PLAN PROPOSÉ (5 étapes priorités) ===
1) BATCH PRIX : 1 appel /ticker/price (tout le marché) mis en cache 15-20 s, on
   pioche dedans → on passe de 21 à 1 appel au cycle soit ~-95% des appels.
2) TIMEOUT AGRESSIF : 40 s × 4 retries → 10 s × 2. Un prix qui met >10 s est
   périmé de toute façon ; en batch, une erreur = 1 appel à rejouer, pas 21.
3) ESPACER LES COÛTEUX : les régimes (klines 360 bougies × 21 paires) n'ont pas
   besoin d'un refresh toutes les 60 s → toutes les 2-3 min. Le carnet
   (book_sense) → seulement pour les paires proches d'une décision.
4) ARCHITECTURE CŒUR / SATELLITES : les sondes (murs, aspiration, GEX, veille)
   sortent de la boucle de trading → satellites autonomes (leur propre boucle)
   qui écrivent des fichiers JSON ; le cœur LIT les fichiers (coût 0, risque
   réseau 0) au lieu d'appeler les APIs. Pattern déjà validé avec short_btc.py.
5) CIRCUIT-BREAKER 429 : si MEXC répond rate-limit → pause 30-60 s au lieu de
   marteler.

=== 4. VOTRE MISSION (avis strict, pas complaisant) ===
RÉPONDEZ SUR 4 POINTS, en français, factuel, avec des preuves quand c'est possible :

A) PRIORITÉ 1 (batch prix) : est-ce LA bonne première étape ? Y a-t-il des
   RISQUES à passer les 21 appels à 1 appel avec cache ? (cohérence des prix
   entre paires, fraîcheur du cache 15-20 s vs des décisions qui dépendent de
   la milliseconde, ordre des paires, paires non renvoyées par le batch…)
   Précisez ce qui casserait et comment le faire sans casser.

B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ que Buffy n'a pas vues ? Regardez le
   problème en architecture, pas seulement en nombre d'appels.

C) COSTAUD STRUCTUREL : pour rendre le cœur « petit et robuste », est-ce que
   l'architecture cœur/satellites (étape 4) est la bonne voie ? Ou voyez-vous
   un meilleur découpage ? (justifiez)

D) UNE AMÉLIORATION CONCRÈTE ET PROUVÉE de votre cru pour ce moteur, en plus du
   plan proposé (ou une correction d'une étape du plan). Donnez votre avis
   STRICT sur l'ensemble : dites ce qui est bon, ce qui est risqué, ce que vous
   feriez différemment. NE SOYEZ PAS COMPLAISANT : si une étape du plan est mal
   priorisée ou dangereuse, dites-le et proposez mieux."""


MODELS = ["gemini", "grok", "nvidia", "deepseek", "juge", "ultra"]


def ask_famille(model, timeout=240):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2200, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    alive = time.time() + timeout
    t0 = time.time()
    while time.time() < alive:
        try:
            with urllib.request.urlopen(req, timeout=240) as resp:
                d = json.loads(resp.read().decode())
            return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)
        except Exception as e:
            time.sleep(3)
            last = e
    raise last


def ask_codeur(timeout=240):
    payload = json.dumps({
        "task": "code.ia",
        "messages": [{"role": "user", "content": BRIEF
                      + "\n\nNOTE SUPPLÉMENTAIRE CODEUR : tu es le codeur expert. "
                      + "Concentre-toi sur les risques concrets du changement de "
                      + "last_price → batch + cache (sémantique, atomicité du prix, "
                      + "impact sur gestion des positions), et sur le découpage "
                      + "cœur/satellites le plus sûr à mettre en place sans casser "
                      + "le moteur en production."}],
        "max_tokens": 2200, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    alive = time.time() + timeout
    while time.time() < alive:
        try:
            with urllib.request.urlopen(req, timeout=240) as resp:
                d = json.loads(resp.read().decode())
            return d["choices"][0]["message"]["content"], d.get("provider", "?"), 0
        except Exception as e:
            time.sleep(3)
            last = e
    raise last


def main():
    results = {}
    # Famille (6 membres)
    for m in MODELS:
        try:
            content, provider, _ = ask_famille(m)
            results[m] = content
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider})\n\n{content}\n")
            print(f"[OK] FAMILLE {m} -> {f} ({len(content)} chars)")
        except Exception as e:
            print(f"[ERR] FAMILLE {m}: {e}")
        time.sleep(2)
    # Codeur
    try:
        content, provider, _ = ask_codeur()
        results["codeur"] = content
        f = os.path.join(OUT, "AVIS_codeur.md")
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(f"# CODEUR (provider {provider})\n\n{content}\n")
        print(f"[OK] CODEUR -> {f} ({len(content)} chars)")
    except Exception as e:
        print(f"[ERR] CODEUR: {e}")

    print(f"\n=== SYNTHESE ===")
    print(f"Consultation terminée : {len(results)}/7 avis dans {OUT}")


if __name__ == "__main__":
    sys.exit(main())