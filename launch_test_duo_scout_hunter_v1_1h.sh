#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Test 1h - Chasseur Souverain V1
# - Scout (BETA): x5
# - Hunter (ALPHA): x10
# - Etau: 20s
# - Vengeance: 1.5x

TEST_TAG="TEST_DUO_V1_1H"
RUN_SEC=3600
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "Scout=BETA x5 | Hunter=ALPHA x10 | Etau=20s | Vengeance=1.5x"

# Auto-stop after 1 hour
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# BETA = Scout (ouvre la voie, risque plus faible)
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
export STOP_LOSS_BPS=15
export POLL_SEC=0.02
export BOT_LABEL="BETA_SCOUT_X5"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA_SCOUT_X5.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

# Leave the scout a short head start so state file exists.
sleep 2

# ALPHA = Hunter (intervient sur souffrance scout)
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=20
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT=-5.00
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-10
export DUO_SCOUT_SUFFER_USDT=-0.75
export DUO_HUNTER_REVENGE_MULT=1.2
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=12
# Hunter must be execution-focused (duo trigger drives entries).
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=10
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.65
export STOP_LOSS_BPS=6
export POLL_SEC=0.02
export BOT_LABEL="ALPHA_HUNTER_X10"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA_HUNTER_X10.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
