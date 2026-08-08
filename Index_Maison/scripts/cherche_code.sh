#!/bin/bash
# cherche_code.sh — recherche sémantique de code via Semble (extraits précis, -99% tokens).
# Usage:
#   bash cherche_code.sh "comment le routage par complexité fonctionne" [chemin] [top-k]
#   bash cherche_code.sh "où est défini call_provider" ~/prise-ia 5
#
# Semble est installé via uv tool (Python >= 3.10) dans ~/.local/bin.
set -euo pipefail

QUERY="${1:?Usage: cherche_code.sh \"requête\" [chemin] [top-k]}"
CHEMIN="${2:-$(pwd)}"
TOPK="${3:-5}"
SEMBLE="$HOME/.local/bin/semble"

if [ ! -x "$SEMBLE" ]; then
    echo "Semble absent — installer : uv tool install semble" >&2
    exit 1
fi

"$SEMBLE" search "$QUERY" "$CHEMIN" --top-k "$TOPK" --max-snippet-lines 20
