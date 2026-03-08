#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Profil test "plus d'entrees" (modere) sans modifier la base.
# - Levier scout: x5
# - Levier hunter: x5 -> x8 -> x13 (via le script enchaineur existant)
# - Seuils momentum abaisses + polling plus rapide

export BETA_MOMENTUM_THRESHOLD="${BETA_MOMENTUM_THRESHOLD:-0.35}"
export ALPHA_MOMENTUM_THRESHOLD="${ALPHA_MOMENTUM_THRESHOLD:-0.50}"
export BETA_POLL_SEC="${BETA_POLL_SEC:-0.03}"
export ALPHA_POLL_SEC="${ALPHA_POLL_SEC:-0.03}"
export BETA_STOP_LOSS_BPS="${BETA_STOP_LOSS_BPS:-12}"
export ALPHA_STOP_LOSS_BPS="${ALPHA_STOP_LOSS_BPS:-10}"

echo "=== PROFIL PLUS ENTREES (MODERE) ==="
echo "BETA_MOMENTUM_THRESHOLD=${BETA_MOMENTUM_THRESHOLD}"
echo "ALPHA_MOMENTUM_THRESHOLD=${ALPHA_MOMENTUM_THRESHOLD}"
echo "BETA_POLL_SEC=${BETA_POLL_SEC}"
echo "ALPHA_POLL_SEC=${ALPHA_POLL_SEC}"
echo "BETA_STOP_LOSS_BPS=${BETA_STOP_LOSS_BPS}"
echo "ALPHA_STOP_LOSS_BPS=${ALPHA_STOP_LOSS_BPS}"

bash ./launch_modele_14_v63_leviers_5_8_13.sh
