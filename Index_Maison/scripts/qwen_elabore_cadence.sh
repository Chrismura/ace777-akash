#!/bin/bash
# Cadence nocturne Qwen solo — 03:00, lance l'elaboration et journalise.
S=~/ace777-test-day1/Index_Maison/scripts
LOG=~/prise-ia/reports/QWEN_ELABORE.log
echo "== $(date -u +%Y-%m-%dT%H:%MZ) ==" >> "$LOG"
cd "$S" && python3 qwen_elabore.py >> "$LOG" 2>&1
echo "== fin ==" >> "$LOG"
