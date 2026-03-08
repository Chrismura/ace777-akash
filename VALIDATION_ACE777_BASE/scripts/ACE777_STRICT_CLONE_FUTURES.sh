#!/usr/bin/env bash
set -euo pipefail

# ACE777 STRICT CLONE FUTURES
# Clone decisionnel strict (radar + structure + tactic + soft-anomaly),
# transposé sur tuyaux Futures Testnet.

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"

BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
SYMBOL="${SYMBOL:-BTCUSDT}"
LEVERAGE="${LEVERAGE:-5}"
BUY_USDT="${BUY_USDT:-500}"
CYCLES="${CYCLES:-999999}"
SLEEP_SEC="${SLEEP_SEC:-1}"
POLL_SEC="${POLL_SEC:-0.5}"
MOMENTUM_SLEEP_SEC="${MOMENTUM_SLEEP_SEC:-1}"
RECV_WINDOW="${RECV_WINDOW:-60000}"
STOP_FILE="${STOP_FILE:-STOP}"
LOG_FILE="${LOG_FILE:-ACE777_STRICT_CLONE_FUTURES.csv}"
ENABLE_ORDERS="${ENABLE_ORDERS:-TRUE}"
FORCE_ENTRY_SIDE="${FORCE_ENTRY_SIDE:-AUTO}"   # AUTO | BUY | SELL
POSITION_SIDE="${POSITION_SIDE:-BOTH}"         # BOTH | LONG | SHORT

# Core strategy controls (baseline 7h style)
MIN_PROFIT_BPS="${MIN_PROFIT_BPS:-15}"
STOP_LOSS_BPS="${STOP_LOSS_BPS:-10}"
MAX_HOLD_SEC="${MAX_HOLD_SEC:-150}"
MIN_HOLD_SEC="${MIN_HOLD_SEC:-15}"
TRAIL_ARM_BPS="${TRAIL_ARM_BPS:-5}"
TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-3}"
USE_TRAILING="${USE_TRAILING:-1}"

# Radar / structure / tactic
RADAR_GATE="${RADAR_GATE:-TRUE}"
RADAR_MIN_CONF="${RADAR_MIN_CONF:-0.30}"
RADAR_MIN_MOM_BPS="${RADAR_MIN_MOM_BPS:-0.01}"
RADAR_DIR_BPS="${RADAR_DIR_BPS:-0.20}"
RADAR_MAX_SPREAD_BPS="${RADAR_MAX_SPREAD_BPS:-8}"
MOMENTUM_THRESHOLD="${MOMENTUM_THRESHOLD:-${MOMENTUM_THRESHOLD_BPS:-0.01}}"
TREND_FILTER="${TREND_FILTER:-TRUE}"
STRUCTURE_LOOKBACK_MIN="${STRUCTURE_LOOKBACK_MIN:-3}"
ENTRY_SIGNAL="${ENTRY_SIGNAL:-CROSSOVER}"

# Soft anomaly
ANOMALY_SOFT_MODE="${ANOMALY_SOFT_MODE:-TRUE}"
ANOMALY_TICK_BPS="${ANOMALY_TICK_BPS:-40}"
ANOMALY_PNL_USDT="${ANOMALY_PNL_USDT:-0.05}"
SOFT_COOLDOWN_CYCLES="${SOFT_COOLDOWN_CYCLES:-3}"
SOFT_MASS_FACTOR="${SOFT_MASS_FACTOR:-0.5}"
SOFT_STOP_LOSS_BPS="${SOFT_STOP_LOSS_BPS:-7}"
SOFT_TRAIL_GIVEBACK_BPS="${SOFT_TRAIL_GIVEBACK_BPS:-3}"
MIN_HOLD_FOR_ANOMALY="${MIN_HOLD_FOR_ANOMALY:-3}"
LEVERAGE_ANOMALY_MULT="${LEVERAGE_ANOMALY_MULT:-0.5}"
SOFT_NEUTRAL_HOLD_SEC="${SOFT_NEUTRAL_HOLD_SEC:-60}"
NEUTRAL_PNL_MIN_BPS="${NEUTRAL_PNL_MIN_BPS:--1}"
NEUTRAL_PNL_MAX_BPS="${NEUTRAL_PNL_MAX_BPS:-5}"
DYNAMIC_SIZING_ENABLED="${DYNAMIC_SIZING_ENABLED:-TRUE}"
DYNAMIC_SIZE_CONF_LOW="${DYNAMIC_SIZE_CONF_LOW:-0.15}"
DYNAMIC_SIZE_CONF_HIGH="${DYNAMIC_SIZE_CONF_HIGH:-0.25}"
DYNAMIC_SIZE_WEAK_FACTOR="${DYNAMIC_SIZE_WEAK_FACTOR:-0.5}"

