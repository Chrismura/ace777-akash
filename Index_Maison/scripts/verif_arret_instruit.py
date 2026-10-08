#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIF ARRET INSTRUIT — garde mécanique de la classe E26 (câblée le 08/10/2026)
==============================================================================
CLASSE E26 (30/09/2026) : Buffy a lu « stop paper, explique? » comme un ORDRE d'arrêt et a créé
le drapeau `STOP_PAPER` → le moteur s'est arrêté proprement, trou de collecte ~4 min 37 s, et
un état de garde (`slip_stats`) perdu en mémoire. La règle : **aucune interruption sans
instruction EXPLICITE**, et une instruction explicite laisse une TRACE.

CE QUE LA GARDE MESURE (déterministe) : si un drapeau d'arrêt existe, une **trace d'ordre
explicite** doit exister — `strategie/ORDRE_ARRET.json` (`{ts, go, motif}`) — et être **antérieure
ou égale** au drapeau (une trace écrite APRÈS l'acte ne l'autorise pas : c'est la leçon R20.1
appliquée à l'arrêt). Pas de drapeau → rien à juger → **CONFORME** (pas de faux reproche, R14).

LECTURE SEULE · 0 ordre · 0 € · stdlib. Branché par `git_push_auto.sh` (3 h). `--autotest`.

POURQUOI ELLE POUVAIT NE PAS EXISTER : c'est la proposition du HUB (`--ia`) pour E26, câblée après
lecture du code (les drapeaux réels sont ceux ci-dessous), pas recopiée du texte du modèle.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
DRAPEAUX = [RACINE / "hulk-mexc" / "STOP_PAPER", IM / "STOP_ALL", IM / "strategie" / "STOP"]
TRACE = IM / "strategie" / "ORDRE_ARRET.json"
OUT_JSON = IM / "thermo" / "arret_instruit.json"
JOUR = "%Y-%m-%dT%H:%M:%SZ"


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def controler(drapeaux: list[Path], trace: Path) -> tuple[bool, str, list[str]]:
    """Logique pure (autotestable). Rend (ok, detail, drapeaux_présents)."""
    presents = [p for p in drapeaux if p.exists()]
    if not presents:
        return True, "aucun drapeau d'arrêt — rien à autoriser", []
    if not trace.exists():
        return False, (f"{len(presents)} drapeau(x) d'arrêt présent(s) SANS instruction explicite "
                       f"tracée ({trace.name} absent) — classe E26"), [p.name for p in presents]
    try:
        d = json.loads(trace.read_text(encoding="utf-8"))
        ts = str(d.get("ts") or "")
        t_ordre = datetime.strptime(ts, JOUR).replace(tzinfo=timezone.utc)
    except Exception as e:                                  # noqa: BLE001
        return False, f"trace d'ordre illisible ({e}) — non mesurable, on ne verdit pas", [p.name for p in presents]
    plus_tard = [p.name for p in presents
                 if datetime.fromtimestamp(p.stat().st_mtime, timezone.utc) < t_ordre]
    if plus_tard:
        return False, (f"drapeau(x) {plus_tard} antérieur(s) à l'ordre ({ts}) — un drapeau posé "
                       f"AVANT l'ordre n'est pas instruit"), [p.name for p in presents]
    return True, (f"{len(presents)} drapeau(x) couvert(s) par un ordre explicite du {ts} "
                  f"« {str(d.get('go') or '')[:60]} »"), [p.name for p in presents]


def main() -> int:
    if "--autotest" in sys.argv:
        return autotest()
    ok, detail, presents = controler(DRAPEAUX, TRACE)
    res = {"ts": utc(), "ok": ok, "detail": detail, "drapeaux_presents": presents,
           "trace": str(TRACE), "lecture_seule": True, "ordres": 0}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[arret_instruit] {'OK' if ok else 'ANOMALIE'} — {detail}")
    return 0 if ok else 1


def autotest() -> int:
    import tempfile
    cas = []
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        flag = d / "STOP_PAPER"
        trace = d / "ORDRE_ARRET.json"
        # 1) aucun drapeau → conforme
        cas.append(("aucun drapeau → conforme", controler([flag], trace)[0]))
        # 2) drapeau + ordre ANTÉRIEUR → conforme
        trace.write_text(json.dumps({"ts": "2026-01-01T00:00:00Z", "go": "GO Christophe", "motif": "x"}),
                         encoding="utf-8")
        flag.write_text("stop", encoding="utf-8")
        cas.append(("drapeau couvert par un ordre antérieur → conforme", controler([flag], trace)[0]))
        # 3) drapeau SANS trace → anomalie
        trace.unlink()
        cas.append(("drapeau sans trace → ANOMALIE", not controler([flag], trace)[0]))
        # 4) trace POSTÉRIEURE au drapeau → anomalie (une trace après coup n'autorise rien)
        import time as _t
        _t.sleep(1.1)
        ts_apres = datetime.now(timezone.utc).strftime(JOUR)
        trace.write_text(json.dumps({"ts": ts_apres, "go": "après coup", "motif": "x"}),
                         encoding="utf-8")
        cas.append(("trace postérieure à l'acte → ANOMALIE (leçon R20.1)", not controler([flag], trace)[0]))
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  -> {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} ({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


if __name__ == "__main__":
    sys.exit(main())
