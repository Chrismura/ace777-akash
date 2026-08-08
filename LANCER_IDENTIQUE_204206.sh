#!/usr/bin/env bash
# Point d'entrée unique — bot IDENTIQUE au +29,41 USDT du 10/07 session 204206
# Usage: ./LANCER_IDENTIQUE_204206.sh         → restaure + vérif
#        ./LANCER_IDENTIQUE_204206.sh lancer → restaure + vérif + run

exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/29$/REDEMARRER.sh" "$@"
