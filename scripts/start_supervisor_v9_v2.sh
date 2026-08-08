#!/usr/bin/env bash
# Superviseur Vortex v2 — chop_score_v2 + JSON radar (collab Gemini/Cursor)
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vortex_v2_collab 2>/dev/null || source ./scripts/load_config.sh 2>/dev/null || true

export VORTEX_CONTROL_ENABLED=TRUE
export VORTEX_V2_RADAR_PILOT=TRUE
export CONTROL_FILE="${VORTEX_CONTROL_FILE:-runs/vortex_control.json}"
export LOG_BETA="${LOG_BETA:-$(ls -t runs/*_BETA*.csv 2>/dev/null | head -1)}"
INTERVAL_SEC="${SUPERVISOR_INTERVAL_SEC:-18}"
case "$INTERVAL_SEC" in
  ''|*[!0-9]*) INTERVAL_SEC=18 ;;
esac
[ "$INTERVAL_SEC" -lt 15 ] && INTERVAL_SEC=15
[ "$INTERVAL_SEC" -gt 20 ] && INTERVAL_SEC=20

mkdir -p runs
PID_FILE="runs/supervisor_v9_v2.pid"

_force="${FORCE_SUPERVISOR_RESTART:-0}"
[ "${1:-}" = "--force" ] && _force=1

if [ "$_force" = "1" ]; then
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
elif [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Supervisor Vortex v2 déjà actif (pid $(cat "$PID_FILE")) log=${LOG_BETA:-?}"
  exit 0
fi

echo "=== SUPERVISEUR VORTEX V2 === interval=${INTERVAL_SEC}s log=${LOG_BETA}"

nohup env \
  LOG_BETA="$LOG_BETA" \
  INTERVAL_SEC="$INTERVAL_SEC" \
  SWARM_LLM_MACRO_ONLY="${SWARM_LLM_MACRO_ONLY:-TRUE}" \
  VORTEX_LLM_MAX_PREDICT="${VORTEX_LLM_MAX_PREDICT:-45}" \
  VORTEX_LLM_BUDGET_SEC="${VORTEX_LLM_BUDGET_SEC:-1.2}" \
  SUPERVISOR_TAIL_LINES="${SUPERVISOR_TAIL_LINES:-15}" \
  OLLAMA_NUM_THREAD="${OLLAMA_NUM_THREAD:-4}" \
  bash -c '
  cd "'"$_root"'"
  while true; do
    if [ -f "${LOG_BETA:-}" ]; then
      ruby ./scripts/vortex_supervisor_v2_llm.rb "$LOG_BETA" 2>/dev/null | \
        ruby -rjson -e '"'"'j=JSON.parse(STDIN.read); em=j["emergency_override"] ? " EMRG" : " LLM"; t=(j["llm_elapsed_sec"]||"?"); puts "[#{Time.now.strftime("%H:%M:%S")}] mode=#{j["mode"]} chop=#{j["chop_score"]} cohesion=#{j["swarm_cohesion"]} llm=#{t}s#{em} #{j["justification"]}"'"'"' 2>/dev/null || \
        echo "[$(date +%H:%M:%S)] regime compute fail"
    else
      echo "[$(date +%H:%M:%S)] attente log BETA..."
    fi
    sleep "$INTERVAL_SEC"
  done
' >> runs/supervisor_v9_v2.log 2>&1 &

echo $! > "$PID_FILE"
echo "Supervisor Vortex v2 pid=$(cat "$PID_FILE") → ${CONTROL_FILE}"
