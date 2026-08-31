#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
backfill_frontmatter_actifs_20260831.py — Injection du frontmatter minimal sur
les fiches actifs existantes (GO Christophe 31/08, arbitrage Buffy validé).

Pourquoi : la base Portefeuille (filtre type: actif) serait vide si on ne
structure pas l'existant. On injecte UNIQUEMENT un frontmatter minimal :
type: actif, actif: <nom>, statut: valide, date: <mtime>, source: backfill.
Les autres champs (bag_hulk, setup, tags) se peupleront organiquement.

Précautions :
- Backup .bak de chaque fichier modifié (dossier _backfill_backup/).
- NE TOUCHE PAS aux fiches qui ont déjà un frontmatter avec type:.
- NE TOUCHE PAS aux fiches non-actifs évidentes (synthèses, cadres, acteurs...)
  → on se limite aux fiches dont le nom évoque UN actif (pas de mots-clés
  génériques : ACTEURS, CADRE, CONSEILS, CONSULTATION, BRIEF, SYNTHESE, THESE,
  BILAN, RAPPORT, VEILLE, PLAN, PROTOCOLE, GLOSSAIRE).
"""
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path.home() / "Documents/Obsidian_ACE777"
DIR = VAULT / "Crypto_Projet"
BACKUP = DIR / "_backfill_backup"

# Mots-clés d'exclusion : fiches thématiques, PAS des fiches actif
EXCLUS = [
    "ACTEURS", "CADRE", "CONSEILS", "CONSULTATION", "BRIEF", "SYNTHESE",
    "THESE", "BILAN", "RAPPORT", "VEILLE", "PLAN", "PROTOCOLE", "GLOSSAIRE",
    "INDEX", "README", "LIRE", "ARCHIVE", "COLLAB", "MEMOIRE", "REPONSE",
    "SPEC", "HISTORIQUE", "TEMPLATE", "CHIFFRES", "DEEPDIVE_GLOBAL",
    "DOCTRINE", "FICHE_IA", "GATE_IO", "HORS_MAINSTREAM", "RECHERCHE",
    "VERIFICATION", "OBSERVER",
]


def est_fiche_actif(name):
    """Nom de fichier évoquant un actif (et pas une fiche thématique)."""
    upper = name.upper()
    if any(k in upper for k in EXCLUS):
        return False
    # Retire l'extension et la date éventuelle (AAAAMMJJ)
    base = re.sub(r"_\d{8}$", "", name[:-3])
    # Un actif = nom court sans espaces ni séparateurs thématiques
    base_upper = base.upper().replace("_", " ").strip()
    if len(base_upper.split()) > 4:  # nom trop long = probablement thématique
        return False
    return True


def extraire_actif(name):
    """Extrait le nom d'actif du fichier (sans date ni extension)."""
    base = re.sub(r"_\d{8}$", "", name[:-3])
    base = re.sub(r"^(FICHE|NOTE)_?", "", base, flags=re.IGNORECASE)
    return base.replace("_", " ").strip() or name[:-3]


def main():
    BACKUP.mkdir(exist_ok=True)
    modifie, ignore, deja = [], [], []
    for f in sorted(DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        # Déjà un frontmatter avec type ?
        if content.startswith("---"):
            m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if m and "type:" in m.group(1):
                deja.append(f.name)
                continue
        # Fiche thématique ?
        if not est_fiche_actif(f.name):
            ignore.append(f.name)
            continue
        # Backup + injection minimale
        shutil.copy2(f, BACKUP / f.name)
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")
        actif = extraire_actif(f.name)
        fm = (
            "---\n"
            f"type: actif\n"
            f"actif: {actif}\n"
            "statut: valide\n"
            f"date: {mtime}\n"
            "source: backfill\n"
            "tags: []\n"
            "---\n\n"
        )
        f.write_text(fm + content, encoding="utf-8")
        modifie.append(f.name)

    print(f"=== RÉSULTAT ===")
    print(f"Modifiées (frontmatter injecté) : {len(modifie)}")
    for n in modifie:
        print(f"  + {n}")
    print(f"Déjà structurées (inchangées) : {len(deja)}")
    print(f"Exclues (thématiques) : {len(ignore)}")
    print(f"Backup dans : {BACKUP}")


if __name__ == "__main__":
    main()
