#!/usr/bin/env bash
# === RAPPORT PNL 3 PARTIES (fenêtre 4h découpée en 3) ===
# Usage: ./rapport_pnl_3_parties_4h.sh [START_UTC] [END_UTC]
# Ex: ./rapport_pnl_3_parties_4h.sh 2026-03-09T22:03:24Z 2026-03-10T02:03:24Z

set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RUN_DIR="${RUN_DIR:-runs}"
BETA_CSV="${BETA_CSV:-${RUN_DIR}/MASTER_BASE_V8_5_IMPACT_4H_BETA_X5.csv}"
ALPHA_CSV="${ALPHA_CSV:-${RUN_DIR}/MASTER_BASE_V8_5_IMPACT_4H_ALPHA_X13_BURST13.csv}"

start_utc="${1:-2026-03-09T22:03:24Z}"
end_utc="${2:-2026-03-10T02:03:24Z}"

part1_end="$(ruby -e "
  require 'time'
  s = Time.parse(ARGV[0])
  e = Time.parse(ARGV[1])
  d = (e - s) / 3
  puts (s + d).utc.strftime('%Y-%m-%dT%H:%M:%SZ')
" -- "$start_utc" "$end_utc")"
part2_end="$(ruby -e "
  require 'time'
  s = Time.parse(ARGV[0])
  e = Time.parse(ARGV[1])
  d = (e - s) / 3
  puts (s + 2*d).utc.strftime('%Y-%m-%dT%H:%M:%SZ')
" -- "$start_utc" "$end_utc")"

part_stats() {
  local csv="$1"
  local from="$2"
  local to="$3"
  awk -F',' -v from="$from" -v to="$to" '
    NR==1 { next }
    $4=="FILLED" && $1 >= from && $1 < to {
      orders++; sum+=$9
      if ($9>0) win++; else if ($9<0) loss++; else flat++
    }
    END {
      o=orders+0; w=win+0; l=loss+0; f=flat+0
      wr = (o>0) ? (w/o*100) : 0
      printf "%d %d %d %d %.4f %.2f", o, w, l, f, sum+0, wr
    }
  ' "$csv"
}

echo "=== RAPPORT PNL 3 PARTIES ==="
echo "Fenetre: $start_utc -> $end_utc"
echo

for part in 1 2 3; do
  case $part in
    1) from="$start_utc"; to="$part1_end" ;;
    2) from="$part1_end"; to="$part2_end" ;;
    3) from="$part2_end"; to="$end_utc" ;;
  esac

  a=($(part_stats "$ALPHA_CSV" "$from" "$to"))
  b=($(part_stats "$BETA_CSV" "$from" "$to"))

  tot_o=$((${a[0]:-0} + ${b[0]:-0}))
  tot_w=$((${a[1]:-0} + ${b[1]:-0}))
  tot_l=$((${a[2]:-0} + ${b[2]:-0}))
  tot_f=$((${a[3]:-0} + ${b[3]:-0}))
  tot_n=$(awk -v a="${a[4]:-0}" -v b="${b[4]:-0}" 'BEGIN {printf "%.4f", a+b}')
  tot_wr=$(awk -v o="$tot_o" -v w="$tot_w" 'BEGIN {printf "%.2f", (o>0)?(w/o*100):0}')

  echo "PARTIE_$part"
  echo "  ALPHA orders=${a[0]:-0} win=${a[1]:-0} loss=${a[2]:-0} flat=${a[3]:-0} winrate=${a[5]:-0.00} net=${a[4]:-0}"
  echo "  BETA orders=${b[0]:-0} win=${b[1]:-0} loss=${b[2]:-0} flat=${b[3]:-0} winrate=${b[5]:-0.00} net=${b[4]:-0}"
  echo "  TOTAL orders=$tot_o win=$tot_w loss=$tot_l flat=$tot_f winrate=$tot_wr net=$tot_n"
  echo
done
