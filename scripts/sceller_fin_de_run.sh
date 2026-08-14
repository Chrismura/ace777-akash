#!/usr/bin/env bash
# SCELLER les CSV du run MASTER_VORTEX_V2_COLLAB_4H dès que le run se termine
# (fin de durée ~20:24Z OU bots morts). À lancer détaché :
#   nohup bash scripts/sceller_fin_de_run.sh > /tmp/sceller_fin_run.log 2>&1 &
# Attend passivement ; ne modifie RIEN pendant le run.

set -uo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
tag="MASTER_VORTEX_V2_COLLAB_4H"

echo "[$(date -u +%FT%TZ)] Scelleur de fin de run armé pour ${tag} (ALPHA + BETA)"

# Boucle d'attente : tant qu'un bash -s du run tourne, on attend.
while pgrep -f 'bash -s' >/dev/null 2>&1; do
  sleep 30
done

# Petite marge pour laisser GO_VORTEX finir d'écrire (process_exit, derniers csv)
sleep 10

echo "[$(date -u +%FT%TZ)] Run terminé — scellement des CSV"
./scripts/sceller_test.sh "$tag" ALPHA_X13_BURST13 >> /tmp/sceller_fin_run.log 2>&1
echo "[$(date -u +%FT%TZ)] ALPHA scellé rc=$?"
./scripts/sceller_test.sh "$tag" BETA_X5 >> /tmp/sceller_fin_run.log 2>&1
echo "[$(date -u +%FT%TZ)] BETA scellé rc=$?"

echo "[$(date -u +%FT%TZ)] Vérification croisée :"
./scripts/verifier_test.sh "$(ls -t runs/SCELLE/*_ALPHA_X13_BURST13_*.SIGNATURE.txt | head -1)" >> /tmp/sceller_fin_run.log 2>&1
./scripts/verifier_test.sh "$(ls -t runs/SCELLE/*_BETA_X5_*.SIGNATURE.txt | head -1)" >> /tmp/sceller_fin_run.log 2>&1
echo "[$(date -u +%FT%TZ)] SCELLEMENT TERMINÉ — voir /tmp/sceller_fin_run.log"