# Fatigue
CALORIE_EFFICIENCY_EXIT="${CALORIE_EFFICIENCY_EXIT:-TRUE}"
STALL_THRESHOLD_BPS_PER_SEC="${STALL_THRESHOLD_BPS_PER_SEC:-0.1}"
FATIGUE_CONFIRMATIONS="${FATIGUE_CONFIRMATIONS:-20}"

if [[ "$BASE_URL" != *"testnet.binancefuture.com"* ]]; then
  echo "Abort: BASE_URL must be Futures Testnet."
  exit 1
fi

if [ ! -f "$LOG_FILE" ]; then
  echo "ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg" > "$LOG_FILE"
fi

now_ms() { ruby -e 'puts (Time.now.to_f * 1000).to_i'; }
now_sec() { ruby -e 'puts Time.now.to_i'; }

sign() {
  local q="$1"
  printf '%s' "$q" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256
}

json_get() {
  local json="$1" key="$2"
  ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; v=j[ARGV[0]]; print(v.nil? ? "" : v)' "$key" <<< "$json"
}

as_num() { ruby -e 'n=(Float(ARGV[0]) rescue 0.0); printf("%.8f", n)' -- "$1"; }
abs_num() { ruby -e 'x=(Float(ARGV[0]) rescue 0.0); printf("%.8f", x.abs)' -- "$1"; }
num_add() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a+b)' -- "$1" "$2"; }
num_sub() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a-b)' -- "$1" "$2"; }
num_mul() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a*b)' -- "$1" "$2"; }
num_div() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 1.0); printf("%.8f", b==0.0 ? 0.0 : a/b)' -- "$1" "$2"; }
num_gt() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a>b ? 0 : 1)' -- "$1" "$2"; }
num_ge() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a>=b ? 0 : 1)' -- "$1" "$2"; }
num_lt() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a<b ? 0 : 1)' -- "$1" "$2"; }
num_le() { ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a<=b ? 0 : 1)' -- "$1" "$2"; }

bps_change() {
  local base="$1" px="$2"
  ruby -e 'b=(Float(ARGV[0]) rescue 0.0); p=(Float(ARGV[1]) rescue 0.0); out=(b==0.0 ? 0.0 : ((p-b)/b)*10000.0); printf("%.8f", out)' -- "$base" "$px"
}

public_get() { curl -sS --connect-timeout 10 --max-time 20 "$BASE_URL$1"; }

private_post() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 10 --max-time 25 -X POST -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BASE_URL$path?$q&signature=$sig"
}

trend_bps_from_klines() {
  local json="$1"
  ruby -rjson -e '
    arr=JSON.parse(STDIN.read) rescue []
    if !arr.is_a?(Array) || arr.empty?
      print "0"; exit 0
    end
    first=arr.first; last=arr.last
    op=(first[1].to_f rescue 0.0); cl=(last[4].to_f rescue 0.0)
    if op <= 0.0 then print "0" else printf("%.8f", ((cl-op)/op)*10000.0) end
  ' <<< "$json"
}

floor_step_qty() {
  ruby -e '
    q=(Float(ARGV[0]) rescue 0.0); s=(Float(ARGV[1]) rescue 0.001)
    s=0.001 if s <= 0.0
    out=((q/s).floor)*s
    printf("%.8f", out)
  ' -- "$1" "$2"
}

symbol_filters() {
  local ex step min
  ex="$(public_get "/fapi/v1/exchangeInfo?symbol=$SYMBOL" || true)"
  step="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; s=(j["symbols"]||[])[0]||{}; f=(s["filters"]||[]).find{|x| x["filterType"]=="LOT_SIZE"}||{}; print(f["stepSize"] || "0.001")' <<< "$ex")"
  min="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; s=(j["symbols"]||[])[0]||{}; f=(s["filters"]||[]).find{|x| x["filterType"]=="LOT_SIZE"}||{}; print(f["minQty"] || "0.001")' <<< "$ex")"
  printf '%s,%s' "$step" "$min"
}

