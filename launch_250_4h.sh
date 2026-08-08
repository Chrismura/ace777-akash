#!/usr/bin/env bash
# === SETUP 250$ × 4h — override profil masse_250 (hors canonique) ===

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh masse_250

export RUN_DURATION="04:00:00"

echo "=== 250\$ × 4h === OVERRIDE masse_250 | BETA=${BUY_USDT_BETA} ALPHA=${BUY_USDT_ALPHA} | LLM gate ON"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
