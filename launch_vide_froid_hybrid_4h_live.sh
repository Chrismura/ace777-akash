#!/bin/bash
# === VIDE FROID HYBRID 4H — BINANCE LIVE (argent réel) ===
# Prérequis : ~/.binance_live.env avec clés Futures mainnet
# Masses : BETA 200 / ALPHA 800 USDT (inchangé)

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

_args=("$@")
set --
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vide_froid_hybrid_reference
set -- "${_args[@]}"

export BINANCE_MODE=live
export BINANCE_ALLOW_MAINNET=TRUE
export BASE_URL=https://fapi.binance.com
export WATCHDOG_PING_URL=https://fapi.binance.com/fapi/v1/ping
export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-MASTER_HYBRID_VF_LIVE_4H}"
export RUN_DURATION="${RUN_DURATION:-04:00:00}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --duration)
      shift
      export RUN_DURATION="${1:-04:00:00}"
      ;;
    *)
      echo "Usage: $0 [--duration HH:MM:SS]"
      exit 1
      ;;
  esac
  shift || true
done

if [ ! -f "${HOME}/.binance_live.env" ]; then
  echo ""
  echo "ERREUR: ~/.binance_live.env introuvable."
  echo ""
  echo "Crée le fichier avec tes clés Binance Futures MAINNET :"
  echo '  export BINANCE_API_KEY="ta_cle"'
  echo '  export BINANCE_API_SECRET="ton_secret"'
  echo ""
  echo "Puis relance: ./launch_vide_froid_hybrid_4h_live.sh"
  exit 1
fi

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║  LIVE MAINNET — ARGENT RÉEL                      ║"
echo "║  BETA 200 USDT | ALPHA 800 USDT | levier x3/x13  ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""
echo "Profil: ${ACE777_CONFIG_NAME} | durée ${RUN_DURATION}"
sleep 3

if [ "${CAFFEINATE_RUN}" = "TRUE" ] && command -v caffeinate >/dev/null 2>&1; then
  exec caffeinate -is ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
else
  exec ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
fi
