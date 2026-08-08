#!/usr/bin/env python3
"""Hygiène collab : une ligne par touche dans MEMOIRE_COLLAB (workspace + coffre)."""
from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parent  # veille-punk/
WORKSPACE_MEM = _ROOT.parent / "Index_Maison" / "MEMOIRE_COLLAB.md"


def _load_obsidian_env() -> None:
    if os.environ.get("OBSIDIAN_DIR"):
        return
    env_path = _ROOT / "obsidian.env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export ") :]
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


_load_obsidian_env()
OBSIDIAN_ROOT = Path(
    os.environ.get("OBSIDIAN_DIR", "/Users/christophe/Documents/Obsidian_ACE777")
)
COFFRE_MEM = OBSIDIAN_ROOT / "Swarm_Bus" / "09_MEMOIRE_COLLAB.md"


def _ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")


def _append_table_row(path: Path, row: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(
            "# Mémoire collaborative — ce qu’on touche\n\n"
            "## Journal (récent en haut)\n\n"
            "| ts | Qui | Action | Où | Quoi |\n"
            "|----|-----|--------|-----|------|\n"
            f"{row}\n",
            encoding="utf-8",
        )
        return
    text = path.read_text(encoding="utf-8")
    marker = "| ts | Qui | Action | Où | Quoi |"
    # Cible le journal (dernier tableau avec ce header), pas la légende
    journal_at = text.rfind("## Journal")
    search_from = journal_at if journal_at >= 0 else 0
    idx = text.find(marker, search_from)
    if idx < 0:
        idx = text.find(marker)
    if idx < 0:
        path.write_text(
            text.rstrip()
            + "\n\n## Journal (récent en haut)\n\n"
            + marker
            + "\n|----|-----|--------|-----|------|\n"
            + row
            + "\n",
            encoding="utf-8",
        )
        return
    # après le header + la ligne séparateur
    after_header = text.find("\n", idx)
    if after_header < 0:
        path.write_text(text.rstrip() + "\n" + row + "\n", encoding="utf-8")
        return
    after_sep = text.find("\n", after_header + 1)
    if after_sep < 0:
        path.write_text(text.rstrip() + "\n" + row + "\n", encoding="utf-8")
        return
    insert_at = after_sep + 1
    path.write_text(text[:insert_at] + row + "\n" + text[insert_at:], encoding="utf-8")


def log_touch(
    qui: str,
    action: str,
    ou: str,
    quoi: str,
    *,
    also_coffre: bool = True,
) -> str:
    """action: + ~ ✕ ★ — retourne la ligne écrite."""
    row = f"| {_ts()} | {qui} | {action} | `{ou}` | {quoi} |"
    try:
        _append_table_row(WORKSPACE_MEM, row)
    except OSError as e:
        print(f"[memoire] workspace: {e}", flush=True)
    if also_coffre:
        try:
            _append_table_row(COFFRE_MEM, row)
        except OSError as e:
            print(f"[memoire] coffre: {e}", flush=True)
            # fallback OUTBOX
            try:
                out = (
                    _ROOT.parent
                    / "Index_Maison"
                    / "OUTBOX_OBSIDIAN"
                    / "Swarm_Bus"
                    / "09_MEMOIRE_COLLAB.md"
                )
                _append_table_row(out, row)
                print(f"[memoire] outbox: {out}", flush=True)
            except OSError as e2:
                print(f"[memoire] outbox: {e2}", flush=True)
    return row


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 5:
        print("usage: memoire_collab.py <Qui> <+> <où> <quoi...>")
        sys.exit(2)
    qui, action, ou = sys.argv[1], sys.argv[2], sys.argv[3]
    quoi = " ".join(sys.argv[4:])
    print(log_touch(qui, action, ou, quoi))
