#!/usr/bin/env bash
# Watchdog ACE777 — stop propre si API Binance injoignable trop longtemps
# Usage: lancé en arrière-plan par launch_test_master_base_v8_5_impact.sh
# Exit: touche STOP_ALPHA + STOP_BETA après WATCHDOG_FAIL_SEC (défaut 120s cumulés)

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

INTERVAL_SEC="${WATCHDOG_INTERVAL_SEC:-30}"
FAIL_THRESHOLD="${WATCHDOG_FAIL_SEC:-120}"
PING_URL="${WATCHDOG_PING_URL:-https://testnet.binancefuture.com/fapi/v1/ping}"
# Preflight health check — le moteur live garde 0.2–0.3s
PING_CONNECT="${WATCHDOG_CONNECT_TIMEOUT:-1}"
PING_MAX="${WATCHDOG_MAX_TIME:-2}"

fail_accum=0
tag="${TEST_TAG_OVERRIDE:-unknown}"

log() { echo "WATCHDOG: $1" >&2; }

ping_ok() {
  local resp
  resp="$(curl -sS --connect-timeout "$PING_CONNECT" --max-time "$PING_MAX" "$PING_URL" 2>/dev/null || true)"
  [ "$resp" = "{}" ]
}

while true; do
  mp=""
  [ -f runs/master.pid ] && mp="$(cat runs/master.pid 2>/dev/null || true)"
  if [ -z "$mp" ] || ! kill -0 "$mp" 2>/dev/null; then
    log "master.pid absent — watchdog stop"
    exit 0
  fi

  if ping_ok; then
    [ "$fail_accum" -gt 0 ] && log "réseau OK (reset après ${fail_accum}s down)"
    fail_accum=0
  else
    fail_accum=$((fail_accum + INTERVAL_SEC))
    log "Binance unreachable — down cumulé ${fail_accum}s / ${FAIL_THRESHOLD}s (tag=${tag})"
    if [ "$fail_accum" -ge "$FAIL_THRESHOLD" ]; then
      touch STOP_ALPHA STOP_BETA 2>/dev/null || true
      log "STOP déclenché — réseau down >= ${FAIL_THRESHOLD}s"
      exit 1
    fi
  fi
  sleep "$INTERVAL_SEC"
done
