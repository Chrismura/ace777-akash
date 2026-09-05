#!/usr/bin/env bash
# STOP SHADOW MODE — pose runs/STOP_SHADOW, le moteur sort proprement (fills conservés)
cd "$HOME/ace777-test-day1" || exit 1
touch runs/STOP_SHADOW
PID="$(cat runs/shadow.pid 2>/dev/null || true)"
if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
  sleep 3
  kill -0 "$PID" 2>/dev/null && kill "$PID" 2>/dev/null
fi
rm -f runs/shadow.pid
echo "SHADOW_OFF_OK: STOP_SHADOW posé — fills et ticks conservés dans runs/"
tail -3 runs/SHADOW_SC_$(date -u +%Y%m%d).log 2>/dev/null || true
