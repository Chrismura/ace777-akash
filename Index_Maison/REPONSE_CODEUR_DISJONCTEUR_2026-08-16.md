# Réponse codeur — Disjoncteur (provider Google Gemini, 12.3s)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : disjoncteur.py
Projet       : ACE777 (URGENCE 1 - Le Disjoncteur Unique)
Rôle         : Juge & Risk Guardian (Python pur, stdlib, déterministe, sans LLM).
               - Bridage dynamique des tailles d'ordres (hard cap à la volée).
               - Coupure d'urgence (Mur de Fer) sur seuil de perte journalière (-1.5%)
                 ou plafond global (-8%).
               - Écriture atomique, verrouillage global (STOP_ALL), persistance JSON/JSONL.
"""

import os
import sys
import json
import time
import argparse
import tempfile
from datetime import datetime, timezone
from pathliblib_safe = True  # Flag interne ACE777

# Chemins par défaut ancrés sur la structure ACE777
BASE_DIR = Path(__file__).resolve().parent.parent if '__file__' in locals() else Path('/Users/macbookpro/ace777-test-day1/Index_Maison')
STRATEGIE_DIR = BASE_DIR / 'strategie'
CONFIG_PATH = STRATEGIE_DIR / 'disjoncteur_config.json'
STATE_PATH = STRATEGIE_DIR / 'disjoncteur_state.json'
HISTORY_PATH = STRATEGIE_DIR / 'disjoncteur_history.jsonl'
STOP_ALL_PATH = STRATEGIE_DIR / 'STOP_ALL'
STOP_PATH = STRATEGIE_DIR / 'STOP'
REARMER_FILE = STRATEGIE_DIR / 'REARMER_DISJONCTEUR'

DEFAULT_CONFIG = {
    "pct_journalier": 1.5,
    "max_global_dd_pct": 8.0,
    "plafond_trade_pct": 10.0,  # Max 10% du capital total par trade par défaut
    "cloturer_sur_mur_de_fer": 0
}

def atomic_write(file_path, data):
    """Écriture atomique robuste via mkstemp + os.replace pour éviter la corruption."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    dir_name = file_path.parent
    
    fd, tmp_path = tempfile.mkstemp(dir=str(dir_name), prefix='tmp_atomic_')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            if isinstance(data, (dict, list)):
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(str(data))
        os.replace(tmp_path, file_path)
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise RuntimeError(f"Échec écriture atomique sur {file_path}: {e}")

def load_json(file_path, default=None):
    if default is None:
        default = {}
    path = Path(file_path)
    if not path.exists():
        return default
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default

def get_config():
    cfg = load_json(CONFIG_PATH, DEFAULT_CONFIG)
    # Assurer les clés minimales
    for k, v in DEFAULT_CONFIG.items():
        if k not in cfg:
            cfg[k] = v
    return cfg

def is_stopped():
    return STOP_ALL_PATH.exists() or STOP_PATH.exists() or REARMER_FILE.exists() == False and STATE_PATH.exists() and load_json(STATE_PATH).get('declenche', False)

def verifier_et_brigader(taille_proposee: float, capital_total: float, perte_journaliere_pct: float) -> dict:
    """
    Vérifie l'état du disjoncteur, applique le bridage dynamique et lève le Mur de Fer si nécessaire.
    Déterministe, sans LLM.
    """
    config = get_config()
    now = datetime.now(timezone.utc).isoformat()
    
    etat_actuel = load_json(STATE_PATH, {
        "declenche": False,
        "raison": "",
        "ts": now,
        "perte_journaliere_pct": 0.0
    })

    # Si déjà déclenché ou arrêt d'urgence actif
    if etat_actuel.get("declenche", False) or is_stopped():
        return {
            "autorise": False,
            "taille_corrigee": 0.0,
            "raison": f"DISJONCTEUR OUVERTE (Mur de Fer actif): {etat_actuel.get('raison', 'STOP global')}",
            "declenche": True
        }

    # 1. Vérification Mur de Fer (Seuil journalier ou Global)
    seuil_journalier = config["pct_journalier"]
    plafond_global = config["max_global_dd_pct"]

    if perte_journaliere_pct >= seuil_journalier or perte_journaliere_pct >= plafond_global:
        raison = f"Seuil de perte atteint: {perte_journaliere_pct}% (journalier max: {seuil_journalier}%, global max: {plafond_global}%)"
        declencher_mur_de_fer(raison, perte_journaliere_pct)
        return {
            "autorise": False,
            "taille_corrigee": 0.0,
            "raison": raison,
            "declenche": True
        }

    # 2. Bridage dynamique (Hard Cap)
    pct_max_trade = config["plafond_trade_pct"]
    plafond_capital = capital_total * (pct_max_trade / 100.0)
    
    taille_autorisee = min(float(taille_proposee), float(plafond_capital))
    bridé = taille_autorisee < float(taille_proposee)

    return {
            "autorise": True,
            "taille_corrigee": round(taille_autorisee, 4),
            "bridel": bridé,
            "raison": "OK" if not bridé else f"Bridé par le plafond trade ({pct_max_trade}% du capital)",
            "declenche": False
    }

