#!/usr/bin/env bash
# ============================================================
# TEST SIGNATURE DELETE — condition JUGE n°1 (17/08/2026)
# Valide la signature HMAC de private_delete() sur le TESTNET.
# ZÉRO EFFET DE BORD : DELETE sur un ordre INEXISTANT.
#   - signature valide   -> Binance répond code=-2011 (Unknown order)
#   - signature invalide -> Binance répond code=-1022 (Invalid signature)
# Aucun ordre n'est placé, rien n'est modifié.
# ============================================================
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"

# --- Clés testnet ---
if [ ! -f "$HOME/.binance_testnet.env" ]; then
  echo "❌ $HOME/.binance_testnet.env introuvable"
  exit 1
fi
# shellcheck disable=SC1090
source "$HOME/.binance_testnet.env"
: "${BINANCE_API_KEY:?missing}"
: "${BINANCE_API_SECRET:?missing}"

BASE_URL="https://testnet.binancefuture.com"
RECV_WINDOW=60000

# --- Reproduction EXACTE de la mécanique du moteur (patch V3) ---
now_ms() { ruby -e 'puts (Time.now.to_f * 1000).to_i'; }

sign() {
  local q="$1"
  printf '%s' "$q" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | od -A n -t x1 | tr -d ' \n'
}

private_delete() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 8 --max-time 15 -X DELETE \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}

private_post() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 8 --max-time 15 -X POST \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}

private_get() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl -sS --connect-timeout 8 --max-time 15 -X GET \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "$BASE_URL$path?$q&signature=$sig"
}

echo "=============================================================="
echo "TEST 1 — DELETE signé sur ordre inexistant (ACESTOPTEST000)"
echo "  Attendu si signature VALIDE : code=-2011 (Unknown order)"
echo "  Attendu si signature FAUSSE  : code=-1022 (Invalid signature)"
echo "=============================================================="
ts="$(now_ms)"
q1="symbol=BTCUSDT&origClientOrderId=ACESTOPTEST000&timestamp=$ts&recvWindow=$RECV_WINDOW"
r1="$(private_delete "/fapi/v1/order" "$q1")"
echo "Réponse : $r1"
echo ""

echo "=============================================================="
echo "TEST 2 — Contrôle GET signé (vérif clé API + position actuelle)"
echo "  Ne MODIFIE rien : lecture seule du risque de position"
echo "=============================================================="
ts="$(now_ms)"
q2="timestamp=$ts&recvWindow=$RECV_WINDOW"
r2="$(private_get "/fapi/v1/openOrders" "$q2")"
echo "Réponse (extrait) : $(echo "$r2" | head -c 300)"
echo ""

echo "=============================================================="
echo "ANALYSE"
echo "=============================================================="
if echo "$r1" | grep -q '"code":-2011'; then
  echo "✅ TEST 1 PASSÉ : signature DELETE VALIDE (Binance a reconnu la requête signée)"
elif echo "$r1" | grep -q '"code":-1022'; then
  echo "❌ TEST 1 ÉCHOUÉ : signature DELETE INVALIDE (HMAC erroné)"
elif [ -z "$r1" ]; then
  echo "⚠️ TEST 1 : réponse vide (réseau ?) — à retenter"
else
  echo "⚠️ TEST 1 : réponse inattendue → $r1"
fi
if echo "$r2" | grep -q '\[.*\]'; then
  echo "✅ TEST 2 PASSÉ : clé API + GET signé fonctionnent (openOrders accessible — carnet d'ordres ouvert)"
else
  echo "⚠️ TEST 2 : réponse inattendue → $(echo "$r2" | head -c 150)"
fi
