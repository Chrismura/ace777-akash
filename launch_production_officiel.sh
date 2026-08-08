#!/usr/bin/env bash
# === RUN OFFICIEL PRODUCTION CONTINUE ===
# Moteur INCHANGÉ : genesis_manifest.txt + GEMINI_TEST (x13 fixe via ramp=gemini)
# Enveloppe seule : preflight machine + relance garage sur exit 75
#
# Lancer :
#   ./launch_production_officiel.sh
# Arrêter :
#   ./stop_ace777_hard.sh
#
# Testnet par défaut. Mainnet : BINANCE_MODE=live ./launch_production_officiel.sh

set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== RUN OFFICIEL PRODUCTION CONTINUE ==="
echo "Setup champion : GEMINI_TEST | ramp=gemini x13 fixe | profil vortex_v2_collab"
echo "Moteur         : genesis_manifest.txt (non modifié)"
echo "Durée cycle    : ${RUN_DURATION:-04:00:00} (auto-relance si crash sans STOP)"
echo "Mode Binance   : ${BINANCE_MODE:-testnet}"
echo "Arrêt total    : ./stop_ace777_hard.sh"
echo ""

if pgrep -fl "ace777-test-day1|launch_vortex|GEMINI_TEST|watchdog_ace777|genesis_manifest" >/dev/null 2>&1; then
  echo "ERREUR: un run est déjà actif."
  echo "  ./stop_ace777_hard.sh"
  pgrep -fl "ace777|launch_vortex|GEMINI|watchdog_ace777" 2>/dev/null || true
  exit 1
fi

rm -f STOP STOP_ALPHA STOP_BETA

export LAUNCH_V85_SCRIPT="./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh"
export ACE777_PRODUCTION_CONTINUE="TRUE"
export RUN_DURATION="${RUN_DURATION:-04:00:00}"
export BINANCE_MODE="${BINANCE_MODE:-testnet}"
export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"

# Profil champion chargé par launch_vortex via vortex_v2_collab
exec ./launch_vortex_v2_collab_4h_binance.sh "$@"
