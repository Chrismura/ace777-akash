#!/usr/bin/env bash
set -euo pipefail

# Charge systematique des cles testnet depuis fichier local.
# Cela evite de retaper/exporter les cles a chaque terminal.
KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
SHELL_KEY_BEFORE="${BINANCE_API_KEY:-}"
SHELL_SECRET_BEFORE="${BINANCE_API_SECRET:-}"
if [[ -f "$KEYS_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$KEYS_FILE"
  if [[ -n "$SHELL_KEY_BEFORE$SHELL_SECRET_BEFORE" ]] && \
     ([[ "${BINANCE_API_KEY:-}" != "$SHELL_KEY_BEFORE" ]] || [[ "${BINANCE_API_SECRET:-}" != "$SHELL_SECRET_BEFORE" ]]); then
    echo "ALERTE_CLES: variables shell modifiees/reesetees, cles rechargees depuis $KEYS_FILE."
  else
    echo "INFO_CLES: cles chargees depuis $KEYS_FILE."
  fi
fi

: "${BINANCE_API_KEY:?missing BINANCE_API_KEY (utilise $KEYS_FILE)}"
: "${BINANCE_API_SECRET:?missing BINANCE_API_SECRET (utilise $KEYS_FILE)}"
if [[ "$BINANCE_API_KEY" =~ [[:space:]] || "$BINANCE_API_SECRET" =~ [[:space:]] ]]; then
  echo "Abort: cles invalides (espaces/retours ligne detectes)."
  exit 1
fi
if (( ${#BINANCE_API_KEY} < 40 || ${#BINANCE_API_SECRET} < 40 || ${#BINANCE_API_KEY} > 90 || ${#BINANCE_API_SECRET} > 90 )); then
  echo "Abort: format de cles suspect (KEY_LEN=${#BINANCE_API_KEY} SECRET_LEN=${#BINANCE_API_SECRET})."
  echo "Attendu: longueur typique proche de 64/64 sur Binance testnet."
  exit 1
fi
: "${BINANCE_BASE_URL:=https://testnet.binance.vision}"
: "${BINANCE_BASE_URL_FALLBACK:=https://api1.binance.com}"

load_kv_file() {
  local f="$1"
  local line key val
  [ -f "$f" ] || return 0
  while IFS= read -r line || [ -n "$line" ]; do
    line="${line%%#*}"
    line="${line%"${line##*[![:space:]]}"}"
    line="${line#"${line%%[![:space:]]*}"}"
    [ -z "$line" ] && continue
    case "$line" in
      *=*)
        key="${line%%=*}"
        val="${line#*=}"
        if [[ "$key" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
          export "$key=$val"
        fi
        ;;
      *)
        # Ignore non KEY=VALUE lines.
        ;;
    esac
  done < "$f"
}

SETTINGS_FILE="${SETTINGS_FILE:-sniper_settings.1437}"
VORTEX_FILE="${VORTEX_FILE:-tempo_vortex.1437}"
RELATIVITE_FILE="${RELATIVITE_FILE:-relativite_v2.1437}"
ELASTIC_FILE="${ELASTIC_FILE:-elastic_vortex.1437}"
MASS_FILE="${MASS_FILE:-vortex_mass.1437}"
ANOMALY_FILE="${ANOMALY_FILE:-anomaly_soft.1437}"
RADAR_FILE="${RADAR_FILE:-radar_gate.1437}"
INDEX_FILE="${INDEX_FILE:-index_feed.1437}"
STRUCTURE_FILE="${STRUCTURE_FILE:-structure_153.1437}"
TACTIC_FILE="${TACTIC_FILE:-tactic_91.1437}"
REACTION_FILE="${REACTION_FILE:-reaction_5.1437}"
load_kv_file "$SETTINGS_FILE"
load_kv_file "$VORTEX_FILE"
load_kv_file "$RELATIVITE_FILE"
load_kv_file "$ELASTIC_FILE"
load_kv_file "$MASS_FILE"
load_kv_file "$ANOMALY_FILE"
load_kv_file "$RADAR_FILE"
load_kv_file "$INDEX_FILE"
load_kv_file "$STRUCTURE_FILE"
load_kv_file "$TACTIC_FILE"
load_kv_file "$REACTION_FILE"

SYMBOL="${SYMBOL:-BTCUSDT}"
BUY_USDT="${BUY_USDT:-12}"
CYCLES="${CYCLES:-10}"
SLEEP_SEC="${SLEEP_SEC:-5}"
POLL_SEC="${POLL_SEC:-2}"
RECV_WINDOW="${RECV_WINDOW:-60000}"
MAX_ERRORS="${MAX_ERRORS:-3}"
RETRY_MAX="${RETRY_MAX:-3}"
RETRY_DELAY_SEC="${RETRY_DELAY_SEC:-2}"
STOP_FILE="${STOP_FILE:-STOP}"
LOG_FILE="${LOG_FILE:-mini_run_smart_log.csv}"
WATCHDOG_ENABLED="${WATCHDOG_ENABLED:-TRUE}"
WATCHDOG_MAX_SKIP_STREAK="${WATCHDOG_MAX_SKIP_STREAK:-50}"
WATCHDOG_MAX_CYCLE_SEC="${WATCHDOG_MAX_CYCLE_SEC:-900}"
CRASH_WATCHDOG_ENABLED="${CRASH_WATCHDOG_ENABLED:-FALSE}"
CRASH_ALERT_BPS="${CRASH_ALERT_BPS:-18}"
CRASH_CHECK_MS="${CRASH_CHECK_MS:-500}"
MODE="${MODE:-BOTH_SPOT}"  # LONG_ONLY | BOTH_SPOT
MOMENTUM_SLEEP_SEC="${MOMENTUM_SLEEP_SEC:-1}"
MOMENTUM_THRESHOLD_BPS="${MOMENTUM_THRESHOLD_BPS:-1}"
INDEX_MODE="${INDEX_MODE:-FALSE}"
INDEX_SYMBOLS="${INDEX_SYMBOLS:-BTCUSDT,BTCUSDC,BTCFDUSD}"
RADAR_GATE="${RADAR_GATE:-TRUE}"
RADAR_MIN_CONF="${RADAR_MIN_CONF:-0.55}"
RADAR_MIN_MOM_BPS="${RADAR_MIN_MOM_BPS:-0.5}"
RADAR_DIR_BPS="${RADAR_DIR_BPS:-0.2}"
RADAR_MAX_SPREAD_BPS="${RADAR_MAX_SPREAD_BPS:-$MAX_SLIPPAGE_BPS}"

# RESONANCE.1437 + HOLOGRAPHIC MEMORY gate (live entry condition).
RESONANCE_GATE_ENABLED="${RESONANCE_GATE_ENABLED:-TRUE}"
V_ACE_HZ="${V_ACE_HZ:-7.2}"
RANGE_USD="${RANGE_USD:-200}"
SPIKE_USD="${SPIKE_USD:-1500}"
TICK_BASE_USD="${TICK_BASE_USD:-5}"
TICK_SPIKE_USD="${TICK_SPIKE_USD:-60}"
RESONANCE_PHASE_LOCK_MIN="${RESONANCE_PHASE_LOCK_MIN:-0.45}"
RESONANCE_STRICT_LOCK_MIN="${RESONANCE_STRICT_LOCK_MIN:-0.60}"
RESONANCE_FAST_BPS="${RESONANCE_FAST_BPS:-25}"
RESONANCE_PANIC_BPS="${RESONANCE_PANIC_BPS:-60}"
HOLO_MACRO_BIAS="${HOLO_MACRO_BIAS:-NEUTRAL}"  # BULL | BEAR | NEUTRAL
HOLO_STRICT="${HOLO_STRICT:-TRUE}"

# Structure/Tactic/Reaction layer (light hierarchy)
EMA_STRUCTURE="${EMA_STRUCTURE:-153}"
TREND_FILTER="${TREND_FILTER:-FALSE}"
SMOOTHING_153="${SMOOTHING_153:-0.987}"
STRUCTURE_LOOKBACK_MIN="${STRUCTURE_LOOKBACK_MIN:-3}"
EMA_TACTIC="${EMA_TACTIC:-91}"
ENTRY_SIGNAL="${ENTRY_SIGNAL:-CROSSOVER}"
TACTIC_MAX_HOLD_SEC="${TACTIC_MAX_HOLD_SEC:-$MAX_HOLD_SEC}"
TACTIC_MIN_HOLD_SEC="${TACTIC_MIN_HOLD_SEC:-$MIN_HOLD_SEC}"
VOL_LOOKBACK="${VOL_LOOKBACK:-5}"
ITL_SCALE="${ITL_SCALE:-10}"
STALL_CONFIRMATIONS="${STALL_CONFIRMATIONS:-$FATIGUE_CONFIRMATIONS}"

# Strategy controls (basis points)
MIN_PROFIT_BPS="${MIN_PROFIT_BPS:-10}"  # +0.10%
STOP_LOSS_BPS="${STOP_LOSS_BPS:-5}"     # -0.05%
MAX_HOLD_SEC="${MAX_HOLD_SEC:-30}"      # force exit after N seconds
TRAIL_ARM_BPS="${TRAIL_ARM_BPS:-10}"    # arm trailing once this gain is reached
TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-3}"  # exit after this pullback from peak
USE_TRAILING="${USE_TRAILING:-1}"       # 1=enable trailing logic

# Optional tempo vortex controls.
DYNAMIC_TIMEOUT="${DYNAMIC_TIMEOUT:-FALSE}"
ENTROPY_SCALING="${ENTROPY_SCALING:-0.1437}"
MIN_HOLD="${MIN_HOLD:-5s}"
MAX_HOLD="${MAX_HOLD:-180s}"
STALL_DETECTION="${STALL_DETECTION:-3_cycles}"
MAX_SLIPPAGE_BPS="${MAX_SLIPPAGE_BPS:-8}"
MIN_LIQUIDITY_CHECK="${MIN_LIQUIDITY_CHECK:-FALSE}"
LIQUIDITY_BUFFER="${LIQUIDITY_BUFFER:-1.5}"
S_RATIO="${S_RATIO:-1.0}"

# Optional relativity profile controls.
T_BASE="${T_BASE:-45}"
K_ENTROPY="${K_ENTROPY:-0.1437}"
STALL_THRESHOLD_BPS_PER_SEC="${STALL_THRESHOLD_BPS_PER_SEC:-0.1}"
F_A_SMOOTHING="${F_A_SMOOTHING:-0.85}"
CALORIE_EFFICIENCY_EXIT="${CALORIE_EFFICIENCY_EXIT:-TRUE}"

# Optional elastic vortex controls.
TIME_IS_VARIABLE="${TIME_IS_VARIABLE:-FALSE}"
EXIT_BY_FATIGUE="${EXIT_BY_FATIGUE:-TRUE}"
MASS_EXPANSION_RATIO="${MASS_EXPANSION_RATIO:-1.437}"
FORCE_THRESHOLD="${FORCE_THRESHOLD:-0.001437}"
FATIGUE_CONFIRMATIONS="${FATIGUE_CONFIRMATIONS:-3}"

# Optional dynamic mass controls.
DYNAMIC_MASS="${DYNAMIC_MASS:-FALSE}"
BASE_MASS="${BASE_MASS:-$BUY_USDT}"
BOOST_FACTOR="${BOOST_FACTOR:-1.437}"
MIN_STALL_BPS="${MIN_STALL_BPS:-2}"
FATIGUE_THRESHOLD="${FATIGUE_THRESHOLD:-0.5}"
ORDER_SMOOTHING="${ORDER_SMOOTHING:-TRUE}"
ORDER_SMOOTH_ALPHA="${ORDER_SMOOTH_ALPHA:-0.7}"

# Soft anomaly neutralization (do not hard-reject, reduce risk temporarily).
ANOMALY_SOFT_MODE="${ANOMALY_SOFT_MODE:-TRUE}"
ANOMALY_TICK_BPS="${ANOMALY_TICK_BPS:-40}"
ANOMALY_PNL_USDT="${ANOMALY_PNL_USDT:-0.05}"
SOFT_COOLDOWN_CYCLES="${SOFT_COOLDOWN_CYCLES:-3}"
SOFT_MASS_FACTOR="${SOFT_MASS_FACTOR:-0.5}"
SOFT_MAX_HOLD_SEC="${SOFT_MAX_HOLD_SEC:-90}"
SOFT_STOP_LOSS_BPS="${SOFT_STOP_LOSS_BPS:-7}"
SOFT_TRAIL_GIVEBACK_BPS="${SOFT_TRAIL_GIVEBACK_BPS:-2}"

# LIVE reset policy (operator can override only by explicitly setting FALSE).
LIVE_ONLY="${LIVE_ONLY:-FALSE}"
FORCE_SYMBOL_BTCUSDT="${FORCE_SYMBOL_BTCUSDT:-TRUE}"
FORCE_DISABLE_SYNTHETIC="${FORCE_DISABLE_SYNTHETIC:-TRUE}"

# Network/proxy hardening for recurring HTTP 403 issues.
PROXY_BYPASS_BINANCE="${PROXY_BYPASS_BINANCE:-TRUE}"
HTTP_PROXY_OVERRIDE="${HTTP_PROXY_OVERRIDE:-}"
HTTPS_PROXY_OVERRIDE="${HTTPS_PROXY_OVERRIDE:-}"
NO_PROXY_EXTRA="${NO_PROXY_EXTRA:-}"

CURL_LAST_HTTP_CODE="000"
CURL_LAST_ERROR=""

if [ ! -f "$LOG_FILE" ]; then
  echo "ts,cycle,side,status,orderId,executedQty,cumQuote,pnl,exitReason,holdSec,refPrice,msg" > "$LOG_FILE"
fi

now_ms() {
  ruby -e 'puts (Time.now.to_f * 1000).to_i'
}

now_sec() {
  ruby -e 'puts Time.now.to_i'
}

bool_is_true() {
  local v="${1:-}"
  case "$v" in
    TRUE|true|1|yes|YES|on|ON) return 0 ;;
    *) return 1 ;;
  esac
}

init_live_reset_policy() {
  if bool_is_true "$LIVE_ONLY"; then
    BINANCE_BASE_URL="https://api.binance.com"
  else
    BINANCE_BASE_URL="https://testnet.binance.vision"
  fi
  if bool_is_true "$FORCE_SYMBOL_BTCUSDT"; then
    SYMBOL="BTCUSDT"
  fi
  if bool_is_true "$FORCE_DISABLE_SYNTHETIC"; then
    INDEX_MODE="FALSE"
  fi
}

validate_credentials_inputs() {
  case "${BINANCE_API_KEY:-}" in
    ""|"TA_CLE_TESTNET"|"TA_CLE_LIVE"|"YOUR_API_KEY"|"YOUR_TESTNET_KEY"|TA_*|YOUR_*)
      echo "Abort: BINANCE_API_KEY invalide (placeholder)."
      return 1
      ;;
  esac
  case "${BINANCE_API_SECRET:-}" in
    ""|"TON_SECRET_TESTNET"|"TON_SECRET_LIVE"|"YOUR_API_SECRET"|"YOUR_TESTNET_SECRET"|TON_*|YOUR_*)
      echo "Abort: BINANCE_API_SECRET invalide (placeholder)."
      return 1
      ;;
  esac
  return 0
}

build_no_proxy_list() {
  local base_host
  base_host="$(ruby -ruri -e 'u=URI(ARGV[0]) rescue nil; print(u&.host.to_s)' -- "$BINANCE_BASE_URL")"
  if [ -n "$NO_PROXY_EXTRA" ]; then
    printf '%s' "localhost,127.0.0.1,::1,api.binance.com,api1.binance.com,testnet.binance.vision,$base_host,$NO_PROXY_EXTRA"
  else
    printf '%s' "localhost,127.0.0.1,::1,api.binance.com,api1.binance.com,testnet.binance.vision,$base_host"
  fi
}

curl_exec() {
  local method="$1"
  local url="$2"
  shift 2
  local body_file err_file http_code body err_text
  body_file="$(mktemp)"
  err_file="$(mktemp)"
  if [ -n "$HTTP_PROXY_OVERRIDE" ]; then
    export HTTP_PROXY="$HTTP_PROXY_OVERRIDE"
  fi
  if [ -n "$HTTPS_PROXY_OVERRIDE" ]; then
    export HTTPS_PROXY="$HTTPS_PROXY_OVERRIDE"
  fi
  if bool_is_true "$PROXY_BYPASS_BINANCE"; then
    export NO_PROXY="$(build_no_proxy_list)"
    export no_proxy="$NO_PROXY"
  fi
  http_code="$(curl -sS --connect-timeout 10 --max-time 25 \
    -X "$method" "$@" \
    -o "$body_file" -w "%{http_code}" "$url" 2>"$err_file" || true)"
  body="$(<"$body_file")"
  err_text="$(<"$err_file")"
  rm -f "$body_file" "$err_file"
  CURL_LAST_HTTP_CODE="${http_code:-000}"
  CURL_LAST_ERROR="$err_text"
  printf '%s' "$body"
  if [ -n "$body" ] || [ "${CURL_LAST_HTTP_CODE}" != "000" ]; then
    return 0
  fi
  return 1
}

http_403_json() {
  local target="$1"
  local err_escaped
  err_escaped="$(printf '%s' "$CURL_LAST_ERROR" | ruby -rjson -e 'print(JSON.generate(STDIN.read)[1..-2])')"
  printf '{"code":403,"msg":"HTTP 403 from %s (proxy/network). no_proxy=%s curl_err=%s"}' "$target" "${NO_PROXY:-unset}" "$err_escaped"
}

preflight_live_connectivity() {
  local ping_resp time_resp acct_resp acct_code
  ping_resp="$(curl_exec "GET" "$BINANCE_BASE_URL/api/v3/ping" || true)"
  if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
    echo "Preflight failed: HTTP 403 on /ping (base=$BINANCE_BASE_URL)."
    return 1
  fi
  time_resp="$(curl_exec "GET" "$BINANCE_BASE_URL/api/v3/time" || true)"
  if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
    echo "Preflight failed: HTTP 403 on /time (base=$BINANCE_BASE_URL)."
    return 1
  fi
  acct_resp="$(private_get_retry "omitZeroBalances=true" || true)"
  acct_code="$(json_get "$acct_resp" "code")"
  if [ "$acct_code" = "403" ]; then
    echo "Preflight failed: HTTP 403 on signed /account."
    return 1
  fi
  if [ -n "$acct_code" ]; then
    echo "Preflight failed: API credentials invalides sur /account (code=$acct_code msg=$(json_get "$acct_resp" "msg"))."
    return 1
  fi
  return 0
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

num_add() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a+b)' -- "$a" "$b"
}

