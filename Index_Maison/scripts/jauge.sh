#!/bin/bash
# jauge.sh — jauge d'energie A LA DEMANDE (correction famille 09/08 : plus de
# KeepAlive permanent -> la RAM est liberee ; on lance la jauge quand on la regarde).
# Usage : jauge.sh start | stop | status
ACTION="${1:-status}"
case "$ACTION" in
  start)
    if ! launchctl start com.ace777.jauge-energie 2>/dev/null; then
      # job non charge -> on le charge PUIS on le demarre (KeepAlive=false : load ne suffit pas)
      launchctl load "$HOME/Library/LaunchAgents/com.ace777.jauge-energie.plist" 2>/dev/null
      sleep 1
      launchctl start com.ace777.jauge-energie 2>/dev/null
    fi
    sleep 2
    if curl -s --max-time 3 http://127.0.0.1:8898/ >/dev/null 2>&1; then
      echo "Jauge lancée -> http://127.0.0.1:8898/"
    else
      echo "Jauge démarrée mais pas encore répond — reessaie dans 2 s : jauge.sh status"
    fi
    ;;
  stop)
    launchctl stop com.ace777.jauge-energie 2>/dev/null
    echo "Jauge arrêtée (RAM libérée)."
    ;;
  status)
    for i in 1 2 3; do
      if curl -s --max-time 3 http://127.0.0.1:8898/ >/dev/null 2>&1; then
        echo "Jauge ACTIVE sur http://127.0.0.1:8898/"
        exit 0
      fi
      sleep 1
    done
    echo "Jauge ARRÊTÉE (a la demande). Lance avec : jauge.sh start"
    ;;
  *)
    echo "usage: jauge.sh start | stop | status"
    ;;
esac
