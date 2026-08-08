#!/bin/bash
# === VIDE FROID 4H — profil classic (stase 5bps, confirm 500ms) ===

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vide_froid_classic

export RUN_DURATION="04:00:00"

echo "=== VIDE FROID 4H CLASSIC === Profil: ${ACE777_CONFIG_NAME}"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
