#!/usr/bin/env bash
# ============================================================
# TEST ALGO ORDER API — Binance Futures TESTNET (17/08/2026)
# La nouvelle API Algo Order (POST/DELETE /fapi/v1/algoOrder)
# remplace l'ancien endpoint pour les STOP_MARKET.
# Ordres fantômes (triggerPrice éloigné) + annulation immédiate.
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
# triggerPrice éloigné (2% sous le marché pour un SELL stop LONG)
TRIGGER=$(ruby -e 'printf("%.1f", Float(ARGV[0]) * 0.98)' -- "$PX")

echo ""
echo "=============================================================="
echo "A. PLACEMENT — algoType=CONDITIONAL + triggerPrice + positionSide"
echo "   (sans reduceOnly — interdit en hedge ; closePosition=true)"
echo "=============================================================="

place() {
  local label="$1" extra="$2"
  local id="ACESTOPTEST$((RANDOM % 9000 + 1000))"
  local ts="$(now_ms)"
  local q="algoType=CONDITIONAL&symbol=BTCUSDT&side=SELL&type=STOP_MARKET&triggerPrice=$TRIGGER&workingType=MARK_PRICE&clientAlgoId=$id&timestamp=$ts&recvWindow=$RECV_WINDOW"
  q="${q}${extra}"
  local r
  r="$(private_post "/fapi/v1/algoOrder" "$q")"
  local code
  code="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; puts j["code"]')"
  if [ -z "$code" ]; then
    local algo_id
    algo_id="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["algoId"]')"
    echo "✅ $label → ACCEPTÉ algoId=$algo_id clientAlgoId=$id"
    echo "$id"
  else
    local msg
    msg="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["msg"]')"
    echo "❌ $label → code=$code msg=$msg"
    echo ""
  fi
}

echo "--- A1 : positionSide=LONG + quantity (sans reduceOnly) ---"
A1=$(place "A1 posSide+qty" "&positionSide=LONG&quantity=0.001")

echo "--- A2 : positionSide=LONG + closePosition=true (Close-All) ---"
A2=$(place "A2 posSide+closePosition" "&positionSide=LONG&closePosition=true")

echo ""
echo "=============================================================="
echo "B. ANNULATION — DELETE /fapi/v1/algoOrder?clientAlgoId="
echo "=============================================================="
for id in $A1 $A2; do
  if [ -n "$id" ] && [ "$id" != "" ]; then
    ts="$(now_ms)"
    q="clientAlgoId=$id&timestamp=$ts&recvWindow=$RECV_WINDOW"
    r="$(private_delete "/fapi/v1/algoOrder" "$q")"
    code="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; puts j["code"]')"
    if [ -z "$code" ]; then
      echo "✅ ANNULATION $id → succès ($(echo "$r" | head -c 120))"
    else
      msg="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["msg"]')"
      echo "❌ ANNULATION $id → code=$code msg=$msg"
    fi
  fi
done

echo ""
echo "=============================================================="
echo "Nettoyage : vérif qu'il ne reste RIEN (algo + ordres classiques)"
echo "=============================================================="
ts="$(now_ms)"
q="timestamp=$ts&recvWindow=$RECV_WINDOW"
sig="$(sign "$q")"
curl -sS -m 8 -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
  "$BASE_URL/fapi/v1/openOrders?$q&signature=$sig" \
  | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue []; puts "  Ordres classiques ouverts: #{j.size}"'
