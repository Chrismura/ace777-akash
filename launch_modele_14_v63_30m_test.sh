#!/usr/bin/env bash
set -euo pipefail

cd /app

# MODELE 14 (trade ref ~14.8 USDT) + dernieres mises a jour V6.3
# - Signature historique: ALPHA hunter revenge 1.5x, leverage x10
# - Ajouts recents: Lagrange feedback, ALARM_V6.3, phase-shift 13->8->5->0,
#   sentinel avec garde d'equite (accelerer a 5s si depassement).

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

TEST_TAG="${TEST_TAG:-TEST_MODELE_14_V63_30M}"
RUN_SEC="${RUN_SEC:-1800}"
SCOUT_LEVERAGE="${SCOUT_LEVERAGE:-5}"
HUNTER_LEVERAGE="${HUNTER_LEVERAGE:-8}"
BETA_MOMENTUM_THRESHOLD="${BETA_MOMENTUM_THRESHOLD:-0.45}"
ALPHA_MOMENTUM_THRESHOLD="${ALPHA_MOMENTUM_THRESHOLD:-0.65}"
BETA_POLL_SEC="${BETA_POLL_SEC:-0.05}"
ALPHA_POLL_SEC="${ALPHA_POLL_SEC:-0.05}"
BETA_STOP_LOSS_BPS="${BETA_STOP_LOSS_BPS:-12}"
ALPHA_STOP_LOSS_BPS="${ALPHA_STOP_LOSS_BPS:-10}"
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
echo "MODELE14: SCOUT x${SCOUT_LEVERAGE} | HUNTER x${HUNTER_LEVERAGE} | V6.3 ON | GlobalStop=-5 non-blocking"
echo "ENTREES: BETA_MOM=${BETA_MOMENTUM_THRESHOLD} ALPHA_MOM=${ALPHA_MOMENTUM_THRESHOLD} BETA_POLL=${BETA_POLL_SEC}s ALPHA_POLL=${ALPHA_POLL_SEC}s"

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
export LEVERAGE='"$SCOUT_LEVERAGE"'
export BUY_USDT=250
export MOMENTUM_THRESHOLD='"$BETA_MOMENTUM_THRESHOLD"'
export STOP_LOSS_BPS='"$BETA_STOP_LOSS_BPS"'
export POLL_SEC='"$BETA_POLL_SEC"'
export BOT_LABEL="BETA_X'"$SCOUT_LEVERAGE"'_MODELE14"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

sleep 2

# ALPHA = hunter modele 14 + updates
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
export LEVERAGE='"$HUNTER_LEVERAGE"'
export BUY_USDT=250
export MOMENTUM_THRESHOLD='"$ALPHA_MOMENTUM_THRESHOLD"'
export STOP_LOSS_BPS='"$ALPHA_STOP_LOSS_BPS"'
export POLL_SEC='"$ALPHA_POLL_SEC"'
export BOT_LABEL="ALPHA_MODELE14_X'"$HUNTER_LEVERAGE"'"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
