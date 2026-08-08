#!/usr/bin/env bash
# Hygiène #3 — rapport erreurs session ACE (après STOP ou incident)
# Usage:
#   ./scripts/rapport_erreurs_session.sh
#   ./scripts/rapport_erreurs_session.sh --since 2026-07-22T11:44:55Z
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
exec python3 "$ROOT/scripts/rapport_erreurs_session.py" "$@"
