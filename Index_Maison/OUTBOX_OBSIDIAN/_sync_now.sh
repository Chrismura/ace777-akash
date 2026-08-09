#!/bin/bash
set -euo pipefail
VAULT="/Users/christophe/Documents/Obsidian_ACE777"
OB="/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"
mkdir -p "$VAULT/$(dirname "CONSOLE_GENERALE.md")" && cp "$OB/CONSOLE_GENERALE.md" "$VAULT/CONSOLE_GENERALE.md" && echo OK CONSOLE_GENERALE.md
mkdir -p "$VAULT/$(dirname "Index_Maison/CONSOLE_GENERALE.md")" && cp "$OB/Index_Maison/CONSOLE_GENERALE.md" "$VAULT/Index_Maison/CONSOLE_GENERALE.md" && echo OK Index_Maison/CONSOLE_GENERALE.md
mkdir -p "$VAULT/$(dirname "Cahier/Journal_2026-08-08.md")" && cp "$OB/Cahier/Journal_2026-08-08.md" "$VAULT/Cahier/Journal_2026-08-08.md" && echo OK Cahier/Journal_2026-08-08.md
if [ -f "$OB/Index_Maison/Journal_2026-08-08.md" ]; then mkdir -p "$VAULT/Index_Maison" && cp "$OB/Index_Maison/Journal_2026-08-08.md" "$VAULT/Index_Maison/Journal_2026-08-08.md" && echo OK Index_Maison/Journal_2026-08-08.md; fi
mkdir -p "$VAULT/$(dirname "PLAN_DE_VOL.md")" && cp "$OB/PLAN_DE_VOL.md" "$VAULT/PLAN_DE_VOL.md" && echo OK PLAN_DE_VOL.md
mkdir -p "$VAULT/$(dirname "AUTO_PROCESSUS.md")" && cp "$OB/AUTO_PROCESSUS.md" "$VAULT/AUTO_PROCESSUS.md" && echo OK AUTO_PROCESSUS.md
# --- 08/08 19:05Z : A_Mon_Attention + MEMOIRE_COLLAB ne remontaient JAMAIS ---
# (constat « Obsidian ne bouge pas » : dossier vault figé au 07/08)
mkdir -p "$VAULT/A_Mon_Attention" && cp -f "$OB/A_Mon_Attention/"*.md "$VAULT/A_Mon_Attention/" && echo OK A_Mon_Attention/
mkdir -p "$VAULT/Index_Maison/A_Mon_Attention" && cp -f "$OB/A_Mon_Attention/"*.md "$VAULT/Index_Maison/A_Mon_Attention/" && echo OK Index_Maison/A_Mon_Attention/
# MEMOIRE_COLLAB : le vault est la source de verite (67 Ko), le miroir OUTBOX
# (12 Ko) ne doit JAMAIS l'ecraser — aucune copie OUTBOX->vault ici.
# --- 09/08 : AUTO_EVOL/IDEES.md (Qwen-elabore ecrit ICI) ne remontait JAMAIS ---
mkdir -p "$VAULT/AUTO_EVOL" && cp -f "$OB/AUTO_EVOL/IDEES.md" "$VAULT/AUTO_EVOL/IDEES.md" && echo OK AUTO_EVOL/IDEES.md
echo SYNC_VIA_TERMINAL_DONE
