#!/usr/bin/env bash
# ==============================================================================
# ACE777 — PROTOCOLE DE PRÉ-VOL TOTAL INDUSTRIEL (V3.1)
# Objectif : Certification stérile 365j avant lancement de l'essaim NUAGE.
# Zéro écriture sur le modèle champion disque.
# ==============================================================================
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

C_N="\033[0m"
C_R="\033[0;31m"
C_G="\033[0;32m"
C_Y="\033[0;33m"
C_C="\033[0;36m"

fail() {
  echo -e "${C_R}FAIL: $1${C_N}" >&2
  exit 1
}

sign_query() {
  printf '%s' "$1" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256
}

echo -e "${C_C}=== INITIALISATION CHECK-UP PREFLIGHT TOTAL V3.1 ===${C_N}"

# 0. Config & champion (lecture seule)
echo -n "0. Audit config & champion... "
if [ ! -f "./config_active.env" ]; then
  fail "config_active.env introuvable"
fi
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh 2>/dev/null || fail "config_active.env illisible"
for f in genesis_manifest.txt radar_gate.rb; do
  [ -f "$_root/$f" ] || fail "fichier manquant: $f"
done
_min_usdt=$(( ${BUY_USDT_BETA:-200} + ${BUY_USDT_ALPHA:-800} ))
echo -e "${C_G}OK (${ACE777_CONFIG_NAME:-?} BETA=${BUY_USDT_BETA:-?} ALPHA=${BUY_USDT_ALPHA:-?} min=${_min_usdt})${C_N}"

# 1. EXTERMINATION DES TIMERS ET ZOMBIES ORPHELINS
echo -n "1. Purge des fantômes Unix... "
if [ -f "runs/timer.pid" ]; then
  _tp="$(tr -d ' \n\r' < runs/timer.pid 2>/dev/null || true)"
  if [ -n "$_tp" ]; then
    kill -9 "$_tp" 2>/dev/null || true
  fi
  rm -f runs/timer.pid
fi

if pgrep -fl 'ace777|NUAGE|genesis_manifest|watchdog_ace777|ace777_launch_v85|launch_vide_froid_4h_binance|tail -n 0 -F runs/|tail -F runs/\.NUAGE|caffeinate -is.*ace777' 2>/dev/null | grep -vi ollama | grep -q .; then
  ./stop_ace777_hard.sh >/dev/null 2>&1 || true
fi

pkill -9 -f "File.write\('STOP_ALPHA'" 2>/dev/null || true
pkill -9 -f 'ace777_launch_v85_nuage' 2>/dev/null || true
pkill -9 -f 'launch_vide_froid_4h_binance_NUAGE' 2>/dev/null || true
pkill -9 -f 'watchdog_ace777' 2>/dev/null || true
pkill -9 -f 'genesis_manifest' 2>/dev/null || true
pkill -9 -f 'tail -n 0 -F runs/' 2>/dev/null || true
pkill -9 -f 'tail -F runs/\.NUAGE' 2>/dev/null || true
pkill -9 -f 'caffeinate -is.*ace777' 2>/dev/null || true

