#!/usr/bin/env bash
set -euo pipefail

cd /app

# Profil 7h30:
# - ALPHA direct (sans attente duo)
# - levier ALPHA lisse de x5 vers x13
# - paramètres repris depuis les variables shell utilisateur

export RUN_SEC_OVERRIDE=27000
export GLOBAL_STOP_USDT="${GLOBAL_STOP_USDT:--32.00}"
export BETA_MOMENTUM_THRESHOLD="${MOMENTUM_THRESHOLD:-0.85}"
export ALPHA_REVENGE_MULT="${ALPHA_REVENGE_MULT:-1.618}"
export BETA_STOP_LOSS_BPS="${STOP_LOSS_BPS:-16}"
export ALPHA_STOP_LOSS_BPS="${STOP_LOSS_BPS:-16}"

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
