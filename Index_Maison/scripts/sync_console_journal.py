#!/usr/bin/env python3
"""Sync console/journal/hygiene notes into Obsidian vault (md only)."""
import sys
from pathlib import Path
from datetime import datetime, timezone
from shutil import copy2

WS = Path("/Users/christophe/ace777-test-day1/Index_Maison")
VAULT = Path.home() / "Documents" / "Obsidian_ACE777"

files = [
    "CONSOLE_GENERALE.md",
    "PLAN_DE_VOL.md",
    "AUTO_PROCESSUS.md",
    "Journal_2026-07-28.md",
    "COUTUMES_AGORA.md",
]
VAULT.mkdir(parents=True, exist_ok=True)
(cahier := VAULT / "Cahier").mkdir(exist_ok=True)
(im := VAULT / "Index_Maison").mkdir(exist_ok=True)

for name in files:
    src = WS / name
    if not src.exists():
        print("MISS", src)
        continue
    copy2(src, im / name)
    if name.startswith("Journal_"):
        copy2(src, cahier / name)
    if name in ("CONSOLE_GENERALE.md", "PLAN_DE_VOL.md", "AUTO_PROCESSUS.md", "COUTUMES_AGORA.md"):
        copy2(src, VAULT / name)
    print("OK", name)

# AGORA hub links
agora = VAULT / "AGORA.md"
links = [
    "[[CONSOLE_GENERALE]] — clin d’œil",
    "[[PLAN_DE_VOL]] — vols / GO",
    "[[AUTO_PROCESSUS]] — ce qui est branché",
    "[[Cahier/Journal_2026-07-28]] — journal du jour",
]
if agora.exists():
    t = agora.read_text(encoding="utf-8")
    for L in links:
        if L.split("]]")[0] not in t:
            t = t.rstrip() + "\n- " + L + "\n"
    agora.write_text(t, encoding="utf-8")

# mémoire — 19/09 : on écrit dans le CANON du WORKSPACE, plus dans le miroir du
# vault : la ligne écrite dans le miroir était écrasée au miroir suivant (copie
# intégrale depuis le canon) = entrée silencieusement perdue. Le chemin mort
# Swarm_Bus/09_MEMOIRE_COLLAB.md (supprimé) est retiré.
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | CONSOLE+journal | Journal 28 + console + plan vol + auto_processus |"
def _scelle_rituel():
    """Rituel de scellement (R20.1) — chargé PAR CHEMIN, tolérant si absent."""
    try:
        ici = str(Path(__file__).resolve().parent)
        if ici not in sys.path:
            sys.path.insert(0, ici)
        import scelle_rituel
        return scelle_rituel
    except Exception:
        return None


for mem in [WS / "MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "CONSOLE+journal" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        def _ecrire(_mem=mem, _t=t):
            _mem.write_text(_t.replace(m, m + "\n" + line, 1), encoding="utf-8")
        sr = _scelle_rituel()
        if sr is not None:
            sr.ecrire_sous_scelle("Index_Maison/MEMOIRE_COLLAB.md", _ecrire,
                                  motif="sync_console_journal — entrée CONSOLE+journal")
        else:
            _ecrire()
print("DONE_SYNC")
