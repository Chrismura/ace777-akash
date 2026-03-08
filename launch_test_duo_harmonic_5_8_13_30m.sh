#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Test 30m - Duo Harmonic 5-8-13 + V6.3 phase-shift/sentinel

# Charge systematique des cles depuis fichier local securise.
# But: eviter les re-saisies et neutraliser les variables shell corrompues.
KEYS_FILE="${BINANCE_TESTNET_ENV_FILE:-$HOME/.binance_testnet.env}"
SHELL_KEY_BEFORE="${BINANCE_API_KEY:-}"
SHELL_SECRET_BEFORE="${BINANCE_API_SECRET:-}"
if [[ -f "$KEYS_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$KEYS_FILE"
  if [[ -n "$SHELL_KEY_BEFORE$SHELL_SECRET_BEFORE" ]] && \
     ([[ "${BINANCE_API_KEY:-}" != "$SHELL_KEY_BEFORE" ]] || [[ "${BINANCE_API_SECRET:-}" != "$SHELL_SECRET_BEFORE" ]]); then
    echo "ALERTE_CLES: variables shell modifiees/reesetees, valeurs rechargees depuis $KEYS_FILE."
  else
    echo "INFO_CLES: cles chargees depuis $KEYS_FILE."
  fi
fi
if [[ -z "${BINANCE_API_KEY:-}" || -z "${BINANCE_API_SECRET:-}" ]]; then
  echo "ERREUR: BINANCE_API_KEY/BINANCE_API_SECRET manquantes."
  echo "Action: renseigne $KEYS_FILE puis relance."
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
BINANCE_BASE_URL="${BINANCE_BASE_URL:-https://testnet.binance.vision}"

preflight_binance_auth() {
  local ping_http ts query sig acct_resp
  ping_http="$(curl -sS -o /dev/null -w "%{http_code}" --max-time 10 "$BINANCE_BASE_URL/fapi/v1/ping" || true)"
  if [[ "$ping_http" != "200" ]]; then
    echo "ERREUR_PREFLIGHT: ping Binance KO (http=$ping_http base=$BINANCE_BASE_URL)."
    return 1
  fi

  ts="$(python3 -c 'import time; print(int(time.time()*1000))')"
  query="timestamp=$ts&recvWindow=60000"
  sig="$(printf '%s' "$query" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256)"
  acct_resp="$(curl -sS --max-time 15 -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BINANCE_BASE_URL/fapi/v2/account?$query&signature=$sig" || true)"

  if [[ "$acct_resp" == *'"code":-2014'* || "$acct_resp" == *'"code":-2015'* || "$acct_resp" == *'"code":-1022'* ]]; then
    echo "ERREUR_PREFLIGHT: credentials Binance invalides (code API detecte)."
    return 1
  fi
  if [[ "$acct_resp" == *'"assets"'* || "$acct_resp" == *'"positions"'* ]]; then
    echo "PREFLIGHT_OK: authentification Binance valide."
    return 0
  fi

  echo "ERREUR_PREFLIGHT: reponse account inattendue (auth non confirmee)."
  return 1
}

if ! preflight_binance_auth; then
  echo "ABORT: stop avant lancement pour eviter un run perdu."
  exit 1
fi

TEST_TAG="TEST_DUO_HARMONIC_5813_30M_V63"
RUN_SEC=1800
START_EPOCH="$(date +%s)"
END_UTC="$(date -u -r $((START_EPOCH + RUN_SEC)) +%Y-%m-%dT%H:%M:%SZ)"
LEVERAGE_BETA="${LEVERAGE_BETA:-5}"
LEVERAGE_ALPHA="${LEVERAGE_ALPHA:-13}"
DUO_HUNTER_REVENGE_MULT="${DUO_HUNTER_REVENGE_MULT:-1.618}"
DUO_GLOBAL_STOP_SESSION_USDT="${DUO_GLOBAL_STOP_SESSION_USDT:--5.00}"
BETA_STOP_LOSS_BPS="${STOP_LOSS_BPS:-12}"
ALPHA_STOP_LOSS_BPS="${ALPHA_STOP_LOSS_BPS:-8}"
BETA_POLL_SEC="${POLL_SEC:-0.03}"
ALPHA_POLL_SEC="${ALPHA_POLL_SEC:-0.03}"
BETA_LOG="runs/${TEST_TAG}_BETA_X${LEVERAGE_BETA}.csv"
ALPHA_LOG="runs/${TEST_TAG}_ALPHA_X${LEVERAGE_ALPHA}_BURST13.csv"

# Clean start
killall caffeinate ruby 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json runs/duo_burst_state.json runs/duo_alarm_v63.json

echo "=== ${TEST_TAG} ==="
echo "Start UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "End UTC:   ${END_UTC}"
echo "BETA x${LEVERAGE_BETA} | ALPHA x${LEVERAGE_ALPHA} | Duo PLUS ACTIF | Trigger=-4bps/-0.30 | TTL=120s | Dopamine=ON | HunterSL=12bps | GlobalStop=${DUO_GLOBAL_STOP_SESSION_USDT} non-blocking | Lagrange+PhaseShift=ON"
if ! bash -n ./ACE777_STRICT_CLONE_FUTURES_V2.sh; then
  echo "ERREUR: ACE777_STRICT_CLONE_FUTURES_V2.sh invalide (syntax shell)."
  exit 1
fi

# Auto-stop after 30 minutes
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_ALPHA','')" &) >/dev/null 2>&1
(ruby -e "sleep ${RUN_SEC}; File.write('STOP_BETA','')" &) >/dev/null 2>&1

# BETA = Scout
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=SCOUT
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT='"$DUO_GLOBAL_STOP_SESSION_USDT"'
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_DOPAMINE_MODE=TRUE
export REWARD_SENSITIVITY_BOOST=0.2
export PAIN_ADAPTIVE_FILTER=1.5
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=BUY
export POSITION_SIDE=LONG
export LEVERAGE='"$LEVERAGE_BETA"'
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.35
export STOP_LOSS_BPS='"$BETA_STOP_LOSS_BPS"'
export POLL_SEC='"$BETA_POLL_SEC"'
export BOT_LABEL="BETA_X'"$LEVERAGE_BETA"'"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="'"$BETA_LOG"'"
export STOP_FILE="STOP_BETA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
' &

sleep 2

# ALPHA = Hunter
caffeinate -is bash -c '
export DUO_MODE=TRUE
export DUO_ROLE=HUNTER
export DUO_STATE_FILE="runs/duo_state.json"
export DUO_EVENT_TTL_SEC=120
export DUO_SESSION_FILE="runs/duo_session.json"
export DUO_GLOBAL_STOP_SESSION_USDT='"$DUO_GLOBAL_STOP_SESSION_USDT"'
export DUO_GLOBAL_STOP_HALT_RUN=FALSE
export DUO_SCOUT_SUFFER_BPS=-4
export DUO_SCOUT_SUFFER_USDT=-0.30
export DUO_HUNTER_REVENGE_MULT='"$DUO_HUNTER_REVENGE_MULT"'
export DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE
export DUO_HUNTER_PERSIST_LINK=TRUE
export DUO_FORCE_OPPOSITE=TRUE
export DUO_MOMENTUM_HANDOVER=TRUE
export DUO_HUNTER_STOP_LOSS_BPS=12
export DUO_DOPAMINE_MODE=TRUE
export REWARD_SENSITIVITY_BOOST=0.2
export PAIN_ADAPTIVE_FILTER=1.5
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
export RADAR_GATE=FALSE
export TREND_FILTER=FALSE
export FORCE_ENTRY_SIDE=AUTO
export POSITION_SIDE=SHORT
export LEVERAGE='"$LEVERAGE_ALPHA"'
export BUY_USDT=250
export MOMENTUM_THRESHOLD=0.50
export STOP_LOSS_BPS='"$ALPHA_STOP_LOSS_BPS"'
export POLL_SEC='"$ALPHA_POLL_SEC"'
export BOT_LABEL="ALPHA_X'"$LEVERAGE_ALPHA"'_BURST13"
export RUN_DURATION_SEC='"$RUN_SEC"'
export RUN_START_EPOCH='"$START_EPOCH"'
export LOG_FILE="'"$ALPHA_LOG"'"
export STOP_FILE="STOP_ALPHA"
bash ./ACE777_STRICT_CLONE_FUTURES_V2.sh
'

echo ""
echo "=== RESUME FIN DE CYCLE (${TEST_TAG}) ==="
SUMMARY_FILE="master_base/pnl/pnl_resume_$(date -u +%Y-%m-%d_%H%M)_${TEST_TAG}_30M.txt"
SUMMARY_BODY="$(ruby - "$BETA_LOG" "$ALPHA_LOG" <<'RUBY'
require 'csv'
require 'time'

def summarize(path)
  return {trades: 0, pnl: 0.0, wins: 0, losses: 0, zeros: 0, reasons: [], rows: []} unless File.exist?(path)
  rows = []
  CSV.foreach(path, headers: true) { |r| rows << r }
  filled = rows.select { |r| r['status'] == 'FILLED' }
  pnl = filled.sum { |r| r['pnl'].to_f }
  wins = filled.count { |r| r['pnl'].to_f > 0 }
  losses = filled.count { |r| r['pnl'].to_f < 0 }
  zeros = filled.count { |r| r['pnl'].to_f == 0 }
  reasons = filled.group_by { |r| r['exitReason'] }.transform_values(&:size).sort_by { |_, v| -v }.first(5)
  typed_rows = filled.map do |r|
    t = (Time.parse(r['ts']).utc rescue nil)
    next nil unless t
    c = (Integer(r['cycle']) rescue nil)
    {t: t, pnl: r['pnl'].to_f, cycle: c}
  end.compact
  {trades: filled.size, pnl: pnl, wins: wins, losses: losses, zeros: zeros, reasons: reasons, rows: typed_rows}
end

beta_path = ARGV[0]
alpha_path = ARGV[1]
beta = summarize(beta_path)
alpha = summarize(alpha_path)
total = beta[:pnl] + alpha[:pnl]
all_rows = beta[:rows] + alpha[:rows]

puts "BETA  trades=#{beta[:trades]} pnl=#{format('%.4f', beta[:pnl])} wins=#{beta[:wins]} losses=#{beta[:losses]} zero=#{beta[:zeros]}"
puts "ALPHA trades=#{alpha[:trades]} pnl=#{format('%.4f', alpha[:pnl])} wins=#{alpha[:wins]} losses=#{alpha[:losses]} zero=#{alpha[:zeros]}"
puts "TOTAL pnl=#{format('%.4f', total)}"
puts "BETA  top_exit=#{beta[:reasons].map { |k, v| "#{k}:#{v}" }.join(', ')}"
puts "ALPHA top_exit=#{alpha[:reasons].map { |k, v| "#{k}:#{v}" }.join(', ')}"

if all_rows.empty?
  puts "FENETRE UTC=NA"
  puts "BLOCS UTC=NA"
  exit
end

min_t = all_rows.map { |x| x[:t] }.min
max_t = all_rows.map { |x| x[:t] }.max
span = max_t - min_t
b1 = min_t + span / 3.0
b2 = min_t + (2.0 * span / 3.0)
blocks = [
  ["DEBUT", min_t, b1],
  ["MILIEU", b1, b2],
  ["FIN", b2, max_t + 1]
]

def block_stats(rows, from_t, to_t)
  sel = rows.select { |x| x[:t] >= from_t && x[:t] < to_t }
  times = sel.map { |x| x[:t] }
  cycles = sel.map { |x| x[:cycle] }.compact
  {
    trades: sel.size,
    pnl: sel.sum { |x| x[:pnl] },
    t_from: times.min,
    t_to: times.max,
    c_from: cycles.min,
    c_to: cycles.max
  }
end

puts "FENETRE UTC=#{min_t.iso8601}..#{max_t.iso8601}"
blocks.each do |name, from_t, to_t|
  bs = block_stats(beta[:rows], from_t, to_t)
  as = block_stats(alpha[:rows], from_t, to_t)
  total_block = bs[:pnl] + as[:pnl]
  block_from = [bs[:t_from], as[:t_from]].compact.min
  block_to = [bs[:t_to], as[:t_to]].compact.max
  beta_cycles = (bs[:c_from] && bs[:c_to]) ? "#{bs[:c_from]}..#{bs[:c_to]}" : "NA"
  alpha_cycles = (as[:c_from] && as[:c_to]) ? "#{as[:c_from]}..#{as[:c_to]}" : "NA"
  puts "#{name} DE=#{(block_from ? block_from.iso8601 : 'NA')} A=#{(block_to ? block_to.iso8601 : 'NA')} | total=#{format('%.4f', total_block)} trades=#{bs[:trades] + as[:trades]} | beta=#{format('%.4f', bs[:pnl])} cycles=#{beta_cycles} | alpha=#{format('%.4f', as[:pnl])} cycles=#{alpha_cycles}"
end
RUBY
)"

{
  echo "DUREE=30 minutes"
  printf '%s\n' "$SUMMARY_BODY"
} | tee "$SUMMARY_FILE"
echo "RESUME_SAUVE=${SUMMARY_FILE}"