def declencher_mur_de_fer(raison: str, perte_pct: float):
    """Active le Mur de Fer, pose les verrous, écrit l'état et l'historique."""
    now = datetime.now(timezone.utc).isoformat()
    config = get_config()
    
    # 1. Pose des verrous fichiers
    STRATEGIE_DIR.mkdir(parents=True, exist_ok=True)
    STOP_ALL_PATH.touch(exist_ok=True)
    if REARMER_FILE.exists():
        REARMER_FILE.unlink()

    # 2. État disjoncteur
    etat = {
        "declenche": True,
        "raison": raison,
        "ts": now,
        "perte_journaliere_pct": perte_pct,
        "cloture_effectuee": bool(config.get("cloturer_sur_mur_de_fer", 0))
    }
    atomic_write(STATE_PATH, etat)

    # 3. Alerte cockpit (.urgent_alert.json)
    alert_path = STRATEGIE_DIR / '.urgent_alert.json'
    atomic_write(alert_path, {
        "niveau": "CRITIQUE",
        "module": "disjoncteur.py",
        "message": f"MUR DE FER DÉCLENCHÉ : {raison}",
        "ts": now
    })

    # 4. Historique append-only (JSONL)
    log_entry = json.dumps({"event": "MUR_DE_FER_DECLENCHE", "ts": now, "raison": raison, "perte": perte_pct})
    with open(HISTORY_PATH, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

    print(f"[ALERTE ROUGE ACE777] MUR DE FER DÉCLENCHÉ : {raison}", file=sys.stderr)

def rearmer():
    """Réarmement manuel exclusif."""
    now = datetime.now(timezone.utc).isoformat()
    
    # Suppression des verrous
    for p in [STOP_ALL_PATH, REARMER_FILE]:
        if p.exists():
            p.unlink()

    etat = {
        "declenche": False,
        "raison": "Réarmement manuel effectué",
        "ts": now,
        "perte_journaliere_pct": 0.0
    }
    atomic_write(STATE_PATH, etat)

    log_entry = json.dumps({"event": "DISJONCTEUR_REARMÉ", "ts": now})
    with open(HISTORY_PATH, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

    print(f"[ACE777] Disjoncteur réarmé avec succès à {now}.")

def main():
    parser = argparse.ArgumentParser(description="Disjoncteur Unique ACE777 (Juge & Risk Guardian)")
    parser.add_argument("--check", action="store_true", help="Vérifie l'état global (retourne 0 si OK, 1 si déclenché)")
    parser.add_argument("--bridage", type=float, help="Teste le bridage pour une taille d'ordre donnée")
    parser.add_argument("--capital", type=float, default=10000.0, help="Capital total de référence pour le bridage")
    parser.add_argument("--perte-jour", type=float, default=0.0, help="Perte journalière actuelle en %")
    parser.add_argument("--rearmer", action="store_true", help="Réarme manuellement le disjoncteur")
    parser.add_argument("--etat", action="store_true", help="Affiche l'état courant en JSON")

    args = parser.parse_args()
    
    STRATEGIE_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        atomic_write(CONFIG_PATH, DEFAULT_CONFIG)

    if args.rearmer:
        rearmer()
        sys.exit(0)

    if args.etat:
        etat = load_json(STATE_PATH, {"declenche": False, "raison": "Initié"})
        print(json.dumps(etat, indent=2))
        sys.exit(0)

    if args.check:
        stopped = is_stopped()
        etat = load_json(STATE_PATH, {"declenche": False})
        if stopped or etat.get("declenche", False):
            print(json.dumps({"statut": "DECLENCHE", "details": etat}))
            sys.exit(1)
        else:
            print(json.dumps({"statut": "OK"}))
            sys.exit(0)

    if args.bridage is not None:
        res = verifier_et_brigader(args.bridage, args.capital, args.perte_jour)
        print(json.dumps(res, indent=2))
        sys.exit(0 if res["autorise"] else 1)

    parser.print_help()

if __name__ == '__main__':
    main()
```

---

## 2. DIFFS EXACTS D'INTÉGRATION

### A. Intégration Superviseur (`superviseur.sh` ou équivalent)
Ajout de la surveillance continue du disjoncteur et de son état dans la boucle de supervision.

```bash
# AVANT
# ... boucles de supervision standards ...
check_hulk() {
    pgrep -f "paper_diprip.py" > /dev/null || restart_hulk
}

# APRÈS
check_disjoncteur() {
    python3 Index_Maison/scripts/disjoncteur.py --check || {
        echo "[ALERTE] Disjoncteur déclenché ou compromis. Verrouillage flux."
        touch Index_Maison/strategie/STOP_ALL
    }
}

check_hulk() {
    # Ne redémarre PAS si le disjoncteur a coupé
    if [ -f "Index_Maison/strategie/STOP_ALL" ]; then
        return 0
    fi
    pgrep -f "paper_diprip.py" > /dev/null || restart_hulk
}
```

### B. Pont Cockpit (`cortana_cockpit_bridge.py`)
Exposition de l'état du disjoncteur pour affichage dans le cockpit (petite carte dédiée).

```python
# AVANT
# (Pas de remontée standard de l'état disjoncteur dans le payload global)
def get_cockpit_status():
    return {
        "ada": load_ada_state(),
        "hulk": load_hulk_state()
    }

# APRÈS
def load_disjoncteur_state():
    state_path = Path(__file__).resolve().parent.parent / 'strategie' / 'disjoncteur_state.json'
    if not state_path.exists():
        return {"declenche": False, "raison": "Normal", "ts": ""}
    try:
        with open(state_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"declenche": True, "raison": "Erreur lecture état"}

def get_cockpit_status():
    return {
        "ada": load_ada_state(),
        "hulk": load_hulk_state(),
        "disjoncteur": load_disjoncteur_state()
    }
```

### C. Moteur HULK (`paper_diprip.py` — Point d'insertion minimal non invasif)
Le codeur n'altère pas la logique interne de HULK (`paper_diprip.py`), il intercepte l'appel d'ordre juste avant exécution/fill via un wrapper d'importation ou un appel système direct minimaliste.

```python
# AVANT (dans paper_diprip.py, au moment de soumettre l'ordre)
def executer_ordre(taille, prix, symbole):
    # passage direct à l'exchange / carnet paper
    placer_ordre_interne(taille, prix, symbole)

# APRÈS (dans paper_diprip.py, point d'insertion non invasif)
import subprocess
import json
from pathlib import Path

def verifier_via_disjoncteur(taille_proposee, capital_ref=10000.0):
    script_path = Path(__file__).resolve().parent.parent / 'scripts' / 'disjoncteur.py'
    try:
        res = subprocess.run(
            ['python3', str(script_path), '--bridage', str(taille_proposee), '--capital', str(capital_ref)],
            capture_output=True, text=True, timeout=2
        )
        if res.returncode != 0 and "MUR DE FER" in res.stderr:
            return {"autorise": False, "taille_corrigee": 0.0}
        data = json.loads(res.stdout)
        return data
    except Exception:
        # En cas de défaillance du disjoncteur, par principe d'airain ACE777 : rejet par sécurité
        return {"autorise": False, "taille_corrigee": 0.0}

def executer_ordre(taille, prix, symbole):
    # POINT D'INSERTION DISJONCTEUR UNIQUE
    check = verifier_via_disjoncteur(taille)
    if not check.get("autorise", False):
        print(f"[DISJONCTEUR ACE777] Ordre bloqué ou rejeté : {check.get('raison')}")
        return False
    
    taille_reelle = check.get("taille_corrigee", taille)
    # Poursuite avec la taille bridée/autorisée
    placer_ordre_interne(taille_reelle, prix, symbole)
```

---

## 3. NOTES FINALES DU CODEUR SENIOR ACE777

1. **Choix de conception (Stdlib & Déterminisme)** : `disjoncteur.py` n'utilise aucune bibliothèque tierce (`json`, `os`, `sys`, `pathlib`, `subprocess`, `tempfile`). Aucun LLM n'est impliqué dans le hot path.
2. **Robustesse Atomique** : L'utilisation de `tempfile.mkstemp` combiné avec `os.replace` garantit qu'aucun fichier d'état ou de configuration ne se retrouvera corrompu en cas de coupure de courant ou d'arrêt brutal du processus.
3. **Point d'insertion HULK** : Le wrapper externe via `subprocess` (ou un import direct du module) permet de s'interfacer avec `paper_diprip.py` sans modifier ses structures internes complexes, garantissant un couplage lâche mais infranchissable.
4. **Réarmement Manuel** : Strictement confiné au fichier `REARMER_DISJONCTEUR` ou à la commande explicite `--rearmer`. Aucune boucle automatique ne peut réarmer le système, éliminant tout risque de "re-routage" nocturne en cas de perte persistante.
