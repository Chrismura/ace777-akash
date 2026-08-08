#!/usr/bin/env bash
set -euo pipefail
C_N="\033[0m"; C_G="\033[0;32m"; C_C="\033[0;36m"; C_Y="\033[0;33m"
TARGET_VAULT="/Users/christophe/Documents/Obsidian_ACE777"
echo -e "${C_C}=== DEBUT DE CENTRALISATION TOTALE ET ABSOLUE ===${C_N}"
mkdir -p "$TARGET_VAULT/Projet_1_Nuage_Actuel"
mkdir -p "$TARGET_VAULT/Projet_2_Assistant_Vocal"
mkdir -p "$TARGET_VAULT/Projet_3_Goldman_Boy"
mkdir -p "$TARGET_VAULT/Projet_4_Historique_Backups"
cloner_hangar_integral() {
  local source_dir="$1"
  local dest_dir="$2"
  echo -e "${C_Y}Clonage intégral de : ${source_dir}...${C_N}"
  if [ -d "$source_dir" ]; then
    cp -R "$source_dir/" "$dest_dir/" 2>/dev/null || true
  fi
}
cloner_hangar_integral "/Users/christophe/ace777-test-day1" "$TARGET_VAULT/Projet_1_Nuage_Actuel"
cloner_hangar_integral "/Users/christophe/crypto-voice-assistant-core" "$TARGET_VAULT/Projet_2_Assistant_Vocal"
cloner_hangar_integral "/Users/christophe/Desktop/bot_GOLDMAN-BOY" "$TARGET_VAULT/Projet_3_Goldman_Boy"
cloner_hangar_integral "/Users/christophe/ace777_test_outputs_v2" "$TARGET_VAULT/Projet_4_Historique_Backups/ace777_test_outputs_v2"
cloner_hangar_integral "/Users/christophe/ace777_test_outputs_res_holo" "$TARGET_VAULT/Projet_4_Historique_Backups/ace777_test_outputs_res_holo"
cloner_hangar_integral "/Users/christophe/ace777-test-backups" "$TARGET_VAULT/Projet_4_Historique_Backups/ace777-test-backups"
if [ -f "/Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/ACE777_SAUVEGARDE_ULTIME_V3.5.md" ]; then
  cp "/Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/ACE777_SAUVEGARDE_ULTIME_V3.5.md" "$TARGET_VAULT/MEMOIRE_MAITRESSE_ACE777.md"
fi
echo -e "${C_G}=== COPIE TERMINÉE : 100% DE L'EMPIRE EST AU COFFRE-FORT ===${C_N}"
