#!/usr/bin/env python3
"""
Liste les runs ACE (date + plus-value Alpha/Beta/combo).
N'exécute RIEN — lecture seule + commande de lancement à coller (GO humain).

Usage:
  python3 liste_runs.py              # tri date (récent → vieux)
  python3 liste_runs.py --pnl        # tri plus-value (meilleur → pire)
  python3 liste_runs.py --top 10
  python3 liste_runs.py --tag NUAGE_TEST_8H_CMP
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
RUNS = ROOT / "runs"


def sum_nz_pnl(csv_path: Path) -> tuple[int, float]:
    if not csv_path.exists():
        return 0, 0.0
    total = 0.0
    n = 0
    with csv_path.open(newline="", encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            try:
                p = float(r.get("pnl") or 0)
            except ValueError:
                continue
            if abs(p) > 1e-12:
                n += 1
                total += p
    return n, round(total, 4)


def find_pair(tag: str) -> tuple[Path | None, Path | None]:
    """Trouve CSV Alpha/Beta pour un tag."""
    alphas = sorted(RUNS.glob(f"{tag}_ALPHA*.csv"))
    betas = sorted(RUNS.glob(f"{tag}_BETA*.csv"))
    # préférer X13 / X5 si plusieurs
    def prefer(paths: list[Path], needle: str) -> Path | None:
        if not paths:
            return None
        for p in paths:
            if needle in p.name:
                return p
        return paths[0]

    return prefer(alphas, "X13"), prefer(betas, "X5")


def duration_hint(meta: dict) -> str:
    s = meta.get("start_utc") or ""
    e = meta.get("planned_end_utc") or ""
    if not s or not e:
        return "04:00:00"
    try:
        t0 = datetime.fromisoformat(s.replace("Z", "+00:00"))
        t1 = datetime.fromisoformat(e.replace("Z", "+00:00"))
        sec = int((t1 - t0).total_seconds())
        if sec <= 0:
            return "04:00:00"
        h, rem = divmod(sec, 3600)
        m, s2 = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{s2:02d}"
    except Exception:
        return "04:00:00"


def collect() -> list[dict]:
    rows: list[dict] = []
    for meta_path in RUNS.glob("*_run_meta.json"):
        tag = meta_path.name.replace("_run_meta.json", "")
        meta: dict = {}
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            pass
        tag = str(meta.get("tag") or tag)
        a, b = find_pair(tag)
        na, sa = sum_nz_pnl(a) if a else (0, 0.0)
        nb, sb = sum_nz_pnl(b) if b else (0, 0.0)
        start = meta.get("start_utc") or ""
        mtime = meta_path.stat().st_mtime
        if a and a.exists():
            mtime = max(mtime, a.stat().st_mtime)
        if b and b.exists():
            mtime = max(mtime, b.stat().st_mtime)
        rows.append(
            {
                "tag": tag,
                "start": start,
                "mtime": mtime,
                "alpha": sa,
                "beta": sb,
                "combo": round(sa + sb, 4),
                "n_a": na,
                "n_b": nb,
                "dur": duration_hint(meta),
                "has_fills": bool(na or nb),
            }
        )
    return rows


def launch_cmd(tag: str, dur: str) -> str:
    return (
        f"cd {ROOT} && caffeinate -dims ./GO_USINE_NUAGE.sh {dur} {tag}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Runs ACE : date + plus-value")
    ap.add_argument("--pnl", action="store_true", help="Trier par combo PnL")
    ap.add_argument("--top", type=int, default=20, help="Nombre de lignes")
    ap.add_argument("--tag", default="", help="Filtrer un tag")
    ap.add_argument("--all", action="store_true", help="Aussi les runs sans fills")
    ap.add_argument("--cmd", action="store_true", help="Afficher commande lancement")
    args = ap.parse_args()

    rows = collect()
    if args.tag:
        rows = [r for r in rows if args.tag in r["tag"]]
    if not args.all:
        rows = [r for r in rows if r["has_fills"]]

    if args.pnl:
        rows.sort(key=lambda r: (r["combo"], r["mtime"]), reverse=True)
        titre = "TRI PLUS-VALUE (combo = Alpha+Beta, fills ≠ 0)"
    else:
        rows.sort(key=lambda r: (r["start"] or "", r["mtime"]), reverse=True)
        titre = "TRI DATE (récent → vieux)"

    rows = rows[: max(1, args.top)]

    print(f"=== RUNS ACE — {titre} ===")
    print(
        f"{'date_utc':<22} {'combo':>9} {'alpha':>9} {'beta':>9}  {'nA':>3} {'nB':>3}  tag"
    )
    print("-" * 92)
    for r in rows:
        date = (r["start"] or datetime.fromtimestamp(r["mtime"], tz=timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))[:22]
        print(
            f"{date:<22} {r['combo']:>+9.2f} {r['alpha']:>+9.2f} {r['beta']:>+9.2f}  "
            f"{r['n_a']:>3} {r['n_b']:>3}  {r['tag']}"
        )

    if args.cmd and rows:
        print("\n=== COMMANDES À COLLER (seulement si GO humain + Mac froid) ===")
        print("# Ne lance PAS automatiquement — copie à la main.\n")
        for r in rows[:5]:
            print(f"# {r['tag']}  combo={r['combo']:+.2f}  date={r['start'] or '?'}")
            print(launch_cmd(r["tag"], r["dur"]))
            print()

    if not rows:
        print("(aucun run avec fills — essaie --all)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
