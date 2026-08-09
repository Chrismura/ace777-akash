#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genere par Google Gemini via hub (loi 1quinquies : Ada specifie, le hub ecrit) — 09/08 conditions famille
# Fichier : integrite.py
import os
import sys
import json
import re
import subprocess
import hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path

MAISON = Path.home() / "ace777-test-day1"
INDEX_MAISON = MAISON / "Index_Maison"
WORM_PATH = INDEX_MAISON / "WORM_JOURNAL.log"
CRITIQUES_PATH = INDEX_MAISON / "FICHIERS_CRITIQUES.txt"
INTEGRITE_PATH = INDEX_MAISON / "INTEGRITE_BASE.json"
HUB_URL = "http://127.0.0.1:11435"

def ecrire_worm(niveau, categorie, message):
    ts_iso = datetime.now(timezone.utc).isoformat()
    msg_propre = str(message).replace("\n", " ").replace("|", "/")
    ligne = f"| {ts_iso} | {niveau} | {categorie} | {msg_propre} |\n"
    # macOS : uappnd = append-only, l'append direct fonctionne (corrige checker 09/08).
    try:
        with open(WORM_PATH, "a", encoding="utf-8") as f:
            f.write(ligne)
    except IOError as e:
        print(f"Erreur ecriture WORM : {e}", file=sys.stderr)

def calculer_sha256(chemin_fichier):
    sha256_hash = hashlib.sha256()
    try:
        with open(chemin_fichier, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except (IOError, OSError):
        return None

def charger_fichiers_critiques():
    fichiers = []
    if not CRITIQUES_PATH.exists():
        return fichiers
    try:
        with open(CRITIQUES_PATH, "r", encoding="utf-8") as f:
            for ligne in f:
                chemin = ligne.strip()
                if chemin and not chemin.startswith("#"):
                    fichiers.append(Path(chemin))
    except IOError:
        pass
    return fichiers

def lire_dernieres_lignes_worm(n=200):
    if not WORM_PATH.exists():
        return []
    lignes = []
    try:
        with open(WORM_PATH, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except IOError:
        return []
    return [l.strip() for l in lignes[-n:]]

def verifier_trace_modification_recente(chemin_str):
    lignes = lire_dernieres_lignes_worm(200)
    maintenant = datetime.now(timezone.utc)
    
    motif = re.compile(r"\|\s*(?P<ts>[^|]+)\s*\|\s*(?P<niveau>[^|]+)\s*\|\s*(?P<cat>[^|]+)\s*\|\s*(?P<msg>.*)\s*\|")
    
    for ligne in lignes:
        match = motif.search(ligne)
        if not match:
            continue
        
        ts_str = match.group("ts").strip()
        cat = match.group("cat").strip()
        msg = match.group("msg").strip()
        
        if cat != "MODIF":
            continue
            
        if chemin_str not in msg:
            continue
            
        try:
            ts_entree = datetime.fromisoformat(ts_str)
            if ts_entree.tzinfo is None:
                ts_entree = ts_entree.replace(tzinfo=timezone.utc)
            
            difference = maintenant - ts_entree
            if difference <= timedelta(hours=1):
                return True
        except ValueError:
            continue
            
    return False

def commande_init():
    INDEX_MAISON.mkdir(parents=True, exist_ok=True)
    fichiers = charger_fichiers_critiques()
    base = {}
    
    for chemin in fichiers:
        if chemin.exists() and chemin.is_file():
            h = calculer_sha256(chemin)
            if h:
                base[str(chemin)] = h
                
    # La base est critique (444). integrite.py est le SEUL autorise a la reecrire :
    # chmod temporaire + re-verrouillage, trace WORM (audit tiers 09/08).
    try:
        if INTEGRITE_PATH.exists():
            os.chmod(INTEGRITE_PATH, 0o600)
        with open(INTEGRITE_PATH, "w", encoding="utf-8") as f:
            json.dump(base, f, indent=4, ensure_ascii=False)
        os.chmod(INTEGRITE_PATH, 0o444)
        print(f"Base d'integrite initialisee avec succes : {INTEGRITE_PATH}")
        ecrire_worm("INFO", "INIT", f"Base d'integrite creee avec {len(base)} fichiers.")
    except IOError as e:
        print(f"Erreur lors de l'ecriture de la base d'integrite : {e}", file=sys.stderr)

def executer_analyse():
    if not INTEGRITE_PATH.exists():
        print("Erreur : Base d'integrite introuvable. Lancez 'init' d'abord.", file=sys.stderr)
        return None, None, None
        
    try:
        with open(INTEGRITE_PATH, "r", encoding="utf-8") as f:
            base = json.load(f)
    except (IOError, json.JSONDecodeError):
        print("Erreur : Impossible de lire la base d'integrite.", file=sys.stderr)
        return None, None, None
        
    nb_ok = 0
    nb_traces = 0
    nb_violations = 0
    
    for chemin_str, hash_origine in base.items():
        chemin = Path(chemin_str)
        
        if not chemin.exists() or not chemin.is_file():
            message = f"Fichier critique manquant : {chemin_str}"
            if verifier_trace_modification_recente(chemin_str):
                nb_traces += 1
            else:
                nb_violations += 1
                ecrire_worm("ALERTE", "VIOLATION", message)
            continue
            
        hash_actuel = calculer_sha256(chemin)
        if hash_actuel is None:
            continue
            
        if hash_actuel == hash_origine:
            nb_ok += 1
        else:
            message = f"Modification detectee sur le fichier critique : {chemin_str}"
            if verifier_trace_modification_recente(chemin_str):
                nb_traces += 1
                print(f"[TRACE] Modification tracee pour : {chemin_str}")
            else:
                nb_violations += 1
                print(f"[VIOLATION] Modification non tracee pour : {chemin_str}")
                ecrire_worm("ALERTE", "VIOLATION", message)
                
    return nb_ok, nb_traces, nb_violations

def commande_check():
    print("Verification de l'integrite des fichiers critiques...")
    nb_ok, nb_traces, nb_violations = executer_analyse()
    if nb_ok is not None:
        print(f"Verification terminee. OK: {nb_ok} | Traces: {nb_traces} | Violations: {nb_violations}")

def commande_rapport():
    print("Generation du rapport d'integrite...")
    nb_ok, nb_traces, nb_violations = executer_analyse()
    if nb_ok is not None:
        print("--- BILAN INTEGRITE ---")
        print(f"Fichiers OK            : {nb_ok}")
        print(f"Modifies et traces     : {nb_traces}")
        print(f"Violations non tracees : {nb_violations}")
        print("-----------------------")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 integrite.py [init|check|rapport]", file=sys.stderr)
        sys.exit(0)
        
    action = sys.argv[1].lower()
    
    if action == "init":
        commande_init()
    elif action == "check":
        commande_check()
    elif action == "rapport":
        commande_rapport()
    else:
        print(f"Action inconnue : {action}", file=sys.stderr)
        
    sys.exit(0)

if __name__ == "__main__":
    main()

