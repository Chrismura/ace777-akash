#!/usr/bin/env bash
# SUPERVISEUR L2 PASSIF — lanceur v2 (zéro ordre, zéro clé, zéro contact shadow/champion)
# Simple et robuste : lance le python en arrière-plan, vérifie qu'il écrit, c'est tout.
# Usage :  ./launch_l2_superviseur.sh              (tourne jusqu'à STOP : touch runs/STOP_L2)
set -u
cd "$HOME/ace777-test-day1" || exit 1

DAY="$(date -u +%Y%m%d)"
LOG="runs/L2_${DAY}_LAUNCH.log"

# arrêt demandé ? (touch runs/STOP_L2 est géré par le python lui-même)

nohup python3 Index_Maison/scripts/superviseur_l2.py >> "$LOG" 2>&1 &
sleep 3

if ps aux | grep -q "[s]uperviseur_l2"; then
  PID=$(ps aux | grep "[s]uperviseur_l2" | grep -v grep | awk '{print $2}' | head -1)
  echo "$PID" > runs/l2.pid
  echo "L2_ON: pid=$PID day=$DAY"
  echo "  snaps : runs/L2_${DAY}_SNAPS.csv"
  echo "  murs  : runs/L2_${DAY}_MURS.csv"
  echo "  stop  : touch runs/STOP_L2"
  echo "  log   : $LOG"
else
  echo "L2_ERREUR — voir $LOG"
  tail -5 "$LOG"
  exit 1
fi
