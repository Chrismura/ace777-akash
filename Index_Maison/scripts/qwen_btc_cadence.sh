#!/bin/bash
# Cadence analyse BTC Qwen — 2x/jour, journalise dans analyses/ (score_justesse).
S=~/ace777-test-day1/Index_Maison/scripts
LOG=~/prise-ia/reports/QWEN_BTC.log
echo "== $(date -u +%Y-%m-%dT%H:%MZ) ==" >> "$LOG"
cd "$S" && python3 qwen_btc.py >> "$LOG" 2>&1
echo "== fin ==" >> "$LOG"
