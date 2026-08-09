#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genere par Google Gemini via hub (loi 1quinquies : Ada specifie, le hub ecrit) — 09/08 conditions famille
# Fichier : gardien.py
import os
import sys
import json
import re
import subprocess
import hashlib
from datetime import datetime
from pathlib import Path

MAISON = Path("/Users/christophe/ace777-test-day1")
INDEX_MAISON = MAISON / "Index_Maison"
WORM_PATH = INDEX_MAISON / "WORM_JOURNAL.log"
CRITIQUES_PATH = INDEX_MAISON / "FICHIERS_CRITIQUES.txt"
SIGNATURES_DIR = INDEX_MAISON / "SIGNATURES"

def ecrire_worm(niveau, categorie, message):
    ts = datetime.now().isoformat()
    msg_propre = str(message).replace("\n", " ").replace("|", "/")
    ligne = f"| {ts} | {niveau} | {categorie} | {msg_propre} |\n"
    # macOS : uappnd = append-only. L'ouverture en mode "a" fonctionne SANS
    # retirer le flag (on ne peut que ajouter). Corrige 09/08 (checker Ada) :
    # lsattr n'existe pas sur macOS -> on ecrit directement en append.
    with open(WORM_PATH, "a", encoding="utf-8") as f:
        f.write(ligne)

def calculer_sha256(chemin):
    hasher = hashlib.sha256()
    with open(chemin, "rb") as f:
        while True:
            bloc = f.read(65536)
            if not bloc:
                break
            hasher.update(bloc)
    return hasher.hexdigest()

def charger_critiques():
    if not CRITIQUES_PATH.exists():
        print(f"Erreur critique : Fichier {CRITIQUES_PATH} absent.", file=sys.stderr)
        sys.exit(1)
    critiques = set()
    with open(CRITIQUES_PATH, "r", encoding="utf-8") as f:
        for ligne in f:
            chemin = ligne.strip()
            if chemin and not chemin.startswith("#"):
                critiques.add(os.path.abspath(chemin))
    return critiques

def verifier_critique(cible):
    critiques = charger_critiques()
    abs_cible = os.path.abspath(cible)
    if abs_cible not in critiques:
        print(f"Erreur C1 : Le fichier {cible} n'est pas dans la liste des fichiers critiques.", file=sys.stderr)
        ecrire_worm("REFUS", "SECURITE", f"Tentative d'acces non autorise hors liste critique : {cible}")
        sys.exit(1)
    return abs_cible

def commande_pre(args):
    if len(args) < 4:
        print("Usage incorrect pour pre", file=sys.stderr)
        sys.exit(1)
    
    action = ""
    cible = ""
    justif = ""
    
    i = 0
    while i < len(args):
        if args[i] == "--action" and i + 1 < len(args):
            action = args[i+1]
            i += 2
        elif args[i] == "--cible" and i + 1 < len(args):
            cible = args[i+1]
            i += 2
        elif args[i] == "--justif" and i + 1 < len(args):
            justif = args[i+1]
            i += 2
        else:
            i += 1

    if not cible:
        print("Erreur : --cible manquant", file=sys.stderr)
        sys.exit(1)

    abs_cible = verifier_critique(cible)
    ecrire_worm("INFO", "PRE_MODIF", f"Action: {action} | Cible: {abs_cible} | Justification: {justif}")
    print(f"Pre-enregistrement WORM effectue avec succes pour {abs_cible}")

