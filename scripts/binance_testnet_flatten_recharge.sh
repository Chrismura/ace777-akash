#!/usr/bin/env bash
# Ferme toutes les positions testnet (hedge OK) + affiche solde.
# Faucet auto souvent bloqué → lien UI si solde < 1000.
# Usage: ./scripts/binance_testnet_flatten_recharge.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
exec python3 "$ROOT/scripts/binance_testnet_flatten_recharge.py" "$@"
