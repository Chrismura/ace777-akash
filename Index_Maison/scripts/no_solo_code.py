#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Généré par Google Gemini via hub (loi 1quinquies : Ada spécifie, le hub écrit) — 09/08
# Fichier : no_solo_code.py

"""
Traceur d'auteur de code (contre-mesure famille 2, loi 1quinquies)
Compatible Python 3.9+, macOS, stdlib uniquement.
"""

import os
import sys
import re
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Constantes de chemins (absolus et relatifs au Home)
HOME = Path("/Users/christophe")
VAULT = HOME / "Documents" / "Obsidian_ACE777"
MAISON = HOME / "ace777-test-day1"
OUTBOX = MAISON / "Index_Maison" / "OUTBOX_OBSIDIAN"
MEMOIRE_COLLAB = VAULT / "MEMOIRE_COLLAB.md"
CODE_AUTHORS = MAISON / "Index_Maison" / "CODE_AUTHORS.md"
SCRIPTS_DIR = MAISON / "Index_Maison" / "scripts"

HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
TAG_MACHINE = "[LECTURE_COMPLETE_OK]"

# Regex pour détecter l'en-tête d'auteur dans les fichiers Python
REGEX_AUTEUR = re.compile(
    r"^\s*#\s*(?:Généré|Écrit|Codé|Auteur)\s+(?:par\s+|:\s*)(.+)|"
    r"^\s*#\s*auteur\s*:\s*(.+)",
    re.IGNORECASE | re.MULTILINE
)


def obtenir_temps_iso_utc() -> str:
    """Retourne l'horodatage UTC actuel au format ISO 8601 (ex: 2026-08-09T12:57:00Z)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extraire_derniere_preuve() -> Optional[datetime]:
    """
    Recherche la plus RÉCENTE occurrence du TAG_MACHINE dans MEMOIRE_COLLAB.md
    (les entrées récentes sont EN HAUT : on prend le MAX des timestamps, jamais
    la dernière ligne rencontrée). Extrait l'horodatage du format `| YYYY-MM-DDTHH:MMZ |`.
    Fix checker 09/08 : la ligne commence par `|`, la regex doit donc chercher APRÈS le pipe.
    """
    if not MEMOIRE_COLLAB.exists():
        return None

    plus_recent = None
    motif = re.compile(r"\|\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:?\d{2})?)\s*\|")
    try:
        with open(MEMOIRE_COLLAB, "r", encoding="utf-8", errors="replace") as f:
            for ligne in f:
                if TAG_MACHINE in ligne:
                    match = motif.search(ligne)
                    if match:
                        ts_str = match.group(1)
                        if ts_str.endswith("Z"):
                            ts_str = ts_str.replace("Z", "+00:00")
                        try:
                            dt = datetime.fromisoformat(ts_str)
                            if dt.tzinfo is None:
                                dt = dt.replace(tzinfo=timezone.utc)
                            if plus_recent is None or dt > plus_recent:
                                plus_recent = dt
                        except ValueError:
                            pass
    except Exception:
        pass

    return plus_recent


nels_regle_1septies = lambda: (
    (dt := extraire_derniere_preuve()) is not None
    and (datetime.now(timezone.utc) - dt.astimezone(timezone.utc)) < timedelta(hours=24)
)


def verifier_regle_1septies_ou_quitter() -> None:
    """Applique la règle 1septies : la preuve doit avoir moins de 24h."""
    if not nels_regle_1septies():
        print("ERREUR [Règle 1septies] : Preuve de lecture [LECTURE_COMPLETE_OK] absente ou datant de plus de 24h dans MEMOIRE_COLLAB.md.", file=sys.stderr)
        sys.exit(1)


def initialiser_rapport() -> None:
    """Crée ou initialise le fichier CODE_AUTHORS.md avec son en-tête Markdown."""
    verifier_regle_1septies_ou_quitter()
    
    CODE_AUTHORS.parent.mkdir(parents=True, exist_ok=True)
    
    en_tete = (
        "# Rapport de Traçabilité des Auteurs de Code (Loi 1quinquies)\n\n"
        "Ce document consigne les auteurs de chaque script Python pour interdire le code en solo.\n\n"
        "| Date | Fichier | Auteur | Méthode |\n"
        "| :--- | :--- | :--- | :--- |\n"
    )
    
    with open(CODE_AUTHORS, "w", encoding="utf-8") as f:
        f.write(en_tete)
        
    print(f"Fichier initialisé avec succès : {CODE_AUTHORS}")


def analyser_scripts() -> Tuple[int, int, List[Dict[str, str]], List[str]]:
    """
    Scanne les .py de Index_Maison/scripts/ et calcule les métriques.
    Retourne: (total_lignes, total_fichiers, fichiers_avec_auteur, fichiers_sans_auteur)
    """
    total_lignes = 0
    total_fichiers = 0
    fichiers_avec_auteur = []
    fichiers_sans_auteur = []

    if not SCRIPTS_DIR.exists():
        return 0, 0, [], []

    for chemin_script in SCRIPTS_DIR.glob("**/*.py"):
        if chemin_script.is_file():
            total_fichiers += 1
            contenu = ""
            lignes_compte = 0
            try:
                with open(chemin_script, "r", encoding="utf-8", errors="replace") as f:
                    lignes = f.readlines()
                    lignes_compte = len(lignes)
                    contenu = "".join(lignes)
            except Exception:
                pass

            total_lignes += lignes_compte
            rel_path = str(chemin_script.relative_to(MAISON))

            # Recherche d'un en-tête d'auteur
            match = REGEX_AUTEUR.search(contenu)
            if match:
                # Récupère le premier groupe non vide capturé par la regex
                auteur = next((m for m in match.groups() if m is not None), "Inconnu").strip()
                fichiers_avec_auteur.append({
                    "fichier": rel_path,
                    "auteur": auteur,
                    "methode": "en-tete"
                })
            else:
                fichiers_sans_auteur.append(rel_path)

    return total_lignes, total_fichiers, fichiers_avec_auteur, fichiers_sans_auteur


def faire_audit() -> None:
    """Exécute l'audit des scripts et consigne le rapport."""
    verifier_regle_1septies_ou_quitter()

    total_lignes, total_fichiers, avec_auteur, sans_auteur = analyser_scripts()
    date_iso = obtenir_temps_iso_utc()

    print(f"--- RAPPORT D'AUDIT CODE_AUTHORS ({date_iso}) ---")
    print(f"Total fichiers .py : {total_fichiers}")
    print(f"Total lignes de code : {total_lignes}")
    print(f"Fichiers tracés avec en-tête : {len(avec_auteur)}")
    print(f"Fichiers SANS en-tête (code solo potentiel) : {len(sans_auteur)}")
    for f_sans in sans_auteur:
        print(f"  [ALERTE] Sans en-tête : {f_sans}")

    # Si le fichier CODE_AUTHORS.md n'existe pas, on l'initialise d'abord
    if not CODE_AUTHORS.exists():
        initialiser_rapport()

    # Ajout des lignes dans le rapport Markdown (append)
    lignes_rapport = []
    for item in avec_auteur:
        ligne_md = f"| {date_iso[:10]} | {item['fichier']} | {item['auteur']} | {item['methode']} |\n"
        lignes_rapport.append(ligne_md)

    for f_sans in sans_auteur:
        ligne_md = f"| {date_iso[:10]} | {f_sans} | **NON RENSEIGNÉ (Solo ?)** | absent |\n"
        lignes_rapport.append(ligne_md)

    with open(CODE_AUTHORS, "a", encoding="utf-8") as f:
        f.writelines(lignes_rapport)

    print(f"Rapport mis à jour avec succès dans : {CODE_AUTHORS}")

    # Fix audit tiers (famille differente) : un audit qui trouve des scripts sans
    # auteur doit sortir en erreur (exit 1) pour permettre de BLOQUER le pipeline
    # (loi 1quinquies stricte : interdiction du code en solo).
    if sans_auteur:
        print(f"⚠️ {len(sans_auteur)} script(s) SANS auteur — code solo potentiel (loi 1quinquies).", file=sys.stderr)
        sys.exit(1)


