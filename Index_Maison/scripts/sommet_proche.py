#!/usr/bin/env python3
"""Guetteur de sommet PROCHE — lecture seule, ne décide jamais.

Lit Index_Maison/thermo/history.jsonl (points ~6 min avec mark, funding,
longShort, topTraderLS, takerRatio) et chuchote quand :
  - cassure micro : mark sous le max des ~11 min précédentes (2 points)
  - + au moins 2 contextes chauds parmi : L/S élevé, funding élevé,
    pression vendeuse au taker.

Seuils ADAPTATIFS : calculés comme quantiles de l'historique chargé
(jamais de fixe déguisé — R17). Ce script ne trade pas, il LOGUE.
Sortie : Index_Maison/data/sommet_proche_hist.jsonl + live.
"""
import json
import os
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST = os.path.join(BASE, "thermo", "history.jsonl")
RACINE = os.path.dirname(BASE)  # ~/ace777-test-day1 : les runs/ L2 vivent ici
OUT_H = os.path.join(BASE, "data", "sommet_proche_hist.jsonl")
OUT_L = os.path.join(BASE, "data", "sommet_proche_live.json")

FEN_MICRO_SEC = 11 * 60  # ~11 min : 2 points à 6 min d'intervalle


def charger():
    rows = []
    try:
        with open(HIST, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                if r.get("tsUnix") is None or r.get("mark") is None:
                    continue
                rows.append(r)
    except FileNotFoundError:
        pass
    rows.sort(key=lambda r: float(r["tsUnix"]))
    return rows


def quantile(xs, q):
    if not xs:
        return None
    s = sorted(xs)
    i = min(len(s) - 1, max(0, int(q * len(s))))
    return s[i]


_CACHE_L2 = {}  # fnom -> liste (ts, bid) triée (un seul chargement/jour)


def _charger_l2(fnom):
    import csv as _csv
    if fnom in _CACHE_L2:
        return _CACHE_L2[fnom]
    vals = []
    try:
        with open(os.path.join(RACINE, "runs", fnom), encoding="utf-8") as fh:
            for r in _csv.DictReader(fh):
                try:
                    rt = datetime.fromisoformat(
                        str(r["ts"]).replace("Z", "+00:00")).timestamp()
                    vals.append((rt, float(r["bid1_sz"])))
                except Exception:
                    continue
    except Exception:
        pass
    vals.sort()
    _CACHE_L2[fnom] = vals
    return vals


def _med_bid(vals, t0, t1):
    import bisect as _bi
    lo = _bi.bisect_left(vals, (t0, float("-inf")))
    sel = sorted(v for (t, v) in vals[lo:] if t <= t1)
    if not sel:
        return None
    return sel[len(sel) // 2]


def liquidite_retiree(t_epoch):
    """Murs L2 : profondeur bid médiane sur [T-60min, T] vs même fenêtre
    la veille (runs/L2_YYYYMMDD_SNAPS.csv). Retourne (retiree?, pct).
    Fail-open : fichiers absents → (False, None)."""
    from datetime import timedelta as _td
    try:
        dt = datetime.fromtimestamp(t_epoch, timezone.utc)
        auj = dt.strftime("%Y%m%d")
        veille = (dt - _td(days=1)).strftime("%Y%m%d")
        m_auj = _med_bid(_charger_l2(f"L2_{auj}_SNAPS.csv"),
                         t_epoch - 3600, t_epoch)
        m_veil = _med_bid(_charger_l2(f"L2_{veille}_SNAPS.csv"),
                          t_epoch - 3600 - 86400, t_epoch - 86400)
        if m_auj is None or not m_veil:
            return False, None
        pct = 100.0 * (m_auj / m_veil - 1)
        return pct <= -30, round(pct, 1)
    except Exception:
        return False, None


def analyser(rows):
    # 1) distribution des mouvements micro sur tout l'historique
    moves = []
    for i, r in enumerate(rows):
        t = float(r["tsUnix"])
        px = float(r["mark"])
        prec = [float(x["mark"]) for x in rows[:i]
                if t - float(x["tsUnix"]) <= FEN_MICRO_SEC]
        if not prec:
            continue
        moves.append(100.0 * (px / max(prec) - 1))
    # seuil adaptatif : le pire décile des cassures micro observées
    seuil_drop = quantile([m for m in moves if m < 0], 0.5)  # médiane des baisses
    if seuil_drop is None or seuil_drop > -0.05:
        seuil_drop = -0.15  # garde-fou initial, re-mesuré à chaque run
    # contextes : quantiles hauts (funding chaud) + ANORMALITÉ vs régime
    # récent pour le L/S (un L/S qui chute vite = deleverage = signal,
    # même sous le quantile global — leçon du 29/10 16h).
    ls_vals = [float(r["longShort"]) for r in rows if r.get("longShort")]
    f_vals = [float(r["funding"]) for r in rows if r.get("funding") is not None]
    ls_chaud = quantile(ls_vals, 0.7) or 1.8
    f_chaud = quantile(f_vals, 0.7) or 0.00008

    chuchotements = []
    for i, r in enumerate(rows):
        t = float(r["tsUnix"])
        px = float(r["mark"])
        prec = [x for x in rows[:i] if t - float(x["tsUnix"]) <= FEN_MICRO_SEC]
        if not prec:
            continue
        haut = max(float(x["mark"]) for x in prec)
        drop = 100.0 * (px / haut - 1)
        ctx = []
        ls = r.get("longShort")
        if ls is not None and float(ls) >= ls_chaud:
            ctx.append(f"L/S {ls}≥{ls_chaud:.2f}")
        # deleverage : L/S en chute vs médiane des 2h précédentes
        prec_ls = [float(x["longShort"]) for x in rows[:i]
                   if t - float(x["tsUnix"]) <= 7200 and x.get("longShort")]
        if ls is not None and prec_ls:
            med = quantile(prec_ls, 0.5)
            if med and float(ls) <= med * 0.95:
                ctx.append(f"delev L/S {ls} vs méd {med:.2f} (−5%)")
        f = r.get("funding")
        if f is not None and float(f) >= f_chaud:
            ctx.append(f"funding {f}≥{f_chaud}")
        tr = r.get("takerRatio")
        if tr is not None and float(tr) < 0.5:
            ctx.append(f"taker {tr}<0.5 vendeur")
        # murs L2 : les teneurs de marché retirent la liquidité avant l'orage ?
        # (contexte dur : profondeur mesurée, pas une opinion)
        # Garde anti-bruit : passé −1,5 % sous le max du jour on n'est plus
        # « près du sommet » mais en pleine chute → silence (phase contagion,
        # pas rumeur : un chuchoteur qui crie pendant tout le crash ne sert
        # à rien et réveille l'orchestre pour rien).
        max24 = max(
            (float(x["mark"]) for x in rows[:i + 1]
             if t - float(x["tsUnix"]) <= 86400 and x.get("mark")),
            default=None)
        if max24 and px < max24 * 0.985:
            continue
        liq_out, liq_pct = liquidite_retiree(t)
        if liq_out:
            ctx.append(f"liquidité retirée {liq_pct}% vs veille (murs L2)")
        # gradué sans crier au loup : le deleverage (rare) suffit seul,
        # sinon il faut 2 contextes (le funding chaud seul = fond sonore).
        a_delev = any(c.startswith("delev") for c in ctx)
        chuchote = (drop <= seuil_drop) and (a_delev or len(ctx) >= 2)
        if chuchote:
            chuchotements.append({
                "ts": datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "tsUnix": t,
                "prix": px,
                "drop_micro_pct": round(drop, 3),
                "contextes": ctx,
                "seuil_drop": round(seuil_drop, 3),
            })
    meta = {"seuil_drop_mesure": round(seuil_drop, 3),
            "ls_chaud_q70": round(ls_chaud, 3),
            "funding_chaud_q70": f_chaud,
            "n_points": len(rows), "n_chuchotements": len(chuchotements)}
    return chuchotements, meta


def main():
    rows = charger()
    if not rows:
        print("pas d'historique", file=sys.stderr)
        return 1
    chuch, meta = analyser(rows)
    with open(OUT_H, "w", encoding="utf-8") as f:
        for c in chuch:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    live = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "meta": meta, "derniers": chuch[-5:]}
    with open(OUT_L, "w", encoding="utf-8") as f:
        json.dump(live, f, ensure_ascii=False, indent=1)
    print(f"points={meta['n_points']} seuil_drop={meta['seuil_drop_mesure']} "
          f"LS70={meta['ls_chaud_q70']} chuchotements={meta['n_chuchotements']}")
    for c in chuch:
        print(f"  🤫 {c['ts']} @ {c['prix']:.0f} drop {c['drop_micro_pct']}% | {'; '.join(c['contextes'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
