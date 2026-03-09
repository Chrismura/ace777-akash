#!/usr/bin/env bash
set -euo pipefail

cd /app

# Variante "demain":
# - ALPHA entre en direct (sans attente duo)
# - exposition lissee via rampe de levier jusqu'a x13
# - script principal conserve, cette variante est a part

export ALPHA_DUO_MODE=FALSE
export ALPHA_FORCE_ENTRY_SIDE=SELL
export ALPHA_RADAR_GATE=FALSE
export ALPHA_TREND_FILTER=FALSE
export ALPHA_MOMENTUM_THRESHOLD=0.01
export ALPHA_LEVERAGE_TARGET=13
export ALPHA_LEVERAGE_RAMP_ENABLED=TRUE
export ALPHA_LEVERAGE_RAMP_START=5
export ALPHA_LEVERAGE_RAMP_END=13
export ALPHA_LEVERAGE_RAMP_CYCLES=180

exec ./launch_test_duo_harmonic_5_8_13_6h.sh
