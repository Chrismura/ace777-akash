#!/usr/bin/env bash
# Surveillance du run POST-CORRECTIF rc=1 (14/08) — validation du fix swarm_neighbor_load.
# Log : runs/SURVEILLANCE_FIX_RC1.log  (append-only, horodate)
cd "$(dirname "$0")/.." || exit 1
LOG="runs/SURVEILLANCE_FIX_RC1.log"
mkdir -p runs
while true; do
  ts="$(date -u +%FT%TZ)"
  bots="$(pgrep -f 'bash -s' | wc -l | tr -d ' ')"
  exit_dump="$(tail -1 runs/EXIT_DUMP.log 2>/dev/null)"
  proc_exit="$(tail -1 runs/PROCESS_EXIT.log 2>/dev/null)"
  shock="$(grep -c 'SWARM shockwave' runs/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log 2>/dev/null)"
  echo "[$ts] bots=$bots shockwaves_tot=$shock | last_exit=[$exit_dump] | last_proc=[$proc_exit]" | tee -a "$LOG"
  # Détection mort : si un PROCESS_EXIT rc=1 apparaît APRÈS le démarrage du fix (12:51Z),
  # alerte forte (le fix aurait échoué).
  if echo "$proc_exit" | grep -q "rc=1" && [ "$(echo "$proc_exit" | cut -c2-20)" \> "2026-08-14T12:51:00Z" ]; then
    echo "[$ts] ⚠️ MORT RC=1 DÉTECTÉE APRÈS LE FIX — vérifier immédiatement !" | tee -a "$LOG"
  fi
  sleep 120
done
