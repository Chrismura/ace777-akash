#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preuve_lecture.py — UNE SEULE VÉRITÉ pour la « preuve de lecture du coffre » (règle 1septies).

POURQUOI CE FICHIER EXISTE (réparation du 20/09/2026) :
    Deux organes jugeaient la MÊME preuve chacun avec son propre code
    (`gatekeeper.py` ~ BLOQUANT pour verif-setup, et `superviseur_auto.py` ~ rappel) :
    deux vérités pour un seul fait — la maison a déjà payé cette erreur (règle d'or #6).

    Pire : les deux exigeaient une preuve de MOINS DE 24 H, même quand
    `INVENTAIRE_COMPLET.md` n'avait pas changé d'un seul fichier. Conséquence mesurée :
    il fallait relire 2 127 lignes (~35 000 tokens) TOUS LES JOURS, pour rien.
    C'est exactement le gaspillage que le prototype ne peut plus se payer.

LA RÈGLE (nouvelle) : une preuve reste valable tant que CE QU'ELLE ATTESTE n'a pas changé.
    - fraîche si (a) moins de 24 h, OU
    - (b) l'EMPREINTE de l'inventaire (liste des fichiers, sans horodatage) est IDENTIQUE
      à celle enregistrée lors de la dernière lecture prouvée.
    Autrement dit : on relit quand la carte change, pas quand l'horloge tourne.
    Table de vérité : inventaire inchangé + preuve d'hier -> VALABLE (0 token dépensé).
                      inventaire changé (fichier ajouté/retiré) -> RE-LECTURE exigée.
    (L'empreinte ignore l'horodatage de génération et les compteurs : elle ne bouge que
     si la STRUCTURE du coffre bouge.)

CLI (compatible avec l'ancien `gatekeeper.py`) :
    python3 preuve_lecture.py            -> vérifie (exit 0 frais / exit 1 à relire)
    python3 preuve_lecture.py --detail   -> idem + âge et raison
    python3 preuve_lecture.py --tag      -> grave la preuve (état + ligne à coller) et affiche la ligne
"""
import sys
import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

HOME = Path("/Users/christophe")
VAULT = HOME / "Documents" / "Obsidian_ACE777"
INVENTAIRE_PATH = VAULT / "INVENTAIRE_COMPLET.md"
# Le journal réel de la maison vit dans le repo (fix autopsie V7 du 11/09).
MEMOIRE_PATH = HOME / "ace777-test-day1" / "Index_Maison" / "MEMOIRE_COLLAB.md"
ETAT_PATH = HOME / "ace777-test-day1" / "Index_Maison" / "strategie" / "preuve_lecture.json"

TAG_CHERCHE = "[LECTURE_COMPLETE_OK]"
SEUIL_HEURES = 24.0

# Lignes volatiles de l'inventaire : horodatage de génération. Tout le reste est
# structurel (liste de fichiers + compteurs) et ne change que si le coffre change.
_MOTIF_VOLATILE = re.compile(r"(g[ée]n[ée]r[ée]\s+le|^genere\s*:)", re.IGNORECASE)
_MOTIF_LIGNE_TS = re.compile(r"^\s*\|\s*(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2})Z\s*\|")


def lire_utf8(chemin: Path) -> str:
    if not chemin.is_file():
        return ""
    try:
        with open(str(chemin), "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


def empreinte_inventaire() -> str:
    """Empreinte de la STRUCTURE de l'inventaire (liste des fichiers), horodatage exclu."""
    contenu = lire_utf8(INVENTAIRE_PATH)
    if not contenu:
        return ""
    lignes = [l.strip() for l in contenu.splitlines()
              if l.strip() and not _MOTIF_VOLATILE.search(l.strip())]
    return hashlib.sha256("\n".join(lignes).encode("utf-8")).hexdigest()


def _charger_etat() -> dict:
    try:
        with open(str(ETAT_PATH), "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _ecrire_etat(data: dict) -> None:
    ETAT_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = ETAT_PATH.with_suffix(".json.tmp")
    with open(str(tmp), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    import os
    os.replace(str(tmp), str(ETAT_PATH))


def extraire_derniere_preuve(contenu_memoire: str):
    """Timestamp de la preuve la plus RÉCENTE du journal (le journal est ordonné récent→ancien)."""
    plus_recent = None
    for ligne in contenu_memoire.splitlines():
        if TAG_CHERCHE not in ligne:
            continue
        m = _MOTIF_LIGNE_TS.search(ligne)
        if not m:
            continue
        try:
            dt = datetime.strptime(f"{m.group(1)}T{m.group(2)}Z", "%Y-%m-%dT%H:%MZ")
            dt = dt.replace(tzinfo=timezone.utc)
            if plus_recent is None or dt > plus_recent:
                plus_recent = dt
        except ValueError:
            pass
    return plus_recent


def compter_fichiers_inventaire() -> int:
    contenu = lire_utf8(INVENTAIRE_PATH)
    m = re.search(r"(\d+)\s+fichiers\s+\.md", contenu, re.IGNORECASE)
    try:
        return int(m.group(1)) if m else 0
    except ValueError:
        return 0


def verifier():
    """Retourne (ok, raison, age_heures|None, empreinte)."""
    empreinte = empreinte_inventaire()
    contenu = lire_utf8(MEMOIRE_PATH)
    if not contenu:
        return False, "journal introuvable ou vide", None, empreinte

    dt_preuve = extraire_derniere_preuve(contenu)
    if dt_preuve is None:
        return False, f"aucun tag {TAG_CHERCHE} dans le journal", None, empreinte

    age_h = (datetime.now(timezone.utc) - dt_preuve).total_seconds() / 3600.0
    if age_h < SEUIL_HEURES:
        return True, f"preuve fraîche ({age_h:.1f} h)", age_h, empreinte

    # Preuve « périmée » à l'horloge : on regarde si la carte a bougé.
    etat = _charger_etat()
    if empreinte and etat.get("empreinte_inventaire") == empreinte:
        return True, (f"preuve de {dt_preuve.strftime('%Y-%m-%dT%H:%MZ')} toujours valable — "
                      f"l'inventaire n'a pas changé depuis (aucune re-lecture nécessaire)"), age_h, empreinte

    return False, (f"preuve périmée ({age_h:.1f} h) ET l'inventaire a changé depuis la dernière lecture "
                   f"— relire INVENTAIRE_COMPLET.md"), age_h, empreinte


def generer_ligne_tag() -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    return f"| {ts} | Ada | ★ | LECTURE COMPLETE {TAG_CHERCHE} {compter_fichiers_inventaire()} fichiers |"


def graver() -> str:
    """Grave la preuve : enregistre l'empreinte de l'inventaire lu + rend la ligne à coller."""
    ligne = generer_ligne_tag()
    m = _MOTIF_LIGNE_TS.match(ligne)
    ts = f"{m.group(1)}T{m.group(2)}Z" if m else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    _ecrire_etat({
        "dernier_ts": ts,
        "empreinte_inventaire": empreinte_inventaire(),
        "fichiers": compter_fichiers_inventaire(),
        "note": "Empreinte de l'inventaire AU MOMENT de la lecture prouvée (preuve_lecture.py --tag).",
    })
    return ligne


def main() -> None:
    args = sys.argv[1:]
    if "--tag" in args:
        print(graver())
        sys.exit(0)

    ok, raison, age_h, _ = verifier()
    if "--detail" in args:
        if age_h is not None:
            print(f"Âge calculé : {age_h:.1f} heures")
    if ok:
        print(f"OK preuve fraîche ({raison}).")
        sys.exit(0)
    print(f"PREUVE PÉRIMÉE — {raison}")
    sys.exit(1)


if __name__ == "__main__":
    main()
