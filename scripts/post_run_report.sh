#!/usr/bin/env bash
# Rapport PnL auto post-run — archive + index + RUN_INDEX
# Usage: STATE_TAG=MASTER_BASE_V8_5_IMPACT_8H00 ./scripts/post_run_report.sh

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

export RUN_DIR="${RUN_DIR:-runs}"
tag="${STATE_TAG:-${TEST_TAG_OVERRIDE:-}}"
meta_path=""
if [ -n "$tag" ]; then
  meta_path="${RUN_DIR}/${tag}_run_meta.json"
fi

# Profil réel du run (meta lancé avec vortex_v2_collab) > config_active.env seul
if [ -n "$meta_path" ] && [ -f "$meta_path" ]; then
  eval "$(ruby -rjson -e '
    m = JSON.parse(File.read(ARGV[0]))
    cn = m["config"].to_s.gsub(/"/, "\\\"")
    cv = m["version"].to_s.gsub(/"/, "\\\"")
    puts "export ACE777_CONFIG_NAME=\"#{cn}\"" if cn != "" && cn != "?"
    puts "export ACE777_CONFIG_VERSION=\"#{cv}\"" if cv != "" && cv != "?"
  ' "$meta_path")"
elif [ -z "${ACE777_CONFIG_LOADED:-}" ] && [ -f "./config_active.env" ]; then
  # shellcheck source=scripts/load_config.sh
  source ./scripts/load_config.sh 2>/dev/null || true
fi

ruby "${_root}/scripts/generate_pnl_report.rb"
./scripts/diagnostic_alpha.sh 2>/dev/null || true
# Hygiène #3 — toujours WHY_ARRET après un run
STATE_TAG="${STATE_TAG:-${TEST_TAG_OVERRIDE:-NUAGE_PROD_4H}}" \
  ./scripts/rapport_erreurs_session.sh 2>/dev/null || true
