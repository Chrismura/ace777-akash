#!/usr/bin/env bash
# Watchdog Ghost — paper + veille. Relance si mort. Ne touche pas ACE.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
LOG="$ROOT/runs/WATCHDOG_GHOST.log"
mkdir -p "$ROOT/runs"
ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
log() { echo "$(ts) $*" | tee -a "$LOG"; }

# --- PAPER ---
if pgrep -f 'scripts/paper_diprip.py' >/dev/null 2>&1; then
  log "PAPER: OK pid=$(pgrep -f 'scripts/paper_diprip.py' | head -1)"
else
  if [ -f STOP_PAPER ]; then
    log "PAPER: mort + STOP_PAPER présent — pas de relance (stop volontaire)"
  else
    log "PAPER: MORT — relance"
    nohup python3 scripts/paper_diprip.py >>runs/PAPER_WATCHDOG_STDOUT.log 2>&1 &
    sleep 2
    if pgrep -f 'scripts/paper_diprip.py' >/dev/null 2>&1; then
      log "PAPER: RELANCÉ pid=$(pgrep -f 'scripts/paper_diprip.py' | head -1)"
    else
      log "PAPER: FAIL relance"
    fi
  fi
fi

# --- VEILLE / digest (Qwen yeux) ---
if pgrep -f 'scripts/digest_watch.py' >/dev/null 2>&1; then
  log "VEILLE: OK pid=$(pgrep -f 'scripts/digest_watch.py' | head -1)"
else
  if [ -f STOP_DIGEST ]; then
    log "VEILLE: mort + STOP_DIGEST présent — pas de relance"
  else
    log "VEILLE: MORT — relance --live"
    nohup python3 scripts/digest_watch.py --live >>runs/DIGEST_WATCHDOG_STDOUT.log 2>&1 &
    sleep 2
    if pgrep -f 'scripts/digest_watch.py' >/dev/null 2>&1; then
      log "VEILLE: RELANCÉ pid=$(pgrep -f 'scripts/digest_watch.py' | head -1)"
    else
      log "VEILLE: FAIL relance"
    fi
  fi
fi

# Fraîcheur DIGEST (info)
if [ -f runs/DIGEST_LATEST.md ]; then
  age=$(( $(date +%s) - $(stat -f %m runs/DIGEST_LATEST.md) ))
  log "DIGEST_LATEST age=${age}s"
fi

# State paper (info)
st=$(ls -t runs/PAPER_V1_*_state.json 2>/dev/null | head -1 || true)
if [ -n "$st" ]; then
  age=$(( $(date +%s) - $(stat -f %m "$st") ))
  log "PAPER_STATE $(basename "$st") age=${age}s"
fi

log "CHECK_DONE"
