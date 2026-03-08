#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Charge automatique des cles API (optionnel)
KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  if [[ -f "$KEYS_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$KEYS_FILE"
  fi
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  echo "Ajoute-les dans $KEYS_FILE."
  exit 1
fi
export BINANCE_API_KEY BINANCE_API_SECRET

TEST_TAG="TEST_DUO_V6_HASHRATE_6H"
RUN_SEC=21600
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

killall caffeinate ruby 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json runs/duo_burst_state.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "V6+Hashrate | BETA x5 | ALPHA x8->x13 | FastDeathBoost | StaseExit | BurstCooldown=188s"

(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# BETA = Scout
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
export BOT_LABEL="BETA_X5_V6"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA_X5.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

sleep 2

# ALPHA = Hunter
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=20
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-11
export DUO_SCOUT_SUFFER_USDT=-0.80
export DUO_HUNTER_REVENGE_MULT=1.625
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=9
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=8
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.65
export STOP_LOSS_BPS=8

export DUO_V6_SENSITIVITY_BOOST=TRUE
export DUO_V6_FAST_DEATH_SEC=30
export DUO_V6_BOOST_MULT=0.5
export DUO_V6_BOOST_TTL_SEC=40
export DUO_V6_STASE_EXIT=TRUE
export DUO_V6_STASE_EMA_SEC=30
export DUO_V6_STASE_BREAK_BPS=3
export DUO_V6_BURST_X13=TRUE
export DUO_V6_BURST_MULT=1.625
export DUO_V6_BURST_MIN_LOSS_BPS=15
export DUO_V6_BURST_MIN_SPEED_BPS_PER_SEC=0.5
export DUO_V6_BURST_COOLDOWN_SEC=188
export DUO_V6_BURST_FILE="runs/duo_burst_state.json"

export BTC_HASHRATE_GATE=TRUE
export BTC_HASHRATE_REFRESH_SEC=300
export BTC_HASHRATE_REQUIRE_UPTREND=FALSE
export BTC_HASHRATE_MIN_DELTA_PCT=0
export BTC_HASHRATE_FAIL_OPEN=TRUE
export BTC_HASHRATE_MOMENTUM_MULT_STRONG=0.9
export BTC_HASHRATE_MOMENTUM_MULT_WEAK=1.1
export BTC_HASHRATE_STRONG_DELTA_PCT=1.0
export BTC_HASHRATE_WEAK_DELTA_PCT=-1.0

export BOT_LABEL="ALPHA_X8_V6_HASH"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA_X8.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
