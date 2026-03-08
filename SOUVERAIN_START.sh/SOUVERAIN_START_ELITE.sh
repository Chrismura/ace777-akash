#!/usr/bin/env bash
set -euo pipefail

# --- PROTOCOLE PARALLELE ACE777 SOUVERAIN (ELITE) ---
# Fusion:
# - orchestration PID-safe + trap propre
# - hedge explicite LONG/SHORT via FORCE_ENTRY_SIDE + POSITION_SIDE
# - parametres explicites (levier/masse/seuils)

cd /Users/christophe/ace777-test-day1

RUN_DIR="runs/ACE777_SYNCHRO_REEL_7H"
mkdir -p "$RUN_DIR"
rm -f STOP_ALPHA STOP_BETA "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid

# Durée mission (9h par défaut)
DURATION_SEC="${DURATION_SEC:-32400}"
AUTO_STOP_ENABLED="${AUTO_STOP_ENABLED:-FALSE}"

# Paramètres communs
LEVERAGE="${LEVERAGE:-5}"
BUY_USDT="${BUY_USDT:-250}"
ENABLE_ORDERS="${ENABLE_ORDERS:-TRUE}"
SLEEP_SEC="${SLEEP_SEC:-1}"
POLL_SEC="${POLL_SEC:-0.5}"

echo "🚀 Déploiement Binôme Souverain ELITE (${DURATION_SEC}s)..."

cleanup() {
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  kill "${PID_ALPHA:-}" "${PID_BETA:-}" "${PID_TIMER_ALPHA:-}" "${PID_TIMER_BETA:-}" 2>/dev/null || true
  echo "🛑 Arrêt propre exécuté."
}

trap cleanup SIGINT SIGTERM

# --- ALPHA (Sniper LONG) ---
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
echo "🎯 ALPHA [PID:${PID_ALPHA}] déployée (LONG / seuil 0.60 / SL 5)"

# --- BETA (Lourd SHORT) ---
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
echo "🐘 BETA [PID:${PID_BETA}] déployée (SHORT / seuil 0.35 / SL 15)"

echo "🛡️ Surveillance active. CTRL+C => arrêt propre des 2 unités."
echo "📁 Logs: ${RUN_DIR}/ALPHA_SNIPER.csv | ${RUN_DIR}/BETA_LOURD.csv"

wait "$PID_ALPHA" "$PID_BETA"
echo "🏆 Mission terminée. Rapports disponibles."
