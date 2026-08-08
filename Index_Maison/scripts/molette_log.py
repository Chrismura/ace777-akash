#!/usr/bin/env python3
"""Append un bloc dans JOURNAL_MOLETTES_SETUP.md (qui / quoi / pourquoi).

Usage:
  python3 molette_log.py \\
    --molette NUAGE_STORM_HUNTER --avant 0 --apres 1 \\
    --pourquoi "Retest après claque Beta 14:14" --qui Humain
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

WS = Path(__file__).resolve().parents[1]
J = WS / "JOURNAL_MOLETTES_SETUP.md"
OUT = WS / "OUTBOX_OBSIDIAN" / "JOURNAL_MOLETTES_SETUP.md"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--molette", required=True)
    ap.add_argument("--avant", default="?")
    ap.add_argument("--apres", required=True)
    ap.add_argument("--pourquoi", required=True)
    ap.add_argument("--qui", default="Humain")
    ap.add_argument("--preuve", default="pas encore")
    a = ap.parse_args()
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    block = f"""
### {day} — `{a.molette}` {a.avant} → {a.apres}

| | |
|--|--|
| **Qui** | {a.qui} |
| **Molette** | `{a.molette}` |
| **Avant → Après** | {a.avant} → **{a.apres}** |
| **Pourquoi** | {a.pourquoi} |
| **Preuve** | {a.preuve} |
| **ts** | {ts} |

"""
    for path in (J, OUT):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(
                "# Journal des molettes / setups\n\n## Journal (récent en haut)\n"
                + block,
                encoding="utf-8",
            )
            continue
        text = path.read_text(encoding="utf-8")
        marker = "## Journal (récent en haut)"
        if marker in text:
            text = text.replace(marker, marker + "\n" + block, 1)
        else:
            text = text.rstrip() + "\n\n## Journal (récent en haut)\n" + block
        path.write_text(text, encoding="utf-8")
    print(f"MOLETTE_LOG {a.molette} {a.avant}->{a.apres}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
