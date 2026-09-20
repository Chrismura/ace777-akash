#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Généré par Google Gemini via hub (loi 1quinquies : Ada spécifie, le hub écrit) — 09/08
# Fichier : gatekeeper.py
#
# ⚠️ 20/09/2026 — CE FICHIER N'EST PLUS QU'UNE PORTE D'ENTRÉE.
#   Toute la logique de la preuve de lecture vit désormais dans `preuve_lecture.py`
#   (une seule vérité, règle d'or #6) parce qu'elle était dupliquée ici ET dans
#   `superviseur_auto.py` — deux codes, deux verdicts possibles pour un seul fait.
#   Effet mesuré de l'ancienne règle : re-lire 2 127 lignes (~35 000 tokens) tous les
#   24 h même quand l'inventaire n'avait pas changé d'un fichier. La nouvelle règle
#   rend la preuve valable tant que la carte du coffre n'a pas bougé.
#   Interface conservée à l'identique : verif-setup appelle ce fichier et lit stdout.
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from preuve_lecture import verifier, graver, extraire_derniere_preuve, lire_utf8, MEMOIRE_PATH
except Exception as e:  # fail-closed : jamais de validation sur un juge cassé
    print(f"REFUS : juge de preuve indisponible ({e})")
    sys.exit(1)


def main() -> None:
    args = sys.argv[1:]

    if "--tag" in args:
        print(graver())
        sys.exit(0)

    ok, raison, age_h, _empreinte = verifier()

    if "--detail" in args:
        dt = extraire_derniere_preuve(lire_utf8(MEMOIRE_PATH))
        if dt is not None:
            print(f"Horodatage de la dernière preuve : {dt.strftime('%Y-%m-%dT%H:%MZ')}")
        if age_h is not None:
            print(f"Âge calculé : {age_h:.1f} heures")
        print(f"Raison : {raison}")

    if ok:
        print(f"OK preuve fraîche ({raison}).")
        sys.exit(0)

    print(f"PREUVE PÉRIMÉE ({raison}) — relire INVENTAIRE_COMPLET.md et graver le tag.")
    sys.exit(1)


if __name__ == "__main__":
    main()
