#!/usr/bin/env bash
set -euo pipefail

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET}"
: "${BINANCE_BASE_URL:=https://testnet.binance.vision}"

SYMBOL="${SYMBOL:-BTCUSDT}"
BUY_USDT="${BUY_USDT:-12}"   # > min notional pour éviter -1013
CYCLES="${CYCLES:-3}"
SLEEP_SEC="${SLEEP_SEC:-5}"

log_file="${LOG_FILE:-mini_run_log.csv}"
if [ ! -f "$log_file" ]; then
  echo "ts,cycle,side,status,orderId,executedQty,cumQuote,msg" > "$log_file"
fi

sign() {
  local q="$1"
  printf '%s' "$q" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256
}

private_post() {
  local path="$1"
  local q="$2"
  local sig
  sig="$(sign "$q")"
  curl -sS -X POST -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BINANCE_BASE_URL$path?$q&signature=$sig"
}

for i in $(seq 1 "$CYCLES"); do
  ts=$(ruby -e 'puts (Time.now.to_f * 1000).to_i')
  q_buy="symbol=$SYMBOL&side=BUY&type=MARKET&quoteOrderQty=$BUY_USDT&timestamp=$ts&recvWindow=60000"
  buy_resp="$(private_post "/api/v3/order" "$q_buy")"

  buy_qty="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["executedQty"] || "")' <<< "$buy_resp")"
  buy_id="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["orderId"] || "")' <<< "$buy_resp")"
  buy_quote="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["cummulativeQuoteQty"] || "")' <<< "$buy_resp")"
  echo "$(date -u +%FT%TZ),$i,BUY,FILLED,$buy_id,$buy_qty,$buy_quote,ok" >> "$log_file"

  ts=$(ruby -e 'puts (Time.now.to_f * 1000).to_i')
  q_sell="symbol=$SYMBOL&side=SELL&type=MARKET&quantity=$buy_qty&timestamp=$ts&recvWindow=60000"
  sell_resp="$(private_post "/api/v3/order" "$q_sell")"

  sell_qty="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["executedQty"] || "")' <<< "$sell_resp")"
  sell_id="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["orderId"] || "")' <<< "$sell_resp")"
  sell_quote="$(ruby -rjson -e 'j=JSON.parse(STDIN.read); print(j["cummulativeQuoteQty"] || "")' <<< "$sell_resp")"
  echo "$(date -u +%FT%TZ),$i,SELL,FILLED,$sell_id,$sell_qty,$sell_quote,ok" >> "$log_file"

  echo "Cycle $i OK | BUY qty=$buy_qty | SELL qty=$sell_qty"
  sleep "$SLEEP_SEC"
done

echo "Done. Log: $log_file"
