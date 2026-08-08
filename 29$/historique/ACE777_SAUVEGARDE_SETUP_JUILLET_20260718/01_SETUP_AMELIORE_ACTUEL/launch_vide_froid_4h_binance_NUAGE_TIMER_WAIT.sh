#!/usr/bin/env bash
# === ESSAIM NUAGE V2.2 — Stroboscope + kill tail/genesis ===
# Enveloppe éphémère /tmp — champion disque INTACT
# Réf: NUAGE_V2.1_STROBOSCOPE_ROBUSTE

set -euo pipefail

ACE777_ROOT="${ACE777_ROOT:-/Users/christophe/ace777-test-day1}"
cd "$ACE777_ROOT"

# ═══ PURGE TOTALE AUTOMATIQUE — à CHAQUE départ (obligatoire) ═══
# NE PAS appeler stop_ace777_hard ici : il tue launch_vide_froid (auto-suicide).
nuage_self_pids() {
  local p="$$" pp=""
  while [ -n "$p" ] && [ "$p" -gt 1 ]; do
    echo "$p"
    pp="$(ps -p "$p" -o ppid= 2>/dev/null | tr -d ' ' || true)"
    [ -z "$pp" ] || [ "$pp" = "$p" ] && break
    p="$pp"
  done
}

nuage_pgrep_kill() {
  local pattern="$1"
  local keep pid args
  keep="$(nuage_self_pids | tr '\n' '|' | sed 's/|$//')"
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    pid="${line%% *}"
    args="${line#* }"
    case "|${keep}|" in *"|${pid}|"*) continue ;; esac
    case "$args" in *launch_vide_froid_4h_binance_NUAGE*) continue ;; esac
    kill -9 "$pid" 2>/dev/null || true
  done < <(pgrep -fl "$pattern" 2>/dev/null || true)
}

nuage_purge_totale() {
  echo "=== NUAGE PURGE TOTALE — début ==="

  rm -f STOP STOP_ALPHA STOP_BETA

  nuage_pgrep_kill "tail -f.*NUAGE"
  nuage_pgrep_kill "tail -n 0 -F.*NUAGE"
  nuage_pgrep_kill "tail -F.*NUAGE"
  nuage_pgrep_kill "ace777_launch_v85_nuage"
  nuage_pgrep_kill "genesis_manifest"
  nuage_pgrep_kill "bash -s"
  nuage_pgrep_kill "watchdog_ace777"
  nuage_pgrep_kill "launch_test_master_base_v8_6_fortress"
  nuage_pgrep_kill "caffeinate -is.*ace777"
  nuage_pgrep_kill "launch_test_master_base"

  RUN_DIR="${RUN_DIR:-runs}"
  rm -f "$RUN_DIR"/master.pid "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid
  rm -f "$RUN_DIR"/alpha_wrapper.pid "$RUN_DIR"/beta_wrapper.pid
  rm -f "$RUN_DIR"/ALPHA_X13_BURST13_genesis.pid "$RUN_DIR"/ALPHA_X13_BURST13_wrapper.pid
  rm -f "$RUN_DIR"/BETA_X5_genesis.pid "$RUN_DIR"/BETA_X5_wrapper.pid
  rm -f "$RUN_DIR"/timer.pid "$RUN_DIR"/supervisor_v9_v2.pid
  rm -f "$RUN_DIR"/duo_state.json "$RUN_DIR"/duo_session.json "$RUN_DIR"/swarm_telemetry.json
  rm -f "$RUN_DIR"/.NUAGE*.raw.log 2>/dev/null || true

  rm -f /tmp/alpha_heartbeat.txt
  rm -rf /tmp/ace777_ram_exchange 2>/dev/null || true
  mkdir -p /tmp/ace777_ram_exchange

  rm -f /tmp/ace777_launch_v85_nuage_*.sh 2>/dev/null || true

  sleep 1

  _left=""
  _left="$(pgrep -fl "ace777-test-day1|genesis_manifest|bash -s|watchdog_ace777|ace777_launch_v85|launch_test_master" 2>/dev/null | grep -vi ollama || true)"
  if [ -n "$_left" ]; then
    _left="$(echo "$_left" | while IFS= read -r line; do
      pid="${line%% *}"
      case "$(nuage_self_pids | tr '\n' ' ')" in *" $pid "*|"$pid "*) continue ;; esac
      echo "$line"
    done)"
  fi
  if [ -n "$_left" ]; then
    echo "PURGE_WARN: résidus détectés — 2e passe"
    echo "$_left"
    nuage_pgrep_kill "ace777_launch_v85_nuage"
    nuage_pgrep_kill "bash -s"
    nuage_pgrep_kill "watchdog_ace777"
    sleep 1
  else
    echo "PURGE_OK: zéro process ACE777"
  fi

  echo "PURGE_OK: STOP supprimés | pid/genesis/wrapper/raw/RAM/heartbeat nettoyés"
  echo "=== NUAGE PURGE TOTALE — fin ==="
  echo ""
}

