#!/bin/bash
set -euo pipefail
LOG="/Users/christophe/ace777-test-day1/Index_Maison/scripts/garage_liens_graph.log"
exec > >(tee "$LOG") 2>&1
VAULT="$HOME/Documents/Obsidian_ACE777"
OB="$VAULT/.obsidian"

osascript -e 'quit app "Obsidian"' 2>/dev/null || true
sleep 2
killall Obsidian 2>/dev/null || true
sleep 1

python3 <<'PY'
import json
from pathlib import Path
from datetime import datetime, timezone

vault = Path.home() / "Documents" / "Obsidian_ACE777"
ob = vault / ".obsidian"
ob.mkdir(exist_ok=True)

# Enable graph again (vault is light)
core_path = ob / "core-plugins.json"
core = {}
if core_path.exists():
    try:
        core = json.loads(core_path.read_text(encoding="utf-8"))
    except Exception:
        core = {}
core["graph"] = True
core["backlink"] = True
core["outgoing-link"] = True
core["file-explorer"] = True
core["global-search"] = True
core["switcher"] = True
core["command-palette"] = True
core["page-preview"] = False  # keep off - can be heavy
core["canvas"] = False
core_path.write_text(json.dumps(core, indent=2), encoding="utf-8")
print("OK graph + backlinks ON")

# Hub note: ossature reliée
(vault / "OSSATURE.md").write_text("""# Ossature — séparé mais relié

**Règle :** chaque monde a sa place, mais **tout se pointe**.

```
                    [[AGORA]]
                       |
         +-------------+-------------+
         |             |             |
   [[OU_EST_QUOI]]  [[COUTUMES_AGORA]]  [[00_PLAN_RAPATRIEMENT]]
         |             |
    hors coffre      collab IA/humain
         |
    ace777 / Hulk / Cortana (chemins dans OU_EST_QUOI)
```

## Coffre (Obsidian)
| Nœud | Vers |
|------|------|
| [[AGORA]] | porte |
| [[Index_Maison/01_TABLEAU_VIVANT]] | améliorations |
| [[Index_Maison/Suivi_Info/COMPTES]] | comptes X |
| [[Index_Maison/A_Mon_Attention/INDEX]] | file attention |
| [[Swarm_Bus/00_LIRE_MOI]] | bus agents |
| [[Swarm_Bus/09_MEMOIRE_COLLAB]] | journal touches |
| [[Cahier/00_Accueil]] | cahier humain |

## Dehors (relié par texte, pas par fichiers lourds)
Voir chemins dans [[OU_EST_QUOI]] — code ACE, Hulk, Cortana, backups.

## Graph View
OK **maintenant** (vault léger). Si l’écran noir revient → Settings → désactiver Graph et dire à Cursor.
""", encoding="utf-8")

# Patch AGORA with OSSATURE + graph note
agora = vault / "AGORA.md"
a = """# Agora

**Coffre unique** — notes / collab. Séparé du code, **relié** par liens.

## Lire d’abord
- [[OSSATURE]] — carte des liens
- [[COUTUMES_AGORA]]
- [[OU_EST_QUOI]] — où est le hors-coffre
- [[00_PLAN_RAPATRIEMENT]]

## Travail
- [[Index_Maison/01_TABLEAU_VIVANT]]
- [[Index_Maison/Suivi_Info/COMPTES]]
- [[Index_Maison/A_Mon_Attention/INDEX]]
- [[Swarm_Bus/09_MEMOIRE_COLLAB]]
- [[Swarm_Bus/00_LIRE_MOI]]
- [[Cahier/00_Accueil]]

## Graph
Ouvre **Graph View** (icône ou Cmd/Ctrl+G selon config) — le vault est léger, c’est rebranché.

Pas de code / target / .env ici.
"""
agora.write_text(a, encoding="utf-8")

# Coutumes: graph OK if light
c = vault / "COUTUMES_AGORA.md"
if c.exists():
    t = c.read_text(encoding="utf-8")
    old = "- Pas de Graph tant que fragile."
    new = "- Graph View : **OK** si vault léger (< ~100 Mo notes). Si crash → couper Graph."
    if old in t:
        t = t.replace(old, new)
    elif "Graph View" not in t:
        t = t.replace(
            "## 6. Hygiène Obsidian (Mac Air 8 Go)",
            "## 6. Hygiène Obsidian (Mac Air 8 Go)\n" + new + "\n",
        )
    if "OSSATURE" not in t:
        t += "\n\nLien carte : [[OSSATURE]] — séparé mais relié.\n"
    c.write_text(t, encoding="utf-8")

# OU_EST_QUOI link to OSSATURE
ou = vault / "OU_EST_QUOI.md"
if ou.exists():
    t = ou.read_text(encoding="utf-8")
    if "OSSATURE" not in t:
        t = t.rstrip() + "\n\nCarte des liens : [[OSSATURE]].\n"
        ou.write_text(t, encoding="utf-8")

ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ~ | Graph+OSSATURE | Graph View rebranché ; ossature liens coffre↔dehors |"
for mem in [vault/"Swarm_Bus"/"09_MEMOIRE_COLLAB.md", vault/"Index_Maison"/"MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "Graph View rebranché" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        mem.write_text(t.replace(m, m + "\n" + line, 1), encoding="utf-8")

print("OK", vault)
print("du would be checked outside")
PY

du -sh "$VAULT"
echo "DONE_LIENS"
