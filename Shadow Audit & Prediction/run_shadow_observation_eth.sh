#!/bin/bash
set -euo pipefail

# Shadow Audit & Prediction launcher
# Mode: observation only (no orders)

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export SYMBOL="${SYMBOL:-ETHUSDT}"
export RADAR_THRESHOLD="${RADAR_THRESHOLD:-0.75}"
export MOMENTUM_THRESHOLD="${MOMENTUM_THRESHOLD:-0.92}"
export BETA_DT_MS="${BETA_DT_MS:-500}"
export ALPHA_DT_MS="${ALPHA_DT_MS:-32}"
export MASS_ANCHOR="${MASS_ANCHOR:-1.618}"
export LLM_GATE_ENABLED="${LLM_GATE_ENABLED:-TRUE}"
# Queen 1.5B only (hard lock)
export LLM_MODEL="qwen2.5-coder:1.5b"
export LLM_OLLAMA_URL="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"
export MICRO_VETO_MIN_TENSION="${MICRO_VETO_MIN_TENSION:-1.0}"
export OUTPUT_CSV="${OUTPUT_CSV:-runs/SHADOW_AUDIT_PREDICTION_ETH.csv}"
export SKIP_LOG_ENABLED="${SKIP_LOG_ENABLED:-TRUE}"
export SKIP_LOG_CSV="${SKIP_LOG_CSV:-${OUTPUT_CSV%.csv}_skips.csv}"

echo "=== SHADOW AUDIT & PREDICTION (ETH) ==="
echo "Mode: OBSERVATION_ONLY (ORDERS=FALSE)"
echo "Architecture: BETA=${BETA_DT_MS}ms | ALPHA=${ALPHA_DT_MS}ms | ORCHESTRATEUR=Qwen1.5B"
echo "Constants: radar=${RADAR_THRESHOLD} mom=${MOMENTUM_THRESHOLD} mass=${MASS_ANCHOR}"
echo "LLM: ${LLM_MODEL} @ ${LLM_OLLAMA_URL}"
echo "Micro-veto: ON only if tension > ${MICRO_VETO_MIN_TENSION}"
echo "Output: ${OUTPUT_CSV}"
echo "Skip log: ${SKIP_LOG_ENABLED} -> ${SKIP_LOG_CSV}"

exec python3 "./Shadow Audit & Prediction/shadow_observation_suture_eth.py"
