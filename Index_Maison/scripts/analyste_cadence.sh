#!/usr/bin/env bash
# analyste_cadence.sh — le chief parle 2x/jour (GO plomberie 07/08)
# Indices clés : radar (climat global), funding (levier), fearGreed (sentiment).
set -uo pipefail
LOG=/tmp/analyste_cadence.log
echo "=== $(date -u +%FT%TZ) ===" >> "$LOG"
cd ~/ace777-test-day1/Index_Maison/scripts || exit 1
for indice in radar funding fearGreed; do
  echo "-- $indice" >> "$LOG"
  python3 cortana_analyse.py "$indice" >> "$LOG" 2>&1 || echo "[$indice] ECHEC" >> "$LOG"
done
