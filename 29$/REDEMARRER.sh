#!/usr/bin/env bash
# Setup IDENTIQUE session 204206 (+29,41 USDT du 10/07/2026 20:27 UTC)
# Usage: ./29$/REDEMARRER.sh          → restaure + vérif (sans lancer)
#        ./29$/REDEMARRER.sh lancer   → restaure + vérif + lancement

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "=== SETUP IDENTIQUE 204206 — $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

# 1. Hygiène process
if pgrep -fl "ace777-test-day1|launch_vortex|GEMINI_TEST|watchdog_ace777|genesis_manifest" 2>/dev/null | grep -v watchdogd >/dev/null; then
  echo "Process actifs détectés → stop hard..."
  ./stop_ace777_hard.sh
fi

# 2. Moteur champion (37fca367 — barrière OUI, PHI NON)
echo "Restauration genesis 37fca367..."
cp "$ROOT/genesis_manifest.txt.SAUVE_avant_champion_restore" "$ROOT/genesis_manifest.txt"

# 3. Lanceur GEMINI champion (BETA x3, ALPHA x13 fixe)
echo "Restauration GEMINI_TEST champion (BETA x3)..."
cp "$ROOT/launch_test_master_base_v8_5_impact_GEMINI_TEST.sh.SAUVE_20260711_1336" \
   "$ROOT/launch_test_master_base_v8_5_impact_GEMINI_TEST.sh"

# 4. Purge STOP
rm -f STOP STOP_ALPHA STOP_BETA

# 5. Vérif
unset ALPHA_RAMP_MODE 2>/dev/null || true
./scripts/verif_setup_champion.sh
rc=$?
if [ "$rc" -ne 0 ]; then
  echo "VERIF ÉCHEC — ne pas lancer."
  exit "$rc"
fi

if [ "${1:-}" != "lancer" ]; then
  echo ""
  echo "VERIF OK — prêt. Pour lancer:"
  echo "  ./29$/REDEMARRER.sh lancer"
  exit 0
fi

echo ""
echo "=== LANCEMENT IDENTIQUE 204206 ==="
unset ALPHA_RAMP_MODE
export LAUNCH_V85_SCRIPT="./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh"
exec ./launch_vortex_v2_collab_4h_binance.sh
