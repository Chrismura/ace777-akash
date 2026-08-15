#!/usr/bin/env bash
# =============================================================================
# APPEL_FIN_RUN_4H.sh — fin du run 4h (comparaison hub) :
#   1) attend la fin (process GO_VORTEX / launch_test_master morts, max 6h)
#   2) calcule le bilan des trades du run 4h (CSV filtre > 17:00 UTC)
#   3) ecrit RAPPORT_FIN_RUN_4H.md
#   4) appelle Cortana (cortana_thermo.py alert) pour prevenir Christophe
# Cree 2026-08-12 19:45 par Buffy (point de controle ~23:00).
# Usage : ./APPEL_FIN_RUN_4H.sh   (en detache, start_new_session)
# =============================================================================
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

LOG="runs/APPEL_FIN_RUN_4H.log"
CSV="runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"
REPORT="runs/RAPPORT_FIN_RUN_4H.md"
echo "=== $(date '+%H:%M:%S') FIN-RUN : surveille la fin du run 4h (hub) ===" | tee -a "$LOG"

# 1) Attendre la fin du run (max 6h = 21600s)
MAX_WAIT=21600
elapsed=0
while [ "$elapsed" -lt "$MAX_WAIT" ]; do
  alive=$(pgrep -f 'GO_VORTEX_V2|launch_vortex_v2|launch_test_master_base_v8' | grep -v grep | wc -l | tr -d ' ')
  if [ "$alive" -eq 0 ]; then
    echo "=== $(date '+%H:%M:%S') RUN TERMINE (process morts) ===" | tee -a "$LOG"
    break
  fi
  sleep 30
  elapsed=$((elapsed + 30))
done

if [ "$elapsed" -ge "$MAX_WAIT" ]; then
  echo "=== $(date '+%H:%M:%S') TIMEOUT 6h — je fais quand meme le bilan ===" | tee -a "$LOG"
fi

# 2) petit temps pour laisser les fichiers se fermer
sleep 15

# 3) Bilan des trades du run 4h (filtre > 17:00 UTC = 2026-08-12T17:)
echo "=== $(date '+%H:%M:%S') CALCUL BILAN (filtre > 17:00 UTC) ===" | tee -a "$LOG"
if [ -f "$CSV" ]; then
  # lignes du run 4h avec un trade (BUY/SELL rempli)
  grep '2026-08-12T1[7-9]\|2026-08-12T2[0-1]' "$CSV" 2>/dev/null | \
    awk -F, '$3=="BUY" || $3=="SELL" {print}' > /tmp/run4h_trades.csv
  NB=$(wc -l < /tmp/run4h_trades.csv | tr -d ' ')
  PNL=$(awk -F, 'NR>0 {s+=$9} END {printf "%.2f", s}' /tmp/run4h_trades.csv)
  echo "trades: $NB | pnl: $PNL USDT" | tee -a "$LOG"
else
  NB="?"; PNL="?"
  echo "CSV introuvable: $CSV" | tee -a "$LOG"
fi

# 4) ecrire le rapport
{
  echo "# RAPPORT FIN RUN 4H — COMPARAISON HUB (2026-08-12)"
  echo
  echo "- Genere : $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  echo "- Run : MASTER_VORTEX_V2_COLLAB_4H (gate hub, 19:00 → fin)"
  echo "- Trades (filtre > 17:00 UTC) : **$NB**"
  echo "- PnL total : **$PNL USDT**"
  echo
  echo "## Reference (hier, Ollama)"
  echo "- 8 trades, PnL -12,26 USDT"
  echo
  echo "## Details des trades"
  echo
  if [ -f /tmp/run4h_trades.csv ]; then
    column -s, -t /tmp/run4h_trades.csv 2>/dev/null | head -30 | tee -a "$REPORT" >> /dev/null
    cat /tmp/run4h_trades.csv >> "$REPORT"
  fi
} > "$REPORT"
echo "=== rapport ecrit: $REPORT ===" | tee -a "$LOG"

# 5) Appel vocal Cortana — message bref et naturel
MSG="Christophe, le run de quatre heures est terminé. $NB trades exécutés, "
if [ "$PNL" = "?" ]; then
  MSG="${MSG}le bilan est dans le rapport."
elif python3 -c "exit(0 if float('$PNL') >= 0 else 1)" 2>/dev/null; then
  MSG="${MSG}plus ${PNL} dollars de test. Le juge du hub a bien travaillé."
else
  MSG="${MSG}moins ${PNL#-} dollars de test."
fi
echo "=== $(date '+%H:%M:%S') APPELLE CORTANA ===" | tee -a "$LOG"
python3 Index_Maison/scripts/cortana_thermo.py alert "$MSG" 2>&1 | tail -3 | tee -a "$LOG"
echo "=== $(date '+%H:%M:%S') FIN DU SCRIPT ===" | tee -a "$LOG"
