#!/bin/bash
# === MODELE EXACT ARCHIVE (MASTER_BASE) ===
# Date/Heure run de reference:
# Start UTC: 2026-03-09T22:03:24Z
# End UTC:   2026-03-10T02:03:24Z
#
# Source de lancement:
#   LLM_GATE_ENABLED=TRUE ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
#
# Parametres observes dans le run:
# - Tag: MASTER_BASE_V8_5_IMPACT_4H
# - BETA: Leverage=3, BuyUSDT=200
# - ALPHA: Leverage ramp 5->13, BuyUSDT=800
# - V8 Resonance: impulse_thr=0.96, dt_ms=128
# - V8 Tension: wall_drop=6.5%, dt_ms=128, filter=0.85, depth=20

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export LLM_GATE_ENABLED=TRUE
export RUN_DURATION="04:00:00"
export TEST_TAG_OVERRIDE="MASTER_BASE_V8_5_IMPACT_4H"
export MOMENTUM_THRESHOLD="0.96"
export BUY_USDT_BETA="200"
export BUY_USDT_ALPHA="800"

exec ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
