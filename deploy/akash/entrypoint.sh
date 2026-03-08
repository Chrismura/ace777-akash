#!/usr/bin/env bash
set -euo pipefail

cd /app

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"

mkdir -p "${HOME}"
cat > "${HOME}/.binance_testnet.env" <<EOF
export BINANCE_API_KEY="${BINANCE_API_KEY}"
export BINANCE_API_SECRET="${BINANCE_API_SECRET}"
EOF
chmod 600 "${HOME}/.binance_testnet.env"

# Optional overrides from Akash environment
export MOMENTUM_THRESHOLD="${MOMENTUM_THRESHOLD:-0.94}"
export WALL_DROP_THRESHOLD="${WALL_DROP_THRESHOLD:-0.033}"
export BUY_USDT_BETA="${BUY_USDT_BETA:-250}"
export BUY_USDT_ALPHA="${BUY_USDT_ALPHA:-250}"
export GLOBAL_STOP_USDT="${GLOBAL_STOP_USDT:--32.00}"
export FLUID_EXIT_SENSITIVITY="${FLUID_EXIT_SENSITIVITY:-1.0}"
export DYNAMIC_HOLD="${DYNAMIC_HOLD:-TRUE}"

LAUNCH_SCRIPT="${LAUNCH_SCRIPT:-./launch_test_master_base_v8_6_fortress.sh}"
RUN_DURATION="${RUN_DURATION:-04:00:00}"

cleanup() {
  touch STOP STOP_ALPHA STOP_BETA STOP_DUO1_ALPHA STOP_DUO1_BETA || true
}

trap cleanup TERM INT

exec bash "$LAUNCH_SCRIPT" --duration "$RUN_DURATION"
