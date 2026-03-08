#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Test 6h - Duo Scout/Hunter V5 (anti V-reversal, scelle)
# - Scout (BETA): x7
# - Hunter (ALPHA): x9
# - Etau: 20s
# - Vengeance: 1.2x
# - Stop global panier: -5 USDT

TEST_TAG="TEST_DUO_V5_6H_ANTI_VREV"
RUN_SEC=21600
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"

# Clean start
killall caffeinate ruby 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "BETA x7 | ALPHA x9 | Etau=20s | Vengeance=1.2x | Trigger=-11bps/-0.80 | GlobalStop=-5"

# Auto-stop after 6 hours
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
export LEVERAGE=7
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.45
export STOP_LOSS_BPS=15
export BOT_LABEL="BETA_X7"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA_X7.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

# Head start for state file
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
export DUO_HUNTER_REVENGE_MULT=1.2
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=12
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE=9
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.65
export STOP_LOSS_BPS=10
export BOT_LABEL="ALPHA_X9"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA_X9.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'
