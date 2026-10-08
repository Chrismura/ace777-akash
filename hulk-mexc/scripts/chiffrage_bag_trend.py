#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_BAG_TREND.py — combien valent, EN DOLLARS, trois logiques de sortie/bag,
rejouées sur les VRAIS achats du moteur (aucune entrée inventée) ?

QUESTION (Christophe, 08/10/2026) :
  « pour le bag, il faut considérer le TREND : trend haussier = tenir plus de bag ;
    trend baissier = tout vendre et racheter plus bas. Trouve la meilleure logique
    pour AUGMENTER le bag. »

MÉTHODE (mêmes conventions que les chiffrages maison) :
  - entrées = les VRAIS événements BUY / BAG_DCA du journal PAPER_V1 le plus récent
    (ts, paire, prix, qty) — inchangés pour les 3 variantes.
  - prix réels : klines 1h MEXC (cache runs/replay_cache, fetch si périmé).
  - frais 5 bps/côté (10 bps aller-retour), tarif maison.
  - amplitude amp7 = range journalier MÉDIAN des 7 jours PRÉCÉDENTS l'entrée
    (walk-forward : aucune donnée du futur).
  - trend = calculé sur les bougies AVANT l'entrée (walk-forward) :
      SMA72 = moyenne des 72 clôtures avant l'entrée ;
      trend HAUSSIER si px > SMA72 ET SMA72 monte ; BAISSIER si px < SMA72 ET SMA72 baisse.

  A  ACTUEL     : paliers rip FIXES (+6 %/+8 %, 25 % chacun) + 2× (vend 50 % du reste)
                  + runner avec giveback FIXE 4 % + bag crash/slow FIXES (-20 %/-8 %).
  B  3 TRANCHES : paliers CALÉS sur amp7 (0,5×amp / 1,0×amp, 20 % chacun)
                  + runner trailing amplitude (arm 1,0×amp, giveback 0,4×amp)
                  + SOUCHE 20 % jamais vendue + bag crash/slow calés sur amp7.
  C  TREND+BAG  : comme B, MAIS le bag suit le trend :
                  - trend HAUSSIER : on vend MOINS (souche 30 %), pas de crash/slow,
                    on RACHÈTE sur les creux (le bag GROSSIT en jetons) ;
                  - trend BAISSIER : on VEND dans le rebond puis on RACHÈTE plus bas
                    (le bag grossit en jetons) ;
                  - neutre : comme B.

SORTIE : $ nets (valeur finale / mise initiale) + GROSSISSEMENT DU BAG (jetons finaux /
         jetons initiaux) + MFE/MAE, sur TOUT l'échantillon, sur les 2 moitiés
         chronologiques (R17.3) et par paire.

