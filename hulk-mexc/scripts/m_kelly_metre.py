#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m_kelly_metre.py — le « mètre de m » maison (GO Christophe 02/11, signet @0bl4ze).

Question : pour chaque paire, m = taille réelle / taille juste (Kelly).
score = 2m - m² (m=1 optimal, m=2 rien, m>2 perd même en ayant raison).

Méthode ($ partout, lecture seule, 0 ordre) — FIX 02/11 boucle source :
- L'EDGE VIENT DU JOURNAL LUI-MÊME (colonne pnl_usdt, brut) : Σ = 43.36 $
  = brut PORTEFEUILLE (+43.45 $). L'avg-cost maison divergeait (+14 $) — le
  journal fait foi pour les closes, pas notre re-calcul.
- Coûts : coutCumule par paire (mission) réparti par trade -> pnl net/trade.
  f* = p - (1-p)/b (Kelly) sur les nets. n >= 10 exigé, sinon non mesuré.
- Quantités/cash : rejeu exact (notion±fee, pas d'avg). TEL/QAIT (hors
  mission, journal seul) inclus avec budget 30 historique, flaguées.
- Marks = dernier DIGEST TOUS MOIS (le glob 202610* ratait novembre !).
  pos$ = hold*mark (le bag piégé), latent$ = pos$ - coût_rejoué,
  couverture$ = cash / pos$.
