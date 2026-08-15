#!/usr/bin/env python3
"""
rapport_erreurs_session.py — hygiène ACE777 (#3)

Agrège en 1 fichier les raisons de fin / morts / stale / watchdog
sans rescanner le LIVE à la main à chaque incident.

Usage:
  python3 scripts/rapport_erreurs_session.py
  python3 scripts/rapport_erreurs_session.py --since 2026-07-22T11:44:55Z
  TAG=NUAGE_PROD_4H python3 scripts/rapport_erreurs_session.py

Sorties:
  runs/RAPPORT_ERREURS_<ts>.md
  runs/RAPPORT_ERREURS_DERNIER.md
  engle/journal/ERR_SESSION_DERNIER.md

Contexte site (alpage / groupe / 2 SIM / WiFi) :
  les compteurs tension_stale / ping sont des SIGNAUX, pas un verdict
  « c’est forcément le réseau ». Bugs process (set -e, watchdog, STOP)
  restent classés à part.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
ENGLE_J = ROOT / "engle" / "journal"
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def strip(s: str) -> str:
    return ANSI.sub("", s)


def load_meta(tag: str) -> dict:
    p = RUNS / f"{tag}_run_meta.json"
    if p.exists():
        return json.loads(p.read_text())
    return {}


def session_start(meta: dict, since: str | None) -> str:
    if since:
        return since
    return meta.get("start_utc") or "1970-01-01T00:00:00Z"


def iter_live(tag: str):
    p = RUNS / f"{tag}_LIVE_COLOR.log"
    if not p.exists():
        return
    with p.open("r", errors="replace") as f:
        for line in f:
            yield strip(line.rstrip("\n"))


def ts_from_line(line: str) -> str | None:
    # ISO in PROCESS_* lines
    m = re.search(r"(20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)", line)
    if m:
        return m.group(1)
    return None


def classify(line: str) -> str | None:
    l = line.lower()
    if "watchdog_semantic" in l and ("stale" in l or "max_relaunch" in l or "stop session" in l):
        return "E-WATCHDOG"
    if "watchdog_duo" in l and ("max " in l or "stop session" in l or "mort" in l):
        return "E-WATCHDOG"
    if "process_die" in l or "process_exit" in l:
        return "E-PROC"
    if "tension_stale" in l or "nuage_age_ms" in l:
        return "E-STALE"
    if "duo no_trigger" in l or "duo stale" in l or "duo no_state" in l:
        return "E-DUO"
    if "spread_too_wide" in l:
        return "E-SPREAD"
    if "storm_hunter arm" in l:
        return "I-HUNTER"  # info positive
    if "terminated: 15" in l or "killed_by_signal" in l:
        return "E-PROC"
    return None


def csv_fills(tag: str, unit: str, start: str) -> tuple[int, float, Counter]:
    name = {
        "ALPHA": f"{tag}_ALPHA_X13_BURST13.csv",
        "BETA": f"{tag}_BETA_X5.csv",
    }.get(unit)
    if not name:
        return 0, 0.0, Counter()
    path = RUNS / name
    if not path.exists():
        return 0, 0.0, Counter()
    fills = []
    reasons = Counter()
    for r in csv.DictReader(path.open()):
        if (r.get("ts") or "") < start:
            continue
        if r.get("side") in ("BUY", "SELL"):
            fills.append(r)
            reasons[(r.get("exitReason") or "?")[:40]] += 1
    pnl = sum(float(r.get("pnl") or 0) for r in fills)
    return len(fills), pnl, reasons


def parse_iso(ts: str) -> datetime | None:
    try:
        return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def read_stop_reason_file() -> str | None:
    for p in (RUNS / "STOP_REASON.txt", ROOT / "STOP_REASON.txt"):
        if p.exists():
            t = p.read_text(errors="replace").strip()
            if t:
                return t.replace("\n", " | ")
    return None


def last_process_exit_ts(lines: list[str]) -> str | None:
    last = None
    for line in lines:
        if "PROCESS_EXIT" in line:
            ts = ts_from_line(line)
            if ts:
                last = ts
    return last


def count_net_retry(tag: str, start: str) -> int:
    n = 0
    for line in iter_live(tag) or []:
        if not line_in_session(line, start):
            continue
        if "NET_RETRY" in line or "NET_RETRY_EXHAUSTED" in line:
            n += 1
    return n


def infer_why_arret(
    meta: dict,
    start: str,
    last_die: list[str],
    last_watch: list[str],
    net_retries: int,
) -> dict:
    """Une ligne WHY_ARRET — obligatoire en hygiène."""
    written = read_stop_reason_file()
    planned = meta.get("planned_end_utc") or ""
    end_ts = last_process_exit_ts(last_die) or ""
    early_min = None
    timing = "unknown"
    start_dt = parse_iso(start)
    end_dt = parse_iso(end_ts) if end_ts else None
    planned_dt = parse_iso(planned) if planned else None
    ran_min = None
    if start_dt and end_dt:
        ran_min = (end_dt - start_dt).total_seconds() / 60.0
    if end_dt and planned_dt:
        early_min = (planned_dt - end_dt).total_seconds() / 60.0
        if early_min > 15:
            timing = "early_stop"
        elif early_min < -5:
            timing = "late_or_overrun"
        else:
            timing = "near_timer"

    cause = "unknown"
    detail: list[str] = []
    if written and "reason=" in written:
        m = re.search(r"reason=([^\s|]+)", written)
        if m:
            cause = m.group(1)
            detail.append(f"STOP_REASON.txt={written}")
    elif any("max_relaunch" in x or "max BETA" in x or "max ALPHA" in x for x in last_watch):
        cause = "watchdog_max_relaunch"
    elif any("WATCHDOG_SEMANTIC" in x and "STOP session" in x for x in last_watch):
        cause = "watchdog_semantic_stop"
    elif any("stop=STOP_" in x for x in last_die) or any(
        "why=clean_end_or_self_exit_0" in x for x in last_die
    ):
        if timing == "near_timer":
            cause = "timer_or_stop_nominal"
        elif timing == "early_stop":
            cause = "stop_files_early_writer_unknown"
        else:
            cause = "stop_files_clean_exit"
    elif any("killed_by_signal_9" in x for x in last_die):
        cause = "sigkill"
    elif any("killed_by_signal_15" in x for x in last_die):
        cause = "sigterm"
    elif any("nonzero_rc_" in x for x in last_die):
        cause = "process_nonzero_rc"
    elif not last_die:
        cause = "no_process_exit_logged"

    if net_retries >= 3:
        detail.append(f"context_net_retry={net_retries}")
    if ran_min is not None:
        detail.append(f"ran_min={ran_min:.1f}")
    if early_min is not None:
        detail.append(f"vs_planned_min={early_min:+.1f}")
    if timing != "unknown":
        detail.append(f"timing={timing}")

    why_line = f"WHY_ARRET={cause}"
    if detail:
        why_line += " | " + " | ".join(detail)
    return {
        "why_line": why_line,
        "cause": cause,
        "timing": timing,
        "stop_reason_file": written,
        "ran_min": ran_min,
        "early_min": early_min,
        "end_ts": end_ts,
    }


def iter_extra_logs(tag: str):
    """Watchdog etc. parfois hors LIVE — fichiers dédiés."""
    for p in (
        RUNS / "WATCHDOG_SEMANTIC.log",
        RUNS / "PROCESS_EXIT.log",
        RUNS / "DUO_PID_WATCHDOG.log",
        RUNS / f"{tag}_launcher.log",
    ):
        if not p.exists():
            continue
        with p.open("r", errors="replace") as f:
            for line in f:
                yield strip(line.rstrip("\n"))


def line_in_session(line: str, start: str) -> bool:
    """Filtre session : ISO UTC ou HH:MM:SS local (UTC+2 alpage)."""
    ts = ts_from_line(line)
    if ts:
        return ts >= start
    m = re.search(r"\] (\d{2}):(\d{2}):(\d{2})\b", line)
    if not m:
        # PROCESS_/WATCHDOG sans horloge locale : garder
        return ("PROCESS_" in line) or ("WATCHDOG" in line)
    try:
        start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return True
    # horloge LIVE ≈ heure locale Paris/alpage (UTC+2 été)
    hh, mm, ss = map(int, m.groups())
    local = start_dt.astimezone(timezone.utc).replace(tzinfo=None)
    # approx: compare minutes since midnight UTC+2 vs start in UTC+2
    start_local_min = ((int(start_dt.timestamp()) + 2 * 3600) % 86400) // 60
    line_local_min = hh * 60 + mm
    # même jour de session : accepte si HH:MM >= début local − 5 min
    return line_local_min >= max(0, start_local_min - 5)


def build(tag: str, since: str | None) -> dict:
    meta = load_meta(tag)
    start = session_start(meta, since)
    buckets: dict[str, list[str]] = {
        "E-WATCHDOG": [],
        "E-PROC": [],
        "E-STALE": [],
        "E-DUO": [],
        "E-SPREAD": [],
        "I-HUNTER": [],
    }
    counts = Counter()
    last_die = []
    last_watch = []

    def ingest(line: str) -> None:
        if not line_in_session(line, start):
            return
        code = classify(line)
        if not code:
            return
        counts[code] += 1
        if len(buckets[code]) < 25:
            buckets[code].append(line[:220])
        if code == "E-PROC" and ("PROCESS_DIE" in line or "PROCESS_EXIT" in line):
            last_die.append(line[:240])
        if code == "E-WATCHDOG":
            last_watch.append(line[:240])

    for line in iter_live(tag) or []:
        ingest(line)
    for line in iter_extra_logs(tag):
        ingest(line)

    af, ap, ar = csv_fills(tag, "ALPHA", start)
    bf, bp, br = csv_fills(tag, "BETA", start)
    net_retries = count_net_retry(tag, start)
    why = infer_why_arret(meta, start, last_die, last_watch, net_retries)

    # lecture courte
    verdict = [f"**{why['why_line']}**"]
    if why["cause"] == "stop_files_early_writer_unknown":
        verdict.append(
            "STOP posés **avant** la fin timer — writer non tracé (manuel / autre outil). "
            "Prochains runs: `runs/STOP_REASON.txt` (timer / duo) obligatoire."
        )
    if counts["E-WATCHDOG"]:
        verdict.append(
            "Signaux watchdog (sémantique ou duo PID) — voir section WATCHDOG."
        )
    if counts["E-PROC"]:
        verdict.append(
            "Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`."
        )
    if net_retries >= 3:
        verdict.append(
            f"Contexte réseau: {net_retries} NET_RETRY (rc=28 typique) — signal alpage, "
            "pas forcément la cause du STOP."
        )
    if counts["E-STALE"] >= 20:
        verdict.append(
            f"Beaucoup de `tension_stale` ({counts['E-STALE']}) = signal latence feed NUAGE "
            "(gate 800ms). Sur alpage/WiFi/SIM : possible pic réseau — **à corréler**, "
            "pas à conclure seul."
        )
    elif counts["E-STALE"]:
        verdict.append(f"`tension_stale` présent ({counts['E-STALE']}) — signal léger.")
    if counts["E-DUO"]:
        verdict.append(f"Issues duo ({counts['E-DUO']}) — scout/hunter désynchro.")
    if len(verdict) == 1:
        verdict.append("Pas d’autre incident classé — lire WHY_ARRET ci-dessus.")

    return {
        "ts": utc_now(),
        "tag": tag,
        "session_start": start,
        "meta": meta,
        "counts": dict(counts),
        "buckets": buckets,
        "last_die": last_die[-8:],
        "last_watch": last_watch[-8:],
        "alpha": {"fills": af, "pnl": ap, "exits": dict(ar.most_common(6))},
        "beta": {"fills": bf, "pnl": bp, "exits": dict(br.most_common(6))},
        "verdict": verdict,
        "why": why,
        "net_retries": net_retries,
    }


def to_md(d: dict) -> str:
    why = d.get("why") or {}
    lines = [
        f"# RAPPORT ERREURS SESSION — {d['tag']}",
        "",
        f"## WHY_ARRET (ligne obligatoire)",
        "",
        f"`{why.get('why_line', 'WHY_ARRET=unknown')}`",
        "",
        f"- Généré : `{d['ts']}`",
        f"- Fenêtre depuis : `{d['session_start']}`",
        f"- Fin process : `{why.get('end_ts', '?')}`",
        f"- Meta start/end : `{d['meta'].get('start_utc', '?')}` → `{d['meta'].get('planned_end_utc', '?')}`",
        f"- Watchdog meta : stale={d['meta'].get('watchdog_stale_sec', '?')}s "
        f"max_relaunch={d['meta'].get('watchdog_max_relaunch', '?')}",
        f"- NET_RETRY (fenêtre) : {d.get('net_retries', 0)}",
        "",
        "## Contexte site (rappel)",
        "",
        "Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. "
        "Le bot **tient** souvent malgré ça. Les compteurs réseau sont des "
        "**signaux** à croiser avec PROCESS_DIE / logique storm — "
        "**ne pas tout attribuer au setup terrain.**",
        "",
        "## Verdict court",
        "",
    ]
    for v in d["verdict"]:
        lines.append(f"- {v}")
    lines += [
        "",
        "## Compteurs",
        "",
        "| Code | Nb | Sens |",
        "|------|----|------|",
        f"| E-WATCHDOG | {d['counts'].get('E-WATCHDOG', 0)} | heartbeat / max relaunch |",
        f"| E-PROC | {d['counts'].get('E-PROC', 0)} | mort process / signal |",
        f"| E-STALE | {d['counts'].get('E-STALE', 0)} | tension/NUAGE age (signal latence) |",
        f"| E-DUO | {d['counts'].get('E-DUO', 0)} | no_trigger / stale duo |",
        f"| E-SPREAD | {d['counts'].get('E-SPREAD', 0)} | spread trop large |",
        f"| I-HUNTER | {d['counts'].get('I-HUNTER', 0)} | STORM_HUNTER arm (info) |",
        "",
        "## PnL fills (fenêtre)",
        "",
        f"- ALPHA : fills={d['alpha']['fills']} pnl={d['alpha']['pnl']:+.4f} "
        f"exits={d['alpha']['exits']}",
        f"- BETA : fills={d['beta']['fills']} pnl={d['beta']['pnl']:+.4f} "
        f"exits={d['beta']['exits']}",
        f"- **TOTAL** : {d['alpha']['pnl'] + d['beta']['pnl']:+.4f}",
        "",
        "## Derniers PROCESS_DIE / EXIT",
        "",
    ]
    if d["last_die"]:
        for x in d["last_die"]:
            lines.append(f"- `{x}`")
    else:
        lines.append("- *(aucun)*")
    lines += ["", "## Derniers WATCHDOG", ""]
    if d["last_watch"]:
        for x in d["last_watch"]:
            lines.append(f"- `{x}`")
    else:
        lines.append("- *(aucun)*")
    lines += [
        "",
        "## Échantillon E-STALE (max 8)",
        "",
    ]
    for x in d["buckets"].get("E-STALE", [])[:8]:
        lines.append(f"- `{x}`")
    if not d["buckets"].get("E-STALE"):
        lines.append("- *(aucun)*")
    lines += [
        "",
        "## Suite hygiène",
        "",
        "1. Si E-WATCHDOG dominant → axe #3 (heartbeat / stale / relaunch), pas un knob storm.",
        "2. Si E-PROC `last_cmd=` clair → bug bash / set -e (comme E11).",
        "3. Si E-STALE seul sans mort → surveiller ; élargir gate seulement avec preuve.",
        "4. Append manuel dans `engle/JOURNAL_ERREURS.md` si nouvel ID (E15…).",
        "",
        "---",
        "*scripts/rapport_erreurs_session.py — zéro ordre, zéro genesis.*",
        "",
    ]
    return "\n".join(lines)


def detect_latest_tag() -> str | None:
    """Déduit le tag du run le plus récent via runs/*_run_meta.json (mtime).
    Fix 15/08 : évite de retomber sur un tag par défaut (NUAGE_PROD_4H) qui
    n'est pas le run réellement testé (faux diagnostic E-STALE/E-PROC)."""
    try:
        metas = sorted(
            RUNS.glob("*_run_meta.json"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        suffix = "_run_meta.json"
        for p in metas:
            tag = p.name[: -len(suffix)]
            if tag:
                return tag
    except OSError:
        pass
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default=None)
    ap.add_argument("--since", default=None, help="ISO UTC start filtre")
    args = ap.parse_args()
    tag = args.tag or __import__("os").environ.get("STATE_TAG") or detect_latest_tag() or "NUAGE_PROD_4H"

    RUNS.mkdir(parents=True, exist_ok=True)
    ENGLE_J.mkdir(parents=True, exist_ok=True)

    d = build(tag, args.since)
    md = to_md(d)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    out = RUNS / f"RAPPORT_ERREURS_{stamp}.md"
    latest = RUNS / "RAPPORT_ERREURS_DERNIER.md"
    engle = ENGLE_J / "ERR_SESSION_DERNIER.md"
    why_line = (d.get("why") or {}).get("why_line") or "WHY_ARRET=unknown"
    out.write_text(md)
    latest.write_text(md)
    engle.write_text(md)
    (RUNS / "LAST_STOP_REASON.txt").write_text(why_line + "\n")
    # json machine
    (RUNS / f"RAPPORT_ERREURS_{stamp}.json").write_text(json.dumps(d, indent=2))
    # Toujours imprimer la ligne WHY en premier (hygiène)
    print(why_line)
    print(md)
    print(f"\nécrit: {out}")
    print(f"écrit: {latest}")
    print(f"écrit: {engle}")
    print(f"écrit: {RUNS / 'LAST_STOP_REASON.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
