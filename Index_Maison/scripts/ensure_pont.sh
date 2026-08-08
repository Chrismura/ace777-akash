#!/usr/bin/env bash
# Garde le pont cockpit :17777 allumé (idempotent).
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
LOG="/tmp/cortana_cockpit_bridge.log"
if curl -fsS --connect-timeout 1 "http://127.0.0.1:17777/status" >/dev/null 2>&1; then
  echo "PONT=ON :17777"
  exit 0
fi
echo "PONT=OFF — démarrage…"
nohup /usr/bin/python3 "$ROOT/Index_Maison/scripts/cortana_cockpit_bridge.py" >>"$LOG" 2>&1 &
for _ in 1 2 3 4 5 6 7 8 9 10; do
  sleep 0.3
  if curl -fsS --connect-timeout 1 "http://127.0.0.1:17777/status" >/dev/null 2>&1; then
    echo "PONT=ON :17777"
    exit 0
  fi
done
echo "PONT=FAIL — voir $LOG" >&2
exit 1
