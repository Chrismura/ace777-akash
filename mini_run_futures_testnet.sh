#!/usr/bin/env bash
set -euo pipefail

# ACE777 - Futures Testnet runner (observe + optional real testnet orders)

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"

BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
SYMBOL="${SYMBOL:-BTCUSDT}"
LEVERAGE="${LEVERAGE:-2}"
BUY_USDT="${BUY_USDT:-100}"
CYCLES="${CYCLES:-10}"
SLEEP_SEC="${SLEEP_SEC:-2}"
HOLD_SEC="${HOLD_SEC:-20}"
MAX_HOLD_SEC="${MAX_HOLD_SEC:-120}"
MIN_PROFIT_BPS="${MIN_PROFIT_BPS:-15}"
STOP_LOSS_BPS="${STOP_LOSS_BPS:-10}"
RECV_WINDOW="${RECV_WINDOW:-60000}"
ENABLE_ORDERS="${ENABLE_ORDERS:-FALSE}"   # FALSE = observe only, TRUE = place real testnet orders
LOG_FILE="${LOG_FILE:-futures_testnet_log.csv}"
STOP_FILE="${STOP_FILE:-STOP}"

# Clone decision core from spot baseline (radar + structure + tactic + soft-anomaly)
MOMENTUM_THRESHOLD_BPS="${MOMENTUM_THRESHOLD_BPS:-0.01}"
TREND_FILTER="${TREND_FILTER:-FALSE}"
STRUCTURE_LOOKBACK_MIN="${STRUCTURE_LOOKBACK_MIN:-3}"
ENTRY_SIGNAL="${ENTRY_SIGNAL:-CROSSOVER}"
RADAR_GATE="${RADAR_GATE:-TRUE}"
RADAR_MIN_CONF="${RADAR_MIN_CONF:-0.30}"
RADAR_MIN_MOM_BPS="${RADAR_MIN_MOM_BPS:-0.01}"
RADAR_DIR_BPS="${RADAR_DIR_BPS:-0.20}"
RADAR_MAX_SPREAD_BPS="${RADAR_MAX_SPREAD_BPS:-8}"
ANOMALY_SOFT_MODE="${ANOMALY_SOFT_MODE:-TRUE}"
ANOMALY_TICK_BPS="${ANOMALY_TICK_BPS:-40}"
ANOMALY_PNL_USDT="${ANOMALY_PNL_USDT:-0.05}"
SOFT_COOLDOWN_CYCLES="${SOFT_COOLDOWN_CYCLES:-3}"
SOFT_MASS_FACTOR="${SOFT_MASS_FACTOR:-0.5}"
SOFT_STOP_LOSS_BPS="${SOFT_STOP_LOSS_BPS:-7}"

if [[ "$BASE_URL" != *"testnet.binancefuture.com"* ]]; then
  echo "Abort: BASE_URL must be Binance Futures TESTNET."
  exit 1
fi

if [ ! -f "$LOG_FILE" ]; then
  echo "ts,cycle,mode,entry_side,entry_price,exit_price,qty,bps,pnl_usdt,reason,msg" > "$LOG_FILE"
fi

now_ms() {
  ruby -e 'puts (Time.now.to_f * 1000).to_i'
}

sign() {
  local q="$1"
  printf '%s' "$q" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256
}

json_get() {
  local json="$1"
  local key="$2"
  ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; v=j[ARGV[0]]; print(v.nil? ? "" : v)' "$key" <<< "$json"
}

as_num() {
  local v="$1"
  ruby -e 'n=(Float(ARGV[0]) rescue 0.0); printf("%.8f", n)' -- "$v"
}

num_gt() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a>b ? 0 : 1)' -- "$1" "$2"
}

num_ge() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a>=b ? 0 : 1)' -- "$1" "$2"
}

num_le() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a<=b ? 0 : 1)' -- "$1" "$2"
}

bps_change() {
  local base="$1"
  local px="$2"
  ruby -e 'b=(Float(ARGV[0]) rescue 0.0); p=(Float(ARGV[1]) rescue 0.0); out=(b==0.0 ? 0.0 : ((p-b)/b)*10000.0); printf("%.8f", out)' -- "$base" "$px"
}

num_div() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 1.0); printf("%.8f", b==0.0 ? 0.0 : a/b)' -- "$1" "$2"
}

num_mul() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a*b)' -- "$1" "$2"
}

num_sub() {
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a-b)' -- "$1" "$2"
}

floor_step_qty() {
  ruby -e '
    q=(Float(ARGV[0]) rescue 0.0)
    s=(Float(ARGV[1]) rescue 0.001)
    s=0.001 if s <= 0.0
    out=((q/s).floor)*s
    printf("%.8f", out)
  ' -- "$1" "$2"
}

public_get() {
  local path_q="$1"
  curl -sS --connect-timeout 10 --max-time 20 "$BASE_URL$path_q"
}

private_post() {
  local path="$1"
  local q="$2"
  local sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 10 --max-time 25 -X POST \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}