check_radar() {
  local mom_bps="$1" spread_bps="$2"
  radar_direction="long"; radar_reason="radar_off"; radar_conf="0.5"; radar_allow="true"
  if [ "$RADAR_GATE" = "TRUE" ]; then
    radar_out="$(ruby "./radar_gate.rb" \
      --mom-bps "$mom_bps" \
      --spread-bps "$spread_bps" \
      --min-conf "$RADAR_MIN_CONF" \
      --min-mom-bps "$RADAR_MIN_MOM_BPS" \
      --dir-bps "$RADAR_DIR_BPS" \
      --max-spread-bps "$RADAR_MAX_SPREAD_BPS")"
    radar_allow="$(json_get "$radar_out" "allow")"
    radar_direction="$(json_get "$radar_out" "direction")"
    radar_reason="$(json_get "$radar_out" "reason")"
    radar_conf="$(json_get "$radar_out" "confidence")"
  fi
  [ "$radar_allow" = "true" ]
}

apply_dynamic_sizing() {
  local base_usdt="$1"
  local conf="${2:-0}"
  local out="$base_usdt"
  dynamic_size_note="full"
  if [ "$DYNAMIC_SIZING_ENABLED" = "TRUE" ]; then
    if ruby -e 'c=(Float(ARGV[0]) rescue 0.0); lo=(Float(ARGV[1]) rescue 0.15); hi=(Float(ARGV[2]) rescue 0.25); exit((c>=lo && c<=hi) ? 0 : 1)' -- "$conf" "$DYNAMIC_SIZE_CONF_LOW" "$DYNAMIC_SIZE_CONF_HIGH"; then
      out="$(num_mul "$base_usdt" "$DYNAMIC_SIZE_WEAK_FACTOR")"
      dynamic_size_note="weak_conf_half"
    elif ruby -e 'c=(Float(ARGV[0]) rescue 0.0); hi=(Float(ARGV[1]) rescue 0.25); exit(c>hi ? 0 : 1)' -- "$conf" "$DYNAMIC_SIZE_CONF_HIGH"; then
      out="$base_usdt"
      dynamic_size_note="strong_conf_full"
    fi
  fi
  cycle_buy_usdt="$out"
}

detect_soft_anomaly() {
  local tick_bps_abs="$1"
  local anomaly_tick_eff="$ANOMALY_TICK_BPS"
  cycle_buy_usdt="$BUY_USDT"
  cycle_stop_loss_bps="$STOP_LOSS_BPS"
  cycle_trail_giveback_bps="$TRAIL_GIVEBACK_BPS"
  cycle_soft_mode=0

  if num_gt "$LEVERAGE" "1"; then
    anomaly_tick_eff="$(num_mul "$ANOMALY_TICK_BPS" "$LEVERAGE_ANOMALY_MULT")"
  fi

  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && [ "$soft_cooldown_remaining" -gt 0 ]; then
    cycle_soft_mode=1
    cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
    cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
    cycle_trail_giveback_bps="$SOFT_TRAIL_GIVEBACK_BPS"
    soft_cooldown_remaining=$((soft_cooldown_remaining - 1))
  fi
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$tick_bps_abs" "$anomaly_tick_eff"; then
    cycle_soft_mode=1
    cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
    cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
    cycle_trail_giveback_bps="$SOFT_TRAIL_GIVEBACK_BPS"
    soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
    echo "Cycle $i SOFT anomaly mode ON | tick_bps=$tick_bps_abs > $anomaly_tick_eff"
  fi
}

echo "--- ACE777 STRICT CLONE FUTURES TESTNET ---"
echo "Symbol=$SYMBOL Leverage=$LEVERAGE BuyUSDT=$BUY_USDT Orders=$ENABLE_ORDERS"

