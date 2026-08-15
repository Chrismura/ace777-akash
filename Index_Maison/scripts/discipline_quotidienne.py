#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""discipline_quotidienne.py — BOUCLE DE DISCIPLINE CONTINUE (Cortana + Ada) — 15/08/2026.

Chaque jour (launchd com.ace777.discipline-quotidienne, 07:15) :
  1. Re-note CORTANA (score_justesse.py) — la boucle F1 se nourrit toute seule.
  2. Note ADA v1 (zone/voilure vs volatilité BTC 24h) — nouvelle métrique.
  3. Écrit thermo/DISCIPLINE_QUOTIDIENNE.md (visibilité) + DISCIPLINE_ALERT.md si intervention.
  4. Jamais d'ordre. Ne touche ni au moteur ni au genesis.

Alertes (intervention humaine) :
  - Cortana global < 50 %
  - Ada zone-accuracy < 60 %
  - aucune analyse Cortana depuis > 48 h (boucle affamée)
  - score en baisse de >= 5 pts vs le jour précédent

Usage : python3 discipline_quotidienne.py
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts"))
THERMO = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo"))
STRAT = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie"))
HISTORY = THERMO / "history.jsonl"
ANALYSES = THERMO / "analyses"
ADA_JOURNAL = STRAT / "ada_gardienne_historique.jsonl"
JUSTESSE_V2 = SCRIPTS / "justesse_v2.json"
ADA_OUT = SCRIPTS / "justesse_ada_v1.json"
RAPPORT = THERMO / "DISCIPLINE_QUOTIDIENNE.md"
ALERTE = THERMO / "DISCIPLINE_ALERT.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_history() -> list:
    out = []
    try:
        with open(HISTORY) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
    except Exception:
        pass
    return out


def mark_at(history, target_ts):
    """mark BTC au dernier instant <= target_ts."""
    best = None
    for row in history:
        ts = row.get("tsUnix")
        if ts is not None and ts <= target_ts and row.get("mark") is not None:
            best = row["mark"]
    return best


def mark_after_24h(history, target_ts):
    """mark BTC au premier instant >= target_ts + 24h (fenêtre d'évaluation)."""
    t = target_ts + 24 * 3600
    for row in history:
        if row.get("tsUnix") is not None and row.get("tsUnix") >= t and row.get("mark") is not None:
            return row["mark"]
    return None