def declarer_auteur(fichier: str, auteur: str) -> None:
    """Déclare manuellement l'auteur d'un fichier et met à jour le rapport."""
    verifier_regle_1septies_ou_quitter()

    if not CODE_AUTHORS.exists():
        initialiser_rapport()

    date_iso = obtenir_temps_iso_utc()
    ligne_md = f"| {date_iso[:10]} | {fichier} | {auteur} | manuel |\n"

    with open(CODE_AUTHORS, "a", encoding="utf-8") as f:
        f.write(ligne_md)

    print(f"Déclaration enregistrée : {fichier} écrit par {auteur} (manuel).")


def main() -> None:
    """Point d'entrée principal du script."""
    if len(sys.argv) < 2:
        print("Usage :", file=sys.stderr)
        print("  python3 no_solo_code.py init", file=sys.stderr)
        print("  python3 no_solo_code.py audit", file=sys.stderr)
        print("  python3 no_solo_code.py declare --file <chemin> --author <nom>", file=sys.stderr)
        sys.exit(1)

    commande = sys.argv[1]

    if commande == "init":
        initialiser_rapport()
    elif commande == "audit":
        faire_audit()
    elif commande == "declare":
        # Analyse simple des arguments --file et --author
        fichier_val = None
        auteur_val = None
        
        args = sys.argv[2:]
        i = 0
        while i < len(args):
            if args[i] == "--file" and i + 1 < len(args):
                fichier_val = args[i + 1]
                i += 2
            elif args[i] == "--author" and i + 1 < len(args):
                auteur_val = args[i + 1]
                i += 2
            else:
                i += 1

        if not fichier_val or not auteur_val:
            print("ERREUR : Les arguments --file et --author sont obligatoires pour 'declare'.", file=sys.stderr)
            sys.exit(1)

        declarer_auteur(fichier_val, auteur_val)
    else:
        print(f"Commande inconnue : {commande}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

