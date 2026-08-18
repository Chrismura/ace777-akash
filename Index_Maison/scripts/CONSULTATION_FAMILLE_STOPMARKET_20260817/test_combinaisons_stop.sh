#!/usr/bin/env bash
# ============================================================
# TEST COMBINAISONS STOP_MARKET — Binance Futures TESTNET (17/08/2026)
# But : trouver la combinaison de paramètres ACCEPTÉE (erreur -1106
# sur reduceOnly quand positionSide est fourni en mode hedge).
# Ordres fantômes : stopPrice éloigné du marché + annulation immédiate.
# IDs de test distincts (ACESTOPTEST*) — aucun impact sur le run en cours.
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

# Prix actuel BTCUSDT testnet
PX=$(curl -sS -m 5 "https://testnet.binancefuture.com/fapi/v1/ticker/price?symbol=BTCUSDT" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["price"]')
echo "Prix BTCUSDT testnet : $PX"
# stopPrice éloigné : 2% sous le marché pour un SELL stop (déclenchement quasi impossible en qq secondes)
STOP_SELL=$(ruby -e 'printf("%.1f", Float(ARGV[0]) * 0.98)' -- "$PX")
QTY="0.001"
TS_NOW="$(now_ms)"

# Ordres à tester (tous SELL stop, close_side d'un LONG)
run_test() {
  local label="$1" params="$2"
  local id="ACESTOPTEST$((RANDOM % 9000 + 1000))"
  local ts="$(now_ms)"
  local q="symbol=BTCUSDT&side=SELL&type=STOP_MARKET&quantity=$QTY&stopPrice=$STOP_SELL&workingType=MARK_PRICE&newClientOrderId=$id&timestamp=$ts&recvWindow=$RECV_WINDOW"
  q="${q}${params}"
  local r
  r="$(private_post "/fapi/v1/order" "$q")"
  local code
  code="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; puts j["code"]')"
  if [ -z "$code" ]; then
    # ordre ACCEPTÉ → on l'annule immédiatement (propre)
    local order_id
    order_id="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["orderId"]')"
    local qc="symbol=BTCUSDT&orderId=$order_id&timestamp=$(now_ms)&recvWindow=$RECV_WINDOW"
    private_delete "/fapi/v1/order" "$qc" >/dev/null 2>&1
    echo "✅ $label → ACCEPTÉ (orderId=$order_id, annulé)"
  else
    local msg
    msg="$(echo "$r" | ruby -rjson -e 'j=JSON.parse(STDIN.read); puts j["msg"]')"
    echo "❌ $label → code=$code msg=$msg"
  fi
}

echo "=============================================================="
echo "T1 : reduceOnly=true + positionSide=LONG   (ce qu'on fait actuellement → -1106 attendu)"
echo "=============================================================="
run_test "T1 reduceOnly+posSide" "&reduceOnly=true&positionSide=LONG"

echo ""
echo "=============================================================="
echo "T2 : positionSide=LONG SANS reduceOnly   (hypothèse : bon format hedge)"
echo "=============================================================="
run_test "T2 posSide seul" "&positionSide=LONG"

echo ""
echo "=============================================================="
echo "T3 : reduceOnly=true SANS positionSide   (mode one-way)"
echo "=============================================================="
run_test "T3 reduceOnly seul" "&reduceOnly=true"

echo ""
echo "=============================================================="
echo "T4 : ni reduceOnly ni positionSide"
echo "=============================================================="
run_test "T4 ni l'un ni l'autre" ""

echo ""
echo "=============================================================="
echo "Nettoyage final : vérif carnet vide (nos tests)"
echo "=============================================================="
ts="$(now_ms)"
q="timestamp=$ts&recvWindow=$RECV_WINDOW"
sig="$(sign "$q")"
curl -sS -m 8 -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
  "$BASE_URL/fapi/v1/openOrders?$q&signature=$sig" \
  | ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue []; j.each{|o| puts "  RESTANT: #{o["clientOrderId"]} #{o["type"]} #{o["side"]} stopPrice=#{o["stopPrice"]}"}; puts "  Total ordres ouverts: #{j.size}"'
