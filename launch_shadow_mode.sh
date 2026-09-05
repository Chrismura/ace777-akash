#!/usr/bin/env bash
# SHADOW MODE SCÉNARIO C — lanceur (zéro ordre, zéro clé, zéro contact champion)
# Usage :  ./launch_shadow_mode.sh              (tourne jusqu'à runs/STOP_SHADOW ou STOP)
#          RUN_SEC=900 ./launch_shadow_mode.sh (auto-stop après 900 s pour essai)
set -uo pipefail
cd "$HOME/ace777-test-day1" || exit 1

RUN_SEC="${RUN_SEC:-0}"
# Porte d'amorçage approuvée Gemini R25 : 90 min d'entrées forcées (journalisées BOOTSTRAP)
# pour que les fills virtuels naissent — les SORTIES restent TOUJOURS gouvernées par H.
SHADOW_BOOTSTRAP_MIN="${SHADOW_BOOTSTRAP_MIN:-90}"
export SHADOW_BOOTSTRAP_MIN
TAG="SHADOW_SC_$(date -u +%Y%m%d)"
PID_FILE="runs/shadow.pid"

# hygiène : pas de double instance
if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE" 2>/dev/null)" 2>/dev/null; then
  echo "SHADOW_ERR: déjà lancé (pid $(cat "$PID_FILE")) — arrêt : touch runs/STOP_SHADOW"
  exit 1
fi
rm -f runs/STOP_SHADOW

mkdir -p runs
nohup python3 shadow_mode_sc.py > "runs/${TAG}_LAUNCH.log" 2>&1 &
echo $! > "$PID_FILE"
echo "SHADOW_ON: pid=$(cat "$PID_FILE") tag=${TAG} bootstrap=${SHADOW_BOOTSTRAP_MIN}min"
echo "  fills  : runs/${TAG}_FILLS.csv"
echo "  ticks  : runs/${TAG}_TICKS.csv"
echo "  stop   : touch runs/STOP_SHADOW   (ou ./stop_shadow_mode.sh)"
echo "  essai  : RUN_SEC=900 ./launch_shadow_mode.sh"

if [ "$RUN_SEC" -gt 0 ] 2>/dev/null; then
  (
    sleep "$RUN_SEC"
    touch runs/STOP_SHADOW
  ) &
  disown
  echo "  auto-stop programmé dans ${RUN_SEC}s"
fi
