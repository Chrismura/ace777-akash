#!/bin/bash
# superviseur.sh - Superviseur de processus vitaux + heartbeat (brique C)
# Lancement : bash superviseur.sh &   (ou launchd KeepAlive)
# Corrections intégration (Buffy 11/08) : bash 3.2 macOS (pas de declare -A),
# chemins explicites (journal_radar.log est dans ../strategie/).

# === VARIABLES DE CONFIGURATION ===
SCRIPTS_DIR="/Users/christophe/ace777-test-day1/Index_Maison/scripts"
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
    case "$proc" in
        hub)
            nohup python3 "$SCRIPTS_DIR/../..//prise-ia/hub_prise_ia.py" > /dev/null 2>&1 &
            ;;
        vigie)
            nohup python3 "$SCRIPTS_DIR/vigie_live.py" > /dev/null 2>&1 &
            ;;
        cockpit)
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

    # --- VIGIE + HEARTBEAT (décrochage silencieux WebSocket) ---
    if is_running "vigie_live.py"; then
        mtime=$(get_mtime "$HEARTBEAT_FILE")
        now=$(date +%s)
        age=$((now - mtime))
        if [ "$age" -gt "$HEARTBEAT_MAX_AGE" ]; then
            restart_process "vigie" "heartbeat absent depuis ${age}s (décrochage)"
            status_line="$status_line | vigie:RELAUNCH_HEARTBEAT"
        else
            status_line="$status_line | vigie:OK"
        fi
    else
        restart_process "vigie" "processus absent"
        status_line="$status_line | vigie:RELAUNCH"
    fi

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
