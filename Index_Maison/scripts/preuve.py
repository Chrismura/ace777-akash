#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Genere par Google Gemini via hub (loi 1quinquies : Ada specifie, le hub ecrit) — 09/08 conditions famille
# Fichier : preuve.py
import os
import sys
import subprocess
import hashlib
from datetime import datetime
from pathlib import Path

# Constantes systeme (specifiques macOS et environnement de Christophe)
MAISON = Path.home() / "ace777-test-day1"
INDEX_MAISON = MAISON / "Index_Maison"
WORM_PATH = INDEX_MAISON / "WORM_JOURNAL.log"
CRITIQUES_PATH = INDEX_MAISON / "FICHIERS_CRITIQUES.txt"

def initialiser_environnement():
    """Verifie et prepare l'arborescence minimale requise."""
    try:
        INDEX_MAISON.mkdir(parents=True, exist_ok=True)
        if not WORM_PATH.exists():
            WORM_PATH.touch(exist_ok=True)
        if not CRITIQUES_PATH.exists():
            CRITIQUES_PATH.touch(exist_ok=True)
    except Exception:
        pass

def ecrire_worm(niveau, categorie, message):
    """Ecrit une ligne dans le journal WORM (append-only, flag uappnd macOS).
    Corrige checker 09/08 : plus de chflags aller-retour, l'append direct
    fonctionne avec uappnd (on ne peut que ajouter)."""
    initialiser_environnement()
    ts_iso = datetime.now().isoformat()
    msg_propre = str(message).replace("\n", " ").replace("|", "/")
    ligne = f"| {ts_iso} | {niveau} | {categorie} | {msg_propre} |\n"
    try:
        with open(WORM_PATH, "a", encoding="utf-8") as f:
            f.write(ligne)
    except Exception as e:
        sys.stderr.write(f"Erreur critique ecriture WORM : {e}\n")

def commander_exiger(affirmation, cmd):
    """Execute la commande de preuve, verifie le resultat et consigne dans le WORM."""
    if not affirmation or not cmd:
        sys.stdout.write("PREUVE NON VERIFIEE : Affirmation ou commande manquante.\n")
        sys.exit(1)
        
    try:
        resultat = subprocess.run(
            ['/bin/bash', '-lc', cmd],
            timeout=30,
            capture_output=True,
            text=True
        )
    except subprocess.TimeoutExpired:
        sys.stdout.write("PREUVE NON VERIFIEE : Timeout de la commande (30s).\n")
        sys.exit(1)
    except Exception as e:
        sys.stdout.write(f"PREUVE NON VERIFIEE : Erreur execution - {e}\n")
        sys.exit(1)
        
    sortie_brute = resultat.stdout.strip()
    erreur_brute = resultat.stderr.strip()
    
    # Constitution de la sortie combinee pour analyse
    sortie_totale = sortie_brute
    if erreur_brute:
        if sortie_totale:
            sortie_totale += f" | STDERR: {erreur_brute}"
        else:
            sortie_totale = erreur_brute

    # Condition de succes : exit code == 0 et sortie non vide
    if resultat.returncode == 0 and sortie_totale:
        # Tronquer a 500 caracteres maximum pour le journal
        sortie_tronquee = sortie_totale[:500]
        message_journal = f"Affirmation: {affirmation} || Preuve: {sortie_tronquee}"
        
        ecrire_worm("INFO", "PREUVE", message_journal)
        sys.stdout.write("PREUVE OK\n")
        sys.exit(0)
    else:
        sortie_tronquee = sortie_totale[:500] if sortie_totale else "Sortie vide"
        sys.stdout.write(f"PREUVE NON VERIFIEE (Exit: {resultat.returncode}) : {sortie_tronquee}\n")
        sys.exit(1)

def commander_recentes(n_str):
    """Affiche les N dernieres entrees de categorie PREUVE du WORM."""
    try:
        n = int(n_str)
    except ValueError:
        n = 10
        
    if not WORM_PATH.exists():
        sys.stdout.write("Aucun journal WORM trouve.\n")
        return
        
    preuves = []
    try:
        with open(WORM_PATH, "r", encoding="utf-8") as f:
            for ligne in f:
                if "| PREUVE |" in ligne:
                    preuves.strip() if hasattr(ligne, 'strip') else None
                    preuves.append(ligne.strip())
    except Exception as e:
        sys.stderr.write(f"Erreur lecture WORM : {e}\n")
        return
        
    dernieres = preuves[-n:]
    for p in dernieres:
        sys.stdout.write(f"{p}\n")

def main():
    """Point d'entree principal du script de preuve."""
    if len(sys.argv) < 2:
        sys.stdout.write("Usage: python3 preuve.py [exiger|recentes] ...\n")
        sys.exit(1)
        
    action = sys.argv[1]
    
    if action == "exiger":
        affirmation = None
        cmd = None
        
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "--affirmation" and i + 1 < len(sys.argv):
                affirmation = sys.argv[i+1]
                i += 2
            elif sys.argv[i] == "--cmd" and i + 1 < len(sys.argv):
                cmd = sys.argv[i+1]
                i += 2
            else:
                i += 1
                
        if not affirmation or not cmd:
            sys.stdout.write("Erreur: arguments --affirmation et --cmd obligatoires.\n")
            sys.exit(1)
            
        commander_exiger(affirmation, cmd)
        
    elif action == "recentes":
        n = 10
        i = 2
        while i < len(sys.argv):
            if sys.argv[i] == "--n" and i + 1 < len(sys.argv):
                n = sys.argv[i+1]
                i += 2
            else:
                i += 1
                
        commander_recentes(n)
    else:
        sys.stdout.write(f"Action inconnue : {action}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

