#!/usr/bin/env python3
"""verdict_marche_maths.py — VERDICT DÉTERMINISTE (GO Christophe 18/10 « câble tout »).

Le LLM ne décide plus LONG/SHORT/NEUTRE : il COMMENTE le verdict calculé ici.
Règle calibrée sur history.jsonl le 18/10 (n≈1 943 points, horizon 24h, seuil 0,3 %) :
  chg24 <= -0.96  → LONG   (contrarian, hit 63,5 % in-sample sur 780 signaux)
  chg24 >= +1.78  → SHORT
  sinon           → NEUTRE (bande mesurée, pas un refuge)
R17 : seuils = quantiles q20/q80 du chg24 historique — jamais choisis.
  --calibrer les recalcule (provenance écrite dans PARAMS).
In-sample ≠ promesse : le verdict est jugé comme les avis (score_justesse).

Usage :
  python3 verdict_marche_maths.py --chg24 -1.2        # → LONG
  python3 verdict_marche_maths.py --calibrer           # recalcule seuils + affiche
  python3 verdict_marche_maths.py --calibrer --appliquer
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations

import argparse
import bisect
import json
import statistics
import sys
from pathlib import Path

THERMO = Path(__file__).resolve().parents[1] / "thermo"
HISTORY = THERMO / "history.jsonl"

PARAMS = {
    "feature": "chg24",
    "seuil_long": -0.96,   # chg24 <= seuil → LONG
    "seuil_short": 1.78,   # chg24 >= seuil → SHORT
    "horizon": "24h",
    "seuil_move_pct": 0.3,
    "calibre_le": "2026-10-18",
    "n_points": 1943,
    "hit_insample": 0.635,
    "n_signaux": 780,
    "methode": "quantiles q20/q80 du chg24 sur history.jsonl (pas de choix humain)",
}


def verdict(chg24: float | None) -> dict:
    """Verdict déterministe. chg24=None → NEUTRE (donnée absente, jamais inventée)."""
    if chg24 is None:
        return {"verdict": "NEUTRE", "motif": "chg24 absent"}
    try:
        v = float(chg24)
    except (TypeError, ValueError):
        return {"verdict": "NEUTRE", "motif": "chg24 illisible"}
    if v <= PARAMS["seuil_long"]:
        return {"verdict": "LONG", "motif": f"chg24={v:.2f} <= {PARAMS['seuil_long']} (contrarian calibré)"}
    if v >= PARAMS["seuil_short"]:
        return {"verdict": "SHORT", "motif": f"chg24={v:.2f} >= {PARAMS['seuil_short']} (contrarian calibré)"}
    return {"verdict": "NEUTRE", "motif": f"chg24={v:.2f} dans la bande [{PARAMS['seuil_long']}, {PARAMS['seuil_short']}]"}


def calibrer(appliquer: bool = False) -> int:
    px = []
    for ln in HISTORY.open(encoding="utf-8"):
        try:
            d = json.loads(ln)
            px.append((float(d["tsUnix"]), float(d["mark"]), float(d.get("chg24") or 0.0)))
        except Exception:
            continue
    px.sort()
    ts = [p[0] for p in px]

    def fut(t: float, h: int = 86400):
        i = bisect.bisect_right(ts, t) - 1
        j = bisect.bisect_right(ts, t + h) - 1
        if i < 0 or j < 0:
            return None
        return (px[j][1] / px[i][1] - 1) * 100

    vals = [(c, fut(t)) for t, _, c in px[::10] if fut(t) is not None]
    chgs = sorted(v for v, _ in vals)
    lo, hi = chgs[int(len(chgs) * 0.2)], chgs[int(len(chgs) * 0.8)]
    h = n = 0
    for v, m in vals:
        sig = "LONG" if v <= lo else ("SHORT" if v >= hi else None)
        if sig is None:
            continue
        n += 1
        if (m > 0.3 and sig == "LONG") or (m < -0.3 and sig == "SHORT"):
            h += 1
    print(f"[calibrage] n={len(vals)} lo={lo:.2f} hi={hi:.2f} hit={h/n:.3f} sur {n} signaux")
    if appliquer:
        PARAMS["seuil_long"] = round(lo, 2)
        PARAMS["seuil_short"] = round(hi, 2)
        PARAMS["calibre_le"] = __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%d")
        PARAMS["hit_insample"] = round(h / n, 3)
        PARAMS["n_signaux"] = n
        src = Path(__file__).read_text(encoding="utf-8")
        import re
        src = re.sub(r'"seuil_long": [^,]+', f'"seuil_long": {PARAMS["seuil_long"]}', src)
        src = re.sub(r'"seuil_short": [^,]+', f'"seuil_short": {PARAMS["seuil_short"]}', src)
        Path(__file__).write_text(src, encoding="utf-8")
        print("[calibrage] ÉCRIT dans PARAMS (re-jouer les preuves après)")
    else:
        print("[calibrage] DRY-RUN — rien d'écrit (--appliquer pour écrire)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chg24", type=float, default=None)
    ap.add_argument("--calibrer", action="store_true")
    ap.add_argument("--appliquer", action="store_true")
    args = ap.parse_args()
    if args.calibrer:
        return calibrer(args.appliquer)
    print(json.dumps(verdict(args.chg24), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
