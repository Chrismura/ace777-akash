#!/usr/bin/env bash
# Hygiène après arrêt ACE — TOUJOURS une ligne WHY_ARRET, puis nettoyage / vérif / commande
# Usage:
#   ./scripts/hygiene_apres_arret.sh
#   ./scripts/hygiene_apres_arret.sh --kill-orphans   # tue caffeinate/GO/timer orphelins
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

KILL_ORPHANS=0
[[ "${1:-}" == "--kill-orphans" ]] && KILL_ORPHANS=1

echo "=== HYGIENE APRES ARRET ACE ==="

# 1) Rapport erreurs → WHY_ARRET (obligatoire)
TAG="${STATE_TAG:-NUAGE_PROD_4H}"
export STATE_TAG="$TAG"
echo "--- rapport erreurs ($TAG) ---"
./scripts/rapport_erreurs_session.sh || true

if [ -f runs/LAST_STOP_REASON.txt ]; then
  echo
  echo ">>> $(cat runs/LAST_STOP_REASON.txt)"
  echo
else
  echo ">>> WHY_ARRET=missing_rapport — relancer ./scripts/rapport_erreurs_session.sh"
fi

# 2) Orphelins (optionnel)
if [ "$KILL_ORPHANS" -eq 1 ]; then
  echo "--- kill orphans ---"
  pkill -f 'caffeinate -dims ./GO_USINE_NUAGE' 2>/dev/null || true
  pkill -f 'caffeinate -dims env' 2>/dev/null || true
  pkill -f "File.write\('STOP_ALPHA'" 2>/dev/null || true
  pkill -f 'File.write..STOP_ALPHA' 2>/dev/null || true
  pkill -f 'ace777_launch_v85_nuage' 2>/dev/null || true
  pkill -f 'launch_test_master_base_v8_6_fortress' 2>/dev/null || true
  # timers ruby orphelins
  pkill -f "sleep .*File.write\('STOP_ALPHA'" 2>/dev/null || true
  sleep 1
fi

# 3) Cleanup léger + stérilité
./scripts/post_stop_cleanup.sh 2>/dev/null || true
if [ -x ./scripts/verif_sterilite.sh ]; then
  echo "--- verif sterilite ---"
  ./scripts/verif_sterilite.sh || true
fi

# 4) Commande run prête (Christophe colle — l'agent ne lance pas)
echo
echo "=== COMMANDE RUN (a coller SI tu veux relancer) ==="
cat <<'EOF'
cd /Users/christophe/ace777-test-day1

# 1) hygiène déjà faite — vérifier encore :
./scripts/verif_sterilite.sh

# 2) run 4h molette MIN 3.0 (même stack que cet aprem)
caffeinate -dims env \
  NUAGE_BIDIR_SIDES=1 \
  NUAGE_STORM_LATCH=1 \
  NUAGE_STORM_SCOUT_HOLD=1 \
  NUAGE_STORM_HUNTER=1 \
  NUAGE_MIN_ENTRY_TENSION=3.0 \
  ./GO_USINE_NUAGE.sh 04:00:00 NUAGE_PROD_4H
EOF

echo "=== HYGIENE OK — lire runs/RAPPORT_ERREURS_DERNIER.md ==="
