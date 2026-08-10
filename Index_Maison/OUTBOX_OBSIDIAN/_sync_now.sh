#!/bin/bash
set -euo pipefail
VAULT="/Users/christophe/Documents/Obsidian_ACE777"
OB="/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"
mkdir -p "$VAULT/$(dirname "CONSOLE_GENERALE.md")" && cp "$OB/CONSOLE_GENERALE.md" "$VAULT/CONSOLE_GENERALE.md" && echo OK CONSOLE_GENERALE.md
mkdir -p "$VAULT/$(dirname "Index_Maison/CONSOLE_GENERALE.md")" && cp "$OB/Index_Maison/CONSOLE_GENERALE.md" "$VAULT/Index_Maison/CONSOLE_GENERALE.md" && echo OK Index_Maison/CONSOLE_GENERALE.md
mkdir -p "$VAULT/$(dirname "Cahier/Journal_2026-08-10.md")" && cp "$OB/Cahier/Journal_2026-08-10.md" "$VAULT/Cahier/Journal_2026-08-10.md" && echo OK Cahier/Journal_2026-08-10.md
mkdir -p "$VAULT/$(dirname "Index_Maison/Journal_2026-08-10.md")" && cp "$OB/Index_Maison/Journal_2026-08-10.md" "$VAULT/Index_Maison/Journal_2026-08-10.md" && echo OK Index_Maison/Journal_2026-08-10.md
mkdir -p "$VAULT/$(dirname "PLAN_DE_VOL.md")" && cp "$OB/PLAN_DE_VOL.md" "$VAULT/PLAN_DE_VOL.md" && echo OK PLAN_DE_VOL.md
mkdir -p "$VAULT/$(dirname "AUTO_PROCESSUS.md")" && cp "$OB/AUTO_PROCESSUS.md" "$VAULT/AUTO_PROCESSUS.md" && echo OK AUTO_PROCESSUS.md
echo SYNC_VIA_TERMINAL_DONE
