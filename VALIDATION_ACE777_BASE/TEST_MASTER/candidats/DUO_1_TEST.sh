#!/usr/bin/env bash
set -euo pipefail

# DUO_1_TEST
# Test hedge en mode validation (avant promotion MASTER).
# Chaque ligne live est horodatee via:
#   VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh

ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"

RUN_DIR="runs/ACE777_SYNCHRO_REEL_7H"
mkdir -p "$RUN_DIR"

DURATION_SEC="${DURATION_SEC:-14400}"  # 4h
AUTO_STOP_ENABLED="${AUTO_STOP_ENABLED:-FALSE}"
LEVERAGE="${LEVERAGE:-5}"
BUY_USDT="${BUY_USDT:-250}"
ENABLE_ORDERS="${ENABLE_ORDERS:-TRUE}"

STOP_ALPHA="STOP_DUO1_ALPHA"
STOP_BETA="STOP_DUO1_BETA"
LOG_ALPHA="${RUN_DIR}/DUO1_ALPHA_TEST.csv"
LOG_BETA="${RUN_DIR}/DUO1_BETA_TEST.csv"

log() {
  printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"
}

cleanup() {
  touch "$STOP_ALPHA" "$STOP_BETA" 2>/dev/null || true
  kill "${PID_ALPHA:-}" "${PID_BETA:-}" "${PID_TIMER_ALPHA:-}" "${PID_TIMER_BETA:-}" 2>/dev/null || true
  log "DUO_1_TEST stop propre."
}
trap cleanup SIGINT SIGTERM EXIT

rm -f "$STOP_ALPHA" "$STOP_BETA"

log "DUO_1_TEST start | duration=${DURATION_SEC}s | leverage=${LEVERAGE} | buy_usdt=${BUY_USDT}"

if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  ruby -e "sleep ${DURATION_SEC}; File.write('${STOP_ALPHA}','')" &
  PID_TIMER_ALPHA=$!
  ruby -e "sleep ${DURATION_SEC}; File.write('${STOP_BETA}','')" &
  PID_TIMER_BETA=$!
fi

caffeinate -is bash -c "\
  LOG_FILE='${LOG_ALPHA}' \
  STOP_FILE='${STOP_ALPHA}' \
  ENABLE_ORDERS='${ENABLE_ORDERS}' \
  LEVERAGE='${LEVERAGE}' \
  BUY_USDT='${BUY_USDT}' \
  MOMENTUM_THRESHOLD='0.60' \
  POLL_SEC='0.10' \
  STOP_LOSS_BPS='5' \
  TREND_FILTER='FALSE' \
  RADAR_GATE='TRUE' \
  ANOMALY_SOFT_MODE='TRUE' \
  SOFT_NEUTRAL_HOLD_SEC='40' \
  MIN_HOLD_FOR_ANOMALY='3' \
  MIN_PROFIT_BPS='10' \
  TRAIL_GIVEBACK_BPS='2' \
  bash ./VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh\
" &
PID_ALPHA=$!

caffeinate -is bash -c "\
  LOG_FILE='${LOG_BETA}' \
  STOP_FILE='${STOP_BETA}' \
  ENABLE_ORDERS='${ENABLE_ORDERS}' \
  LEVERAGE='${LEVERAGE}' \
  BUY_USDT='${BUY_USDT}' \
  MOMENTUM_THRESHOLD='0.35' \
  POLL_SEC='0.05' \
  STOP_LOSS_BPS='15' \
  TREND_FILTER='FALSE' \
  RADAR_GATE='TRUE' \
  ANOMALY_SOFT_MODE='TRUE' \
  SOFT_NEUTRAL_HOLD_SEC='40' \
  MIN_HOLD_FOR_ANOMALY='3' \
  MIN_PROFIT_BPS='10' \
  TRAIL_GIVEBACK_BPS='2' \
  bash ./VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh\
" &
PID_BETA=$!

log "DUO_1_TEST running | alpha_pid=${PID_ALPHA} beta_pid=${PID_BETA}"
log "Logs: ${LOG_ALPHA} | ${LOG_BETA}"

wait "$PID_ALPHA" "$PID_BETA"
trap - SIGINT SIGTERM EXIT
cleanup
log "DUO_1_TEST termine."