LIMITES ÉCRITES (règle #8 — une limite non déclarée est une bombe) :
  1. On simule UNE position par entrée, sur une fenêtre glissante ; on ne rejoue PAS la
     chaîne complète du moteur (re-entry, compounding, cash par paire). Le $ compare des
     RÈGLES DE SORTIE/BAG, il ne prédit pas le PnL exact du moteur patché.
  2. Ordre intra-bougie supposé : les paliers (haut) sont touchés en premier, puis le
     stop/trailing (bas) — hypothèse favorable répétée, à lire comme telle.
  3. Ajout de bag (trend haussier) : on réinvestit le cash des paliers au creux
     (0,5×amp sous l'entrée) — pas de levier, pas d'argent externe.
  0 €, aucun ordre, aucune écriture ailleurs que le rapport imprimé.
"""
import csv
import glob
import json
import os
import statistics as st
import sys
import time
import urllib.request
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
PROFILS = os.path.join(BASE, "strategie", "universe_profils.json")
FEE = 0.0005          # 5 bps par côté
HOLD_H = 72           # fenêtre de simulation maximale (heures)
DAYS = 45

# ------------------------------------------------------------------ klines ----


def fetch(pair, days=DAYS):
    """Klines 1h MEXC avec cache local (convention maison)."""
    cf = os.path.join(CACHE, f"{pair}_1h_{days}j.json")
    if os.path.exists(cf) and time.time() - os.path.getmtime(cf) < 6 * 3600:
        try:
            return json.load(open(cf))
        except Exception:
            pass
    end = int(time.time() * 1000)
    cur = end - days * 86400 * 1000
    out = []
    while cur < end:
        u = (f"https://api.mexc.com/api/v3/klines?symbol={pair}&interval=60m"
             f"&startTime={cur}&endTime={end}&limit=500")
        try:
            with urllib.request.urlopen(u, timeout=20) as r:
                data = json.loads(r.read().decode())
        except Exception as e:
            print(f"  ! {pair} requête échouée: {e}", file=sys.stderr)
            break
        if not data:
            break
        out += data
        last = data[-1][0]
        if last <= cur:
            break
        cur = last + 1
        time.sleep(0.15)
    bars = [{"t": d[0], "o": float(d[1]), "h": float(d[2]), "l": float(d[3]),
             "c": float(d[4])} for d in out]
    try:
        json.dump(bars, open(cf, "w"))
    except Exception:
        pass
    return bars


# ------------------------------------------------------------------ entrées ----


def journal_le_plus_recent():
    fs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")))
    return fs[-1] if fs else None


def lire_entrees(chemin):
    """Les VRAIS achats (BUY + BAG_DCA) du journal — entrées identiques pour A/B/C."""
    out = []
    with open(chemin, newline="", encoding="utf-8", errors="ignore") as f:
        for r in csv.DictReader(f):
            ev = (r.get("event") or "").strip().upper()
            if ev not in ("BUY", "BAG_DCA"):
                continue
            try:
                ts = int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                         .replace(tzinfo=timezone.utc).timestamp() * 1000)
                px = float(r["price"])
                qty = float(r["qty"])
            except Exception:
                continue
            if px <= 0 or qty <= 0:
                continue
            out.append({"pair": r["pair"].strip(), "t": ts, "px": px, "qty": qty,
                        "notional": px * qty})
    return out


# ----------------------------------------------------- amplitude + trend ------


def amp7(bars, t0):
    """Range journalier médian des 7 jours AVANT t0 (walk-forward)."""
    avant = [b for b in bars if b["t"] < t0][-24 * 7:]
    if len(avant) < 24:
        return None
    par_jour = {}
    for b in avant:
        d = datetime.fromtimestamp(b["t"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
        j = par_jour.setdefault(d, {"h": b["h"], "l": b["l"]})
        j["h"] = max(j["h"], b["h"])
        j["l"] = min(j["l"], b["l"])
    amps = [(j["h"] - j["l"]) / j["l"] * 100 for j in par_jour.values() if j["l"] > 0]
    return st.median(amps) if amps else None


def trend_of(bars, t0, px):
    """Trend walk-forward sur les 96 h AVANT l'entrée."""
    avant = [b for b in bars if b["t"] < t0]
    if len(avant) < 96:
        return "neutre"
    c = [b["c"] for b in avant]
    sma72 = sum(c[-72:]) / 72
    sma72_prev = sum(c[-96:-24]) / 72
    if px > sma72 and sma72 > sma72_prev:
        return "haussier"
    if px < sma72 and sma72 < sma72_prev:
        return "baissier"
    return "neutre"


# --------------------------------------------------------------- simulateur ---
# Une position = 1 unité de qty initiale. La "souche" (core) n'est jamais vendue par
# les règles. Les niveaux sont exprimés en (type, valeur) : ("amp",k)=k×amp7, ("fix",x)=x%.


def lvl(expr, entry, amp):
    kind, val = expr
    if kind == "amp":
        return entry * (1.0 + val * amp / 100.0)
    return entry * (1.0 + val / 100.0)


def simuler(bars, t0, entry, amp, trend, p, profile_stop):
    apres = [b for b in bars if b["t"] > t0][:HOLD_H]
    if not apres:
        return None

    core = p.get("core_frac", 0.0)
    work = 1.0 - core                     # qty gouvernée par les règles
    cash = 0.0                            # produits, en unités de valeur initiale
    peak = entry
    mfe = 0.0
    mae = 0.0
    sold = 0.0
    holds = list(p.get("ladder", []))     # [[expr, frac], ...]
    holds = [[e, f, False] for (e, f) in holds]
    double_done = False
    armed = False
    rebought = False
    add_done = False

    crash = p.get("crash")                # (expr_dd, frac) sur la qty gouvernée
    slow = p.get("slow")
    gb_expr = p.get("gb_expr")
    arm_expr = p.get("arm_expr")
    stop_expr = p.get("stop_expr")
    rebuy_expr = p.get("rebuy_expr")      # C baissier : rachat plus bas
    add_expr = p.get("add_expr")          # C haussier : ajout au creux

    def sell(q, px):
        nonlocal work, cash, sold
        q = min(q, work)
        if q <= 0:
            return
        cash += q * (px / entry) * (1 - FEE)
        work -= q
        sold += q

    for b in apres:
        h, l, c = b["h"], b["l"], b["c"]
        peak = max(peak, h)
        mfe = max(mfe, (h / entry - 1.0) * 100.0)
        mae = min(mae, (l / entry - 1.0) * 100.0)

        # 1) paliers (touchés sur le haut)
        for L in holds:
            if L[2]:
                continue
            Lx = lvl(L[0], entry, amp)
            if h >= Lx:
                sell(L[1], Lx)
                L[2] = True

        # 2) 2× → vend une fraction du RESTE
        if p.get("double_mult") and not double_done and h >= entry * p["double_mult"]:
            sell(work * p.get("double_frac", 0.5), entry * p["double_mult"])
            double_done = True

        # 3) ajout de bag sur creux (C haussier) — réinvestit le cash accumulé
        if add_expr and not add_done and cash > 0:
            A = lvl(add_expr, entry, amp)
            if l <= A:
                buy_px = min(l, A)
                add_qty = cash * entry / buy_px          # jetons achetés (cash en unités de V0)
                work += add_qty * (1 - FEE)
                cash = 0.0
                add_done = True

        # 4) trailing amplitude (si armé) sur le reste
        if gb_expr and arm_expr:
            if peak >= lvl(arm_expr, entry, amp):
                armed = True
            if armed:
                floor = peak * (1.0 - (lvl(gb_expr, entry, amp) - entry) / entry)
                if l <= floor:
                    sell(work, min(floor, peak))

        # 5) stop dur (amplitude) sur le bas
        if stop_expr and work > 0:
            S = entry * (1.0 - p["stop_frac"] * amp / 100.0) if stop_expr == "amp" \
                else entry * (1.0 - profile_stop / 100.0)
            if l <= S:
                sell(work, S)

        # 6) bag crash / slow (règles fixes ou amplitude)
        if crash and work > 0:
            Cd = entry * (1.0 - (crash[0][1] * amp / 100.0 if crash[0][0] == "amp"
                                 else crash[0][1] / 100.0))
            if l <= Cd:
                sell(work * crash[1], Cd)
        if slow and work > 0:
            Sd = entry * (1.0 - (slow[0][1] * amp / 100.0 if slow[0][0] == "amp"
                                 else slow[0][1] / 100.0))
            if l <= Sd:
                sell(work, Sd)

        # 7) rachat plus bas (C baissier) : le cash RACHÈTE des jetons plus bas
        if rebuy_expr and not rebought and cash > 0:
            R = entry * (1.0 - rebuy_expr[1] * amp / 100.0)
            if l <= R:
                buy_px = min(l, R)
                add_qty = cash * entry / buy_px          # rachat plus bas → plus de jetons
                work += add_qty * (1 - FEE)
                cash = 0.0
                rebought = True

    # fin de fenêtre : le reste (work + core) est valorisé à la dernière clôture
    end_px = apres[-1]["c"]
    final_qty = (work + core) * 1.0
    final_value = cash + (work + core) * (end_px / entry) * (1 - FEE)
    return {
        "value_mult": final_value,          # × la mise initiale
        "qty_growth": final_qty,            # × les jetons initiaux (bag)
        "mfe_pct": mfe, "mae_pct": mae,
        "sold_frac": sold,
    }


# ---------------------------------------------------------------- stratégies --

def strat_A(trend, pair):
    """ACTUEL : paliers rip fixes + 2× + runner giveback 4 % + bag crash -20 %/slow -8 %."""
    early = pair in ("XRPUSDT", "HBARUSDT")
    p1, p2 = (2.0, 6.0) if early else (6.0, 8.0)
    return {
        "ladder": [[("fix", p1), 0.25], [("fix", p2), 0.25]],
        "double_mult": 2.0, "double_frac": 0.5,
        "arm_expr": ("fix", 10.0), "gb_expr": ("fix", 4.0),  # giveback 4 % depuis le pic
        "stop_expr": "profile", "stop_frac": None,
        "crash": [("fix", 20.0), 0.90],
        "slow": [("fix", 8.0), 1.0],
        "core_frac": 0.0,
    }


def strat_B(trend, pair):
    """3 TRANCHES calées sur l'amplitude + souche 20 % intouchable."""
    return {
        "ladder": [[("amp", 0.5), 0.20], [("amp", 1.0), 0.20]],
        "double_mult": None, "double_frac": 0.0,
        "arm_expr": ("amp", 1.0), "gb_expr": ("amp", 0.4),
        "stop_expr": "amp", "stop_frac": 1.5,
        "crash": [("amp", 2.5), 0.90],
        "slow": [("amp", 1.0), 1.0],
        "core_frac": 0.20,
    }


def strat_C(trend, pair):
    """B + bag piloté par le TREND (haussier = tenir/grossir ; baissier = vendre+racheter)."""
    if trend == "haussier":
        return {
            "ladder": [[("amp", 0.6), 0.15], [("amp", 1.2), 0.15]],
            "double_mult": None,
            "arm_expr": ("amp", 1.0), "gb_expr": ("amp", 0.6),   # on laisse courir plus large
            "stop_expr": "amp", "stop_frac": 2.0,                # stop plus lâche en hausse
            "crash": None, "slow": None,                          # PAS de vidage du bag en hausse
            "core_frac": 0.30,                                    # plus de bag tenu
            "add_expr": ("amp", 0.5),                             # add au creux (0,5×amp sous l'entrée)
        }
    if trend == "baissier":
        return {
            "ladder": [[("amp", 0.4), 0.25], [("amp", 0.8), 0.25]],
            "double_mult": None,
            "arm_expr": ("amp", 0.5), "gb_expr": ("amp", 0.4),
            "stop_expr": "amp", "stop_frac": 1.5,
            "crash": None, "slow": None,
            "core_frac": 0.15,
            "rebuy_expr": ("amp", 1.0),                           # rachat 1,0×amp plus bas
        }
    return strat_B(trend, pair)


# ---------------------------------------------------------------------- main --


def load_profils():
    try:
        return json.load(open(PROFILS, encoding="utf-8"))
    except Exception:
        return {}


def main():
    j = journal_le_plus_recent()
    if not j:
        print("aucun journal PAPER_V1_*.csv")
        return 1
    entrees = lire_entrees(j)
    profils = load_profils()

    # uniquement les paires à profil 'trail' + les grosses amplitudes (là où est le gap)
    kl = {}
    res = []
    for e in entrees:
        p = e["pair"]
        if p not in kl:
            kl[p] = fetch(p)
        bars = kl[p]
        if not bars:
            continue
        amp = amp7(bars, e["t"])
        if amp is None or amp <= 0:
            continue
        tr = trend_of(bars, e["t"], e["px"])
        stop_prof = float(((profils.get(p) or {}).get("calib") or {}).get("stop_pct") or 10.0)
        row = {"pair": p, "t": e["t"], "amp": amp, "trend": tr,
               "notional": e["notional"]}
        ok = True
        for nom, fn in (("A", strat_A), ("B", strat_B), ("C", strat_C)):
            r = simuler(bars, e["t"], e["px"], amp, tr, fn(tr, p), stop_prof)
            if r is None:
                ok = False
                break
            row[nom] = r
        if ok:
            res.append(row)

    if not res:
        print("aucune entrée rejouable — mesure impossible, on ne conclut pas")
        return 1

    print(f"CHIFFRAGE BAG/TREND — journal {os.path.basename(j)}")
    print(f"  entrées réelles rejouées : {len(res)}  · notionnel cumulé "
          f"{sum(x['notional'] for x in res):,.0f} $")
    amps = [x["amp"] for x in res]
    print(f"  amp7 (walk-forward)      : médiane {st.median(amps):.1f} % · "
          f"max {max(amps):.1f} %")
    trc = {}
    for x in res:
        trc[x["trend"]] = trc.get(x["trend"], 0) + 1
    print(f"  trend à l'entrée        : {trc}\n")

    def bloc(titre, v):
        notion = sum(x["notional"] for x in v)
        print(f"  --- {titre} (n={len(v)}, notionnel {notion:,.0f} $) ---")
        for k in ("A", "B", "C"):
            val = sum(x["notional"] * x[k]["value_mult"] for x in v)
            gain = val - notion
            qty = sum(x["notional"] * x[k]["qty_growth"] for x in v)
            qty0 = notion
            pnl = gain / notion * 100 if notion else 0
            print(f"    {k:2s}  valeur {val:9,.0f} $  |  PnL {gain:+8.2f} $ ({pnl:+.2f} %)  "
                  f"|  bag (jetons) ×{qty/qty0:.3f}")
        db = (sum(x["notional"] * x["B"]["value_mult"] for x in v)
              - sum(x["notional"] * x["A"]["value_mult"] for x in v))
        dc = (sum(x["notional"] * x["C"]["value_mult"] for x in v)
              - sum(x["notional"] * x["A"]["value_mult"] for x in v))
        print(f"    → Δ B−A : {db:+8.2f} $   ·   Δ C−A : {dc:+8.2f} $")
        return db, dc

    print("VERDICT\n")
    bloc("TOUT l'échantillon", res)
    res_t = sorted(res, key=lambda x: x["t"])
    cut = len(res_t) // 2
    print()
    bloc("1re MOITIÉ", res_t[:cut])
    print()
    bloc("2e MOITIÉ", res_t[cut:])

    # par paire (où ça compte le plus : grosses amplitudes)
    par_p = {}
    for x in res:
        par_p.setdefault(x["pair"], []).append(x)
    print("\n  -- par paire (triées par amplitude médiane) --")
    for p in sorted(par_p, key=lambda k: -st.median([x["amp"] for x in par_p[k]])):
        v = par_p[p]
        a = sum(x["notional"] * x["A"]["value_mult"] for x in v)
        b = sum(x["notional"] * x["B"]["value_mult"] for x in v)
        c = sum(x["notional"] * x["C"]["value_mult"] for x in v)
        n = sum(x["notional"] for x in v)
        print(f"    {p:12s} amp={st.median([x['amp'] for x in v]):6.1f}%  n={len(v):2d}  "
              f"A {a-n:+8.2f}$  B {b-n:+8.2f}$  C {c-n:+8.2f}$  ({c-a:+8.2f}$ C−A)")

    # MFE : jusqu'où le prix montait vraiment (le potentiel laissé sur la table)
    print("\n  -- potentiel laissé (MFE médiane / MAE médiane) --")
    print(f"    MFE médiane {st.median([x['A']['mfe_pct'] for x in res]):.1f} % · "
          f"MAE médiane {st.median([x['A']['mae_pct'] for x in res]):.1f} %")
    return 0


if __name__ == "__main__":
    sys.exit(main())
