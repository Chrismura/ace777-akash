#!/usr/bin/env bash
# Démarre le superviseur V9 (régime TREND/CHOP) en arrière-plan
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh 2>/dev/null || true

export VORTEX_CONTROL_ENABLED=TRUE
export SUPERVISOR_MODEL="${SUPERVISOR_MODEL:-${LLM_MODEL:-qwen2.5-coder:1.5b}}"

# Auto-détecte le dernier log BETA
latest_beta="$(ls -t runs/*_BETA_X5.csv 2>/dev/null | head -1 || true)"
export LOG_BETA="${LOG_BETA:-${latest_beta:-runs/MASTER_BASE_V8_5_IMPACT_4H_BETA_X5.csv}}"

mkdir -p runs
if [ -f runs/supervisor_v9.pid ] && kill -0 "$(cat runs/supervisor_v9.pid)" 2>/dev/null; then
  echo "Supervisor V9 déjà actif (pid $(cat runs/supervisor_v9.pid))"
  exit 0
fi

nohup ./tendance/supervisor_v9.sh >> runs/supervisor_v9.log 2>&1 &
echo $! > runs/supervisor_v9.pid
echo "Supervisor V9 démarré pid=$(cat runs/supervisor_v9.pid) model=${SUPERVISOR_MODEL} log=${LOG_BETA}"
