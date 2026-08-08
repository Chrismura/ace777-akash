#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/rapatrie_B.log"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u) PHASE B ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

SRC="/Users/christophe/Documents/Obsidian_ACE777/Index_Maison"
# fallback workspace if gros vault incomplete
WS="/Users/christophe/ace777-test-day1/Index_Maison"
LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
DEST="$LIGHT/Index_Maison"

mkdir -p "$DEST"

copy_md_tree() {
  local from="$1"
  local to="$2"
  [[ -d "$from" ]] || return 0
  mkdir -p "$to"
  # find md files only, skip huge
  find "$from" -type f -name '*.md' -size -500k | while read -r f; do
    rel="${f#$from/}"
    mkdir -p "$to/$(dirname "$rel")"
    cp "$f" "$to/$rel"
    echo "CP $rel"
  done
}

# Prefer workspace (complete session) then overlay from gros vault
echo "--- from workspace ---"
copy_md_tree "$WS" "$DEST"
echo "--- from gros vault (si plus récent) ---"
if [[ -d "$SRC" ]]; then
  find "$SRC" -type f -name '*.md' -size -500k | while read -r f; do
    rel="${f#$SRC/}"
    mkdir -p "$DEST/$(dirname "$rel")"
    # copy if missing or source newer
    if [[ ! -f "$DEST/$rel" ]] || [[ "$f" -nt "$DEST/$rel" ]]; then
      cp "$f" "$DEST/$rel"
      echo "OV $rel"
    fi
  done
fi

# ensure plan at root
cp -f "$WS/00_PLAN_RAPATRIEMENT.md" "$LIGHT/00_PLAN_RAPATRIEMENT.md" 2>/dev/null || true

# AGORA update
python3 <<'PY'
from pathlib import Path
from datetime import datetime, timezone
light = Path.home()/"Documents"/"Obsidian_ACE777_LIGHT"
agora = light/"AGORA.md"
agora.write_text("""# Agora

Place commune (vault LIGHT stable).

## Liens
- [[00_PLAN_RAPATRIEMENT]] — plan rapatriement
- [[Index_Maison/01_TABLEAU_VIVANT]] — améliorations
- [[Index_Maison/Suivi_Info/COMPTES]] — comptes suivis
- [[Index_Maison/A_Mon_Attention/INDEX]] — à ton attention
- [[Swarm_Bus/09_MEMOIRE_COLLAB]] — journal collab
- [[Swarm_Bus/10_ATTENTION_VOCALE]] — résumé oral
- [[Swarm_Bus/00_LIRE_MOI]] — bus

## Rappel
Code vocal / lourds = hors vault. Mac Air OK si notes légères.
""", encoding="utf-8")
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | `Index_Maison/` | Phase B OK — Index Maison md rapatrié LIGHT |"
for mem in [light/"Swarm_Bus"/"09_MEMOIRE_COLLAB.md", light/"Index_Maison"/"MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "Phase B OK" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        mem.write_text(t.replace(m, m+"\n"+line, 1), encoding="utf-8")
print("AGORA+mem OK")
PY

echo "--- VERIFY ---"
du -sh "$LIGHT"
find "$LIGHT" -type f | wc -l
find "$DEST" -name '*.md' | wc -l
ls "$DEST"
ls "$DEST/Suivi_Info" 2>/dev/null || true
ls "$DEST/A_Mon_Attention" 2>/dev/null || true
ls "$DEST/Evaluations" 2>/dev/null | wc -l

# mark plan checkbox B mentally in a note
echo "DONE_B"
echo "Rouvre Obsidian LIGHT — reste 2-3 min sur AGORA."
