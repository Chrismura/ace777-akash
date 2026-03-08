#!/usr/bin/env bash
set -euo pipefail

# V2 wrapper:
# - reinforces neutral-zone breathing before soft anomaly can cut
# - wider trailing giveback (less nervous)
# - keeps strict clone core and Futures pipes

cd /Users/christophe/ace777-test-day1

export TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-3}"
export SOFT_TRAIL_GIVEBACK_BPS="${SOFT_TRAIL_GIVEBACK_BPS:-3}"
export MIN_HOLD_FOR_ANOMALY="${MIN_HOLD_FOR_ANOMALY:-3}"
export SOFT_NEUTRAL_HOLD_SEC="${SOFT_NEUTRAL_HOLD_SEC:-60}"
export NEUTRAL_PNL_MIN_BPS="${NEUTRAL_PNL_MIN_BPS:--1}"
export NEUTRAL_PNL_MAX_BPS="${NEUTRAL_PNL_MAX_BPS:-5}"
export LEVERAGE_ANOMALY_MULT="${LEVERAGE_ANOMALY_MULT:-0.5}"
export BOT_LABEL="${BOT_LABEL:-$(basename "${LOG_FILE:-ACE777}")}"
export RUN_DURATION_SEC="${RUN_DURATION_SEC:-0}"
export RUN_START_EPOCH="${RUN_START_EPOCH:-$(date +%s)}"

# Prefix every live output line with UTC timestamp + bot label + elapsed.
bash ./ACE777_STRICT_CLONE_FUTURES.sh 2>&1 | while IFS= read -r line; do
  now_epoch="$(date +%s)"
  run_start_epoch="${RUN_START_EPOCH:-0}"
  run_duration_sec="${RUN_DURATION_SEC:-0}"
  case "$run_start_epoch" in ''|*[!0-9-]*) run_start_epoch=0 ;; esac
  case "$run_duration_sec" in ''|*[!0-9-]*) run_duration_sec=0 ;; esac
  elapsed=$((now_epoch - run_start_epoch))
  if [ "$run_duration_sec" -gt 0 ]; then
    rem=$((run_duration_sec - elapsed))
    if [ "$rem" -lt 0 ]; then rem=0; fi
    timer="r-${rem}s"
  else
    timer="r-0s"
  fi
  colored_line="$line"
  if [[ "$line" =~ pnl=([-+]?[0-9]*\.?[0-9]+) ]]; then
    pnl_val="${BASH_REMATCH[1]}"
    pnl_token="pnl=${pnl_val}"
    pnl_color="$(awk -v v="$pnl_val" 'BEGIN{ if (v>0) print "\033[32m"; else if (v<0) print "\033[31m"; else print "\033[33m" }')"
    pnl_reset=$'\033[0m'
    colored_token="${pnl_color}${pnl_token}${pnl_reset}"
    colored_line="${line/$pnl_token/$colored_token}"
  fi
  if [[ "$line" =~ hold=([0-9]+)s ]]; then
    hold_sec="${BASH_REMATCH[1]}"
    hold_token="hold=${hold_sec}s"
    hold_color="$(awk -v v="$hold_sec" 'BEGIN{ if (v>=120) print "\033[31m"; else if (v>=60) print "\033[33m"; else print "\033[36m" }')"
    hold_reset=$'\033[0m'
    colored_hold="${hold_color}${hold_token}${hold_reset}"
    colored_line="${colored_line/$hold_token/$colored_hold}"
  fi
  if [[ "$line" =~ tension=([-+]?[0-9]*\.?[0-9]+) ]]; then
    tension_val="${BASH_REMATCH[1]}"
    tension_color="$(awk -v v="$tension_val" 'BEGIN{ if (v>=1.0) print "\033[32m"; else if (v>=0.85) print "\033[33m"; else print "\033[91m" }')"
    tension_reset=$'\033[0m'
    colored_tension_val="${tension_color}${tension_val}${tension_reset}"
    colored_line="${colored_line/tension=${tension_val}/tension=${colored_tension_val}}"
  fi
  if [[ "$line" =~ Cycle[[:space:]]+([0-9]+) ]]; then
    cycle_num="${BASH_REMATCH[1]}"
    cycle_color=$'\033[94m'
    cycle_reset=$'\033[0m'
    colored_cycle_num="${cycle_color}${cycle_num}${cycle_reset}"
    colored_line="${colored_line/Cycle ${cycle_num}/Cycle ${colored_cycle_num}}"
  fi
  if [[ "$colored_line" == *"BUY"* || "$colored_line" == *"SELL"* ]]; then
    side_buy_color=$'\033[32m'
    side_sell_color=$'\033[31m'
    side_reset=$'\033[0m'
    colored_line="${colored_line//BUY/${side_buy_color}BUY${side_reset}}"
    colored_line="${colored_line//SELL/${side_sell_color}SELL${side_reset}}"
  fi
  if [[ "$colored_line" == *"X13"* || "$colored_line" == *"x13"* ]]; then
    x13_color=$'\033[35m'
    x13_reset=$'\033[0m'
    colored_line="${colored_line//X13/${x13_color}X13${x13_reset}}"
    colored_line="${colored_line//x13/${x13_color}x13${x13_reset}}"
  fi
  if [[ "$colored_line" == *"Leverage=13"* ]]; then
    lev13_color=$'\033[35m'
    lev13_reset=$'\033[0m'
    colored_line="${colored_line//Leverage=13/${lev13_color}Leverage=13${lev13_reset}}"
  fi
  ts_date="$(date -u +%Y-%m-%d)"
  ts_time="$(date -u +T%H:%M:%SZ)"
  ts_color=$'\033[36m'
  ts_reset=$'\033[0m'
  # Color only the time part, keep the date plain.
  colored_ts="${ts_date}${ts_color}${ts_time}${ts_reset}"
  colored_label="$BOT_LABEL"
  if [[ "$BOT_LABEL" == *"X13"* || "$BOT_LABEL" == *"x13"* ]]; then
    label_color=$'\033[35m'
    label_reset=$'\033[0m'
    colored_label="${colored_label//X13/${label_color}X13${label_reset}}"
    colored_label="${colored_label//x13/${label_color}x13${label_reset}}"
  fi
  printf '%s [%s] %s | %s\n' "$colored_ts" "$colored_label" "$colored_line" "$timer"
done
