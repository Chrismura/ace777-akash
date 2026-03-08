#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# VORTEX CIRCULAIRE v6.3 (Fibonacci 5-8-13) - 30 min
# Mapping from user config:
# - fibonacci_sequence [5,8,13] -> LEVERAGE scout=5, hunter=8, burst=13(eq via 1.618)
# - lagrange_multiplicator_lambda=1.618 -> DUO_HUNTER_REVENGE_MULT
# - recovery_ratio=0.618 -> DUO_V6_BOOST_MULT
# - emergency_slingshot_enabled=true -> DUO_V6_BURST_X13=TRUE
# - max_drawdown_per_spiral=fib_8 -> stop-loss 8 bps on hunter
# - sync_delay_ms=13 -> launch offset 0.013s

KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  if [[ -f "$KEYS_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$KEYS_FILE"
  fi
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  echo "Charge-les via: source ~/.binance_testnet.env"
  exit 1
fi
export BINANCE_API_KEY BINANCE_API_SECRET

RUN_SEC="${RUN_SEC:-1800}"
TEST_TAG="${TEST_TAG:-TEST_DUO_VORTEX_CIRC_V63_30M}"
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

# Clean start (targeted, avoids broad killall ruby)
touch STOP STOP_ALPHA STOP_BETA
sleep 1
pkill -f "ACE777_STRICT_CLONE_FUTURES.sh" 2>/dev/null || true
pkill -f "ACE777_STRICT_CLONE_FUTURES_V2.sh" 2>/dev/null || true
pkill -f "launch_test_duo_" 2>/dev/null || true
pkill -f "caffeinate -is bash -c" 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json runs/duo_burst_state.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "Vortex 5/8/13 | lambda=1.618 | recovery=0.618 | drawdown=fib8 | GlobalStop=-5 non-blocking"

# Auto-stop after RUN_SEC
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# P1 Leader = SCOUT
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=SCOUT
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export FORCE_ENTRY_SIDE=BUY
export POSITION_SIDE=LONG
export LEVERAGE=5
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.30
export STOP_LOSS_BPS=12
export POLL_SEC=0.05
export BOT_LABEL="P1_SCOUT_VORTEX_5"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_P1_SCOUT.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

# sync_delay_ms=13
sleep 0.013

# P2 Support = HUNTER
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-5
export DUO_SCOUT_SUFFER_USDT=-0.618
export DUO_HUNTER_REVENGE_MULT=1.618
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=8
export DUO_V6_SENSITIVITY_BOOST=TRUE
export DUO_V6_FAST_DEATH_SEC=30
export DUO_V6_BOOST_MULT=0.618
export DUO_V6_BOOST_TTL_SEC=40
export DUO_V6_STASE_EXIT=TRUE
export DUO_V6_STASE_EMA_SEC=30
export DUO_V6_STASE_BREAK_BPS=2
export DUO_V6_BURST_X13=TRUE
export DUO_V6_BURST_MULT=1.618
export DUO_V6_BURST_MIN_LOSS_BPS=13
export DUO_V6_BURST_MIN_SPEED_BPS_PER_SEC=0.8
export DUO_V6_BURST_COOLDOWN_SEC=188
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=8
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.55
export STOP_LOSS_BPS=8
export POLL_SEC=0.05
export BOT_LABEL="P2_HUNTER_VORTEX_8"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_P2_HUNTER.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
