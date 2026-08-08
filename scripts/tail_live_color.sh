#!/usr/bin/env bash
# Suivre les logs LIVE colorés du bot (pas le CSV — celui-ci est brut)
# Usage:
#   ./scripts/tail_live_color.sh                    # dernier run
#   ./scripts/tail_live_color.sh MASTER_HYBRID_VF_20260708

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tag="${1:-}"

if [ -n "$tag" ]; then
  log="${_root}/runs/${tag}_LIVE_COLOR.log"
else
  log="$(ls -t "${_root}"/runs/*_LIVE_COLOR.log 2>/dev/null | head -1 || true)"
fi

if [ -z "$log" ] || [ ! -f "$log" ]; then
  echo "Log coloré introuvable."
  echo ""
  echo "Ouvre un terminal Mac (Terminal.app ou iTerm) et lance :"
  echo "  cd ${_root}"
  echo "  ./scripts/tail_live_color.sh MASTER_HYBRID_VF_20260708"
  echo ""
  echo "Si le run a démarré avant ce fix, utilise :"
  echo "  tail -f ~/.cursor/projects/Users-christophe/terminals/631254.txt"
  exit 1
fi

echo "=== LOG COLORÉ === $log"
echo "Couleurs : cyan=info | vert=OK/BUY | jaune=SKIP/SELL | rouge=perte"
echo ""

# -R préserve les codes ANSI (couleurs)
if command -v less >/dev/null 2>&1; then
  LESS='-R' tail -f "$log" | less -R +F
else
  tail -f "$log"
fi
