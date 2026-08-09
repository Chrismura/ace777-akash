#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Généré par Google Gemini via hub (loi 1quinquies : Ada spécifie, le hub écrit) — 09/08
# Fichier : gatekeeper.py
import sys
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

HOME = Path("/Users/christophe")
VAULT = HOME / "Documents" / "Obsidian_ACE777"
MEMOIRE_PATH = VAULT / "MEMOIRE_COLLAB.md"
INVENTAIRE_PATH = VAULT / "INVENTAIRE_COMPLET.md"
TAG_CHERCHE = "[LECTURE_COMPLETE_OK]"
SEUIL_HEURES = 24.0

def lire_fichier_utf8(chemin: Path) -> str:
    """Lit un fichier en UTF-8 de manière robuste."""
    if not chemin.is_file():
        return ""
    try:
        with open(str(chemin), "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""

def extraire_derniere_preuve(contenu_memoire: str) -> Optional[datetime]:
    """Cherche la plus récente occurrence du tag (MEMOIRE_COLLAB : récentes EN HAUT).
    Fix checker 09/08 : on prend le MAX des timestamps trouvés, jamais la dernière
    ligne rencontrée (qui serait la plus ancienne si le fichier est ordonné récent→ancien)."""
    lignes = contenu_memoire.splitlines()
    plus_recent = None
    
    # Format recherché au début de ligne : | YYYY-MM-DDTHH:MMZ | ou similaire
    motif_ligne = re.compile(r"^\s*\|\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z)\s*\|")

    for ligne in lignes:
        if TAG_CHERCHE in ligne:
            match = motif_ligne.search(ligne)
            if match:
                ts_str = match.group(1)
                try:
                    dt = datetime.strptime(ts_str, "%Y-%m-%dT%H:%MZ")
                    dt = dt.replace(tzinfo=timezone.utc)
                    if plus_recent is None or dt > plus_recent:
                        plus_recent = dt
                except ValueError:
                    pass
    return plus_recent

def compter_fichiers_inventaire() -> int:
    """Lit INVENTAIRE_COMPLET.md pour trouver le nombre de fichiers .md."""
    contenu = lire_fichier_utf8(INVENTAIRE_PATH)
    if not contenu:
        return 0
    
    # Recherche du motif type '1096 fichiers .md'
    motif = re.compile(r"(\d+)\s+fichiers\s+\.md", re.IGNORECASE)
    for ligne in contenu.splitlines():
        match = motif.search(ligne)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                pass
    return 0

def generer_ligne_tag() -> str:
    """Génère la ligne exacte à graver dans MEMOIRE_COLLAB."""
    maintenant_utc = datetime.now(timezone.utc)
    ts_str = maintenant_utc.strftime("%Y-%m-%dT%H:%MZ")
    nb_fichiers = compter_fichiers_inventaire()
    return f"| {ts_str} | Ada | ★ | LECTURE COMPLETE {TAG_CHERCHE} {nb_fichiers} fichiers |"

def verifier_preuve(mode_detail: bool = False) -> int:
    """Vérifie si la preuve est fraîche (< 24h)."""
    contenu = lire_fichier_utf8(MEMOIRE_PATH)
    if not contenu:
        print("AUCUNE PREUVE : Fichier MEMOIRE_COLLAB.md introuvable ou vide.")
        return 1

    dt_preuve = extraire_derniere_preuve(contenu)
    if dt_preuve is None:
        print("AUCUNE PREUVE : Tag [LECTURE_COMPLETE_OK] introuvable ou horodatage invalide.")
        return 1

    maintenant = datetime.now(timezone.utc)
    delta = maintenant - dt_preuve
    age_heures = delta.total_seconds() / 3600.0

    if mode_detail:
        print(f"Horodatage de la dernière preuve : {dt_preuve.strftime('%Y-%m-%dT%H:%MZ')}")
        print(f"Âge calculé : {age_heures:.1f} heures")

    if age_heures < SEUIL_HEURES:
        print(f"OK preuve fraîche ({age_heures:.1f}h).")
        return 0
    else:
        print(f"PREUVE PÉRIMÉE ({age_heures:.1f}h) — relire INVENTAIRE_COMPLET.md et graver le tag.")
        return 1

def main() -> None:
    args = sys.argv[1:]
    
    # Gestion de l'option --tag
    if "--tag" in args:
        print(generer_ligne_tag())
        sys.exit(0)

    # Gestion de l'option --detail
    mode_detail = "--detail" in args

    # Exécution de la vérification standard
    code_sortie = verifier_preuve(mode_detail=mode_detail)
    sys.exit(code_sortie)

if __name__ == "__main__":
    main()

