#!/bin/bash
# backup_light_check.sh — contrôle backup LÉGER (réserve P5 + JUGE E1).
# - Présence des 5 dossiers hors zone : métadonnées uniquement (test -d), rapide.
# - Taille (du -sk) : ESPACÉE toutes les 6 h (fichier cache de timestamp).
# - Écrit DEUX fichiers bruts (loi du brut), fusionnés par le générateur :
#     system/backup_presence.json   (présence, à chaque run)
#     system/backup_sizes.json      (tailles, espacé 6 h)
# Usage : lancé par launchd (plist com.ace777.backup-check, StartInterval 1800).
set -u

BASE="${ACE777_BASE:-$HOME/ace777-test-day1/Index_Maison}"
SYSTEM_DIR="$BASE/system"
PRESENCE_FILE="$SYSTEM_DIR/backup_presence.json"
SIZE_FILE="$SYSTEM_DIR/backup_sizes.json"
CACHE_TS="$SYSTEM_DIR/.backup_size_ts"
SIX_HOURS=21600

mkdir -p "$SYSTEM_DIR"

DIRS=(
  "$HOME/mirofis"
  "$HOME/crypto-voice-assistant-core"
  "$HOME/ACE777_ARCHIVES_BRUTES_DONNEES"
  "$HOME/Assistant_Vocal_HORS_VAULT"
  "$HOME/Obsidian_BACKUPS_HORS_VAULT"
)
now=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# --- 1. Présence (à CHAQUE run — 30 min via plist) : métadonnées uniquement ---
{
  echo "{"
  echo "  \"generated_at\": \"$now\","
  echo "  \"present\": {"
  first=1
  for d in "${DIRS[@]}"; do
    name=$(basename "$d")
    if [ -d "$d" ]; then v="true"; else v="false"; fi
    if [ "$first" = "1" ]; then first=0; else echo "    ,"; fi
    printf '    "%s": %s' "$name" "$v"
  done
  echo ""
  echo "  }"
  echo "}"
} > "$PRESENCE_FILE"

# --- 2. Taille (ESPACÉE 6 h — jamais bloquant) ---
need_size=0
if [ ! -f "$CACHE_TS" ]; then
  need_size=1
else
  ts=$(cat "$CACHE_TS" 2>/dev/null || echo 0)
  now_epoch=$(date +%s)
  if [ $(( now_epoch - ts )) -ge $SIX_HOURS ]; then
    need_size=1
  fi
fi

if [ "$need_size" = "1" ]; then
  {
    echo "{"
    echo "  \"generated_at\": \"$now\","
    echo "  \"sizes_ko\": {"
    first=1
    for d in "${DIRS[@]}"; do
      name=$(basename "$d")
      if [ -d "$d" ]; then
        s=$(du -sk "$d" 2>/dev/null | awk '{print $1}')
        [ -z "$s" ] && s=0
      else
        s=0
      fi
      if [ "$first" = "1" ]; then first=0; else echo "    ,"; fi
      printf '    "%s": %s' "$name" "$s"
    done
    echo ""
    echo "  }"
    echo "}"
  } > "$SIZE_FILE"
  date +%s > "$CACHE_TS"
fi

exit 0
