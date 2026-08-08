#!/bin/bash
set -euo pipefail
MAIN="/Users/christophe/Documents/Obsidian_ACE777"
OUT="$HOME/Obsidian_BACKUPS_HORS_VAULT"
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/obsidian_fix3.log"
exec > >(tee "$LOG") 2>&1

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

mkdir -p "$OUT"
# Move ALL heavy/backup junk OUT of vault
for d in \
  "_backup_vault_merge_obsidian_fix" \
  "_backup_vault_merge_20260728T2100Z" \
  "_backup_vault_merge_20260728T2101Z" \
  ".obsidian_corrompu" \
  ".smart-connections_STOPPED"
 do
  if [[ -e "$MAIN/$d" ]]; then
    mv "$MAIN/$d" "$OUT/$d"
    echo "OUT $d"
  fi
done

# Projet_1 might be heavy code too - check and exclude; if huge move
du -sh "$MAIN/Projet_1_Nuage_Actuel" 2>&1
# exclude in app.json
python3 <<'PY'
import json
from pathlib import Path
ap = Path("/Users/christophe/Documents/Obsidian_ACE777/.obsidian/app.json")
app = json.loads(ap.read_text()) if ap.exists() else {}
ign = app.get("userIgnoreFilters") or []
for pat in ["Projet_1_Nuage_Actuel/", "Projet_3_Goldman_Boy/", "Projet_4_Historique_Backups/", "_Cerveau/", "Hulk/", "Cahier/", "Prototypes/"]:
  if pat not in ign: ign.append(pat)
app["userIgnoreFilters"] = ign
ap.write_text(json.dumps(app, indent=2), encoding="utf-8")
print("ignore", ign)
PY

echo "--- AFTER ---"
du -sh "$MAIN" 2>&1
du -sh "$MAIN"/* "$MAIN"/.[!.]* 2>/dev/null | sort -h
find "$MAIN" -type f 2>/dev/null | wc -l
echo "DONE_FIX3"
