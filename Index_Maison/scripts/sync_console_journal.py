#!/usr/bin/env python3
"""Sync console/journal/hygiene notes into Obsidian vault (md only)."""
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

# mémoire
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | CONSOLE+journal | Journal 28 + console + plan vol + auto_processus |"
for mem in [VAULT / "Swarm_Bus" / "09_MEMOIRE_COLLAB.md", im / "MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "CONSOLE+journal" in t:
        continue
    m = "|----|-----|--------|-----|------|"
    if m in t:
        mem.write_text(t.replace(m, m + "\n" + line, 1), encoding="utf-8")
print("DONE_SYNC")
