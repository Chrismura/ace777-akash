#!/usr/bin/env bash
# CSV en couleurs (lisible) — alternative au log LIVE
# Usage: ./scripts/tail_csv_color.sh [BETA|ALPHA]

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
unit="${1:-BETA}"
tag="${2:-}"

if [ -z "$tag" ]; then
  if [ "$unit" = "ALPHA" ]; then
    f="$(ls -t "${_root}"/runs/*_ALPHA_*.csv 2>/dev/null | head -1)"
  else
    f="$(ls -t "${_root}"/runs/*_BETA_*.csv 2>/dev/null | head -1)"
  fi
else
  if [ "$unit" = "ALPHA" ]; then
    f="${_root}/runs/${tag}_ALPHA_X13_BURST13.csv"
  else
    f="${_root}/runs/${tag}_BETA_X5.csv"
  fi
fi

[ -f "$f" ] || { echo "CSV introuvable: $f"; exit 1; }

R='\033[1;31m' G='\033[1;32m' Y='\033[1;33m' C='\033[1;36m' M='\033[1;35m' N='\033[0m'

echo -e "${C}=== CSV COLORÉ ===${N} $f"
echo -e "${Y}SKIP${N}=jaune | ${G}FILLED gain${N} | ${R}FILLED perte${N} | ${M}BETA${N}/${C}ALPHA${N}"
echo ""

tail -f "$f" | while IFS= read -r line; do
  if [[ "$line" == ts,* ]]; then
    echo -e "${C}${line}${N}"
  elif [[ "$line" == *",SKIP,"* ]] || [[ "$line" == *",SKIPPED"* ]]; then
    echo -e "${Y}${line}${N}"
  elif [[ "$line" == *",FILLED"* ]]; then
    pnl="$(echo "$line" | awk -F, '{print $9}')"
    if awk -v p="$pnl" 'BEGIN{exit (p+0>0)?0:1}'; then
      echo -e "${G}${line}${N}"
    elif awk -v p="$pnl" 'BEGIN{exit (p+0<0)?0:1}'; then
      echo -e "${R}${line}${N}"
    else
      echo "$line"
    fi
  else
    echo "$line"
  fi
done