num_sub() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a-b)' -- "$a" "$b"
}

num_mul() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); printf("%.8f", a*b)' -- "$a" "$b"
}

num_div() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 1.0); printf("%.8f", b == 0.0 ? 0.0 : a/b)' -- "$a" "$b"
}

num_ge() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a >= b ? 0 : 1)' -- "$a" "$b"
}

num_le() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a <= b ? 0 : 1)' -- "$a" "$b"
}

bps_change() {
  local base="$1"
  local px="$2"
  ruby -e 'b=(Float(ARGV[0]) rescue 0.0); p=(Float(ARGV[1]) rescue 0.0); out=(b == 0.0 ? 0.0 : ((p-b)/b)*10000.0); printf("%.8f", out)' -- "$base" "$px"
}

to_int() {
  local raw="$1"
  local fallback="$2"
  local cleaned
  cleaned="$(printf '%s' "$raw" | tr -cd '0-9')"
  if [ -z "$cleaned" ]; then
    printf '%s' "$fallback"
  else
    printf '%s' "$cleaned"
  fi
}

compute_dynamic_hold() {
  local base="$1"
  local min_hold="$2"
  local max_hold="$3"
  local streak="$4"
  local scaling="$5"
  ruby -e '
    base=(Float(ARGV[0]) rescue 30.0)
    min_h=(Float(ARGV[1]) rescue 5.0)
    max_h=(Float(ARGV[2]) rescue 180.0)
    streak=(Float(ARGV[3]) rescue 0.0)
    scale=(Float(ARGV[4]) rescue 0.0)
    factor=1.0 + (streak * scale)
    hold=(base * factor).round
    hold=min_h if hold < min_h
    hold=max_h if hold > max_h
    print hold.to_i
  ' -- "$base" "$min_hold" "$max_hold" "$streak" "$scaling"
}