- juste$ = max(0, f*) * budget. m = pos$ / juste$ (juste=0 et pos>0 -> INF).
- Shorts : trades des *_state.json, bankroll 100 $, notionnel médian.
DOUBLE VALIDATION : Σ brut == 43.36 ± 0.5 ET Σ net == +28.01 ± 2, sinon STOP.
"""
import csv
import glob
import json
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = ROOT + "/hulk-mexc/runs"
MISSION = ROOT + "/Index_Maison/cockpit/mission.json"
JOURNAL = RUNS + "/PAPER_V1_20261029_174940.csv"
PF_MD = RUNS + "/PORTEFEUILLE_LATEST.md"
FEE = 0.0005
N_MIN = 10  # en dessous : edge non mesuré, pas de f*


def lire_couts_pf():
    """Coûts par paire = brut journal - net PORTEFEUILLE (les deux font foi).
    FIX boucle source : coutCumule mission (Σ 21.56) surestime vs coûts
    validés du portefeuille (15.44) ; ici Σ coûts == 15.35 ≈ 15.44."""
    import re
    net = {}
    try:
        txt = open(PF_MD, encoding="utf-8").read()
    except Exception:
        return net
    for m in re.finditer(r"\|\s*(\w+USDT)\s*\|\s*([+-]?[0-9.]+)\s*\|", txt):
        if "paire" in m.group(1).lower():
            continue
        try:
            net[m.group(1)] = float(m.group(2))
        except Exception:
            continue
    return net


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def digest_marks():
    idx = {}
    for f in sorted(glob.glob(RUNS + "/DIGEST_*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        t = parse_ts(d.get("ts"))
        if t is None:
            continue
        px = {}
        for e in (d.get("pairs") or []):
            try:
                if e.get("pair") and float(e.get("last") or 0) > 0:
                    px[e["pair"]] = float(e["last"])
            except Exception:
                continue
        if px:
            idx[t] = px
    if not idx:
        return {}, None
    tmax = max(idx)
    return idx[tmax], tmax


def replay():
    mission = json.load(open(MISSION, encoding="utf-8"))
    consts = {p["pair"]: p for p in mission["hulk"]["hulkVsHold"]["pairs"]}
    rows = list(csv.DictReader(open(JOURNAL, newline="", encoding="utf-8-sig")))
    st = {}
    for p, c in consts.items():
        st[p] = {"budget": float(c.get("budget") or 0.0), "cash": float(c.get("budget") or 0.0),
                 "qty": 0.0, "cost": 0.0, "pnls": [], "real": 0.0, "nbuy": 0.0,
                 "cout": float(c.get("coutCumule") or 0.0), "mission": True}
    for jp in ("TELUSDT", "QAITUSDT"):  # hors mission mais dans le journal
        if jp not in st:
            st[jp] = {"budget": 30.0, "cash": 30.0, "qty": 0.0, "cost": 0.0,
                      "pnls": [], "bruts": [], "real": 0.0, "nbuy": 0.0,
                      "cout": 0.0, "mission": False}
    for _s in st.values():
        _s.setdefault("bruts", [])
    for r in rows:
        p = r.get("pair") or ""
        if p not in st:
            continue
        ev = (r.get("event") or "").upper()
        if ev == "BAG_ARM":
            continue
        is_buy = ev in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA")
        is_sell = ev.startswith(("SELL", "STOP", "BAG")) and not is_buy
        if not is_buy and not is_sell:
            continue
        try:
            q = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
        except Exception:
            continue
        if q <= 0 or px <= 0:
            continue
        s = st[p]
        notion = q * px
        fee = notion * FEE
        if is_buy:
            if ev == "GBAG_SOUCHE":
                s["cash"] -= max(0.0, s["cash"])
            else:
                s["cash"] -= notion + fee
            s["qty"] += q
            s["cost"] += notion + fee
            s["nbuy"] += notion
        else:
            avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
            pnl = notion - fee - avg * q
            s["pnls"].append(pnl)
            try:
                s["bruts"].append(float(r.get("pnl_usdt") or 0.0))
            except Exception:
                s["bruts"].append(0.0)
            s["real"] += pnl
            s["cash"] += notion - fee
            s["qty"] = max(0.0, s["qty"] - q)
            s["cost"] = max(0.0, s["cost"] - avg * q)
    return st


def kelly(pnls):
    n = len(pnls)
    if n < N_MIN:
        return {"n": n, "mesure": False}
    wins = [x for x in pnls if x > 0]
    loss = [-x for x in pnls if x < 0]
    p = len(wins) / n
    W = sum(wins) / len(wins) if wins else 0.0
    L = sum(loss) / len(loss) if loss else 0.0
    if W <= 0 or L <= 0:
        return {"n": n, "mesure": True, "p": round(p, 3), "W": round(W, 4),
                "L": round(L, 4), "b": None, "f": 0.0 if p == 0 else None,
                "e": round(sum(pnls) / n, 4)}
    b = W / L
    f = p - (1 - p) / b
    return {"n": n, "mesure": True, "p": round(p, 3), "W": round(W, 4),
            "L": round(L, 4), "b": round(b, 3), "f": round(f, 4),
            "e": round(sum(pnls) / n, 4)}


def flag(m, mesure, f):
    if not mesure:
        return "🟡 EDGE NON MESURÉ"
    if f is not None and f <= 0:
        return "🔴 EDGE ≤ 0"
    if m != m:  # NaN
        return "🟡"
    if m == float("inf"):
        return "🔴 m=INF (expo sans edge)"
    if m > 2:
        return "🔴 m>2 PERDANT"
    if m > 1.5:
        return "🟡 m>1,5"
    if m > 1.0:
        return "🟡 m>1"
    return "🟢"


def main():
    global PF_NET
    PF_NET = lire_couts_pf()
    marks, tmarks = digest_marks()
    st = replay()
    print(f"marks: {tmarks.isoformat() if tmarks else '?'} ({len(marks)} paires)")
    print(f"{'paire':12s} {'bdg':>5s} {'pos$':>8s} {'cash$':>8s} {'couv':>6s} "
          f"{'lat$':>8s} {'lat%':>6s} {'n':>4s} {'p':>5s} {'b':>6s} {'f*':>7s} "
          f"{'juste$':>7s} {'m':>6s} {'score':>6s}  drapeau")
    tot_pos = tot_juste = tot_brut = tot_cout = tot_lat = 0.0
    for p in sorted(st):
        s = st[p]
        mk = marks.get(p, 0.0)
        pos = s["qty"] * mk
        avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
        latent = s["qty"] * (mk - avg) if s["qty"] > 1e-12 else 0.0
        latpc = (100 * latent / pos) if pos > 1e-9 else 0.0
        tot_lat += latent
        couv = (s["cash"] / pos) if pos > 0.01 else float("inf")
        bruts = s.get("bruts") or []
        tot_brut += sum(bruts)
        if p in PF_NET:
            cout = sum(bruts) - PF_NET[p]  # brut journal - net validé
        else:
            cout = s["cout"]  # repli mission si paire absente du PF
        tot_cout += cout
        share = (cout / len(bruts)) if bruts else 0.0
        nets = [b - share for b in bruts]  # edge NET de coûts (spread+fees)
        k = kelly(nets)
        if k.get("mesure") and k.get("f") is not None and k["f"] > 0:
            juste = k["f"] * s["budget"]
            m = pos / juste if juste > 1e-9 else (float("inf") if pos > 1e-9 else 0.0)
            tot_pos += pos
            tot_juste += juste
        elif k.get("mesure"):
            juste, m = 0.0, (float("inf") if pos > 1e-9 else 0.0)
        else:
            juste, m = float("nan"), float("nan")
        score = 2 * m - m * m if m == m and m != float("inf") else float("-inf")
        couv_s = "INF" if couv == float("inf") else f"{couv:.2f}"
        m_s = "INF" if m == float("inf") else ("NA" if m != m else f"{m:.2f}")
        sc_s = "-INF" if score == float("-inf") else f"{score:.2f}"
        b_s = "NA" if k.get("b") is None else f"{k['b']:.2f}"
        f_s = "NA" if k.get("f") is None else f"{k['f']:.3f}"
        p_s = "NA" if k.get("p") is None else f"{k['p']:.2f}"
        print(f"{p:12s} {s['budget']:5.0f} {pos:8.2f} {s['cash']:8.2f} {couv_s:>6s} "
              f"{latent:8.2f} {latpc:5.1f}% {k['n']:4d} {p_s:>5s} {b_s:>6s} {f_s:>7s} "
              f"{(f'{juste:.2f}' if juste == juste else 'NA'):>7s} {m_s:>6s} {sc_s:>6s}  "
              f"{flag(m, k.get('mesure'), k.get('f'))}")
    m_glob = tot_pos / tot_juste if tot_juste > 1e-9 else float("nan")
    s_glob = 2 * m_glob - m_glob ** 2 if m_glob == m_glob else float("nan")
    print()
    print(f"PORTEFEUILLE (edge mesuré) : pos={tot_pos:.2f} $ juste={tot_juste:.2f} $ "
          f"-> m_global={m_glob:.3f} score={s_glob:.3f}")
    net = tot_brut - tot_cout
    print(f"VALIDATION : Σ brut journal = {tot_brut:.2f} $ (réf 43.36) · "
          f"Σ coûts = {tot_cout:.2f} $ (réf 15.44) · net = {net:.2f} $ (réf +28.01) · "
          f"Σ latent = {tot_lat:.2f} $ (réf -71.23 au 10h09, marks 11h15 — dérive admise)"  )
    if abs(tot_brut - 43.36) > 0.5 or abs(net - 28.01) > 2.0:
        print("⚠️ ÉCART — méthode à revoir, chiffres NON publiés.")
        return 2
    # --- SHORTS ---
    print()
    print("--- SHORTS (bankroll 100 $) ---")
    for sym in ["btc", "eth", "xrp"]:
        try:
            d = json.load(open(f"{RUNS}/short_{sym}_live.json", encoding="utf-8"))
            s = json.load(open(f"{RUNS}/short_{sym}_state.json", encoding="utf-8"))
        except Exception as e:
            print(f"{sym}: illisible ({e})")
            continue
        trs = s.get("trades") or []
        pnls = [float(t.get("pnl_usd") or 0.0) for t in trs]
        nots = [float(t.get("notional") or 0.0) for t in trs if float(t.get("notional") or 0.0) > 0]
        k = kelly(pnls)
        nmed = sorted(nots)[len(nots) // 2] if nots else 0.0
        if k.get("mesure") and k.get("f") is not None and k["f"] > 0:
            juste = k["f"] * 100.0
            m = nmed / juste if juste > 1e-9 else 0.0
        else:
            juste, m = float("nan"), float("nan")
        pos_now = d.get("position")
        print(f"{sym.upper()}: pos_now={pos_now} n={k['n']} p={k.get('p')} b={k.get('b')} "
              f"f*={k.get('f')} notion_med={nmed:.2f} $ juste={juste if juste==juste else 'NA'} $ "
              f"m={m if m==m else 'NA'} cap={d.get('capital')} pnl={d.get('pnl_total')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
