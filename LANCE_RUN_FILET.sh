#!/usr/bin/env bash
# ============================================================
# LANCE_RUN_FILET.sh — recharge les plists fragiles (superviseur-core, vigie-live)
# PUIS lance le run VORTEX avec filet STOP_MARKET actif (patch 64fb153f).
# Usage: ./LANCE_RUN_FILET.sh
# ============================================================
set -uo pipefail
cd "$(cd "$(dirname "$0")" && pwd)"

echo "=== Recharge les 2 plists fragiles (anti-Errno35) ==="
for p in com.ace777.superviseur-core com.ace777.vigie-live; do
  launchctl bootout "gui/$(id -u)/$p" 2>/dev/null
  launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/$p.plist" 2>/dev/null
  sleep 1
done

echo "=== Vérif 5/5 plists de garde-fou ==="
_absents=""
for p in com.ace777.sante-index com.ace777.veille-degradation com.ace777.dms-veille com.ace777.superviseur-core com.ace777.vigie-live; do
  if launchctl list 2>/dev/null | grep -q "$p"; then
    echo "  OK   $p"
  else
    _absents="$_absents $p"
    echo "  MANQ $p"
  fi
done
if [ -n "$_absents" ]; then
  echo "FAIL: plists manquantes:$_absents — relance ce script."
  exit 1
fi

echo "=== Lancement run VORTEX 4h + filet STOP_MARKET (patch 64fb153f) ==="
exec env ACE_STOP_MARKET_ENABLED=TRUE ACE_STOP_MARKET_BPS=20 ./GO_VORTEX_V2.sh 04:00:00
