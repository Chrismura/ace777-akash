#!/usr/bin/env bash
# Cockpit ACE777 — lancement simple et déterministe.
# Les serveurs HTTP/pont sont gérés par LaunchAgents ; ce script ne crée aucun doublon.
set -uo pipefail

ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
PY="/usr/bin/python3"
ONLY_DAEMONS=0
[[ "${1:-}" == "--daemons" ]] && ONLY_DAEMONS=1

echo "=== COCKPIT UP ==="

# Feed passif : aucune commande trading, uniquement mission.json/mission.js.
"$PY" "$ROOT/Index_Maison/scripts/cockpit_mission_feed.py" \
  >/tmp/cockpit_feed_desktop.log 2>&1 || true

# Vérifier que le serveur persistant sert bien le cockpit.
if ! curl -fsS --connect-timeout 2 \
  "http://127.0.0.1:17800/cockpit/index.html" >/dev/null 2>&1; then
  echo "HTTP cockpit indisponible sur :17800" >&2
  exit 1
fi

if [[ $ONLY_DAEMONS -eq 1 ]]; then
  echo "HTTP=ON :17800"
  exit 0
fi

URL="http://127.0.0.1:17800/cockpit/index.html?v=$(date +%s)"
BRAVE="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

if [[ -x "$BRAVE" ]]; then
  echo "Ouverture Brave app : $URL"
  # Nouvelle instance Brave dédiée : ne pas réutiliser la session personnelle existante.
  open -na "Brave Browser" --args --user-data-dir="$HOME/Library/Application Support/ACE777-Cockpit-Brave" --new-window --app="$URL" >/tmp/cockpit_brave_desktop.log 2>&1 &
else
  echo "Brave absent — ouverture navigateur par défaut : $URL"
  open "$URL"
fi

echo "COCKPIT=ON"
exit 0
