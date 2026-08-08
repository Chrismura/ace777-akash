#!/usr/bin/env bash
# Enchaîne Pack B dès que Pack A (VALIDATION) est terminé.
# Lancer hors Cursor : nohup / Terminal.
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
LOGA="runs/VALIDATION_VOIE_A_PACK_A_LAUNCH.log"
LOGCHAIN="runs/VALIDATION_VOIE_A_CHAIN.log"
mkdir -p runs

log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" | tee -a "$LOGCHAIN"; }

log "CHAIN: attente fin Pack A…"

# Vivant tant que caffeinate/GO_VALIDATION Pack A ou lanceur A tourne
while pgrep -f 'GO_VALIDATION_VOIE_A.sh A' >/dev/null 2>&1 \
   || pgrep -f '_launch_validation_voie_a_A.sh' >/dev/null 2>&1; do
  sleep 30
done

# Si EXIT déjà dans le log A, OK ; sinon attendre un peu
if ! grep -q 'EXIT:' "$LOGA" 2>/dev/null; then
  log "CHAIN: process A disparu, pause 15s…"
  sleep 15
fi

log "CHAIN: Pack A terminé → hygiene + Pack B"
bash scripts/hygiene_mac_ram.sh >>"$LOGCHAIN" 2>&1 || true
sleep 3
rm -f STOP STOP_ALPHA STOP_BETA

# Relance Pack B via Terminal (même pattern que A)
osascript <<'APPLESCRIPT'
tell application "Terminal"
  activate
  do script "cd /Users/christophe/ace777-test-day1 && rm -f STOP STOP_ALPHA STOP_BETA && echo '=== VALIDATION VOIE A — PACK B (témoin) 4h ===' && caffeinate -dims ./GO_VALIDATION_VOIE_A.sh B 04:00:00 2>&1 | tee -a runs/VALIDATION_VOIE_A_PACK_B_LAUNCH.log; echo EXIT:$? | tee -a runs/VALIDATION_VOIE_A_PACK_B_LAUNCH.log"
end tell
APPLESCRIPT

log "CHAIN: Pack B lancé (onglet Terminal). Fin prévue ~+4h."
echo "OK" > runs/VALIDATION_VOIE_A_CHAIN_B_LAUNCHED.flag
