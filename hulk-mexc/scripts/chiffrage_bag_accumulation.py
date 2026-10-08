#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_BAG_ACCUMULATION.py — « faire GROSSIR le bag » : est-ce que re-entrer après
une sortie et parquer une NOUVELLE SOUCHE à chaque cycle rapporte plus que de rester
avec une seule souche ?

QUESTION (Christophe, 08/10/2026) : « trouve la meilleure logique pour AUGMENTER le bag »,
et décision explicite : MESURER l'accumulation de souche AVANT de la câbler.

MÉTHODE (conventions maison) :
  - entrées = les VRAIS achats du journal PAPER_V1 le plus récent (mêmes entrées pour A/C/D).
  - prix réels : klines 1h MEXC (cache runs/replay_cache).
  - fenêtre longue (168 h = 7 j) pour laisser le temps aux CYCLES (sortie → re-entrée).
  - amp7 + trend en walk-forward (aucune donnée du futur).

  A  ACTUEL      : paliers rip fixes + 2× + giveback 4 % + bag crash/slow fixes.
  C  TREND (câblé): 3 tranches amplitude + souche intouchable + trend (add/rebuy) — UN cycle.
  D  ACCUMULATION : comme C, MAIS quand le tradable est soldé, on RE-ENTRE au creux
                    (repli de REENTRY_AMP×amp sous la sortie) et on PARQUE une nouvelle
                    souche à chaque cycle → le bag GROSSIT en jetons.

