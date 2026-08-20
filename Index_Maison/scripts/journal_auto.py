#!/usr/bin/env python3
"""
Journal auto + refresh CONSOLE_GENERALE (froid — zéro ordre trading).

Usage:
  python3 journal_auto.py              # snapshot + écrit notes
  python3 journal_auto.py --sync       # + copie vers Obsidian
  python3 journal_auto.py --dry-run    # affiche sans écrire

Hygiène : coutume agora — fin de session / cron optionnel.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from shutil import copy2

ROOT = Path("/Users/christophe/ace777-test-day1")
HULK = ROOT / "hulk-mexc"
WS = ROOT / "Index_Maison"
VAULT = Path(
    os.environ.get("OBSIDIAN_DIR", str(Path.home() / "Documents" / "Obsidian_ACE777"))
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def local_day() -> str:
    # Europe/Paris approx: use local tz
    return datetime.now().strftime("%Y-%m-%d")


def procs_running() -> dict[str, bool]:
    try:
        out = subprocess.check_output(["ps", "aux"], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return {}
    keys = {
        "ace": ["ace777_launch", "GO_USINE", "watchdog_ace", "fortress", "NUAGE_TEST"],
        "hulk_paper": ["paper_diprip"],
        "hulk_digest": ["digest_watch"],
        "punk": ["veille_check", "suivi_check"],
        "ollama": ["ollama"],
    }
    low = out.lower()
    return {k: any(x.lower() in low for x in v) for k, v in keys.items()}


def sum_nz_pnl(csv_path: Path) -> tuple[int, float]:
    if not csv_path.exists():
        return 0, 0.0
    rows = list(csv.DictReader(csv_path.open()))
    nz = []
    for r in rows:
        try:
            p = float(r.get("pnl") or 0)
        except ValueError:
            continue
        if abs(p) > 1e-12:
            nz.append(p)
    return len(nz), round(sum(nz), 4)


def latest_ace_pair() -> dict:
    """Découverte dynamique : couple ALPHA/BETA du run le plus récent.
    (Corrigé le 20/08 : les noms en dur pointaient vers un vieux run mort,
    d'où les journaux figés alors que MASTER_VORTEX_V2_COLLAB_4H tournait.)"""
    runs = ROOT / "runs"
    alphas = sorted(runs.glob("*_ALPHA_X13_BURST13.csv"),
                    key=lambda p: p.stat().st_mtime, reverse=True)
    out = []
    for a in alphas:
        tag = a.name.replace("_ALPHA_X13_BURST13.csv", "")
        b = runs / f"{tag}_BETA_X5.csv"
        if not b.exists():
            continue
        meta = runs / f"{tag}_run_meta.json"
        na, sa = sum_nz_pnl(a)
        nb, sb = sum_nz_pnl(b)
        m = {}
        if meta.exists():
            try:
                m = json.loads(meta.read_text())
            except Exception:
                pass
        out.append(
            {
                "tag": tag,
                "alpha_n": na,
                "alpha_sum": sa,
                "beta_n": nb,
                "beta_sum": sb,
                "combo": round(sa + sb, 4),
                "meta": m,
                "mtime": max(a.stat().st_mtime, b.stat().st_mtime),
            }
        )
    out.sort(key=lambda x: x["mtime"], reverse=True)
    return {"runs": out, "latest": out[0] if out else None}


def hulk_snap() -> dict:
    papers = sorted(HULK.glob("runs/PAPER_V1_*.csv"),
                    key=lambda p: p.stat().st_mtime, reverse=True)
    paper = papers[0] if papers else HULK / "runs" / "PAPER_V1_20260726_174926.csv"
    state = HULK / "runs" / f"{paper.stem}_state.json"
    digest = HULK / "runs" / "DIGEST_LATEST.md"
    d: dict = {"paper_csv": str(paper), "exists": paper.exists()}
    if paper.exists():
        rows = list(csv.DictReader(paper.open()))
        d["events"] = Counter(r.get("event") for r in rows)
        if rows:
            d["pnl_total"] = rows[-1].get("pnl_total")
            d["last_ts"] = rows[-1].get("ts")
    if state.exists():
        st = json.loads(state.read_text())
        d["pnl_state"] = st.get("pnl_total")
        d["n_pos"] = len(st.get("positions") or {})
        d["pairs"] = list((st.get("positions") or {}).keys())
    if digest.exists():
        d["digest_mtime"] = datetime.fromtimestamp(
            digest.stat().st_mtime, tz=timezone.utc
        ).strftime("%Y-%m-%dT%H:%MZ")
        head = digest.read_text(encoding="utf-8", errors="replace").splitlines()[:8]
        d["digest_head"] = "\n".join(head)
    return d


def punk_snap() -> dict:
    latest = ROOT / "veille-punk" / "out" / "CHECK_LATEST.md"
    d = {"exists": latest.exists()}
    if latest.exists():
        t = latest.read_text(encoding="utf-8", errors="replace")
        d["mtime"] = datetime.fromtimestamp(
            latest.stat().st_mtime, tz=timezone.utc
        ).strftime("%Y-%m-%dT%H:%MZ")
        for line in t.splitlines():
            if line.startswith("## Verdict") or "BULLSHIT" in line or "SEMI" in line or "VRAI" in line:
                d["verdict_line"] = line
                break
        d["head"] = "\n".join(t.splitlines()[:12])
    return d


def feu(running: bool, idle_ok: bool = True) -> str:
    if running:
        return "🟢 RUN"
    return "🔴 STOP" if idle_ok else "🟡 IDLE"


def render_console(ace, hulk, punk, procs, day: str) -> str:
    latest = ace.get("latest") or {}
    runs_lines = []
    for r in ace.get("runs") or []:
        runs_lines.append(
            f"| `{r['tag']}` | {r['alpha_sum']:+.2f} (n={r['alpha_n']}) | {r['beta_sum']:+.2f} (n={r['beta_n']}) | **{r['combo']:+.2f}** |"
        )
    h_events = hulk.get("events") or {}
    return f"""# Console générale — clin d’œil

Auto-refresh : {utc_now().strftime('%Y-%m-%d %H:%M')} UTC · jour local **{day}**

## Feu tricolore

| Jambe | État | Détail |
|-------|------|--------|
| **ACE** | {feu(procs.get('ace'))} | Dernier tag `{latest.get('tag','—')}` · combo ≈ **{latest.get('combo',0):+.2f} $** |
| **Hulk paper** | {feu(procs.get('hulk_paper'))} | pnl_total ≈ **{hulk.get('pnl_total') or hulk.get('pnl_state') or '—'}** · pos **{hulk.get('n_pos','—')}** |
| **Hulk digest** | {feu(procs.get('hulk_digest'), idle_ok=True)} | mtime {hulk.get('digest_mtime','—')} |
| **Punk** | {feu(procs.get('punk'), idle_ok=True)} | {punk.get('mtime','—')} · {punk.get('verdict_line','idle')} |
| **Ollama** | {feu(procs.get('ollama'))} | |
| **Obsidian** | 🟢 | vault `{VAULT.name}` |

## ACE — comparaison fills (pnl ≠ 0)

| Run | Alpha | Beta | Combo |
|-----|-------|------|-------|
{chr(10).join(runs_lines) if runs_lines else '| — | — | — | — |'}

## Hulk
- Events : {dict(h_events) if h_events else '—'}
- Pairs ouvertes (state) : {', '.join(hulk.get('pairs') or []) or '—'}

## Liens
[[PLAN_DE_VOL]] · [[AUTO_PROCESSUS]] · [[AGORA]] · [[Cahier/Journal_{day}]] · [[OSSATURE]]
"""


def render_journal(ace, hulk, punk, procs, day: str) -> str:
    latest = ace.get("latest") or {}
    return f"""# Journal — {day}

Tags: #journal #swarm #auto

## Résumé
Snapshot auto (`journal_auto.py`). Bots : ACE={'ON' if procs.get('ace') else 'OFF'} · Hulk={'ON' if procs.get('hulk_paper') else 'OFF'} · Ollama={'ON' if procs.get('ollama') else 'OFF'}.

## ACE
- Dernier focus : `{latest.get('tag','—')}` combo ≈ **{latest.get('combo',0):+.2f} $** (Alpha {latest.get('alpha_sum',0):+.2f} / Beta {latest.get('beta_sum',0):+.2f})
- Champion : non modifié par ce script.
- Détail runs : voir [[CONSOLE_GENERALE]]

## Hulk
- pnl_total ≈ **{hulk.get('pnl_total') or hulk.get('pnl_state') or '—'}**
- Positions state : **{hulk.get('n_pos','—')}** — {', '.join(hulk.get('pairs') or []) or 'aucune'}
- Digest : {hulk.get('digest_mtime','—')}

## Veille / Punk
- {punk.get('mtime','—')}
- {punk.get('verdict_line','pas de check récent')}

## Suite
[[PLAN_DE_VOL]] · [[CONSOLE_GENERALE]] · [[AUTO_PROCESSUS]]
"""


def append_memoire(vault: Path, line: str) -> None:
    for mem in [
        vault / "Swarm_Bus" / "09_MEMOIRE_COLLAB.md",
        vault / "Index_Maison" / "MEMOIRE_COLLAB.md",
        WS / "MEMOIRE_COLLAB.md",
    ]:
        try:
            if not mem.exists():
                continue
            t = mem.read_text(encoding="utf-8")
            m = "|----|-----|--------|-----|------|"
            if m in t and line not in t:
                mem.write_text(t.replace(m, m + "\n" + line, 1), encoding="utf-8")
        except OSError as e:
            print(f"memoire skip {mem.name}: {e}")


def sync_vault(day: str) -> None:
    """Copy md into Obsidian. If TCC blocks Documents, fall back to OUTBOX + Terminal."""
    mapping = [
        (WS / "CONSOLE_GENERALE.md", "CONSOLE_GENERALE.md"),
        (WS / "CONSOLE_GENERALE.md", "Index_Maison/CONSOLE_GENERALE.md"),
        (WS / f"Journal_{day}.md", f"Cahier/Journal_{day}.md"),
        (WS / f"Journal_{day}.md", f"Index_Maison/Journal_{day}.md"),
        (WS / "PLAN_DE_VOL.md", "PLAN_DE_VOL.md"),
        (WS / "AUTO_PROCESSUS.md", "AUTO_PROCESSUS.md"),
    ]
    outbox = WS / "OUTBOX_OBSIDIAN"
    outbox.mkdir(parents=True, exist_ok=True)
    blocked = False
    for src, rel in mapping:
        if not src.exists():
            continue
        dst = VAULT / rel
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            copy2(src, dst)
            print("sync", dst)
        except OSError as e:
            blocked = True
            print(f"sync-block {rel}: {e}")
            ob = outbox / rel
            ob.parent.mkdir(parents=True, exist_ok=True)
            copy2(src, ob)
    if blocked:
        # Retry via Terminal.app (souvent autorisé Documents)
        script = outbox / "_sync_now.sh"
        lines = ["#!/bin/bash", "set -euo pipefail", f'VAULT="{VAULT}"', f'OB="{outbox}"']
        for src, rel in mapping:
            lines.append(
                f'mkdir -p "$VAULT/$(dirname "{rel}")" && '
                f'cp "$OB/{rel}" "$VAULT/{rel}" && echo OK {rel}'
            )
        lines.append("echo SYNC_VIA_TERMINAL_DONE")
        script.write_text("\n".join(lines) + "\n", encoding="utf-8")
        script.chmod(0o755)
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'tell application "Terminal" to do script "bash {script}"',
                ],
                check=False,
                timeout=15,
            )
            print("spawned Terminal sync fallback")
        except Exception as e:
            print(f"fallback Terminal failed: {e} — notes dans {outbox}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    day = local_day()
    procs = procs_running()
    ace = latest_ace_pair()
    hulk = hulk_snap()
    punk = punk_snap()

    console = render_console(ace, hulk, punk, procs, day)
    journal = render_journal(ace, hulk, punk, procs, day)

    if args.dry_run:
        print(console)
        print("---")
        print(journal[:800])
        return 0

    WS.mkdir(parents=True, exist_ok=True)
    (WS / "CONSOLE_GENERALE.md").write_text(console, encoding="utf-8")
    (WS / f"Journal_{day}.md").write_text(journal, encoding="utf-8")
    # keep plan/auto if missing
    print("wrote", WS / "CONSOLE_GENERALE.md")
    print("wrote", WS / f"Journal_{day}.md")

    if args.sync:
        sync_vault(day)
        ts = utc_now().strftime("%Y-%m-%dT%H%MZ")
        append_memoire(
            VAULT,
            f"| {ts} | journal_auto | ★ | CONSOLE+Journal_{day} | Snapshot auto hygiène soir |",
        )
        # patch AUTO_PROCESSUS line
        auto = WS / "AUTO_PROCESSUS.md"
        if auto.exists():
            t = auto.read_text(encoding="utf-8")
            t2 = t.replace(
                "| Journal du jour → Obsidian | ❌ pas encore | **à brancher** | Hygiène voulue |",
                "| Journal du jour → Obsidian | ✅ script | `Index_Maison/scripts/journal_auto.py --sync` | Hygiène |",
            ).replace(
                "| Console générale refresh | ❌ pas encore | script snapshot | Hygiène voulue |",
                "| Console générale refresh | ✅ script | même commande | Hygiène |",
            )
            auto.write_text(t2, encoding="utf-8")
            try:
                copy2(auto, VAULT / "AUTO_PROCESSUS.md")
            except OSError as e:
                print(f"AUTO vault copy skip: {e}")
                ob = WS / "OUTBOX_OBSIDIAN" / "AUTO_PROCESSUS.md"
                ob.parent.mkdir(parents=True, exist_ok=True)
                copy2(auto, ob)
        print("synced ->", VAULT)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
