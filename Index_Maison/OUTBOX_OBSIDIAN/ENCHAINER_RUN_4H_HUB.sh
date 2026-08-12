#!/usr/bin/env bash
# =============================================================================
# ENCHAINER_RUN_4H_HUB.sh — attend la fin du run de preuve (30 min),
# puis lance le run 4h GO_VORTEX_V2 (gate hub ACTIF, profil vortex_v2_collab).
# Créé 2026-08-12 — preuve bascule hub (llm_wind) → comparaison 4h équitable.
#
# Usage : ./ENCHAINER_RUN_4H_HUB.sh   (en détaché, ex. via start_new_session)
# =============================================================================
set -u
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

LOG="runs/ENCHAINER_4H_HUB.log"
echo "=== $(date '+%H:%M:%S') ENCHAÎNEUR : attente fin du run de preuve ===" | tee -a "$LOG"

# 1) Attendre la fin de TOUS les process du run actuel (poll 15s, max 45 min)
MAX_WAIT=2700   # 45 min max (le run 30 min doit finir à ~19:00)
elapsed=0
while [ "$elapsed" -lt "$MAX_WAIT" ]; do
  alive=$(pgrep -f 'GO_VORTEX_V2|launch_vortex_v2|launch_test_master_base_v8' | grep -v grep | wc -l | tr -d ' ')
  if [ "$alive" -eq 0 ]; then
    echo "=== $(date '+%H:%M:%S') run de preuve TERMINÉ — je lance le 4h ===" | tee -a "$LOG"
    break
  fi
  sleep 15
  elapsed=$((elapsed + 15))
done

if [ "$elapsed" -ge "$MAX_WAIT" ]; then
  echo "=== $(date '+%H:%M:%S') TIMEOUT 45min — les process tournent encore, j'arrête l'enchaîneur ===" | tee -a "$LOG"
  exit 1
fi

# 2) Hygiène : petits sleep pour laisser les derniers fichiers se fermer
sleep 10

# 3) Nettoyage kill-switches (sinon fortress ne part pas)
rm -f STOP STOP_ALPHA STOP_BETA runs/STOP_REASON.txt runs/LAST_STOP_REASON.txt

# 4) Vérifs rapides avant GO
echo "=== $(date '+%H:%M:%S') Vérifs pré-GO ===" | tee -a "$LOG"
curl -sS --connect-timeout 2 --max-time 5 http://127.0.0.1:11439/api/tags >/dev/null 2>&1 \
  && echo "PONT HUB OK ✓" | tee -a "$LOG" \
  || echo "PONT HUB KO ✗ — j'arrête (pas de run sans juge)" | tee -a "$LOG"

curl -s --max-time 5 http://127.0.0.1:11435/health >/dev/null 2>&1 \
  && echo "HUB OK ✓" | tee -a "$LOG" \
  || echo "HUB KO ✗" | tee -a "$LOG"

# 5) Lancement du run 4h (gate ON via GO_VORTEX_V2)
echo "=== $(date '+%H:%M:%S') LANCEMENT GO_VORTEX_V2 04:00:00 (gate hub ACTIF) ===" | tee -a "$LOG"
# Le script GO_VORTEX_V2 doit tourner en premier plan de CETTE session
# (il gère lui-même sa boucle de relance). On le laisse écrire son log.
caffeinate -dims ./GO_VORTEX_V2.sh 04:00:00 2>&1 | tee -a "$LOG"
echo "=== $(date '+%H:%M:%S') FIN du run 4h (code $?) ===" | tee -a "$LOG"
