#!/usr/bin/env bash
# === COPIE EXACTE 4H FORTRESS ===
# Setup identique au run 2026-03-10 : V8.6 FORTRESS, BETA=200, ALPHA=800, 4h

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export LLM_GATE_ENABLED="TRUE"
export LLM_MODEL="qwen2.5-coder:1.5b"
# Masse par défaut fortress: BETA=200, ALPHA=800
# STOP_LOSS_BPS=16, MOMENTUM_THRESHOLD=0.96, GLOBAL_STOP=-45

echo "=== COPIE EXACTE 4H FORTRESS ==="
echo "BETA=200 ALPHA=800 | LLM gate ON | Durée 4h"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
