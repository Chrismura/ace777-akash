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

# mémoire — 19/09 : on écrit dans le CANON du WORKSPACE, plus dans le miroir du
# vault : la ligne écrite dans le miroir était écrasée au miroir suivant (copie
# intégrale depuis le canon) = entrée silencieusement perdue. Le chemin mort
# Swarm_Bus/09_MEMOIRE_COLLAB.md (supprimé) est retiré.
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
line = f"| {ts} | Cursor | ★ | CONSOLE+journal | Journal 28 + console + plan vol + auto_processus |"
# CORRECTIF 09/10/2026 (GO « go1 ») — même défaut que `journal_auto.py` : l'ancien code
# exigeait le séparateur legacy `|----|-----|--------|-----|------|`, ABSENT du canon →
# no-op silencieux. On insère sous l'en-tête (ou sous le séparateur s'il existe).
_HEADER_JOURNAL = "| ts | Qui | Action | Où | Quoi |"


def _inserer_dans_journal(texte: str, ligne: str):
    """Retourne le texte avec `ligne` en tête du Journal, ou None si impossible/déjà là."""
    if ligne in texte:
        return None
    i = texte.find(_HEADER_JOURNAL)
    if i < 0:
        return None
    fin_entete = texte.find("\n", i)
    if fin_entete < 0:
        return None
    j = fin_entete + 1
    fin_suivante = texte.find("\n", j)
    if fin_suivante < 0:
        fin_suivante = len(texte)
    suivante = texte[j:fin_suivante]
    est_sep = bool(suivante.strip()) and set(suivante.strip()) <= set("|-: ")
    insert_at = (fin_suivante + 1) if est_sep else j
    return texte[:insert_at] + ligne + "\n" + texte[insert_at:]


for mem in [WS / "MEMOIRE_COLLAB.md"]:
    if not mem.exists():
        continue
    t = mem.read_text(encoding="utf-8")
    if "CONSOLE+journal" in t:
        continue
    nouveau = _inserer_dans_journal(t, line)
    if nouveau is not None:
        def _ecrire(_mem=mem, _texte=nouveau):
            _mem.write_text(_texte, encoding="utf-8")
        _ecrire()
print("DONE_SYNC")
