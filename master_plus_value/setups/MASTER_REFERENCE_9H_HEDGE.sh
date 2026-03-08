#!/usr/bin/env bash
set -euo pipefail

# MASTER reference run (HEDGE 9H)
# Uses BASE wrapper (UTC timestamped output):
#   /Users/christophe/ace777-test-day1/VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh

cd /Users/christophe/ace777-test-day1

mkdir -p runs/ACE777_SYNCHRO_REEL_7H/
killall ruby 2>/dev/null || true
rm -f STOP_ALPHA STOP_BETA

# Auto-stop timer is OFF by default to avoid missing spike windows.
AUTO_STOP_ENABLED="${AUTO_STOP_ENABLED:-FALSE}"
DURATION_SEC="${DURATION_SEC:-32400}"

if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  (ruby -e "sleep ${DURATION_SEC}; File.write('STOP_ALPHA','')" &)
  (ruby -e "sleep ${DURATION_SEC}; File.write('STOP_BETA','')" &)
fi

caffeinate -is bash -c '
LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/ALPHA_SNIPER_9H.csv" \
STOP_FILE="STOP_ALPHA" \
ENABLE_ORDERS=TRUE \
MOMENTUM_THRESHOLD=0.60 \
POLL_SEC=0.10 \
STOP_LOSS_BPS=5 \
LEVERAGE=5 \
BUY_USDT=250 \
bash ./VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

caffeinate -is bash -c '
LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/BETA_LOURD_RAPIDE_9H.csv" \
STOP_FILE="STOP_BETA" \
ENABLE_ORDERS=TRUE \
MOMENTUM_THRESHOLD=0.35 \
POLL_SEC=0.05 \
STOP_LOSS_BPS=15 \
LEVERAGE=5 \
BUY_USDT=250 \
bash ./VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh
'