nuage_purge_totale

_args=("$@")
set --
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh
set -- "${_args[@]}"

export RUN_DURATION="${RUN_DURATION:-00:15:00}"
export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --duration)
      shift
      export RUN_DURATION="${1:-00:15:00}"
      ;;
    *)
      echo "Usage: $0 [--duration HH:MM:SS]"
      exit 1
      ;;
  esac
  shift || true
done

export SWARM_COUPLING_ENABLED=TRUE
export SWARM_TELEMETRY_HEARTBEAT_SEC="${SWARM_TELEMETRY_HEARTBEAT_SEC:-2}"
export ACE777_RAM_EXCHANGE="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
mkdir -p "${ACE777_RAM_EXCHANGE}"

export DUO_STATE_FILE="${ACE777_RAM_EXCHANGE}/duo_state.json"
export DUO_SESSION_FILE="${ACE777_RAM_EXCHANGE}/duo_session.json"
export SWARM_TELEMETRY_FILE="${ACE777_RAM_EXCHANGE}/swarm_telemetry.json"
export DUO_V6_BURST_FILE="${ACE777_RAM_EXCHANGE}/duo_burst.json"
export DUO_V63_ALARM_FILE="${ACE777_RAM_EXCHANGE}/duo_v63_alarm.json"

export BETA_LEVERAGE_OVERRIDE=5
export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-NUAGE_SMOKE_15M}"
export ACE777_NUAGE_MODE=TRUE
export ACE777_NUAGE_VERSION="V2.2.1_NO_SUICIDE"

export ALPHA_HEARTBEAT_FILE="/tmp/alpha_heartbeat.txt"

export NUAGE_WATCHDOG_INTERVAL_SEC="${NUAGE_WATCHDOG_INTERVAL_SEC:-30}"
export NUAGE_WATCHDOG_STALE_SEC="${NUAGE_WATCHDOG_STALE_SEC:-60}"
export NUAGE_WATCHDOG_MAX_RELAUNCH="${NUAGE_WATCHDOG_MAX_RELAUNCH:-5}"
export NUAGE_WATCHDOG_INIT_TIMEOUT_SEC="${NUAGE_WATCHDOG_INIT_TIMEOUT_SEC:-120}"
export NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC="${NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC:-60}"

NUAGE_V85="/tmp/ace777_launch_v85_nuage_$$.sh"
export LAUNCH_V85_SCRIPT="${NUAGE_V85}"
export ACE777_GENESIS_SOURCE="${ACE777_ROOT}/genesis_manifest.txt"

cat > "${NUAGE_V85}" <<'NUAGE_V85_EOF'
#!/usr/bin/env bash
set -euo pipefail

if [ -d /app ]; then
  cd /app
else
  cd "${ACE777_ROOT:-/Users/christophe/ace777-test-day1}"
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
    echo "PREFLIGHT_ERR: BINANCE_MODE=live mais ~/.binance_live.env introuvable" >&2
    exit 1
  fi
elif [ -f "${HOME}/.binance_testnet.env" ]; then
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  export BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
  export WATCHDOG_PING_URL="${WATCHDOG_PING_URL:-https://testnet.binancefuture.com/fapi/v1/ping}"
  echo "INFO_CLES: testnet depuis ${HOME}/.binance_testnet.env"
fi

