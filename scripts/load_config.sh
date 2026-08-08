#!/usr/bin/env bash
# Charge config_active.env (+ profil optionnel) une seule fois par run.
# Usage : source ./scripts/load_config.sh [profil]
# Exemple : source ./scripts/load_config.sh masse_250

_ace777_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ -n "${ACE777_CONFIG_LOADED:-}" ]; then
  return 0 2>/dev/null || exit 0
fi

if [ ! -f "${_ace777_root}/config_active.env" ]; then
  echo "CONFIG_ERR: config_active.env introuvable dans ${_ace777_root}" >&2
  return 1 2>/dev/null || exit 1
fi

set -a
# shellcheck source=/dev/null
source "${_ace777_root}/config_active.env"
if [ -n "${1:-}" ]; then
  _profile="${_ace777_root}/config_profiles/${1}.env"
  if [ ! -f "$_profile" ]; then
    echo "CONFIG_ERR: profil introuvable: $_profile" >&2
    return 1 2>/dev/null || exit 1
  fi
  # shellcheck source=/dev/null
  source "$_profile"
fi
set +a

export ACE777_CONFIG_LOADED=1
echo "=== CONFIG === name=${ACE777_CONFIG_NAME} v=${ACE777_CONFIG_VERSION} BETA=${BUY_USDT_BETA} ALPHA=${BUY_USDT_ALPHA}"
