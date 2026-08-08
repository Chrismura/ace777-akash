#!/usr/bin/env python3
"""Phase 1A — coller un texte/URL → note Obsidian Veille_secteur (ne trade pas).

Usage:
  python3 scripts/veille_secteur_ingest.py --title "..." --source "@beamnxw" --utile Qwen
  # puis coller le texte sur stdin, terminer par Ctrl-D

  echo "mon résumé" | python3 scripts/veille_secteur_ingest.py -t "Idee loops" -s "article"

Écrit dans:
  ~/Documents/Obsidian_ACE777/Veille_secteur/YYYY-MM-DD_HHMM.md
  et met à jour INDEX.md (best-effort)
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path.home() / "Documents" / "Obsidian_ACE777" / "Veille_secteur"


def slug(s: str) -> str:
    s = re.sub(r"[^\w\-]+", "_", s.strip(), flags=re.UNICODE)
    return (s[:40] or "note").strip("_")


def main() -> int:
    ap = argparse.ArgumentParser(description="Ingest veille → Obsidian (mode collage)")
    ap.add_argument("-t", "--title", required=True)
    ap.add_argument("-s", "--source", default="manuel")
    ap.add_argument(
        "--utile",
        default="à classer",
        help="Hulk / ACE / Qwen / Cortana / ignore",
    )
    ap.add_argument("--tester", default="rien", help="une idée ou 'rien'")
    args = ap.parse_args()

    print("Colle le texte (fin = Ctrl-D) :", file=sys.stderr)
    body = sys.stdin.read().strip()
    if not body:
        print("FAIL: texte vide", file=sys.stderr)
        return 1

    VAULT.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    fname = f"{now.strftime('%Y-%m-%d_%H%M')}_{slug(args.title)}.md"
    path = VAULT / fname

    md = f"""# Veille secteur — {now.strftime('%Y-%m-%d %H:%M')}

## Signal

**{args.title}** — source : {args.source}

{body}

## Utile pour nous ?

- {args.utile}

## À tester un jour ?

- {args.tester}

---
_Ingest Phase 1A — ne trade pas._
"""
    path.write_text(md, encoding="utf-8")
    print(f"OK → {path}")

    index = VAULT / "INDEX.md"
    try:
        prev = index.read_text(encoding="utf-8") if index.exists() else "# Index — Veille secteur\n\n| Date | Fichier | Utile pour |\n|------|---------|------------|\n"
        if fname not in prev:
            line = f"| {now.strftime('%Y-%m-%d %H:%M')} | [[{path.stem}]] | {args.utile} |\n"
            # insert after header table if present
            if "| Date |" in prev:
                parts = prev.splitlines()
                out = []
                inserted = False
                for i, ln in enumerate(parts):
                    out.append(ln)
                    if (not inserted) and ln.startswith("|---"):
                        out.append(line.rstrip())
                        inserted = True
                if not inserted:
                    out.append(line.rstrip())
                index.write_text("\n".join(out) + "\n", encoding="utf-8")
            else:
                index.write_text(prev.rstrip() + "\n" + line, encoding="utf-8")
    except OSError as e:
        print(f"WARN index: {e}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
