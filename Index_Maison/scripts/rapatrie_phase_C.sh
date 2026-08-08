#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/rapatrie_C.log"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u) PHASE C Swarm_Bus ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

SRC="/Users/christophe/Documents/Obsidian_ACE777/Swarm_Bus"
LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
DEST="$LIGHT/Swarm_Bus"
mkdir -p "$DEST" "$DEST/Punk"

# Core bus md files (not huge)
for f in \
  00_LIRE_MOI.md \
  01_ETAT_GLOBAL.md \
  02_ACE_SESSION.md \
  03_HULK_SCORE.md \
  03_HULK_SIGNAL.md \
  04_CMP_ACE8H_HULK.md \
  05_VEILLE_SECTEUR.md \
  06_DECISION.md \
  06_PARLIAMENT_VOTE.md \
  07_PUNK_VEILLE.md \
  08_LECONS.md \
  09_MEMOIRE_COLLAB.md \
  10_ATTENTION_VOCALE.md
 do
  if [[ -f "$SRC/$f" ]]; then
    # keep LIGHT version if newer for 09/10 (session), else take SRC if missing
    if [[ ! -f "$DEST/$f" ]]; then
      cp "$SRC/$f" "$DEST/$f"
      echo "CP $f"
    elif [[ "$f" != "09_MEMOIRE_COLLAB.md" && "$f" != "10_ATTENTION_VOCALE.md" && "$SRC/$f" -nt "$DEST/$f" ]]; then
      cp "$SRC/$f" "$DEST/$f"
      echo "OV $f"
    else
      echo "KEEP $f"
    fi
  else
    echo "MISS $f"
  fi
done

# Punk checks: last 20 md only by mtime
if [[ -d "$SRC/Punk" ]]; then
  ls -t "$SRC/Punk"/*.md 2>/dev/null | head -20 | while read -r f; do
    base=$(basename "$f")
    # skip if > 500k
    sz=$(wc -c < "$f" | tr -d ' ')
    if [[ "$sz" -gt 512000 ]]; then
      echo "SKIP big $base ($sz)"
      continue
    fi
    cp "$f" "$DEST/Punk/$base"
    echo "CP Punk/$base"
  done
fi

# Update 00_LIRE_MOI in Swarm if needed for 09/10
python3 <<'PY'
from pathlib import Path
from datetime import datetime, timezone
dest = Path.home()/"Documents"/"Obsidian_ACE777_LIGHT"/"Swarm_Bus"
lire = dest/"00_LIRE_MOI.md"
if lire.exists():
    t = lire.read_text(encoding="utf-8")
    if "09_MEMOIRE_COLLAB" not in t:
        t = t.rstrip() + "\n| [[09_MEMOIRE_COLLAB]] | Mémoire collab / Agora |\n| [[10_ATTENTION_VOCALE]] | Résumé oral Cortana |\n"
        lire.write_text(t, encoding="utf-8")
        print("patched 00_LIRE_MOI")
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | `Swarm_Bus/` | Phase C OK — Swarm_Bus md (+20 Punk max) |"
for mem in [dest/"09_MEMOIRE_COLLAB.md", Path.home()/"Documents"/"Obsidian_ACE777_LIGHT"/"Index_Maison"/"MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "Phase C OK" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        mem.write_text(t.replace(m, m+"\n"+line, 1), encoding="utf-8")
print("mem logged")
PY

echo "--- VERIFY ---"
du -sh "$LIGHT"
find "$LIGHT" -type f | wc -l
ls "$DEST"
ls "$DEST/Punk" 2>/dev/null | wc -l
echo "DONE_C"
