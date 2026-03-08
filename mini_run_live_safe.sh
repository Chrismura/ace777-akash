#!/usr/bin/env bash
set -euo pipefail

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"
: "${BINANCE_BASE_URL:=https://testnet.binance.vision}"

SYMBOL="${SYMBOL:-BTCUSDT}"
BUY_USDT="${BUY_USDT:-12}"
CYCLES="${CYCLES:-10}"
SLEEP_SEC="${SLEEP_SEC:-10}"
RECV_WINDOW="${RECV_WINDOW:-60000}"
MAX_ERRORS="${MAX_ERRORS:-3}"
RETRY_MAX="${RETRY_MAX:-3}"
RETRY_DELAY_SEC="${RETRY_DELAY_SEC:-2}"
STOP_FILE="${STOP_FILE:-STOP}"
LOG_FILE="${LOG_FILE:-mini_run_safe_log.csv}"

if [ ! -f "$LOG_FILE" ]; then
  echo "ts,cycle,side,status,orderId,executedQty,cumQuote,pnl,msg" > "$LOG_FILE"
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
  ruby -e 'v=ARGV[0]; n=(Float(v) rescue 0.0); printf("%.8f", n)' -- "$v"
}

num_sub() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a-b)' -- "$a" "$b"
}

num_add() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a+b)' -- "$a" "$b"
}

private_post_retry() {
  local path="$1"
  local q="$2"
  local sig
  local out=""
  local attempt

  sig="$(sign "$q")"

  for attempt in $(seq 1 "$RETRY_MAX"); do
    out="$(curl -sS --connect-timeout 10 --max-time 25 -X POST \
      -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
      "$BINANCE_BASE_URL$path?$q&signature=$sig" || true)"
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
    sleep "$RETRY_DELAY_SEC"
  done

  return 1
}

error_count=0
ok_cycles=0
total_pnl="0.00000000"
requested_cycles="$CYCLES"

for i in $(seq 1 "$requested_cycles"); do
  if [ -f "$STOP_FILE" ]; then
    echo "STOP file detected ($STOP_FILE). Stopping safely at cycle $i."
    break
  fi

  ts="$(now_ms)"
  q_buy="symbol=$SYMBOL&side=BUY&type=MARKET&quoteOrderQty=$BUY_USDT&timestamp=$ts&recvWindow=$RECV_WINDOW"
  if ! buy_resp="$(private_post_retry "/api/v3/order" "$q_buy")"; then
    error_count=$((error_count + 1))
    echo "$(date -u +%FT%TZ),$i,BUY,ERROR,,,,,network_or_timeout" >> "$LOG_FILE"
    echo "Cycle $i BUY failed (network/timeout). errors=$error_count/$MAX_ERRORS"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then
      echo "Max errors reached. Stopping."
      break
    fi
    sleep "$SLEEP_SEC"
    continue
  fi

  buy_code="$(json_get "$buy_resp" "code")"
  if [ -n "$buy_code" ]; then
    error_count=$((error_count + 1))
    buy_msg="$(json_get "$buy_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,BUY,ERROR,,,,,code=$buy_code msg=$buy_msg" >> "$LOG_FILE"
    echo "Cycle $i BUY API error: code=$buy_code msg=$buy_msg"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then
      echo "Max errors reached. Stopping."
      break
    fi
    sleep "$SLEEP_SEC"
    continue
  fi

  buy_qty="$(json_get "$buy_resp" "executedQty")"
  buy_id="$(json_get "$buy_resp" "orderId")"
  buy_quote="$(as_num "$(json_get "$buy_resp" "cummulativeQuoteQty")")"
  echo "$(date -u +%FT%TZ),$i,BUY,FILLED,$buy_id,$buy_qty,$buy_quote,,ok" >> "$LOG_FILE"

  ts="$(now_ms)"
  q_sell="symbol=$SYMBOL&side=SELL&type=MARKET&quantity=$buy_qty&timestamp=$ts&recvWindow=$RECV_WINDOW"
  if ! sell_resp="$(private_post_retry "/api/v3/order" "$q_sell")"; then
    error_count=$((error_count + 1))
    echo "$(date -u +%FT%TZ),$i,SELL,ERROR,,,,,network_or_timeout" >> "$LOG_FILE"
    echo "Cycle $i SELL failed (network/timeout). errors=$error_count/$MAX_ERRORS"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then
      echo "Max errors reached. Stopping."
      break
    fi
    sleep "$SLEEP_SEC"
    continue
  fi

  sell_code="$(json_get "$sell_resp" "code")"
  if [ -n "$sell_code" ]; then
    error_count=$((error_count + 1))
    sell_msg="$(json_get "$sell_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,SELL,ERROR,,,,,code=$sell_code msg=$sell_msg" >> "$LOG_FILE"
    echo "Cycle $i SELL API error: code=$sell_code msg=$sell_msg"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then
      echo "Max errors reached. Stopping."
      break
    fi
    sleep "$SLEEP_SEC"
    continue
  fi

  sell_qty="$(json_get "$sell_resp" "executedQty")"
  sell_id="$(json_get "$sell_resp" "orderId")"
  sell_quote="$(as_num "$(json_get "$sell_resp" "cummulativeQuoteQty")")"
  pnl_cycle="$(num_sub "$sell_quote" "$buy_quote")"
  total_pnl="$(num_add "$total_pnl" "$pnl_cycle")"
  ok_cycles=$((ok_cycles + 1))
  echo "$(date -u +%FT%TZ),$i,SELL,FILLED,$sell_id,$sell_qty,$sell_quote,$pnl_cycle,ok" >> "$LOG_FILE"

  echo "Cycle $i OK | BUY=$buy_quote USDT | SELL=$sell_quote USDT | PnL=$pnl_cycle USDT"
  sleep "$SLEEP_SEC"
done

echo
echo "Run complete."
echo "Symbol: $SYMBOL"
echo "Requested cycles: $requested_cycles"
echo "Successful cycles: $ok_cycles"
echo "Errors: $error_count"
echo "Total PnL (quote): $total_pnl USDT"
echo "Log: $LOG_FILE"
echo "Kill switch file: $STOP_FILE (create it to stop next run)"