compute_fa() {
  local vol_rel="$1"
  local vol_asp="$2"
  local s_ratio="$3"
  ruby -e '
    v=(Float(ARGV[0]) rescue 0.0)
    a=(Float(ARGV[1]) rescue 0.0)
    s=(Float(ARGV[2]) rescue 1.0)
    s=1.0 if s <= 0.0
    print ((v * a) / s)
  ' -- "$vol_rel" "$vol_asp" "$s_ratio"
}

ema() {
  local prev="$1"
  local raw="$2"
  local alpha="$3"
  ruby -e '
    p=(Float(ARGV[0]) rescue 0.0)
    r=(Float(ARGV[1]) rescue 0.0)
    a=(Float(ARGV[2]) rescue 0.85)
    a=0.0 if a < 0.0
    a=1.0 if a > 1.0
    print((a * p) + ((1.0-a) * r))
  ' -- "$prev" "$raw" "$alpha"
}

abs_num() {
  local v="$1"
  ruby -e 'x=(Float(ARGV[0]) rescue 0.0); printf("%.8f", x.abs)' -- "$v"
}

compute_hold_relativity() {
  local t_base="$1"
  local fa="$2"
  local k_entropy="$3"
  local min_hold="$4"
  local max_hold="$5"
  ruby -e '
    t=(Float(ARGV[0]) rescue 45.0)
    f=(Float(ARGV[1]) rescue 0.0)
    k=(Float(ARGV[2]) rescue 0.1437)
    mn=(Float(ARGV[3]) rescue 5.0)
    mx=(Float(ARGV[4]) rescue 180.0)
    hold=(t / (1.0 + (f*k))).round
    hold=mn if hold < mn
    hold=mx if hold > mx
    print hold.to_i
  ' -- "$t_base" "$fa" "$k_entropy" "$min_hold" "$max_hold"
}

apply_time_elasticity() {
  local hold="$1"
  local force="$2"
  local threshold="$3"
  local ratio="$4"
  local min_hold="$5"
  local max_hold="$6"
  ruby -e '
    h=(Float(ARGV[0]) rescue 30.0)
    f=(Float(ARGV[1]) rescue 0.0)
    t=(Float(ARGV[2]) rescue 0.001437)
    r=(Float(ARGV[3]) rescue 1.437)
    mn=(Float(ARGV[4]) rescue 5.0)
    mx=(Float(ARGV[5]) rescue 180.0)
    r=1.0 if r <= 0.0
    # If force is weak, expand hold; if strong, contract hold.
    out = (f < t) ? (h * r) : (h / r)
    out = mn if out < mn
    out = mx if out > mx
    print out.round.to_i
  ' -- "$hold" "$force" "$threshold" "$ratio" "$min_hold" "$max_hold"
}

compute_order_mass() {
  local base_mass="$1"
  local boost="$2"
  local force="$3"
  local force_threshold="$4"
  local fatigue_score="$5"
  local fatigue_threshold="$6"
  ruby -e '
    base=(Float(ARGV[0]) rescue 12.0)
    boost=(Float(ARGV[1]) rescue 1.437)
    force=(Float(ARGV[2]) rescue 0.0)
    force_t=(Float(ARGV[3]) rescue 0.001437)
    fatigue=(Float(ARGV[4]) rescue 0.0)
    fatigue_t=(Float(ARGV[5]) rescue 0.5)
    m=base
    if force > force_t
      m = base * boost
    end
    if fatigue >= fatigue_t
      m = m / boost
    end
    m = 5.0 if m < 5.0
    printf("%.4f", m)
  ' -- "$base_mass" "$boost" "$force" "$force_threshold" "$fatigue_score" "$fatigue_threshold"
}

private_post_retry() {
  local path="$1"
  local q="$2"
  local sig out attempt req_url

  sig="$(sign "$q")"
  req_url="$BINANCE_BASE_URL$path?$q&signature=$sig"
  for attempt in $(seq 1 "$RETRY_MAX"); do
    out="$(curl_exec "POST" "$req_url" \
      -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
      || true)"
    if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
      if [ "$BINANCE_BASE_URL" != "$BINANCE_BASE_URL_FALLBACK" ]; then
        BINANCE_BASE_URL="$BINANCE_BASE_URL_FALLBACK"
        req_url="$BINANCE_BASE_URL$path?$q&signature=$sig"
        continue
      fi
      http_403_json "$path"
      return 0
    fi
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
    sleep "$RETRY_DELAY_SEC"
  done
  return 1
}

private_get_retry() {
  local path_q="$1"
  local sig out attempt req_url
  local ts q
  ts="$(now_ms)"
  q="$path_q&timestamp=$ts&recvWindow=$RECV_WINDOW"
  sig="$(sign "$q")"
  req_url="$BINANCE_BASE_URL/api/v3/account?$q&signature=$sig"
  for attempt in $(seq 1 "$RETRY_MAX"); do
    out="$(curl_exec "GET" "$req_url" \
      -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
      || true)"
    if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
      if [ "$BINANCE_BASE_URL" != "$BINANCE_BASE_URL_FALLBACK" ]; then
        BINANCE_BASE_URL="$BINANCE_BASE_URL_FALLBACK"
        req_url="$BINANCE_BASE_URL/api/v3/account?$q&signature=$sig"
        continue
      fi
      http_403_json "/api/v3/account"
      return 0
    fi
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
    sleep "$RETRY_DELAY_SEC"
  done
  return 1
}

private_delete_retry() {
  local path="$1"
  local q="$2"
  local sig out attempt req_url

  sig="$(sign "$q")"
  req_url="$BINANCE_BASE_URL$path?$q&signature=$sig"
  for attempt in $(seq 1 "$RETRY_MAX"); do
    out="$(curl_exec "DELETE" "$req_url" \
      -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
      || true)"
    if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
      if [ "$BINANCE_BASE_URL" != "$BINANCE_BASE_URL_FALLBACK" ]; then
        BINANCE_BASE_URL="$BINANCE_BASE_URL_FALLBACK"
        req_url="$BINANCE_BASE_URL$path?$q&signature=$sig"
        continue
      fi
      http_403_json "$path"
      return 0
    fi
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
    sleep "$RETRY_DELAY_SEC"
  done
  return 1
}

