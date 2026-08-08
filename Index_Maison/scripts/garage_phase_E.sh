#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/garage_E.log"
exec > >(tee "$LOG") 2>&1
echo "=== $(date -u) GARAGE Phase E ==="

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

LIGHT="$HOME/Documents/Obsidian_ACE777_LIGHT"
OLD="$HOME/Documents/Obsidian_ACE777"
STABLE="$HOME/Documents/Obsidian_ACE777_STABLE"
HORS="$HOME/Obsidian_BACKUPS_HORS_VAULT"
mkdir -p "$HORS"

# Resolve current light/stable source
SRC=""
if [[ -d "$LIGHT" ]]; then SRC="$LIGHT"; fi
if [[ -d "$STABLE" ]]; then SRC="$STABLE"; fi
if [[ -z "$SRC" ]]; then echo "FAIL no LIGHT/STABLE"; exit 1; fi
echo "SRC=$SRC"

# Archive OLD heavy vault if it exists and is different from SRC
if [[ -d "$OLD" ]]; then
  OLD_R=$(cd "$OLD" && pwd)
  SRC_R=$(cd "$SRC" && pwd)
  if [[ "$OLD_R" != "$SRC_R" ]]; then
    ARCH="$HORS/Obsidian_ACE777_ARCHIVE_LOURD_$(date -u +%Y%m%dT%H%MZ)"
    mv "$OLD" "$ARCH"
    echo "OK ancien gros -> $ARCH"
  fi
fi

# Final name Documents/Obsidian_ACE777
FINAL="$HOME/Documents/Obsidian_ACE777"
if [[ ! -e "$FINAL" ]]; then
  mv "$SRC" "$FINAL"
  echo "OK $SRC -> Obsidian_ACE777"
elif [[ "$(cd "$FINAL" && pwd)" != "$(cd "$SRC" && pwd)" ]]; then
  echo "WARN FINAL exists and differs from SRC — keep FINAL, merge missing md from SRC"
  rsync -a --ignore-existing --include='*/' --include='*.md' --exclude='*' "$SRC/" "$FINAL/" || true
else
  echo "OK FINAL already = vault"
fi
VAULT="$FINAL"

python3 <<PY
import json
from pathlib import Path
from datetime import datetime, timezone
vault = Path("$VAULT").resolve()
p = Path.home() / "Library/Application Support/obsidian/obsidian.json"
p.with_suffix(".json.bak_garage_E").write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
ts = int(datetime.now().timestamp() * 1000)
p.write_text(json.dumps({"vaults": {"ace777": {"path": str(vault), "ts": ts, "open": True}}}), encoding="utf-8")
print("obsidian.json", vault)

(vault / "OU_EST_QUOI.md").write_text(f"""# Où est quoi — le garage

Mis à jour : {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%MZ')}

## Dans Obsidian (oui)
Notes, décisions, agora, Index, Swarm (md), Cahier, coutumes.
**Coffre unique :** `{vault}`

| Note | Rôle |
|------|------|
| [[AGORA]] | Entrée |
| [[COUTUMES_AGORA]] | Règles |
| [[OU_EST_QUOI]] | Cette carte |
| [[00_PLAN_RAPATRIEMENT]] | Plan |
| [[Swarm_Bus/09_MEMOIRE_COLLAB]] | Journal |
| [[Index_Maison/01_TABLEAU_VIVANT]] | Améliorations |

## Hors Obsidian (non — volontaire)
| Quoi | Où |
|------|-----|
| Code vocal | `~/crypto-voice-assistant-core/` · `~/Assistant_Vocal_HORS_VAULT/` |
| Archives lourdes | `~/Obsidian_BACKUPS_HORS_VAULT/` |
| ACE / Hulk + runs | `~/ace777-test-day1/` |
| `.env` / `target/` | hors coffre |

## Pourquoi pas tout dans Obsidian ?
Obsidian = notes. Code + builds = Go → crash sur 8 Go. Garage = léger ici, outils à côté.
""", encoding="utf-8")

(vault / "AGORA.md").write_text("""# Agora

**Coffre unique** — notes / collab seulement.

## Lire d’abord
- [[COUTUMES_AGORA]]
- [[OU_EST_QUOI]]
- [[00_PLAN_RAPATRIEMENT]]

## Travail
- [[Index_Maison/01_TABLEAU_VIVANT]]
- [[Index_Maison/Suivi_Info/COMPTES]]
- [[Index_Maison/A_Mon_Attention/INDEX]]
- [[Swarm_Bus/09_MEMOIRE_COLLAB]]
- [[Cahier/00_Accueil]]

Pas de code / target / .env / runs bruts ici.
""", encoding="utf-8")

src = Path("/Users/christophe/ace777-test-day1/Index_Maison/COUTUMES_AGORA.md")
if src.exists():
    (vault / "COUTUMES_AGORA.md").write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

# strengthen coutumes line about not everything in obsidian
c = vault / "COUTUMES_AGORA.md"
if c.exists():
    t = c.read_text(encoding="utf-8")
    if "Pas tout dans Obsidian" not in t:
        t = t.replace(
            "## 2. Un seul vault léger",
            "## 2. Un seul vault léger — **pas tout dedans**\nOui : tu as bien compris. Obsidian = cerveau notes/collab. **Non** : code, builds, fills bruts, secrets.\n\n## 2b. Un seul vault léger",
        )
        c.write_text(t, encoding="utf-8")

ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | `Obsidian_ACE777` | GARAGE prêt — coffre unique + OU_EST_QUOI |"
for mem in [vault/"Swarm_Bus"/"09_MEMOIRE_COLLAB.md", vault/"Index_Maison"/"MEMOIRE_COLLAB.md"]:
    if mem.exists() and "GARAGE prêt" not in mem.read_text(encoding="utf-8"):
        t = mem.read_text(encoding="utf-8")
        m = "|----|-----|--------|-----|------|"
        if m in t:
            mem.write_text(t.replace(m, m + "\\n" + line, 1), encoding="utf-8")
print("notes OK")
PY

# Punk path
echo "export OBSIDIAN_DIR=\"$HOME/Documents/Obsidian_ACE777\"" > /Users/christophe/ace777-test-day1/veille-punk/obsidian.env

echo "--- VERIFY ---"
du -sh "$VAULT"
ls "$VAULT/AGORA.md" "$VAULT/OU_EST_QUOI.md" "$VAULT/COUTUMES_AGORA.md"
python3 -c "import json;from pathlib import Path;print(json.loads((Path.home()/'Library/Application Support/obsidian/obsidian.json').read_text()))"
echo "DONE_GARAGE"
