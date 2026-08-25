#!/bin/bash
# superviseur.sh - Superviseur de processus vitaux + heartbeat (brique C)
# Lancement : bash superviseur.sh &   (ou launchd KeepAlive)
# Corrections intégration (Buffy 11/08) : bash 3.2 macOS (pas de declare -A),
# chemins explicites (journal_radar.log est dans ../strategie/).

# === VARIABLES DE CONFIGURATION ===
SCRIPTS_DIR="/Users/christophe/ace777-test-day1/Index_Maison/scripts"

# === TRACE DE MORT (PAA-ACE777 ajout 2, 20/08) ===
# Le 19/08, ce script est mort à 14:09:12 SANS trace (classe 1, probablement
# OOM). Désormais toute mort (TERM/INT/ERR/EXIT rc!=0) est journalisée dans
# /tmp/superviseur_morts.log avec signal, ligne, RSS (diagnostic OOM) et stack.
source "$SCRIPTS_DIR/trap_mort.sh"
TRAP_MORT_LOG="/tmp/superviseur_morts.log"
trap_mort_init 2>/dev/null || true
STRATEGIE_DIR="/Users/christophe/ace777-test-day1/Index_Maison/strategie"
LOG_FILE="$SCRIPTS_DIR/superviseur.log"
HEARTBEAT_FILE="$STRATEGIE_DIR/journal_radar.log"
RESTART_DIR="/tmp/superviseur_restarts"
LOCK_FILE="/tmp/superviseur.lock"

MAX_RESTARTS=3
RESTART_WINDOW_MIN=10
SLEEP_INTERVAL=60
HEARTBEAT_MAX_AGE=180

# === FONCTIONS ===

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

is_running() {
    pgrep -f "$1" > /dev/null 2>&1
}

get_mtime() {
    if [ -f "$1" ]; then
        stat -f %m "$1"
    else
        echo 0
    fi
}

check_restart_limit() {
    local proc="$1"
    mkdir -p "$RESTART_DIR"
    find "$RESTART_DIR" -name "${proc}_*" -mmin "-$RESTART_WINDOW_MIN" | wc -l
}

record_restart() {
    local proc="$1"
    mkdir -p "$RESTART_DIR"
    touch "$RESTART_DIR/${proc}_$(date +%s)"
}

# Relance selon le processus (bash 3.2 : case au lieu de declare -A)
restart_process() {
    local proc="$1"
    local reason="$2"
    local count
    count=$(check_restart_limit "$proc")

    if [ "$count" -ge "$MAX_RESTARTS" ]; then
        log "ALERTE: $proc a atteint $MAX_RESTARTS relances en $RESTART_WINDOW_MIN min - intervention humaine requise"
        return 1
    fi

    log "RELANCE $proc : $reason"
    # CORRECTIF 16/08 (Buffy) : tuer l'ancien process AVANT de relancer.
    # Sinon accumulation de doublons (13 vigies en 7h). Les pkill ne matchent
    # JAMAIS superviseur.sh lui-même (patterns = noms de scripts Python).
    case "$proc" in
        hub)
            pkill -f "hub_prise_ia.py" 2>/dev/null; sleep 1
            nohup python3 "$SCRIPTS_DIR/../..//prise-ia/hub_prise_ia.py" > /dev/null 2>&1 &
            ;;
        vigie)
            pkill -f "vigie_live.py" 2>/dev/null; sleep 1
            nohup python3 "$SCRIPTS_DIR/vigie_live.py" > /dev/null 2>&1 &
            ;;
        cockpit)
            pkill -f "cockpit_http_server.py" 2>/dev/null; sleep 1
            nohup python3 "$SCRIPTS_DIR/cockpit_http_server.py" > /dev/null 2>&1 &
            ;;
    esac
    record_restart "$proc"
    sleep 2
}

# === GARDE-FOU ANTI-DOUBLON ===
if [ -f "$LOCK_FILE" ]; then
    old_pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if ps -p "$old_pid" > /dev/null 2>&1; then
        echo "Superviseur déjà en cours (PID $old_pid)"
        exit 0
    fi
fi
echo $$ > "$LOCK_FILE"

log "=== Superviseur démarré (PID $$) ==="

# === BOUCLE PRINCIPALE ===
while true; do
    status_line="vérif"

    # --- HUB (dossier prise-ia) ---
    if is_running "hub_prise_ia.py"; then
        status_line="$status_line | hub:OK"
    else
        restart_process "hub" "processus absent"
        status_line="$status_line | hub:RELAUNCH"
    fi

    # --- VIGIE : gérée par launchd (plist com.ace777.vigie-live, KeepAlive=true).
    # 24/08 : retirée de la supervision ici — deux propriétaires (launchd + ce
    # superviseur) se battaient au boot (le pkill de relance tuait celle de
    # launchd qui en relançait une 2e → doublons). launchd en maintient une
    # seule ; la fraîcheur du heartbeat est couverte par veille_degradation +
    # sante_index (alerte, pas de relance auto).
    status_line="$status_line | vigie:launchd"

    # --- COCKPIT ---
    if is_running "cockpit_http_server.py"; then
        status_line="$status_line | cockpit:OK"
    else
        restart_process "cockpit" "processus absent"
        status_line="$status_line | cockpit:RELAUNCH"
    fi

    log "$status_line"
    sleep "$SLEEP_INTERVAL"
done
