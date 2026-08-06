#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""score_justesse.py — le PROFESSEUR note l'analyste (chantier 3, C6)
=====================================================================
Exigence Christophe (06/08) : chaque analyse est ENREGISTRÉE, et on
compare ensuite avec ce que le marché a RÉELLEMENT fait -> score de
justesse de l'analyste (Cortana/Gemini).

Comment ça marche :
  1. Lit analyses/YYYY-MM-DD.jsonl (journal des analyses).
  2. Pour chaque analyse : extrait l'AVIS STRICT (LONG/SHORT/NEUTRE)
     + HORIZON (24h / 1 semaine) + CONFIANCE.
  3. Retrouve le prix mark au moment de l'analyse (history.jsonl) et le
     prix mark à l'horizon indiqué.
  4. Juge : LONG gagné si prix monté · SHORT gagné si prix baissé ·
     NEUTRE = abstention (pas noté, mais compté).
  5. Affiche un tableau + un score global par indice et global.

Usage :
  python3 score_justesse.py            # note toutes les analyses
  python3 score_justesse.py --jour 2026-08-06
  python3 score_justesse.py --detail   # détail de chaque analyse

Note : l'avis est extrait par regex de la section `AVIS STRICT : ...`
(le prompt v3 force ce format). Les analyses sans avis (avant v3)
sont signalées comme « sans verdict ».
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

THERMO_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
HISTORY = os.path.join(THERMO_DIR, "history.jsonl")

HORIZONS = {"24h": 24 * 3600, "1 semaine": 7 * 24 * 3600, "1sem": 7 * 24 * 3600,
            "semaine": 7 * 24 * 3600, "48h": 48 * 3600, "1h": 3600, "4h": 4 * 3600}


def load_history():
    out = []
    if not os.path.exists(HISTORY):
        return out
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


def load_analyses(jour=None):
    entries = []
    if not os.path.isdir(ANALYSES_DIR):
        return entries
    for fn in sorted(os.listdir(ANALYSES_DIR)):
        if not fn.endswith(".jsonl"):
            continue
        if jour and jour not in fn:
            continue
        with open(os.path.join(ANALYSES_DIR, fn)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except Exception:
                    continue
    return entries


def parse_avis(analyse):
    """Extrait AVIS STRICT / HORIZON / CONFIANCE du texte d'analyse."""
    txt = analyse.get("analyse", "") or ""
    avis = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", txt)
    horizon = re.search(r"HORIZON\s*:\s*([0-9]+h|1\s*semaine|semaine|48h|24h|1h|4h)", txt)
    confiance = re.search(r"CONFIANCE\s*:\s*(\w+)", txt)
    return {
        "avis": avis.group(1).upper() if avis else None,
        "horizon": horizon.group(1).strip().lower() if horizon else None,
        "confiance": confiance.group(1).lower() if confiance else None,
    }


def ts_of(analyse):
    """Timestamp unix de l'analyse (faits_bruts.ts ou ts ISO)."""
    raw = analyse.get("faits_bruts") or {}
    if raw.get("ts"):
        try:
            return datetime.fromisoformat(raw["ts"].replace("Z", "+00:00")).timestamp()
        except Exception:
            pass
    try:
        return datetime.fromisoformat(analyse["ts"].replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def mark_at(history, target_ts, before=True):
    """mark le plus proche de target_ts (before=True -> dernier point <= target)."""
    best = None
    for row in history:
        ts = row.get("tsUnix")
        m = row.get("mark")
        if ts is None or m is None:
            continue
        if before:
            if ts <= target_ts:
                best = m
        else:
            if ts >= target_ts:
                return m
            best = m
    return best


def juger(analyse, history):
    """Retourne le verdict pour une analyse."""
    avis_info = parse_avis(analyse)
    avis = avis_info["avis"]
    if avis not in ("LONG", "SHORT"):
        return {**avis_info, "statut": "sans_verdict" if not avis else "abstention",
                "detail": f"avis={avis}"}

    t0 = ts_of(analyse)
    if t0 is None:
        return {**avis_info, "statut": "ts_introuvable"}

    hor = avis_info["horizon"] or "24h"
    seconds = HORIZONS.get(hor, 24 * 3600)

    p0 = mark_at(history, t0, before=True)
    if p0 is None:
        return {**avis_info, "statut": "prix_depart_introuvable"}

    t1 = t0 + seconds
    p1 = mark_at(history, t1, before=False)
    if p1 is None:
        return {**avis_info, "statut": "en_attente",
                "detail": f"horizon {hor} pas encore écoulé (p0={p0:.0f})"}

    move = (p1 - p0) / p0 * 100.0
    if avis == "LONG":
        gagne = move > 0.05
        perdu = move < -0.05
    else:  # SHORT
        gagne = move < -0.05
        perdu = move > 0.05
    if gagne:
        statut = "HIT ✅"
    elif perdu:
        statut = "MISS ❌"
    else:
        statut = "FLAT ➖"
    return {**avis_info, "statut": statut, "p0": p0, "p1": p1,
            "move_pct": round(move, 2), "detail": f"{p0:.0f} -> {p1:.0f} ({move:+.2f}%)"}


def main():
    ap = argparse.ArgumentParser(description="Score de justesse de l'analyste")
    ap.add_argument("--jour", default=None, help="YYYY-MM-DD (défaut: tous)")
    ap.add_argument("--detail", action="store_true", help="détail ligne par ligne")
    a = ap.parse_args()

    history = load_history()
    analyses = load_analyses(a.jour)
    if not analyses:
        print("Aucune analyse dans le journal. (lancer d'abord cortana_analyse.py)")
        return 0

    print(f"=== SCORE DE JUSTESSE — {len(analyses)} analyse(s) ===\n")
    total_hit = total_scored = 0
    par_indice = {}

    for an in analyses:
        v = juger(an, history)
        ligne = f"  [{an.get('ts','?')[:16]}] {an.get('indice','?'):14} "
        ligne += f"{v['avis'] or '-':5} h={v['horizon'] or '?':9} c={v['confiance'] or '?':7} "
        ligne += f"→ {v['statut']}"
        if a.detail and v.get("detail"):
            ligne += f"  ({v['detail']})"
        print(ligne)
        if v["statut"] in ("HIT ✅", "MISS ❌", "FLAT ➖"):
            total_scored += 1
            par_indice.setdefault(an.get("indice"), [0, 0])
            if v["statut"] == "HIT ✅":
                total_hit += 1
                par_indice[an.get("indice")][0] += 1
            par_indice[an.get("indice")][1] += 1

    print()
    if total_scored:
        pct = total_hit / total_scored * 100
        print(f"  GLOBAL : {total_hit}/{total_scored} = {pct:.0f} % de justesse")
        for indice, (h, n) in sorted(par_indice.items()):
            print(f"    {indice:14} : {h}/{n}")
    else:
        print("  Aucun verdict noté pour l'instant — il faut attendre que les horizons (24h/semaine) s'écoulent.")
    print("\n  NB: NEUTRE = abstention (comptée mais pas notée) · en_attente = horizon pas encore écoulé.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