public_get_retry() {
  local path_q="$1"
  local out attempt req_url
  req_url="$BINANCE_BASE_URL$path_q"
  for attempt in $(seq 1 "$RETRY_MAX"); do
    out="$(curl_exec "GET" "$req_url" || true)"
    if [ "${CURL_LAST_HTTP_CODE}" = "403" ]; then
      if [ "$BINANCE_BASE_URL" != "$BINANCE_BASE_URL_FALLBACK" ]; then
        BINANCE_BASE_URL="$BINANCE_BASE_URL_FALLBACK"
        req_url="$BINANCE_BASE_URL$path_q"
        continue
      fi
      http_403_json "$path_q"
      return 0
    fi
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
    sleep "$RETRY_DELAY_SEC"
  done
  return 1
}

composite_price() {
  local symbols_csv="$1"
  local symbol resp px prices
  prices=""
  IFS=',' read -r -a _syms <<< "$symbols_csv"
  for symbol in "${_syms[@]}"; do
    symbol="${symbol//[[:space:]]/}"
    [ -z "$symbol" ] && continue
    resp="$(public_get_retry "/api/v3/ticker/price?symbol=$symbol" || true)"
    px="$(as_num "$(json_get "$resp" "price")")"
    if num_gt "$px" "0"; then
      prices="${prices}${px}\n"
    fi
  done
  if [ -z "$prices" ]; then
    printf "0"
    return 0
  fi
  ruby -e '
    vals=STDIN.read.split.map(&:to_f).select{|x| x > 0}
    if vals.empty?
      print "0"
    else
      printf("%.8f", vals.sum / vals.length)
    end
  ' <<< "$(printf '%b' "$prices")"
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

resonance_buf_push() {
  local buf="$1"
  local v="$2"
  ruby -e '
    vals=STDIN.read.split.map{|x| (Float(x) rescue nil)}.compact
    x=(Float(ARGV[0]) rescue nil)
    vals << x if x
    vals=vals.last(60)
    puts vals.map{|n| format("%.8f", n)}.join("\n")
  ' -- "$v" <<< "$buf"
}

resonance_buf_avg() {
  local buf="$1"
  ruby -e '
    vals=STDIN.read.split.map{|x| (Float(x) rescue nil)}.compact
    if vals.empty?
      print "0"
    else
      printf("%.8f", vals.sum / vals.length)
    end
  ' <<< "$buf"
}

resonance_mode_from_entropy() {
  local e="$1"
  ruby -e '
    x=(Float(ARGV[0]) rescue 0.0)
    if x <= 0.15
      print "NORMAL"
    elsif x <= 0.20
      print "TURBO"
    elsif x <= 0.25
      print "VENTURI"
    else
      print "SAFE"
    end
  ' -- "$e"
}

account_asset_free() {
  local json="$1"
  local asset="$2"
  ruby -rjson -e '
    j=JSON.parse(STDIN.read) rescue {}
    b=(j["balances"] || []).find{|x| x["asset"]==ARGV[0]}
    print((b && b["free"]) ? b["free"] : "0")
  ' "$asset" <<< "$json"
}

num_lt() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a < b ? 0 : 1)' -- "$a" "$b"
}

num_gt() {
  local a="$1"
  local b="$2"
  ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); exit(a > b ? 0 : 1)' -- "$a" "$b"
}

floor_step_qty() {
  local qty="$1"
  local step="$2"
  ruby -e '
    q=(Float(ARGV[0]) rescue 0.0)
    s=(Float(ARGV[1]) rescue 0.00001)
    s=0.00001 if s <= 0.0
    out=((q/s).floor)*s
    printf("%.8f", out)
  ' -- "$qty" "$step"
}

lot_filter_value() {
  local json="$1"
  local key="$2"
  ruby -rjson -e '
    j=JSON.parse(STDIN.read) rescue {}
    sym=(j["symbols"] || [])[0] || {}
    lot=(sym["filters"] || []).find{|f| f["filterType"]=="LOT_SIZE"} || {}
    v=lot[ARGV[0]]
    print(v.nil? ? "" : v)
  ' "$key" <<< "$json"
}

watchdog_on_skip() {
  if [ "$WATCHDOG_ENABLED" != "TRUE" ]; then
    return 0
  fi
  skip_streak=$((skip_streak + 1))
  if [ "$skip_streak" -ge "$WATCHDOG_MAX_SKIP_STREAK" ]; then
    watchdog_tripped=1
  fi
}

sleep_secs_from_ms() {
  local ms="$1"
  ruby -e '
    ms=(ARGV[0].to_f rescue 500.0)
    ms=100.0 if ms < 100.0
    printf("%.3f", ms/1000.0)
  ' -- "$ms"
}

cancel_open_orders_symbol() {
  local ts q cancel_resp
  ts="$(now_ms)"
  q="symbol=$SYMBOL&timestamp=$ts&recvWindow=$RECV_WINDOW"
  cancel_resp="$(private_delete_retry "/api/v3/openOrders" "$q" || true)"
  printf '%s' "$cancel_resp"
}

error_count=0
ok_cycles=0
total_pnl="0.00000000"
stall_streak=0
skip_streak=0
watchdog_tripped=0
fa_smooth="0.0"
soft_cooldown_remaining=0
run_start_sec="$(now_sec)"
prev_order_mass="$BUY_USDT"
resonance_dabs_buf=""
resonance_price_ref_60=""
resonance_ref_ts="$(now_sec)"
resonance_last_mode="NA"
resonance_last_lock="0"
resonance_last_gate="init"
resonance_last_side="FLAT"

# thresholds for current cycle exits
profit_mult="$(num_add "1.0" "$(num_div "$MIN_PROFIT_BPS" "10000")")"
MIN_HOLD_SEC="$(to_int "$MIN_HOLD" "5")"
MAX_HOLD_SEC_VORTEX="$(to_int "$MAX_HOLD" "$MAX_HOLD_SEC")"
STALL_CYCLES="$(to_int "$STALL_DETECTION" "3")"
poll_sleep_sec="$POLL_SEC"
if [ "$CRASH_WATCHDOG_ENABLED" = "TRUE" ]; then
  crash_sleep_sec="$(sleep_secs_from_ms "$CRASH_CHECK_MS")"
  if ruby -e 'a=(ARGV[0].to_f rescue 0.0); b=(ARGV[1].to_f rescue 0.0); exit(a < b ? 0 : 1)' -- "$crash_sleep_sec" "$poll_sleep_sec"; then
    poll_sleep_sec="$crash_sleep_sec"
  fi
fi
structure_lookback_min="$(ruby -e 'e=(ARGV[0].to_i rescue 153); d=[[e/50,3].max,12].min; print d' -- "$EMA_STRUCTURE")"
if [ -n "${STRUCTURE_LOOKBACK_MIN:-}" ] && [ "${STRUCTURE_LOOKBACK_MIN}" != "3" ]; then
  structure_lookback_min="${STRUCTURE_LOOKBACK_MIN}"
fi
lot_step_qty="0.00001000"
lot_min_qty="0.00001000"
init_live_reset_policy
if ! validate_credentials_inputs; then
  exit 1
fi
if ! preflight_live_connectivity; then
  echo "Abort: preflight echec (reseau/proxy/credentials)."
  exit 1
fi
if exinfo_resp="$(public_get_retry "/api/v3/exchangeInfo?symbol=$SYMBOL")"; then
  parsed_step="$(lot_filter_value "$exinfo_resp" "stepSize")"
  parsed_min="$(lot_filter_value "$exinfo_resp" "minQty")"
  if [ -n "$parsed_step" ]; then
    lot_step_qty="$parsed_step"
  fi
  if [ -n "$parsed_min" ]; then
    lot_min_qty="$parsed_min"
  fi
fi
init_px_resp="$(public_get_retry "/api/v3/ticker/price?symbol=$SYMBOL" || true)"
resonance_price_ref_60="$(as_num "$(json_get "$init_px_resp" "price")")"
if ! num_gt "$resonance_price_ref_60" "0"; then
  resonance_price_ref_60="0"
fi

