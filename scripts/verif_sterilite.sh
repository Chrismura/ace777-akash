#!/usr/bin/env bash
# Vérification binaire stérilité ACE777/NUAGE — exit 0 = GO | exit 1 = STOP
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Motifs PRÉCIS — éviter le bare "ace777" (matche le chemin du projet / preflight lui-même → faux NOK)
PATTERN='ace777_launch_v85|launch_vide_froid_4h_binance|launch_test_master_base_v8_6_fortress|watchdog_ace777|genesis_manifest\.txt|NUAGE_PROD_|MASTER_VORTEX_|tail -n 0 -F runs/|tail -F runs/\.NUAGE|/tmp/launch_vide_froid_4h_binance_NUAGE'

_left="$(pgrep -fl "$PATTERN" 2>/dev/null | grep -vi ollama | grep -vi 'verif_sterilite\|preflight_total\|GO_USINE_NUAGE\|GO_VORTEX' || true)"

if [ -n "$_left" ]; then
  echo "STERILE=NOK"
  echo "$_left"
  exit 1
fi

# Fichiers STOP doivent exister avant un run (pas après purge pré-run)
if [ "${1:-}" = "--pre-run" ]; then
  for f in STOP STOP_ALPHA STOP_BETA; do
    if [ ! -f "$f" ]; then
      echo "STERILE=NOK — manquant: $f (pose STOP avant run)"
      exit 1
    fi
  done
  if [ -f runs/master.pid ]; then
    echo "STERILE=NOK — runs/master.pid existe encore"
    exit 1
  fi
fi

echo "STERILE=OK"
exit 0
