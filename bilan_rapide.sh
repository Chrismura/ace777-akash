#!/usr/bin/env bash
# =============================================================================
# ACE777 — BILAN RAPIDE du dernier run
#
# Usage:
#   ./bilan_rapide.sh                # dernier run (toutes les sessions du jour)
#   ./bilan_rapide.sh 2026-08-18     # run d'une date précise
#
# Affiche en 1 commande : PnL, trades, wins/losses, raisons de sortie,
# fluid (le parasite), SKIP, santé du compte, ordres orphelins.
# Lecture seule — ne touche à rien.
# =============================================================================
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

DATE_FILTER="${1:-$(date +%Y-%m-%d)}"
BETA_CSV="runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"
ALPHA_CSV="runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"

echo "═══════════════════════════════════════════════════════"
echo "  BILAN RAPIDE — date: $DATE_FILTER"
echo "═══════════════════════════════════════════════════════"

# --- Fonction analyse d'un CSV ----------------------------------------------
analyse() {
  local csv="$1" nom="$2"
  [ -f "$csv" ] || { echo "❌ $nom : CSV manquant ($csv)"; return; }
  awk -F',' -v d="$DATE_FILTER" -v n="$nom" '
    NR>1 && index($1, d) == 1 {
      tot++
      if ($4 == "FILLED") {
        filled++
        pnl += $9
        if ($9 > 0) win++
        else if ($9 < 0) loss++
        else zero++
        reason[$10]++
      } else if ($4 == "SKIPPED") {
        skip++
      }
    }
    END {
      printf "  %s\n", n
      printf "    PnL      : %+8.2f $\n", pnl
      printf "    Trades   : %d (win=%d loss=%d zero=%d)\n", filled, win, loss, zero
      printf "    SKIP     : %d / %d cycles\n", skip, tot
      if (filled > 0) {
        printf "    Sorties  : "
        first = 1
        for (r in reason) { if (!first) printf ", "; printf "%s(%d)", r, reason[r]; first = 0 }
        printf "\n"
      }
    }' "$csv"
}

analyse "$BETA_CSV" "BETA (x5)"
echo ""
analyse "$ALPHA_CSV" "ALPHA (x13)"

echo ""
echo "───────────────────────────────────────────────────────"
echo "  SANTÉ (dernier run de la journée)"
echo "───────────────────────────────────────────────────────"

# Fin de run propre ?
EXIT_DUMP="runs/EXIT_DUMP.log"
if [ -f "$EXIT_DUMP" ]; then
  LAST=$(grep "$DATE_FILTER" "$EXIT_DUMP" | tail -2)
  echo "$LAST" | sed 's/^/  /'
fi

# STOP files (freins de relance présents = run terminé proprement)
STOPS=0
for f in STOP STOP_ALPHA STOP_BETA; do [ -f "$f" ] && STOPS=$((STOPS+1)); done
[ "$STOPS" -gt 0 ] && echo "  ✅ Run terminé (STOP files présents)" || echo "  ⚠️  Pas de STOP files — vérifier qu'aucun run ne tourne"

# Process actifs ?
PROCS=$(ps aux | grep -E "bash -s|GO_VORTEX|launch_vortex" | grep -v grep | wc -l | tr -d ' ')
[ "$PROCS" -eq 0 ] && echo "  ✅ Aucun process de run actif" || echo "  ⚠️  $PROCS process de run encore actifs !"

echo ""
echo "  💡 Rappel : le champion est scellé (md5 = $(cat Index_Maison/strategie/CHAMPION_ACTIF 2>/dev/null || echo '?'))."
echo "═══════════════════════════════════════════════════════"
