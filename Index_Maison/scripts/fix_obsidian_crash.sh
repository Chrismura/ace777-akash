#!/bin/bash
set -euo pipefail
MAIN="/Users/christophe/Documents/Obsidian_ACE777"
AV="$MAIN/Assistant_Vocal"
OB="$MAIN/.obsidian"
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/obsidian_fix.log"
exec > >(tee "$LOG") 2>&1

echo "=== $(date -u) fix Obsidian saute ==="
# Quit Obsidian
osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

echo "--- taille Assistant_Vocal ---"
du -sh "$AV" 2>&1 || true
du -sh "$AV/target" 2>&1 || true
find "$AV" -type f 2>/dev/null | wc -l

# Exclude heavy folder from Obsidian indexing
mkdir -p "$OB"
APPJSON="$OB/app.json"
python3 <<'PY'
import json
from pathlib import Path
p = Path("/Users/christophe/Documents/Obsidian_ACE777/.obsidian/app.json")
data = {}
if p.exists():
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        data = {}
# Obsidian uses userIgnoreFilters (list of patterns)
ign = data.get("userIgnoreFilters") or []
for pat in ["Assistant_Vocal/", "Assistant_Vocal", "_backup_vault_merge_*/", "*.lock", "**/target/", "**/node_modules/"]:
    if pat not in ign:
        ign.append(pat)
data["userIgnoreFilters"] = ign
# lighter startup
data["alwaysUpdateLinks"] = False
p.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("OK app.json ignore:", ign)
PY

# Move Rust build artifacts out of vault if present (keep source, drop target/)
if [[ -d "$AV/target" ]]; then
  BAK="$MAIN/_backup_vault_merge_obsidian_fix"
  mkdir -p "$BAK"
  mv "$AV/target" "$BAK/Assistant_Vocal_target_$(date -u +%Y%m%dT%H%MZ)"
  echo "OK target/ sorti du vault -> $BAK"
fi

# Clear Obsidian workspace cache that may reopen graph crashy
rm -f "$OB/workspace.json" "$OB/workspace-mobile.json" 2>/dev/null || true
# keep a minimal workspace without graph
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
          "state": { "file": "AGORA.md", "mode": "source" }
        }
      }
    ],
    "direction": "vertical"
  },
  "left": { "id": "left", "type": "split", "children": [], "direction": "horizontal", "collapsed": true },
  "right": { "id": "right", "type": "split", "children": [], "direction": "horizontal", "collapsed": true },
  "active": "md",
  "lastOpenFiles": ["AGORA.md"]
}
WS
echo "OK workspace -> AGORA only (pas de graph)"

# Clear electron cache (safe)
CACHE="$HOME/Library/Application Support/obsidian/Cache"
CODE="$HOME/Library/Application Support/obsidian/Code Cache"
rm -rf "$CACHE" "$CODE" 2>/dev/null || true
echo "OK cache Electron vidé"

# Note for user
cat > "$MAIN/00_SI_OBSIDIAN_SAUTE.md" <<'MD'
# Si Obsidian saute

Cause probable : le dossier `Assistant_Vocal/` contient un **projet Rust** (Cargo, target…) — trop lourd pour l’index / graph sur Mac 8 Go.

Déjà fait :
- `Assistant_Vocal/` exclu de l’index Obsidian
- `target/` sorti du vault (backup)
- démarrage sur `AGORA.md` sans graph
- cache vidé

À faire : rouvrir Obsidian. **Ne pas** ouvrir Graph View tant que ça n’est pas stable.
MD

echo "DONE_FIX"
