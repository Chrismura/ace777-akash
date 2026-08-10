# E3 — CODE PRODUIT PAR LE HUB (via NVIDIA build.nvidia.com (100+ modeles), task code.ia) — 10/08/2026

## Mission envoyee

Systeme ACE777 - Mac 8 Go, hub local 11435, 9 providers gratuits, 29 services launchd. Setup des 3 etages en cours (SPEC V2.1 validee par la famille : GO unanime GEMINI + JUGE, loi 1quinquies). Tu es le CODEUR du hub.

TA MISSION : implémenter l'étape E3 de la SPEC V2.1 (2 livrables), avec les réserves famille intégrées :

## LIVRABLE 1 — README_MIROFISH.md
Fichier : ~/Library/LaunchAgents/DESACTIVES_2026-08-10/README_MIROFISH.md
Contexte : Mirofish = MEMBRE DE L'EQUIPE (simulation sociale multi-agents, recherche-grade, jamais d'execution), mis en PAUSE BUDGETAIRE le 10/08 (tournait a vide 14 h). Option (c) confirmee par la famille : desactive + sorti de la liste surveillee (regle skip_check dans le superviseur) + code ~/mirofis/ (1 Go) en backup uniquement.
Contenu du README (reserve famille P3 - reversibilite) :
- Date de mise en pause, decision (membre equipe, pause budgetaire)
- Procedure EXACTE de re-activation : restaurer les plists (cp DESACTIVES_2026-08-10/com.ace777.mirofish*.plist ~/Library/LaunchAgents/), retirer la regle skip_check dans le superviseur, launchctl load, verifier HEALTHY dans state.json
- Rappel : donnees sauvegardees dans Index_Maison/MIROFISH_DONNEES_2026-08-10/ (728 Ko)
- Redige en francais, structure claire, actionnable.

## LIVRABLE 2 — Verification version coeur Rust dans cortana_cockpit_bridge.py
Fichier a modifier : ~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py
Reserve famille P4 (JUGE) : le coeur Rust ~/crypto-voice-assistant-core/ est hors perimetre du setup mais sauvegarde (4,4 Go). Ajouter une fonction qui :
- lit ~/crypto-voice-assistant-core/VERSION (si le fichier existe)
- compare a une version attendue (EXPECTED_RUST_VERSION, a definir)
- loggue un warning si version != attendue, un error si fichier VERSION manquant
- ne doit JAMAIS planter le script (try/except, non fatal)

CONTRAINTES :
- Python 3.9 stdlib uniquement (macOS), pas de dependance
- Non fatal : toute erreur = log, jamais d'exception
- Respecter le style du fichier existant (commentaires en francais, docstring)
- Loi du brut : pas de prose inutile, du code propre

REPONDS EN FRANCAIS avec :
1. Le contenu COMPLET de README_MIROFISH.md (pret a copier)
2. Le code COMPLET de la fonction a ajouter dans cortana_cockpit_bridge.py (pret a copier)
3. Les instructions d'integration exactes (ou inserer, quoi modifier)

Hub /health a l'envoi : {"status": "ok", "providers": 9}

