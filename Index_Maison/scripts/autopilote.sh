#!/bin/bash
# autopilote.sh — LE DÉMARREUR ACE777 (CONTRAT_AUTOGESTION §5, GO 2) — 09/08/2026
# Cadence : toutes les 15 min (launchd com.ace777.autopilote).
# 1) Pulse machine (lecture seule) · 2) Auto-heal infra (jobs absents) ·
# 3) Brief matin 1x/jour · 4) Hub santé (info).
# RÈGLE ABSOLUE : ne touche JAMAIS au moteur (ACE/Hulk/champion/molettes).
set -uo pipefail
SCRIPTS=~/ace777-test-day1/Index_Maison/scripts
LOG=/tmp/autopilote.log
BRIEF_MARKER=/tmp/autopilote_brief_$(date +%Y-%m-%d)
echo "[$(date '+%Y-%m-%d %H:%M:%S')] ===== AUTOPILOTE =====" >> "$LOG"

# 1) PULSE (lecture seule) — met à jour SOUS_L_OEIL
if [ -f "$SCRIPTS/pulse_sous_loeil.sh" ]; then
  bash "$SCRIPTS/pulse_sous_loeil.sh" >>"$LOG" 2>&1 && echo "pulse OK" >>"$LOG" || echo "pulse WARN/NOK (info)" >>"$LOG"
fi

# 2) AUTO-HEAL : job attendu absent de launchctl → bootstrap le plist
for job in com.ace777.prise-ia com.ace777.cockpit-pont com.ace777.cockpit-http com.ace777.mirofish com.ace777.mirofish-front com.ace777.superviseur com.ace777.vigie; do
  if ! launchctl list 2>/dev/null | grep -q "$job"; then
    echo "job absent: $job → bootstrap" >>"$LOG"
    if [ -f "$HOME/Library/LaunchAgents/$job.plist" ]; then
      launchctl bootstrap gui/$(id -u) "$HOME/Library/LaunchAgents/$job.plist" 2>>"$LOG" || true
    fi
  fi
done

# 3) BRIEF MATIN 1x/jour (marqueur date)
if [ ! -f "$BRIEF_MARKER" ] && [ -f "$SCRIPTS/brief_matin.sh" ]; then
  if bash "$SCRIPTS/brief_matin.sh" >>"$LOG" 2>&1; then
    touch "$BRIEF_MARKER"
    echo "brief matin OK" >>"$LOG"
  else
    echo "brief matin ERR (réessai au prochain passage)" >>"$LOG"
  fi
fi

# 4) HUB santé (info)
curl -s --max-time 2 http://127.0.0.1:11435/health >>"$LOG" 2>&1 && echo "" >>"$LOG"

echo "AUTOPILOTE DONE" >>"$LOG"
