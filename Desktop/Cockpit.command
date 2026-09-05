#!/usr/bin/env bash
# Cockpit ACE777 — double-clic pour ouvrir la version actuelle
set -uo pipefail
ROOT="$HOME/ace777-test-day1"
cd "$ROOT"

# Régénère uniquement le feed passif avant ouverture.
/usr/bin/python3 "$ROOT/Index_Maison/scripts/cockpit_mission_feed.py" >/tmp/cockpit_feed_desktop.log 2>&1 || true

URL="http://127.0.0.1:17800/cockpit/index.html?v=$(date +%s)"
BRAVE="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

if [[ -x "$BRAVE" ]]; then
  open -na "Brave Browser" --args --new-window --app="$URL"
else
  open "$URL"
fi
