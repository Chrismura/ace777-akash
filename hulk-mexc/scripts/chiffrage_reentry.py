#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE REENTRY + RUNS v2 (20/10/2026, Buffy)
===============================================
GO Christophe 20/10 : « tu as fait des tests ici ? » — v1 a prouve qu'une attribution
sans comptabilite cash ment : retirer des achats sans rendre le cash non-depense
donne OFF=-462 $ (absurde). Ici COMPTABILITE COMPLETE : richesse = -achats + ventes
+ terminal. Chaque dollar non depense RESTE du cash.

Lots FIFO avec mouvements exacts (core_trend deplace, house/cons vident, dca_rebuy
remplace) — meme moteur que chiffrage_attribution.py (valide a 2,56 $).
Regime porte par les lots -> PnL par regime d'entree.

Variantes : BASE / OFF (29 achats reentry sautes) / DEEP10 (dd>=10 gardes) /
DEEP12 (dd>=12 gardes). Mur intestable (0 wall= dans les motifs reentry).

Validation : qty baseline vs state (<0,05) ET realise attribue vs CSV (<3 $).
Limite 1er ordre : pas de re-deploiement du cash libere (majorant si cash dort,
minorant s'il est redeploye en bull). Lecture seule. 0 E.
"""
import csv, glob, json, os, re, sys
from collections import defaultdict, deque
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(SCRIPTS, "..", "runs")
FEE = 0.0005 + float(os.environ.get("REPLAY_SLIP_BPS", "0")) / 10000.0

def dernier_csv():
    return sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)[-1]

def dd_of(reason):
    m = re.search(r"dd=([\d.]+)", reason or "")
    return float(m.group(1)) if m else None

def keep_buy(reason, mode):
    if "reentry_dump" not in (reason or ""):
        return True
    if mode == "OFF":
        return False
    dd = dd_of(reason)
    if dd is None:
        return True
    if mode == "DEEP10":
        return dd >= 10.0
    if mode == "DEEP12":
        return dd >= 12.0
    return True

def replay(mode):
    rows = list(csv.DictReader(open(dernier_csv(), newline="", encoding="utf-8-sig")))
    pos = defaultdict(float); bag = defaultdict(float); cons = defaultdict(float)
    lots_p = defaultdict(deque); lots_b = defaultdict(deque)
    cash = 0.0; attr = 0.0; csvp = 0.0; n_skip = 0
    last_px = {}
    reg = defaultdict(lambda: [0.0, 0])
    for r in rows:
        ev = (r.get("event") or "").strip(); p = (r.get("pair") or "").strip()
        if not p:
            continue
        try: px = float(r.get("price") or 0)
        except: continue
        if px > 0:
            last_px[p] = px
        if ev == "SKIP":
            continue
        try: q = float(r.get("qty") or 0)
        except: continue
        note = r.get("reason") or ""; rg = (r.get("regime") or "?").strip()
        if ev in ("BUY", "GBAG_PYRAMIDE"):
            if keep_buy(note, mode):
                pos[p] += q; cash -= q * px
                lots_p[p].append([q, px, rg])
            else:
                n_skip += 1
        elif ev == "GBAG_SOUCHE":
            bag[p] += q; cash -= q * px
            lots_b[p].append([q, px, "souche"])
        elif ev == "BAG_DCA":
            cash -= q * px
            if "trend_" in note:
                pos[p] += q; lots_p[p].append([q, px, rg])
            else:
                bag[p] = q; lots_b[p] = deque([[q, px, rg]])
        elif ev == "BAG_ARM":
            if "core_trend" in note:
                mv = min(q, pos[p]); pos[p] -= mv; bag[p] = mv
                rest = mv
                while rest > 1e-12 and lots_p[p]:
                    take = min(lots_p[p][0][0], rest); l = lots_p[p][0]
                    lots_b[p].append([take, l[1], l[2]])
                    l[0] -= take; rest -= take
                    if l[0] <= 1e-12: lots_p[p].popleft()
            elif "house_half" in note:
                bag[p] = q; pos[p] = 0.0
                lots_b[p] = deque([[q, px, "stake_keep"]]); lots_p[p] = deque()
            elif "conservation_half" in note:
                cons[p] = q; pos[p] = 0.0; lots_p[p] = deque()
        elif ev in ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH"):
            try: csvp += float(r.get("pnl_usdt") or 0)
            except: pass
            book = pos if ev in ("SELL", "SELL_PARTIAL") else bag
            lots = lots_p if ev in ("SELL", "SELL_PARTIAL") else lots_b
            vente = min(q, book[p]); book[p] -= vente
            cash += vente * px * (1.0 - FEE)
            rest = vente; L = lots[p]
            while rest > 1e-12 and L:
                take = min(L[0][0], rest)
                g = (px - L[0][1]) * take
                attr += g
                if mode == "BASE":
                    reg[L[0][2]][0] += g; reg[L[0][2]][1] += 1
                L[0][0] -= take; rest -= take
                if L[0][0] <= 1e-12: L.popleft()
    terminal = {p: (pos[p] + bag[p] + cons[p]) * last_px.get(p, 0.0)
                for p in set(list(pos) + list(bag) + list(cons))}
    wealth = cash + sum(terminal.values())
    return wealth, cash, terminal, n_skip, reg, attr, csvp, {p: pos[p] + bag[p] + cons[p] for p in terminal}

def main():
    st = json.load(open(os.path.join(RUNS, "PAPER_V1_20261018_100103_state.json"), encoding="utf-8"))
    decal = defaultdict(float)
    for k in ("positions", "bags", "conservation", "bag_dca"):
        for pa, v in (st.get(k) or {}).items():
            if isinstance(v, dict): decal[pa] += float(v.get("qty") or 0)
    w0, c0, t0, _, reg, attr, csvp, qb = replay("BASE")
    mx = max((abs(qb.get(p, 0.0) - decal.get(p, 0.0)) for p in set(list(qb) + list(decal))), default=0.0)
    print(f"VALIDATION qty={mx:.4f} (<0,05) | attribue={attr:.2f} vs csv={csvp:.2f} (attendu ~+2,5 comme attribution v1)")
    if mx > 0.05:
        print("STOP"); return 2
    print(f"\nBASE richesse={w0:.2f} (cash={c0:.2f} terminal={sum(t0.values()):.2f})")
    print(f"{'variante':<8}{'richesse':>10}{'delta':>10}  skips")
    res = {}
    for mode in ("OFF", "DEEP10", "DEEP12"):
        w, c, t, ns, _, _, _, _ = replay(mode)
        print(f"{mode:<8}{w:>10.2f}{w - w0:>+10.2f}  {ns}")
        res[mode] = round(w - w0, 2)
    print("\n=== PnL par REGIME d'entree (BASE, FIFO exact) ===")
    for rg, (v, n) in sorted(reg.items(), key=lambda kv: -kv[1][0]):
        print(f"  {rg:<14} {v:>+9.2f}$  n={n:<4} /lot={v/max(n,1):+7.3f}")
    json.dump({"wealth_base": round(w0, 2), "deltas": res,
               "regimes": {k: [round(v[0], 2), v[1]] for k, v in reg.items()}},
              open(os.path.join(RUNS, "CHIFFRAGE_REENTRY.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\n-> runs/CHIFFRAGE_REENTRY.json")
    return 0

if __name__ == "__main__":
    sys.exit(main())
