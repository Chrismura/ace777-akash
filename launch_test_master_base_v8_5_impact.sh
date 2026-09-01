#!/usr/bin/env bash
set -euo pipefail

# === MASTER BASE V8.5 IMPACT ===
# Lanceur duo BETA_X5 + ALPHA_X13_BURST13 (config exacte nuit 20260310)
# Utilise le corps genesis (V8 Resonance, V8 Tension, etc.)

if [ -d /app ]; then
  cd /app
else
  cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi

_binance_mode="${BINANCE_MODE:-testnet}"
if [ "$_binance_mode" = "live" ]; then
  if [ -f "${HOME}/.binance_live.env" ]; then
    set -a
    # shellcheck source=/dev/null
    source "${HOME}/.binance_live.env"
    set +a
    export BASE_URL="${BASE_URL:-https://fapi.binance.com}"
    export BINANCE_ALLOW_MAINNET="${BINANCE_ALLOW_MAINNET:-TRUE}"
    export WATCHDOG_PING_URL="${WATCHDOG_PING_URL:-https://fapi.binance.com/fapi/v1/ping}"
    echo "INFO_CLES: LIVE mainnet depuis ${HOME}/.binance_live.env"
  else
    echo "PREFLIGHT_ERR: BINANCE_MODE=live mais ~/.binance_live.env introuvable"
    exit 1
  fi
elif [ -f "${HOME}/.binance_testnet.env" ]; then
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  export BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
  echo "INFO_CLES: testnet depuis ${HOME}/.binance_testnet.env"
fi

RUN_DIR="${RUN_DIR:-runs}"
duration_sec="${RUN_SEC_OVERRIDE:-14400}"
tag="${TEST_TAG_OVERRIDE:-MASTER_BASE_V8_5_IMPACT_4H}"
# Sidecar de session (P0/P2) : identifie sans ambiguïté venue, rôles, schéma,
# modèle de frais et empreinte du champion. Le champion reste inchangé.
run_id="${ACE777_RUN_ID:-${tag}_$(date -u +%Y%m%dT%H%M%SZ)_$$}"
RUN_SIDECAR="${RUN_DIR}/${run_id}_session.json"
mkdir -p "$RUN_DIR"

export DUO_STATE_FILE="${RUN_DIR}/duo_state.json"
export DUO_SESSION_FILE="${RUN_DIR}/duo_session.json"
export VORTEX_CONTROL_FILE="${RUN_DIR}/vortex_control.json"
export SWARM_TELEMETRY_FILE="${RUN_DIR}/swarm_telemetry.json"
export DUO_V6_BURST_FILE="${RUN_DIR}/duo_burst.json"
export DUO_V63_ALARM_FILE="${RUN_DIR}/duo_v63_alarm.json"
export LOG_BETA="${RUN_DIR}/${tag}_BETA_X5.csv"
export LOG_ALPHA="${RUN_DIR}/${tag}_ALPHA_X13_BURST13.csv"

if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ]; then
  chmod +x ./scripts/stop_supervisor_v9_v2.sh ./scripts/start_supervisor_v9_v2.sh 2>/dev/null || true
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
fi

rm -f STOP STOP_ALPHA STOP_BETA "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid "$RUN_DIR"/master.pid
rm -f "$DUO_SESSION_FILE" "$DUO_STATE_FILE"
rm -f "$SWARM_TELEMETRY_FILE"
if [ -f "$RUN_DIR/timer.pid" ]; then
  kill "$(cat "$RUN_DIR/timer.pid")" 2>/dev/null || true
fi
pkill -f "File.write('STOP_ALPHA'" 2>/dev/null || true
rm -f "$RUN_DIR/timer.pid"

if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ] && [ "${VORTEX_CONTROL_ENABLED:-FALSE}" = "TRUE" ]; then
  export FORCE_SUPERVISOR_RESTART=1
  ./scripts/start_supervisor_v9_v2.sh --force
  unset FORCE_SUPERVISOR_RESTART
