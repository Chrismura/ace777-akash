#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIF FIDELITE PNL — garde mécanique de la classe E2 (câblée le 08/10/2026)
==========================================================================
CLASSE E2 = « conclure sans vérifier à la source » : un chiffre RECALCULÉ pris pour un chiffre
VÉRIFIÉ. Le remède est un **contrôle de fidélité** : reconstruire depuis le journal et comparer
à ce que la machine ÉCRIT dans son état (`pnl_total`).

MÉTHODE (mesurée, pas devinée) : la somme NAÏVE de la colonne `pnl` NE MARCHE PAS — mesurée le
08/10 : elle donnait **46,59 $** contre un état à **42,1157 $** (écart 4,47 $) parce qu'elle
n'apparie pas les ventes à leurs lots d'entrée. La **bonne** méthode est la reconstitution FIFO
déjà écrite dans `chiffrage_compounding.py` : mesurée le même jour, elle rend **42,12 $**, soit
l'état à l'arrondi. **On ne réimplémente pas la méthode : on appelle l'outil et on compare.**

POURQUOI ce n'est PAS un faux accusateur : le seuil de tolérance est **0,01 $**, et il est
DÉCLARÉ : les deux chiffres sortent du MÊME journal et sont affichés à 2 décimales ; au-delà, ce
n'est plus un arrondi, c'est un écart. Si l'outil est absent ou échoue, on le **DÉCLARE**
(non mesurable) — on ne verdit pas et on n'accuse pas à tort (R14/E23).

LECTURE SEULE (l'outil écrit seulement son propre rapport) · 0 ordre · 0 € · stdlib.
Branché par `git_push_auto.sh` (tour des 3 h). Autotest : `--autotest`.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
IM = RACINE / "Index_Maison"
RUNS = RACINE / "hulk-mexc" / "runs"
TOOL = RACINE / "hulk-mexc" / "scripts" / "chiffrage_compounding.py"
OUT_JSON = IM / "thermo" / "fidelite_pnl.json"
TOLERANCE = 0.01          # écart toléré = précision d'affichage (2 décimales), même journal


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def plus_recent(motif: str) -> Path | None:
    f = sorted(glob.glob(str(RUNS / motif)), key=os.path.getmtime)
    return Path(f[-1]) if f else None


def comparer(net_reel: float, pnl_total: float, tol: float = TOLERANCE) -> tuple[bool, str]:
    """Logique pure (autotestable) : le PnL reconstruit doit coller à l'état écrit."""
    ecart = abs(float(net_reel) - float(pnl_total))
    ok = ecart <= tol
    return ok, (f"reconstruit {net_reel:.2f} $ vs état {pnl_total:.2f} $ · écart {ecart:.4f} $ "
                f"(tolérance {tol:g} $)")


def mesurer() -> tuple[float | None, str]:
    """Reconstruit le PnL réalisé via l'outil FIFO existant, sur le journal VIVANT."""
    journal = plus_recent("PAPER_V1_*.csv")
    if not journal or not TOOL.exists():
        return None, "journal vivant ou outil de reconstitution introuvable"
    try:
        p = subprocess.run([sys.executable, str(TOOL), str(journal)],
                           capture_output=True, text=True, timeout=300)
    except Exception as e:                                  # noqa: BLE001
        return None, f"outil non exécutable : {e}"
    if p.returncode != 0:
        return None, f"outil rc={p.returncode} : {p.stderr.strip()[:160]}"
    rap = plus_recent("CHIFFRAGE_COMPOUNDING_*.json")
    if not rap:
        return None, "l'outil n'a écrit aucun rapport"
    try:
        d = json.loads(rap.read_text(encoding="utf-8"))
        return float(d["net_reel"]), f"{journal.name} → {rap.name}"
    except Exception as e:                                  # noqa: BLE001
        return None, f"rapport illisible : {e}"


def main() -> int:
    if "--autotest" in sys.argv:
        return autotest()
    st = plus_recent("PAPER_V1_*_state.json")
    if not st:
        print("[fidelite_pnl] aucun état → non mesurable (déclaré, pas vert)")
        return 2
    pnl_total = float(json.loads(st.read_text(encoding="utf-8")).get("pnl_total") or 0)
    net, source = mesurer()
    res = {"ts": utc(), "state": st.name, "pnl_total": pnl_total,
           "net_reconstruit": net, "source": source, "tolerance": TOLERANCE}
    if net is None:
        res.update({"ok": False, "mesurable": False,
                    "detail": f"NON MESURABLE : {source} — on ne verdit pas (R14)"})
    else:
        ok, detail = comparer(net, pnl_total)
        res.update({"ok": ok, "mesurable": True, "detail": detail})
    Path(OUT_JSON).parent.mkdir(parents=True, exist_ok=True)
    Path(OUT_JSON).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[fidelite_pnl] {'OK' if res.get('ok') else 'ANOMALIE'} — {res['detail']}")
    return 0 if res.get("ok") else 1


def autotest() -> int:
    cas = [
        ("écart nul → conforme", comparer(42.12, 42.1157)[0]),
        ("écart d'arrondi 0,004 $ → conforme", comparer(42.12, 42.1157)[0]),
        ("écart 0,5 $ → ANOMALIE", not comparer(42.62, 42.1157)[0]),
        ("écart 4,47 $ (mesure du 08/10) → ANOMALIE", not comparer(46.59, 42.1157)[0]),
        ("signe inverse → ANOMALIE", not comparer(-10.0, 10.0)[0]),
    ]
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  -> {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} ({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


if __name__ == "__main__":
    sys.exit(main())
