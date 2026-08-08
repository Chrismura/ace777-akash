#!/bin/bash
# === MASTER BASE MODEL ===
# Reference cycle:
# Start UTC: 2026-03-09T22:03:24Z
# End UTC:   2026-03-10T02:03:24Z
# Tag: MASTER_BASE_V8_5_IMPACT_4H
#
# Cycle description kept for traceability:
# BETA x5 | ALPHA x13 | Masse 1.618->3.236 (alarm) | Trigger=-3bps/-0.80 | GlobalStop=-45.00 HALT | Lagrange+PhaseShift=ON
#
# Runtime profile seen in cycle:
# - BETA: Leverage=3, BuyUSDT=200
# - ALPHA: Leverage ramp 5->13, BuyUSDT=800
# - V8 Resonance: impulse_thr=0.96, dt_ms=128
# - V8 Tension: wall_drop=6.5%, dt_ms=128, filter=0.85, depth=20
#
# PNL:
# - PNL_TOTAL_USDT: A_VERIFIER

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

export LLM_GATE_ENABLED=TRUE
export RUN_DURATION="04:00:00"
export TEST_TAG_OVERRIDE="MASTER_BASE_V8_5_IMPACT_4H"
export MOMENTUM_THRESHOLD="0.96"
export BUY_USDT_BETA="200"
export BUY_USDT_ALPHA="800"

exec ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
