#!/usr/bin/env bash
# patch_process_exit_log.sh — ajoute PROCESS_EXIT + PROCESS_DIE sur un launcher NUAGE-like
# Usage: ./scripts/patch_process_exit_log.sh path/to/launcher.sh
set -euo pipefail
TARGET="${1:-}"
[ -n "$TARGET" ] && [ -f "$TARGET" ] || { echo "Usage: $0 <launcher.sh>" >&2; exit 1; }

python3 - "$TARGET" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
changed = False

old_wait = '''  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}'''

new_wait = '''  set +e
  wait "$wrapper_pid" 2>/dev/null
  local rc=$?
  set -e

  # PROCESS_EXIT (E10) — ne plus perdre le code/signal de mort
  local how="exit" sig="" why=""
  if [ "$rc" -eq 0 ]; then
    how="exit0"
    why="clean_end_or_self_exit_0"
  elif [ "$rc" -gt 128 ]; then
    how="signal"
    sig=$((rc - 128))
    why="killed_by_signal_${sig}"
  else
    why="nonzero_rc_${rc}"
  fi
  local exit_line
  exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} wrapper=${wrapper_pid} genesis=${genesis_pid:-?} how=${how} why=${why} rc=${rc}"
  mkdir -p "${RUN_DIR}"
  echo "$exit_line" >> "${RUN_DIR}/PROCESS_EXIT.log" 2>/dev/null || true
  echo "$exit_line" >> "$live_log" 2>/dev/null || true
  echo "[$unit] ${C_Y:-}${exit_line}${C_N:-}"
  if [ "$rc" -ne 0 ] && [ -f "$raw_log" ]; then
    cp -f "$raw_log" "${RUN_DIR}/.${tag}_${unit}.raw.EXIT.rc${rc}.log" 2>/dev/null || true
  fi

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}'''

if "PROCESS_EXIT unit=" in text:
    print(f"skip wait (déjà patché): {path}")
elif old_wait in text:
    text = text.replace(old_wait, new_wait, 1)
    changed = True
    print(f"patched wait: {path}")
else:
    print(f"WARN: bloc wait NUAGE introuvable: {path}")

old_pre = '''NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"

duo_hunter_phase_barrier() { :; }'''

q = chr(39)
new_pre = (
    'NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"\n'
    'ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"\n'
    '\n'
    '# PROCESS_DIE — dernière commande si set -e / signal tue bash -s (E10)\n'
    '_ACE777_DIE_LOGGED=0\n'
    'ace777_process_die_log() {\n'
    '  local ec=${1:-$?}\n'
    '  [ "${_ACE777_DIE_LOGGED:-0}" = "1" ] && return 0\n'
    '  _ACE777_DIE_LOGGED=1\n'
    '  echo "PROCESS_DIE | ts=$(date -u +%Y-%m-%dT%H:%M:%SZ) role=${DUO_ROLE:-?} stop=${STOP_FILE:-?} ec=${ec} last_cmd=${BASH_COMMAND:-?} line=${BASH_LINENO[0]:-?}"\n'
    '}\n'
    f'trap {q}ace777_process_die_log $?{q} ERR\n'
    f'trap {q}ace777_process_die_log $?{q} EXIT\n'
    '\n'
    'duo_hunter_phase_barrier() { :; }'
)

if "PROCESS_DIE |" in text and "ace777_process_die_log" in text:
    print(f"skip trap (déjà patché): {path}")
elif old_pre in text:
    text = text.replace(old_pre, new_pre, 1)
    changed = True
    print(f"patched trap: {path}")
else:
    print(f"WARN: preamble NUAGE introuvable (trap non appliqué): {path}")

# Fallback v8.5-style run_unit (pipe) — log rc simple
old_v85 = '''  local rc=$?
  set -e
  return "$rc"
}'''

new_v85 = '''  local rc=$?
  set -e
  local exit_line
  exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} how=pipe_run_unit why=rc_${rc} rc=${rc}"
  mkdir -p "${RUN_DIR:-runs}"
  echo "$exit_line" >> "${RUN_DIR:-runs}/PROCESS_EXIT.log" 2>/dev/null || true
  echo "[$unit] $exit_line" >> "${live_log}" 2>/dev/null || true
  echo "[$unit] $exit_line"
  return "$rc"
}'''

if "run_unit()" in text and "ace777_stream_genesis" not in text and "PROCESS_EXIT unit=" not in text:
    if old_v85 in text and text.count(old_v85) == 1:
        text = text.replace(old_v85, new_v85, 1)
        changed = True
        print(f"patched v8.5 pipe run_unit: {path}")

if changed:
    path.write_text(text)
    print(f"OK wrote {path}")
else:
    print(f"no change: {path}")
PY
