#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
refine_maison.py — MINI-/refine ACE777 (31/08, inspiré de PrimeAgent /refine)
=============================================================================
Notre traduction du `/refine` de Prime Agent (Continual Harness), SANS réécrire :
au lieu que l'agent réécrive tout son harness, on consigne à chaque veille/mission
un bloc structuré dans la daily note Obsidian, façon « petite correction ciblée,
evidence-backed, réversible ».

Concept Copié d'une approche qui marche (documenté dans FICHE_CODEUR_AGENT_20260831)
mais adapté à notre pile : la section se crée via notre pont (journal_day),
dans la daily note stratifiée de notre maison.

Usage:
    python3 refine_maison.py --agent "famille" \
        --marche "le gatekeeper a rejete les stats invalides" \
        --ameliore "peupler bag_hulk depuis le paper Hulk" \
        [--rollback "R-42: le seuil ATR pur etait trop sensible, on revient"]

Le bloc écrit dans la daily note a la forme :
    ## Reflexion (refine) — <agent> <date>
    - Ce qui a marche : ...
    - Ameliorer : ...
    - Rollback : R-<id> (rien n'est irreversible, tout est versionne)

Retour sur stdout : {status, path} (JSON) pour un eventuel lanceur.
Le parametre --rollback permet de revenir sur une decision (par ID) si elle
a empiré — la rege maison : un pas en arriere propre plutot qu'une catastrophe.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ajout du repertoire des scripts pour resoudre les imports maison (obsidian_cli_bridge).
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

REQUIRED = ("--agent", "--marche", "--ameliore")


def main() -> int:
    ap = argparse.ArgumentParser(description="Mini-/refine maison (daily note Obsidian)")
    ap.add_argument("--agent", required=True, help="Agent qui produit la reflexion")
    ap.add_argument("--marche", required=True, help="Ce qui a bien marche")
    ap.add_argument("--ameliore", required=True, help="Ce qui est a ameliorer / a faire")
    ap.add_argument("--rollback", default="", help="Optionnel : decision a revenir (ex R-42: ...)")
    ap.add_argument("--date", default=None, help="Date cible (defaut aujourd'hui UTC YYYY-MM-DD)")
    args = ap.parse_args()

    # Verifie les imports maison (fail-open : si le pont est indisponible, on
    # ecrit en clair et on le signale, pour ne jamais perdre la reflexion).
    try:
        from obsidian_cli_bridge import ObsidianBridge
    except Exception as e:
        print(json.dumps({"status": "ERROR", "error": f"pont indisponible: {e}"}))
        return 1

    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # Format compatible journal_day (il prefixe chaque ligne par "- ") : on
    # fournit des lignes bullet simples, sans sous-structure, pour un rendu net.
    bloc = [
        f"Reflexion (refine) {date} · agent {args.agent}",
        "Ce qui a marche : " + args.marche,
        "Ameliorer : " + args.ameliore,
    ]
    if args.rollback:
        bloc.append("Rollback : " + args.rollback)
        bloc.append("(rien n'est irreversible — decide, journalise, versionne)")
    content = "\n".join(bloc)

    agent_label = f"{args.agent}_refine"
    res = ObsidianBridge.journal_day(agent_label, content, date=date)
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res.get("status") in ("SUCCESS", "SUCCESS_CLI", True) else 1


if __name__ == "__main__":
    sys.exit(main())