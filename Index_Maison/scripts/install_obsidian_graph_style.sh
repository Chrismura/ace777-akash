#!/usr/bin/env bash
# À lancer dans TON Terminal (Cursor n’a pas le droit d’écrire dans Documents/).
set -euo pipefail
VAULT="${OBSIDIAN_VAULT:-$HOME/Documents/Obsidian_ACE777}"
ROOT="$HOME/ace777-test-day1/Index_Maison"
OB="$ROOT/OUTBOX_OBSIDIAN"
CSS_SRC="$OB/obsidian-snippets/ace777-graph-galactique.css"

echo "=== FIX OBSIDIAN GRAPH (fond Argona) ==="
echo "VAULT=$VAULT"

[[ -d "$VAULT/.obsidian" ]] || { echo "FAIL: pas de .obsidian dans $VAULT"; exit 1; }
[[ -f "$CSS_SRC" ]] || { echo "FAIL: snippet manquant $CSS_SRC"; exit 1; }

mkdir -p "$VAULT/.obsidian/snippets" "$VAULT/graph_cerveau"

# 1) CSS snippet
cp -f "$CSS_SRC" "$VAULT/.obsidian/snippets/ace777-graph-galactique.css"
echo "OK snippet CSS copié"

# 2) Activer le snippet
python3 - <<PY
import json
from pathlib import Path
vault = Path("$VAULT")
app = vault / ".obsidian" / "appearance.json"
data = {}
if app.exists():
    try:
        data = json.loads(app.read_text())
    except Exception:
        data = {}
en = list(data.get("enabledCssSnippets") or [])
if "ace777-graph-galactique" not in en:
    en.append("ace777-graph-galactique")
data["enabledCssSnippets"] = en
# forcer thème sombre utile pour les couleurs graph
if "cssTheme" not in data:
    data.setdefault("theme", data.get("theme", "obsidian"))
app.write_text(json.dumps(data, indent=2) + "\n")
print("OK appearance.json → snippet ON")
print("enabledCssSnippets =", en)
PY

# 3) colorGroups familles
python3 - <<PY
import json
from pathlib import Path
vault = Path("$VAULT") / ".obsidian" / "graph.json"
fam = Path("$OB/obsidian-graph/graph.json.ace777-families")
groups = json.loads(fam.read_text())["colorGroups"]
if vault.exists():
    data = json.loads(vault.read_text())
    bak = vault.with_suffix(".json.bak-ace777")
    if not bak.exists():
        bak.write_text(vault.read_text())
else:
    data = {"collapse-filter": True, "search": "", "showTags": False, "showAttachments": False, "hideUnresolved": False, "showOrphans": True, "collapse-color-groups": False, "colorGroups": [], "collapse-display": False, "showArrow": False, "textFadeMultiplier": 0, "nodeSizeMultiplier": 1, "lineSizeMultiplier": 1, "collapse-forces": False, "centerStrength": 0.5, "repelStrength": 10, "linkStrength": 1, "linkDistance": 250, "scale": 1, "close": True}
data["colorGroups"] = groups
data["collapse-color-groups"] = False
vault.write_text(json.dumps(data, indent=2) + "\n")
print("OK graph.json colorGroups", len(groups))
PY

# 4) page cerveau (animation réelle) dans le vault
python3 "$ROOT/scripts/build_cerveau_graph.py"
cp -f "$ROOT/graph_cerveau/index.html" "$VAULT/graph_cerveau/index.html"
cp -f "$ROOT/graph_cerveau/data.js" "$VAULT/graph_cerveau/data.js"
cp -f "$OB/CERVEAU_GALACTIQUE.md" "$VAULT/CERVEAU_GALACTIQUE.md" 2>/dev/null || true

echo ""
echo "DONE."
echo "  1. Quitter Obsidian complètement (Cmd+Q)"
echo "  2. Relancer Obsidian"
echo "  3. Graphe global → fond noir/nébuleuse (plus gris plat)"
echo "  4. Animation type Argona :"
echo "     open $ROOT/graph_cerveau/index.html"
echo "     ou dans Obsidian : ouvrir graph_cerveau/index.html (aperçu navigateur)"