def commande_apply(args):
    cible = ""
    nouveau = ""
    justif = ""
    
    i = 0
    while i < len(args):
        if args[i] == "--cible" and i + 1 < len(args):
            cible = args[i+1]
            i += 2
        elif args[i] == "--nouveau" and i + 1 < len(args):
            nouveau = args[i+1]
            i += 2
        elif args[i] == "--justif" and i + 1 < len(args):
            justif = args[i+1]
            i += 2
        else:
            i += 1

    if not cible or not nouveau:
        print("Erreur : --cible et --nouveau obligatoires", file=sys.stderr)
        sys.exit(1)

    abs_cible = verifier_critique(cible)
    abs_nouveau = os.path.abspath(nouveau)

    if not os.path.exists(abs_nouveau):
        print(f"Erreur : Le fichier temporaire nouveau {abs_nouveau} n'existe pas.", file=sys.stderr)
        sys.exit(1)

    # 1. Pre-enregistrement automatique dans WORM
    ecrire_worm("INFO", "APPLY_PRE", f"Demande d'application pour {abs_cible} | Justification: {justif}")

    # 2. Verification double signature (C4)
    basename = Path(abs_cible).name
    sig_file = SIGNATURES_DIR / f"{basename}.sig"

    if not sig_file.exists():
        print(f"Erreur C4 : Fichier de signature manquant {sig_file}", file=sys.stderr)
        ecrire_worm("ERREUR", "SIGNATURE", f"Signature manquante pour {abs_cible}")
        sys.exit(1)

    hash_nouveau = calculer_sha256(abs_nouveau)

    ada_trouve = False
    famille_trouve = False

    with open(sig_file, "r", encoding="utf-8") as f:
        lignes = f.readlines()
        for ligne in lignes:
            ligne_propre = ligne.strip()
            if ligne_propre.startswith("ADA:"):
                h = ligne_propre.split(":", 1)[1].strip()
                if h == hash_nouveau:
                    ada_trouve = True
            elif ligne_propre.startswith("FAMILLE:"):
                h = ligne_propre.split(":", 1)[1].strip()
                if h == hash_nouveau:
                    famille_trouve = True

    if not ada_trouve or not famille_trouve:
        print("Erreur C4 : Double signature invalide ou absente pour le nouveau hash.", file=sys.stderr)
        ecrire_worm("ERREUR", "SIGNATURE", f"Double signature invalide pour {abs_cible} (hash: {hash_nouveau})")
        sys.exit(1)

    # Hash avant modification
    hash_avant = "INEXISTANT"
    if os.path.exists(abs_cible):
        hash_avant = calculer_sha256(abs_cible)

    # 3. Application de la modification
    try:
        # Assurer les droits d'ecriture temporaires si necessaire
        if os.path.exists(abs_cible):
            os.chmod(abs_cible, 0o600)
        
        with open(abs_nouveau, "rb") as fn:
            contenu = fn.read()
        with open(abs_cible, "wb") as fc:
            fc.write(contenu)
            
        os.chmod(abs_cible, 0o400) # Verrouillage standard post-application
    except Exception as e:
        print(f"Erreur lors de l'ecriture du fichier cible : {e}", file=sys.stderr)
        ecrire_worm("ERREUR", "SYSTEME", f"Echec de l'ecriture de {abs_cible} : {e}")
        sys.exit(1)

    hash_apres = calculer_sha256(abs_cible)
    ecrire_worm("SUCCES", "APPLY", f"Fichier modifie : {abs_cible} | Hash avant: {hash_avant} | Hash apres: {hash_apres}")
    print(f"Application reussie pour {abs_cible}. Hash: {hash_apres}")

def commande_status():
    print("=== STATUT DU GARDIEN ===")
    
    # Etat du WORM (macOS : ls -lO affiche les flags, uappnd = append-only)
    if WORM_PATH.exists():
        print(f"WORM Journal : PRESENT ({WORM_PATH})")
        res = subprocess.run(["ls", "-lO", str(WORM_PATH)], capture_output=True, text=True)
        if "uappnd" in res.stdout:
            print("WORM Protection : ACTIF (append-only)")
        else:
            print("WORM Protection : INACTIF ou non supporte")
    else:
        print(f"WORM Journal : ABSENT ({WORM_PATH})")

    # Nombre de signatures
    nb_sig = 0
    if SIGNATURES_DIR.exists():
        nb_sig = len(list(SIGNATURES_DIR.glob("*.sig")))
    print(f"Nombre de signatures enregistrees : {nb_sig}")

    # Droits des fichiers critiques
    print("\n--- Droits des fichiers critiques ---")
    try:
        critiques = charger_critiques()
        for c in critiques:
            p = Path(c)
            if p.exists():
                mode = oct(p.stat().st_mode)[-3:]
                print(f"[OK] {c} -> droits: {mode}")
            else:
                print(f"[INTROUVABLE] {c}")
    except SystemExit:
        print("Erreur : Impossible de charger la liste des fichiers critiques.")

def main():
    if not INDEX_MAISON.exists():
        print(f"Erreur : Repertoire Index_Maison introuvable a {INDEX_MAISON}", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python3 gardien.py [pre|apply|status] ...", file=sys.stderr)
        sys.exit(1)

    commande = sys.argv[1]
    args = sys.argv[2:]

    if commande == "pre":
        commande_pre(args)
    elif commande == "apply":
        commande_apply(args)
    elif commande == "status":
        commande_status()
    else:
        print(f"Commande inconnue : {commande}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

