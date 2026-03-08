#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# ⚡ ACE777 SOUVERAIN ELITE STYLE ⚡
# Binôme parallèle hedge-ready (LONG/SHORT) avec rigueur PID-safe
# ============================================================

cd /Users/christophe/ace777-test-day1

# 1) Préparation souveraine
RUN_DIR="runs/ACE777_SYNCHRO_REEL_7H"
mkdir -p "$RUN_DIR"
rm -f STOP_ALPHA STOP_BETA "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid

# Paramétrage global (modifiable au lancement)
DURATION_SEC="${DURATION_SEC:-32400}"   # 9h
AUTO_STOP_ENABLED="${AUTO_STOP_ENABLED:-FALSE}"
LEVERAGE="${LEVERAGE:-5}"
BUY_USDT="${BUY_USDT:-250}"
ENABLE_ORDERS="${ENABLE_ORDERS:-TRUE}"
SLEEP_SEC="${SLEEP_SEC:-1}"
POLL_SEC="${POLL_SEC:-0.5}"

echo "⚡ DÉPLOIEMENT UNITÉ ÉLITE ACE777 (${DURATION_SEC}s) ⚡"

cleanup() {
  # Arrêt propre prioritaire
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  kill "${PID_ALPHA:-}" "${PID_BETA:-}" "${PID_TIMER_ALPHA:-}" "${PID_TIMER_BETA:-}" 2>/dev/null || true
  echo "🛑 ARRÊT GLOBAL SÉCURISÉ."
}
trap cleanup SIGINT SIGTERM

# 2) UNITÉ ALPHA — Sniper LONG (précision)
if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  ruby -e "sleep ${DURATION_SEC}; File.write('STOP_ALPHA','')" &
  PID_TIMER_ALPHA=$!
fi

caffeinate -is bash -c "
  LOG_FILE='${RUN_DIR}/ALPHA_SNIPER.csv' \
  STOP_FILE='STOP_ALPHA' \
  ENABLE_ORDERS='${ENABLE_ORDERS}' \
  LEVERAGE='${LEVERAGE}' \
  BUY_USDT='${BUY_USDT}' \
  MOMENTUM_THRESHOLD='0.60' \
  STOP_LOSS_BPS='5' \
  TREND_FILTER='FALSE' \
  RADAR_GATE='TRUE' \
  ANOMALY_SOFT_MODE='TRUE' \
  FORCE_ENTRY_SIDE='BUY' \
  POSITION_SIDE='LONG' \
  SLEEP_SEC='${SLEEP_SEC}' \
  POLL_SEC='${POLL_SEC}' \
  bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
" &
PID_ALPHA=$!
echo "$PID_ALPHA" > "${RUN_DIR}/alpha.pid"
echo "🎯 ALPHA [PID:${PID_ALPHA}] -> LONG (viseur 0.60 / SL 5)"

# 3) UNITÉ BÊTA — Lourd SHORT (couverture)
if [ "$AUTO_STOP_ENABLED" = "TRUE" ]; then
  ruby -e "sleep ${DURATION_SEC}; File.write('STOP_BETA','')" &
  PID_TIMER_BETA=$!
fi

caffeinate -is bash -c "
  LOG_FILE='${RUN_DIR}/BETA_LOURD.csv' \
  STOP_FILE='STOP_BETA' \
  ENABLE_ORDERS='${ENABLE_ORDERS}' \
  LEVERAGE='${LEVERAGE}' \
  BUY_USDT='${BUY_USDT}' \
  MOMENTUM_THRESHOLD='0.35' \
  STOP_LOSS_BPS='15' \
  TREND_FILTER='FALSE' \
  RADAR_GATE='TRUE' \
  ANOMALY_SOFT_MODE='TRUE' \
  FORCE_ENTRY_SIDE='SELL' \
  POSITION_SIDE='SHORT' \
  SLEEP_SEC='${SLEEP_SEC}' \
  POLL_SEC='${POLL_SEC}' \
  bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
" &
PID_BETA=$!
echo "$PID_BETA" > "${RUN_DIR}/beta.pid"
echo "🐘 BÊTA [PID:${PID_BETA}] -> SHORT (souffle 0.35 / SL 15)"

echo "🛡️ BINÔME EN GARDE."
echo "📁 Logs: ${RUN_DIR}/ALPHA_SNIPER.csv | ${RUN_DIR}/BETA_LOURD.csv"
echo "🧭 Arrêt manuel propre: touch STOP_ALPHA && touch STOP_BETA"

wait "$PID_ALPHA" "$PID_BETA"
echo "🏆 MISSION ACCOMPLIE. RAPPORTS DISPONIBLES."
