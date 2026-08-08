#!/bin/bash
# === VIDE FROID 4H BINANCE — lanceur canonique ===
# Config : config_active.env (source unique)
# Usage : ./launch_vide_froid_4h_binance.sh [--duration HH:MM:SS]

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Isoler $@ : load_config ne doit pas hériter de --duration
_args=("$@")
set --
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh
set -- "${_args[@]}"

export RUN_DURATION="${RUN_DURATION:-04:00:00}"
export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"
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

echo "=== VIDE FROID 4H BINANCE ==="
echo "Profil: ${ACE777_CONFIG_NAME} | BETA 70% | ALPHA 50% | 250ms | Shock -16bps | 64ms | durée ${RUN_DURATION}"
if [ "${CAFFEINATE_RUN}" = "TRUE" ] && command -v caffeinate >/dev/null 2>&1; then
  exec caffeinate -is ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
else
  exec ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
fi
