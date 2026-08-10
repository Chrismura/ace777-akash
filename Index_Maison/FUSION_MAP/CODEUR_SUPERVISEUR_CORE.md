# SUPERVISEUR_CORE — CODE PRODUIT PAR LE HUB (via NVIDIA build.nvidia.com (100+ modeles), task code.ia) — 10/08/2026

## Mission envoyee

Systeme ACE777 - Mac 8 Go, hub local 11435, 9 providers gratuits. Fusion des services en cours (FUSION_MAP.md, decision famille unanime : ameliorer d'abord). Tu es le CODEUR du hub.

TA MISSION : creer /Users/christophe/ace777-test-day1/Index_Maison/scripts/superviseur_core.sh — la COLONNE VERTEBRALE monitoring qui absorbe 5 services launchd qui tournaient en parallele (heartbeat, pulse-sous-loeil, vigie, surveillance-quotas, rotation-logs). Le plist tournera toutes les 15 min (900 s) ; les cadences internes de chaque check (1 h, 30 min, 6 h) sont gerees par des fichiers timestamp dans $HOME/.superviseur_core/ (pas de cron).

REGLES ABSOLUES :
1. Le superviseur LIT state.json, il ne l'ECRIT JAMAIS (le state-generator est le SEUL ecrivain de Index_Maison/system/state.json)
2. Chaque check doit produire EXACTEMENT les memes sorties que le script original (memes chemins, memes fichiers) — liste ci-dessous
3. Non fatal : un check qui echoue n'empeche pas les autres (set -u, pas de set -e global)
4. Bash macOS standard (pas de GNU utils, pas de date -d), Python3 stdlib si besoin
5. Commentaires en francais, style des scripts existants
6. Un seul run = execution SEQUENTIELLE des checks dont la cadence est due (timestamp age >= intervalle)

LES 5 CHECKS A ABSORBER (chemins REELS verifies) :

## 1. HEARTBEAT (cadence 1 h) — script original heartbeat.py
- Verifie hub /health (timeout 6 s), RAM (vm_stat), git status
- Ecrit ~/prise-ia/heartbeat.json (json : horodatage, hub_ok, ram, git, etc.)
- Si hub KO plusieurs fois : ecrit Index_Maison/OUTBOX_OBSIDIAN/A_Mon_Attention/HEARTBEAT_ALERT.md ET cree Index_Maison/PAUSE_ORCHESTRATRICE
- Conserve ce comportement a l'identique (PAUSE file inclus)

## 2. PULSE SOUS L'OEIL (cadence 15 min = a CHAQUE run) — script original pulse_sous_loeil.sh
- Lecture seule "machine OK ?" : mode VOL/FROID (pgrep ACE/Hulk/Ollama), RAM, champion md5 (genesis_manifest.txt prefixe 37fca367), age heartbeat/live
- Ecrit Index_Maison/SOUS_L_OEIL.md + copie vers Index_Maison/OUTBOX_OBSIDIAN/SOUS_L_OEIL.md + Index_Maison/OUTBOX_OBSIDIAN/Index_Maison/SOUS_L_OEIL.md (LES 3 COPIES)
- Verdict PULSE=OK/WARN/NOK selon nombre de fail/warn

## 3. VIGIE (cadence 30 min) — script original vigie.sh
- Sentinelle securite : chmod 600 des secrets trop ouverts (.env, credentials, id_rsa...), detection nouvelle persistance (LaunchAgents/cron diff vs ~/.vigie/persistence.txt), ports d'ecoute non-loopback, integrite fichiers cles (sha256 baseline ~/.vigie/baseline.txt), secrets suivis par git, FileVault/pare-feu/womp, hub 11435 expose
- Etat dans ~/.vigie/ (state.txt, SECURITE_VIGIE.md) — ne doit ALERTER qu'au CHANGEMENT (state persiste)
- Exit 2 si alertes = etat constate, PAS une erreur (ne pas faire echouer le core)

## 4. SURVEILLANCE QUOTAS (cadence 30 min) — script original surveillance_quotas.py
- Lit ~/prise-ia/usage.jsonl + ~/prise-ia/providers.json
- Calcule usage/jour par provider vs cloud_daily_budget (routing.json) et quotas par tache
- Ecrit ~/prise-ia/reports/SURVEILLANCE_QUOTAS.log + SURVEILLANCE_QUOTAS.out.log
- Alerte dans le log si un quota depasse

## 5. ROTATION LOGS (cadence 6 h) — script original rotation_logs.py
- Rotation COPYTRUNCATE des fichiers > 500 Ko : usage.jsonl, hub_events.jsonl, reports/*.log, SUPERVISEUR.log (3 backups .1 .2 .3)
- Ne JAMAIS supprimer le fichier live (copie puis truncate) — ne touche JAMAIS au hub
- Journalise dans ~/prise-ia/reports/ROTATION.log

## CONTRAT DE SORTIE (le core doit imprimer en fin de run)
Ligne unique : CORE=OK|WARN|NOK checks=heartbeat:OK,pulse:OK,vigie:OK,quotas:OK,rotation:OK
OK = 0 fail, WARN = au moins 1 warn (ou vigie a des alertes = etat constate), NOK = un check a echoue (exception/erreur)

## CONTRAINTES DE MISE EN OEUVRE
- Fichier de sortie : /Users/christophe/ace777-test-day1/Index_Maison/scripts/superviseur_core.sh (executable)
- Fichiers timestamp : $HOME/.superviseur_core/<check>.last (date epoch via python3 -c 'import time;print(int(time.time()))' pour rester portable)
- Log du core : /tmp/superviseur-core.log (append, borne 500 lignes)
- Le core ne doit JAMAIS appeler le hub en LLM — uniquement des checks locaux + curl /health
- Garde un drapeau --force pour forcer tous les checks (test)

REPONDS EN FRANCAIS, CONCIS :
1. Le code COMPLET de superviseur_core.sh (pret a copier, dans un bloc ```bash```) — c'est l'ESSENTIEL
2. 5 lignes max : chmod + test --force + les 5 chemins de sortie attendus

Hub /health a l'envoi : {"status": "ok", "providers": 9}

Contexte reel (extraits bruts des scripts originaux a absorber) :
--- heartbeat.py (extrait) ---
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Généré par Google Gemini via hub (loi 1quinquies : Ada spécifie, le hub écrit) — 09/08
# Fichier : heartbeat.py
import os
import sys
import json
import re
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

HOME = Path("/Users/christophe")
VAULT = HOME / "Documents" / "Obsidian_ACE777"
MAISON = HOME / "ace777-test-day1"
OUTBOX = MAISON / "Index_Maison" / "OUTBOX_OBSIDIAN"
PRISE_IA = HOME / "prise-ia"
REPORTS = PRISE_IA / "reports"
HEARTBEAT_JSON = PRISE_IA / "heartbeat.json"
GRAPH_FILE = MAISON / "Index_Maison" / "graph_cerveau" / "data.js"
QWEN_IDEES = OUTBOX / "AUTO_EVOL" / "IDEES.md"
QWEN_LOG = REPORTS / "QWEN_ELABORE.log"
PAUSE_FILE = MAISON / "Index_Maison" / "PAUSE_ORCHESTRATRICE"
ALERT_FILE = OUTBOX / "A_Mon_Attention" / "HEARTBEAT_ALERT.md"
HUB_HEALTH_URL = "http://127.0.0.1:11435/health"

def obtenir_temps_actuel():
    return datetime.now(timezone.utc)

def fichier_age_heures(chemin):
    if not chemin.exists():
        return 9999.0
    mtime = chemin.stat().st_mtime
    dt_mtime = datetime.fromtimestamp(mtime, timezone.utc)
    delta = obtenir_temps_actuel() - dt_mtime
    return delta.total_seconds() / 3600.0

courant_epoch = lambda: obtenir_temps_actuel().strftime("%Y-%m-%dT%H:%M:%SZ")

def verifier_hub():
    req = Request(HUB_HEALTH_URL, method="GET")
    try:
        with urlopen(req, timeout=6) as response:
            return response.status == 200
    except (URLError, HTTPError, TimeoutError, Exception):
        return False

def mesurer_ram():
    try:
        res = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True, timeout=5)
        sortie = res.stdout
        match = re.search(r"System-wide memory free percentage:\s*(\d+)%", sortie)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return 100
--- pulse_sous_loeil.sh (extrait) ---
#!/usr/bin/env bash
# Pulse « sous l'œil » — machine OK toute seule ? (lecture seule, jamais de GO)
# Écrit Index_Maison/SOUS_L_OEIL.md (+ OUTBOX miroir).
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
OUT="$ROOT/Index_Maison"
TS_UTC="$(date -u +%Y-%m-%dT%H:%MZ)"
TS_LOC="$(date +%Y-%m-%dT%H:%M)"
REPORT="$OUT/SOUS_L_OEIL.md"
LOG_DIR="$OUT/scripts/logs"
mkdir -p "$LOG_DIR" "$OUT/OUTBOX_OBSIDIAN/Index_Maison"

alive() { pgrep -lf "$1" >/dev/null 2>&1; }
count_p() { pgrep -lf "$1" 2>/dev/null | wc -l | tr -d ' '; }

ACE_ON=0; HULK_ON=0; OLLAMA_ON=0
alive 'GO_USINE_NUAGE|ace777_launch_v85|launch_vide_froid' && ACE_ON=1
# fallback: fortress pendant vol
[[ "$ACE_ON" -eq 0 ]] && alive 'launch_test_master_base_v8_6_fortress' && ACE_ON=1
alive 'paper_diprip' && HULK_ON=1
alive 'ollama serve' && OLLAMA_ON=1

MODE="FROID"
[[ "$ACE_ON" -eq 1 || "$HULK_ON" -eq 1 ]] && MODE="VOL"

# RAM
eval "$(python3 - <<'PY'
import subprocess
try:
  ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
  ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
  if ":" not in line: continue
  k, v = line.split(":", 1)
  try: d[k.strip()] = int(v.strip().rstrip("."))
  except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"FREE_MB={free:.0f}")
if free >= 400: print("RAM_LABEL=OK")
elif free >= 200: print("RAM_LABEL=TIGHT")
else: print("RAM_LABEL=CRITIQUE")
PY
)"

# Champion
GEN_MD5="$(md5 -q "$ROOT/genesis_manifest.txt" 2>/dev/null || echo MISSING)"
if [[ "$GEN_MD5" == 37fca367* ]]; then CHAMP="OK"; else CHAMP="FAIL"; fi

# Heartbeat / LIVE age (si vol)
HB_AGE="—"
LIVE_AGE="—"
LIVE_TAG="—"
--- vigie.sh (extrait) ---
#!/usr/bin/env bash
# ============================================================
# vigie.sh — LA VIGIE : sentinelle de sécurité ACE777
# Lecture seule SAUF chmod 600 des secrets trop ouverts (seul auto-fix).
# Usage : bash vigie.sh [--force]
# Launchd : com.ace777.vigie.plist (toutes les 30 min + au login)
# NB : vit hors de ~/Documents (TCC) pour être exécutable par launchd.
# NB : baseline et références créées le 06/08/2026 APRÈS un audit manuel complet
#      de la machine (vérifiée avant la première exécution de la Vigie).
# ============================================================
set -uo pipefail

HOME_DIR="$HOME"
VAULT="$HOME_DIR/Documents/Obsidian_ACE777"
STATE_DIR="$HOME_DIR/.vigie"
LOG="$HOME_DIR/Library/Logs/vigie.log"
NOTE="$STATE_DIR/SECURITE_VIGIE.md"
BASELINE="$STATE_DIR/baseline.txt"
PERSIST_REF="$STATE_DIR/persistence.txt"
STATE_FILE="$STATE_DIR/state.txt"

mkdir -p "$STATE_DIR"
FORCE=0; [ "${1:-}" = "--force" ] && FORCE=1

ALERTS=(); FIXED=()
now="$(date '+%Y-%m-%dT%H:%M:%S%z')"
log() { printf '%s %s\n' "$now" "$1" >> "$LOG"; }

# ---------- 1) Permissions des secrets (auto-chmod 600) ----------
fix_perm() {
  local f="$1" p
  [ -e "$f" ] || return
  # ne touche que les fichiers appartenant à l'utilisateur courant
  [ "$(stat -f %u "$f" 2>/dev/null)" = "$(id -u)" ] || return
  p=$(stat -f '%Lp' "$f" 2>/dev/null)
  if [ -n "$p" ] && [ "$p" != "600" ]; then
    chmod 600 "$f" 2>/dev/null && FIXED+=("chmod 600 : $f")
  fi
}
while IFS= read -r f; do fix_perm "$f"; done < <(find "$HOME_DIR" -maxdepth 4 \( -iname '*.env' -o -iname '*credential*' -o -iname '*secret*' -o -iname '*api_key*' -o -iname '*.pem' -o -iname 'id_rsa' -o -iname 'id_ed25519' \) -not -path '*/Library/*' -not -path '*/.git/*' 2>/dev/null)
for f in "$HOME_DIR/.config/manicode/credentials.json" "$HOME_DIR/.claude.json" "$HOME_DIR/.binance_testnet.env" "$HOME_DIR/prise-ia/.env" "$HOME_DIR/crypto-voice-assistant-core/.env"; do
  [ -e "$f" ] && fix_perm "$f"
done

# ---------- 2) Persistance nouvelle (1 seule alerte par item) ----------
persist_now="$STATE_DIR/persistence.now"
{
  ls -1 "$HOME_DIR/Library/LaunchAgents/" 2>/dev/null
  ls -1 /Library/LaunchAgents/ 2>/dev/null
  ls -1 /Library/LaunchDaemons/ 2>/dev/null
  crontab -l 2>/dev/null
} | sort -u > "$persist_now"
SEEN="$STATE_DIR/seen.txt"
[ -f "$SEEN" ] || : > "$SEEN"
if [ ! -f "$PERSIST_REF" ]; then
  cp "$persist_now" "$PERSIST_REF"
else
  while IFS= read -r item; do
    if ! grep -qxF "$item" "$PERSIST_REF" 2>/dev/null; then
      if ! grep -qxF "$item" "$SEEN" 2>/dev/null; then
--- surveillance_quotas.py (extrait) ---
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# surveillance_quotas.py — ecrit par GEMINI (delegation Ada, loi 1quinquies)
# Etape 2 Phase 0 : remplace la jauge supprimee (surveillance minimale quotas).
#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime, timezone
from collections import defaultdict

HOME = os.path.expanduser("~")
BASE_DIR = os.path.join(HOME, "prise-ia")
USAGE_FILE = os.path.join(BASE_DIR, "usage.jsonl")
PROVIDERS_FILE = os.path.join(BASE_DIR, "providers.json")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.log")

def read_json_file(path, description):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERREUR: {description} introuvable: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERREUR: {description} invalide: {path} - {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"ERREUR: impossible de lire {description}: {path} - {e}", file=sys.stderr)
--- rotation_logs.py (extrait) ---
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rotation_logs.py — ecrit par GEMINI (delegation Ada, loi 1quinquies)
# Etape 4 Phase 0 : rotation COPYTRUNCATE des logs (ne touche jamais le hub).
import os
import shutil
from datetime import datetime, timezone

SEUIL_OCTETS = 500000
BACKUP_COUNT = 3
BASE_DIR = "/Users/christophe/prise-ia"
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
ROTATION_LOG = os.path.join(REPORTS_DIR, "ROTATION.log")

def get_files():
    files = [
        os.path.join(REPORTS_DIR, "SYNC_LOG.md"),
        os.path.join(BASE_DIR, "usage.jsonl"),
        os.path.join(BASE_DIR, "hub_events.jsonl"),
        os.path.join(REPORTS_DIR, "SUPERVISEUR.log"),
    ]
    try:
        for entry in os.listdir(REPORTS_DIR):
            full = os.path.join(REPORTS_DIR, entry)
            if os.path.isfile(full) and (entry.endswith(".log") or entry.endswith(".out.log") or entry.endswith(".err.log")):
                files.append(full)
    except OSError:
        pass
    return files
--- superviseur_auto.py JOBS_ATTENDUS (a noter pour mise a jour ulterieure) ---
MAX_AGE_PREUVE_H = 24

HUB_URL = "http://127.0.0.1:11435/v1/chat/completions"
HUB_HEALTH_URL = "http://127.0.0.1:11435/health"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"

# Les 14 jobs launchd attendus (labels complets, vérifiés)
JOBS_ATTENDUS = [
    "com.ace777.qwen-btc", "com.ace777.cockpit-http", "com.ace777.cortana.horaire",
    "com.ace777.prise-ia", "com.ace777.analyse-usage", "com.ace777.analyste-cadence",
    "com.ace777.cockpit-pont", "com.ace777.journal-soir", "com.ace777.gitpush",
    "com.ace777.cortana.urgent", "com.ace777.brief-matin", "com.ace777.pulse-sous-loeil",
    "com.ace777.qwen-elabore", "com.ace777.vigie",
]

TIMEOUT_RESEAU = 5
TIMEOUT_HUB = 600
MAX_LOG_LINES = 200
MAX_RELANCES_JOUR_PAR_JOB = 3

# ============================================================================
--- FUSION_MAP.md (debut) ---
# 🗺️ FUSION_MAP — LA CARTE DE LA FUSION (10/08/2026)

> Écrite AVANT de casser quoi que ce soit (règle codeur + consultation famille : « on ne relit
> jamais le code pendant la fusion »). Objectif : zéro oubli de fonctionnalité.

## 🎯 Architecture cible

```
AVANT (6 services de supervision + monitoring)          APRÈS (2)
─────────────────────────────────────────────           ─────────────────────────
com.ace777.superviseur        (1 h, cerveau grok)   →   com.ace777.superviseur      (1 h, INCHANGÉ)
com.ace777.heartbeat          (1 h)                 ─┐
com.ace777.pulse-sous-loeil   (15 min)              ─┤→   com.ace777.superviseur-core (15 min)
com.ace777.vigie              (30 min)              ─┤      superviseur_core.sh
com.ace777.surveillance-quotas(30 min)              ─┤      (cadences internes par timestamp)
com.ace777.rotation-logs      (6 h)                 ─┘
```

**Règle d'or (codeur + famille)** : superviseur_core **LIT state.json, ne l'écrit JAMAIS**
(le state-generator est le SEUL écrivain) · KeepAlive · intervalle 900 s (> 120 s).

---

## 📋 Ce que chaque service fait — et ce que superviseur_core doit ABSORBER

| # | Service (plist) | Cadence | Ce qu'il fait (vérifié, pas de mémoire) | Absorbé par core ? |
|---|---|---|---|---|
| 1 | `com.ace777.heartbeat` | 1 h | Vérifie hub /health (6 s), RAM, git ; écrit `~/prise-ia/heartbeat.json` ; alerte HEARTBEAT_ALERT.md + fichier PAUSE si anomalie | ✅ **OUI** (cadence 1 h interne) |
| 2 | `com.ace777.pulse-sous-loeil` | 15 min | Lecture seule « machine OK ? » : mode vol/froid, process ACE/Hulk/Ollama, RAM, champion md5, heartbeat age ; écrit `SOUS_L_OEIL.md` (+ miroirs OUTBOX) | ✅ **OUI** (cadence 15 min = celle du core) |
| 3 | `com.ace777.vigie` | 30 min | Sentinelle sécurité : chmod 600 secrets trop ouverts (seul auto-fix), détection nouvelle persistance, ports non-loopback, intégrité fichiers clés (baseline sha256), secrets dans git, FileVault/pare-feu/womp, hub exposé ; état `~/.vigie/` | ✅ **OUI** (cadence 30 min interne) |
| 4 | `com.ace777.surveillance-quotas` | 30 min | Lit `usage.jsonl` + `providers.json` ; vérifie quotas/jour vs cloud_daily_budget ; écrit rapport `reports/SURVEILLANCE_QUOTAS.log` | ✅ **OUI** (cadence 30 min interne) |
| 5 | `com.ace777.rotation-logs` | 6 h | Rotation COPYTRUNCATE des logs > 500 Ko (usage.jsonl, hub_events, reports/*.log, SUPERVISEUR.log), 3 backups, log ROTATION.log | ✅ **OUI** (cadence 6 h interne) |
| 6 | `com.ace777.superviseur` | 1 h | **LE CERVEAU** : lit state/coffre → état → décision via hub `supervise.decision` (grok-4.3, fallback gemini) → agit (escalades, rappels lecture) | ❌ **INCHANGÉ** (reste tel quel) |

---

## 🔢 Ordre de la fusion (à respecter STRICTEMENT)

1. **Écrire** `superviseur_core.sh` (délégué au codeur du hub, task `code.ia`)
2. **TESTER manuellement** superviseur_core.sh SEUL (run réel) → doit produire :


## Reponse du codeur

```bash
#!/usr/bin/env bash
# ============================================================
# superviseur_core.sh — COLONNE VERTEBRALE monitoring ACE777
# Absorbe 5 services launchd : heartbeat, pulse-sous-loeil,
# vigie, surveillance-quotas, rotation-logs.
# Cadences internes par fichiers timestamp (~/.superviseur_core/)
# Lancement : launchd toutes les 15 min (900 s)
# ============================================================
set -uo pipefail

# ---------- Configuration ----------
HOME_DIR="$HOME"
MAISON="$HOME_DIR/ace777-test-day1"
INDEX="$MAISON/Index_Maison"
OUTBOX="$INDEX/OUTBOX_OBSIDIAN"
PRISE_IA="$HOME_DIR/prise-ia"
REPORTS="$PRISE_IA/reports"
STATE_DIR="$HOME_DIR/.superviseur_core"
LOG_CORE="/tmp/superviseur-core.log"
FORCE=0

# ---------- Utilitaires ----------
mkdir -p "$STATE_DIR" "$REPORTS" "$OUTBOX/A_Mon_Attention" "$OUTBOX/Index_Maison"

# Timestamp epoch portable (Python3)
epoch_now() {
    python3 -c 'import time; print(int(time.time()))'
}

# Vérifie si un check est dû (age >= intervalle secondes)
check_due() {
    local check="$1" interval="$2"
    [ "$FORCE" -eq 1 ] && return 0
    local last_file="$STATE_DIR/${check}.last"
    [ ! -f "$last_file" ] && return 0
    local last=$(cat "$last_file" 2>/dev/null || echo 0)
    local now=$(epoch_now)
    [ $((now - last)) -ge "$interval" ]
}

# Marque un check comme exécuté
mark_done() {
    local check="$1"
    epoch_now > "$STATE_DIR/${check}.last"
}

# Log core (append, borné 500 lignes)
core_log() {
    local msg="$1"
    echo "$(date '+%Y-%m-%dT%H:%M:%S%z') $msg" >> "$LOG_CORE"
    # Borne : garde les 500 dernières lignes
    if [ -f "$LOG_CORE" ]; then
        local lines=$(wc -l < "$LOG_CORE" 2>/dev/null || echo 0)
        if [ "$lines" -gt 500 ]; then
            tail -n 500 "$LOG_CORE" > "$LOG_CORE.tmp" && mv "$LOG_CORE.tmp" "$LOG_CORE"
        fi
    fi
}

# ---------- Check 1 : HEARTBEAT (1 h) ----------
check_heartbeat() {
    local status="OK" fail=0
    core_log "HEARTBEAT: début"
    
    # Vérifie hub /health (timeout 6 s)
    local hub_ok="false"
    if curl -s --max-time 6 http://127.0.0.1:11435/health >/dev/null 2>&1; then
        hub_ok="true"
    fi
    
    # RAM via vm_stat
    local ram_free=0
    eval "$(python3 - <<'PY'
import subprocess, re
try:
    ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
    ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
    if ":" not in line: continue
    k, v = line.split(":", 1)
    try: d[k.strip()] = int(v.strip().rstrip("."))
    except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"RAM_FREE={free:.0f}")
PY
)"
    
    # Git status
    local git_status="clean"
    if [ -d "$MAISON/.git" ]; then
        git -C "$MAISON" status --porcelain >/dev/null 2>&1 && git_status="dirty" || git_status="clean"
    fi
    
    # Écrit heartbeat.json
    python3 - "$hub_ok" "$ram_free" "$git_status" <<'PY'
import json, sys, os
from datetime import datetime, timezone
hub_ok = sys.argv[1] == "true"
ram_free = int(sys.argv[2])
git_status = sys.argv[3]
data = {
    "horodatage": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "hub_ok": hub_ok,
    "ram_free_mb": ram_free,
    "git_status": git_status,
    "source": "superviseur_core"
}
path = os.path.expanduser("~/prise-ia/heartbeat.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as f:
    json.dump(data, f, indent=2)
PY
    
    # Si hub KO : alerte + PAUSE (comportement identique)
    if [ "$hub_ok" = "false" ]; then
        fail=1
        # Vérifie si déjà alerté récemment (évite spam)
        local alert_file="$OUTBOX/A_Mon_Attention/HEARTBEAT_ALERT.md"
        local pause_file="$MAISON/Index_Maison/PAUSE_ORCHESTRATRICE"
        if [ ! -f "$alert_file" ] || [ $(( $(epoch_now) - $(stat -f %m "$alert_file" 2>/dev/null || echo 0) )) -gt 3600 ]; then
            cat > "$alert_file" <<EOF
# 🚨 HEARTBEAT ALERT

**Date** : $(date '+%Y-%m-%dT%H:%M:%S%z')
**Statut** : HUB INJOIGNABLE

Le hub local (127.0.0.1:11435) ne répond pas.
Cela peut indiquer un problème majeur.

**Actions** :
- Vérifier le processus hub
- Redémarrer si nécessaire
EOF
            touch "$pause_file"
            core_log "HEARTBEAT: ALERTE hub KO + PAUSE créée"
        fi
    fi
    
    mark_done "heartbeat"
    core_log "HEARTBEAT: fin (hub_ok=$hub_ok)"
    [ "$fail" -eq 0 ] && echo "OK" || echo "NOK"
}

# ---------- Check 2 : PULSE SOUS L'OEIL (15 min = chaque run) ----------
check_pulse() {
    local status="OK" fail=0 warn=0
    core_log "PULSE: début"
    
    # Mode VOL/FROID
    local ace_on=0 hulk_on=0 ollama_on=0
    pgrep -lf 'GO_USINE_NUAGE|ace777_launch_v85|launch_vide_froid' >/dev/null 2>&1 && ace_on=1
    [ "$ace_on" -eq 0 ] && pgrep -lf 'launch_test_master_base_v8_6_fortress' >/dev/null 2>&1 && ace_on=1
    pgrep -lf 'paper_diprip' >/dev/null 2>&1 && hulk_on=1
    pgrep -lf 'ollama serve' >/dev/null 2>&1 && ollama_on=1
    
    local mode="FROID"
    [ "$ace_on" -eq 1 ] || [ "$hulk_on" -eq 1 ] && mode="VOL"
    
    # RAM
    local ram_label="OK" ram_free=0
    eval "$(python3 - <<'PY'
import subprocess
try:
    ps = int(subprocess.check_output(["pagesize"], stderr=subprocess.DEVNULL).decode().strip())
except Exception:
    ps = 16384
out = subprocess.check_output(["vm_stat"], stderr=subprocess.DEVNULL).decode()
d = {}
for line in out.splitlines()[1:]:
    if ":" not in line: continue
    k, v = line.split(":", 1)
    try: d[k.strip()] = int(v.strip().rstrip("."))
    except Exception: pass
free = (d.get("Pages free", 0) + d.get("Pages speculative", 0)) * ps / 1024 / 1024
print(f"FREE_MB={free:.0f}")
if free >= 400: print("RAM_LABEL=OK")
elif free >= 200: print("RAM_LABEL=TIGHT")
else: print("RAM_LABEL=CRITIQUE")
PY
)"
    
    # Champion md5
    local champ="FAIL"
    local gen_md5=$(md5 -q "$MAISON/genesis_manifest.txt" 2>/dev/null || echo "MISSING")
    [[ "$gen_md5" == 37fca367* ]] && champ="OK"
    
    # Age heartbeat/live
    local hb_age="—" live_age="—"
    if [ -f "$PRISE_IA/heartbeat.json" ]; then
        hb_age=$(python3 -c "import os,time; print(f'{int(time.time()-os.path.getmtime(os.path.expanduser(\"~/prise-ia/heartbeat.json\")))}s')" 2>/dev/null || echo "—")
    fi
    
    # Verdict
    local verdict="OK"
    [ "$champ" = "FAIL" ] && { warn=$((warn+1)); verdict="WARN"; }
    [ "$ram_label" = "CRITIQUE" ] && { fail=$((fail+1)); verdict="NOK"; }
    [ "$ram_label" = "TIGHT" ] && { warn=$((warn+1)); [ "$verdict" = "OK" ] && verdict="WARN"; }
    
    # Écrit SOUS_L_OEIL.md (3 copies)
    local report="$INDEX/SOUS_L_OEIL.md"
    cat > "$report" <<EOF
# 👁️ SOUS L'ŒIL — Pulse machine

**Date** : $(date '+%Y-%m-%dT%H:%M:%S%z')
**Mode** : $mode
**Verdict** : $verdict

## Processus
- ACE (GO_USINE_NUAGE) : $([ "$ace_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")
- HULK (paper_diprip) : $([ "$hulk_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")
- OLLAMA (serve) : $([ "$ollama_on" -eq 1 ] && echo "✅ actif" || echo "❌ inactif")

## Ressources
- RAM libre : ${ram_free} Mo ($ram_label)
- Champion (genesis_manifest) : $champ

## Fraîcheur
- Heartbeat : $hb_age
- LIVE : $live_age

---
*Généré par superviseur_core.sh — lecture seule, jamais de GO*
EOF
    cp "$report" "$OUTBOX/SOUS_L_OEIL.md"
    cp "$report" "$OUTBOX/Index_Maison/SOUS_L_OEIL.md"
    
    mark_done "pulse"
    core_log "PULSE: fin (verdict=$verdict)"
    echo "$verdict"
}

# ---------- Check 3 : VIGIE (30 min) ----------
check_vigie() {
    local status="OK" fail=0
    core_log "VIGIE: début"
    
    local vigie_dir="$HOME_DIR/.vigie"
    mkdir -p "$vigie_dir"
    local alerts=() fixed=()
    local now="$(date '+%Y-%m-%dT%H:%M:%S%z')"
    
    # 1) Permissions secrets (auto-chmod 600)
    fix_perm() {
        local f="$1" p
        [ -e "$f" ] || return
        [ "$(stat -f %u "$f" 2>/dev/null)" = "$(id -u)" ] || return
        p=$(stat -f '%Lp' "$f" 2>/dev/null)
        if [ -n "$p" ] && [ "$p" != "600" ]; then
            chmod 600 "$f" 2>/dev/null && fixed+=("chmod 600 : $f")
        fi
    }
    while IFS= read -r f; do fix_perm "$f"; done < <(find "$HOME_DIR" -maxdepth 4 \( -iname '*.env' -o -iname '*credential*' -o -iname '*secret*' -o -iname '*api_key*' -o -iname '*.pem' -o -iname 'id_rsa' -o -iname 'id_ed25519' \) -not -path '*/Library/*' -not -path '*/.git/*' 2>/dev/null)
    for f in "$HOME_DIR/.config/manicode/credentials.json" "$HOME_DIR/.claude.json" "$HOME_DIR/.binance_testnet.env" "$HOME_DIR/prise-ia/.env" "$HOME_DIR/crypto-voice-assistant-core/.env"; do
        [ -e "$f" ] && fix_perm "$f"
    done
    
    # 2) Persistance nouvelle
    local persist_now="$vigie_dir/persistence.now"
    {
        ls -1 "$HOME_DIR/Library/LaunchAgents/" 2>/dev/null
        ls -1 /Library/LaunchAgents/ 2>/dev/null
        ls -1 /Library/LaunchDaemons/ 2>/dev/null
        crontab -l 2>/dev/null
    } | sort -u > "$persist_now"
    local seen="$vigie_dir/seen.txt"
    [ -f "$seen" ] || : > "$seen"
    if [ ! -f "$vigie_dir/persistence.txt" ]; then
        cp "$persist_now" "$vigie_dir/persistence.txt"
    else
        while IFS= read -r item; do
            if ! grep -qxF "$item" "$vigie_dir/persistence.txt" 2>/dev/null; then
                if ! grep -qxF "$item" "$seen" 2>/dev/null; then
                    alerts+=("NOUVELLE PERSISTANCE: $item")
                    echo "$item" >> "$seen"
                fi
            fi
        done < "$persist_now"
    fi
    
    # 3) Ports non-loopback
    local ports=$(lsof -iTCP -sTCP:LISTEN -P 2>/dev/null | grep -v "127.0.0.1" | grep -v "::1" | grep -v "localhost" | grep -v "COMMAND" | head -5)
    [ -n "$ports" ] && alerts+=("PORTS NON-LOOPBACK: $ports")
    
    # 4) Intégrité fichiers clés (baseline sha256)
    if [ -f "$vigie_dir/baseline.txt" ]; then
        while IFS= read -r line; do
            [ -z "$line" ] && continue
            local hash=$(echo "$line" | awk '{print $1}')
            local file=$(echo "$line" | awk '{print $2}')
            if [ -f "$file" ]; then
                local current=$(shasum -a 256 "$file" | awk '{print $1}')
                [ "$current" != "$hash" ] && alerts+=("INTEGRITE: $file modifié")
            fi
        done < "$vigie_dir/baseline.txt"
    fi
    
    # 5) Secrets suivis par git
    if [ -d "$MAISON/.git" ]; then
        local git_secrets=$(git -C "$MAISON" ls-files 2>/dev/null | grep -E '\.env$|credential|secret|api_key' | head -3)
        [ -n "$git_secrets" ] && alerts+=("SECRETS DANS GIT: $git_secrets")
    fi
    
    # 6) FileVault / pare-feu / womp
    local fv=$(fdesetup status 2>/dev/null | grep -c "On" || echo 0)
    [ "$fv" -eq 0 ] && alerts+=("FILEVAULT DESACTIVE")
    local pf=$(/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate 2>/dev/null | grep -c "enabled" || echo 0)
    [ "$pf" -eq 0 ] && alerts+=("PARE-FEU DESACTIVE")
    local womp=$(pmset -g custom 2>/dev/null | grep -c "womp.*1" || echo 0)
    [ "$womp" -eq 0 ] && alerts+=("WOMP DESACTIVE")
    
    # 7) Hub 11435 exposé
    local hub_exposed=$(lsof -iTCP:11435 -sTCP:LISTEN -P 2>/dev/null | grep -v "127.0.0.1" | grep -v "::1" | grep -v "COMMAND" | head -1)
    [ -n "$hub_exposed" ] && alerts+=("HUB EXPOSE: $hub_exposed")
    
    # Écrit état (ne alerte qu'au CHANGEMENT)
    local state_file="$vigie_dir/state.txt"
    local prev_state=""
    [ -f "$state_file" ] && prev_state=$(cat "$state_file")
    local new_state="OK"
    [ ${#alerts[@]} -gt 0 ] && new_state="ALERTES: ${#alerts[@]}"
    
    if [ "$new_state" != "$prev_state" ]; then
        # Écrit SECURITE_VIGIE.md seulement si changement
        cat > "$vigie_dir/SECURITE_VIGIE.md" <<EOF
# 🛡️ SECURITE VIGIE

**Date** : $now
**État** : $new_state

## Alertes (${#alerts[@]})
$(for a in "${alerts[@]}"; do echo "- $a"; done)

## Corrections auto (${#fixed[@]})
$(for f in "${fixed[@]}"; do echo "- $f"; done)

---
*Généré par superviseur_core.sh — sentinelle sécurité*
EOF
        echo "$new_state" > "$state_file"
        core_log "VIGIE: changement d'état -> $new_state"
    fi
    
    # Exit 2 si alertes = état constaté, PAS une erreur
    mark_done "vigie"
    core_log "VIGIE: fin (alertes=${#alerts[@]})"
    if [ ${#alerts[@]} -gt 0 ]; then
        echo "WARN"
    else
        echo "OK"
    fi
}

# ---------- Check 4 : SURVEILLANCE QUOTAS (30 min) ----------
check_quotas() {
    local status="OK" fail=0
    core_log "QUOTAS: début"
    
    python3 <<'PY'
import os, json, sys
from datetime import datetime, timezone
from collections import defaultdict

HOME = os.path.expanduser("~")
BASE_DIR = os.path.join(HOME, "prise-ia")
USAGE_FILE = os.path.join(BASE_DIR, "usage.jsonl")
PROVIDERS_FILE = os.path.join(BASE_DIR, "providers.json")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.log")
OUT_LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.out.log")

os.makedirs(REPORT_DIR, exist_ok=True)


