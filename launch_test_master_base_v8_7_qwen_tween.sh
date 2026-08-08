#!/usr/bin/env bash
set -euo pipefail

# === MASTER BASE V8.7 QWEN_TWEEN ===
# Même setup exact que V8.6 (nuit) + Ollama qwen2.5-coder:1.5b
# Prérequis: ollama pull qwen2.5-coder:1.5b

export LLM_GATE_ENABLED="TRUE"
export LLM_MODEL="${LLM_MODEL:-qwen2.5-coder:1.5b}"
export LLM_OLLAMA_URL="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"

# Tag différent pour distinguer les runs
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-MASTER_BASE_V8_7_QWEN_TWEEN_4H}"

echo "=== V8.7 QWEN_TWEEN === LLM gate ON, model=$LLM_MODEL"
exec "$(dirname "$0")/launch_test_master_base_v8_6_fortress.sh" "$@"