ts="$(now_ms)"
q_lev="symbol=$SYMBOL&leverage=$LEVERAGE&timestamp=$ts&recvWindow=$RECV_WINDOW"
lev_resp="$(private_post "/fapi/v1/leverage" "$q_lev" || true)"
lev_code="$(json_get "$lev_resp" "code")"
if [ -n "$lev_code" ]; then
  echo "Abort leverage error: code=$lev_code msg=$(json_get "$lev_resp" "msg")"
  exit 1
fi

IFS=',' read -r lot_step lot_min <<< "$(symbol_filters)"
soft_cooldown_remaining=0
ok_count=0
dynamic_size_note="na"

for i in $(seq 1 "$CYCLES"); do
  dynamic_size_note="na"
  if [ -f "$STOP_FILE" ]; then
    echo "STOP file detected ($STOP_FILE). Stopping safely at cycle $i."
    break
  fi

  p1_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
  p1="$(as_num "$(json_get "$p1_resp" "price")")"
  sleep "$MOMENTUM_SLEEP_SEC"
  p2_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
  p2="$(as_num "$(json_get "$p2_resp" "price")")"
  mom_bps="$(bps_change "$p1" "$p2")"
  tick_bps_abs="$(abs_num "$mom_bps")"

  book_resp="$(public_get "/fapi/v1/ticker/bookTicker?symbol=$SYMBOL" || true)"
  bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"
  ask_px="$(as_num "$(json_get "$book_resp" "askPrice")")"
  spread_bps="0"
  if num_gt "$ask_px" "0"; then
    spread_bps="$(num_mul "$(num_div "$(num_sub "$ask_px" "$bid_px")" "$ask_px")" "10000")"
  fi

  structure_direction="neutral"
  structure_trend_bps="0"
  if [ "$TREND_FILTER" = "TRUE" ]; then
    limit=$((STRUCTURE_LOOKBACK_MIN + 1))
    tr="$(public_get "/fapi/v1/klines?symbol=$SYMBOL&interval=1m&limit=$limit" || true)"
    structure_trend_bps="$(trend_bps_from_klines "$tr")"
    if num_ge "$structure_trend_bps" "1"; then
      structure_direction="long"
    elif num_le "$structure_trend_bps" "-1"; then
      structure_direction="short"
    fi
  fi

  mom_direction="neutral"
  if num_ge "$mom_bps" "$MOMENTUM_THRESHOLD"; then
    mom_direction="long"
  elif num_le "$mom_bps" "-$MOMENTUM_THRESHOLD"; then
    mom_direction="short"
  fi

  if ! check_radar "$mom_bps" "$spread_bps"; then
    echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,radar_block,reason=$radar_reason conf=$radar_conf mom_bps=$mom_bps spread_bps=$spread_bps" >> "$LOG_FILE"
    echo "Cycle $i SKIP | radar blocked: reason=$radar_reason conf=$radar_conf"
    sleep "$SLEEP_SEC"
    continue
  fi

  if [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
    radar_direction="$structure_direction"
  fi
  if [ "$ENTRY_SIGNAL" = "CROSSOVER" ] && [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
    if [ "$mom_direction" != "neutral" ] && [ "$mom_direction" != "$structure_direction" ]; then
      echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,tactic_mismatch,mom=$mom_direction structure=$structure_direction" >> "$LOG_FILE"
      echo "Cycle $i SKIP | tactic mismatch mom=$mom_direction structure=$structure_direction"
      sleep "$SLEEP_SEC"
      continue
    fi
  fi

  detect_soft_anomaly "$tick_bps_abs"
  apply_dynamic_sizing "$cycle_buy_usdt" "$radar_conf"

  if [ "$ENABLE_ORDERS" != "TRUE" ]; then
    echo "$(date -u +%FT%TZ),$i,OBSERVE,NA,$p1,$p2,0,$mom_bps,0,observe_only,ok" >> "$LOG_FILE"
    echo "Cycle $i/$CYCLES OBSERVE | mom_bps=$mom_bps radar=$radar_direction"
    sleep "$SLEEP_SEC"
    continue
  fi

  side="BUY"; close_side="SELL"; signed_dir="1"
  if [ "$radar_direction" = "short" ] && num_le "$mom_bps" "-$MOMENTUM_THRESHOLD"; then
    side="SELL"; close_side="BUY"; signed_dir="-1"
  fi
  if [ "$FORCE_ENTRY_SIDE" = "BUY" ]; then
    side="BUY"; close_side="SELL"; signed_dir="1"
  elif [ "$FORCE_ENTRY_SIDE" = "SELL" ]; then
    side="SELL"; close_side="BUY"; signed_dir="-1"
  fi

  position_side_param=""
  if [ "$POSITION_SIDE" = "LONG" ] || [ "$POSITION_SIDE" = "SHORT" ]; then
    position_side_param="&positionSide=$POSITION_SIDE"
  fi

  raw_qty="$(num_div "$(num_mul "$cycle_buy_usdt" "$LEVERAGE")" "$p2")"
  qty="$(floor_step_qty "$raw_qty" "$lot_step")"
  if ! num_ge "$qty" "$lot_min"; then
    echo "$(date -u +%FT%TZ),$i,SKIP,$side,$p2,,$qty,0,0,qty_too_small,min=$lot_min" >> "$LOG_FILE"
    echo "Cycle $i SKIP | qty too small ($qty < $lot_min)"
    sleep "$SLEEP_SEC"
    continue
  fi

  ts="$(now_ms)"
  q_entry="symbol=$SYMBOL&side=$side&type=MARKET&quantity=$qty${position_side_param}&timestamp=$ts&recvWindow=$RECV_WINDOW"
  entry_resp="$(private_post "/fapi/v1/order" "$q_entry" || true)"
  entry_code="$(json_get "$entry_resp" "code")"
  if [ -n "$entry_code" ]; then
    msg="$(json_get "$entry_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,ENTRY_ERROR,$side,$p2,,$qty,0,0,entry_error,code=$entry_code msg=$msg" >> "$LOG_FILE"
    echo "Cycle $i ENTRY error: code=$entry_code msg=$msg"
    sleep "$SLEEP_SEC"
    continue
  fi

  entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"
  if ! num_gt "$entry_price" "0"; then entry_price="$p2"; fi

  reason="timeout"
  start_s="$(now_sec)"
  peak_bps="-999999.00000000"
  prev_bps=""
  prev_ts="$(now_sec)"
  fatigue_count=0
  slow_velocity_count=0
  current_bps="0"
  while true; do
    if [ -f "$STOP_FILE" ]; then reason="kill_switch"; break; fi
    now_s="$(now_sec)"
    hold_sec=$((now_s - start_s))
    if [ "$hold_sec" -ge "$MAX_HOLD_SEC" ]; then reason="timeout"; break; fi

    tick_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
    px="$(as_num "$(json_get "$tick_resp" "price")")"
    current_bps="$(num_mul "$(bps_change "$entry_price" "$px")" "$signed_dir")"
    if num_ge "$current_bps" "$peak_bps"; then peak_bps="$current_bps"; fi

    if [ "$CALORIE_EFFICIENCY_EXIT" = "TRUE" ] && [ "$hold_sec" -ge "$MIN_HOLD_SEC" ]; then
      now_tick="$(now_sec)"
      dt=$((now_tick - prev_ts)); [ "$dt" -le 0 ] && dt=1
      if [ -n "$prev_bps" ]; then
        delta_bps="$(num_sub "$current_bps" "$prev_bps")"
        vel_bps_s="$(num_div "$(abs_num "$delta_bps")" "$dt")"
        if num_lt "$vel_bps_s" "$STALL_THRESHOLD_BPS_PER_SEC"; then
          slow_velocity_count=$((slow_velocity_count + 1))
        else
          slow_velocity_count=0
        fi
        if [ "$slow_velocity_count" -ge "$FATIGUE_CONFIRMATIONS" ]; then
          fatigue_count=$((fatigue_count + 1))
          if [ "$fatigue_count" -ge "$FATIGUE_CONFIRMATIONS" ]; then
            reason="exit_fatigue"; break
          fi
        fi
      fi
      prev_bps="$current_bps"
      prev_ts="$now_tick"
    fi

    active_stop_loss_bps="$cycle_stop_loss_bps"
    active_trail_giveback_bps="$cycle_trail_giveback_bps"
    # Anti-panique: no anomaly-driven cut in the first few seconds.
    if [ "$cycle_soft_mode" -eq 1 ] && [ "$hold_sec" -lt "$MIN_HOLD_FOR_ANOMALY" ]; then
      active_stop_loss_bps="$STOP_LOSS_BPS"
      active_trail_giveback_bps="$TRAIL_GIVEBACK_BPS"
    fi
    # Neutral zone protection: do not let soft-anomaly cut too early.
    if [ "$cycle_soft_mode" -eq 1 ] && [ "$hold_sec" -lt "$SOFT_NEUTRAL_HOLD_SEC" ]; then
      if num_ge "$current_bps" "$NEUTRAL_PNL_MIN_BPS" && num_le "$current_bps" "$NEUTRAL_PNL_MAX_BPS"; then
        active_stop_loss_bps="$STOP_LOSS_BPS"
        active_trail_giveback_bps="$TRAIL_GIVEBACK_BPS"
      fi
    fi
    if num_le "$current_bps" "-$active_stop_loss_bps"; then reason="stop_loss"; break; fi
    if [ "$USE_TRAILING" = "1" ]; then
      if num_ge "$peak_bps" "$TRAIL_ARM_BPS"; then
        trail_floor="$(num_sub "$peak_bps" "$active_trail_giveback_bps")"
        if num_le "$current_bps" "$trail_floor"; then reason="trailing_stop"; break; fi
      fi
    else
      if num_ge "$current_bps" "$MIN_PROFIT_BPS"; then reason="target"; break; fi
    fi
    sleep "$POLL_SEC"
  done

  ts="$(now_ms)"
  if [ "$POSITION_SIDE" = "BOTH" ]; then
    q_exit="symbol=$SYMBOL&side=$close_side&type=MARKET&quantity=$qty&reduceOnly=true&timestamp=$ts&recvWindow=$RECV_WINDOW"
  else
    q_exit="symbol=$SYMBOL&side=$close_side&type=MARKET&quantity=$qty${position_side_param}&timestamp=$ts&recvWindow=$RECV_WINDOW"
  fi
  exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"
  exit_code="$(json_get "$exit_resp" "code")"
  if [ -n "$exit_code" ]; then
    msg="$(json_get "$exit_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,EXIT_ERROR,$side,$entry_price,,$qty,$current_bps,0,$reason,code=$exit_code msg=$msg" >> "$LOG_FILE"
    echo "Cycle $i EXIT error: code=$exit_code msg=$msg"
    sleep "$SLEEP_SEC"
    continue
  fi

  exit_price="$(as_num "$(json_get "$exit_resp" "avgPrice")")"
  if ! num_gt "$exit_price" "0"; then
    if [ -n "${px:-}" ] && num_gt "${px:-0}" "0"; then
      exit_price="$px"
    else
      exit_price="$p2"
    fi
  fi
  bps="$(num_mul "$(bps_change "$entry_price" "$exit_price")" "$signed_dir")"
  pct="$(num_div "$bps" "100")"
  pnl_usdt="$(num_mul "$(num_sub "$exit_price" "$entry_price")" "$(num_mul "$qty" "$signed_dir")")"
  anomaly_pnl_eff="$ANOMALY_PNL_USDT"
  if num_gt "$LEVERAGE" "1"; then
    anomaly_pnl_eff="$(num_mul "$ANOMALY_PNL_USDT" "$LEVERAGE_ANOMALY_MULT")"
  fi
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$(abs_num "$pnl_usdt")" "$anomaly_pnl_eff"; then
    soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
    echo "Cycle $i SOFT anomaly mode ON | pnl_abs=$(abs_num "$pnl_usdt") > $anomaly_pnl_eff"
  fi
  hold_done=$(( $(now_sec) - start_s ))
  echo "$(date -u +%FT%TZ),$i,$side,FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,radar=$radar_direction conf=$radar_conf size_note=$dynamic_size_note soft=$cycle_soft_mode pct=$pct" >> "$LOG_FILE"
  echo "Cycle $i/$CYCLES ORDER | side=$side qty=$qty reason=$reason hold=${hold_done}s bps=$bps pct=${pct}% pnl=$pnl_usdt conf=$radar_conf size=$dynamic_size_note"
  ok_count=$((ok_count + 1))
  sleep "$SLEEP_SEC"
done

echo
echo "Done."
echo "Log: $LOG_FILE"
echo "Successful order-cycles: $ok_count"
