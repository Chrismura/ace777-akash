#!/bin/bash
# BONNET DE FORME CHAMPION — +29,41 USDT (20260710_204206)
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if pgrep -fl "ace777-test-day1|launch_vortex|GEMINI_TEST|bash -s" >/dev/null 2>&1; then
  echo "ERREUR: run actif — ./bonnet_forme_champion/ARRETER.sh d'abord"
  exit 1
fi

rm -f STOP STOP_ALPHA STOP_BETA
export LAUNCH_V85_SCRIPT="./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh"
exec ./launch_vortex_v2_collab_4h_binance.sh "$@"
