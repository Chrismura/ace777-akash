#!/bin/bash
# Sync OUTBOX → vault Obsidian_ACE777 (lancer depuis Terminal si TCC bloque Cursor)
set -euo pipefail
VAULT="/Users/christophe/Documents/Obsidian_ACE777"
OB="/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN"
SRC="/Users/christophe/ace777-test-day1/Index_Maison"

mkdir -p "$VAULT" "$VAULT/Index_Maison" "$VAULT/Cahier" "$VAULT/A_Mon_Attention" \
  "$VAULT/cockpit" "$VAULT/maquettes" "$VAULT/Swarm_Bus"

copy() {
  local rel="$1"
  local from=""
  if [ -f "$OB/$rel" ]; then from="$OB/$rel"
  elif [ -f "$SRC/$rel" ]; then from="$SRC/$rel"
  else echo "SKIP missing $rel"; return 0
  fi
  mkdir -p "$VAULT/$(dirname "$rel")"
  cp "$from" "$VAULT/$rel"
  # miroir Index_Maison/ si pas déjà sous ce préfixe
  case "$rel" in
    Index_Maison/*) ;;
    *)
      mkdir -p "$VAULT/Index_Maison/$(dirname "$rel")"
      cp "$from" "$VAULT/Index_Maison/$rel"
      ;;
  esac
  echo "OK $rel"
}

# Canons fréquents
for f in \
  INDEX_COMMANDES.md \
  COCKPIT_LOOK_FIGE.md \
  OSSATURE_INDEX.md \
  CONSOLE_GENERALE.md \
  PLAN_DE_VOL.md \
  AUTO_PROCESSUS.md \
  MEMOIRE_COLLAB.md \
  01_TABLEAU_VIVANT.md \
  THERMO_DERNIER.md \
  SOUS_L_OEIL.md \
  AGORA.md
do
  copy "$f"
done

# Journal du jour (si présent)
TODAY=$(date +%Y-%m-%d)
[ -f "$OB/Cahier/Journal_${TODAY}.md" ] && copy "Cahier/Journal_${TODAY}.md"
[ -f "$SRC/Cahier/Journal_${TODAY}.md" ] && copy "Cahier/Journal_${TODAY}.md"

# Cockpit UI
copy "cockpit/index.html"
[ -f "$SRC/maquettes/ace777-cockpit-maquette-arcade-radar.png" ] && \
  cp "$SRC/maquettes/ace777-cockpit-maquette-arcade-radar.png" "$VAULT/maquettes/" && \
  cp "$SRC/maquettes/ace777-cockpit-maquette-arcade-radar.png" "$VAULT/Index_Maison/maquettes/" 2>/dev/null || true

# Attention récente cockpit
[ -f "$SRC/A_Mon_Attention/2026-07-29_cockpit_arcade.md" ] && \
  cp "$SRC/A_Mon_Attention/2026-07-29_cockpit_arcade.md" "$VAULT/A_Mon_Attention/" && \
  echo "OK A_Mon_Attention/2026-07-29_cockpit_arcade.md"

# Swarm bus mémoire
[ -f "$OB/Swarm_Bus/09_MEMOIRE_COLLAB.md" ] && \
  cp "$OB/Swarm_Bus/09_MEMOIRE_COLLAB.md" "$VAULT/Swarm_Bus/09_MEMOIRE_COLLAB.md" && \
  echo "OK Swarm_Bus/09_MEMOIRE_COLLAB.md"

echo SYNC_VIA_TERMINAL_DONE