symbol_filters() {
  local ex step min
  ex="$(public_get "/fapi/v1/exchangeInfo?symbol=$SYMBOL" || true)"
  step="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; s=(j["symbols"]||[])[0]||{}; f=(s["filters"]||[]).find{|x| x["filterType"]=="LOT_SIZE"}||{}; print(f["stepSize"] || "0.001")' <<< "$ex")"
  min="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; s=(j["symbols"]||[])[0]||{}; f=(s["filters"]||[]).find{|x| x["filterType"]=="LOT_SIZE"}||{}; print(f["minQty"] || "0.001")' <<< "$ex")"
  printf '%s,%s' "$step" "$min"
}

trend_bps_from_klines() {
  local json="$1"
  ruby -rjson -e '
    arr=JSON.parse(STDIN.read) rescue []
    if !arr.is_a?(Array) || arr.empty?
      print "0"
      exit 0
    end
    first=arr.first
    last=arr.last
    op=(first[1].to_f rescue 0.0)
    cl=(last[4].to_f rescue 0.0)
    if op <= 0.0
      print "0"
    else
      printf("%.8f", ((cl-op)/op)*10000.0)
    end
  ' <<< "$json"
}

abs_num() {
  ruby -e 'x=(Float(ARGV[0]) rescue 0.0); printf("%.8f", x.abs)' -- "$1"
}

echo "--- ACE777 FUTURES TESTNET ---"
echo "Symbol=$SYMBOL Leverage=$LEVERAGE BuyUSDT=$BUY_USDT Orders=$ENABLE_ORDERS"

# Set leverage once
ts="$(now_ms)"
q_lev="symbol=$SYMBOL&leverage=$LEVERAGE&timestamp=$ts&recvWindow=$RECV_WINDOW"
lev_resp="$(private_post "/fapi/v1/leverage" "$q_lev" || true)"
lev_code="$(json_get "$lev_resp" "code")"
if [ -n "$lev_code" ]; then
  echo "Abort leverage error: code=$lev_code msg=$(json_get "$lev_resp" "msg")"
  exit 1
fi

IFS=',' read -r lot_step lot_min <<< "$(symbol_filters)"
ok_count=0
soft_cooldown_remaining=0

