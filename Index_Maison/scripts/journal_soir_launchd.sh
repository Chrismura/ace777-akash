#!/bin/bash
# Wrapper LaunchAgent — log + journal du soir
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
LOG_DIR="$ROOT/Index_Maison/scripts/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/journal_soir_$(date +%Y%m%d).log"
{
  echo "=== $(date -u +%Y-%m-%dT%H:%MZ) journal_soir ==="
  # shellcheck disable=SC1091
  [[ -f "$ROOT/veille-punk/obsidian.env" ]] && source "$ROOT/veille-punk/obsidian.env"
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/journal_auto.py" --sync
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/thermo_quotidien_free.py" || echo "THERMO_WARN"
  /usr/bin/python3 "$ROOT/Index_Maison/scripts/memoire_log.py" journal_soir "★" "journal" "snapshot soir auto" || true
  echo "OK"
} >>"$LOG" 2>&1