RUN_DIR="${RUN_DIR:-runs}"
duration_sec="${RUN_SEC_OVERRIDE:-900}"
tag="${TEST_TAG_OVERRIDE:-NUAGE_SMOKE_15M}"
mkdir -p "$RUN_DIR"

RAM="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
mkdir -p "$RAM"
export DUO_STATE_FILE="${DUO_STATE_FILE:-${RAM}/duo_state.json}"
export DUO_SESSION_FILE="${DUO_SESSION_FILE:-${RAM}/duo_session.json}"
export SWARM_TELEMETRY_FILE="${SWARM_TELEMETRY_FILE:-${RAM}/swarm_telemetry.json}"
export DUO_V6_BURST_FILE="${DUO_V6_BURST_FILE:-${RAM}/duo_burst.json}"
export DUO_V63_ALARM_FILE="${DUO_V63_ALARM_FILE:-${RAM}/duo_v63_alarm.json}"
export SWARM_COUPLING_ENABLED=TRUE
export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
export LOG_BETA="${RUN_DIR}/${tag}_BETA_X5.csv"
export LOG_ALPHA="${RUN_DIR}/${tag}_ALPHA_X13_BURST13.csv"

if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ]; then
  chmod +x ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
fi

rm -f STOP STOP_ALPHA STOP_BETA
rm -f "$RUN_DIR"/alpha_wrapper.pid "$RUN_DIR"/beta_wrapper.pid "$RUN_DIR"/master.pid
rm -f "$RUN_DIR"/ALPHA_X13_BURST13_genesis.pid "$RUN_DIR"/ALPHA_X13_BURST13_wrapper.pid
rm -f "$RUN_DIR"/BETA_X5_genesis.pid "$RUN_DIR"/BETA_X5_wrapper.pid
rm -f "$DUO_SESSION_FILE" "$DUO_STATE_FILE" "$SWARM_TELEMETRY_FILE"
rm -f "${ALPHA_HEARTBEAT_FILE}"
if [ -f "$RUN_DIR/timer.pid" ]; then
  kill "$(cat "$RUN_DIR/timer.pid")" 2>/dev/null || true
fi
pkill -f "File.write('STOP_ALPHA'" 2>/dev/null || true
rm -f "$RUN_DIR/timer.pid"

./scripts/preflight_ace777.sh

echo $$ > "${RUN_DIR}/master.pid"
echo "NUAGE_V2.1: kill -9 -$$ pour arrêter"

start_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
end_utc="$(ruby -e 'puts (Time.now + ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- "$duration_sec" 2>/dev/null || echo N/A)"
export RUN_START_UTC="$start_utc" RUN_END_UTC="$end_utc"

ruby -rjson -e '
  require "fileutils"
  rd = ENV.fetch("RUN_DIR", "runs")
  FileUtils.mkdir_p(rd)
  meta = {
    "start_utc" => ENV["RUN_START_UTC"],
    "planned_end_utc" => ENV.fetch("RUN_END_UTC", ""),
    "tag" => ENV.fetch("TEST_TAG_OVERRIDE", ""),
    "launcher" => "NUAGE_V2.1_STROBOSCOPE",
    "version" => ENV.fetch("ACE777_NUAGE_VERSION", "V2.1"),
    "swarm" => ENV.fetch("SWARM_COUPLING_ENABLED", "?"),
    "nuage_max_age_ms" => ENV.fetch("NUAGE_TENSION_MAX_AGE_MS", "?"),
    "beta_leverage" => ENV.fetch("BETA_LEVERAGE_OVERRIDE", "5"),
    "ram_exchange" => ENV.fetch("ACE777_RAM_EXCHANGE", "?"),
    "alpha_heartbeat" => ENV.fetch("ALPHA_HEARTBEAT_FILE", "?"),
    "watchdog_stale_sec" => ENV.fetch("NUAGE_WATCHDOG_STALE_SEC", "60"),
    "watchdog_init_timeout_sec" => ENV.fetch("NUAGE_WATCHDOG_INIT_TIMEOUT_SEC", "120"),
    "watchdog_max_relaunch" => ENV.fetch("NUAGE_WATCHDOG_MAX_RELAUNCH", "5"),
    "index_sync" => "DISABLED_THESIS_3"
  }
  File.write(File.join(rd, "#{meta["tag"]}_run_meta.json"), JSON.pretty_generate(meta))
