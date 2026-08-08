#!/usr/bin/env bash
# Nuit : Ghost Hulk 30min + à la fin du run ACE → hygiène + 1 relance (set MIN 2.5).
# Log: runs/NUIT_GHOST_RELANCE.log
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
LOG="$ROOT/runs/NUIT_GHOST_RELANCE.log"
mkdir -p "$ROOT/runs"
exec >>"$LOG" 2>&1

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
echo "$(ts) NUIT_START pid=$$"

# --- Ghost loop (background) ---
(
  cd "$ROOT/hulk-mexc"
  while true; do
    ./scripts/watchdog_hulk_ghost.sh || true
    sleep 1800
  done
) &
GHOST_PID=$!
echo "$(ts) GHOST_LOOP pid=$GHOST_PID"
echo "$GHOST_PID" > "$ROOT/runs/nuit_ghost_loop.pid"

# --- Wait ACE current run end ---
# Prefer planned_end from meta; also accept no GO/caffeinate
META="$ROOT/runs/NUAGE_PROD_4H_run_meta.json"
PLANNED=""
if [ -f "$META" ]; then
  PLANNED="$(python3 -c 'import json;print(json.load(open("'"$META"'")).get("planned_end_utc",""))' 2>/dev/null || true)"
fi
echo "$(ts) wait ACE planned_end=$PLANNED"

ace_alive() {
  pgrep -f 'caffeinate -dims env .*GO_USINE_NUAGE|caffeinate -dims ./GO_USINE_NUAGE|/tmp/ace777_launch_v85' >/dev/null 2>&1
}

# Wait until past planned end OR process gone for 90s
while true; do
  NOW_EPOCH="$(date -u +%s)"
  if [ -n "$PLANNED" ]; then
    PLAN_EPOCH="$(python3 -c 'from datetime import datetime,timezone; s="'"$PLANNED"'"; print(int(datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()))' 2>/dev/null || echo 0)"
    if [ "$PLAN_EPOCH" -gt 0 ] && [ "$NOW_EPOCH" -ge "$PLAN_EPOCH" ]; then
      echo "$(ts) PAST_PLANNED_END"
      break
    fi
  fi
  if ! ace_alive; then
    echo "$(ts) ACE_PROCESS_GONE — confirm 90s"
    sleep 90
    if ! ace_alive; then
      echo "$(ts) ACE_CONFIRMED_DEAD"
      break
    fi
  fi
  sleep 60
done

# Drain orphans briefly
echo "$(ts) HYGIENE"
pkill -f 'File.write..STOP_ALPHA' 2>/dev/null || true
pkill -f 'ace777_launch_v85_nuage' 2>/dev/null || true
pkill -f 'launch_test_master_base_v8_6_fortress' 2>/dev/null || true
sleep 2
./scripts/rapport_erreurs_session.sh || true
./scripts/post_stop_cleanup.sh || true

# Wallet: masses adaptées si solde serré (200+700=900 < ~975+)
# Set = matin MIN 2.5 + storm/BIDIR
echo "$(ts) RELANCE_ACE MIN_ENTRY=2.5"
nohup caffeinate -dims env \
  BUY_USDT_BETA=200 \
  BUY_USDT_ALPHA=700 \
  NUAGE_BIDIR_SIDES=1 \
  NUAGE_STORM_LATCH=1 \
  NUAGE_STORM_SCOUT_HOLD=1 \
  NUAGE_STORM_HUNTER=1 \
  NUAGE_MIN_ENTRY_TENSION=2.5 \
  ./GO_USINE_NUAGE.sh 04:00:00 NUAGE_PROD_4H \
  >"$ROOT/runs/NUIT_RELANCE_GO.out" 2>&1 &
echo "$(ts) RELANCE_PID=$! out=runs/NUIT_RELANCE_GO.out"
echo "$(ts) NUIT_DONE — Ghost loop continues pid=$GHOST_PID"
# keep ghost loop attached to this script's wait
wait "$GHOST_PID" || true