rm -f runs/master.pid runs/alpha.pid runs/beta.pid runs/timer.pid
rm -f runs/*wrapper*.pid runs/*genesis*.pid 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA
rm -rf /tmp/ace777_ram_exchange
mkdir -p /tmp/ace777_ram_exchange
rm -f /tmp/alpha_heartbeat.txt

if ! ./scripts/verif_sterilite.sh >/dev/null 2>&1; then
  fail "processus ACE777 encore actifs après purge (voir verif_sterilite.sh)"
fi
touch STOP STOP_ALPHA STOP_BETA
echo -e "${C_G}STERILE=OK${C_N}"

# 2. VÉRIFICATION THERMIQUE
echo -n "2. Diagnostic thermique MacBook Air... "
_local_temp="$(sysctl -n machdep.xcpm.cpu_thermal_level 2>/dev/null || echo "0")"
if [ "$_local_temp" -gt 5 ]; then
  echo -e "${C_Y}WARN: CPU sous contrainte thermique (${_local_temp}). Laissez refroidir.${C_N}"
else
  echo -e "${C_G}TEMP_NORMAL=OK (level=${_local_temp})${C_N}"
fi

# 3. AUDIT LIGNE SURF (curl fapi ping — pas ICMP)
echo -n "3. Interrogation ligne Surf (fapi ping)... "
_binance_mode="${BINANCE_MODE:-testnet}"
if [ "$_binance_mode" = "live" ]; then
  _ping_url="${WATCHDOG_PING_URL:-https://fapi.binance.com/fapi/v1/ping}"
else
  _ping_url="${WATCHDOG_PING_URL:-https://testnet.binancefuture.com/fapi/v1/ping}"
fi

_ping_resp=""
_ping_ms=""
for _attempt in 1 2 3; do
  _curl_out="$(curl -sS -o /tmp/ace777_preflight_ping.json -w '%{time_total}' \
    --connect-timeout 2 --max-time 5 "$_ping_url" 2>/dev/null || true)"
  _ping_resp="$(cat /tmp/ace777_preflight_ping.json 2>/dev/null || true)"
  _ping_ms="$(ruby -e 'ms=(Float(ARGV[0]) rescue 0.0)*1000.0; printf("%.0f", ms)' "$_curl_out" 2>/dev/null || echo "?")"
  [ "$_ping_resp" = "{}" ] && break
  sleep 0.3
done
rm -f /tmp/ace777_preflight_ping.json

if [ "$_ping_resp" != "{}" ]; then
  fail "Binance inaccessible (3 tentatives) url=${_ping_url}"
fi
echo -e "${C_G}PING=${_ping_ms}ms OK${C_N}"

# 4. AUDIT COMPTE & WALLET (API signée)
echo -n "4. Connexion API & vérification solde USDT... "
if [ "$_binance_mode" = "live" ]; then
  [ -f "${HOME}/.binance_live.env" ] || fail "~/.binance_live.env manquant (BINANCE_MODE=live)"
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_live.env"
  set +a
  export BASE_URL="${BASE_URL:-https://fapi.binance.com}"
else
  [ -f "${HOME}/.binance_testnet.env" ] || fail "~/.binance_testnet.env manquant"
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  export BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
fi

[ -n "${BINANCE_API_KEY:-}" ] || fail "BINANCE_API_KEY manquante"
[ -n "${BINANCE_API_SECRET:-}" ] || fail "BINANCE_API_SECRET manquante"

_ts="$(ruby -e 'puts (Time.now.to_f * 1000).to_i')"
_q="timestamp=${_ts}&recvWindow=60000"
_sig="$(sign_query "$_q")"
_balance_json="$(curl -sS --connect-timeout 5 --max-time 15 \
  -H "X-MBX-APIKEY: ${BINANCE_API_KEY}" \
  "${BASE_URL}/fapi/v2/balance?${_q}&signature=${_sig}" 2>/dev/null || true)"

_solde_usdt="$(ruby -rjson -e '
  begin
    j = JSON.parse(STDIN.read)
    if j.is_a?(Hash) && j["code"]
      print "ERR"
    else
      b = j.find { |x| x["asset"] == "USDT" }
      print((b["availableBalance"] || b["balance"] || "0").to_f.round(2))
    end
  rescue
    print "ERR"
  end
' <<< "$_balance_json" 2>/dev/null || echo "ERR")"

if [ "$_solde_usdt" = "ERR" ] || [ -z "$_solde_usdt" ]; then
  _api_msg="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; puts j["msg"] || j["code"] || "?"' <<< "$_balance_json" 2>/dev/null || echo "?")"
  fail "API balance rejetée (${_api_msg})"
fi

if ruby -e 'exit((Float(ARGV[0]) < Float(ARGV[1])) ? 0 : 1)' "$_solde_usdt" "$_min_usdt" 2>/dev/null; then
  fail "Solde insuffisant (${_solde_usdt} USDT < ${_min_usdt} requis). Risque -2028."
fi
echo -e "${C_G}SOLDE=${_solde_usdt} USDT NOMINAL OK (min=${_min_usdt})${C_N}"

# 5. Certification finale pre-run
echo -n "5. Certification stérilité pre-run... "
if ! ./scripts/verif_sterilite.sh --pre-run >/dev/null 2>&1; then
  fail "verif_sterilite --pre-run NOK"
fi
echo -e "${C_G}CERTIFIED=OK${C_N}"

echo -e "${C_G}=== FEU VERT : LE COCKPIT EST CERTIFIÉ STÉRILE ET PRÊT ===${C_N}"
exit 0