' 2>/dev/null || true

echo "=== ${tag} — ESSAIM NUAGE V2.1 Stroboscope Robuste ==="
echo "Start UTC: $start_utc | End UTC: $end_utc"
echo "SWARM=ON | BETA x${BETA_LEVERAGE_OVERRIDE:-5} | GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms"
echo "Heartbeat: ${ALPHA_HEARTBEAT_FILE} | Stale=${NUAGE_WATCHDOG_STALE_SEC:-60}s"
echo "MaxRelaunch=${NUAGE_WATCHDOG_MAX_RELAUNCH:-5} | INDEX SYNC: OFF"

NUAGE_RELAUNCH_COUNT=0
NUAGE_WATCHDOG_GRACE_UNTIL=0
NUAGE_ALPHA_BOOT_EPOCH=0
PID_ALPHA_WRAPPER=0
PID_BETA_WRAPPER=0
PID_SEMANTIC_WATCHDOG=0
PID_WATCHDOG=0
PID_TIMER=0

_linebuf() {
  if command -v stdbuf >/dev/null 2>&1; then
    stdbuf -oL -eL "$@"
  else
    "$@"
  fi
}

nuage_resolve_bash_s_pid() {
  local parent="$1"
  local pid="" gpid="" args="" i=0

  [ -n "$parent" ] || return 1

  while [ "$i" -lt 100 ]; do
    for pid in $(pgrep -P "$parent" 2>/dev/null || true); do
      args="$(ps -p "$pid" -o args= 2>/dev/null || true)"
      case "$args" in
        *"bash -s"*|*"bash -s "*) echo "$pid"; return 0 ;;
      esac
      for gpid in $(pgrep -P "$pid" 2>/dev/null || true); do
        args="$(ps -p "$gpid" -o args= 2>/dev/null || true)"
        case "$args" in
          *"bash -s"*|*"bash -s "*) echo "$gpid"; return 0 ;;
        esac
      done
    done
    sleep 0.1
    i=$((i + 1))
  done

  echo "$parent"
  return 0
}

nuage_kill_tail_for_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local tpf="${RUN_DIR}/${unit}_tail.pid"
  local tp=""

  [ -f "$tpf" ] && tp="$(tr -d ' \n\r' <"$tpf" 2>/dev/null || true)"
  if [ -n "$tp" ]; then
    pkill -P "$tp" 2>/dev/null || true
    kill -TERM "$tp" 2>/dev/null || true
    sleep 0.5
    pkill -KILL -P "$tp" 2>/dev/null || true
    kill -KILL "$tp" 2>/dev/null || true
  fi
  pkill -f "tail -n 0 -F ${raw_log}" 2>/dev/null || true
  pkill -f "tail -F ${raw_log}" 2>/dev/null || true
  rm -f "$tpf"
}

nuage_kill_genesis_tree() {
  local unit="$1"
  local gpf="${RUN_DIR}/${unit}_genesis.pid"
  local wpf="${RUN_DIR}/${unit}_wrapper.pid"
  local gp="" wp=""

  nuage_kill_tail_for_unit "$unit"

  [ -f "$gpf" ] && gp="$(tr -d ' \n\r' <"$gpf" 2>/dev/null || true)"
  [ -f "$wpf" ] && wp="$(tr -d ' \n\r' <"$wpf" 2>/dev/null || true)"

  if [ -n "$gp" ]; then
    pkill -P "$gp" 2>/dev/null || true
    kill -TERM "$gp" 2>/dev/null || true
    sleep 2
    pkill -KILL -P "$gp" 2>/dev/null || true
    kill -KILL "$gp" 2>/dev/null || true
  fi

  if [ -n "$wp" ] && [ "$wp" != "$gp" ]; then
    pkill -P "$wp" 2>/dev/null || true
    kill -TERM "$wp" 2>/dev/null || true
    sleep 1
    pkill -KILL -P "$wp" 2>/dev/null || true
    kill -KILL "$wp" 2>/dev/null || true
  fi

  rm -f "$gpf" "$wpf"
}

