#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_codeur_cli_obsidian_20260831.py — Chantier « CLI Obsidian »
soumis à la FAMILLE (2 membres : gemini, juge) ET au CODEUR (GO Christophe, 31/08).

Sujet : Obsidian vient de sortir une CLI officielle (v1.12+, février 2026). On l'a
installée et vérifiée sur le vault ACE777 (create/append/read OK). On veut remplacer
notre bricolage OUTBOX_OBSIDIAN (écritures de fichiers .md espérées vues par l'app)
par des commandes CLI officielles, via un petit pont (obsidian_cli_bridge.py) qui
garde le fallback fichier si Obsidian est fermé (la CLI exige l'app ouverte).

Buffy (chef scientifique) a un plan. On demande un AVIS STRICT + UNE amélioration
prouvée chacun + les dangers non vus.

Résultat : dossier CONSULTATION_FAMILLE_CODEUR_CLI_OBSIDIAN_20260831/AVIS_*.md
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CODEUR_CLI_OBSIDIAN_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — CHANTIER « PONT CLI OBSIDIAN » À VALIDER

=== 1. NOTRE SYSTÈME (la « maison ACE777 ») ===
On fait tourner une maison de trading/veille crypto avec plusieurs IA (Cortana, la
famille : gemini/grok/nvidia/deepseek/juge/ultra, et des agents). Toute notre
mémoire collective vit dans Obsidian (vault ~/Documents/Obsidian_ACE777) : fiches
par actif crypto, protocoles, synthèses de consultations, journaux, deepdives.

AUJOURD'HUI, nos IA écrivent des fichiers .md dans un dossier intermédiaire
(OUTBOX_OBSIDIAN/) via des scripts Python maison. C'est du bricolage : l'app
Obsidian « voit » les fichiers via la synchro de dossier, mais on n'a aucun canal
officiel (pas de modèles, pas de tags gérés par l'app, pas de vérification que la
note est bien indexée dans le vault).

=== 2. LA NOUVEAUTÉ : CLI OFFICIELLE OBSIDIAN (vérifiée, pas une hypothèse) ===
Obsidian a sorti une CLI officielle (v1.12+, février 2026). On l'a installée sur le
MacBook (binaire /Applications/Obsidian.app/Contents/MacOS/obsidian-cli, v1.13.7)
et ACTIVÉE dans Settings → General → Advanced. VÉRIFIÉ À L'INSTANT sur le vault :
- `obsidian create name="..." content="..."` → crée une note DANS le vault actif ✅
- `obsidian append path="note.md" content="..."` → ajoute du contenu ✅
- `obsidian read path="note.md"` → lit ✅
- `obsidian search query="..." vault=ace777` → cherche (lent sur gros vault, à
  confirmer) 
- `obsidian tags counts`, `obsidian daily`, `obsidian daily:append` ✅
CONTRAINTE : l'app Obsidian DOIT tourner pour que la CLI réponde (la CLI parle à
l'app via un canal local).

=== 3. LE PLAN PROPOSÉ (Buffy) ===
Créer un module `obsidian_cli_bridge.py` dans la maison (même pattern que nos
satellites validés : short_btc.py, satellite_aspiration.py) qui :
1) ENVELOPPE la CLI : fonctions create_note(name, content, template?), append(path,
   content), read(path), search(query) — avec nos conventions de nommage
   (ex. FICHE_EDEL_20260831.md, SYNTHESE_FAMILLE_...).
2) REMPLACE progressivement les écritures OUTBOX_OBSIDIAN/ des synthèses
   famille/Cortana par des écritures CLI directes (additif, réversible par config).
3) GARDE le fallback fichier : si Obsidian est fermé (CLI injoignable), on écrit le
   .md dans OUTBOX_OBSIDIAN/ comme avant (fail-open, jamais de perte).
4) DÉTECTE l'état de l'app (ping CLI rapide) avant chaque écriture pour éviter les
   timeouts d'attente.

=== 4. VOTRE MISSION (avis strict, pas complaisant) ===
RÉPONDEZ SUR 4 POINTS, en français, factuel, avec des preuves quand c'est possible :

A) Le plan (pont CLI + fallback) est-il le bon découpage ? Y a-t-il des RISQUES
   à écrire directement dans le vault via la CLI ? (latence par commande,
   verrouillage de fichiers pendant que l'app écrit, corruption, volume de
   commandes si on écrit 50 synthèses/jour, coût par commande…)
   Précisez ce qui casserait et comment le faire sans casser.

B) AUTRES approches que Buffy n'a pas vues ? (API locale d'Obsidian, URI scheme
   obsidian://, plugin maison, REST API communautaire…) Comparez avec la CLI
   officielle : laquelle est la plus ROBUSTE pour de l'écriture automatisée par IA ?

C) COSTAUD STRUCTUREL : pour que nos fiches soient FIABLES (une synthèse écrite =
   une synthèse lisible et indexée dans Obsidian), que faut-il vérifier après
   chaque écriture ? (read-back ? recherche ? journal ?)

D) UNE AMÉLIORATION CONCRÈTE ET PROUVÉE de votre cru pour ce pont, en plus du plan
   proposé (ou une correction d'une étape du plan). Donnez votre avis STRICT sur
   l'ensemble : ce qui est bon, ce qui est risqué, ce que vous feriez différemment.
   NE SOYEZ PAS COMPLAISANT : si le plan est mal pensé, dites-le et proposez mieux."""


MODELS = ["gemini", "juge"]


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
                      + "Concentre-toi sur les risques concrets d'un pont Python qui "
                      + "sous-traite des appels obsidian-cli (subprocess, timeout, "
                      + "détection app ouverte, read-back de vérification, volume de "
                      + "commandes), et sur le design du module le plus sûr à mettre "
                      + "en place sans casser les écritures actuelles OUTBOX_OBSIDIAN."}],
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
    # Famille (2 membres)
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
    print(f"Consultation terminée : {len(results)}/3 avis dans {OUT}")


if __name__ == "__main__":
    sys.exit(main())
