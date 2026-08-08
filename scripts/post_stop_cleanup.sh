#!/usr/bin/env bash
# Nettoyage post-run ACE777 — parasites CPU/RAM avant prochain run
# Appelé automatiquement par stop_ace777.sh et stop_ace777_hard.sh
# Usage manuel: ./scripts/post_stop_cleanup.sh

set -uo pipefail
_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

echo "=== POST_STOP_CLEANUP — début ==="

_killed=0

_kill_pattern() {
  local label="$1"
  local pattern="$2"
  local n
  n="$(pgrep -f "$pattern" 2>/dev/null | wc -l | tr -d ' ')"
  if [ "${n:-0}" -gt 0 ]; then
    pkill -9 -f "$pattern" 2>/dev/null || pkill -f "$pattern" 2>/dev/null || true
    echo "CLEANUP: ${label} — ${n} process tué(s)"
    _killed=$((_killed + n))
  fi
}

# 1. Zombies Cursor ripgrep (indexation bloquée — gros CPU)
_kill_pattern "Cursor ripgrep" "ripgrep/bin/rg"

# 2. Ollama llama-server (LLM gate — RAM ~100-500 Mo)
_kill_pattern "Ollama llama-server" "llama-server"

# 3. Caffeinate lié au run ACE777
_kill_pattern "caffeinate run" "caffeinate -is -w"

# 4. Résidus ACE777 (passe légère si stop soft)
for pat in \
  "launch_vortex_v2_collab" \
  "launch_test_master_base" \
  "GEMINI_TEST" \
  "watchdog_ace777" \
  "genesis_manifest" \
  "vortex_supervisor_v2_llm.rb" \
  "tail.*genesis_manifest" \
  "bash -s"
do
  if pgrep -f "$pat" 2>/dev/null | grep -q .; then
    n="$(pgrep -f "$pat" 2>/dev/null | wc -l | tr -d ' ')"
    pkill -9 -f "$pat" 2>/dev/null || true
    echo "CLEANUP: résidu ACE777 [$pat] — ${n} process"
    _killed=$((_killed + n))
  fi
done

sleep 1

# 5. Vérification finale
_left=""
_left="$(pgrep -fl "ace777-test-day1|launch_vortex|launch_test_master|GEMINI_TEST|watchdog_ace777|genesis_manifest|vortex_supervisor_v2_llm" 2>/dev/null || true)"
_rg_left="$(pgrep -fl "ripgrep/bin/rg" 2>/dev/null | wc -l | tr -d ' ')"

if [ -n "$_left" ]; then
  echo "CLEANUP_WARN: process ACE777 résiduels:"
  echo "$_left"
else
  echo "CLEANUP_OK: 0 process ACE777"
fi

if [ "${_rg_left:-0}" -gt 0 ]; then
  echo "CLEANUP_WARN: ${_rg_left} ripgrep Cursor encore actif"
else
  echo "CLEANUP_OK: 0 ripgrep zombie"
fi

# 6. RAM (info — purge sudo = manuel)
if command -v memory_pressure >/dev/null 2>&1; then
  _free="$(memory_pressure 2>/dev/null | awk '/Pages free/{print $3}' | head -1)"
  echo "CLEANUP_INFO: Pages free=${_free:-?} (sudo purge si besoin)"
fi

echo "CLEANUP_OK: STOP/STOP_ALPHA/STOP_BETA conservés"
echo "=== POST_STOP_CLEANUP — fin (tués=${_killed}) ==="
