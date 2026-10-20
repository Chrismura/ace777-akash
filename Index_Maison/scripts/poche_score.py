#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""poche_score.py — LE PROFESSEUR NOTE LES POCHES (chantier 20/10, GO Christophe).

Lecture seule des avis émis par poche_avis.py + mouvements réalisés (klines
MEXC daily). Même règle que score_justesse v2 : HIT = bon sens ET |move| >=
seuil_move de LA PAIRE ; NEUTRE + marché qui bouge = MISS (pas d'échappatoire).

Usage :
  python3 poche_score.py              # note tous les avis échus (>24h)
Sortie : Index_Maison/thermo/poche_score.json
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations
import glob, json, sys, urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
THERMO = RACINE / "Index_Maison" / "thermo"
OUT = THERMO / "poche_score.json"


def klines(sym: str, limit: int = 200) -> dict[str, float]:
    url = f"https://api.mexc.com/api/v3/klines?symbol={sym}&interval=1d&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "poche-score/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.loads(r.read())
    return {datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc).strftime("%Y-%m-%d"): float(k[4])
            for k in data}


def main() -> int:
    lignes = []
    for f in sorted(glob.glob(str(THERMO / "analyses_poche" / "*.jsonl"))):
        for ligne in open(f, encoding="utf-8"):
            try:
                lignes.append(json.loads(ligne))
            except Exception:
                continue
    px = {}
    for sym in {l.get("pair") for l in lignes if l.get("pair")}:
        try:
            px[sym] = klines(sym)
        except Exception as e:
            print(f"[poche_score] klines {sym} HS : {e}", file=sys.stderr)
    now = datetime.now(timezone.utc)
    brier_scores: dict = {}
    # GO A (20/10) — BRIER (ForecastBench) : (proba - outcome)^2 par avis échu.
    # Événement = celui annoncé par l'avis (rebond / retombée / calme). Baseline
    # hasard = 0.25 (proba 0.5 constante). Skill = 1 - brier/0.25 (>0 = mieux).
    res: dict = {"ts": now.isoformat(), "brier_global": None, "skill_vs_hasard": None,
                 "paires": {}}
    for sym, closes in px.items():
        hit = miss = 0
        details = []
        for l in lignes:
            if l.get("pair") != sym:
                continue
            try:
                t = datetime.fromisoformat(l["ts"])
            except Exception:
                continue
            if (now - t) < timedelta(hours=24):
                continue  # pas échu
            j0, j1 = t.strftime("%Y-%m-%d"), (t + timedelta(days=1)).strftime("%Y-%m-%d")
            if j0 not in closes or j1 not in closes:
                continue
            mv = (closes[j1] / closes[j0] - 1) * 100
            a = l.get("avis")
            seuil = float(l.get("seuil_move") or 0.3)
            bouge = abs(mv) >= seuil
            bon = (mv > 0 and a == "LONG") or (mv < 0 and a == "SHORT")
            if a == "NEUTRE":
                ok = not bouge
                outcome = 1.0 if not bouge else 0.0  # événement = calme annoncé
            else:
                ok = bon and bouge
                outcome = 1.0 if ok else 0.0  # événement = rebond/retombée annoncé
            hit, miss = hit + ok, miss + (not ok)
            p = float(l.get("proba", 0.5))
            brier_scores.setdefault(sym, []).append(round((p - outcome) ** 2, 4))
            details.append({"ts": l["ts"], "avis": a, "move": round(mv, 2),
                            "proba": p, "outcome": outcome, "ok": ok})
        n = hit + miss
        import statistics as _st
        _br = [x for x in (brier_scores.get(sym) or [])]
        _bm = round(_st.mean(_br), 4) if _br else None
        res["paires"][sym] = {"n": n, "hit": hit,
                              "pct": round(100 * hit / n, 1) if n else 0.0,
                              "brier": _bm,
                              "skill_vs_hasard": round(1 - _bm / 0.25, 3) if _bm is not None else None,
                              "details": details[-30:]}
    import statistics as _st2
    _all = [b for v in brier_scores.values() for b in v]
    if _all:
        res["brier_global"] = round(_st2.mean(_all), 4)
        res["skill_vs_hasard"] = round(1 - res["brier_global"] / 0.25, 3)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: {kk: v[kk] for kk in ("n", "hit", "pct")} for k, v in res["paires"].items()},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
