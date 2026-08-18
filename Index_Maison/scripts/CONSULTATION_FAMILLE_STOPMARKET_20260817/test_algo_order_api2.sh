#!/usr/bin/env bash
# ============================================================
# TEST ALGO ORDER API v2 — réponses brutes (17/08/2026)
# ============================================================
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"

source "$HOME/.binance_testnet.env"
: "${BINANCE_API_KEY:?missing}"
: "${BINANCE_API_SECRET:?missing}"

BASE_URL="https://testnet.binancefuture.com"
RECV_WINDOW=60000

now_ms() { ruby -e 'puts (Time.now.to_f * 1000).to_i'; }
sign() {
  local q="$1"
  printf '%s' "$q" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | od -A n -t x1 | tr -d ' \n'
}
private_post() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 8 --max-time 15 -X POST \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}
private_delete() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 8 --max-time 15 -X DELETE \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}

PX=$(curl -sS -m 5 "https://testnet.binancefuture.com/fapi/v1/ticker/price?symbol=BTCUSDT" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["price"]')
echo "Prix BTCUSDT testnet : $PX"
TRIGGER=$(ruby -e 'printf("%.1f", Float(ARGV[0]) * 0.98)' -- "$PX")

# --- Position actuelle (mode hedge ?) ---
ts="$(now_ms)"
q="timestamp=$ts&recvWindow=$RECV_WINDOW"
sig="$(sign "$q")"
echo "=== Positions actuelles ==="
curl -sS -m 8 -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
  "$BASE_URL/fapi/v2/positionRisk?$q&signature=$sig" \
  | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue []; j.each{|p| puts "  #{p["symbol"]} #{p["positionSide"]} amt=#{p["positionAmt"]}" if p["positionAmt"].to_f.abs > 1e-9}; puts "  (aucune position ouverte)" if j.none?{|p| p["positionAmt"].to_f.abs > 1e-9}'

# --- Placement A1 : positionSide + quantity ---
echo ""
echo "=== A1 : positionSide=LONG + quantity=0.001 (sans reduceOnly) ==="
ID1="ACESTOPTEST$((RANDOM % 9000 + 1000))"
ts="$(now_ms)"
q="algoType=CONDITIONAL&symbol=BTCUSDT&side=SELL&type=STOP_MARKET&triggerPrice=$TRIGGER&workingType=MARK_PRICE&positionSide=LONG&quantity=0.001&clientAlgoId=$ID1&timestamp=$ts&recvWindow=$RECV_WINDOW"
R1="$(private_post "/fapi/v1/algoOrder" "$q")"
echo "Réponse : $R1"

# --- Placement A2 : positionSide + closePosition ---
echo ""
echo "=== A2 : positionSide=LONG + closePosition=true ==="
ID2="ACESTOPTEST$((RANDOM % 9000 + 1000))"
ts="$(now_ms)"
q="algoType=CONDITIONAL&symbol=BTCUSDT&side=SELL&type=STOP_MARKET&triggerPrice=$TRIGGER&workingType=MARK_PRICE&positionSide=LONG&closePosition=true&clientAlgoId=$ID2&timestamp=$ts&recvWindow=$RECV_WINDOW"
R2="$(private_post "/fapi/v1/algoOrder" "$q")"
echo "Réponse : $R2"

# --- Placement A3 : SANS positionSide (mode one-way) + closePosition ---
echo ""
echo "=== A3 : closePosition=true SANS positionSide ==="
ID3="ACESTOPTEST$((RANDOM % 9000 + 1000))"
ts="$(now_ms)"
q="algoType=CONDITIONAL&symbol=BTCUSDT&side=SELL&type=STOP_MARKET&triggerPrice=$TRIGGER&workingType=MARK_PRICE&closePosition=true&clientAlgoId=$ID3&timestamp=$ts&recvWindow=$RECV_WINDOW"
R3="$(private_post "/fapi/v1/algoOrder" "$q")"
echo "Réponse : $R3"

# --- Annulation des acceptés ---
echo ""
echo "=== Annulations ==="
for id in "$ID1" "$ID2" "$ID3"; do
  ts="$(now_ms)"
  q="clientAlgoId=$id&timestamp=$ts&recvWindow=$RECV_WINDOW"
  r="$(private_delete "/fapi/v1/algoOrder" "$q")"
  echo "  cancel $id → $r"
done

echo ""
echo "=== Vérif finale : openOrders ==="
ts="$(now_ms)"
q="timestamp=$ts&recvWindow=$RECV_WINDOW"
sig="$(sign "$q")"
curl -sS -m 8 -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
  "$BASE_URL/fapi/v1/openOrders?$q&signature=$sig" \
  | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue []; puts "  Ordres ouverts: #{j.size}"'
