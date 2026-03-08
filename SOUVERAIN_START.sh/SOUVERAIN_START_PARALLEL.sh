#!/usr/bin/env bash
set -euo pipefail

# --- PROTOCOLE PARALLELE ACE777 SOUVERAIN (PID-safe + hedge-ready) ---

cd /Users/christophe/ace777-test-day1

RUN_DIR="runs/ACE777_SYNCHRO_REEL_7H"
mkdir -p "$RUN_DIR"
rm -f STOP_ALPHA STOP_BETA "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid

AUTO_STOP_ENABLED="${AUTO_STOP_ENABLED:-FALSE}"
DURATION_SEC="${DURATION_SEC:-32400}"

echo "🚀 Lancement Binome Souverain (${DURATION_SEC}s)"

# Timer 9h pour ALPHA
if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  (ruby -e "sleep ${DURATION_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
fi

# ALPHA: Sniper (LONG bias) - sizing prudent
caffeinate -is bash -c '
  LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/ALPHA_SNIPER.csv" \
  STOP_FILE="STOP_ALPHA" \
  ENABLE_ORDERS=TRUE \
  LEVERAGE=5 \
  BUY_USDT=250 \
  MOMENTUM_THRESHOLD=0.60 \
  STOP_LOSS_BPS=5 \
  TREND_FILTER=FALSE \
  RADAR_GATE=TRUE \
  ANOMALY_SOFT_MODE=TRUE \
  FORCE_ENTRY_SIDE=BUY \
  POSITION_SIDE=LONG \
  bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &
alpha_pid=$!
echo "$alpha_pid" > "$RUN_DIR/alpha.pid"
echo "🎯 ALPHA deployee (PID=$alpha_pid)"

# Timer 9h pour BETA
if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  (ruby -e "sleep ${DURATION_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1
fi

# BETA: Lourd (SHORT bias) - souffle plus large
caffeinate -is bash -c '
  LOG_FILE="runs/ACE777_SYNCHRO_REEL_7H/BETA_LOURD.csv" \
  STOP_FILE="STOP_BETA" \
  ENABLE_ORDERS=TRUE \
  LEVERAGE=5 \
  BUY_USDT=250 \
  MOMENTUM_THRESHOLD=0.35 \
  STOP_LOSS_BPS=15 \
  TREND_FILTER=FALSE \
  RADAR_GATE=TRUE \
  ANOMALY_SOFT_MODE=TRUE \
  FORCE_ENTRY_SIDE=SELL \
  POSITION_SIDE=SHORT \
  bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &
beta_pid=$!
echo "$beta_pid" > "$RUN_DIR/beta.pid"
echo "🐘 BETA deployee (PID=$beta_pid)"

echo "📁 Logs: $RUN_DIR/ALPHA_SNIPER.csv et $RUN_DIR/BETA_LOURD.csv"
echo "🛑 Arret propre: touch STOP_ALPHA && touch STOP_BETA"

wait "$alpha_pid" "$beta_pid"
echo "🏁 Mission terminee."
