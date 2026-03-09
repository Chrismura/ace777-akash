#!/usr/bin/env bash
set -euo pipefail

cd /app

# MODELE 14 - VERSION ORIGINALE (30 minutes)
# Signature historique: ALPHA hunter revenge 1.5x, leverage x10
# Sans ajouts V6.3 (lagrange/alarm/phase-shift/sentinel)

KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  if [[ -f "$KEYS_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$KEYS_FILE"
  fi
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  exit 1
fi
export BINANCE_API_KEY BINANCE_API_SECRET

TEST_TAG="TEST_MODELE_14_ORIGINAL_30M"
RUN_SEC=1800
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

touch STOP STOP_ALPHA STOP_BETA
sleep 1
pkill -f "ACE777_STRICT_CLONE_FUTURES.sh" 2>/dev/null || true
pkill -f "ACE777_STRICT_CLONE_FUTURES_V2.sh" 2>/dev/null || true
pkill -f "launch_test_duo_" 2>/dev/null || true
pkill -f "caffeinate -is bash -c" 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json runs/duo_burst_state.json runs/duo_alarm_v63.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "MODELE14 ORIGINAL: ALPHA x10 revenge1.5 | V6.3 OFF | GlobalStop=-5 non-blocking"

(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# BETA = scout stable (support)
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=SCOUT
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=20
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export FORCE_ENTRY_SIDE=BUY
export POSITION_SIDE=LONG
export LEVERAGE=5
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.45
export STOP_LOSS_BPS=12
export POLL_SEC=0.05
export BOT_LABEL="BETA_X5_MODELE14"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

sleep 2

# ALPHA = hunter modele 14 original
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=20
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-6
export DUO_SCOUT_SUFFER_USDT=-0.80
export DUO_HUNTER_REVENGE_MULT=1.5
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=10
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=10
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.65
export STOP_LOSS_BPS=10
export POLL_SEC=0.05
export BOT_LABEL="ALPHA_MODELE14_X10"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
