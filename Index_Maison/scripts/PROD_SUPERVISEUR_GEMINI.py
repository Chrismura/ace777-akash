
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
superviseur_auto.py — Superviseur autonome pour macOS (stdlib uniquement)
Exécute un cycle de 6 étapes : LIRE, ÉTAT, DÉCISION (via hub), AGIR, JOURNALISER, POUSSER.
Respecte scrupuleusement les contraintes TCC (passe par l'OUTBOX), sécurités, et limites absolues.
"""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request
import urllib.error

# ==========================================
# CONSTANTES & CONFIGURATION
# ==========================================
HOME = Path.home()
OUTBOX = HOME / "OUTBOX_OBSIDIAN"
ATTENTION_DIR = OUTBOX / "A_Mon_Attention"
LOG_PATH = OUTBOX / "SUPERVISEUR_LOG.md"
ATTENTION_VOCALE_PATH = ATTENTION_DIR / "ATTENTION_VOCALE.md"
STATE_CACHE_PATH = OUTBOX / ".superviseur_state.json"

HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"
HUB_HEALTH_URL = "http://127.0.0.1:11435/health"

# Liste des 14 jobs launchd attendus
JOBS_ATTENDus = [
    "qwen-btc", "cockpit-http", "cortana.horaire", "prise-ia", 
    "analyse-usage", "analyste-cadence", "cockpit-pont", "journal-soir", 
    "gitpush", "cortana.urgent", "brief-matin", "pulse-sous-loeil", 
    "qwen-elabore", "vigie"
]

TIMEOUT_RESEAU = 5
TIMEOUT_HUB = 15
MAX_LOG_LINES = 200
MAX_RELANCES_JOUR_PAR_JOB = 3


# ==========================================
# UTILITAIRES DE SÉCURITÉ & ATOMÉITÉ
# ==========================================

def ecriture_atomique(chemin: Path, contenu: str, mode_append: bool = False, limite_lignes: int = None):
    """Écrit dans un fichier via un fichier temporaire .tmp puis os.replace()."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    
    if mode_append and chemin.exists():
        try:
            lignes = chemin.read_text(encoding="utf-8").splitlines()
        except Exception:
            lignes = []
        lignes.append(contenu)
        if limite_lignes and len(lignes) > limite_lignes:
            lignes = lignes[-limite_lignes:]
        contenu_final = "\n".join(lignes) + "\n"
    else:
        contenu_final = contenu if contenu.endswith("\n") else contenu + "\n"

    tmp_path = chemin.with_suffix(chemin.suffix + ".tmp")
    try:
        tmp_path.write_text(contenu_final, encoding="utf-8")
        os.replace(tmp_path, chemin)
    except Exception as e:
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except Exception:
                pass
        raise e


def charger_etat_interne() -> dict:
    """Charge le cache d'état interne (anti-boucle, compteurs de relance)."""
    if STATE_CACHE_PATH.exists():
        try:
            data = json.loads(STATE_CACHE_PATH.read_text(encoding="utf-8"))
            # Réinitialiser les compteurs si on a changé de jour
            aujourdhui = datetime.now().strftime("%Y-%m-%d")
            if data.get("date") != aujourdhui:
                return {"date": aujourdhui, "relances": {}}
            return data
        except Exception:
            pass
    return {"date": datetime.now().strftime("%Y-%m-%d"), "relances": {}}


def sauvegarder_etat_interne(etat: dict):
    """Sauvegarde le cache d'état de manière atomique."""
    try:
        ecriture_atomique(STATE_CACHE_PATH, json.dumps(etat, indent=2))
    except Exception:
        pass


# ==========================================
# ÉTAPE 1 : LIRE
# ==========================================
def etape_lire() -> dict:
    """1. LIRE — Récupère les contextes depuis l'OUTBOX en priorité, vault en repli."""
    donnees = {}
    fichiers_Cibles = ["TOP_DEMAIN.md", "REVEIL_BUFFY.md", "MEMOIRE_COLLAB.md"]
    
    # Chemins possibles (OUTBOX prioritaire, puis ~/Documents/Vault si accessible)
    dossiers_recherche = [
        OUTBOX,
        HOME / "Documents" / "Vault" / "OUTBOX_OBSIDIAN",
        HOME / "Documents" / "Vault"
    ]

    for nom in fichiers_Cibles:
        contenu = ""
        for dossier in dossiers_recherche:
            f_path = dossier / nom
            if f_path.exists():
                try:
                    # Limiter la lecture aux premiers ko pour la mémoire collaborative / top
                    contenu = f_path.read_text(encoding="utf-8")[:3000]
                    break
                except Exception:
                    pass
        donnees[nom] = contenu if contenu else "[Fichier introuvable ou vide]"
    
    return donnees


# ==========================================
# ÉTAPE 2 : ÉTAT
# ==========================================
def etape_etat() -> dict:
    """2. ÉTAT — Vérifie hub, ollama, jobs launchd, git status."""
    etat = {
        "timestamp": datetime.now().isoformat(),
        "hub_ok": False,
        "ollama_ok": False,
        "jobs_morts": [],
        "git_systeme_propre": True,
        "git_vault_propre": True,
        "details_git": ""
    }

    # 1. Check Hub (/health)
    try:
        req = urllib.request.Request(HUB_HEALTH_URL, headers={"User-Agent": "SuperviseurAuto/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_RESEAU) as resp:
            if resp.status == 200:
                etat["hub_ok"] = True
    except Exception:
        pass

    # 2. Check Ollama
    try:
        req = urllib.request.Request(OLLAMA_TAGS_URL, headers={"User-Agent": "SuperviseurAuto/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_RESEAU) as resp:
            if resp.status == 200:
                etat["ollama_ok"] = True
    except Exception:
        pass

    # 3. Check Launchd Jobs (via launchctl list)
    try:
        res = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=TIMEOUT_RESEAU)
        if res.returncode == 0:
            lignes_launchctl = res.stdout
            for job in JOBS_ATTENDus:
                # Recherche du job dans la liste (format tabulaire launchctl)
                # Un job actif apparaît typiquement avec son PID ou dans la liste sans erreur de statut critique
                trouve = False
                for ligne in lignes_launchctl.splitlines():
                    if job in ligne:
                        trouve = True
                        # Si la colonne PID est '-' ou absente, il est potentiellement arrêté, 
                        # mais launchctl list affiche les services enregistrés. 
                        # On considère mort s'il est totalement absent de la liste active.
                        break
                if not trouve:
                    etat["jobs_morts"].append(job)
    except Exception:
        pass

    # 4. Check Git Système (répertoire courant ou script)
    try:
        res_sys = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, timeout=TIMEOUT_RESEAU, cwd=str(HOME))
        if res_sys.returncode == 0 and res_sys.stdout.strip():
            etat["git_systeme_propre"] = False
            etat["details_git"] += f"Système non propre: {res_sys.stdout.strip()[:100]} | "
    except Exception:
        pass

    return etat


# ==========================================
# ÉTAPE 3 : DÉCISION (via Hub)
# ==========================================
def etape_decision(etat_systeme: dict, contexte_fichiers: dict) -> dict:
    """3. DÉCISION — Interroge le hub (qwen.elabore) pour obtenir un JSON strict."""
    prompt_systeme = (
        "Tu es le module de décision d'un superviseur autonome macOS strict. "
        "Analyse l'état du système fourni. "
        "Tu dois répondre EXCLUSIVEMENT sous forme d'un objet JSON valide, sans markdown autour, respectant ce format exact : "
        '{"action": "none" | "fix" | "ask", "detail": "description précise", "pourquoi": "justification"}.\n'
        "- 'none': tout va bien ou anomalie mineure sans action requise.\n"
        "- 'fix': action mécanique simple requise (ex: relancer un job mort ou pousser git).\n"
        "- 'ask': décision humaine nécessaire, ambigüité, ou blocage persistant.\n"
        "RÈGLE ABSOLUE : Ne JAMAIS toucher au trading/ACE/Hulk."
    )

    prompt_utilisateur = f"""
État actuel du système :
{json.dumps(etat_systeme, indent=2, ensure_ascii=False)}

Contexte fichiers (résumé) :
- TOP_DEMAIN: {contexte_fichiers.get('TOP_DEMAIN.md', '')[:300]}
- REVEIL_BUFFY: {contexte_fichiers.get('REVEIL_BUFFY.md', '')[:300]}
"""

    payload = {
        "task": "qwen.elabore",
        "messages": [
            {"role": "system", "content": prompt_systeme},
            {"role": "user", "content": prompt_utilisateur}
        ],
        "temperature": 0.2,
        "max_tokens": 300
    }

    decision_defaut = {"action": "none", "detail": "Fallback automatique (hub injoignable ou erreur parse)", "pourquoi": "Sécurité par défaut"}

    try:
        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB_URL,
            data=data_bytes,
            headers={"Content-Type": "application/json", "User-Agent": "SuperviseurAuto/1.0"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=None) as resp:
            if resp.status == 200:
                reponse_brute = json.loads(resp.read().decode("utf-8"))
                # Extraction du contenu de la réponse chat completion standard OpenAI-compatible
                content = reponse_brute.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
                
                # Nettoyage éventuel des balises markdown 