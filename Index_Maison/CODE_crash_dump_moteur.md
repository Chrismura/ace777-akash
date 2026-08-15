# RÉPONSE CODEUR (task code.ia · Puter Grok (gratuit)) — 2026-08-14T06:33:12.289393Z

```bash
_crash_dump() {
  local unit="$1" live_log="$2" rc="$3" ts dump_file
  [ "$rc" -eq 0 ] && return 0
  ts=$(date -u +%Y%m%d_%H%M%S 2>/dev/null || echo "now")
  dump_file="${RUN_DIR:-runs}/CRASH_DUMP_${unit}_${ts}.log"
  mkdir -p "${RUN_DIR:-runs}" 2>/dev/null || true
  tail -n 20 "$live_log" 2>/dev/null >> "$dump_file" || true
  if [ -f /tmp/ace777_fatal_rc1.log ]; then
    echo "=== FATAL_RC1 ===" >> "$dump_file" || true
    cat /tmp/ace777_fatal_rc1.log >> "$dump_file" 2>/dev/null || true
  fi
  if declare -f private_get >/dev/null 2>&1; then
    echo "=== POSITION_RISK ===" >> "$dump_file" || true
    private_get "${BASE_URL}/fapi/v2/positionRisk" >> "$dump_file" 2>/dev/null || true
  fi
}

run_unit() {
  trap '' PIPE
  local unit="$1"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  local rc=0
  set +e
  set +o pipefail
  tail -n +85 ./genesis_manifest.txt | bash -s 2>&1 | while IFS= read -r line || [ -n "$line" ]; do
    formatted="[${unit}] ${line}"
    printf '%s\n' "$formatted"
    printf '%s\n' "$formatted" >> "$live_log" 2>/dev/null || true
  done
  rc=${PIPESTATUS[1]:-0}
  trap - PIPE
  set -o pipefail
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
```
