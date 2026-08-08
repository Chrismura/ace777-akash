#!/bin/bash
# === VIDE FROID 8H — profil classic ===

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vide_froid_classic

export RUN_DURATION="08:00:00"

echo "=== VIDE FROID 8H CLASSIC === Profil: ${ACE777_CONFIG_NAME}"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 08:00:00
