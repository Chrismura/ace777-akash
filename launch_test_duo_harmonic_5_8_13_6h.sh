#!/usr/bin/env bash
set -euo pipefail

# Prefer container workspace on Akash, fallback to script directory locally.
if [ -d /app ]; then
  cd /app
else
  cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

# Test 12h30 - Duo Harmonic 5-8-13
# - BETA (Scout): x5
# - ALPHA (Hunter): x8
# - Burst harmonique: 8 * 1.625 = 13 (via revenge mult)
# - Stop global panier: -5 USDT

# Charge systematique des cles depuis fichier local securise.
# But: eviter les re-saisies et neutraliser les variables shell corrompues.
KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
SHELL_KEY_BEFORE="${BINANCE_API_KEY:-}"
SHELL_SECRET_BEFORE="${BINANCE_API_SECRET:-}"
load_keys_from_file() {
  local key_line secret_line key_val secret_val
  [[ -f "$KEYS_FILE" ]] || return 0

  key_line="$(awk -F= '/^export BINANCE_API_KEY=/{print $0; exit}' "$KEYS_FILE" | tr -d '\r')"
  secret_line="$(awk -F= '/^export BINANCE_API_SECRET=/{print $0; exit}' "$KEYS_FILE" | tr -d '\r')"
  [[ -n "$key_line" && -n "$secret_line" ]] || return 0

  key_val="${key_line#export BINANCE_API_KEY=}"
  secret_val="${secret_line#export BINANCE_API_SECRET=}"

  # Retire guillemets englobants si presents.
  key_val="${key_val%\"}"
  key_val="${key_val#\"}"
  secret_val="${secret_val%\"}"
  secret_val="${secret_val#\"}"

  # Ne jamais executer le contenu du fichier; uniquement affecter des chaines.
  BINANCE_API_KEY="$key_val"
  BINANCE_API_SECRET="$secret_val"
  export BINANCE_API_KEY BINANCE_API_SECRET
}

load_keys_from_file
if [[ -n "$SHELL_KEY_BEFORE$SHELL_SECRET_BEFORE" ]] && \
   ([[ "${BINANCE_API_KEY:-}" != "$SHELL_KEY_BEFORE" ]] || [[ "${BINANCE_API_SECRET:-}" != "$SHELL_SECRET_BEFORE" ]]); then
  echo "ALERTE_CLES: variables shell modifiees/reesetees, valeurs rechargees depuis $KEYS_FILE."
else
  echo "INFO_CLES: cles chargees depuis $KEYS_FILE."
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  echo "Action: renseigne $KEYS_FILE puis relance."
  exit 1
fi
if [[ "${BINANCE_API_KEY}" == *"pbpaste"* || "${BINANCE_API_SECRET}" == *"pbpaste"* || "${BINANCE_API_KEY}" == export\ * || "${BINANCE_API_SECRET}" == export\ * ]]; then
  echo "ERREUR: fichier de cles corrompu (commande detectee au lieu d une valeur)."
  echo "Action: re-saisis les cles et reecris $KEYS_FILE."
  exit 1
fi
if [[ "$BINANCE_API_KEY" =~ [[:space:]] || "$BINANCE_API_SECRET" =~ [[:space:]] ]]; then
  echo "ERREUR: cles invalides (espaces/retours ligne detectes)."
  exit 1
