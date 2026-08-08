#!/usr/bin/env bash
# Hygiène entre sessions (exit 75) — tue GEMINI/watchdog/genesis, garde le wrapper vortex parent
# Usage: ./scripts/garage_relance_ace777.sh [VORTEX_PID]
# Ne pose PAS STOP — permet la relance auto du wrapper vortex

set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

VORTEX_PID="${1:-0}"
RUN_DIR="${RUN_DIR:-runs}"

echo "[GARAGE_RELANCE] début (vortex parent pid=${VORTEX_PID})"

for pf in "$RUN_DIR/master.pid" "$RUN_DIR/beta.pid" "$RUN_DIR/alpha.pid" "$RUN_DIR/timer.pid"; do
  if [ -f "$pf" ]; then
    p="$(tr -d ' \n\r' < "$pf" 2>/dev/null || true)"
    if [ -n "$p" ] && [ "$p" != "$VORTEX_PID" ] && kill -0 "$p" 2>/dev/null; then
      kill -TERM -"$p" 2>/dev/null || true
      kill -TERM "$p" 2>/dev/null || true
    fi
  fi
done
sleep 1

_pkill_session() {
  pkill -9 -f "genesis_manifest" 2>/dev/null || true
  pkill -9 -f "tail -n +85" 2>/dev/null || true
  pkill -9 -f "tail.*genesis_manifest" 2>/dev/null || true
  pkill -9 -f "bash -s" 2>/dev/null || true
  pkill -9 -f "launch_test_master_base" 2>/dev/null || true
  pkill -9 -f "launch_test_master" 2>/dev/null || true
  pkill -9 -f "GEMINI_TEST" 2>/dev/null || true
  pkill -9 -f "watchdog_ace777" 2>/dev/null || true
  pkill -9 -f "vortex_supervisor_v2_llm.rb" 2>/dev/null || true
  pkill -9 -f "radar_gate" 2>/dev/null || true
  pkill -9 -f "launch_test_master_base_v8_6_fortress" 2>/dev/null || true
}

_pkill_session
sleep 1
_pkill_session

while IFS= read -r pid; do
  [ -z "$pid" ] && continue
  [ "$pid" = "$VORTEX_PID" ] && continue
  kill -9 "$pid" 2>/dev/null || true
done < <(ps -e -o pid= -o args= 2>/dev/null | grep -E "ace777-test-day1|genesis_manifest|launch_test_master|watchdog_ace777|GEMINI_TEST|vortex_supervisor_v2_llm" | grep -v grep | awk '{print $1}')

if [ -x ./scripts/stop_supervisor_v9_v2.sh ]; then
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
fi

rm -f "$RUN_DIR"/master.pid "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid "$RUN_DIR"/timer.pid
rm -f "$RUN_DIR"/duo_state.json "$RUN_DIR"/duo_session.json "$RUN_DIR"/swarm_telemetry.json
rm -f "$RUN_DIR"/duo_burst.json "$RUN_DIR"/duo_v63_alarm.json 2>/dev/null || true

_left="$(pgrep -fl "genesis_manifest|launch_test_master|GEMINI_TEST|watchdog_ace777|vortex_supervisor_v2_llm" 2>/dev/null || true)"
if [ -n "$_left" ]; then
  echo "[GARAGE_RELANCE] WARN résidu:"
  echo "$_left"
  exit 1
fi

echo "[GARAGE_RELANCE] OK — session nettoyée, vortex parent intact"
