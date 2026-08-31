#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_confrontation_obsidian_20260831.py — Confrontation détaillée
de notre organisation Obsidian vs le système de l'expert (Sébastien Dubois),
soumise à la FAMILLE (3 membres : gemini, juge, deepseek) — GO Christophe 31/08.

Méthode Christophe : « regarde dans les détails comment c'est organisé et copie
si c'est mieux, puis soumets à la famille 3 membres, prompt amélioré ».

Résultat : dossier CONSULTATION_FAMILLE_CONFRONTATION_OBSIDIAN_20260831/AVIS_*.md
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CONFRONTATION_OBSIDIAN_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — CONFRONTATION OBSIDIAN : NOTRE ORGANISATION vs L'EXPERT

=== 1. LA SITUATION ===
On vient de découvrir la CLI officielle Obsidian (v1.12+, installée et testée).
On audite maintenant NOTRE usage d'Obsidian pour l'utiliser à 100%. Christophe
a demandé : « regarde dans les détails comment l'expert organise son système et
copie si c'est mieux, puis fais valider par la famille ».

=== 2. LA RÉFÉRENCE (l'expert) ===
Sébastien Dubois — guide « Obsidian Automation → AI Operating System » (auteur
reconnu, vault de 20 000 notes, 400 skills IA). SON système :
- Registre de ~50 TYPES DE NOTES : chaque type est reconnu (tag/dossier/pattern),
  a un dossier, un template, des propriétés REQUISES avec types et valeurs
  autorisées, des tags obligatoires, des icônes.
- TPL DISPATCHER : un template racine reconnaît le type d'une nouvelle note et
  applique le bon template automatiquement (frontmatter, sections, dossier).
- STATE MACHINES dans le frontmatter : chaque type a des états (ex. article :
  idea → draft → done) ; un changement d'état déclenche des actions (déplacer,
  archiver, horodater).
- « Use exactly ONE sync mechanism » : deux sync + un agent qui écrit = conflits.
- « A query result that only exists at render time is not in your files » : les
  requêtes doivent produire du Markdown réel, pas des vues éphémères.
- « Make the structure machine-readable. Conventions in your head do not
  automate. » : la structure doit être un schéma que les IA peuvent lire.
- Templater + Linter + filing automatique = « 80% de la friction » en moins.
- Daily notes = « the single highest-value automation in Obsidian ».

=== 3. NOTRE ÉTAT MESURÉ (vérifié sur nos fichiers réels, pas théorique) ===
- Vault : 1733 notes, 117 MB. 60 fiches dans Crypto_Projet, 949 signets X,
  journaux dispersés (Cahier/, Index_Maison/...).
- FRONTMATTER : nos 60 fiches Crypto_Projet n'ont AUCUN frontmatter (juste ---
  vides). Les journaux ont des tags inline (#journal #swarm) mais pas de YAML.
- TYPES DE NOTES : aucun type défini. Noms de fichiers MAJUSCULES_SOULIGNÉ_DATE
  mais sans structure commune (une fiche = un titre + du texte, rien d'autre).
- TEMPLATES : plugin désactivé, aucun templates.json. Les IA créent des .md
  bruts via ~15 scripts qui écrivent dans OUTBOX_OBSIDIAN/ (323 fichiers en
  attente), synchronisés par une liste manuelle de cp (fragile).
- LIENS : 0 wikilink dans Crypto_Projet (0/60 fiches). 1341 notes orphelines
  sur 1733 → le graphe est vide.
- SYNC : 3 mécanismes (OUTBOX manuel + obsidian-git + la CLI qu'on vient
  d'ajouter). Plan A en cours : tout basculer sur la CLI (pont avec queue,
  read-back, fail-open disque, circuit breaker, audit — déjà implémenté et
  testé).
- BASES : plugin activé mais 0 base créée. On veut créer Portefeuille.base,
  Veille.base, Signets.base.
- CE QU'ON A DE BIEN : stack IA opérationnelle (famille 6 modèles, Cortana,
  short BTC, satellite aspiration), git maison + journal de chaque action,
  pont CLI bulletproof avec audit, obsidian-git backup auto.

=== 4. NOTRE PLAN DE COPIE (proposé par Buffy, à valider) ===
1) FRONTMATTER UNIFORME sur les fiches : statut, actif, date, source, tags.
2) 4-5 TYPES DE NOTES simplifiés (fiche_actif, synthèse_consultation, veille,
   journal, signet) avec template + propriétés + dossier pour chacun.
3) TEMPLATES : un modèle par type, appliqué par nos agents via le pont CLI
   (obsidian create template=...).
4) DAILY NOTES : activer le plugin + template → journal central des agents.
5) WIKILINKS : chaque fiche actif lie sa synthèse, son événement, son signet →
   le graphe se remplit.
On GARDE notre stack IA et notre journalisation (on ne copie pas tout).

=== 5. VOTRE MISSION (avis strict, pas complaisant, en français) ===
A) VALIDATION DE LA CONFRONTATION : les 13 points du tableau (résumé ci-dessus)
   sont-ils justes ? Y a-t-il un point où on juge mal l'expert, ou où on
   surestime notre état ? Dites-le franchement.
B) LE PLAN DE COPIE (5 points) : est-il bien priorisé ? Trop ambitieux ? Trop
   simple ? Qu'est-ce qui va casser en route (ex. migrer 60 fiches sans
   frontmatter, créer des types sans casser les scripts existants) ?
C) CE QU'ON NE DEVRAIT PAS COPIER : l'expert a un système très lourd (50 types,
   dispatcher, state machines). Pour NOUS (maison de trading avec IA), qu'est-ce
   qui serait de la sur-ingénierie ? Où est la limite juste ?
D) UNE AMÉLIORATION CONCRÈTE de votre cru pour notre plan (ou une correction
   d'un point). Donnez votre avis STRICT global : ce qui est bon, ce qui est
   risqué, ce que vous feriez différemment. NE SOYEZ PAS COMPLAISANT."""


MODELS = ["gemini", "juge", "deepseek"]


def ask_famille(model, timeout=240):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.2,
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
