#!/bin/bash
set -euo pipefail
SRC="/Users/christophe/ace777-test-day1/Index_Maison/00_PLAN_RAPATRIEMENT.md"
LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
cp "$SRC" "$LIGHT/00_PLAN_RAPATRIEMENT.md"
# AGORA link
if ! grep -q '00_PLAN_RAPATRIEMENT' "$LIGHT/AGORA.md" 2>/dev/null; then
  printf '\n- [[00_PLAN_RAPATRIEMENT]] — plan rapatriement\n' >> "$LIGHT/AGORA.md"
fi
TS=$(date -u +%Y-%m-%dT%H%MZ)
LINE="| $TS | Cursor | + | \`00_PLAN_RAPATRIEMENT.md\` | Plan rapatriement agora phases A–F |"
for MEM in "$LIGHT/Swarm_Bus/09_MEMOIRE_COLLAB.md" "$LIGHT/Index_Maison/MEMOIRE_COLLAB.md"; do
  if [[ -f "$MEM" ]] && ! grep -q 'Plan rapatriement agora' "$MEM"; then
    awk -v line="$LINE" '
      BEGIN{done=0}
      {print}
      /^\|----\|-----/{ if(!done){ print line; done=1 } }
    ' "$MEM" > "$MEM.tmp" && mv "$MEM.tmp" "$MEM"
  fi
done
ls -la "$LIGHT/00_PLAN_RAPATRIEMENT.md"
echo DONE_PLAN
