#!/usr/bin/env bash
set -euo pipefail

# === MASTER TENDANCE: SENTINELLE & INVERSION ===
# BETA (sentinelle) LONG, plus lent pour lire la "boite"
# ALPHA (hunter) SHORT en mode inversion avec ramp 5 -> 13

if [ -d /app ]; then
  cd /app
else
  cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi

# Cles Binance
if [ -f "${HOME}/.binance_testnet.env" ]; then
  set -a
  source "${HOME}/.binance_testnet.env"
  set +a
  echo "INFO_CLES: cles chargees depuis ${HOME}/.binance_testnet.env"
fi

# Preflight
if [ -z "${BINANCE_API_KEY:-}" ] || [ -z "${BINANCE_API_SECRET:-}" ]; then
  echo "PREFLIGHT_ERR: BINANCE_API_KEY ou BINANCE_API_SECRET manquant"
  exit 1
fi
ping_resp="$(curl -sS --connect-timeout 5 --max-time 10 "https://testnet.binancefuture.com/fapi/v1/ping" 2>/dev/null || true)"
if [ "$ping_resp" != "{}" ]; then
  echo "PREFLIGHT_ERR: testnet Binance unreachable"
  exit 1
fi
echo "PREFLIGHT_OK: authentification Binance valide."

# Preflight LLM: veto indisponible => pas de run
if [ "${LLM_GATE_ENABLED:-TRUE}" = "TRUE" ]; then
  llm_ping="$(curl -sS --connect-timeout 3 --max-time 6 "${LLM_OLLAMA_URL:-http://127.0.0.1:11434}/api/tags" 2>/dev/null || true)"
  if [ -z "$llm_ping" ]; then
    echo "PREFLIGHT_ERR: LLM_Ollama unreachable (${LLM_OLLAMA_URL:-http://127.0.0.1:11434})"
    exit 1
  fi
fi

RUN_DIR="${RUN_DIR:-runs}"
duration_sec="${RUN_SEC_OVERRIDE:-28800}"
tag="${TEST_TAG_OVERRIDE:-MASTER_TENDANCE_SENTINELLE_INVERSION_8H00}"
mkdir -p "$RUN_DIR"
rm -f STOP_ALPHA STOP_BETA "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid "$RUN_DIR"/master.pid
echo $$ > "${RUN_DIR}/master.pid"
echo "Pour arrêter: kill -9 -$$  (ou ./stop_ace777.sh)"

start_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
end_utc="$(ruby -e 'puts (Time.now + ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- "$duration_sec" 2>/dev/null || echo "N/A")"

echo "=== ${tag} ==="
echo "Start UTC: $start_utc"
echo "End UTC:   $end_utc"
echo "SENTINELLE&INVERSION | Symbol=${SYMBOL:-BTCUSDT} | BETA LONG mom=${MOMENTUM_THRESHOLD_BETA:-0.85} | ALPHA SHORT mom=${MOMENTUM_THRESHOLD_ALPHA:-0.85} shock_inv=${SHOCK_INVERSION_ALPHA:-TRUE} | Radar=${VACUUM_TENSION_THRESHOLD_BETA:-0.618}"

# Mapping symbiose vers flags moteurs existants
if [ "${DUO_SYNC_MODE:-}" = "AGGRESSIVE_HEDGE" ]; then
  export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
  export DUO_V63_ALARM_BPS="${DUO_V63_ALARM_BPS:--3}"
fi

cleanup() {
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  kill "${PID_ALPHA:-}" "${PID_BETA:-}" "${PID_TIMER_ALPHA:-}" "${PID_TIMER_BETA:-}" 2>/dev/null || true
  echo "Arret global."
}
trap cleanup SIGINT SIGTERM

# Timer
ruby -e "sleep ${duration_sec}; File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &
PID_TIMER_ALPHA=$!

run_unit() {
  local unit="$1"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  set +e
  tail -n +85 ./genesis_manifest.txt | bash -s 2>&1 | while IFS= read -r line; do
    printf '[%s] %s\n' "$unit" "$line"
    printf '[%s] %s\n' "$unit" "$line" >> "$live_log" 2>/dev/null || true
  done
  local rc=${PIPESTATUS[1]:-0}
  set -e
  local exit_line
  exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} how=pipe_run_unit why=rc_${rc} rc=${rc}"
  mkdir -p "${RUN_DIR:-runs}"
  echo "$exit_line" >> "${RUN_DIR:-runs}/PROCESS_EXIT.log" 2>/dev/null || true
  echo "[$unit] $exit_line"
  return "$rc"
}

# BETA SENTINELLE — LONG (lecture de boite), momentum plus lent
(
  export LOG_FILE="${RUN_DIR}/${tag}_BETA_SENTINELLE_LONG.csv"
  export STOP_FILE="STOP_BETA"
  export LEVERAGE="${LEVERAGE_BETA:-3}"
  export BUY_USDT="${BUY_USDT_BETA:-400}"
  export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
  export FORCE_ENTRY_SIDE="BUY"
  export POSITION_SIDE="LONG"
  export DUO_MODE="TRUE"
  export DUO_ROLE="SCOUT"
  export V8_RESONANCE_MODE="TRUE"
  export V8_TENSION_MODE="TRUE"
  export VOLATILITY_IMPULSE_DT_MS="${VOLATILITY_DT_MS_BETA:-500}"
  export IMPULSE_RESONANCE_DT_MS="${VOLATILITY_DT_MS_BETA:-500}"
  export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD_BETA:-0.85}"
  export IMPULSE_RESONANCE_WALL_DROP_PCT="${WALL_DROP_PCT_BETA:-6.5}"
  export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.618}"
  export V8_VOID_LOCK_ENABLED="TRUE"
  export V8_SHOCK_EXIT_ENABLED="TRUE"
  export SHOCK_EXIT_10_BPS="${SHOCK_EXIT_10_BPS:-18.0}"
  export V8_SHOCK_SPEED_EPS_BPS_S="${V8_SHOCK_SPEED_EPS_BPS_S:-0.0}"
  export FLUID_EXIT_ENABLED="TRUE"
  export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
  export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
  export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
  export DUO_V63_ALARM_BPS="-3"
  run_unit "BETA_SENTINELLE_LONG"
) &
PID_BETA=$!
echo "$PID_BETA" > "${RUN_DIR}/beta.pid"

