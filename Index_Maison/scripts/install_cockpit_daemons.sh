#!/usr/bin/env bash
# Démarre pont + HTTP en arrière-plan durable (LaunchAgents optionnels).
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
PY=/usr/bin/python3
LABEL_PONT="com.ace777.cockpit-pont"
LABEL_HTTP="com.ace777.cockpit-http"
AGENTS="$HOME/Library/LaunchAgents"

mkdir -p "$AGENTS"

cat > "$AGENTS/${LABEL_PONT}.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>${LABEL_PONT}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PY}</string>
    <string>${ROOT}/Index_Maison/scripts/cortana_cockpit_bridge.py</string>
  </array>
  <key>WorkingDirectory</key><string>${ROOT}</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>/tmp/cortana_cockpit_bridge.log</string>
  <key>StandardErrorPath</key><string>/tmp/cortana_cockpit_bridge.log</string>
</dict>
</plist>
EOF

cat > "$AGENTS/${LABEL_HTTP}.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>${LABEL_HTTP}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PY}</string>
    <string>${ROOT}/Index_Maison/scripts/cockpit_http_server.py</string>
  </array>
  <key>WorkingDirectory</key><string>${ROOT}</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>/tmp/cockpit_http_17800.log</string>
  <key>StandardErrorPath</key><string>/tmp/cockpit_http_17800.log</string>
</dict>
</plist>
EOF

# unload si déjà là (ignore erreurs)
launchctl bootout "gui/$(id -u)/${LABEL_PONT}" 2>/dev/null || true
launchctl bootout "gui/$(id -u)/${LABEL_HTTP}" 2>/dev/null || true
launchctl unload "$AGENTS/${LABEL_PONT}.plist" 2>/dev/null || true
launchctl unload "$AGENTS/${LABEL_HTTP}.plist" 2>/dev/null || true
sleep 0.3

launchctl bootstrap "gui/$(id -u)" "$AGENTS/${LABEL_PONT}.plist" 2>/dev/null \
  || launchctl load "$AGENTS/${LABEL_PONT}.plist"
launchctl bootstrap "gui/$(id -u)" "$AGENTS/${LABEL_HTTP}.plist" 2>/dev/null \
  || launchctl load "$AGENTS/${LABEL_HTTP}.plist"

# kickstart
launchctl kickstart -k "gui/$(id -u)/${LABEL_PONT}" 2>/dev/null || true
launchctl kickstart -k "gui/$(id -u)/${LABEL_HTTP}" 2>/dev/null || true

echo "LaunchAgents: ${LABEL_PONT} + ${LABEL_HTTP} (KeepAlive)"
for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
  sleep 0.4
  ok_p=0; ok_h=0
  curl -fsS --connect-timeout 1 http://127.0.0.1:17777/status >/dev/null 2>&1 && ok_p=1
  curl -fsS --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html >/dev/null 2>&1 && ok_h=1
  if [[ $ok_p -eq 1 && $ok_h -eq 1 ]]; then
    echo "PONT=ON HTTP=ON"
    exit 0
  fi
done
echo "WAIT — pont=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 1 http://127.0.0.1:17777/status 2>/dev/null || echo 000) http=$(curl -s -o /dev/null -w '%{http_code}' --connect-timeout 1 http://127.0.0.1:17800/cockpit/index.html 2>/dev/null || echo 000)"
exit 1
