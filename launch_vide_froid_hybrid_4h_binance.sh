#!/bin/bash
# === VIDE FROID HYBRID 4H — référence stase/shock + duo actuel ===
# Profil : vide_froid_hybrid_reference (A/B test vs vide_froid_binance canonique)

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

_args=("$@")
set --
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vide_froid_hybrid_reference
set -- "${_args[@]}"

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

export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-MASTER_HYBRID_VF_4H}"

echo "=== VIDE FROID HYBRID 4H ==="
echo "Profil: ${ACE777_CONFIG_NAME} | shock=10bps | stase=5/0.5 | duo fixes ON | durée ${RUN_DURATION}"

if [ "${CAFFEINATE_RUN}" = "TRUE" ] && command -v caffeinate >/dev/null 2>&1; then
  exec caffeinate -is ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
else
  exec ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
fi
