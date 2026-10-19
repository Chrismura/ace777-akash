#!/usr/bin/env python3
"""verdict_marche_maths.py — VERDICT DÉTERMINISTE (GO Christophe 18/10 « câble tout »).

Le LLM ne décide plus LONG/SHORT/NEUTRE : il COMMENTE le verdict calculé ici.
Règle calibrée sur history.jsonl le 18/10 (horizon 24h, seuil 0,3 %) :
  chg24 <= seuil_long   → LONG   (contrarian)
  chg24 >= seuil_short  → SHORT
  sinon                 → NEUTRE (bande mesurée, pas un refuge)
R17 : seuils = quantiles q20/q80 du chg24 historique — jamais choisis.
Walk-forward (méthode RALPH/CPCV 18/10) : --calibrer découpe en jours, purge +
embargo autour des jours de test, calibre sur le reste et juge hors-échantillon.
In-sample ≠ promesse : le verdict est jugé comme les avis (score_justesse).

Usage :
  python3 verdict_marche_maths.py --chg24 -1.2        # → LONG
  python3 verdict_marche_maths.py --calibrer           # in-sample + walk-forward
  python3 verdict_marche_maths.py --calibrer --appliquer
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations

import argparse
import bisect
import datetime
import json
import statistics
import sys
from pathlib import Path

THERMO = Path(__file__).resolve().parents[1] / "thermo"
HISTORY = THERMO / "history.jsonl"

PARAMS = {
    "feature": "chg24",
    "seuil_long": -0.96,   # chg24 <= seuil → LONG
    "seuil_short": 1.88,   # chg24 >= seuil → SHORT
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


def _charger() -> list:
    px = []
    for ln in HISTORY.open(encoding="utf-8"):
        try:
            d = json.loads(ln)
            px.append((float(d["tsUnix"]), float(d["mark"]), float(d.get("chg24") or 0.0)))
        except Exception:
            continue
    px.sort()
    return px


def _fut(px: list, ts: list, t: float, h: int = 86400):
    i = bisect.bisect_right(ts, t) - 1
    j = bisect.bisect_right(ts, t + h) - 1
    if i < 0 or j < 0:
        return None
    return (px[j][1] / px[i][1] - 1) * 100


def walk_forward(px: list, plis: int = 5, embargo_j: int = 1) -> dict:
    """CPCV simplifié (RALPH 18/10) : jours groupés, purge+embargo autour du test.

    Chaque pli = 1/5 des jours en test ; l'entraînement exclut les jours de test
    ET leurs voisins (embargo) pour casser la fuite de corrélation sérielle.
    Seuils recalibrés sur le train seul, jugés sur le test seul.
    """
    jours: dict[str, list] = {}
    for t, mark, chg in px:
        jour = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%d")
        jours.setdefault(jour, []).append((t, mark, chg))
    cles = sorted(jours)
    ts = [p[0] for p in px]
    hits = sigs = 0
    detail = []
    for k in range(plis):
        test_idx = set(range(k, len(cles), plis))
        test_jours = {cles[i] for i in test_idx}
        ban = set()
        for i in test_idx:
            for d in range(i - embargo_j, i + embargo_j + 1):
                if 0 <= d < len(cles):
                    ban.add(cles[d])
        train = [v for j, vs in jours.items() if j not in ban for v in vs]
        test = [v for j, vs in jours.items() if j in test_jours for v in vs]
        if len(train) < 200 or len(test) < 50:
            continue
        chgs = sorted(v[2] for v in train)
        lo, hi = chgs[int(len(chgs) * 0.2)], chgs[int(len(chgs) * 0.8)]
        h = n = 0
        for t, _, c in test:
            m = _fut(px, ts, t)
            if m is None:
                continue
            sig = "LONG" if c <= lo else ("SHORT" if c >= hi else None)
            if sig is None:
                continue
            n += 1
            if (m > 0.3 and sig == "LONG") or (m < -0.3 and sig == "SHORT"):
                h += 1
        if n:
            hits += h
            sigs += n
            detail.append({"pli": k, "hit": round(h / n, 3), "n": n,
                           "lo": round(lo, 2), "hi": round(hi, 2)})
    return {"hit_oos": round(hits / sigs, 3) if sigs else None,
            "n_oos": sigs, "plis": detail}


def calibrer(appliquer: bool = False) -> int:
    px = _charger()
    ts = [p[0] for p in px]
    vals = [(c, _fut(px, ts, t)) for t, _, c in px[::10]]
    vals = [(c, m) for c, m in vals if m is not None]
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
    print(f"[calibrage] IN-SAMPLE : lo={lo:.2f} hi={hi:.2f} hit={h/n:.3f} sur {n} signaux (n={len(vals)})")
    wf = walk_forward(px)
    print(f"[calibrage] WALK-FORWARD (purge+embargo 1j, {len(wf['plis'])} plis) : "
          f"hit HORS-ÉCHANTILLON={wf['hit_oos']} sur {wf['n_oos']} signaux")
    for p in wf["plis"]:
        print(f"   pli {p['pli']} : hit={p['hit']} n={p['n']} (lo={p['lo']} hi={p['hi']})")
    gap = (h / n) - (wf["hit_oos"] or 0)
    print(f"[calibrage] écart in-sample − hors-échantillon = {gap:+.3f} "
          f"({'SUR-OPTIMISÉ' if gap > 0.10 else 'tenable'})")
    if appliquer:
        PARAMS["seuil_long"] = round(lo, 2)
        PARAMS["seuil_short"] = round(hi, 2)
        PARAMS["calibre_le"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        PARAMS["hit_insample"] = round(h / n, 3)
        PARAMS["n_signaux"] = n
        PARAMS["hit_oos"] = wf["hit_oos"]
        PARAMS["n_oos"] = wf["n_oos"]
        import re
        src = Path(__file__).read_text(encoding="utf-8")
        # Ancré ^ {4} : ne touche QUE le bloc PARAMS, jamais ces propres lignes
        # (leçon 18/10 : regex non ancrée = le serpent se mord la queue).
        src = re.sub(r'(?m)^    "seuil_long": [^,]+,',
                      f'    "seuil_long": {PARAMS["seuil_long"]},', src)
        src = re.sub(r'(?m)^    "seuil_short": [^,]+,',
                      f'    "seuil_short": {PARAMS["seuil_short"]},', src)
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