def ts_of(ts_str):
    try:
        return datetime.fromisoformat(str(ts_str).replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def score_ada(history) -> dict:
    """v1 : zone (VERT/JAUNE/ROUGE) vs volatilité BTC sur les 24h suivantes.
    ROUGE/PRENDS_LA_PERTE → stress attendu : HIT si |move24| >= 1.5% ou move <= -0.5%.
    JAUNE → HIT si |move24| >= 1.0%. VERT → HIT si |move24| < 1.0% (calme)."""
    hits, n = 0, 0
    details = []
    if not ADA_JOURNAL.exists():
        return {"hit": 0, "n": 0, "pct": None, "details": [], "note": "journal absent"}
    for line in ADA_JOURNAL.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except Exception:
            continue
        zone = str(row.get("zone") or "").upper()
        if zone not in ("VERT", "JAUNE", "ROUGE", "PRENDS_LA_PERTE"):
            continue
        t0 = ts_of(row.get("ts"))
        if t0 is None:
            continue
        p0 = mark_at(history, t0)
        p1 = mark_after_24h(history, t0)
        if p0 is None or p1 is None or p0 == 0:
            continue
        move = (p1 - p0) / p0 * 100.0
        vol = abs(move)
        if zone in ("ROUGE", "PRENDS_LA_PERTE"):
            ok = vol >= 1.5 or move <= -0.5
        elif zone == "JAUNE":
            ok = vol >= 1.0
        else:  # VERT
            ok = vol < 1.0
        hits += 1 if ok else 0
        n += 1
        details.append({"ts": row.get("ts"), "zone": zone, "move24_pct": round(move, 2),
                        "ok": ok, "vol24_pct": round(vol, 2)})
    pct = round(hits / n * 100, 1) if n else None
    return {"hit": hits, "n": n, "pct": pct, "details": details[-30:],
            "note": "v1 zone/voilure vs BTC 24h"}


def main() -> int:
    # 1) Re-note Cortana (boucle F1)
    try:
        subprocess.run([sys.executable, str(SCRIPTS / "score_justesse.py")],
                       check=False, capture_output=True, timeout=180)
    except Exception as e:
        print(f"[ERR] score_justesse : {e}", file=sys.stderr)
    cort = {}
    try:
        cort = json.load(open(JUSTESSE_V2))
    except Exception:
        pass

    # 1b) Dérive mémoire (4 indicateurs @0xWast3, chantier 2) — fail-open
    derive_info = {}
    try:
        p = subprocess.run([sys.executable, str(SCRIPTS / "derive_memoire.py")],
                           check=False, capture_output=True, timeout=60)
        derive_info = {"rc": p.returncode, "md": THERMO / "DERIVE_MEMOIRE.md"}
    except Exception as e:
        print(f"[ERR] derive_memoire : {e}", file=sys.stderr)
        derive_info = {"rc": None}

    # 1c) Kelly ombre (chantier 3, sizing Hulk) — fail-open, non bloquant
    try:
        subprocess.run([sys.executable, str(SCRIPTS / "kelly_ombre.py")],
                       check=False, capture_output=True, timeout=30)
    except Exception:
        pass

    # 1d) AGORA — boucle E4 (leçons HIT/MISS, famille 15/08) : scan PUIS validation,
    #     APRÈS la note Cortana (jamais avant — nvidia). Fail-open, non bloquant.
    try:
        subprocess.run([sys.executable, str(SCRIPTS / "lecons_auto.py"), "--scan"],
                       check=False, capture_output=True, timeout=30)
        subprocess.run([sys.executable, str(SCRIPTS / "lecons_auto.py"), "--valider"],
                       check=False, capture_output=True, timeout=30)
    except Exception as e:
        print(f"[ERR] lecons_auto : {e}", file=sys.stderr)

    # 1e) Nombre de leçons actives (pour le rapport)
    n_lecons = 0
    try:
        base = json.load(open(STRAT / "CONNAISSANCE_PROJETS.json"))
        n_lecons = len(base.get("lecons_agora", []) or [])
    except Exception:
        pass

    # 2) Note Ada
    ada = score_ada(load_history())
    with open(ADA_OUT, "w", encoding="utf-8") as f:
        json.dump({"ts": utc_now(), **ada}, f, ensure_ascii=False, indent=2)

    # 3) Rapport + alertes
    pct = cort.get("pct")
    par = cort.get("par_indice") or {}
    alerts = []
    if pct is not None and pct < 50:
        alerts.append(f"CORTANA sous 50% ({pct}%) — discipline NEUTRE active, à surveiller")
    if ada.get("pct") is not None and ada["pct"] < 60:
        alerts.append(f"ADA zone-accuracy {ada['pct']}% < 60% — sa voilure à revoir")
    if derive_info.get("rc") == 1:
        alerts.append("DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md")
    elif derive_info.get("rc") == 2:
        alerts.append("DÉRIVE MÉMOIRE : au moins 1 indice CRITIQUE — voir DERIVE_MEMOIRE.md")
    last_ana = None
    if ANALYSES.is_dir():
        for fn in ANALYSES.glob("*.jsonl"):
            try:
                m = fn.stat().st_mtime
                last_ana = max(last_ana or 0, m)
            except Exception:
                pass
    if last_ana and (datetime.now(timezone.utc).timestamp() - last_ana) > 48 * 3600:
        alerts.append("AUCUNE analyse Cortana depuis > 48h — boucle affamée, relancer la cadence")

    tend = ""
    hier = RAPPORT.read_text(encoding="utf-8") if RAPPORT.exists() else ""
    m = re.search(r"Score global : (\d+)", hier)
    if m and pct is not None:
        prev = int(m.group(1))
        if pct - prev <= -5:
            tend = f" ({prev}% → {pct}% : baisse ≥ 5 pts)"
            alerts.append(f"Tendance à la baisse : {prev}% → {pct}%")

    lines = [
        f"# DISCIPLINE QUOTIDIENNE — {utc_now()}",
        "",
        "## ALERTES",
        "\n".join(f"- 🔴 {a}" for a in alerts) if alerts else "- ✅ Rien à signaler",
        "",
        "## CORTANA (justesse, 44% = pile-ou-face)",
        (f"- Score global : {pct}%{tend}" if pct is not None else "- Score global : n/d"),
        f"- Analyses notées : {cort.get('total_hit')}/{cort.get('total_scored')}",
        ("- Par indice : " + "; ".join(
            f"{k} {v.get('hit')}/{v.get('n')}" for k, v in sorted(par.items())))
        if par else "- Par indice : —",
        "",
        "## ADA (zone/voilure vs BTC 24h, v1)",
        f"- Zone-accuracy : {ada.get('pct')}% ({ada.get('hit')}/{ada.get('n')})",
        f"- {ada.get('note')}",
        "",
        "## MÉMOIRE (dérive, chantier 2)",
        "- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).",
        "- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).",
        "",
        "## AGORA (leçons apprises, chantier E4)",
        f"- Leçons actives : {n_lecons} (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.",
        "- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).",
        "",
        "## Boucle",
        "- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.",
        "- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.",
        "",
    ]
    RAPPORT.write_text("\n".join(lines), encoding="utf-8")
    alerte_txt = "\n".join(f"- {a}" for a in alerts) if alerts else "OK"
    ALERTE.write_text(f"# DISCIPLINE ALERT — {utc_now()}\n\n{alerte_txt}\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if not alerts else 3


if __name__ == "__main__":
    sys.exit(main())
