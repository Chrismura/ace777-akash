#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# === V8.6 FORTRESS ===
# Correctif 4061 + Masse 1.618->2.5 + Reset PnL

duration_input="${RUN_DURATION:-07:30:00}"
while [ "$#" -gt 0 ]; do
  case "$1" in
    --duration)
      shift
      duration_input="${1:-07:30:00}"
      ;;
    *)
      echo "Usage: $0 [--duration HH:MM:SS|seconds]"
      exit 1
      ;;
  esac
  shift || true
done

duration_sec="$(ruby -e '
  s=ARGV[0].to_s.strip
  out=nil
  if s =~ /\A\d+\z/
    out=s.to_i
  elsif s =~ /\A(\d+):([0-5]\d):([0-5]\d)\z/
    h=$1.to_i; m=$2.to_i; sec=$3.to_i
    out=h*3600 + m*60 + sec
  end
  if out.nil? || out <= 0
    STDERR.puts("Invalid duration: #{s} (expected HH:MM:SS or seconds)")
    exit 1
  end
  puts out
' -- "$duration_input")"

duration_tag="$(ruby -e '
  sec=(Integer(ARGV[0]) rescue 27000)
  h=sec/3600
  m=(sec%3600)/60
  printf("%dH%02d", h, m)
' -- "$duration_sec")"

export RUN_SEC_OVERRIDE="$duration_sec"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-MASTER_BASE_V8_6_FORTRESS_${duration_tag}}"

# Signal & risque
export MOMENTUM_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
export WALL_DROP_THRESHOLD="${WALL_DROP_THRESHOLD:-0.065}"   # 6.5%
export GLOBAL_STOP_USDT="${GLOBAL_STOP_USDT:--45.00}"
export ALPHA_REVENGE_MULT="${ALPHA_REVENGE_MULT:-2.5}"
export STOP_LOSS_BPS="${STOP_LOSS_BPS:-16}"
export FLUID_EXIT_SENSITIVITY="${FLUID_EXIT_SENSITIVITY:-1.0}"

# Correctifs hedge mode (4061)
export POSITION_SIDE_STRICT=TRUE
export BINANCE_HEDGE_MODE=TRUE

# Masse (muscle)
export BUY_USDT_BETA="${BUY_USDT_BETA:-200}"
export BUY_USDT_ALPHA="${BUY_USDT_ALPHA:-800}"

# Pilotage runtime
export RUN_STATE_ENABLED=TRUE
export RUN_STATE_LINK_TOTAL_PNL=TRUE

# Sensibilite sorties fluides (plus grand = plus nerveux)
fluid_brake="$(ruby -e 's=(Float(ARGV[0]) rescue 1.0); s=1.0 if s<=0; printf("%.8f", 0.02/s)' -- "$FLUID_EXIT_SENSITIVITY")"
fluid_invert="$(ruby -e 's=(Float(ARGV[0]) rescue 1.0); s=1.0 if s<=0; printf("%.8f", -0.02/s)' -- "$FLUID_EXIT_SENSITIVITY")"
export FLUID_EXIT_BRAKE_BPS_S="$fluid_brake"
export FLUID_EXIT_INVERT_BPS_S="$fluid_invert"

echo "=== V8.6 FORTRESS === MOM=${MOMENTUM_THRESHOLD} WALL_DROP=${WALL_DROP_THRESHOLD} GLOBAL_STOP=${GLOBAL_STOP_USDT}"

# Base 8.5 (la base fait deja le reset duo_session/duo_state au demarrage)
exec ./launch_test_master_base_v8_5_impact.sh
