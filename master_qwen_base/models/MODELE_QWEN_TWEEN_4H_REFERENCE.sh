#!/bin/bash
# === MODELE QWEN REFERENCE (MASTER_QWEN_BASE) ===
# Reference observed in runs:
# Tag: MASTER_BASE_V8_7_QWEN_TWEEN_4H
# Start UTC (observed): 2026-03-10T11:51:35Z
# End UTC: A_VERIFIER
#
# Cycle description:
# BETA x5 | ALPHA x13 | Masse 1.618->3.236 (alarm) | Trigger=-3bps/-0.80 | GlobalStop=-45.00 HALT | Lagrange+PhaseShift=ON
#
# LLM/Qwen setup:
# - LLM_GATE_ENABLED=TRUE
# - LLM_MODEL=qwen2.5-coder:1.5b
# - LLM_OLLAMA_URL=http://127.0.0.1:11434

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

export LLM_GATE_ENABLED="TRUE"
export LLM_MODEL="${LLM_MODEL:-qwen2.5-coder:1.5b}"
export LLM_OLLAMA_URL="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-MASTER_BASE_V8_7_QWEN_TWEEN_4H}"

exec ./launch_test_master_base_v8_7_qwen_tween.sh --duration 04:00:00
