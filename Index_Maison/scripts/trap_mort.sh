#!/bin/bash
# trap_mort.sh — TRACE DE MORT (exigence famille, PAA-ACE777 ajout 2, 20/08)
#
# La classe 1 (mort silencieuse) = un script meurt SANS trace. Le 19/08,
# superviseur.sh est mort à 14:09:12 sans aucun message (probablement OOM).
# Ce script, sourcé par les scripts critiques, journalise TOUTE sortie
# anormale : signal reçu, code de sortie, ligne, dernière commande.
#
# Usage dans un script critique :
#   source /Users/christophe/ace777-test-day1/Index_Maison/scripts/trap_mort.sh
#   TRAP_MORT_LOG="/tmp/mon_script_mort.log" trap_mort_init
#
# Journalise dans : $TRAP_MORT_LOG (défaut /tmp/ace777_morts.log, append-only).

TRAP_MORT_LOG="${TRAP_MORT_LOG:-/tmp/ace777_morts.log}"

_mort_trace() {
    local signal="$1"
    local rc="$2"
    local line="$3"
    {
        echo "=== MORT $(date '+%Y-%m-%d %H:%M:%S') — pid $$ — $0 ==="
        echo "signal=$signal rc=$rc ligne=$line"
        echo "dernière commande: $(history 1 2>/dev/null | tail -1 | sed 's/^ *[0-9]* *//')"
        # état mémoire du process (pour diagnostiquer un OOM)
        if command -v ps >/dev/null 2>&1; then
            echo "rss_kb=$(ps -o rss= -p $$ 2>/dev/null | tr -d ' ')"
        fi
        echo "stack: $(caller 0 2>/dev/null || echo n/a)"
    } >> "$TRAP_MORT_LOG" 2>/dev/null
}

trap_mort_init() {
    mkdir -p "$(dirname "$TRAP_MORT_LOG")"
    # SIGTERM (arrêt demandé) — normal si volontaire, mais tracé quand même
    trap '_mort_trace TERM $? $LINENO; exit 0' TERM
    # SIGINT
    trap '_mort_trace INT $? $LINENO; exit 0' INT
    # Toute erreur (set -e) : tracer avant de mourir
    trap '_mort_trace ERR $? $LINENO' ERR
    # Sortie du script : tracer si rc != 0
    trap '_mort_trace EXIT $? $LINENO' EXIT
}

# SIGKILL ne peut pas être piégé (kill -9) — mais on trace au démarrage
# l'identité du script pour que la rupture soit détectable a posteriori.
_mort_identite() {
    echo "IDENTITE $(date '+%Y-%m-%d %H:%M:%S') pid=$$ script=$0" >> "$TRAP_MORT_LOG" 2>/dev/null
}