fi
if (( ${#BINANCE_API_KEY} < 40 || ${#BINANCE_API_SECRET} < 40 || ${#BINANCE_API_KEY} > 90 || ${#BINANCE_API_SECRET} > 90 )); then
  echo "ERREUR: format de cles suspect (KEY_LEN=${#BINANCE_API_KEY} SECRET_LEN=${#BINANCE_API_SECRET})."
  echo "Attendu: longueur typique proche de 64/64 sur Binance testnet."
  exit 1
fi
export BINANCE_API_KEY BINANCE_API_SECRET
# Force futures testnet pour eviter tout override shell parasite.
BINANCE_BASE_URL="${BINANCE_BASE_URL_OVERRIDE:-https://testnet.binancefuture.com}"
export BINANCE_BASE_URL

preflight_binance_auth() {
  local ping_http ts query sig acct_resp preview
  ping_http="$(curl -sS -o /dev/null -w "%{http_code}" --max-time 10 "$BINANCE_BASE_URL/fapi/v1/ping" || true)"
  if [[ "$ping_http" != "200" ]]; then
    echo "ERREUR_PREFLIGHT: ping Binance KO (http=$ping_http base=$BINANCE_BASE_URL)."
    return 1
  fi

  ts="$(( $(date +%s) * 1000 ))"
  query="timestamp=$ts&recvWindow=60000"
  sig="$(printf '%s' "$query" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | od -A n -t x1 | tr -d ' \n')"
  acct_resp="$(curl -sS --max-time 15 -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BINANCE_BASE_URL/fapi/v2/account?$query&signature=$sig" || true)"

  if [[ "$acct_resp" == *'"code":-2014'* || "$acct_resp" == *'"code":-2015'* || "$acct_resp" == *'"code":-1022'* ]]; then
    echo "ERREUR_PREFLIGHT: credentials Binance invalides (code API detecte)."
    return 1
  fi
  if [[ "$acct_resp" == *'"assets"'* || "$acct_resp" == *'"positions"'* ]]; then
    echo "PREFLIGHT_OK: authentification Binance valide."
    return 0
  fi

  preview="${acct_resp//$'\n'/ }"
  preview="${preview:0:220}"
  echo "ERREUR_PREFLIGHT: reponse account inattendue (auth non confirmee). preview=$preview"
  return 1
}

if ! preflight_binance_auth; then
  echo "ABORT: stop avant lancement pour eviter un run perdu."
  exit 1
fi

TEST_TAG="${TEST_TAG_OVERRIDE:-TEST_DUO_HARMONIC_5813_12H30}"
RUN_SEC="${RUN_SEC_OVERRIDE:-45000}"
START_EPOCH="$(date +%s)"
END_UTC="$(ruby -e 'puts Time.at(ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- $((START_EPOCH + RUN_SEC)))"

# Core tunables
GLOBAL_STOP_USDT="${GLOBAL_STOP_USDT:--16.00}"
BETA_MOMENTUM_THRESHOLD="${BETA_MOMENTUM_THRESHOLD:-0.8}"
BETA_STOP_LOSS_BPS="${BETA_STOP_LOSS_BPS:-12}"
BETA_FORCE_ENTRY_SIDE="${BETA_FORCE_ENTRY_SIDE:-BUY}"
BETA_POSITION_SIDE="${BETA_POSITION_SIDE:-LONG}"
BETA_BUY_USDT="${BUY_USDT_BETA:-250}"
BETA_LEVERAGE_TARGET="${BETA_LEVERAGE_TARGET:-5}"
BETA_LEVERAGE_RAMP_ENABLED="${BETA_LEVERAGE_RAMP_ENABLED:-FALSE}"
BETA_LEVERAGE_RAMP_START="${BETA_LEVERAGE_RAMP_START:-$BETA_LEVERAGE_TARGET}"
BETA_LEVERAGE_RAMP_END="${BETA_LEVERAGE_RAMP_END:-$BETA_LEVERAGE_TARGET}"
BETA_LEVERAGE_RAMP_CYCLES="${BETA_LEVERAGE_RAMP_CYCLES:-30}"
ALPHA_REVENGE_MULT="${ALPHA_REVENGE_MULT:-3.236}"
ALPHA_STOP_LOSS_BPS="${ALPHA_STOP_LOSS_BPS:-8}"
ALPHA_BUY_USDT="${BUY_USDT_ALPHA:-250}"
DUO_HUNTER_REQUIRE_TRUE_VACUUM="${DUO_HUNTER_REQUIRE_TRUE_VACUUM:-FALSE}"

# ALPHA tunables (overridable from wrapper scripts)
ALPHA_DUO_MODE="${ALPHA_DUO_MODE:-TRUE}"
ALPHA_FORCE_ENTRY_SIDE="${ALPHA_FORCE_ENTRY_SIDE:-AUTO}"
ALPHA_RADAR_GATE="${ALPHA_RADAR_GATE:-TRUE}"
ALPHA_TREND_FILTER="${ALPHA_TREND_FILTER:-TRUE}"
ALPHA_MOMENTUM_THRESHOLD="${ALPHA_MOMENTUM_THRESHOLD:-0.65}"
ALPHA_LEVERAGE_TARGET="${ALPHA_LEVERAGE_TARGET:-13}"
ALPHA_LEVERAGE_RAMP_ENABLED="${ALPHA_LEVERAGE_RAMP_ENABLED:-FALSE}"
ALPHA_LEVERAGE_RAMP_START="${ALPHA_LEVERAGE_RAMP_START:-5}"
ALPHA_LEVERAGE_RAMP_END="${ALPHA_LEVERAGE_RAMP_END:-13}"
ALPHA_LEVERAGE_RAMP_CYCLES="${ALPHA_LEVERAGE_RAMP_CYCLES:-180}"

# Clean start
killall caffeinate ruby 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json

RUNNER="bash"
command -v caffeinate >/dev/null 2>&1 && RUNNER="caffeinate -is bash"

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "BETA x5 | ALPHA x13 | Masse 1.618->3.236 (alarm) | Trigger=-3bps/-0.80 | GlobalStop=${GLOBAL_STOP_USDT} HALT | Lagrange+PhaseShift=ON"

# Auto-stop after 12h30
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# BETA = Scout
$RUNNER -c '
export DUO_MODE=TRUE
export DUO_ROLE=SCOUT
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT='"$GLOBAL_STOP_USDT"'
export DUO_GLOBAL_STOP_HALT_RUN=TRUE
export FORCE_ENTRY_SIDE='"$BETA_FORCE_ENTRY_SIDE"'
export POSITION_SIDE='"$BETA_POSITION_SIDE"'
export LEVERAGE='"$BETA_LEVERAGE_TARGET"'
export LEVERAGE_RAMP_ENABLED='"$BETA_LEVERAGE_RAMP_ENABLED"'
export LEVERAGE_RAMP_START='"$BETA_LEVERAGE_RAMP_START"'
export LEVERAGE_RAMP_END='"$BETA_LEVERAGE_RAMP_END"'
export LEVERAGE_RAMP_CYCLES='"$BETA_LEVERAGE_RAMP_CYCLES"'
export BUY_USDT='"$BETA_BUY_USDT"'
export MOMENTUM_THRESHOLD='"$BETA_MOMENTUM_THRESHOLD"'
export STOP_LOSS_BPS='"$BETA_STOP_LOSS_BPS"'
export BOT_LABEL="BETA_X5"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_BETA_X5.csv"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

# Head start for state file
sleep 2

# ALPHA = Hunter
$RUNNER -c '
export DUO_MODE='"$ALPHA_DUO_MODE"'
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT='"$GLOBAL_STOP_USDT"'
export DUO_GLOBAL_STOP_HALT_RUN=TRUE
export DUO_SCOUT_SUFFER_BPS=-3
export DUO_SCOUT_SUFFER_USDT=-0.80
export DUO_HUNTER_REVENGE_MULT='"$ALPHA_REVENGE_MULT"'
export DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE
export DUO_HUNTER_REQUIRE_TRUE_VACUUM='"$DUO_HUNTER_REQUIRE_TRUE_VACUUM"'
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=9
export DUO_LAGRANGE_FEEDBACK_ENABLED=TRUE
export DUO_LAGRANGE_FEEDBACK_MS=1
export DUO_LAGRANGE_LAMBDA=1.618
export DUO_LAGRANGE_RECOVERY_RATIO=0.618
export DUO_LAGRANGE_PROOF_THRESHOLD=8
export DUO_LAGRANGE_ABSORB_ON_OPPOSE=TRUE
export DUO_V63_PHASE_SHIFT_ENABLED=TRUE
export DUO_V63_ALARM_BPS=13
export DUO_V63_ALARM_TTL_SEC=45
export DUO_V63_SENTINEL_ENABLED=TRUE
export DUO_V63_SENTINEL_MULT=2.0
export DUO_V63_ENGINE_EQUITY_USDT=250
export DUO_V63_PHASE_SHIFT_STEP_SEC=13
export DUO_V63_PHASE_SHIFT_ACCEL_STEP_SEC=5
export RADAR_GATE='"$ALPHA_RADAR_GATE"'
export TREND_FILTER='"$ALPHA_TREND_FILTER"'
export FORCE_ENTRY_SIDE='"$ALPHA_FORCE_ENTRY_SIDE"'
export POSITION_SIDE=SHORT
export LEVERAGE='"$ALPHA_LEVERAGE_TARGET"'
export LEVERAGE_RAMP_ENABLED='"$ALPHA_LEVERAGE_RAMP_ENABLED"'
export LEVERAGE_RAMP_START='"$ALPHA_LEVERAGE_RAMP_START"'
export LEVERAGE_RAMP_END='"$ALPHA_LEVERAGE_RAMP_END"'
export LEVERAGE_RAMP_CYCLES='"$ALPHA_LEVERAGE_RAMP_CYCLES"'
export BUY_USDT='"$ALPHA_BUY_USDT"'
export MOMENTUM_THRESHOLD='"$ALPHA_MOMENTUM_THRESHOLD"'
export STOP_LOSS_BPS='"$ALPHA_STOP_LOSS_BPS"'
export BOT_LABEL="ALPHA_X13_BURST13"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="runs/'"$TEST_TAG"'_ALPHA_X13_BURST13.csv"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'

report_pnl_three_parts() {
  local alpha_log beta_log start_iso end_iso p1_end p2_end
  alpha_log="runs/${TEST_TAG}_ALPHA_X13_BURST13.csv"
  beta_log="runs/${TEST_TAG}_BETA_X5.csv"

  if [[ ! -f "$alpha_log" || ! -f "$beta_log" ]]; then
    echo "RAPPORT_3_PARTIES: logs manquants, skip."
    return 0
  fi

  start_iso="$(ruby -e 'puts Time.at(ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- "$START_EPOCH")"
  end_iso="$(ruby -e 'puts Time.at(ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- $((START_EPOCH + RUN_SEC)))"
  p1_end="$(ruby -e 'puts Time.at(ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- $((START_EPOCH + RUN_SEC / 3)))"
  p2_end="$(ruby -e 'puts Time.at(ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- $((START_EPOCH + (2 * RUN_SEC) / 3)))"

  echo "=== RAPPORT PNL 3 PARTIES ==="
  echo "Fenetre: $start_iso -> $end_iso"
  awk -F',' -v s="$start_iso" -v p1="$p1_end" -v p2="$p2_end" -v e="$end_iso" '
  function seg(ts) {
    if (ts >= s && ts < p1) return 1
    if (ts >= p1 && ts < p2) return 2
    if (ts >= p2 && ts <= e) return 3
    return 0
  }
  function add(role, part, pnl) {
    n[role,part]++
    net[role,part] += pnl
    if (pnl > 0) { w[role,part]++; gp[role,part] += pnl }
    else if (pnl < 0) { l[role,part]++; gl[role,part] += pnl }
    else { z[role,part]++ }
  }
  FNR == 1 { next }
  $4 == "FILLED" {
    part = seg($1)
    if (!part) next
    pnl = $9 + 0
    role = (FILENAME ~ /_ALPHA_/) ? "ALPHA" : "BETA"
    add(role, part, pnl)
    add("TOTAL", part, pnl)
  }
  END {
    for (p = 1; p <= 3; p++) {
      printf("PARTIE_%d\n", p)
      for (i = 1; i <= 3; i++) {
        role = (i == 1) ? "ALPHA" : ((i == 2) ? "BETA" : "TOTAL")
        wr = (n[role,p] > 0) ? (100 * w[role,p] / n[role,p]) : 0
        printf("  %s orders=%d win=%d loss=%d flat=%d winrate=%.2f net=%.4f\n",
               role, n[role,p] + 0, w[role,p] + 0, l[role,p] + 0, z[role,p] + 0, wr, net[role,p] + 0)
      }
    }
  }' "$alpha_log" "$beta_log"
}

report_pnl_three_parts
