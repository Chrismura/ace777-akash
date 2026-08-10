#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deleguer_codeur.py — LE CODEUR DU HUB CODE, PAS MOI (loi 1quinquies).

Déclaration Christophe (10/08) : « ce que je voulais, c'est faire coder au
codeur, pas TOI. C'est clair, il est l'expert. »

LE FLUX OBLIGATOIRE (gravé dans CONTRAT_AUTOGESTION 1quinquies) :
    1. SPEC par Ada (quoi + contraintes + pièges) — jamais de code sans spec
    2. CHOIX du modèle : task code.ia (inferx-coder Qwen3-Coder, fallback nvidia)
    3. Le codeur du hub ÉCRIT le code
    4. Ada INTÈGRE + teste en réel
    5. Audit tiers famille différente (1quater)
    6. GO Christophe

CE SCRIPT : point d'entrée UNIQUE pour déléguer au codeur. Incassable :
- timeout=None (soumettre_hub_illimite.py)
- lancé DÉTACHÉ (lancer_detache.py, start_new_session) → survit à tout
- max_tokens 8000 minimum (une réponse tronquée = code inutilisable)

USAGE :
    python3 deleguer_codeur.py <fichier_spec.md> <fichier_sortie.md> [max_tokens]
    # lance le codeur DÉTACHÉ, retourne immédiatement
    # poller <fichier_sortie.md> pour la réponse (réponse HUB dedans)

EXEMPLE :
    python3 deleguer_codeur.py SPEC_ma_fonction.md CODE_ma_fonction.md 8000
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SOUMETTRE = os.path.join(ROOT, "soumettre_hub_illimite.py")
LANCER = os.path.join(ROOT, "lancer_detache.py")


def main():
    if len(sys.argv) < 3:
        print("Usage: deleguer_codeur.py <spec.md> <sortie.md> [max_tokens]")
        sys.exit(2)
    spec_path = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[2])
    max_tokens = sys.argv[3] if len(sys.argv) > 3 else "8000"

    if not os.path.exists(spec_path):
        print(f"[ECHEC] spec introuvable: {spec_path}", file=sys.stderr)
        sys.exit(1)

    # En-tête de la spec : rappel du rôle (le codeur code, pas Ada)
    with open(spec_path, encoding="utf-8") as f:
        spec = f.read()
    header = (
        "SYSTEME ACE777 - loi 1quinquies : TU ES LE CODEUR DU HUB (expert).\n"
        "Ada (orchestratrice) SPECIFIE, TU CODES. Produis du code Python 3.9\n"
        "stdlib / bash macOS, non fatal, commentaires en francais, pret a copier.\n"
        "Une seule mission, rien d'autre. Contrat de sortie : le code complet.\n\n"
        "=== SPEC (par Ada) ===\n"
    )
    mission_path = spec_path + ".mission.txt"
    try:
        with open(mission_path, "w", encoding="utf-8") as f:
            f.write(header + spec)
        # Vérification que le fichier est bien écrit et non vide
        if os.path.getsize(mission_path) == 0:
            raise IOError("fichier mission vide")
    except Exception as e:
        print(f"[ECHEC] impossible d'écrire la mission: {e}", file=sys.stderr)
        sys.exit(1)

    # Lancement détaché : retourne immédiatement, le codeur travaille en paix
    try:
        r = subprocess.run(
            [sys.executable, LANCER, sys.executable, SOUMETTRE,
             "code.ia", mission_path, out_path, max_tokens],
            capture_output=True, text=True, timeout=60)  # 60s au lieu de 30s
    except subprocess.TimeoutExpired:
        print("[ECHEC] timeout lancement détaché (60s)", file=sys.stderr)
        sys.exit(1)
    print(r.stdout.strip() or r.stderr.strip())
    print(f"[OK] codeur lancé détaché → poll {out_path}")


if __name__ == "__main__":
    main()
