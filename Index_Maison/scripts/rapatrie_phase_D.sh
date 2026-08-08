#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/rapatrie_D.log"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u) PHASE D notes filtrées ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

MAIN="/Users/christophe/Documents/Obsidian_ACE777"
LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
MAX=512000  # 500 KiB

copy_filtered() {
  local name="$1"
  local from="$MAIN/$name"
  local to="$LIGHT/$name"
  [[ -d "$from" ]] || { echo "SKIP no dir $name"; return 0; }
  mkdir -p "$to"
  local n=0
  find "$from" -type f -name '*.md' -size -500k 2>/dev/null | while read -r f; do
    rel="${f#$from/}"
    # skip obvious junk paths
    case "$rel" in
      *target/*|*.git/*|*node_modules/*) continue ;;
    esac
    mkdir -p "$to/$(dirname "$rel")"
    cp "$f" "$to/$rel"
    n=$((n+1))
    echo "CP $name/$rel"
  done
}

# Root single md files
for f in ACE777-Constitution.md Welcome.md 00_SI_OBSIDIAN_SAUTE.md; do
  if [[ -f "$MAIN/$f" ]]; then
    sz=$(wc -c < "$MAIN/$f" | tr -d ' ')
    if [[ "$sz" -le "$MAX" ]]; then
      cp "$MAIN/$f" "$LIGHT/$f"
      echo "CP root/$f"
    fi
  fi
done

copy_filtered "Cahier"
copy_filtered "Hulk"
copy_filtered "Veille_secteur"

# Assistant_Vocal stub already exists — ensure only md stub
mkdir -p "$LIGHT/Assistant_Vocal"
cat > "$LIGHT/Assistant_Vocal/00_LIRE_MOI.md" <<'MD'
# Assistant Vocal

Code hors vault : `~/Assistant_Vocal_HORS_VAULT/` et `~/crypto-voice-assistant-core/`.
MD

python3 <<'PY'
from pathlib import Path
from datetime import datetime, timezone
light = Path.home()/"Documents"/"Obsidian_ACE777_LIGHT"
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | `Cahier+Hulk+Veille` | Phase D OK — notes md filtrées (<500Ko) |"
for mem in [light/"Swarm_Bus"/"09_MEMOIRE_COLLAB.md", light/"Index_Maison"/"MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "Phase D OK" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        mem.write_text(t.replace(m, m+"\n"+line, 1), encoding="utf-8")
# update plan checkmarks lightly in AGORA
agora = light/"AGORA.md"
if agora.exists():
    a = agora.read_text(encoding="utf-8")
    if "Phases A–D" not in a:
        a = a.rstrip() + "\n\nPhases A–D faites. Prochaine : [[00_PLAN_RAPATRIEMENT|GO E]] un seul nom de coffre.\n"
        agora.write_text(a, encoding="utf-8")
print("mem OK")
PY

echo "--- VERIFY ---"
du -sh "$LIGHT"
find "$LIGHT" -type f | wc -l
find "$LIGHT" -name '*.md' | wc -l
# warn if over 5MB
SIZE_K=$(du -sk "$LIGHT" | awk '{print $1}')
echo "size_kb=$SIZE_K"
if [[ "$SIZE_K" -gt 5120 ]]; then
  echo "WARN vault > 5Mo — surveiller"
fi
echo "DONE_D"
