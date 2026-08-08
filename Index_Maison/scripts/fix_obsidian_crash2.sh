#!/bin/bash
set -euo pipefail
MAIN="/Users/christophe/Documents/Obsidian_ACE777"
AV="$MAIN/Assistant_Vocal"
OB="$MAIN/.obsidian"
DEST="$HOME/Assistant_Vocal_HORS_VAULT"
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/obsidian_fix2.log"
exec > >(tee "$LOG") 2>&1

echo "=== $(date -u) fix2 black screen ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
killall "Obsidian Helper" 2>/dev/null || true
killall "Obsidian Helper (Renderer)" 2>/dev/null || true
killall "Obsidian Helper (GPU)" 2>/dev/null || true
sleep 2

echo "--- contenu vault (top) ---"
ls -la "$MAIN" | head -40
echo "--- sizes ---"
du -sh "$MAIN"/* 2>/dev/null | sort -h | tail -20

# 1) MOVE entire Assistant_Vocal OUT of vault (keep notes only stub)
if [[ -d "$AV" ]]; then
  mkdir -p "$DEST"
  # if dest empty-ish, move whole tree
  if [[ ! -d "$DEST/contenu" ]]; then
    mv "$AV" "$DEST/contenu"
    echo "OK Assistant_Vocal -> $DEST/contenu"
  else
    mv "$AV" "$DEST/contenu_bis_$(date -u +%Y%m%dT%H%MZ)"
    echo "OK Assistant_Vocal -> contenu_bis"
  fi
fi

# stub light folder in vault (markdown only, no code)
mkdir -p "$MAIN/Assistant_Vocal"
cat > "$MAIN/Assistant_Vocal/00_LIRE_MOI.md" << MD
# Assistant Vocal — stub

Le **code Rust** a été déplacé hors vault pour stabiliser Obsidian :
\`~/Assistant_Vocal_HORS_VAULT/contenu\`

(aussi : \`~/crypto-voice-assistant-core\`)

Agora : [[AGORA]]
MD

# 2) Disable ALL community plugins (safe mode equivalent)
mkdir -p "$OB"
python3 <<'PY'
import json
from pathlib import Path
ob = Path("/Users/christophe/Documents/Obsidian_ACE777/.obsidian")

# community-plugins.json = enabled list -> empty
(ob / "community-plugins.json").write_text("[]\n", encoding="utf-8")
print("OK community-plugins disabled")

# core-plugins: keep minimal
core = {
  "file-explorer": True,
  "global-search": True,
  "switcher": True,
  "graph": False,
  "backlink": False,
  "canvas": False,
  "outgoing-link": False,
  "tag-pane": False,
  "page-preview": False,
  "daily-notes": False,
  "templates": False,
  "note-composer": False,
  "command-palette": True,
  "slash-command": False,
  "editor-status": True,
  "bookmarks": False,
  "markdown-importer": False,
  "zk-prefixer": False,
  "random-note": False,
  "outline": False,
  "word-count": False,
  "slides": False,
  "audio-recorder": False,
  "workspaces": False,
  "file-recovery": True,
  "publish": False,
  "sync": False,
  "webviewer": False,
  "properties": False,
}
(ob / "core-plugins.json").write_text(json.dumps(core, indent=2), encoding="utf-8")
print("OK core graph/canvas/backlink OFF")

app = {}
ap = ob / "app.json"
if ap.exists():
  try:
    app = json.loads(ap.read_text(encoding="utf-8"))
  except Exception:
    app = {}
app["userIgnoreFilters"] = list(dict.fromkeys((app.get("userIgnoreFilters") or []) + [
  "Assistant_Vocal/", "_backup_vault_merge_*/", "**/target/", "**/node_modules/",
  "*.lock", "Cargo.lock", "*.bin", "*.wasm"
]))
app["alwaysUpdateLinks"] = False
app["promptDelete"] = True
# reduce thrash
app["showUnsupportedFiles"] = False
ap.write_text(json.dumps(app, indent=2), encoding="utf-8")
print("OK app.json")

