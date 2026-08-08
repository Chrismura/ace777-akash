#!/usr/bin/env bash
# Vérification binaire stérilité ACE777/NUAGE — exit 0 = GO | exit 1 = STOP
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PATTERN='ace777|NUAGE|genesis_manifest|bash -s|watchdog_ace777|ace777_launch_v85|launch_vide_froid_4h_binance|launch_test_master_base_v8_6|tail -n 0 -F runs/|tail -F runs/\.NUAGE|caffeinate -is.*ace777'

_left="$(pgrep -fl "$PATTERN" 2>/dev/null | grep -vi ollama || true)"

if [ -n "$_left" ]; then
  echo "STERILE=NOK"
  echo "$_left"
  exit 1
fi

# Fichiers STOP doivent exister avant un run (pas après purge pré-run)
if [ "${1:-}" = "--pre-run" ]; then
  for f in STOP STOP_ALPHA STOP_BETA; do
    if [ ! -f "$f" ]; then
      echo "STERILE=NOK — manquant: $f (pose STOP avant run)"
      exit 1
    fi
  done
  if [ -f runs/master.pid ]; then
    echo "STERILE=NOK — runs/master.pid existe encore"
    exit 1
  fi
fi

echo "STERILE=OK"
exit 0
