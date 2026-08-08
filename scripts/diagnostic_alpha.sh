#!/usr/bin/env bash
# Diagnostic ALPHA dormante — rapport sans modification de config
# Usage: STATE_TAG=MASTER_BASE_V8_5_IMPACT_8H00 ./scripts/diagnostic_alpha.sh

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

if [ -z "${ACE777_CONFIG_LOADED:-}" ] && [ -f "./config_active.env" ]; then
  # shellcheck source=scripts/load_config.sh
  source ./scripts/load_config.sh 2>/dev/null || true
fi

export RUN_DIR="${RUN_DIR:-runs}"
ruby "${_root}/scripts/generate_diag_alpha.rb"
