#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/obsidian_fix4.log"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u) fix4 minimal vault ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
killall "Obsidian Helper" 2>/dev/null || true
killall "Obsidian Helper (Renderer)" 2>/dev/null || true
killall "Obsidian Helper (GPU)" 2>/dev/null || true
sleep 2

MAIN="/Users/christophe/Documents/Obsidian_ACE777"
LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
SUP="$HOME/Library/Application Support/obsidian"
TS=$(date -u +%Y%m%dT%H%MZ)
BAK="$HOME/Obsidian_BACKUPS_HORS_VAULT/app_support_$TS"
mkdir -p "$BAK" "$LIGHT"

# 1) Backup + REMOVE broken electron flags
for f in argv.json Preferences; do
  if [[ -f "$SUP/$f" ]]; then
    cp "$SUP/$f" "$BAK/$f"
    echo "bak $f"
  fi
done
# REMOVE argv.json entirely (wrong format can black-screen)
rm -f "$SUP/argv.json"
echo "OK argv.json removed"

# Reset Preferences to empty object (don't force GPU flags)
echo '{}' > "$SUP/Preferences"
echo "OK Preferences reset"

# Clear ALL caches again
rm -rf "$SUP/Cache" "$SUP/Code Cache" "$SUP/GPUCache" "$SUP/DawnCache" \
       "$SUP/ShaderCache" "$SUP/blob_storage" "$SUP/Session Storage" \
       "$SUP/Local Storage" 2>/dev/null || true
echo "OK all caches cleared"

# 2) Backup and REPLACE vault .obsidian with brand new minimal
if [[ -d "$MAIN/.obsidian" ]]; then
  mv "$MAIN/.obsidian" "$BAK/dot_obsidian_main"
  echo "OK old .obsidian quarantined"
fi
mkdir -p "$MAIN/.obsidian"
# absolute minimal config - no workspace json (Obsidian creates fresh)
echo '[]' > "$MAIN/.obsidian/community-plugins.json"
cat > "$MAIN/.obsidian/core-plugins.json" <<'JSON'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": false,
  "backlink": false,
  "canvas": false,
  "outgoing-link": false,
  "tag-pane": false,
  "page-preview": false,
  "daily-notes": false,
  "templates": false,
  "note-composer": false,
  "command-palette": true,
  "editor-status": true,
  "bookmarks": false,
  "outline": false,
  "word-count": false,
  "file-recovery": true,
  "sync": false,
  "webviewer": false
}
JSON
cat > "$MAIN/.obsidian/app.json" <<'JSON'
{
  "userIgnoreFilters": [
    "Projet_1_Nuage_Actuel/",
    "Projet_3_Goldman_Boy/",
    "Projet_4_Historique_Backups/",
    "Assistant_Vocal/",
    "_Cerveau/",
    "Hulk/",
    "Cahier/",
    "Prototypes/",
    "**/target/",
    "**/node_modules/"
  ],
  "alwaysUpdateLinks": false,
  "showUnsupportedFiles": false
}
JSON
# NO workspace.json — let Obsidian create clean
# NO appearance theme
echo "OK fresh .obsidian minimal"

# 3) Create LIGHT vault (only 4 notes) as fallback test
rm -rf "$LIGHT"
mkdir -p "$LIGHT/.obsidian" "$LIGHT/Swarm_Bus" "$LIGHT/Index_Maison"
cp "$MAIN/AGORA.md" "$LIGHT/AGORA.md" 2>/dev/null || true
# copy essential md only if exist
cp "$MAIN/Swarm_Bus/00_LIRE_MOI.md" "$LIGHT/Swarm_Bus/" 2>/dev/null || true
cp "$MAIN/Swarm_Bus/09_MEMOIRE_COLLAB.md" "$LIGHT/Swarm_Bus/" 2>/dev/null || true
cp "$MAIN/Swarm_Bus/10_ATTENTION_VOCALE.md" "$LIGHT/Swarm_Bus/" 2>/dev/null || true
cp "$MAIN/Index_Maison/01_TABLEAU_VIVANT.md" "$LIGHT/Index_Maison/" 2>/dev/null || true
cp "$MAIN/Index_Maison/MEMOIRE_COLLAB.md" "$LIGHT/Index_Maison/" 2>/dev/null || true
echo '[]' > "$LIGHT/.obsidian/community-plugins.json"
cp "$MAIN/.obsidian/core-plugins.json" "$LIGHT/.obsidian/"
cp "$MAIN/.obsidian/app.json" "$LIGHT/.obsidian/"
cat > "$LIGHT/AGORA.md" <<'MD'
# Agora (vault LIGHT)

Si tu lis ceci sans écran noir → Obsidian OK, le gros vault avait un poison.

Liens :
- [[Swarm_Bus/09_MEMOIRE_COLLAB]]
- [[Index_Maison/01_TABLEAU_VIVANT]]
MD
echo "OK LIGHT vault at $LIGHT"
find "$LIGHT" -type f | wc -l
du -sh "$LIGHT"

# 4) Point Obsidian to LIGHT vault ONLY for test
python3 <<'PY'
import json
from pathlib import Path
from datetime import datetime
p = Path.home() / "Library/Application Support/obsidian/obsidian.json"
bak = p.with_suffix(".json.bak_before_light")
bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
light = str(Path.home() / "Documents/Obsidian_ACE777_LIGHT")
main = "/Users/christophe/Documents/Obsidian_ACE777"
ts = int(datetime.now().timestamp() * 1000)
data = {
  "vaults": {
    "ace777light": {"path": light, "ts": ts, "open": True},
    "d0e81da3ab6046e0": {"path": main, "ts": ts - 1000, "open": False},
  }
}
p.write_text(json.dumps(data), encoding="utf-8")
print("OK obsidian.json -> LIGHT open, main closed")
print(p.read_text())
PY

# latest crash hint
CRASH=$(ls -t "$HOME/Library/Logs/DiagnosticReports"/Obsidian*.ips 2>/dev/null | head -1 || true)
echo "latest crash: $CRASH"
if [[ -n "$CRASH" ]]; then
  grep -E '"exception"|"termination"|EXC_|signal' "$CRASH" | head -10
fi

echo "DONE_FIX4"
echo ""
echo ">>> Ouvre Obsidian : il doit charger Obsidian_ACE777_LIGHT (petit)."
echo ">>> Si STABLE : le problème était le gros vault."
echo ">>> Si SAUTE encore : Obsidian app / GPU Mac — on réinstalle ou on ouvre en safe mode."
