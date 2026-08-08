#!/usr/bin/env bash
# Arrêt propre superviseur Vortex v2
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"
PID_FILE="runs/supervisor_v9_v2.pid"

if [ -f "$PID_FILE" ]; then
  spid="$(cat "$PID_FILE" 2>/dev/null || true)"
  if [ -n "$spid" ] && kill -0 "$spid" 2>/dev/null; then
    kill "$spid" 2>/dev/null || true
    sleep 0.2
    kill -9 "$spid" 2>/dev/null || true
  fi
  rm -f "$PID_FILE"
fi

pkill -f "vortex_supervisor_v2_llm.rb" 2>/dev/null || true
