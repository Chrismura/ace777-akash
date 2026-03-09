#!/usr/bin/env bash
set -euo pipefail

# MASTER reference:
# - Low liquidite
# - Objectif: gains en range (marche lateral)
# - Notional reduit: BUY_USDT=250

cd /app
rm -f STOP

(ruby -e 'sleep 14400; File.write("STOP","")' &)

caffeinate -is bash -c '
LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/ACE777_ESCALIER_4H.csv" \
ENABLE_ORDERS=TRUE \
CYCLES=999999 \
LEVERAGE=5 \
BUY_USDT=250 \
MOMENTUM_THRESHOLD=0.60 \
POLL_SEC=0.10 \
TREND_FILTER=FALSE \
RADAR_GATE=TRUE \
ANOMALY_SOFT_MODE=TRUE \
SOFT_NEUTRAL_HOLD_SEC=40 \
MIN_HOLD_FOR_ANOMALY=3 \
MIN_PROFIT_BPS=10 \
STOP_LOSS_BPS=5 \
TRAIL_GIVEBACK_BPS=2 \
bash ./VALIDATION_ACE777_BASE/scripts/ACE777_STRICT_CLONE_FUTURES_V2.sh
'
