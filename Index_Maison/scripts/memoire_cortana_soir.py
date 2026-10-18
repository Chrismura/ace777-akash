#!/usr/bin/env python3
"""memoire_cortana_soir.py — MÉMOIRE QUI S'ÉCRIT SEULE (GO 5 points 18/10).

Chaque soir : lit analyses du jour + chats + justesse + cris, écrit
thermo/MEMOIRE_CORTANA_YYYY-MM-DD.md (extractif, 0 token LLM, jamais d'invention)
et régénère MEMOIRE_CORTANA_COURANTE.md (7 derniers jours, lu par le prompt).
Branchement : plist 23:50 quotidienne.
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations

import collections
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
THERMO = os.path.normpath(os.path.join(BASE, "..", "thermo"))
ANALYSES = os.path.join(THERMO, "analyses")


def lire_jour(day: str) -> dict:
    avis = collections.Counter()
    indices = collections.Counter()
    providers = collections.Counter()
    lignes = []
    for f in glob.glob(os.path.join(ANALYSES, f"*{day}*.jsonl")):
        try:
            fh = open(f, encoding="utf-8")
        except Exception:
            continue
        with fh:
            for ln in fh:
                try:
                    d = json.loads(ln)
                except Exception:
                    continue
                txt = d.get("analyse") or ""
                m = re.search(r"AVIS\s*STRICT\s*:\s*(LONG|SHORT|NEUTRE)", txt)
                if not m:
                    continue
                avis[m.group(1)] += 1
                indices[d.get("indice") or "?"] += 1
                providers[str(d.get("provider"))[:40]] += 1
                lignes.append((str(d.get("ts")), d.get("indice"), m.group(1)))
    chats = 0
    for f in glob.glob(os.path.join(THERMO, "cortana_chats*.jsonl")):
        try:
            with open(f, encoding="utf-8") as fh:
                chats += sum(1 for ln in fh if day in ln[:60])
        except Exception:
            pass
    cris = []
    try:
        with open(os.path.join(THERMO, "cortana_cris.jsonl"), encoding="utf-8") as fh:
            for ln in fh:
                if day in ln[:30]:
                    cris.append(json.loads(ln))
    except Exception:
        pass
    return {"avis": dict(avis), "indices": dict(indices),
            "providers": dict(providers), "chats": chats, "cris": cris}


def main() -> int:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if len(sys.argv) > 1:
        day = sys.argv[1]
    r = lire_jour(day)
    try:
        sc = json.load(open(os.path.join(BASE, "justesse_cockpit.json"), encoding="utf-8"))
        score_txt = ("score global %s%% (%s/%s) · directionnel %s" % (
            sc.get("pct"), sc.get("total_hit"), sc.get("total_scored"), sc.get("directionnel")))
    except Exception:
        score_txt = "score illisible"
    n_avis = sum(r["avis"].values())
    out = [
        f"# Mémoire Cortana — {day} (auto, extractif, 0 invention)",
        "",
        f"- analyses notées : {n_avis} ({', '.join(f'{k} {v}' for k, v in sorted(r['avis'].items())) or 'aucune'})",
        "- indices : " + (", ".join(f"{k}×{v}" for k, v in sorted(r["indices"].items())) or "aucun"),
        "- plumes : " + (", ".join(f"{k}×{v}" for k, v in sorted(r["providers"].items())) or "aucune"),
        f"- conversations : {r['chats']}",
        "- mains levées : " + (", ".join(f"{c.get('indice')} {c.get('verdict_calc')}" for c in r["cris"]) or "aucune"),
        f"- justesse : {score_txt}",
        "",
        "_Relu automatiquement par le prompt (MEMOIRE_COURANTE). Le passé ne se réécrit pas._",
    ]
    path = os.path.join(THERMO, f"MEMOIRE_CORTANA_{day}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    # rolling 7 jours
    files = sorted(glob.glob(os.path.join(THERMO, "MEMOIRE_CORTANA_2*.md")))[-7:]
    courant = ["# Mémoire courante Cortana (7 derniers jours, auto)",
               ""]
    for fp in files:
        try:
            courant.append(open(fp, encoding="utf-8").read().strip())
            courant.append("\n---\n")
        except Exception:
            pass
    with open(os.path.join(THERMO, "MEMOIRE_CORTANA_COURANTE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(courant))
    print(f"[memoire] {path} + COURANTE ({len(files)} jours)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
