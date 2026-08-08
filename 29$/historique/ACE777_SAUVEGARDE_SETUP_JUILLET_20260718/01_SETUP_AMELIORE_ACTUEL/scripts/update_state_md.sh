#!/usr/bin/env bash
# Génère runs/STATE.md — mémoire canonique du cycle ACE777
# Usage:
#   ./scripts/update_state_md.sh
#   STATE_TAG=MASTER_BASE_V8_5_IMPACT_8H00 STATE_PHASE=running ./scripts/update_state_md.sh

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

# Charger config si pas déjà fait (pour afficher profil / masses / LLM)
if [ -z "${ACE777_CONFIG_LOADED:-}" ] && [ -f "./config_active.env" ]; then
  # shellcheck source=scripts/load_config.sh
  source ./scripts/load_config.sh 2>/dev/null || true
fi

export RUN_DIR="${RUN_DIR:-runs}"
export STATE_PHASE="${STATE_PHASE:-snapshot}"

ruby "${_root}/scripts/generate_state_md.rb"
# Rapport PnL session (filtre via run_meta start_utc) + RAPPORT_PNL_DERNIER
ruby "${_root}/scripts/generate_pnl_report.rb"
