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
    - (b) l'EMPREINTE de la CARTE est IDENTIQUE à celle enregistrée lors de la dernière
      lecture prouvée.
    Autrement dit : on relit quand la carte change, pas quand l'horloge tourne.

RE-SCOPE DE L'EMPREINTE — 29/09/2026 (vérification demandée : « trancher le verrou
de verif-setup »). MESURE : l'ancienne empreinte portait sur TOUTES les lignes de
l'inventaire, annexe des fichiers comprise. Or le coffre PRODUIT des fichiers tous les
jours (SNIFF_*, ROULEMENT_IA_*, Journal_*, VEILLE_HUB_*) : mesuré 1971 → **2048** fichiers .md
entre la preuve du 20/09 et l'inventaire du 27/09, et la preuve était périmée depuis **207 h**.
(Chiffre corrigé le 29/09, classe E10 : cette ligne annonçait « 2084 », qui est le TOTAL de
l'inventaire — « 2048 fichiers .md · 2084 fichiers au total » — alors que le compteur de CE
fichier (`compter_fichiers_inventaire()`, motif `N fichiers .md`) lit les `.md`. On ne compare
que des chiffres pris à la MÊME mesure.) Conséquence : la branche « preuve encore valable, l'inventaire n'a pas
changé » ne pouvait JAMAIS se déclencher — un gate qui crie tous les jours sans qu'aucun
humain n'ait rien à relire est exactement le faux positif R14 que la maison combat.
L'empreinte porte désormais sur la CARTE (les faits qu'une lecture atteste) : le tableau
des fichiers clés + le SQUELETTE des dossiers (noms, sans les compteurs) + les sections
SCRIPTS / SERVICES LAUNCHD / PROVIDERS. Elle ne bouge donc que si la STRUCTURE change
(dossier ajouté/retiré, fichier clé ajouté/retiré) — pas quand le coffre écrit un journal.
L'annexe « TOUS LES FICHIERS » reste dans l'inventaire : elle n'invalide plus la preuve.

SECOND DÉFAUT DU MÊME VERROU, TROUVÉ EN VÉRIFIANT (29/09/2026) : le lecteur d'horodatage
exigeait `HH:MM` (`2026-09-20T17:45Z`) alors que le journal écrit le plus souvent `HHMM`
(`2026-09-29T0900Z`). Conséquence mesurée : le tag que `--tag` venait de graver était
INVISIBLE pour ce même fichier — `--detail` annonçait « preuve de 2026-09-20T17:45Z »
(207,4 h) alors que le tag du 29/09 09:00Z était en tête du journal. La branche « fraîche
(< 24 h) » ne pouvait donc JAMAIS se déclencher sur une ligne au format maison. Corrigé :
le motif accepte les deux formats (même tolérance que le gardien E13).

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
# Deux formats d'horodatage dans le journal : `2026-09-29T0900Z` (le plus courant chez la
# maison) ET `2026-09-20T17:45Z`. La première version exigeait le deux-points : le tag
# gravé par --tag dans le format maison était donc INVISIBLE pour ce lecteur (mesuré le
# 29/09 : la preuve du 29/09 09:00Z était ignorée, ce lecteur retombait sur celle du 20/09).
_MOTIF_LIGNE_TS = re.compile(r"^\s*\|\s*(\d{4}-\d{2}-\d{2})[T ](\d{2}):?(\d{2})Z\s*\|")


def lire_utf8(chemin: Path) -> str:
    if not chemin.is_file():
        return ""
    try:
        with open(str(chemin), "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


_MOTIF_ENTETE_DOSSIER = re.compile(r"^###\s+(.+?)\s*(?:—|-{2,})?\s*(?:\d+\s*\.md.*)?$")


def _squelette_dossier(ligne: str) -> str:
    """`### Signets_X/2026-09 — 175 .md · 0 autres` -> `### Signets_X/2026-09`
    (le NOM du dossier est structurel ; les compteurs grandissent tous les jours)."""
    m = _MOTIF_ENTETE_DOSSIER.match(ligne.strip())
    return "### " + (m.group(1).strip() if m else ligne.strip()[4:].strip())


def empreinte_inventaire() -> str:
    """Empreinte de la CARTE (fichiers clés + squelette des dossiers + scripts/services).

    L'annexe exhaustive « TOUS LES FICHIERS » est EXCLUE : c'est la production du coffre
    (elle grossit d'une dizaine de fichiers/jour) et elle n'atteste pas ce qu'une lecture
    prouve. Voir le re-scope 29/09/2026 en tête de fichier.
    """
    contenu = lire_utf8(INVENTAIRE_PATH)
    if not contenu:
        return ""
    lignes, dans_annexe = [], False
    for l in contenu.splitlines():
        s = l.strip()
        if not s or _MOTIF_VOLATILE.search(s):
            continue
        if s.startswith("## "):
            dans_annexe = s.startswith("## 📁")     # début de l'annexe exhaustive
            lignes.append(s)
            continue
        if dans_annexe:
            if s.startswith("### "):                # squelette seulement, sans les compteurs
                lignes.append(_squelette_dossier(s))
            continue                                # les fichiers listés sont ignorés
        lignes.append(s)
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
            dt = datetime.strptime(f"{m.group(1)}T{m.group(2)}:{m.group(3)}Z", "%Y-%m-%dT%H:%MZ")
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
    ts = f"{m.group(1)}T{m.group(2)}:{m.group(3)}Z" if m else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
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