fi

./scripts/preflight_ace777.sh

echo $$ > "${RUN_DIR}/master.pid"
echo "Pour arrêter: kill -9 -$$  (ou ./stop_ace777.sh)"

start_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
# Métadonnées sidecar : écriture atomique, aucune donnée secrète.
champion_md5="$(md5 -q genesis_manifest.txt 2>/dev/null || printf 'unknown')"
ruby -rjson -e '
  path, run_id, tag, start, planned, config, version, md5 = ARGV
  meta = {
    "run_id" => run_id, "tag" => tag, "venue" => "binance_futures_testnet",
    "engine" => "ACE_DUO", "roles" => {"alpha" => "HUNTER", "beta" => "SCOUT"},
    "schema_version" => "ace_csv_v1_legacy", "fee_model" => "binance_futures_round_trip_bps",
    "fee_round_trip_bps" => 8, "champion_md5" => md5,
    "start_utc" => start, "planned_end_utc" => planned,
    "config" => config, "version" => version,
    "alpha_csv" => "#{tag}_ALPHA_X13_BURST13.csv",
    "beta_csv" => "#{tag}_BETA_X5.csv"
  }
  tmp = "#{path}.tmp"
  File.write(tmp, JSON.pretty_generate(meta) + "\n")
  File.rename(tmp, path)
' "$RUN_SIDECAR" "$run_id" "$tag" "$start_utc" "" "${ACE777_CONFIG_NAME:-?}" "${ACE777_CONFIG_VERSION:-?}" "$champion_md5" 2>/dev/null || true
end_utc="$(ruby -e 'puts (Time.now + ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- "$duration_sec" 2>/dev/null || echo "N/A")"
export RUN_START_UTC="$start_utc"
export RUN_END_UTC="$end_utc"
# Compléter le sidecar après calcul de la fin prévue.
if [ -f "$RUN_SIDECAR" ]; then
  RUN_SIDECAR="$RUN_SIDECAR" RUN_ID="$run_id" RUN_TAG="$tag" RUN_START="$start_utc" RUN_END="$end_utc" python3 - <<'PY'
import json, os
from pathlib import Path
p=Path(os.environ['RUN_SIDECAR'])
d=json.loads(p.read_text())
d['planned_end_utc']=os.environ['RUN_END']
d['start_utc']=os.environ['RUN_START']
d['run_id']=os.environ['RUN_ID']
d['tag']=os.environ['RUN_TAG']
tmp=p.with_suffix('.tmp'); tmp.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n'); tmp.replace(p)
PY
fi

ruby -rjson -e '
  require "fileutils"
  rd = ENV.fetch("RUN_DIR", "runs")
  FileUtils.mkdir_p(rd)
  meta = {
    "start_utc" => ENV["RUN_START_UTC"],
    "planned_end_utc" => ENV.fetch("RUN_END_UTC", ""),
    "run_id" => ENV.fetch("ACE777_RUN_ID", ""),
    "venue" => "binance_futures_testnet",
    "engine" => "ACE_DUO",
    "roles" => {"alpha" => "HUNTER", "beta" => "SCOUT"},
    "schema_version" => "ace_csv_v1_legacy",
    "fee_model" => "binance_futures_round_trip_bps",
    "fee_round_trip_bps" => 8,
    "tag" => ENV.fetch("TEST_TAG_OVERRIDE", ""),
    "config" => ENV.fetch("ACE777_CONFIG_NAME", "?"),
    "version" => ENV.fetch("ACE777_CONFIG_VERSION", "?")
  }
  File.write(File.join(rd, "#{meta["tag"]}_run_meta.json"), JSON.pretty_generate(meta))
' 2>/dev/null || true

echo "=== ${tag} ==="
echo "Start UTC: $start_utc"
echo "End UTC:   $end_utc"
echo "BETA x5 | ALPHA x13 | Masse 1.618->3.236 (alarm) | Trigger=-3bps/-0.80 | GlobalStop=${GLOBAL_STOP_USDT:--45.00} HALT | Lagrange+PhaseShift=ON"

