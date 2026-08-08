#!/usr/bin/env bash
# Cortana P3 — watch (fills/baleine/move/Attention) puis poll voix (~10s launchd).
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$PATH"
export CORTANA_TTS="${CORTANA_TTS:-edge}"
export EDGE_TTS_RATE="${EDGE_TTS_RATE:--18%}"
export EDGE_TTS_VOICE="${EDGE_TTS_VOICE:-fr-FR-VivienneMultilingualNeural}"
set -a
# shellcheck disable=SC1091
source "$ROOT/Index_Maison/config_risk_warm.env" 2>/dev/null || true
set +a

LOG="$ROOT/Index_Maison/thermo/cortana_urgent_poll.log"
{
  echo "---- $(date -u +%Y-%m-%dT%H:%MZ) ----"
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/cockpit_mission_feed.py" || true
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/cortana_watch.py" || true
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/cortana_thermo.py" poll || true
} >>"$LOG" 2>&1