cleanup() {
  kill "${PID_WATCHDOG:-}" "${PID_SEMANTIC_WATCHDOG:-}" 2>/dev/null || true
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  nuage_kill_genesis_tree "ALPHA_X13_BURST13"
  nuage_kill_genesis_tree "BETA_X5"
  kill "${PID_ALPHA_WRAPPER:-}" "${PID_BETA_WRAPPER:-}" "${PID_TIMER:-}" 2>/dev/null || true
  echo "NUAGE_V2.1 arrêt global."
}
trap cleanup SIGINT SIGTERM

ruby -e "sleep ${duration_sec}; File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &
PID_TIMER=$!
echo "$PID_TIMER" > "${RUN_DIR}/timer.pid"

chmod +x ./scripts/watchdog_ace777.sh 2>/dev/null || true
./scripts/watchdog_ace777.sh &
PID_WATCHDOG=$!

ace777_stream_genesis() {
  local genesis="${ACE777_GENESIS_SOURCE:-./genesis_manifest.txt}"
  {
    cat <<'NUAGE_PREAMBLE'

NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"

duo_hunter_phase_barrier() { :; }

alpha_touch_heartbeat() {
  duo_is_hunter || return 0
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}" 2>/dev/null || true
}

nuage_cloud_tension_gate() {
  local cycle="$1"
  local max_age="${NUAGE_TENSION_MAX_AGE_MS:-800}"
  local age_ms path
  duo_is_hunter || return 0
  path="${DUO_STATE_FILE:-runs/duo_state.json}"
  age_ms="$(ruby -rjson -e '
    path = ARGV[0]
    begin
      j = JSON.parse(File.read(path))
      ts = (j["ts_ms"].to_i rescue 0)
      age = ((Time.now.to_f * 1000).to_i - ts)
      age = 0 if age < 0
      print(age)
    rescue
      print(999999)
    end
  ' -- "$path" 2>/dev/null || echo 999999)"
  if [ "$age_ms" -gt "$max_age" ]; then
    echo "$(date -u +%FT%TZ),${cycle},SKIP,SKIPPED,,,,,0,tension_stale,reason=nuage_age_ms=${age_ms} thresh=${max_age}" >> "$LOG_FILE"
    sk_lev="$C_C"; num_ge "$current_leverage" "13" && sk_lev="$C_G"; num_le "$current_leverage" "5" && sk_lev="$C_Y"
    echo "${C_C}$(date -u +%H:%M:%S)${C_N} ${sk_lev}x$current_leverage${C_N} ${C_C}#${cycle}${C_N} SKIP ${C_Y}| tension_stale age=${age_ms}ms>${max_age}ms (NUAGE)${C_N}"
    alpha_touch_heartbeat
    return 1
  fi
  return 0
}

NUAGE_PREAMBLE
    tail -n +85 "$genesis" | awk '
      /^duo_hunter_phase_barrier\(\) \{/ {
        print "duo_hunter_phase_barrier() { :; }"
        skip=1; next
      }
      skip { if (/^\}$/) skip=0; next }
      /^[[:space:]]*duo_hunter_phase_barrier "\$i"/ {
        print "  : # NUAGE bypass barrier (index ignored)"
        next
      }
      /^[[:space:]]*duo_touch_heartbeat$/ && !hb_done {
        print "  duo_touch_heartbeat"
        print "  alpha_touch_heartbeat"
        hb_done=1; next
      }
      /^[[:space:]]*raw_qty="\$\(num_div/ && !gate_done {
        print "  if duo_is_hunter; then"
        print "    nuage_cloud_tension_gate \"$i\" || { alpha_touch_heartbeat; sleep \"$SLEEP_SEC\"; continue; }"
        print "  fi"
        gate_done=1
      }
      { print }
    '
  } | bash -s
}