# appearance: avoid fancy
(ob / "appearance.json").write_text(json.dumps({
  "cssTheme": "",
  "baseFontSize": 16,
  "enabledCssSnippets": []
}, indent=2), encoding="utf-8")
print("OK no theme/snippets")
PY

# 3) Minimal workspace - single markdown leaf, no graph
cat > "$OB/workspace.json" <<'WS'
{
  "main": {
    "id": "main",
    "type": "split",
    "children": [
      {
        "id": "md",
        "type": "leaf",
        "state": {
          "type": "markdown",
          "state": { "file": "AGORA.md", "mode": "source", "source": false }
        }
      }
    ],
    "direction": "vertical"
  },
  "left": {
    "id": "left",
    "type": "split",
    "children": [
      {
        "id": "fe",
        "type": "leaf",
        "state": { "type": "file-explorer", "state": {} }
      }
    ],
    "direction": "horizontal",
    "width": 240
  },
  "right": {
    "id": "right",
    "type": "split",
    "children": [],
    "direction": "horizontal",
    "collapsed": true,
    "width": 0
  },
  "active": "md",
  "lastOpenFiles": ["AGORA.md"]
}
WS
rm -f "$OB/workspace-mobile.json" "$OB/graph.json" "$OB/graph.json.bak" 2>/dev/null || true
# delete cached graph
rm -rf "$OB/graph.json" 2>/dev/null || true
find "$OB" -iname '*graph*' 2>/dev/null | head -20

# 4) Clear all electron caches again
rm -rf "$HOME/Library/Application Support/obsidian/Cache" \
       "$HOME/Library/Application Support/obsidian/Code Cache" \
       "$HOME/Library/Application Support/obsidian/GPUCache" \
       "$HOME/Library/Application Support/obsidian/DawnCache" \
       "$HOME/Library/Application Support/obsidian/ShaderCache" \
       "$HOME/Library/Application Support/obsidian/blob_storage" 2>/dev/null || true
echo "OK caches GPU/Shader/Code cleared"

# 5) Disable hardware acceleration via flag file if supported
# Obsidian/Electron: create argv.json or Preferences
PREF="$HOME/Library/Application Support/obsidian/Preferences"
python3 <<'PY'
import json
from pathlib import Path
p = Path.home() / "Library/Application Support/obsidian/Preferences"
try:
  data = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
except Exception:
  data = {}
# Chromium preference
data["hardware_acceleration_mode_previous"] = False
# some electron apps use this:
if "electron" not in data:
  pass
p.write_text(json.dumps(data), encoding="utf-8")
print("OK Preferences touched")
# argv for disable-gpu
argv = Path.home() / "Library/Application Support/obsidian/argv.json"
argv.write_text(json.dumps({
  "enabled": True,
  "argv": ["--disable-gpu", "--disable-gpu-compositing"]
}, indent=2), encoding="utf-8")
print("OK argv.json disable-gpu")
PY

# 6) vault size after
echo "--- sizes AFTER ---"
du -sh "$MAIN" 2>/dev/null || true
du -sh "$MAIN"/* 2>/dev/null | sort -h | tail -15
find "$MAIN" -type f 2>/dev/null | wc -l

# simplify AGORA to very light (no heavy embeds)
python3 <<'PY'
from pathlib import Path
p = Path("/Users/christophe/Documents/Obsidian_ACE777/AGORA.md")
p.write_text("""# Agora

Place commune — vault unique `Obsidian_ACE777`.

## Liens
- [[Swarm_Bus/09_MEMOIRE_COLLAB]] — journal
- [[Swarm_Bus/10_ATTENTION_VOCALE]] — oral
- [[Index_Maison/01_TABLEAU_VIVANT]] — améliorations
- [[Index_Maison/Suivi_Info/COMPTES]] — comptes suivis
- [[Swarm_Bus/00_LIRE_MOI]] — bus

## Note
Code vocal hors vault : `~/Assistant_Vocal_HORS_VAULT/`
Si écran noir : Settings → désactiver plugins ; ne pas ouvrir Graph.
""", encoding="utf-8")
print("OK AGORA allégé")
PY

echo "DONE_FIX2"
echo "Rouvre Obsidian MAINTENANT (une seule fenêtre)."
