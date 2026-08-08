#!/usr/bin/env bash
# Assure daemons (pont+HTTP) puis ouvre le cockpit.
# Ordre validé : LaunchAgents → pywebview → Brave --app (jamais Safari).
#
# Usage :
#   bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh
#   bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh --daemons
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
PY=/usr/bin/python3
ONLY_DAEMONS=0
[[ "${1:-}" == "--daemons" ]] && ONLY_DAEMONS=1

echo "=== COCKPIT UP ==="

need=0
curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status >/dev/null 2>&1 || need=1
curl -fsS --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html >/dev/null 2>&1 || need=1

if [[ $need -eq 1 ]]; then
  if [[ -f "$HOME/Library/LaunchAgents/com.ace777.cockpit-pont.plist" ]]; then
    echo "Relance daemons LaunchAgents…"
    launchctl kickstart -k "gui/$(id -u)/com.ace777.cockpit-pont" 2>/dev/null || true
    launchctl kickstart -k "gui/$(id -u)/com.ace777.cockpit-http" 2>/dev/null || true
    sleep 1
  fi
fi

if ! curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status >/dev/null 2>&1 \
  || ! curl -fsS --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html >/dev/null 2>&1; then
  echo "Install/repair daemons…"
  bash "$ROOT/Index_Maison/scripts/install_cockpit_daemons.sh" || true
fi

# fallback nohup
if ! curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status >/dev/null 2>&1; then
  echo "Fallback nohup pont…"
  nohup "$PY" "$ROOT/Index_Maison/scripts/cortana_cockpit_bridge.py" >>/tmp/cortana_cockpit_bridge.log 2>&1 &
fi
if ! curl -fsS --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html >/dev/null 2>&1; then
  echo "Fallback nohup http…"
  nohup "$PY" "$ROOT/Index_Maison/scripts/cockpit_http_server.py" >>/tmp/cockpit_http_17800.log 2>&1 &
fi

sleep 0.6
curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status >/dev/null 2>&1 && echo "PONT=ON" || echo "PONT=OFF"
curl -fsS --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html >/dev/null 2>&1 && echo "HTTP=ON" || echo "HTTP=OFF"

if [[ $ONLY_DAEMONS -eq 1 ]]; then
  echo "DONE --daemons"
  exit 0
fi

echo "Fenêtre : pywebview d’abord (Brave --app si échec)"
echo ">>> Recharger = ⌘R (pas F5)"

# Ouvre dans un nouveau Terminal (pywebview bloque sinon ce shell)
if osascript <<'APPLESCRIPT'
tell application "Terminal"
  activate
  do script "cd /Users/christophe/ace777-test-day1 && /usr/bin/python3 Index_Maison/scripts/open_cockpit_app.py"
end tell
APPLESCRIPT
then
  echo "MODE=Terminal+pywebview (nouvel onglet Terminal)"
else
  echo "osascript KO — lance open_cockpit ici"
  "$PY" "$ROOT/Index_Maison/scripts/open_cockpit_app.py"
fi

curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status 2>/dev/null \
  | "$PY" -c "import sys,json;d=json.load(sys.stdin);print('PONT',d.get('pont'),'| ACE',(d.get('ace')or{}).get('label'),'| NET',(d.get('net')or{}).get('label'))" \
  || true
echo "DONE"
exit 0
