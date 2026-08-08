#!/usr/bin/env bash
# Purge totale ACE777/NUAGE — vierge usine — exit 0 = STERILE=OK
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== PURGE VIERGE USINE — début ==="

./stop_ace777_hard.sh 2>/dev/null || true

# pkill retourne 1 si rien à tuer → || true obligatoire (sinon && casse la chaîne)
pkill -9 -f 'ace777_launch_v85_nuage' 2>/dev/null || true
pkill -9 -f 'launch_vide_froid_4h_binance_NUAGE' 2>/dev/null || true
pkill -9 -f 'launch_test_master_base_v8_6_fortress' 2>/dev/null || true
pkill -9 -f 'NUAGE_SMOKE' 2>/dev/null || true
pkill -9 -f 'NUAGE_PROD' 2>/dev/null || true
pkill -9 -f 'watchdog_ace777' 2>/dev/null || true
pkill -9 -f 'caffeinate -is.*ace777' 2>/dev/null || true
pkill -9 -f 'tail -n 0 -F runs/\.NUAGE' 2>/dev/null || true
pkill -9 -f 'tail -F runs/\.NUAGE' 2>/dev/null || true
pkill -9 -f 'bash -s' 2>/dev/null || true
pkill -9 -f 'genesis_manifest' 2>/dev/null || true

rm -f runs/master.pid runs/alpha.pid runs/beta.pid runs/timer.pid
rm -f runs/*wrapper*.pid runs/*genesis*.pid 2>/dev/null || true
rm -rf /tmp/ace777_ram_exchange && mkdir -p /tmp/ace777_ram_exchange
rm -f /tmp/alpha_heartbeat.txt
touch STOP STOP_ALPHA STOP_BETA
chmod +x scripts/verif_sterilite.sh

echo "=== PURGE VIERGE USINE — verif ==="
if ./scripts/verif_sterilite.sh --pre-run; then
  echo "=== PURGE VIERGE USINE — PASS ==="
  exit 0
fi

echo "=== PURGE VIERGE USINE — FAIL (voir ci-dessus) ==="
exit 1
