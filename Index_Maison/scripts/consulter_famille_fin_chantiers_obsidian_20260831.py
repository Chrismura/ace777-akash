#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_fin_chantiers_obsidian_20260831.py — Finalisation des
chantiers Obsidian E, F, G, B, A' soumise à la FAMILLE (3 membres).

Contexte : Christophe est sorti, il veut qu'on finisse TOUS les chantiers A→H.
A-D sont FAITS (pont CLI + gatekeeper, frontmatter 23 fiches, Portefeuille/Signets/
Veille bases, templates journal/factif/synthèse/veille, skills kepano installés).
Reste E, F, G, B, A'. On consulte la famille (règle : famille avant implémentation
structurante) avec un prompt amélioré (avis strict + amélioration prouvée).
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_FIN_CHANTIERS_OBSIDIAN_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — FINALISER LES CHANTIERS OBSIDIAN E/F/G/B/A'

=== 1. OÙ ON EN EST (A→D FAITS) ===
- Pont CLI obsidian_cli_bridge.py : écrit dans le vault via la CLI officielle,
  queue séquentielle, read-back hash, fail-open disque, circuit breaker, audit.
- GATEKEEPER : 4 types stricts (actif, signal, synthese_ia, journal), validation
  des propriétés avant écriture, compilation markdown conforme, write_typed().
- Frontmatter injecté sur 23 fiches actif (Crypto_Projet), Portefeuille.base créé
  (+ Signets.base + Veille.base), templates (journal, factif, synthèse, veille),
  daily notes activées, 4 skills kepano installés (obsidian-markdown/cli/bases/
  json-canvas) dans .agents/skills/.
- Contrainte CLI : l'app Obsidian doit tourner pour la CLI (sinon fallback disque).

=== 2. LES CHANTIERS RESTANTS (votre expertise) ===

[E] CONNECTER LES AGENTS AUX DAILY NOTES : chaque agent/cortana doit pouvoir
    journaliser son activité du jour (obsidian daily:append, ou via le pont).
    QUESTION : le journal central doit-il être UNE seule note par jour que tout
    le monde append (risque de collision/concurrence ?) ou des sections par
    agent ? Comment structurer pour que les LLM relisent tout le contexte en un
    bloc ?

[F] WIKILINKS / GRAPHE : 1341 notes orphelines sur 1733 (77%). On veut relier les
    fiches actif à leurs synthèses/événements/signets en utilisant [[wikilinks]].
    QUESTION : faut-il un script qui injecte des wikilinks automatiquement (via
    le pont, en comparant les noms d'actifs dans le corps des notes) ? Risques de
    faux liens ? Ou vaut-il mieux une règle pour les NOUVELLES fiches seulement
    (Day Zero) et laisser le graphe se remplir organiquement ?

[G] CANVAS : carte visuelle actifs ↔ événements ↔ institutions (fichier .canvas,
    pilotable par nos agents via json-canvas skill). QUESTION : est-ce utile pour
    nous maintenant, ou sur-ingénierie ? Si utile, combien de nœuds/darès garder
    simple ?

[B] FRONTMATTER SUR LES SYNTHÈSES : étendre le frontmatter uniforme aux synthèses
    famille/Cortana (type: synthese_ia, membre, date, statut). Risques sur les
    ~15 scripts qui génèrent ces synthèses ?

[A'] MIGRER LES SCRIPTS SUR LE PONT : ~60 scripts écrivent encore dans
    OUTBOX_OBSIDIAN (synchro manuelle cp). Les faire passer par write_typed
    un par un. QUESTION : comment prioriser (lesquels d'abord) ? Faut-il créer un
    wrapper qui force le passage par le pont sans réécrire chaque script ?

=== 3. VOTRE MISSION (avis strict, pas complaisant, en français) ===
RÉPONDEZ SUR 5 POINTS :
A) [E] Daily notes : une note unique appendée par tous vs sections par agent ?
   Mécanisme anti-collision ? Recommandation concrète.
B) [F] Wikilinks : script automatique vs Day Zero ? Risques de faux liens et
   comment les éviter ? Recommandation.
C) [G] Canvas : vraiment utile pour nous, ou à repousser ? Si utile : taille
   max de la carte, quoi connecter en priorité ?
D) [B]+[A'] : ordre de migration des synthèses sur le pont ? Faut-il un wrapper
   global plutôt que réécrire 60 scripts ? Quelle est la séquence la plus sûre
   (moins de casse) pour passer de OUTBOX → pont ?
E) UNE AMÉLIORATION CONCRÈTE de votre cru pour l'ensemble (ou une correction).
   Donnez votre avis STRICT global : ce qui est bon, risqué, ce que vous feriez
   différemment. NE SOYEZ PAS COMPLAISANT."""


MODELS = ["gemini", "juge", "deepseek"]


def ask_famille(model, timeout=240):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2800, "temperature": 0.2,
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


def main():
    results = {}
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

    print(f"\n=== SYNTHESE ===")
    print(f"Consultation terminée : {len(results)}/3 avis dans {OUT}")


if __name__ == "__main__":
    sys.exit(main())