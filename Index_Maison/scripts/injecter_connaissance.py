#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Injecteur de connaissance ACE777.
- --projet SYMBOLE : extrait la fiche projet (résumé exécutif ≤ max-tokens, SANS leçons).
- --lecons : ajoute les leçons (sizing/stops/garde-fous) — usage EXPLICITE uniquement.
- --sujet TEXTE : détection automatique de projet (symbole/nom présent dans le texte).
- Filtrage strict : faits etat == "verifie" ET score >= 0.6 uniquement.
- Rotation si >3 projets pertinents : 2 plus récents + 1 aléatoire (anti-biais récence).
Sortie : section « CONNAISSANCE PROJET » prête à coller dans un BRIEF famille/Cortana.
"""

import os
import sys
import re
import json
import argparse
import random
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
INDEX_MAISON = os.path.join(BASE_DIR, "Index_Maison")
STRATEGIE_DIR = os.path.join(INDEX_MAISON, "strategie")
CONNAISSANCE_PATH = os.path.join(STRATEGIE_DIR, "CONNAISSANCE_PROJETS.json")

STOP_FILE = os.path.join(STRATEGIE_DIR, "STOP")
STOP_ALL_FILE = os.path.expanduser("~/ace777-test-day1/Index_Maison/STOP_ALL")

SEUIL_INJECTION = 0.6
MAX_TOKENS_DEFAUT = 500


def check_kill_switch():
    if os.path.exists(STOP_FILE) or os.path.exists(STOP_ALL_FILE):
        print("[KILL] Kill switch activé. Arrêt propre.", file=sys.stderr)
        sys.exit(0)


def load_connaissance():
    if not os.path.exists(CONNAISSANCE_PATH):
        return {"projets": {}}
    try:
        with open(CONNAISSANCE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("[ERREUR] CONNAISSANCE_PROJETS.json illisible.", file=sys.stderr)
        return {"projets": {}}


def approx_tokens(text):
    return max(1, len(text) // 4)


def selectionner_projets(projets_dict, cible=None, sujet=None):
    cles = list(projets_dict.keys())
    if cible:
        cible_u = cible.upper()
        for p in cles:
            if p.upper() == cible_u or cible_u in p.upper():
                return [p]
        return []
    if sujet:
        sujet_l = sujet.lower()
        trouves = []
        for p in cles:
            p_data = projets_dict[p]
            hay = " ".join([
                p.lower(), str(p_data.get("nom", "")).lower(),
                str(p_data.get("these", "")).lower(),
            ])
            mots = [m for m in re.findall(r"[a-z0-9]{4,}", sujet_l)]
            if any(m in hay for m in mots) or p.lower() in sujet_l:
                trouves.append(p)
        return rotation(projets_dict, trouves or cles)
    # Pas de cible : rotation générale
    return rotation(projets_dict, cles)


def rotation(projets_dict, cles):
    if len(cles) <= 3:
        return cles
    recents = sorted(
        cles,
        key=lambda x: projets_dict[x].get("updated", ""),
        reverse=True,
    )[:2]
    restants = [p for p in cles if p not in recents]
    return recents + [random.choice(restants)]


def formater_projet(p_nom, p_data, inclure_lecons=False, max_tokens=MAX_TOKENS_DEFAUT):
    check_kill_switch()
    faits_filtres = [
        f for f in p_data.get("faits", [])
        if f.get("etat") == "verifie" and f.get("score", 0.0) >= SEUIL_INJECTION
    ]

    def construire(faits):
        lignes = [f"# CONNAISSANCE PROJET — {p_nom} ({p_data.get('nom', '')})"]
        statut = p_data.get("statut_verification", {})
        if statut:
            lignes.append(f"- Statut vérification : {statut.get('verdict', '?')} "
                          f"({statut.get('score', '?')}%, {statut.get('date', '?')})")
        if p_data.get("these"):
            lignes.append(f"- Thèse : {p_data['these']}")
        lignes.append("## Faits vérifiés")
        for f in faits:
            lignes.append(f"- [{f.get('score', 0)}] {f.get('texte', '')}")
        if inclure_lecons:
            lecons = p_data.get("lecons", [])
            if lecons:
                lignes.append("## Leçons (garde-fous)")
                for l in lecons:
                    lignes.append(f"- {l.get('texte', '')}")
        signets = p_data.get("signets_cles", [])
        if signets:
            lignes.append("## Signets clés")
            for s in signets[:5]:
                lignes.append(f"- {s.get('author', '')} ({s.get('date', '')}) : {s.get('resume', '')[:120]}")
        return "\n".join(lignes)

    texte = construire(faits_filtres)
    # Réduction si dépassement du plafond : on retire les faits les moins bien notés
    while approx_tokens(texte) > max_tokens and len(faits_filtres) > 1:
        faits_filtres = sorted(faits_filtres, key=lambda x: x.get("score", 0), reverse=True)
        faits_filtres.pop()
        texte = construire(faits_filtres)
    return texte


def main():
    check_kill_switch()
    parser = argparse.ArgumentParser(description="Injecteur de connaissance ACE777")
    parser.add_argument("--projet", type=str, help="Symbole/nom du projet (ex. CCUSDT)")
    parser.add_argument("--sujet", type=str, help="Texte libre : détection auto de projet")
    parser.add_argument("--lecons", action="store_true", help="Inclure les leçons (usage explicite)")
    parser.add_argument("--max-tokens", type=int, default=MAX_TOKENS_DEFAUT)
    parser.add_argument("--fichier", type=str, help="Fichier de sortie (optionnel)")
    args = parser.parse_args()

    data = load_connaissance()
    projets = data.get("projets", {})
    if not projets:
        print("[INFO] Base de connaissance vide.", file=sys.stderr)
        sys.exit(0)

    selected = selectionner_projets(projets, cible=args.projet, sujet=args.sujet)
    if not selected:
        print(f"[INFO] Aucun projet trouvé pour : {args.projet or args.sujet}", file=sys.stderr)
        sys.exit(0)

    sections = [formater_projet(p, projets[p], inclure_lecons=args.lecons,
                                max_tokens=args.max_tokens) for p in selected]
    output = "\n\n---\n\n".join(sections)

    if args.fichier:
        check_kill_switch()
        chemin = os.path.abspath(args.fichier)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(chemin), text=True)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(output)
            os.replace(tmp_path, chemin)
            print(f"[SUCCÈS] Injection écrite : {chemin}")
        except Exception:
            if os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
            raise
    else:
        print(output)


if __name__ == "__main__":
    main()
