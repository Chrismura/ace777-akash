#!/bin/bash
# === VIDE FROID 8H BINANCE — même config que 4H ===

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh

export RUN_DURATION="08:00:00"

echo "=== VIDE FROID 8H BINANCE ==="
echo "Profil: ${ACE777_CONFIG_NAME} | BETA 70% | ALPHA 50% | 250ms | Shock -16bps | 64ms"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 08:00:00
