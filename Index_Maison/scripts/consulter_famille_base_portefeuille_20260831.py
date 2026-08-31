#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_base_portefeuille_20260831.py — Conception de la BASE
PORTEFEUILLE Obsidian soumise à la FAMILLE (3 membres : gemini, juge, deepseek).

Règle Christophe (31/08) : « pour ce set up, toujours utiliser la famille et
ensuite on valide ». Le set up Obsidian avance (pont CLI ✅, gatekeeper ✅, daily
notes ✅). Prochaine étape : la base Portefeuille (chantier C de notre plan) —
le premier tableau vivant dans Obsidian.

Résultat : dossier CONSULTATION_FAMILLE_BASE_PORTEFEUILLE_20260831/AVIS_*.md
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_BASE_PORTEFEUILLE_20260831")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 31/08/2026) — CONCEPTION DE LA BASE PORTEFEUILLE OBSIDIAN

=== 1. OÙ ON EN EST (set up Obsidian ACE777, règle famille puis validation) ===
- Pont CLI obsidian_cli_bridge.py : écrit dans le vault via la CLI officielle,
  queue séquentielle, read-back hash, fallback disque, circuit breaker, audit.
- GATEKEEPER : 4 types stricts (actif, signal, synthese_ia, journal), validation
  des propriétés AVANT écriture, compilation markdown conforme (frontmatter YAML
  échappé + body brut). Testé 6/6.
- DAILY NOTES activées (Cahier/YYYY-MM-DD.md avec template journal).
- Vault : 1733 notes, ~60 fiches actifs dans Crypto_Projet/ (actuellement SANS
  frontmatter — à structurer pour les nouvelles créations, Day Zero rule),
  949 signets X, portefeuille Hulk paper (16 positions en paper trading MEXC).

=== 2. LE CHANTIER C : BASE PORTEFEUILLE (notre plan, à concevoir) ===
On veut créer une Base Obsidian (.base — la base de données native) qui agrège
nos fiches actifs en un TABLEAU DE BORD VIVANT, filtrable et visible dans l'app.
Objectif : remplacer/épauler le tableau « score Hulk vs Hold » du cockpit par une
vraie base Obsidian.

LES DONNÉES QU'ON A (réelles, chez nous) :
- Fiches actifs (Crypto_Projet/) : EDEL, CHIP, RED, RWAINC (Allo), QNT, MNSRY,
  CC, HBAR, XRP, BTC, ETH... chacune avec son deepdive, son set up, son statut.
- État Hulk paper : chaque position a un actif, un prix d'entrée, un PnL, un
  statut (ouverte/fermée), un bag size.
- Signets X (949) : veille sur ces actifs, événements, tendances.
- Daily notes (Cahier/) : activité journalière des agents.

CE QU'ON IMAGINE (à valider/améliorer par vous) :
- Un frontmatter uniforme sur les nouvelles fiches actifs (via le gatekeeper,
  type actif) : actif, statut (brouillon/valide/archive), date, source, tags.
- Une base Portefeuille.base avec une vue table : actif, statut, date de fiche,
  source, tags + peut-être des formules (jours depuis création, nb de tags...).
- Éventuellement une vue Kanban (le roadmap Obsidian vient de lancer Kanban view
  pour Bases) : colonnes = statut (brouillon/valide/archive).

=== 3. LES QUESTIONS OUVERTES (vos avis comptent) ===
A) QUELLES COLONNES/PROPRIÉTÉS doit avoir la base Portefeuille pour être VRAIMENT
   utile à Christophe (pas juste jolie) ? On a le choix entre : propriétés de
   fiche (statut, date, source), propriétés calculées (formules Bases), liens
   vers d'autres notes. Que mettriez-vous en colonnes et pourquoi ?

B) COMMENT RELIER la base aux DONNÉES VIVANTES (Hulk paper, PnL) ? Les Bases
   Obsidian lisent le frontmatter des notes. Le PnL de Hulk est dans des JSON
   (state du moteur paper). Doit-on : (1) écrire un résumé PnL dans le
   frontmatter de chaque fiche actif via le pont (journée), (2) créer des notes
   « état portefeuille » périodiques avec le PnL agrégé, (3) autre chose ?

C) STRUCTURE : une base unique (Portefeuille.base) avec plusieurs vues (table,
   kanban, cards) OU plusieurs bases (Portefeuille, Veille, Signets) ? Qu'est-ce
   qui est le plus maintenable pour nous ?

D) UNE AMÉLIORATION CONCRÈTE de votre cru pour ce chantier (ou une correction).
   Donnez votre avis STRICT : ce qui est bon, ce qui est risqué, ce que vous
   feriez différemment. NE SOYEZ PAS COMPLAISANT. Rappel : on ne veut PAS de la
   sur-ingénierie (pas de 50 types, pas de state machines complexes) — on veut
   un tableau de bord UTILE, simple, maintenable, nourri par nos IA."""


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
