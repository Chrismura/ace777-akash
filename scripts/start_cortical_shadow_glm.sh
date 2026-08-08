#!/usr/bin/env bash
# Lance le superviseur cortical GLM-5.2 en mode SHADOW (Phase C)
# N'écrit QUE runs/vortex_control.json.shadow — le live Qwen reste maître.
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vortex_v2_collab 2>/dev/null || source ./scripts/load_config.sh 2>/dev/null || true
# shellcheck source=config_profiles/cortical_shadow_glm.env
[ -f config_profiles/cortical_shadow_glm.env ] && source config_profiles/cortical_shadow_glm.env

export LOG_BETA="${LOG_BETA:-$(ls -t runs/*_BETA*.csv 2>/dev/null | head -1)}"
export LOG_ALPHA="${LOG_ALPHA:-$(ls -t runs/*_ALPHA*.csv 2>/dev/null | head -1)}"
INTERVAL_SEC="${CORTICAL_INTERVAL_SEC:-20}"
case "$INTERVAL_SEC" in
  ''|*[!0-9]*) INTERVAL_SEC=20 ;;
esac
[ "$INTERVAL_SEC" -lt 15 ] && INTERVAL_SEC=15
[ "$INTERVAL_SEC" -gt 30 ] && INTERVAL_SEC=30

SHADOW_FILE="${CORTICAL_SHADOW_FILE:-runs/vortex_control.json.shadow}"
PID_FILE="runs/cortical_shadow_glm.pid"
LOG_FILE="runs/cortical_shadow_glm.log"

if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Cortical shadow GLM déjà actif (pid $(cat "$PID_FILE"))"
  exit 0
fi

if [ -z "${OPENROUTER_API_KEY:-}" ] && [ -z "${ZAI_API_KEY:-}" ]; then
  echo "ERREUR: définir OPENROUTER_API_KEY ou ZAI_API_KEY avant de lancer le shadow."
  echo "  export OPENROUTER_API_KEY=sk-or-..."
  echo "  # ou: export GLM_PROVIDER=zai ZAI_API_KEY=..."
  exit 1
fi

mkdir -p runs
echo "=== CORTICAL SHADOW GLM === interval=${INTERVAL_SEC}s provider=${GLM_PROVIDER:-openrouter} model=${GLM_MODEL:-z-ai/glm-5.2}"
echo "    shadow=${SHADOW_FILE} live_ref=${VORTEX_CONTROL_FILE:-runs/vortex_control.json}"

nohup env \
  LOG_BETA="$LOG_BETA" \
  LOG_ALPHA="$LOG_ALPHA" \
  INTERVAL_SEC="$INTERVAL_SEC" \
  bash -c '
  cd "'"$_root"'"
  while true; do
    if [ -f "${LOG_BETA:-}" ]; then
      ruby ./scripts/cortical_supervisor_glm.rb "$LOG_BETA" 2>/dev/null | \
        ruby -rjson -e '"'"'j=JSON.parse(STDIN.read); st=j["shadow_status"]||"?"; ph=j["market_phase"]||"?"; t=(j["llm_elapsed_sec"]||"?"); puts "[#{Time.now.strftime("%H:%M:%S")}] SHADOW mode=#{j["mode"]} phase=#{ph} cohesion=#{j["swarm_cohesion"]} glm=#{t}s #{st} #{j["justification"]}"'"'"' 2>/dev/null || \
        echo "[$(date +%H:%M:%S)] shadow glm fail"
    else
      echo "[$(date +%H:%M:%S)] attente log BETA..."
    fi
    sleep "$INTERVAL_SEC"
  done
' >> "$LOG_FILE" 2>&1 &

echo $! > "$PID_FILE"
echo "Cortical shadow GLM pid=$(cat "$PID_FILE") → ${SHADOW_FILE}"
echo "Log: ${LOG_FILE}"
