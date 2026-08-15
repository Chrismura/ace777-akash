#!/usr/bin/env bash
# SUPERVISION AUTONOME — run 4h 14/08 (en l'absence de Christophe)
# Surveille : process vivants, PROCESS_EXIT rc!=0, EXIT_DUMP rc!=0, cycles, PNL.
# Log heartbeat toutes les 60s + detection immediate d'anomalie.
set -u
ROOT="/Users/christophe/ace777-test-day1"
RUNS="$ROOT/runs"
LOG="$ROOT/runs/SUPERVISION_4H_$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$RUNS"
{
  echo "=== SUPERVISION START $(date -u +%FT%TZ) ==="
  echo "Master: launch_test_master_base_v8_5_impact_GEMINI_TEST.sh (instrumente)"
  echo "Setup : ALPHA x13 fixe (gemini), BETA x3 | Durée: 4h | Testnet"
} >> "$LOG"

last_beta=0; last_alpha=0
while true; do
  ts="$(date -u +%FT%TZ)"
  # --- 1. Process vivants ---
  lanceur=$(pgrep -f "launch_vortex_v2_collab" | wc -l | tr -d ' ')
  master=$(pgrep -f "v8_6_fortress|v8_5_impact" | wc -l | tr -d ' ')
  bshell=$(pgrep -f "bash -s" | wc -l | tr -d ' ')
  # --- 2. PROCESS_EXIT recents (rc!=0) ---
  rc1=$(grep -c "why=rc_1 rc=1" "$RUNS/PROCESS_EXIT.log" 2>/dev/null || echo 0)
  # --- 3. EXIT_DUMP recents ---
  dump=$(tail -3 "$RUNS/EXIT_DUMP.log" 2>/dev/null | grep -c "rc=[1-9]" || echo 0)
  # --- 4. Cycles (dernier # vu par bot) ---
  cb="$(grep -oE "#[0-9]+" "$RUNS/${tag:-MASTER_VORTEX_V2_COLLAB_4H}_LIVE_COLOR.log" 2>/dev/null | tail -1)"
  beta_n=$(grep -c "BETA" "$RUNS/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log" 2>/dev/null || echo 0)
  # --- 5. FILLED aujourd'hui ---
  f_beta=$(grep -cE "^2026-08-14.*FILLED" "$RUNS/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv" 2>/dev/null || echo 0)
  f_alpha=$(grep -cE "^2026-08-14.*FILLED" "$RUNS/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv" 2>/dev/null || echo 0)
  # --- Log heartbeat ---
  echo "$ts | proc:l=$lanceur m=$master bs=$bshell | rc1_total=$rc1 dump_err=$dump | beta_csv=$f_beta alpha_csv=$f_alpha" >> "$LOG"
  # --- ALERTE : tout mort ---
  if [ "$lanceur" -eq 0 ] && [ "$master" -eq 0 ]; then
    echo "$ts | !! ALERTE: AUCUN PROCESS — run mort (attendu seulement si duree atteinte)" >> "$LOG"
    echo "$ts | dernieres lignes LIVE_COLOR:" >> "$LOG"
    tail -5 "$RUNS/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log" 2>/dev/null >> "$LOG"
    echo "$ts | dernier PROCESS_EXIT:" >> "$LOG"
    tail -3 "$RUNS/PROCESS_EXIT.log" 2>/dev/null >> "$LOG"
    echo "$ts | dernier EXIT_DUMP:" >> "$LOG"
    tail -3 "$RUNS/EXIT_DUMP.log" 2>/dev/null >> "$LOG"
  fi
  # --- ALERTE : nouveau rc=1 recent (3 min) ---
  recent_rc1=$(tail -20 "$RUNS/PROCESS_EXIT.log" 2>/dev/null | grep "why=rc_1 rc=1" | wc -l | tr -d ' ')
  if [ "$recent_rc1" -gt 0 ]; then
    echo "$ts | !! ALERTE: $recent_rc1 rc=1 dans les 20 derniers PROCESS_EXIT" >> "$LOG"
    echo "$ts | details:" >> "$LOG"
    tail -20 "$RUNS/PROCESS_EXIT.log" 2>/dev/null | grep "why=rc_1 rc=1" >> "$LOG"
    echo "$ts | EXIT_DUMP contexte:" >> "$LOG"
    tail -5 "$RUNS/EXIT_DUMP.log" 2>/dev/null >> "$LOG"
  fi
  sleep 60
done
