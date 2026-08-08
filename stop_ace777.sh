#!/usr/bin/env bash
# Arrêt ACE777 — À lancer dans un NOUVEAU terminal

cd /Users/christophe/ace777-test-day1

touch STOP STOP_ALPHA STOP_BETA 2>/dev/null

# 1. Groupe process (priorité)
mp=$(cat runs/master.pid 2>/dev/null)
[ -n "$mp" ] && kill -9 -"$mp" 2>/dev/null
[ -n "$mp" ] && kill -9 "$mp" 2>/dev/null

# 2. Alpha, Beta
for p in $(cat runs/alpha.pid runs/beta.pid 2>/dev/null); do
  kill -9 -"$p" 2>/dev/null
  kill -9 "$p" 2>/dev/null
done

# 3. pkill
pkill -9 -f "launch_vortex_v2_collab" 2>/dev/null
pkill -9 -f "watchdog_ace777" 2>/dev/null
pkill -9 -f "caffeinate -is -w" 2>/dev/null
pkill -9 -f "genesis_manifest" 2>/dev/null
pkill -9 -f "tail -n +85" 2>/dev/null
pkill -9 -f "tail.*genesis" 2>/dev/null
pkill -9 -f "bash -s" 2>/dev/null
pkill -9 -f "launch_test_master_base" 2>/dev/null
pkill -9 -f "launch_test_master" 2>/dev/null
pkill -9 -f "tail.*genesis" 2>/dev/null
pkill -9 -f "radar_gate" 2>/dev/null
pkill -9 -f "ruby.*sleep" 2>/dev/null
pkill -9 -f "vortex_supervisor_v2_llm.rb" 2>/dev/null
if [ -f runs/timer.pid ]; then
  kill -9 "$(cat runs/timer.pid)" 2>/dev/null || true
  rm -f runs/timer.pid
fi
if [ -f runs/supervisor_v9_v2.pid ]; then
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || \
    kill -9 "$(cat runs/supervisor_v9_v2.pid)" 2>/dev/null || true
fi

# 4. Tout ce qui reste
for pid in $(ps -e -o pid= -o args= 2>/dev/null | grep -E "ace777-test-day1|genesis_manifest|launch_test_master" | grep -v grep | awk '{print $1}'); do
  kill -9 "$pid" 2>/dev/null
done

echo "Arrêté."

export STATE_PHASE="stopped"
./scripts/update_state_md.sh 2>/dev/null || true
./scripts/post_run_report.sh 2>/dev/null || true

if [ -x ./scripts/post_stop_cleanup.sh ]; then
  ./scripts/post_stop_cleanup.sh
fi