for i in $(seq 1 "$CYCLES"); do
  if [ -f "$STOP_FILE" ]; then
    echo "STOP file detected ($STOP_FILE). Stopping safely at cycle $i."
    break
  fi

  p1_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
  p1="$(as_num "$(json_get "$p1_resp" "price")")"
  sleep "$SLEEP_SEC"
  p2_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
  p2="$(as_num "$(json_get "$p2_resp" "price")")"
  mom_bps="$(bps_change "$p1" "$p2")"
  mom_abs="$(abs_num "$mom_bps")"
  mom_direction="neutral"
  if num_ge "$mom_bps" "$MOMENTUM_THRESHOLD_BPS"; then
    mom_direction="long"
  elif num_le "$mom_bps" "-$MOMENTUM_THRESHOLD_BPS"; then
    mom_direction="short"
  fi

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
    k_resp="$(public_get "/fapi/v1/klines?symbol=$SYMBOL&interval=1m&limit=$limit" || true)"
    structure_trend_bps="$(trend_bps_from_klines "$k_resp")"
    if num_ge "$structure_trend_bps" "1"; then
      structure_direction="long"
    elif num_le "$structure_trend_bps" "-1"; then
      structure_direction="short"
    fi
  fi

  radar_direction="$mom_direction"
  radar_reason="radar_off"
  radar_conf="0.5"
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
    if [ "$radar_allow" != "true" ]; then
      echo "$(date -u +%FT%TZ),$i,SKIP,,,,,,0,radar_block,reason=$radar_reason conf=$radar_conf mom_bps=$mom_bps spread_bps=$spread_bps" >> "$LOG_FILE"
      echo "Cycle $i SKIP | radar blocked: reason=$radar_reason conf=$radar_conf"
      sleep "$SLEEP_SEC"
      continue
    fi
  fi

  if [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
    radar_direction="$structure_direction"
  fi
  if [ "$ENTRY_SIGNAL" = "CROSSOVER" ] && [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
    if [ "$mom_direction" != "neutral" ] && [ "$mom_direction" != "$structure_direction" ]; then
      echo "$(date -u +%FT%TZ),$i,SKIP,,,,,,0,tactic_mismatch,mom=$mom_direction structure=$structure_direction trend_bps=$structure_trend_bps" >> "$LOG_FILE"
      echo "Cycle $i SKIP | tactic mismatch mom=$mom_direction structure=$structure_direction"
      sleep "$SLEEP_SEC"
      continue
    fi
  fi

  if [ "$ENABLE_ORDERS" != "TRUE" ]; then
    echo "$(date -u +%FT%TZ),$i,OBSERVE,,,,$mom_bps,,,observe_only,mom_bps=$mom_bps p1=$p1 p2=$p2" >> "$LOG_FILE"
    echo "Cycle $i/$CYCLES OBSERVE | p1=$p1 p2=$p2 mom_bps=$mom_bps"
    continue
  fi

  side="BUY"
  close_side="SELL"
  signed_dir="1"
  if [ "$radar_direction" = "short" ] && num_le "$mom_bps" "-$MOMENTUM_THRESHOLD_BPS"; then
    side="SELL"
    close_side="BUY"
    signed_dir="-1"
  fi

  cycle_stop_loss_bps="$STOP_LOSS_BPS"
  cycle_buy_usdt="$BUY_USDT"
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && [ "$soft_cooldown_remaining" -gt 0 ]; then
    cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
    cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
    soft_cooldown_remaining=$((soft_cooldown_remaining - 1))
  fi
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$mom_abs" "$ANOMALY_TICK_BPS"; then
    cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
    cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
    soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
    echo "Cycle $i SOFT anomaly mode ON | tick_bps=$mom_abs > $ANOMALY_TICK_BPS"
  fi

  # Futures sizing uses notional exposure = margin * leverage.
  raw_qty="$(num_div "$(num_mul "$cycle_buy_usdt" "$LEVERAGE")" "$p2")"
  qty="$(floor_step_qty "$raw_qty" "$lot_step")"
  if ! num_ge "$qty" "$lot_min"; then
    echo "$(date -u +%FT%TZ),$i,ORDER,$side,$p2,,$qty,,,skip_qty,qty<$lot_min" >> "$LOG_FILE"
    echo "Cycle $i SKIP | qty too small ($qty < $lot_min)"
    continue
  fi

  ts="$(now_ms)"
  q_entry="symbol=$SYMBOL&side=$side&type=MARKET&quantity=$qty&timestamp=$ts&recvWindow=$RECV_WINDOW"
  entry_resp="$(private_post "/fapi/v1/order" "$q_entry" || true)"
  entry_code="$(json_get "$entry_resp" "code")"
  if [ -n "$entry_code" ]; then
    msg="$(json_get "$entry_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,ORDER,$side,$p2,,$qty,,,entry_error,code=$entry_code msg=$msg" >> "$LOG_FILE"
    echo "Cycle $i ENTRY error: code=$entry_code msg=$msg"
    continue
  fi

  entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"
  if ! num_gt "$entry_price" "0"; then
    entry_price="$p2"
  fi

  reason="timeout"
  start_s="$(date +%s)"
  last_px="$entry_price"
  while true; do
    if [ -f "$STOP_FILE" ]; then
      reason="kill_switch"
      break
    fi
    now_s="$(date +%s)"
    held=$((now_s - start_s))
    if [ "$held" -ge "$MAX_HOLD_SEC" ]; then
      reason="timeout"
      break
    fi
    tick_resp="$(public_get "/fapi/v1/ticker/price?symbol=$SYMBOL" || true)"
    last_px="$(as_num "$(json_get "$tick_resp" "price")")"
    move_bps="$(bps_change "$entry_price" "$last_px")"
    signed_bps="$(num_mul "$move_bps" "$signed_dir")"
    if num_ge "$signed_bps" "$MIN_PROFIT_BPS"; then
      reason="target"
      break
    fi
    if num_le "$signed_bps" "-$cycle_stop_loss_bps"; then
      reason="stop_loss"
      break
    fi
    if [ "$held" -ge "$HOLD_SEC" ]; then
      reason="hold_cycle"
      break
    fi
    sleep 1
  done

  ts="$(now_ms)"
  q_exit="symbol=$SYMBOL&side=$close_side&type=MARKET&quantity=$qty&reduceOnly=true&timestamp=$ts&recvWindow=$RECV_WINDOW"
  exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"
  exit_code="$(json_get "$exit_resp" "code")"
  if [ -n "$exit_code" ]; then
    msg="$(json_get "$exit_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,ORDER,$side,$entry_price,,$qty,,,exit_error,code=$exit_code msg=$msg" >> "$LOG_FILE"
    echo "Cycle $i EXIT error: code=$exit_code msg=$msg"
    continue
  fi

  exit_price="$(as_num "$(json_get "$exit_resp" "avgPrice")")"
  if ! num_gt "$exit_price" "0"; then
    exit_price="$last_px"
  fi
  bps="$(num_mul "$(bps_change "$entry_price" "$exit_price")" "$signed_dir")"
  pct="$(num_div "$bps" "100")"
  pnl_usdt="$(num_mul "$(num_sub "$exit_price" "$entry_price")" "$(num_mul "$qty" "$signed_dir")")"
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$(abs_num "$pnl_usdt")" "$ANOMALY_PNL_USDT"; then
    soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
  fi
  echo "$(date -u +%FT%TZ),$i,ORDER,$side,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,ok pct=$pct" >> "$LOG_FILE"
  echo "Cycle $i/$CYCLES ORDER | side=$side qty=$qty reason=$reason bps=$bps pct=${pct}% pnl=$pnl_usdt"
  ok_count=$((ok_count + 1))
done

echo
echo "Done."
echo "Log: $LOG_FILE"
echo "Successful order-cycles: $ok_count"