stop_vortex_supervisor() {
  if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ]; then
    ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
  fi
}

cleanup() {
  kill "${PID_WATCHDOG:-}" 2>/dev/null || true
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  kill "${PID_ALPHA:-}" "${PID_BETA:-}" "${PID_TIMER_ALPHA:-}" 2>/dev/null || true
  stop_vortex_supervisor
  echo "Arrêt global."
}
trap cleanup SIGINT SIGTERM

ruby -e "sleep ${duration_sec}; File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &
PID_TIMER_ALPHA=$!
echo "$PID_TIMER_ALPHA" > "${RUN_DIR}/timer.pid"

chmod +x ./scripts/watchdog_ace777.sh 2>/dev/null || true
./scripts/watchdog_ace777.sh &
PID_WATCHDOG=$!

# CRASH DUMP (14/08, SPEC validée famille — codeur puter-grok) : au premier rc!=0,
# capture les 20 dernières lignes du log + FATAL_RC1 + dernier fill CSV (vérité C4),
# sans re-run. Zéro impact sur le comportement nominal (rc=0 → pas de dump).
_crash_dump() {
  local unit="$1" live_log="$2" rc="$3" ts dump_file csv
  [ "$rc" -eq 0 ] && return 0
  ts=$(date -u +%Y%m%d_%H%M%S 2>/dev/null || echo "now")
  dump_file="${RUN_DIR:-runs}/CRASH_DUMP_${unit}_${ts}.log"
  mkdir -p "${RUN_DIR:-runs}" 2>/dev/null || true
  tail -n 20 "$live_log" 2>/dev/null >> "$dump_file" || true
  if [ -f /tmp/ace777_fatal_rc1.log ]; then
    echo "=== FATAL_RC1 ===" >> "$dump_file" || true
    cat /tmp/ace777_fatal_rc1.log >> "$dump_file" 2>/dev/null || true
  fi
  csv=$(ls -t "${RUN_DIR:-runs}"/${tag}_*ALPHA*.csv 2>/dev/null | head -1)
  if [ -n "$csv" ] && [ -f "$csv" ]; then
    echo "=== DERNIER FILL CSV ($csv) ===" >> "$dump_file" || true
    tail -n 2 "$csv" >> "$dump_file" 2>/dev/null || true
  fi
}

run_unit() {
  local unit="$1"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  set +e
  # INSTRUMENTATION CAPTURE (14/08, consensus famille 6/6 + codeur) :
  # prefixe injecte avant le genesis dans le pipe bash -s (genesis INTACT).
  # trap EXIT -> dump rc + derniere commande reelle au moment de la mort.
  # trap DEBUG -> capture $_last_cmd via BASH_COMMAND (bash 3.2 macOS).
  export ACE777_UNIT="$unit"
  export ACE777_RUN_DIR="${RUN_DIR:-runs}"
  export ACE777_TRACE_FILE="${RUN_DIR:-runs}/CMD_TRACE_${unit}.log"
  _inst_prefix=$(cat <<'ACE777_INST'
export _last_cmd="INIT"
_DUMP_FILE="${ACE777_RUN_DIR:-runs}/EXIT_DUMP.log"
_TRACE_FILE="${ACE777_TRACE_FILE:-/tmp/ace777_cmd_trace.log}"
: > "$_TRACE_FILE"
exec 9>>"$_TRACE_FILE"
trap 'printf "%s\n" "$BASH_COMMAND" >&9' DEBUG
trap 'rc=$?; trap - DEBUG; _last="$(tail -n 3 "$_TRACE_FILE" 2>/dev/null | head -n 1)"; printf "[EXIT_DUMP] %s rc=%s last=[%s] unit=%s\n" "$(date -u +%FT%TZ)" "$rc" "${_last:-N/A}" "${ACE777_UNIT:-?}" >> "$_DUMP_FILE" 2>/dev/null || true' EXIT
ACE777_INST
)
  { printf '%s\n' "$_inst_prefix"; tail -n +85 ./genesis_manifest.txt; } | bash -s 2>&1 | while IFS= read -r line; do
    formatted="[${unit}] ${line}"
    printf '%s\n' "$formatted"
    printf '%s\n' "$formatted" >> "$live_log"
  done
  local rc=$?
  set -e
  _crash_dump "$unit" "$live_log" "$rc" || true
  local exit_line
  exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} how=pipe_run_unit why=rc_${rc} rc=${rc}"
  mkdir -p "${RUN_DIR:-runs}"
  echo "$exit_line" >> "${RUN_DIR:-runs}/PROCESS_EXIT.log" 2>/dev/null || true
  echo "[$unit] $exit_line" >> "${live_log}" 2>/dev/null || true
  echo "[$unit] $exit_line"
  return "$rc"
}