Contexte reel (brut) :
--- cortana_cockpit_bridge.py (debut) ---
#!/usr/bin/env python3
"""
Pont local cockpit ↔ Cortana + feed mission (127.0.0.1 seulement).
  python3 cortana_cockpit_bridge.py
  GET  /status /mission /alerts /refresh /preflight
  POST /mute /unmute /speak /refresh /panic

Pas d'ouverture de trade. Sortie urgence = /panic mode A|B.
CORS ouvert pour file:// cockpit.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path("/Users/christophe/ace777-test-day1")
SCRIPTS = ROOT / "Index_Maison" / "scripts"
MISSION_JSON = ROOT / "Index_Maison" / "cockpit" / "mission.json"
RUNS = ROOT / "runs"
HULK = ROOT / "hulk-mexc"
PANIC_LOG = ROOT / "Index_Maison" / "cockpit" / "panic.log"
PORT = 17777


def _ace_link() -> dict:
    """LIVE frais = ACE en marche · STALE = log froid · OFF = pas de LIVE."""
    import time

    lives = sorted(RUNS.glob("*_LIVE_COLOR.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not lives:
        return {"state": "OFF", "label": "OFF", "ageSec": None, "run": None, "live": None}
    live = lives[0]
    age = max(0, int(time.time() - live.stat().st_mtime))
--- DESACTIVES_2026-08-10/ ---
com.ace777.mirofish-front.plist
com.ace777.mirofish.plist


## Reponse du codeur

## LIVRABLE 1 — README_MIROFISH.md

```markdown
# Mirofish — Mise en pause budgétaire (10/08/2026)

## Décision
- **Date** : 10 août 2026
- **Statut** : Membre de l'équipe (simulation sociale multi-agents, recherche-grade)
- **Motif** : Pause budgétaire — tournait à vide pendant 14 heures
- **Décision famille** : Option (c) — désactivé + sorti de la liste surveillée (règle `skip_check` dans le superviseur)
- **Code** : `~/mirofis/` (1 Go) conservé en backup uniquement

## Données sauvegardées
- **Emplacement** : `Index_Maison/MIROFISH_DONNEES_2026-08-10/`
- **Taille** : 728 Ko
- **Contenu** : Données de simulation, logs, états des agents

## Procédure de ré-activation (réversible)

### Étape 1 — Restaurer les plists
```bash
cp ~/Library/LaunchAgents/DESACTIVES_2026-08-10/com.ace777.mirofish*.plist ~/Library/LaunchAgents/
```

### Étape 2 — Retirer la règle skip_check
- Ouvrir le fichier superviseur (généralement `~/ace777-test-day1/Index_Maison/scripts/superviseur.py`)
- Rechercher la section `skip_check` ou `MIROFISH`
- Supprimer la ligne/règle correspondante

### Étape 3 — Charger les services
```bash
launchctl load ~/Library/LaunchAgents/com.ace777.mirofish.plist
launchctl load ~/Library/LaunchAgents/com.ace777.mirofish-front.plist
```

### Étape 4 — Vérifier l'état
- Consulter `state.json` (généralement dans `~/ace777-test-day1/Index_Maison/`)
- Vérifier que le statut est `HEALTHY`
- Vérifier les logs : `~/ace777-test-day1/runs/` pour les fichiers `*_LIVE_COLOR.log`

### Étape 5 — Validation finale
- Tester le front : accéder à l'interface cockpit
- Vérifier que les données de `MIROFISH_DONNEES_2026-08-10/` sont bien chargées

## Notes importantes
- **Non exécution** : Mirofish ne doit JAMAIS exécuter d'actions — uniquement simulation
- **Backup** : Le code dans `~/mirofis/` est en lecture seule — ne pas modifier
- **Restauration** : En cas de problème, les plists originales sont dans `DESACTIVES_2026-08-10/`
- **Contact** : Pour toute question, voir la famille (décision collective requise)
```

---

## LIVRABLE 2 — Fonction de vérification Rust

```python
# À ajouter dans cortana_cockpit_bridge.py après les imports et constantes

# Version attendue du coeur Rust (à ajuster selon la version réelle)
EXPECTED_RUST_VERSION = "2.1.0"
RUST_CORE_DIR = Path("/Users/christophe/crypto-voice-assistant-core")


def _check_rust_version() -> None:
    """
    Vérifie la version du coeur Rust (hors périmètre setup, backup uniquement).
    Log un warning si version != attendue, error si VERSION manquant.
    Non fatal : ne plante jamais le script.
    """
    version_file = RUST_CORE_DIR / "VERSION"
    
    try:
        if not version_file.exists():
            print(f"[ERROR] Fichier VERSION manquant : {version_file}", file=sys.stderr)
            return
        
        with open(version_file, "r", encoding="utf-8") as f:
            rust_version = f.read().strip()
        
        if rust_version != EXPECTED_RUST_VERSION:
            print(f"[WARNING] Version Rust inattendue : {rust_version} (attendu : {EXPECTED_RUST_VERSION})", file=sys.stderr)
        else:
            print(f"[INFO] Version Rust OK : {rust_version}")
            
    except Exception as e:
        print(f"[ERROR] Erreur vérification Rust : {e}", file=sys.stderr)
```

---

## Instructions d'intégration

### Fichier : `~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py`

1. **Ajouter les constantes** après les définitions existantes (après `PORT = 17777`) :
   ```python
   EXPECTED_RUST_VERSION = "2.1.0"
   RUST_CORE_DIR = Path("/Users/christophe/crypto-voice-assistant-core")
   ```

2. **Ajouter la fonction** `_check_rust_version()` après la fonction `_ace_link()` (ou après les autres fonctions utilitaires)

3. **Appeler la fonction** dans le `main()` ou au démarrage du serveur, après l'initialisation :
   ```python
   if __name__ == "__main__":
       _check_rust_version()  # Vérification non fatale du coeur Rust
       # ... reste du code existant
   ```

### Vérifications
- Le script ne doit pas planter si le dossier `crypto-voice-assistant-core` n'existe pas
- Le warning/error doit apparaître dans les logs mais ne pas bloquer le démarrage
- Ajuster `EXPECTED_RUST_VERSION` selon la version réelle dans `~/crypto-voice-assistant-core/VERSION`

### Test rapide
```bash
cd ~/ace777-test-day1/Index_Maison/scripts
python3 -c "import cortana_cockpit_bridge; cortana_cockpit_bridge._check_rust_version()"
```

---

**Hub /health** : `{"status": "ok", "providers": 9}` — prêt pour la suite du setup.
