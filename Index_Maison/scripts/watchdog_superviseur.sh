#!/usr/bin/env bash
# ============================================================
# watchdog_superviseur.sh — C10 : relance le superviseur-core
# Vérifie que superviseur_core.sh tourne, sinon le relance.
# Lancement : launchd toutes les 2 min (120 s)
# Corrections famille (10/08) : pgrep robuste (4), vérification
# post-relance (5), plist vérifié avant load (6).
# ============================================================
set -u

STATE_DIR="$HOME/.superviseur_core"
WATCHDOG_LOG="$STATE_DIR/watchdog.log"
PLIST_LABEL="com.ace777.superviseur-core"
PLIST="$HOME/Library/LaunchAgents/$PLIST_LABEL.plist"

mkdir -p "$STATE_DIR"

# Journalisation horodatée
watchdog_log() {
    echo "$(date '+%Y-%m-%dT%H:%M:%S%z') $1" >> "$WATCHDOG_LOG"
}

# Correction 4 (DEEPSEEK+ULTRA) : pgrep ciblé — la commande réelle du
# superviseur se termine par superviseur_core.sh en fin de ligne de commande
# (évite les faux positifs : un éditeur ouvert sur ce fichier).
check_process() {
    pgrep -f 'superviseur_core\.sh$' >/dev/null 2>&1
}

# Correction 6 (ULTRA) : plist doit exister avant toute tentative de relance
if [ ! -f "$PLIST" ]; then
    watchdog_log "ERREUR: plist manquant: $PLIST"
    echo "WATCHDOG=RELANCEMENT"
    exit 1
fi

# Superviseur vivant — rien à faire
if check_process; then
    echo "WATCHDOG=OK"
    exit 0
fi

# Superviseur mort — tentative de relance
watchdog_log "SUPERVISEUR MORT — tentative de relance"

# Essai kickstart (si le service est chargé)
if launchctl kickstart -k "gui/$(id -u)/$PLIST_LABEL" 2>/dev/null; then
    watchdog_log "Relance via kickstart demandée"
else
    # Fallback : chargement du plist
    if launchctl load "$PLIST" 2>/dev/null; then
        watchdog_log "Relance via load demandée"
    else
        watchdog_log "ERREUR: kickstart ET load ont échoué"
        echo "WATCHDOG=RELANCEMENT"
        exit 1
    fi
fi

# Correction 5 (DEEPSEEK) : vérification POST-relance — on attend 3 s
# puis on re-vérifie que le superviseur tourne vraiment.
sleep 3
if check_process; then
    watchdog_log "Relance CONFIRMÉE (processus actif après 3 s)"
    echo "WATCHDOG=RELANCEMENT"
    exit 0
else
    watchdog_log "ÉCHEC: processus toujours absent après relance"
    echo "WATCHDOG=RELANCEMENT"
    exit 1
fi
