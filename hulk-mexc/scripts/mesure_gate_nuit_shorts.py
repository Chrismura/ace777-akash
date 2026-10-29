#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesure_gate_nuit_shorts.py — le gate 08-17h UTC est-il une règle inventée ? (29/10/2026, GO Christophe)

Question falsifiable : les signaux d'entrée (corr ≤ -0,50, frais) paient-ils
moins la NUIT que le JOUR ? Si nuit ≈ jour → le gate est une règle fixe
(R17) → on le tue et on le remplace par du mesuré.
Données : runs/short_{btc,eth,xrp}_signaux.jsonl (15 857 signaux, 31/08→29/10).
Issue : rendement forward du prix logged, +4 h et +24 h (même source, pas d'externe).
LECTURE SEULE. Sortie : stdout + /tmp/GATE_NUIT.json.
"""
import json
from datetime import datetime
from pathlib import Path

RUNS = Path(__file__).resolve().parents[1] / "runs"
SEUIL_CORR = -0.50
SEUIL_HIT = -0.3  # même seuil que justesse (move adverse au short)


def charger(sym):
    rows = []
    p = RUNS / f"short_{sym}_signaux.jsonl"
    try:
        for l in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            if not l.strip():
                continue
            try:
                rows.append(json.loads(l))
            except Exception:
                pass
    except FileNotFoundError:
        pass
    # tri temporel (fichiers append-only mais on ne suppose rien)
    def _ts(r):
        try:
            return datetime.fromisoformat(r.get("ts")).timestamp()
        except Exception:
            return 0
    rows.sort(key=_ts)
    return rows


def serie_prix(rows):
    pts = []
    for r in rows:
        try:
            ts = datetime.fromisoformat(r.get("ts")).timestamp()
            px = float(r.get("prix_btc"))
        except (TypeError, ValueError, AttributeError):
            continue
        if px > 0:
            pts.append((ts, px))
    return pts


def prix_a(pts, ts):
    best = None
    for t, p in pts:
        if t <= ts:
            best = p
        else:
            break
    return best


def mesurer(sym):
    rows = charger(sym)
    pts = serie_prix(rows)
    jour = {"n": 0, "hit4": 0, "ret4": [], "hit24": 0, "ret24": []}
    nuit = {"n": 0, "hit4": 0, "ret4": [], "hit24": 0, "ret24": []}
    for r in rows:
        try:
            c = r.get("corr_dir_btc")
            if c is None or float(c) > SEUIL_CORR:
                continue
            if not r.get("frais"):
                continue
            ts = datetime.fromisoformat(r.get("ts")).timestamp()
        except (TypeError, ValueError, AttributeError):
            continue
        hr = datetime.fromtimestamp(ts, tz=datetime.now().astimezone().tzinfo).hour
        # heure UTC (les ts sont ISO +00:00)
        try:
            hr = datetime.fromisoformat(r.get("ts")).hour
        except Exception:
            pass
        p0 = prix_a(pts, ts)
        if not p0:
            continue
        if not pts or ts + 24 * 3600 > pts[-1][0]:
            continue  # horizon +24h non couvert → pas de verdict partiel
        is_jour = 8 <= hr < 17
        dest = jour if is_jour else nuit
        for h, kh, kr in ((4, "hit4", "ret4"), (24, "hit24", "ret24")):
            p1 = prix_a(pts, ts + h * 3600)
            if not p1:
                continue
            move = 100.0 * (p1 / p0 - 1)
            dest[kr].append(round(move, 3))
            if move <= SEUIL_HIT:
                dest[kh] += 1
        dest["n"] += 1
    def resume(d):
        import statistics as s
        out = {"n": d["n"]}
        for h in (4, 24):
            rets = d[f"ret{h}"]
            out[f"hit{h}"] = d[f"hit{h}"]
            out[f"hit_pct{h}"] = round(100.0 * d[f"hit{h}"] / len(rets), 1) if rets else None
            out[f"ret_med{h}"] = round(s.median(rets), 3) if rets else None
            out[f"ret_moy{h}"] = round(s.mean(rets), 3) if rets else None
        return out
    return {"sym": sym, "n_signaux": len(rows), "jour": resume(jour), "nuit": resume(nuit)}


def main():
    res = {s: mesurer(s) for s in ("btc", "eth", "xrp")}
    Path("/tmp/GATE_NUIT.json").write_text(json.dumps(res, ensure_ascii=False, indent=1),
                                           encoding="utf-8")
    for s, r in res.items():
        print(f"### {s.upper()} ({r['n_signaux']} signaux)")
        for per in ("jour", "nuit"):
            d = r[per]
            print(f"  {per}: n={d['n']} | +4h hit={d['hit_pct4']}% méd={d['ret_med4']}% "
                  f"| +24h hit={d['hit_pct24']}% méd={d['ret_med24']}%")
    # verdict
    for s, r in res.items():
        j, n = r["jour"], r["nuit"]
        if j["n"] >= 5 and n["n"] >= 5 and j["ret_med24"] is not None and n["ret_med24"] is not None:
            ecart = round(n["ret_med24"] - j["ret_med24"], 3)
            print(f"VERDICT {s}: écart nuit-jour médian +24h = {ecart}pt "
                  f"(négatif = la nuit paie PLUS pour un short)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
