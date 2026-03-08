#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# MASTER BASE VALIDE - Test 6h30
# Duo Harmonic 5-8-13 + V6.3 phase-shift/sentinel

KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  if [[ -f "$KEYS_FILE" ]]; then
    # shellcheck disable=SC1090
    source "$KEYS_FILE"
  fi
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  echo "Ajoute-les dans $KEYS_FILE (ou exporte-les une fois)."
  exit 1
fi
export BINANCE_API_KEY BINANCE_API_SECRET

TEST_TAG="TEST_DUO_HARMONIC_5813_6H30_V63"
RUN_SEC=23400
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

killall caffeinate ruby 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json runs/duo_burst_state.json runs/duo_alarm_v63.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "BETA x5 | ALPHA x8 | Duo PLUS ACTIF | Trigger=-4bps/-0.30 | TTL=120s | Dopamine=ON | HunterSL=12bps | GlobalStop=-5 non-blocking | Lagrange+PhaseShift=ON"

(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=SCOUT
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_DOPAMINE_MODE=TRUE
export REWARD_SENSITIVITY_BOOST=0.2
export PAIN_ADAPTIVE_FILTER=1.5
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=BUY
export POSITION_SIDE=LONG
export LEVERAGE=5
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.35
export STOP_LOSS_BPS=12
export POLL_SEC=0.03
export BOT_LABEL="BETA_X5"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA_X5.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

sleep 2

caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-4
export DUO_SCOUT_SUFFER_USDT=-0.30
export DUO_HUNTER_REVENGE_MULT=1.618
export DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=12
export DUO_DOPAMINE_MODE=TRUE
export REWARD_SENSITIVITY_BOOST=0.2
export PAIN_ADAPTIVE_FILTER=1.5
export DUO_LAGRANGE_FEEDBACK_ENABLED=TRUE
export DUO_LAGRANGE_FEEDBACK_MS=1
export DUO_LAGRANGE_LAMBDA=1.618
export DUO_LAGRANGE_RECOVERY_RATIO=0.618
export DUO_LAGRANGE_PROOF_THRESHOLD=8
export DUO_LAGRANGE_ABSORB_ON_OPPOSE=TRUE
export DUO_V63_PHASE_SHIFT_ENABLED=TRUE
export DUO_V63_ALARM_BPS=13
export DUO_V63_ALARM_TTL_SEC=45
export DUO_V63_SENTINEL_ENABLED=TRUE
export DUO_V63_SENTINEL_MULT=2.0
export DUO_V63_ENGINE_EQUITY_USDT=250
export DUO_V63_PHASE_SHIFT_STEP_SEC=13
export DUO_V63_PHASE_SHIFT_ACCEL_STEP_SEC=5
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=8
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.50
export STOP_LOSS_BPS=8
export POLL_SEC=0.03
export BOT_LABEL="ALPHA_X8_BURST13"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA_X8_BURST13.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