run_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  local wrapper_pid=0
  local genesis_pid=0
  local tee_pid=0

  : >"$raw_log"

  (
    trap '' PIPE
    _linebuf tail -n 0 -F "$raw_log" 2>/dev/null | while IFS= read -r line || [ -n "$line" ]; do
      [ -z "${line//[[:space:]]/}" ] && continue
      printf '[%s] %s\n' "$unit" "$line" >>"$live_log" 2>/dev/null || true
      printf '[%s] %s\n' "$unit" "$line"
    done
  ) &
  tee_pid=$!
  echo "$tee_pid" >"${RUN_DIR}/${unit}_tail.pid"

  set +e
  _linebuf ace777_stream_genesis >>"$raw_log" 2>&1 &
  wrapper_pid=$!
  genesis_pid="$(nuage_resolve_bash_s_pid "$wrapper_pid")"
  set -e

  echo "$genesis_pid" >"${RUN_DIR}/${unit}_genesis.pid"
  echo "$wrapper_pid" >"${RUN_DIR}/${unit}_wrapper.pid"

  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}

launch_beta() {
  (
    trap '' PIPE
    set +o pipefail
    export LOG_FILE="$LOG_BETA"
    export STOP_FILE="STOP_BETA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export LEVERAGE="${BETA_LEVERAGE_OVERRIDE:-5}"
    export BUY_USDT="${BUY_USDT_BETA:-200}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export DUO_V63_ALARM_BPS="-3"
    run_unit "BETA_X5"
  ) &
  PID_BETA_WRAPPER=$!
  echo "$PID_BETA_WRAPPER" > "${RUN_DIR}/beta_wrapper.pid"
}

launch_alpha() {
  NUAGE_ALPHA_BOOT_EPOCH="$(date +%s)"
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"

  (
    export LOG_FILE="$LOG_ALPHA"
    export STOP_FILE="STOP_ALPHA"
    export DUO_STATE_FILE DUO_SESSION_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
    export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
    export LEVERAGE="13"
    export LEVERAGE_RAMP_ENABLED="TRUE"
    export LEVERAGE_RAMP_START="13"
    export LEVERAGE_RAMP_END="13"
    export LEVERAGE_RAMP_CYCLES="180"
    export BUY_USDT="${BUY_USDT_ALPHA:-800}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"
    export DUO_V6_BURST_X13="TRUE"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export RUN_STATE_ENABLED="TRUE"
    export RUN_STATE_LINK_TOTAL_PNL="TRUE"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA_WRAPPER=$!
  echo "$PID_ALPHA_WRAPPER" > "${RUN_DIR}/alpha_wrapper.pid"
}

nuage_semantic_watchdog() {
  local hb="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
  local stale_limit="${NUAGE_WATCHDOG_STALE_SEC:-60}"
  local check_interval="${NUAGE_WATCHDOG_INTERVAL_SEC:-30}"
  local max_relaunch="${NUAGE_WATCHDOG_MAX_RELAUNCH:-5}"
  local init_timeout="${NUAGE_WATCHDOG_INIT_TIMEOUT_SEC:-120}"
  local grace_sec="${NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC:-60}"
  local now age_sec boot_age

  while [ -f "${RUN_DIR}/master.pid" ] && kill -0 "$(cat "${RUN_DIR}/master.pid")" 2>/dev/null; do
    sleep "$check_interval"

    now="$(date +%s)"

    if [ ! -f "$hb" ]; then
      if [ "${NUAGE_ALPHA_BOOT_EPOCH:-0}" -gt 0 ]; then
        boot_age=$((now - NUAGE_ALPHA_BOOT_EPOCH))
        if [ "$boot_age" -gt "$init_timeout" ]; then
          echo "CRITICAL: ALPHA init timeout > ${init_timeout}s. Emergency halt."
          touch STOP_ALPHA STOP_BETA
          break
        fi
      fi
      continue
    fi

    if [ "${NUAGE_WATCHDOG_GRACE_UNTIL:-0}" -gt "$now" ]; then
      continue
    fi

    age_sec="$(ruby -e '
      require "time"
      begin
        t = Time.parse(File.read(ARGV[0]).strip).utc
        puts((Time.now.utc - t).to_i)
      rescue
        puts 999999
      end
    ' "$hb" 2>/dev/null || echo 999999)"

    if [ "$age_sec" -le "$stale_limit" ]; then
      continue
    fi

    NUAGE_RELAUNCH_COUNT=$((NUAGE_RELAUNCH_COUNT + 1))
    echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) — relance #${NUAGE_RELAUNCH_COUNT}/${max_relaunch}"

    if [ "$NUAGE_RELAUNCH_COUNT" -gt "$max_relaunch" ]; then
      echo "WATCHDOG_SEMANTIC: max_relaunch=${max_relaunch} atteint → STOP session"
      touch STOP_ALPHA STOP_BETA
      break
    fi

    nuage_kill_genesis_tree "ALPHA_X13_BURST13"
    kill "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true
    wait "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true

    date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"
    NUAGE_WATCHDOG_GRACE_UNTIL=$((now + grace_sec))

    launch_alpha
    echo "WATCHDOG_SEMANTIC: ALPHA relancée — grace ${grace_sec}s — ts_ms BETA = vérité"
  done
}