for i in $(seq 1 "$CYCLES"); do
  if [ -f "$STOP_FILE" ]; then
    echo "STOP file detected ($STOP_FILE). Stopping safely at cycle $i."
    break
  fi

  cycle_soft_mode=0
  cycle_stop_loss_bps="$STOP_LOSS_BPS"
  cycle_trail_giveback_bps="$TRAIL_GIVEBACK_BPS"
  cycle_soft_hold_cap=""

  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && [ "$soft_cooldown_remaining" -gt 0 ]; then
    cycle_soft_mode=1
    cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
    cycle_trail_giveback_bps="$SOFT_TRAIL_GIVEBACK_BPS"
    cycle_soft_hold_cap="$SOFT_MAX_HOLD_SEC"
    soft_cooldown_remaining=$((soft_cooldown_remaining - 1))
  fi

  fatigue_score="$(num_div "$stall_streak" "$STALL_CYCLES")"
  cycle_buy_usdt="$BUY_USDT"
  if [ "$DYNAMIC_MASS" = "TRUE" ]; then
    cycle_buy_usdt="$(compute_order_mass "$BASE_MASS" "$BOOST_FACTOR" "$fa_smooth" "$FORCE_THRESHOLD" "$fatigue_score" "$FATIGUE_THRESHOLD")"
  fi
  if [ "$ORDER_SMOOTHING" = "TRUE" ]; then
    # EMA smoothing prevents abrupt order-size jumps between cycles.
    cycle_buy_usdt="$(num_add "$(num_mul "$prev_order_mass" "$ORDER_SMOOTH_ALPHA")" "$(num_mul "$cycle_buy_usdt" "$(num_sub "1.0" "$ORDER_SMOOTH_ALPHA")")")"
  fi
  if [ "$cycle_soft_mode" -eq 1 ]; then
    cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
    if num_lt "$cycle_buy_usdt" "5"; then
      cycle_buy_usdt="5"
    fi
  fi
  prev_order_mass="$cycle_buy_usdt"

  # Pre-entry microstructure guards: spread/slippage and top-of-book liquidity.
  book_resp=""
  if book_resp="$(public_get_retry "/api/v3/ticker/bookTicker?symbol=$SYMBOL")"; then
    bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"
    ask_px="$(as_num "$(json_get "$book_resp" "askPrice")")"
    bid_qty_top="$(as_num "$(json_get "$book_resp" "bidQty")")"
    ask_qty_top="$(as_num "$(json_get "$book_resp" "askQty")")"

    spread_px="$(num_sub "$ask_px" "$bid_px")"
    spread_bps="$(num_mul "$(num_div "$spread_px" "$ask_px")" "10000")"

    if num_gt "$spread_bps" "$MAX_SLIPPAGE_BPS"; then
      echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,spread_bps=$spread_bps > $MAX_SLIPPAGE_BPS" >> "$LOG_FILE"
      echo "Cycle $i SKIP | spread too high: ${spread_bps} bps"
      watchdog_on_skip
      if [ "$watchdog_tripped" -eq 1 ]; then
        echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
        break
      fi
      sleep "$SLEEP_SEC"
      continue
    fi

    if [ "$MIN_LIQUIDITY_CHECK" = "TRUE" ]; then
      need_qty="$(num_mul "$(num_div "$cycle_buy_usdt" "$ask_px")" "$LIQUIDITY_BUFFER")"
      if num_lt "$ask_qty_top" "$need_qty" || num_lt "$bid_qty_top" "$need_qty"; then
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,liquidity_low need=$need_qty askQty=$ask_qty_top bidQty=$bid_qty_top mass=$cycle_buy_usdt" >> "$LOG_FILE"
        echo "Cycle $i SKIP | liquidity low: need=$need_qty askQty=$ask_qty_top bidQty=$bid_qty_top"
        watchdog_on_skip
        if [ "$watchdog_tripped" -eq 1 ]; then
          echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
          break
        fi
        sleep "$SLEEP_SEC"
        continue
      fi
    fi
  fi

  # Direction signal (very short momentum): up => long-first, down => short-first if BTC inventory allows.
  entry_side="BUY"
  exit_side="SELL"
  entry_mode_used="long_first"
  tick_bps_abs="0"
  radar_reason="none"
  radar_conf="0"
  radar_direction="long"
  if [ "$MODE" = "BOTH_SPOT" ]; then
    if [ "$INDEX_MODE" = "TRUE" ]; then
      p1="$(composite_price "$INDEX_SYMBOLS")"
      sleep "$MOMENTUM_SLEEP_SEC"
      p2="$(composite_price "$INDEX_SYMBOLS")"
    else
      p1_resp="$(public_get_retry "/api/v3/ticker/price?symbol=$SYMBOL" || true)"
      sleep "$MOMENTUM_SLEEP_SEC"
      p2_resp="$(public_get_retry "/api/v3/ticker/price?symbol=$SYMBOL" || true)"
      p1="$(as_num "$(json_get "$p1_resp" "price")")"
      p2="$(as_num "$(json_get "$p2_resp" "price")")"
    fi
    mom_bps="$(bps_change "$p1" "$p2")"
    tick_bps_abs="$(abs_num "$mom_bps")"
    mom_direction="neutral"
    if num_ge "$mom_bps" "$MOMENTUM_THRESHOLD_BPS"; then
      mom_direction="long"
    elif num_le "$mom_bps" "-$MOMENTUM_THRESHOLD_BPS"; then
      mom_direction="short"
    fi

    structure_direction="neutral"
    structure_trend_bps="0"
    if [ "$TREND_FILTER" = "TRUE" ]; then
      trend_limit=$((structure_lookback_min + 1))
      trend_resp="$(public_get_retry "/api/v3/klines?symbol=$SYMBOL&interval=1m&limit=$trend_limit" || true)"
      structure_trend_bps="$(trend_bps_from_klines "$trend_resp")"
      if num_ge "$structure_trend_bps" "1"; then
        structure_direction="long"
      elif num_le "$structure_trend_bps" "-1"; then
        structure_direction="short"
      fi
    fi

    # RESONANCE + HOLOGRAPHIC MEMORY gate: mandatory live entry condition.
    resonance_allow="true"
    resonance_reason="resonance_off"
    resonance_mode="NA"
    resonance_side="FLAT"
    resonance_holo_gate="PASS"
    resonance_phase_lock="0"
    resonance_mkt_hz="0"
    if [ "$RESONANCE_GATE_ENABLED" = "TRUE" ]; then
      if [ "$INDEX_MODE" = "TRUE" ]; then
        rpx_resp="$(public_get_retry "/api/v3/ticker/price?symbol=$SYMBOL" || true)"
        resonance_px_now="$(as_num "$(json_get "$rpx_resp" "price")")"
      else
        resonance_px_now="$p2"
      fi
      if ! num_gt "$resonance_px_now" "0"; then
        resonance_px_now="$p1"
      fi
      if ! num_gt "$resonance_price_ref_60" "0"; then
        resonance_price_ref_60="$resonance_px_now"
      fi
      resonance_delta_abs="$(abs_num "$(num_sub "$resonance_px_now" "$p1")")"
      resonance_dabs_buf="$(resonance_buf_push "$resonance_dabs_buf" "$resonance_delta_abs")"
      resonance_atr="$(resonance_buf_avg "$resonance_dabs_buf")"
      resonance_tickvel="$(num_div "$resonance_atr" "$MOMENTUM_SLEEP_SEC")"
      resonance_atr_norm="$(ruby -e 'a=(Float(ARGV[0]) rescue 0.0); r=(Float(ARGV[1]) rescue 200.0); s=(Float(ARGV[2]) rescue 1500.0); x=(a-r)/(s-r); x=0.0 if x<0.0; x=1.0 if x>1.0; printf("%.8f", x)' -- "$resonance_atr" "$RANGE_USD" "$SPIKE_USD")"
      resonance_tv_norm="$(ruby -e 't=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 5.0); s=(Float(ARGV[2]) rescue 60.0); x=(t-b)/(s-b); x=0.0 if x<0.0; x=1.0 if x>1.0; printf("%.8f", x)' -- "$resonance_tickvel" "$TICK_BASE_USD" "$TICK_SPIKE_USD")"
      resonance_vm="$(num_mul "$resonance_atr_norm" "$resonance_tv_norm")"
      # Live mkt_hz must breathe every cycle (5s): use vm + real tick/spread components.
      resonance_mkt_hz="$(ruby -e 'vm=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); s=(Float(ARGV[2]) rescue 0.0); hz=0.1 + (vm*4.0) + (b*0.25) + (s*0.40); hz=0.1 if hz<0.1; hz=20.0 if hz>20.0; printf("%.8f", hz)' -- "$resonance_vm" "$tick_bps_abs" "$spread_bps")"
      resonance_phase_lock="$(ruby -e 'mhz=(Float(ARGV[0]) rescue 0.1); ahz=(Float(ARGV[1]) rescue 7.2); d=(mhz-ahz).abs; s=1.0-(d/20.0); s=0.0 if s<0.0; s=1.0 if s>1.0; printf("%.8f", s)' -- "$resonance_mkt_hz" "$V_ACE_HZ")"
      resonance_entropy="$(ruby -e 'b=(Float(ARGV[0]) rescue 0.0); e=0.08 + ((b/80.0)*0.22); e=0.08 if e<0.08; e=0.30 if e>0.30; printf("%.8f", e)' -- "$tick_bps_abs")"
      resonance_mode="$(resonance_mode_from_entropy "$resonance_entropy")"
      if num_ge "$tick_bps_abs" "$RESONANCE_PANIC_BPS"; then
        resonance_mode="SAFE"
      elif num_ge "$tick_bps_abs" "$RESONANCE_FAST_BPS" && [ "$resonance_mode" = "NORMAL" ]; then
        resonance_mode="VENTURI"
      fi
      mom60_bps="$(bps_change "$resonance_price_ref_60" "$resonance_px_now")"
      resonance_side="FLAT"
      if num_gt "$mom60_bps" "0"; then
        resonance_side="LONG"
      elif num_lt "$mom60_bps" "0"; then
        resonance_side="SHORT"
      fi
      now_ref="$(now_sec)"
      if [ $((now_ref - resonance_ref_ts)) -ge 60 ]; then
        resonance_ref_ts="$now_ref"
        resonance_price_ref_60="$resonance_px_now"
      fi
      resonance_holo_gate="PASS"
      if [ "$HOLO_STRICT" = "TRUE" ]; then
        if [ "$HOLO_MACRO_BIAS" = "BEAR" ] && [ "$resonance_side" = "LONG" ]; then
          resonance_holo_gate="BLOCK_LONG_HOLO"
        elif [ "$HOLO_MACRO_BIAS" = "BULL" ] && [ "$resonance_side" = "SHORT" ]; then
          resonance_holo_gate="BLOCK_SHORT_HOLO"
        fi
      fi
      resonance_phase_lock_min_eff="$RESONANCE_PHASE_LOCK_MIN"
      if [ "$HOLO_STRICT" = "TRUE" ]; then
        resonance_phase_lock_min_eff="$RESONANCE_STRICT_LOCK_MIN"
      fi
      resonance_structure_ok="false"
      if [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
        if [ "$structure_direction" = "long" ] && [ "$resonance_side" = "LONG" ]; then
          resonance_structure_ok="true"
        elif [ "$structure_direction" = "short" ] && [ "$resonance_side" = "SHORT" ]; then
          resonance_structure_ok="true"
        fi
      fi
      resonance_allow="true"
      resonance_reason="ok"
      if [ "$resonance_mode" = "SAFE" ]; then
        resonance_mode_lc="$(printf '%s' "$resonance_mode" | tr '[:upper:]' '[:lower:]')"
        resonance_allow="false"
        resonance_reason="mode_${resonance_mode_lc}"
      elif [ "$resonance_mode" = "NORMAL" ] && [ "$resonance_structure_ok" != "true" ] && num_lt "$resonance_phase_lock" "$resonance_phase_lock_min_eff"; then
        resonance_allow="false"
        resonance_reason="mode_normal_no_structure"
      elif [ "$resonance_side" = "FLAT" ]; then
        resonance_allow="false"
        resonance_reason="flat_side"
      elif num_lt "$resonance_phase_lock" "$resonance_phase_lock_min_eff"; then
        resonance_allow="false"
        resonance_reason="phase_lock_low"
      elif [ "$resonance_holo_gate" != "PASS" ]; then
        resonance_holo_gate_lc="$(printf '%s' "$resonance_holo_gate" | tr '[:upper:]' '[:lower:]')"
        resonance_allow="false"
        resonance_reason="${resonance_holo_gate_lc}"
      fi
      resonance_last_mode="$resonance_mode"
      resonance_last_lock="$resonance_phase_lock"
      resonance_last_gate="$resonance_reason"
      resonance_last_side="$resonance_side"
      if [ "$resonance_allow" != "true" ]; then
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,resonance_block reason=$resonance_reason mode=$resonance_mode side=$resonance_side lock=$resonance_phase_lock lock_min=$resonance_phase_lock_min_eff mkt_hz=$resonance_mkt_hz struct_ok=$resonance_structure_ok" >> "$LOG_FILE"
        echo "Cycle $i SKIP | resonance blocked: reason=$resonance_reason mode=$resonance_mode side=$resonance_side lock=$resonance_phase_lock lock_min=$resonance_phase_lock_min_eff mkt_hz=$resonance_mkt_hz"
        watchdog_on_skip
        if [ "$watchdog_tripped" -eq 1 ]; then
          echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
          break
        fi
        sleep "$SLEEP_SEC"
        continue
      fi
    fi

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
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,radar_block reason=$radar_reason conf=$radar_conf mom_bps=$mom_bps spread_bps=$spread_bps" >> "$LOG_FILE"
        echo "Cycle $i SKIP | radar blocked: reason=$radar_reason conf=$radar_conf"
        watchdog_on_skip
        if [ "$watchdog_tripped" -eq 1 ]; then
          echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
          break
        fi
        sleep "$SLEEP_SEC"
        continue
      fi
    else
      radar_direction="$mom_direction"
      if [ "$radar_direction" = "neutral" ]; then
        radar_direction="long"
      fi
      radar_reason="radar_off"
      radar_conf="0.5"
    fi

    # Structure overrides micro direction when trend exists.
    if [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
      radar_direction="$structure_direction"
    fi

    # Tactic crossover gate: only trade when micro direction aligns with structure.
    if [ "$ENTRY_SIGNAL" = "CROSSOVER" ] && [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" != "neutral" ]; then
      if [ "$mom_direction" != "neutral" ] && [ "$mom_direction" != "$structure_direction" ]; then
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,tactic_mismatch mom=$mom_direction structure=$structure_direction trend_bps=$structure_trend_bps" >> "$LOG_FILE"
        echo "Cycle $i SKIP | tactic mismatch mom=$mom_direction structure=$structure_direction"
        watchdog_on_skip
        if [ "$watchdog_tripped" -eq 1 ]; then
          echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
          break
        fi
        sleep "$SLEEP_SEC"
        continue
      fi
    fi

    if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$tick_bps_abs" "$ANOMALY_TICK_BPS"; then
      cycle_soft_mode=1
      cycle_stop_loss_bps="$SOFT_STOP_LOSS_BPS"
      cycle_trail_giveback_bps="$SOFT_TRAIL_GIVEBACK_BPS"
      cycle_soft_hold_cap="$SOFT_MAX_HOLD_SEC"
      cycle_buy_usdt="$(num_mul "$cycle_buy_usdt" "$SOFT_MASS_FACTOR")"
      if num_lt "$cycle_buy_usdt" "5"; then
        cycle_buy_usdt="5"
      fi
      soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
      echo "Cycle $i SOFT anomaly mode ON | tick_bps=${tick_bps_abs} > ${ANOMALY_TICK_BPS}"
    fi
    if [ "$radar_direction" = "short" ] && num_le "$mom_bps" "-$MOMENTUM_THRESHOLD_BPS"; then
      # Check BTC free for a SELL-first cycle in spot.
      acct_resp="$(private_get_retry "omitZeroBalances=false" || true)"
      btc_free="$(as_num "$(account_asset_free "$acct_resp" "BTC")")"
      raw_sell_qty="$(as_num "$(num_div "$cycle_buy_usdt" "$ask_px")")"
      sell_qty_needed="$(floor_step_qty "$raw_sell_qty" "$lot_step_qty")"
      if num_ge "$sell_qty_needed" "$lot_min_qty" && num_ge "$btc_free" "$sell_qty_needed"; then
        entry_side="SELL"
        exit_side="BUY"
        entry_mode_used="short_first_spot"
      elif [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" = "short" ]; then
        # Hard structure enforcement: in short structure, do not fallback to BUY when SELL inventory is insufficient.
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,structure_short_no_inventory need=$sell_qty_needed btc_free=$btc_free" >> "$LOG_FILE"
        echo "Cycle $i SKIP | structure short enforced, insufficient BTC inventory"
        watchdog_on_skip
        if [ "$watchdog_tripped" -eq 1 ]; then
          echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
          break
        fi
        sleep "$SLEEP_SEC"
        continue
      fi
    elif [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" = "short" ]; then
      # Hard structure enforcement: do not BUY against short structure.
      echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,,,$ask_px,structure_short_block_buy mom_bps=$mom_bps trend_bps=$structure_trend_bps" >> "$LOG_FILE"
      echo "Cycle $i SKIP | structure short enforced, BUY blocked"
      watchdog_on_skip
      if [ "$watchdog_tripped" -eq 1 ]; then
        echo "Watchdog triggered: skip streak reached $WATCHDOG_MAX_SKIP_STREAK cycles. Stopping safely."
        break
      fi
      sleep "$SLEEP_SEC"
      continue
    elif [ "$TREND_FILTER" = "TRUE" ] && [ "$structure_direction" = "long" ]; then
      # Keep long structure explicit.
      entry_side="BUY"
      exit_side="SELL"
      entry_mode_used="long_first"
    fi
  fi

  ts="$(now_ms)"
  if [ "$entry_side" = "BUY" ]; then
    q_entry="symbol=$SYMBOL&side=BUY&type=MARKET&quoteOrderQty=$cycle_buy_usdt&timestamp=$ts&recvWindow=$RECV_WINDOW"
  else
    q_entry="symbol=$SYMBOL&side=SELL&type=MARKET&quantity=$sell_qty_needed&timestamp=$ts&recvWindow=$RECV_WINDOW"
  fi

  if ! entry_resp="$(private_post_retry "/api/v3/order" "$q_entry")"; then
    error_count=$((error_count + 1))
    echo "$(date -u +%FT%TZ),$i,ENTRY,ERROR,,,,,,,network_or_timeout mode=$entry_mode_used" >> "$LOG_FILE"
    echo "Cycle $i ENTRY failed (network/timeout). errors=$error_count/$MAX_ERRORS"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then break; fi
    sleep "$SLEEP_SEC"
    continue
  fi

  entry_code="$(json_get "$entry_resp" "code")"
  if [ -n "$entry_code" ]; then
    error_count=$((error_count + 1))
    entry_msg="$(json_get "$entry_resp" "msg")"
    echo "$(date -u +%FT%TZ),$i,ENTRY,ERROR,,,,,,,code=$entry_code msg=$entry_msg mode=$entry_mode_used" >> "$LOG_FILE"
    echo "Cycle $i ENTRY API error: code=$entry_code msg=$entry_msg"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then break; fi
    sleep "$SLEEP_SEC"
    continue
  fi

  entry_qty="$(json_get "$entry_resp" "executedQty")"
  entry_id="$(json_get "$entry_resp" "orderId")"
  entry_quote="$(as_num "$(json_get "$entry_resp" "cummulativeQuoteQty")")"
  skip_streak=0
  entry_avg="$(num_div "$entry_quote" "$entry_qty")"
  loss_mult_cycle="$(num_sub "1.0" "$(num_div "$cycle_stop_loss_bps" "10000")")"
  stop_price_long="$(num_mul "$entry_avg" "$loss_mult_cycle")"
  target_price_long="$(num_mul "$entry_avg" "$profit_mult")"

  echo "$(date -u +%FT%TZ),$i,ENTRY,FILLED,$entry_id,$entry_qty,$entry_quote,,,,,ok side=$entry_side mode=$entry_mode_used mass=$cycle_buy_usdt soft=$cycle_soft_mode radar_dir=$radar_direction radar_conf=$radar_conf radar_reason=$radar_reason resonance_mode=${resonance_last_mode:-na} resonance_side=${resonance_last_side:-na} resonance_lock=${resonance_last_lock:-0} resonance_gate=${resonance_last_gate:-na} structure_dir=${structure_direction:-na} trend_bps=${structure_trend_bps:-0}" >> "$LOG_FILE"

  start_sec="$(now_sec)"
  exit_reason="timeout"
  ref_price="$entry_avg"
  peak_bps="-999999.00000000"
  cycle_max_hold="$TACTIC_MAX_HOLD_SEC"
  if [ "$DYNAMIC_TIMEOUT" = "TRUE" ]; then
    # Relativity law: F_a = (vol_rel * volume_asp) / S-Ratio, T_hold = T_base/(1+F_a*K)
    vol_rel="$(num_div "$spread_bps" "10000")"
    vol_asp="$(num_div "$(num_mul "$(num_add "$ask_qty_top" "$bid_qty_top")" "$ask_px")" "$BUY_USDT")"
    fa_raw="$(compute_fa "$vol_rel" "$vol_asp" "$S_RATIO")"
    fa_smooth="$(ema "$fa_smooth" "$fa_raw" "$F_A_SMOOTHING")"
    cycle_max_hold="$(compute_hold_relativity "$T_BASE" "$fa_smooth" "$K_ENTROPY" "$MIN_HOLD_SEC" "$MAX_HOLD_SEC_VORTEX")"
    if [ "$TIME_IS_VARIABLE" = "TRUE" ]; then
      cycle_max_hold="$(apply_time_elasticity "$cycle_max_hold" "$fa_smooth" "$FORCE_THRESHOLD" "$MASS_EXPANSION_RATIO" "$MIN_HOLD_SEC" "$MAX_HOLD_SEC_VORTEX")"
    fi
  fi
  if [ -n "$cycle_soft_hold_cap" ] && num_gt "$cycle_max_hold" "$cycle_soft_hold_cap"; then
    cycle_max_hold="$cycle_soft_hold_cap"
  fi

  prev_bps=""
  prev_ts="$(now_sec)"
  slow_velocity_count=0
  fatigue_count=0
  cycle_stall_confirmations="$STALL_CONFIRMATIONS"
  while true; do
    if [ -f "$STOP_FILE" ]; then
      exit_reason="kill_switch"
      break
    fi

    now_s="$(now_sec)"
    hold_sec=$((now_s - start_sec))
    if [ "$WATCHDOG_ENABLED" = "TRUE" ] && [ "$hold_sec" -ge "$WATCHDOG_MAX_CYCLE_SEC" ]; then
      exit_reason="watchdog_cycle_cap"
      break
    fi
    if [ "$hold_sec" -ge "$cycle_max_hold" ]; then
      exit_reason="timeout"
      break
    fi

    if ticker_resp="$(public_get_retry "/api/v3/ticker/price?symbol=$SYMBOL")"; then
      px="$(as_num "$(json_get "$ticker_resp" "price")")"
      ref_price="$px"

      current_bps="$(bps_change "$entry_avg" "$px")"
      if num_ge "$current_bps" "$peak_bps"; then
        peak_bps="$current_bps"
      fi
      if [ "$CRASH_WATCHDOG_ENABLED" = "TRUE" ]; then
        if [ "$entry_side" = "BUY" ]; then
          if num_le "$current_bps" "-$CRASH_ALERT_BPS"; then
            exit_reason="crash_watchdog"
            break
          fi
        else
          short_bps="$(num_sub "0" "$current_bps")"
          if num_le "$short_bps" "-$CRASH_ALERT_BPS"; then
            exit_reason="crash_watchdog"
            break
          fi
        fi
      fi

      now_tick="$(now_sec)"
      dt=$((now_tick - prev_ts))
      if [ "$dt" -le 0 ]; then dt=1; fi
      if [ -n "$prev_bps" ]; then
        delta_bps="$(num_sub "$current_bps" "$prev_bps")"
        vel_bps_s="$(num_div "$(abs_num "$delta_bps")" "$dt")"
        if [ "$CALORIE_EFFICIENCY_EXIT" = "TRUE" ] && [ "$hold_sec" -ge "$MIN_HOLD_SEC" ]; then
          if num_lt "$vel_bps_s" "$STALL_THRESHOLD_BPS_PER_SEC"; then
            slow_velocity_count=$((slow_velocity_count + 1))
          else
            slow_velocity_count=0
          fi
          min_stall_abs="$(num_div "$MIN_STALL_BPS" "10000")"
          if num_lt "$(abs_num "$current_bps")" "$MIN_STALL_BPS"; then
            slow_velocity_count=$((slow_velocity_count + 1))
          fi
          if [ "$slow_velocity_count" -ge "$cycle_stall_confirmations" ]; then
            if [ "$EXIT_BY_FATIGUE" = "TRUE" ]; then
              if num_lt "$fa_smooth" "$FORCE_THRESHOLD"; then
                fatigue_count=$((fatigue_count + 1))
              else
                fatigue_count=0
              fi
              if [ "$fatigue_count" -ge "$cycle_stall_confirmations" ]; then
                exit_reason="exit_fatigue"
                break
              fi
            else
              exit_reason="exit_stall"
              break
            fi
          fi
        fi
      fi
      prev_bps="$current_bps"
      prev_ts="$now_tick"

      if [ "$entry_side" = "BUY" ]; then
        if num_le "$px" "$stop_price_long"; then
          exit_reason="stop_loss"
          break
        fi
      else
        short_bps="$(num_sub "0" "$current_bps")"
        if num_le "$short_bps" "-$cycle_stop_loss_bps"; then
          exit_reason="stop_loss"
          break
        fi
      fi

      if [ "$entry_side" = "BUY" ]; then
        if [ "$USE_TRAILING" = "1" ]; then
          if num_ge "$peak_bps" "$TRAIL_ARM_BPS"; then
            trail_floor="$(num_sub "$peak_bps" "$cycle_trail_giveback_bps")"
            if num_le "$current_bps" "$trail_floor"; then
              exit_reason="trailing_stop"
              break
            fi
          fi
        else
          if num_ge "$px" "$target_price_long"; then
            exit_reason="target"
            break
          fi
        fi
      else
        short_bps="$(num_sub "0" "$current_bps")"
        if [ "$USE_TRAILING" = "1" ]; then
          if num_ge "$short_bps" "$TRAIL_ARM_BPS"; then
            short_trail_floor="$(num_sub "$short_bps" "$cycle_trail_giveback_bps")"
            # re-evaluate on next tick via last short bps by checking giveback relative to peak surrogate
            if [ -n "${short_peak_bps:-}" ]; then
              short_trail_floor="$(num_sub "$short_peak_bps" "$cycle_trail_giveback_bps")"
              if num_le "$short_bps" "$short_trail_floor"; then
                exit_reason="trailing_stop"
                break
              fi
            fi
            short_peak_bps="${short_peak_bps:-$short_bps}"
            if num_ge "$short_bps" "$short_peak_bps"; then
              short_peak_bps="$short_bps"
            fi
          fi
        else
          if num_ge "$short_bps" "$MIN_PROFIT_BPS"; then
            exit_reason="target"
            break
          fi
        fi
      fi
    fi

    sleep "$poll_sleep_sec"
  done

  if [ "$exit_reason" = "crash_watchdog" ]; then
    cancel_msg="$(cancel_open_orders_symbol || true)"
    if [ -n "$cancel_msg" ]; then
      echo "Cycle $i WATCHDOG | cancel_open_orders attempted before market exit"
    fi
  fi

  ts="$(now_ms)"
  if [ "$exit_side" = "SELL" ]; then
    q_exit="symbol=$SYMBOL&side=SELL&type=MARKET&quantity=$entry_qty&timestamp=$ts&recvWindow=$RECV_WINDOW"
  else
    q_exit="symbol=$SYMBOL&side=BUY&type=MARKET&quantity=$entry_qty&timestamp=$ts&recvWindow=$RECV_WINDOW"
  fi
  if ! exit_resp="$(private_post_retry "/api/v3/order" "$q_exit")"; then
    error_count=$((error_count + 1))
    hold_done=$(( $(now_sec) - start_sec ))
    echo "$(date -u +%FT%TZ),$i,EXIT,ERROR,,,,,${exit_reason},$hold_done,$ref_price,network_or_timeout side=$exit_side" >> "$LOG_FILE"
    echo "Cycle $i EXIT failed (network/timeout). errors=$error_count/$MAX_ERRORS"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then break; fi
    sleep "$SLEEP_SEC"
    continue
  fi

  exit_code="$(json_get "$exit_resp" "code")"
  if [ -n "$exit_code" ]; then
    error_count=$((error_count + 1))
    exit_msg="$(json_get "$exit_resp" "msg")"
    hold_done=$(( $(now_sec) - start_sec ))
    echo "$(date -u +%FT%TZ),$i,EXIT,ERROR,,,,,${exit_reason},$hold_done,$ref_price,code=$exit_code msg=$exit_msg side=$exit_side" >> "$LOG_FILE"
    echo "Cycle $i EXIT API error: code=$exit_code msg=$exit_msg"
    if [ "$error_count" -ge "$MAX_ERRORS" ]; then break; fi
    sleep "$SLEEP_SEC"
    continue
  fi

  exit_qty="$(json_get "$exit_resp" "executedQty")"
  exit_id="$(json_get "$exit_resp" "orderId")"
  exit_quote="$(as_num "$(json_get "$exit_resp" "cummulativeQuoteQty")")"
  if [ "$entry_side" = "BUY" ]; then
    pnl_cycle="$(num_sub "$exit_quote" "$entry_quote")"
  else
    pnl_cycle="$(num_sub "$entry_quote" "$exit_quote")"
  fi
  pnl_abs="$(abs_num "$pnl_cycle")"
  if [ "$ANOMALY_SOFT_MODE" = "TRUE" ] && num_gt "$pnl_abs" "$ANOMALY_PNL_USDT"; then
    soft_cooldown_remaining="$SOFT_COOLDOWN_CYCLES"
    echo "Cycle $i SOFT anomaly mode ON | pnl_abs=${pnl_abs} > ${ANOMALY_PNL_USDT}"
  fi
  total_pnl="$(num_add "$total_pnl" "$pnl_cycle")"
  ok_cycles=$((ok_cycles + 1))
  hold_done=$(( $(now_sec) - start_sec ))

  echo "$(date -u +%FT%TZ),$i,EXIT,FILLED,$exit_id,$exit_qty,$exit_quote,$pnl_cycle,$exit_reason,$hold_done,$ref_price,ok side=$exit_side mode=$entry_mode_used soft=$cycle_soft_mode" >> "$LOG_FILE"
  echo "Cycle $i OK | mode=$entry_mode_used reason=$exit_reason hold=${hold_done}s | ENTRY=$entry_quote EXIT=$exit_quote | PnL=$pnl_cycle"
  if [ "$exit_reason" = "timeout" ] || [ "$exit_reason" = "stop_loss" ]; then
    stall_streak=$((stall_streak + 1))
  else
    stall_streak=0
  fi
  sleep "$SLEEP_SEC"
done

echo
echo "Run complete."
run_end_sec="$(now_sec)"
elapsed_total_sec=$((run_end_sec - run_start_sec))
elapsed_total_min="$(ruby -e 's=(ARGV[0].to_f rescue 0.0); printf("%.2f", s/60.0)' -- "$elapsed_total_sec")"
echo "Symbol: $SYMBOL"
echo "Requested cycles: $CYCLES"
echo "Successful cycles: $ok_cycles"
echo "Errors: $error_count"
echo "Elapsed total: ${elapsed_total_sec}s (${elapsed_total_min}m)"
echo "Total PnL (quote): $total_pnl USDT"
echo "Profit target: +${MIN_PROFIT_BPS} bps"
echo "Stop loss: -${STOP_LOSS_BPS} bps"
if [ "$USE_TRAILING" = "1" ]; then
  echo "Trailing: armed at +${TRAIL_ARM_BPS} bps, giveback ${TRAIL_GIVEBACK_BPS} bps"
fi
if [ "$DYNAMIC_TIMEOUT" = "TRUE" ]; then
  echo "Max hold: dynamic relativity (T_BASE=${T_BASE}s, K=${K_ENTROPY}, min=${MIN_HOLD_SEC}s, max=${MAX_HOLD_SEC_VORTEX}s, smoothing=${F_A_SMOOTHING}, S_RATIO=${S_RATIO})"
  if [ "$TIME_IS_VARIABLE" = "TRUE" ]; then
    echo "Elastic time: ratio=${MASS_EXPANSION_RATIO}, force_threshold=${FORCE_THRESHOLD}"
  fi
  if [ "$EXIT_BY_FATIGUE" = "TRUE" ]; then
    echo "Fatigue exit: enabled (confirmations=${FATIGUE_CONFIRMATIONS}, stall_bps_s=${STALL_THRESHOLD_BPS_PER_SEC})"
  fi
else
  echo "Max hold: ${MAX_HOLD_SEC}s"
fi
if [ "$DYNAMIC_MASS" = "TRUE" ]; then
  echo "Dynamic mass: base=${BASE_MASS}, boost=${BOOST_FACTOR}, fatigue_threshold=${FATIGUE_THRESHOLD}"
fi
if [ "$ANOMALY_SOFT_MODE" = "TRUE" ]; then
  echo "Anomaly soft mode: ON (tick>${ANOMALY_TICK_BPS}bps, abs_pnl>${ANOMALY_PNL_USDT}, cooldown=${SOFT_COOLDOWN_CYCLES})"
fi
if [ "$INDEX_MODE" = "TRUE" ]; then
  echo "Index mode: ON (symbols=${INDEX_SYMBOLS})"
fi
if [ "$RESONANCE_GATE_ENABLED" = "TRUE" ]; then
  echo "Resonance gate: ON (V_ACE_HZ=${V_ACE_HZ}, phase_lock_min=${RESONANCE_PHASE_LOCK_MIN}, strict_lock_min=${RESONANCE_STRICT_LOCK_MIN}, fast=${RESONANCE_FAST_BPS}bps, panic=${RESONANCE_PANIC_BPS}bps, holo_bias=${HOLO_MACRO_BIAS}, holo_strict=${HOLO_STRICT})"
fi
if [ "$WATCHDOG_ENABLED" = "TRUE" ]; then
  echo "Watchdog: ON (max_skip_streak=${WATCHDOG_MAX_SKIP_STREAK}, max_cycle_sec=${WATCHDOG_MAX_CYCLE_SEC})"
fi
if [ "$CRASH_WATCHDOG_ENABLED" = "TRUE" ]; then
  echo "Crash watchdog: ON (alert=-${CRASH_ALERT_BPS}bps, check_ms=${CRASH_CHECK_MS}, action=CANCEL_ALL_ORDERS+MARKET_EXIT)"
fi
echo "Log: $LOG_FILE"
echo "Kill switch file: $STOP_FILE"
echo
echo "PnL reel par cycle:"
ruby -rcsv -e '
  file=ARGV[0]
  rows=CSV.read(file, headers:true) rescue []
  cumul=0.0
  printed=false
  rows.each do |r|
    next unless r["side"]=="EXIT" && r["status"]=="FILLED"
    cycle=(r["cycle"] || "").to_s
    pnl=(Float(r["pnl"]) rescue 0.0)
    reason=(r["exitReason"] || "")
    hold=(r["holdSec"] || "")
    cumul += pnl
    puts "  cycle=#{cycle} pnl=#{format("%.8f", pnl)} cumul=#{format("%.8f", cumul)} reason=#{reason} hold=#{hold}s"
    printed=true
  end
  puts "  (aucun cycle rempli)" unless printed
' -- "$LOG_FILE"
