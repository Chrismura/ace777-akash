#!/usr/bin/env bash
# Arrêt total ACE777 — hygiène profonde (vortex, watchdog, caffeinate, états)
# Usage: ./stop_ace777_hard.sh

set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RUN_DIR="${RUN_DIR:-runs}"

echo "=== STOP_ACE777_HARD — début ==="

# 1. Bloquer toute relance auto
touch STOP STOP_ALPHA STOP_BETA 2>/dev/null || true

# 2. Stop soft (rapport PnL + supervisor propre si possible)
./stop_ace777.sh 2>/dev/null || true

# 3. Process groups depuis pidfiles
for pf in "$RUN_DIR/master.pid" "$RUN_DIR/beta.pid" "$RUN_DIR/alpha.pid" "$RUN_DIR/timer.pid" "$RUN_DIR/supervisor_v9_v2.pid"; do
  if [ -f "$pf" ]; then
    p="$(tr -d ' \n\r' < "$pf" 2>/dev/null || true)"
    if [ -n "$p" ] && kill -0 "$p" 2>/dev/null; then
      kill -TERM -"$p" 2>/dev/null || true
      kill -TERM "$p" 2>/dev/null || true
    fi
  fi
done
sleep 1

# 4. Passe kill large (ordre: enfants → parents)
_pkill_hard() {
  pkill -9 -f "genesis_manifest" 2>/dev/null || true
  pkill -9 -f "tail -n +85" 2>/dev/null || true
  pkill -9 -f "tail.*genesis_manifest" 2>/dev/null || true
  pkill -9 -f "bash -s" 2>/dev/null || true
  pkill -9 -f "launch_test_master_base" 2>/dev/null || true
  pkill -9 -f "launch_test_master" 2>/dev/null || true
  pkill -9 -f "GEMINI_TEST" 2>/dev/null || true
  pkill -9 -f "watchdog_ace777" 2>/dev/null || true
  pkill -9 -f "vortex_supervisor_v2_llm.rb" 2>/dev/null || true
  pkill -9 -f "radar_gate" 2>/dev/null || true
  pkill -9 -f "launch_vortex_v2_collab" 2>/dev/null || true
  pkill -9 -f "launch_test_master_base_v8_6_fortress" 2>/dev/null || true
  pkill -9 -f "ace777_launch_v85_nuage" 2>/dev/null || true
  pkill -9 -f "launch_vide_froid_4h_binance_NUAGE" 2>/dev/null || true
  pkill -9 -f "tail -n 0 -F runs/\\.NUAGE" 2>/dev/null || true
  pkill -9 -f "tail -F runs/\\.NUAGE" 2>/dev/null || true
  pkill -9 -f "caffeinate -is -w" 2>/dev/null || true
  pkill -9 -f "caffeinate -is.*ace777" 2>/dev/null || true
  pkill -9 -f "ace777-test-day1" 2>/dev/null || true
}

_pkill_hard
sleep 1
_pkill_hard

# 5. Sweep résiduel par scan ps
while IFS= read -r pid; do
  [ -n "$pid" ] && kill -9 "$pid" 2>/dev/null || true
done < <(ps -e -o pid= -o args= 2>/dev/null | grep -E "ace777-test-day1|genesis_manifest|launch_vortex|launch_test_master|watchdog_ace777|GEMINI_TEST|vortex_supervisor_v2_llm|ace777_launch_v85_nuage|launch_vide_froid_4h_binance_NUAGE|tail -n 0 -F runs/\\.NUAGE|tail -F runs/\\.NUAGE" | grep -v grep | awk '{print $1}')

# 6. Supervisor script
if [ -x ./scripts/stop_supervisor_v9_v2.sh ]; then
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
fi

# 7. Nettoyage états sémantiques (STOP conservés = pas de relance vortex)
rm -f "$RUN_DIR"/master.pid "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid "$RUN_DIR"/timer.pid
rm -f "$RUN_DIR"/duo_state.json "$RUN_DIR"/duo_session.json "$RUN_DIR"/swarm_telemetry.json
rm -f "$RUN_DIR"/duo_burst.json "$RUN_DIR"/duo_v63_alarm.json 2>/dev/null || true

# 8. Vérification — boucle jusqu'à propre
_left=""
for _ in 1 2 3 4 5; do
  _left="$(pgrep -fl "ace777-test-day1|launch_vortex|launch_test_master|GEMINI_TEST|watchdog_ace777|genesis_manifest|vortex_supervisor_v2_llm|ace777_launch_v85_nuage|launch_vide_froid_4h_binance_NUAGE|tail -n 0 -F runs/|tail -F runs/\\.NUAGE" 2>/dev/null || true)"
  if [ -z "$_left" ]; then
    break
  fi
  echo "=== Passe extra (résidu) ==="
  echo "$_left"
  _pkill_hard
  sleep 1
done

echo ""
if pgrep -fl "ace777-test-day1|launch_vortex|launch_test_master|GEMINI_TEST|watchdog_ace777|genesis_manifest|vortex_supervisor_v2_llm|ace777_launch_v85_nuage|launch_vide_froid_4h_binance_NUAGE|tail -n 0 -F runs/|tail -F runs/\\.NUAGE" >/dev/null 2>&1; then
  echo "STOP_HARD_WARN: processus résiduels — vérifier manuellement:"
  pgrep -fl "ace777|launch_vortex|launch_test|GEMINI|watchdog_ace777|genesis|vortex_supervisor" 2>/dev/null || true
  exit 1
fi

echo "STOP_HARD_OK: zéro process ACE777"
echo "STOP_HARD_OK: STOP/STOP_ALPHA/STOP_BETA posés (relance bloquée)"
echo "STOP_HARD_OK: pid + duo_state + swarm nettoyés"
export STATE_PHASE="stopped"
./scripts/update_state_md.sh 2>/dev/null || true

# 9. Nettoyage parasites (ripgrep, Ollama, résidus) — automatique chaque stop
if [ -x ./scripts/post_stop_cleanup.sh ]; then
  ./scripts/post_stop_cleanup.sh
fi

echo "=== STOP_ACE777_HARD — fin ==="