# ALPHA INVERSION — SHORT, burst + ramp 5->13, choc inversion actif
(
  export LOG_FILE="${RUN_DIR}/${tag}_ALPHA_INVERSION_SHORT_BURST13.csv"
  export STOP_FILE="STOP_ALPHA"
  export LEVERAGE="${LEVERAGE_ALPHA_START:-5}"
  export LEVERAGE_RAMP_ENABLED="TRUE"
  export LEVERAGE_RAMP_START="${LEVERAGE_ALPHA_START:-5}"
  export LEVERAGE_RAMP_END="${LEVERAGE_ALPHA_END:-13}"
  export LEVERAGE_RAMP_CYCLES="${LEVERAGE_ALPHA_RAMP_CYCLES:-180}"
  export BUY_USDT="${BUY_USDT_ALPHA:-400}"
  export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
  export FORCE_ENTRY_SIDE="SELL"
  export POSITION_SIDE="SHORT"
  export DUO_MODE="TRUE"
  export DUO_ROLE="HUNTER"
  export DUO_V6_BURST_X13="TRUE"
  export V8_RESONANCE_MODE="TRUE"
  export V8_TENSION_MODE="TRUE"
  export VOLATILITY_IMPULSE_DT_MS="${VOLATILITY_DT_MS_ALPHA:-32}"
  export IMPULSE_RESONANCE_DT_MS="${VOLATILITY_DT_MS_ALPHA:-32}"
  export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD_ALPHA:-0.96}"
  export IMPULSE_RESONANCE_WALL_DROP_PCT="${WALL_DROP_PCT_ALPHA:-6.5}"
  export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.618}"
  export V8_VOID_LOCK_ENABLED="TRUE"
  export V8_SHOCK_EXIT_ENABLED="${SHOCK_INVERSION_ALPHA:-TRUE}"
  export SHOCK_EXIT_10_BPS="${SHOCK_EXIT_10_BPS:-18.0}"
  export V8_SHOCK_SPEED_EPS_BPS_S="${V8_SHOCK_SPEED_EPS_BPS_S:-0.0}"
  export DUO_HUNTER_AGGR_TRAIL_ARM_BPS="${DUO_HUNTER_AGGR_TRAIL_ARM_BPS:-12}"
  export DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS="${DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS:-9}"
  export FLUID_EXIT_ENABLED="TRUE"
  export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
  export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
  export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
  export RUN_STATE_ENABLED="${RUN_STATE_ENABLED:-FALSE}"
  export RUN_STATE_LINK_TOTAL_PNL="${RUN_STATE_LINK_TOTAL_PNL:-FALSE}"
  run_unit "ALPHA_INVERSION_SHORT"
) &
PID_ALPHA=$!
echo "$PID_ALPHA" > "${RUN_DIR}/alpha.pid"

echo "Duo en marche. Logs: ${RUN_DIR}/${tag}_BETA_SENTINELLE_LONG.csv | ${RUN_DIR}/${tag}_ALPHA_INVERSION_SHORT_BURST13.csv"
wait "$PID_ALPHA" "$PID_BETA"
echo "Mission terminee."

# Rapport PnL
beta_csv="${RUN_DIR}/${tag}_BETA_SENTINELLE_LONG.csv"
alpha_csv="${RUN_DIR}/${tag}_ALPHA_INVERSION_SHORT_BURST13.csv"
if [ -f "$beta_csv" ] && [ -f "$alpha_csv" ]; then
  beta_pnl="$(awk -F',' 'NR>1 && $4=="FILLED" {sum+=$9} END {printf "%.4f", sum+0}' "$beta_csv")"
  alpha_pnl="$(awk -F',' 'NR>1 && $4=="FILLED" {sum+=$9} END {printf "%.4f", sum+0}' "$alpha_csv")"
  total_pnl="$(awk -v b="$beta_pnl" -v a="$alpha_pnl" 'BEGIN {printf "%.4f", b+0+a+0}')"
  beta_count="$(awk -F',' 'NR>1 && $4=="FILLED" {c++} END {print c+0}' "$beta_csv")"
  alpha_count="$(awk -F',' 'NR>1 && $4=="FILLED" {c++} END {print c+0}' "$alpha_csv")"
  echo
  echo "=== RAPPORT PNL 3 PARTIES ==="
  echo "Partie 1 BETA:  $beta_count trades | pnl=$beta_pnl USDT"
  echo "Partie 2 ALPHA: $alpha_count trades | pnl=$alpha_pnl USDT"
  echo "Partie 3 TOTAL: pnl=$total_pnl USDT"
  echo "============================="
fi
