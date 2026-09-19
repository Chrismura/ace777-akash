#!/usr/bin/env python3
"""Une ligne MEMOIRE_COLLAB — pour TOUT le monde (Cursor, Punk, humain, scripts).

Usage:
  python3 memoire_log.py Cursor "★" "Index/cockpit" "bulles portefeuille OK"
  python3 memoire_log.py --qui Humain --action ★ --ou GO --quoi "relance ACE"

Écrit : Index_Maison/MEMOIRE_COLLAB.md + OUTBOX (sync Obsidian = Terminal).
Ne touche PAS au trading.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
MEM = WS / "MEMOIRE_COLLAB.md"
OUT = WS / "OUTBOX_OBSIDIAN" / "MEMOIRE_COLLAB.md"
OUT2 = WS / "OUTBOX_OBSIDIAN" / "Index_Maison" / "MEMOIRE_COLLAB.md"
# 3e miroir : le COFFRE Obsidian lui-même. obsidian_writer protège désormais ce
# stem (cf. son PROTECTED_STEMS) → il ne le consomme plus (sans ça, la copie
# racine de l'OUTBOX était prise pour une note brute → write_note dans 00_Inbox
# = doublon + archivage en boucle). La livraison au coffre est donc faite ICI,
# en direct, sans dépendre du daemon.
VAULT_MEM = Path.home() / "Documents" / "Obsidian_ACE777" / "Index_Maison" / "MEMOIRE_COLLAB.md"


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")


def _append(path: Path, row: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    marker = "| ts | Qui | Action | Où | Quoi |"
    sep = "|----|-----|--------|-----|------|"
    if not path.exists():
        path.write_text(
            "# Mémoire collaborative — ce qu’on touche\n\n"
            "## Journal (récent en haut)\n\n"
            f"{marker}\n{sep}\n{row}\n",
            encoding="utf-8",
        )
        return
    text = path.read_text(encoding="utf-8")
    if row in text:
        return  # dédup exacte
    journal_at = text.rfind("## Journal")
    search_from = journal_at if journal_at >= 0 else 0
    idx = text.find(marker, search_from)
    if idx < 0:
        idx = text.find(marker)
    if idx < 0:
        path.write_text(
            text.rstrip() + f"\n\n## Journal (récent en haut)\n\n{marker}\n{sep}\n{row}\n",
            encoding="utf-8",
        )
        return
    after_header = text.find("\n", idx)
    after_sep = text.find("\n", after_header + 1)
    if after_sep < 0:
        path.write_text(text.rstrip() + "\n" + row + "\n", encoding="utf-8")
        return
    insert_at = after_sep + 1
    path.write_text(text[:insert_at] + row + "\n" + text[insert_at:], encoding="utf-8")


def log_touch(qui: str, action: str, ou: str, quoi: str) -> str:
    action = (action or "★").strip()
    if len(action) > 3:
        action = "★"
    row = f"| {_ts()} | {qui} | {action} | {ou} | {quoi} |"
    # 1) la vérité = le workspace (canon, append-only)
    try:
        _append(MEM, row)
    except OSError as e:
        print(f"[memoire_log] {MEM.name}: {e}", file=sys.stderr)
    # 2) miroirs = COPIE INTÉGRALE (v2 19/09) : OUTBOX racine (poussé par
    #    git_push_auto.sh = sauvegarde versionnée du repo système) + OUTBOX/
    #    Index_Maison (mapping coffre) + le COFFRE en direct. Avant : on n'écrivait
    #    qu'UNE ligne dans l'OUTBOX → le coffre ne recevait qu'un stub de 462 o, et
    #    les lecteurs qui pointaient dessus (superviseur 1septies, brief) ne
    #    voyaient RIEN. Un miroir doit porter la mémoire ENTIÈRE, pas un extrait.
    for p in (OUT, OUT2, VAULT_MEM):
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(MEM, p)
        except OSError as e:
            print(f"[memoire_log] {p.name}: {e}", file=sys.stderr)
    return row


def main() -> int:
    if len(sys.argv) >= 5 and not sys.argv[1].startswith("-"):
        qui, action, ou = sys.argv[1], sys.argv[2], sys.argv[3]
        quoi = " ".join(sys.argv[4:])
        print(log_touch(qui, action, ou, quoi))
        return 0
    ap = argparse.ArgumentParser(description="Log 1 ligne MEMOIRE_COLLAB")
    ap.add_argument("--qui", default="Cursor")
    ap.add_argument("--action", default="★")
    ap.add_argument("--ou", required=True)
    ap.add_argument("--quoi", required=True)
    a = ap.parse_args()
    print(log_touch(a.qui, a.action, a.ou, a.quoi))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
