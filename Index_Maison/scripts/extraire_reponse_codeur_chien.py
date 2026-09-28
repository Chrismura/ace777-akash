#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrait les livrables du CODEUR (REPONSE_CODEUR_CHIEN_DE_GARDE_20260910.md)
vers leurs fichiers réels — étape V4 (GO Christophe 10/09 : « go » sur la
proposition « installe le chien : fichiers + tests harnais + plist, sans
l'activer tant que la famille n'a pas validé le premier rapport »).

Lecture seule sur la réponse ; écrit SEULEMENT les fichiers nouveaux listés.
Ne touche PAS au moteur, NE charge AUCUN plist en launchd.
"""
import os
import re
import sys

RACINE = os.path.expanduser("~/ace777-test-day1")
REPONSE = os.path.join(RACINE, "Index_Maison", "REPONSE_CODEUR_CHIEN_DE_GARDE_20260910.md")

# (titre de section attendu, chemin de destination)
LIVRABLES = [
    ("chien_de_garde.py",
     "Index_Maison/scripts/chien_de_garde.py"),
    ("generer_registre_organes.py",
     "Index_Maison/scripts/generer_registre_organes.py"),
    ("criticite_organes.json",
     "Index_Maison/strategie/criticite_organes.json"),
    ("com.ace777.chien-de-garde.plist",
     "Index_Maison/plists/com.ace777.chien-de-garde.plist"),
    ("CHIEN_RAPPORT.md",
     "Index_Maison/thermo/CHIEN_RAPPORT.md"),
    ("test_chien_de_garde.py",
     "Index_Maison/scripts/test_chien_de_garde.py"),
]


def extraire_blocs(texte):
    """Retourne {titre_section: contenu_dernier_bloc_fermé}."""
    sections = {}
    courant = None
    for m in re.finditer(r"^### (.*?)\s*$|```(\w*)\n(.*?)\n```",
                         texte, flags=re.M | re.S):
        if m.group(1) is not None:
            courant = m.group(1).strip()
        elif courant:
            sections.setdefault(courant, m.group(3))
    return sections


def main():
    with open(REPONSE, encoding="utf-8") as f:
        texte = f.read()
    blocs = extraire_blocs(texte)
    ecris, manquants = [], []
    for titre, dest_rel in LIVRABLES:
        contenu = None
        for cle, bloc in blocs.items():
            if titre in cle and bloc.strip():
                contenu = bloc
                break
        if contenu is None:
            manquants.append(titre)
            continue
        dest = os.path.join(RACINE, dest_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        existe = os.path.exists(dest)
        if existe:  # 1 écriture = 1 backup
            bak = "/tmp/" + os.path.basename(dest) + ".bak-avant-extraction-V4-20260910"
            with open(dest, encoding="utf-8") as src:
                with open(bak, "w", encoding="utf-8") as out:
                    out.write(src.read())
            print(f"backup: {bak}")
        with open(dest, "w", encoding="utf-8") as out:
            out.write(contenu if contenu.endswith("\n") else contenu + "\n")
        ecris.append((dest_rel, "remplacé" if existe else "créé", len(contenu)))
    for dest_rel, statut, n in ecris:
        print(f"écrit : {dest_rel} ({statut}, {n} chars)")
    if manquants:
        print("MANQUANTS :", ", ".join(manquants))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