SORTIE : $ (valeur finale / mise) + jetons finaux / jetons initiaux (bag), tout / 2 moitiés / par paire.
0 €, aucun ordre. Limites déclarées : ordre intra-bougie supposé favorable aux paliers ;
on modélise le réinvestissement du cash réalisé, sans cash externe.
"""
import os
import sys
import statistics as st

SRC = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SRC)
import chiffrage_bag_trend as M  # noqa: E402

HOLD_H = 168          # 7 jours
REENTRY_AMP = 0.5     # re-entrée si le prix redescend de 0.5×amp sous la sortie


def params(trend, pair):
    return M.strat_C(trend, pair)


def sim_accum(bars, t0, entry0, amp, trend, p):
    """A/C-style rules + re-entrée + SOUCHE ACCUMULÉE à chaque cycle."""
    apres = [b for b in bars if b["t"] > t0][:HOLD_H]
    if not apres:
        return None
    core_frac = float(p.get("core_frac", 0.0))
    stop_mult = 1.5
    core = 0.0            # jetons accumulés (fraction de la qty initiale)
    cash = 0.0            # produits, en unités de valeur initiale
    entry = entry0
    work = 1.0 - core_frac
    core += core_frac
    peak = entry0
    rip_step = 0
    cycles = 1
    waiting = False
    last_exit = entry0
    if trend == "haussier":
        p1, p2, frac, gb, add = p["ladder"][0][0][1], p["ladder"][1][0][1], p["ladder"][0][1], p["gb_expr"][1], p.get("add_expr", ("amp", 0))[1]
    elif trend == "baissier":
        p1, p2, frac, gb, add = p["ladder"][0][0][1], p["ladder"][1][0][1], p["ladder"][0][1], p["gb_expr"][1], p.get("rebuy_expr", ("amp", 0))[1]
    else:
        p1, p2, frac, gb, add = p["ladder"][0][0][1], p["ladder"][1][0][1], p["ladder"][0][1], p["gb_expr"][1], 0.0

    for b in apres:
        h, l, c = b["h"], b["l"], b["c"]
        if waiting:
            # re-entrée au creux : le cash RACHÈTE des jetons plus bas, nouvelle souche
            seuil = last_exit * (1.0 - REENTRY_AMP * amp / 100.0)
            if cash >= 1.0 and l <= seuil:
                px = min(l, seuil)
                tokens = cash * entry0 / px
                entry = px
                core += core_frac * tokens
                work = (1.0 - core_frac) * tokens
                cash = 0.0
                peak = px
                rip_step = 0
                waiting = False
                cycles += 1
            continue
        peak = max(peak, h)
        chg = (h / entry - 1.0) * 100.0
        # paliers
        nxt = p1 if rip_step == 0 else (p2 if rip_step == 1 else None)
        if nxt is not None and chg >= nxt * amp and work > 0:
            q = min((1.0 - core_frac) * frac, work)
            cash += q * (min(entry * (1 + nxt * amp / 100), h) / entry) * (1 - M.FEE)
            work -= q
            rip_step += 1
            continue
        # stop amplitude
        if work > 0 and l <= entry * (1.0 - stop_mult * amp / 100.0):
            cash += work * (entry * (1.0 - stop_mult * amp / 100.0) / entry) * (1 - M.FEE)
            work = 0
            last_exit = c
            waiting = True
            continue
        # trailing amplitude (armé si pic ≥ 1,0×amp)
        if work > 0 and (peak / entry - 1.0) * 100.0 >= amp:
            floor = peak * (1.0 - gb * amp / 100.0)
            if l <= floor:
                cash += work * (min(floor, peak) / entry) * (1 - M.FEE)
                work = 0
                last_exit = c
                waiting = True
    end_px = apres[-1]["c"]
    final_qty = core + work
    final_value = cash + (core + work) * (end_px / entry0) * (1 - M.FEE)
    return {"value_mult": final_value, "qty_growth": final_qty, "cycles": cycles,
            "mfe_pct": (max(b["h"] for b in apres) / entry0 - 1) * 100}


def main():
    M.HOLD_H = HOLD_H        # fenêtre ÉGALE pour A/C/D (sinon on compare des durées, pas des logiques)
    j = M.journal_le_plus_recent()
    entrees = M.lire_entrees(j)
    profils = M.load_profils()
    kl = {}
    res = []
    for e in entrees:
        p = e["pair"]
        if p not in kl:
            kl[p] = M.fetch(p)
        bars = kl[p]
        if not bars:
            continue
        amp = M.amp7(bars, e["t"])
        if amp is None or amp <= 0 or amp < 7.0:      # gate amp≥7 % (décidé par la mesure)
            continue
        tr = M.trend_of(bars, e["t"], e["px"])
        sp = float(((profils.get(p) or {}).get("calib") or {}).get("stop_pct") or 10.0)
        row = {"pair": p, "t": e["t"], "amp": amp, "trend": tr, "notional": e["notional"]}
        ok = True
        for nom, fn in (("A", lambda t, p_: M.strat_A(t, p_)),
                        ("C", lambda t, p_: M.strat_C(t, p_))):
            r = M.simuler(bars, e["t"], e["px"], amp, tr, fn(tr, p), sp)
            if r is None:
                ok = False
                break
            row[nom] = r
        r = sim_accum(bars, e["t"], e["px"], amp, tr, params(tr, p))
        if r is None:
            ok = False
        if ok:
            row["D"] = r
            res.append(row)

    if not res:
        print("aucune entrée rejouable (amp>=7%) — on ne conclut pas")
        return 1

    notion = sum(x["notional"] for x in res)
    print("CHIFFRAGE ACCUMULATION DE SOUCHE — gate amp>=7 %, fenêtre 7 j")
    print(f"  entrées rejouées : {len(res)} · notionnel {notion:,.0f} $")
    print(f"  cycles moyens (D) : {st.mean([x['D']['cycles'] for x in res]):.2f}\n")

    def bloc(titre, v):
        n = sum(x["notional"] for x in v)
        print(f"  --- {titre} (n={len(v)}, {n:,.0f} $) ---")
        for k in ("A", "C", "D"):
            val = sum(x["notional"] * x[k]["value_mult"] for x in v)
            qty = sum(x["notional"] * x[k]["qty_growth"] for x in v)
            print(f"    {k:2s}  PnL {val-n:+8.2f} $ ({(val-n)/n*100:+.2f} %)  bag ×{qty/n:.3f}")
        dc = sum(x["notional"] * (x["D"]["value_mult"] - x["C"]["value_mult"]) for x in v)
        da = sum(x["notional"] * (x["D"]["value_mult"] - x["A"]["value_mult"]) for x in v)
        print(f"    → Δ D−C {dc:+8.2f} $ · Δ D−A {da:+8.2f} $")

    bloc("TOUT", res)
    res_t = sorted(res, key=lambda x: x["t"])
    cut = len(res_t) // 2
    print()
    bloc("1re MOITIÉ", res_t[:cut])
    print()
    bloc("2e MOITIÉ", res_t[cut:])

    par_p = {}
    for x in res:
        par_p.setdefault(x["pair"], []).append(x)
    print("\n  -- par paire (D−A en $ ; cycles moyens) --")
    for p in sorted(par_p, key=lambda k: -st.median([x["amp"] for x in par_p[k]])):
        v = par_p[p]
        n = sum(x["notional"] for x in v)
        a = sum(x["notional"] * x["A"]["value_mult"] for x in v)
        c = sum(x["notional"] * x["C"]["value_mult"] for x in v)
        d = sum(x["notional"] * x["D"]["value_mult"] for x in v)
        cyc = st.mean([x["D"]["cycles"] for x in v])
        print(f"    {p:12s} amp={st.median([x['amp'] for x in v]):5.1f}% n={len(v):2d} "
              f"cyc={cyc:4.1f}  A {a-n:+7.2f}$  C {c-n:+7.2f}$  D {d-n:+7.2f}$  (D−A {d-a:+7.2f}$)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