launch_beta() {
  (
    export LOG_FILE="$LOG_BETA"
    export STOP_FILE="STOP_BETA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export LEVERAGE="5"
    export BUY_USDT="${BUY_USDT_BETA:-200}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export IRM_REGIME_GATE="${IRM_REGIME_GATE:-TRUE}"
    export IRM_T_COMPRESSED="${IRM_T_COMPRESSED:-0.05}"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="FALSE"
    export TRAIL_ARM_BPS="${TRAIL_ARM_BPS:-15}"
    export TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-8}"
    export FLUID_EXIT_ENABLED="${FLUID_EXIT_ENABLED:-FALSE}"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export DUO_V63_ALARM_BPS="-3"
    run_unit "BETA_X5"
  ) &
  PID_BETA=$!
  echo "$PID_BETA" > "${RUN_DIR}/beta.pid"
}

launch_alpha() {
  (
    export LOG_FILE="$LOG_ALPHA"
    export STOP_FILE="STOP_ALPHA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export LEVERAGE="13"
    export LEVERAGE_RAMP_ENABLED="TRUE"
    export LEVERAGE_RAMP_START="5"
    export LEVERAGE_RAMP_END="13"
    export LEVERAGE_RAMP_CYCLES="180"
    export BUY_USDT="${ACE_ALPHA_BUY_USDT:-270}"  # force la taille (le champion scelle BUY_USDT_ALPHA=800 avant le launcher)
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"
    export DUO_V6_BURST_X13="TRUE"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export IRM_REGIME_GATE="${IRM_REGIME_GATE:-TRUE}"
    export IRM_T_COMPRESSED="${IRM_T_COMPRESSED:-0.05}"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="FALSE"
    export TRAIL_ARM_BPS="${TRAIL_ARM_BPS:-15}"
    export TRAIL_GIVEBACK_BPS="${TRAIL_GIVEBACK_BPS:-8}"
    export FLUID_EXIT_ENABLED="${FLUID_EXIT_ENABLED:-FALSE}"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export RUN_STATE_ENABLED="TRUE"
    export RUN_STATE_LINK_TOTAL_PNL="TRUE"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA=$!
  echo "$PID_ALPHA" > "${RUN_DIR}/alpha.pid"
}

launch_beta
sleep 2
launch_alpha

echo "Duo en marche. Logs: ${LOG_BETA} | ${LOG_ALPHA}"

export STATE_TAG="$tag"
export STATE_PHASE="running"
./scripts/update_state_md.sh 2>/dev/null || true

wait "$PID_BETA" 2>/dev/null || true
wait "$PID_ALPHA" 2>/dev/null || true

echo "Mission terminée."

stop_vortex_supervisor
rm -f "${RUN_DIR}/master.pid" "${RUN_DIR}/alpha.pid" "${RUN_DIR}/beta.pid"
export STATE_PHASE="ended"
./scripts/update_state_md.sh 2>/dev/null || true
./scripts/post_run_report.sh 2>/dev/null || true

beta_csv="$LOG_BETA"
alpha_csv="$LOG_ALPHA"
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