launch_beta
sleep 2
launch_alpha
nuage_semantic_watchdog &
PID_SEMANTIC_WATCHDOG=$!

echo "NUAGE_V2.1 duo en marche."
echo "Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log"
echo "Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}"

# Attendre le TIMER (durée nominale), pas la mort d'un wrapper.
# Sinon: après relance ALPHA, wait ALPHA est déjà mort → dès que BETA sort
# le master affiche "mission terminée" au bout d'1h au lieu de 4h.
echo "NUAGE_V2.2: attente timer ${duration_sec}s (pid=${PID_TIMER}) — pas de fin précoce wrapper"
wait "$PID_TIMER" 2>/dev/null || true
touch STOP_ALPHA STOP_BETA 2>/dev/null || true
sleep 2

kill "${PID_SEMANTIC_WATCHDOG:-}" "${PID_WATCHDOG:-}" 2>/dev/null || true
nuage_kill_genesis_tree "BETA_X5"
nuage_kill_genesis_tree "ALPHA_X13_BURST13"
# PIDs disque = vérité (relances watchdog)
[ -f "${RUN_DIR}/alpha_wrapper.pid" ] && kill "$(tr -d ' \n\r' <"${RUN_DIR}/alpha_wrapper.pid")" 2>/dev/null || true
[ -f "${RUN_DIR}/beta_wrapper.pid" ] && kill "$(tr -d ' \n\r' <"${RUN_DIR}/beta_wrapper.pid")" 2>/dev/null || true
kill "${PID_ALPHA_WRAPPER:-}" "${PID_BETA_WRAPPER:-}" 2>/dev/null || true
pkill -f "tail -n 0 -F ${RUN_DIR}/\.${tag}_" 2>/dev/null || true
pkill -f "tail -F ${RUN_DIR}/\.${tag}_" 2>/dev/null || true
echo "NUAGE_V2.2 mission terminée."
rm -f "${RUN_DIR}/master.pid" "${RUN_DIR}/alpha_wrapper.pid" "${RUN_DIR}/beta_wrapper.pid" "${RUN_DIR}/timer.pid"
rm -f "${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid" "${RUN_DIR}/ALPHA_X13_BURST13_wrapper.pid"
rm -f "${RUN_DIR}/ALPHA_X13_BURST13_tail.pid"
rm -f "${RUN_DIR}/BETA_X5_genesis.pid" "${RUN_DIR}/BETA_X5_wrapper.pid"
rm -f "${RUN_DIR}/BETA_X5_tail.pid"
NUAGE_V85_EOF

chmod +x "${NUAGE_V85}"

echo ""
echo "=== ESSAIM NUAGE V2.1 — Stroboscope Robuste ==="
echo "Version: ${ACE777_NUAGE_VERSION}"
echo "SWARM=ON | BETA x5 | GATE=${NUAGE_TENSION_MAX_AGE_MS}ms"
echo "Heartbeat: ${ALPHA_HEARTBEAT_FILE}"
echo "Durée: ${RUN_DURATION} | Tag: ${TEST_TAG_OVERRIDE}"
echo "Lanceur V8.5: ${NUAGE_V85}"
echo "Champion disque: NON MODIFIÉ"
echo ""

if [ "${CAFFEINATE_RUN}" = "TRUE" ] && command -v caffeinate >/dev/null 2>&1; then
  exec caffeinate -is env ACE777_ROOT="$ACE777_ROOT" ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
else
  exec env ACE777_ROOT="$ACE777_ROOT" ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
fi
