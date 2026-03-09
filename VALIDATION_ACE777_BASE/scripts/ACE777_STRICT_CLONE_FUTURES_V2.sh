#!/usr/bin/env bash
set -euo pipefail

# V2 wrapper:
# - reinforces neutral-zone breathing before soft anomaly can cut
# - wider trailing giveback (less nervous)
# - keeps strict clone core and Futures pipes

cd /app
BASE_DIR="/app/VALIDATION_ACE777_BASE/scripts"

export TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-3}"
export SOFT_TRAIL_GIVEBACK_BPS="${SOFT_TRAIL_GIVEBACK_BPS:-3}"
export MIN_HOLD_FOR_ANOMALY="${MIN_HOLD_FOR_ANOMALY:-3}"
export SOFT_NEUTRAL_HOLD_SEC="${SOFT_NEUTRAL_HOLD_SEC:-60}"
export NEUTRAL_PNL_MIN_BPS="${NEUTRAL_PNL_MIN_BPS:--1}"
export NEUTRAL_PNL_MAX_BPS="${NEUTRAL_PNL_MAX_BPS:-5}"
export LEVERAGE_ANOMALY_MULT="${LEVERAGE_ANOMALY_MULT:-0.5}"

# Prefix every live output line with UTC timestamp for monitoring.
bash "$BASE_DIR/ACE777_STRICT_CLONE_FUTURES.sh" 2>&1 | while IFS= read -r line; do
  printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$line"
done
