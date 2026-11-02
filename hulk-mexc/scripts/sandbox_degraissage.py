#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sandbox_degraissage.py — BAC À SABLE (GO Christophe 02/11, esprit backtest_regime :
on ne CÂBLE que si le solde est > 0 ; exit 0 toujours, outil de mesure, pas un gate).

Question : le Mur de Fer fixe (11,67 %/jour, 25 % global — recalibrés 09/09 mais
TOUJOURS en dur) aurait-il protégé le crash du 29/10 ? Et un Mur MESURÉ (k×σ) ?
Et combien le dégraissage S1/S2/S3 aurait-il économisé ?

LEÇON 02/11 (boucle source) : en clôture QUOTIDIENNE, le crash du 29/10 est
INVISIBLE (flash intraday + rebond) — aucun Mur journalier, fixe ou mesuré, ne
l'aurait attrapé. Le déclencheur doit donc travailler en INTRADAY (le nourrisseur
tourne déjà toutes les 60 s) : equity à chaque snapshot DIGEST (~1/h).

Méthode ($ partout, lecture seule, 0 ordre, sortie stdout) :
1. Equity à chaque DIGEST : un seul passage journal (cash départ = budgets ;
   BUY/DCA/GBAG -> cash -= notion+fee, qty/cost += ; SELL/STOP/BAG* ->
   cash += notion-fee, qty -= q au coût moyen), snapshot au fil des digests :
   equity = Σ cash + Σ qty×mark. Rendements snapshot-à-snapshot, σ glissante
   48 snapshots (~2 j). Mur mesuré : |r| >= k×σ. Grille k = 1..5.
2. Comparaison : fixes 11,67 % et 25 % -> déclenchements depuis 07/24 ?
3. Contrefactuel crash (fenêtre 28/10->02/11) : f* calculé sur trades <= 28/10
   23h59 (journal seul, n>=10, coûts brut-net PF), cibles S1/S2/S3 figées au
   28/10, latent plafonné(t) = latent(t) × cible/pos28. $ économisés au creux
   et au 02/11 (approximation linéaire écrite, sans dynamique de compounding).
RÉFÉRENCES : aucune constante métier en dur (k lu sur grille, f* du journal).
"""
import csv
import glob
import json
import statistics
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = ROOT + "/hulk-mexc/runs"
JOURNAL = RUNS + "/PAPER_V1_20261029_174940.csv"
MISSION = ROOT + "/Index_Maison/cockpit/mission.json"
PF_MD = RUNS + "/PORTEFEUILLE_LATEST.md"
FEE = 0.0005
SIG_WIN = 48  # ~2 jours de snapshots


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def snapshots():
    """[(ts, {pair: mark})] triés, ~1/h depuis 07/24."""
    out = []
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
            out.append((t, px))
    return out


def lire_couts_pf():
    import re
    try:
        txt = open(PF_MD, encoding="utf-8").read()
    except Exception:
        return {}
    net = {}
    for m in re.finditer(r"\|\s*(\w+USDT)\s*\|\s*([+-]?[0-9.]+)\s*\|", txt):
        try:
            net[m.group(1)] = float(m.group(2))
        except Exception:
            continue
    return net


def replay_journal(jusqua=None):
    """Rejeu exact quantités/cash + bruts journal. Retourne (st, bruts_par_paire)."""
    mission = json.load(open(MISSION, encoding="utf-8"))
    consts = {p["pair"]: p for p in mission["hulk"]["hulkVsHold"]["pairs"]}
    for jp in ("TELUSDT", "QAITUSDT"):
        if jp not in consts:
            consts[jp] = {"budget": 30.0}
    rows = list(csv.DictReader(open(JOURNAL, newline="", encoding="utf-8-sig")))
    st = {p: {"budget": float(c.get("budget") or 0.0),
              "cash": float(c.get("budget") or 0.0),
              "qty": 0.0, "cost": 0.0} for p, c in consts.items()}
    bruts = {p: [] for p in st}
    for r in rows:
        t = parse_ts(r.get("ts") or "")
        if t is None or (jusqua is not None and t > jusqua):
            continue
        p = r.get("pair") or ""
        if p not in st:
            continue
        ev = (r.get("event") or "").upper()
        if ev == "BAG_ARM":
            continue
        try:
            q = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
        except Exception:
            continue
        if q <= 0 or px <= 0:
            continue
        s = st[p]
        notion, fee = q * px, q * px * FEE
        if ev in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA"):
            s["cash"] -= max(0.0, s["cash"]) if ev == "GBAG_SOUCHE" else notion + fee
            s["qty"] += q
            s["cost"] += notion + fee
        elif ev.startswith(("SELL", "STOP", "BAG")):
            s["cash"] += notion - fee
            avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
            s["qty"] = max(0.0, s["qty"] - q)
            s["cost"] = max(0.0, s["cost"] - avg * q)
            try:
                bruts[p].append(float(r.get("pnl_usdt") or 0.0))
            except Exception:
                pass
    return st, bruts


def fstar(bruts, cout):
    """Kelly NET (coûts déduits, RIZE). None si non mesurable."""
    n = len(bruts)
    if n < 10:
        return None
    share = cout / n
    nets = [b - share for b in bruts]
    wins = [x for x in nets if x > 0]
    loss = [-x for x in nets if x < 0]
    if not wins or not loss:
        return None
    p = len(wins) / n
    b = (sum(wins) / len(wins)) / (sum(loss) / len(loss))
    f = p - (1 - p) / b
    return f if f > 0 else 0.0


def equity_snapshots(snaps=None):
    """Equity à chaque snapshot DIGEST : un seul passage journal.
    Importable (mur_mesure_daily.py s'en sert — pas de doublon).
    Retour : [(ts, equity)] triés."""
    if snaps is None:
        snaps = snapshots()
    mission = json.load(open(MISSION, encoding="utf-8"))
    consts = {p["pair"]: p for p in mission["hulk"]["hulkVsHold"]["pairs"]}
    for jp in ("TELUSDT", "QAITUSDT"):
        if jp not in consts:
            consts[jp] = {"budget": 30.0}
    rows = list(csv.DictReader(open(JOURNAL, newline="", encoding="utf-8-sig")))
    evs = []
    for r in rows:
        t = parse_ts(r.get("ts") or "")
        if t is None:
            continue
        try:
            q = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
        except Exception:
            continue
        evs.append((t, (r.get("pair") or ""), (r.get("event") or "").upper(), q, px,
                    float(r.get("pnl_usdt") or 0.0) if q and px else 0.0))
    evs.sort(key=lambda e: e[0])
    cur = {p: {"cash": float(c.get("budget") or 0.0), "qty": 0.0, "cost": 0.0}
           for p, c in consts.items()}
    ie = 0
    eq = []
    last_px = {}
    for t, pxm in snaps:
        while ie < len(evs) and evs[ie][0] <= t:
            _, p, ev, q, px, _ = evs[ie]
            ie += 1
            if p not in cur or q <= 0 or px <= 0 or ev == "BAG_ARM":
                continue
            s = cur[p]
            notion, fee = q * px, q * px * FEE
            if ev in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA"):
                s["cash"] -= max(0.0, s["cash"]) if ev == "GBAG_SOUCHE" else notion + fee
                s["qty"] += q
                s["cost"] += notion + fee
            elif ev.startswith(("SELL", "STOP", "BAG")):
                s["cash"] += notion - fee
                avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
                s["qty"] = max(0.0, s["qty"] - q)
                s["cost"] = max(0.0, s["cost"] - avg * q)
        last_px.update(pxm)
        e = sum(s["cash"] for s in cur.values())
        e += sum(s["qty"] * last_px.get(p, 0.0) for p, s in cur.items())
        eq.append((t, round(e, 2)))
    return eq


def main():
    snaps = snapshots()
    print(f"snapshots DIGEST : {len(snaps)} ({snaps[0][0].isoformat()} -> {snaps[-1][0].isoformat()})")
    st, _ = replay_journal()
    eq = equity_snapshots(snaps)
    rets = []
    for i in range(1, len(eq)):
        prev, cur_e = eq[i - 1][1], eq[i][1]
        dt_h = (eq[i][0] - eq[i - 1][0]).total_seconds() / 3600.0 or 1.0
        r = (cur_e - prev) / prev if prev > 1e-9 else 0.0
        rets.append((eq[i][0], r / (dt_h ** 0.5)))  # normalisé /h (σ en /h)
    print("\n--- 10 pires snapshots (rendement horaire normalisé) ---")
    for t, r in sorted(rets, key=lambda x: x[1])[:10]:
        print(f"  {t.strftime('%m-%d %H:%M')} : {r * 100:+.2f} %/h")
    sig = {}
    for i, (t, r) in enumerate(rets):
        win = [x[1] for x in rets[max(0, i - SIG_WIN):i]]
        sig[t] = statistics.pstdev(win) if len(win) >= 24 else None
    print("\n--- Grille k INTRADAY (Mur mesuré : |r| >= k×σ_48snap) ---")
    for k10 in range(10, 55, 5):
        k = k10 / 10.0
        decl = [t for t, r in rets if sig.get(t) and abs(r) >= k * sig[t]]
        print(f"k={k:3.1f} : {len(decl):3d} décl.  "
              + ", ".join(t.strftime("%m-%d %H:%M") for t in decl[:10]))
    n117 = [t for t, r in rets if abs(r) >= 0.1167]
    print(f"FIXE 11,67 % : {len(n117)} déclenchements (jamais tiré — décoratif)")
    print("--- Le 29/10 au soir (crash hack) : à quel k aurait-on tiré ? ---")
    for t, r in rets:
        if t.strftime("%m-%d") == "10-29" and t.hour >= 18 and sig.get(t):
            print(f"  {t.strftime('%m-%d %H:%M')} : |r|/σ = {abs(r) / sig[t]:.2f} "
                  f"-> tire pour tout k <= {abs(r) / sig[t]:.1f}")
    # --- Contrefactuel crash ---
    print("\n--- Contrefactuel crash 29/10 (f* au 28/10 23h59, cibles figées) ---")
    lim = datetime(2026, 10, 28, 23, 59, 59, tzinfo=timezone.utc)
    st28, br28 = replay_journal(jusqua=lim)
    pf = lire_couts_pf()
    marks28 = {}
    for t, pxm in snaps:
        if t <= lim:
            marks28.update(pxm)
        else:
            break
    tot_pos = {s: 0.0 for s in ("S1", "S2", "S3")}
    tot_saved = {s: 0.0 for s in ("S1", "S2", "S3")}
    details = []
    for p, s in st28.items():
        mk = marks28.get(p, 0.0)
        pos = s["qty"] * mk if s["qty"] > 1e-12 else 0.0
        if pos <= 0.01:
            continue
        n = len(br28.get(p, []))
        if p in pf and n:
            cout = sum(br28[p]) - pf[p]
        else:
            cout = 0.0
        f = fstar(br28.get(p, []), cout)
        if f is None:
            details.append((p, pos, "aveugle", 0.0, 0.0, 0.0))
            continue
        if f <= 0:
            details.append((p, pos, "sans-edge", pos, pos, pos))
            tot_saved["S1"] += pos
            tot_saved["S2"] += pos
            tot_saved["S3"] += pos
            continue
        juste = f * float((mission["hulk"]["hulkVsHold"]["pairs"] and
                           next((c.get("budget") or 0 for c in
                                 mission["hulk"]["hulkVsHold"]["pairs"]
                                 if c["pair"] == p), 30.0)) or 30.0)
        avg = (s["cost"] / s["qty"]) if s["qty"] > 1e-12 else 0.0
        lat = s["qty"] * (mk - avg)
        latf = max(0.0, 1.0 + (lat / pos if pos > 1e-9 else 0.0))
        c1, c2, c3 = juste, 0.5 * juste, juste * latf
        a1, a2, a3 = max(0.0, pos - c1), max(0.0, pos - c2), max(0.0, pos - c3)
        tot_saved["S1"] += a1
        tot_saved["S2"] += a2
        tot_saved["S3"] += a3
        tot_pos["S1"] += pos
        details.append((p, pos, f"m={pos / juste:.1f}" if juste > 1e-9 else "m=INF",
                        a1, a2, a3))
    details.sort(key=lambda d: d[3], reverse=True)
    print(f"{'paire':12s} {'pos28$':>8s} {'état':>9s} {'S1 éco':>8s} {'S2 éco':>8s} {'S3 éco':>8s}")
    for p, pos, et, a1, a2, a3 in details:
        print(f"{p:12s} {pos:8.2f} {et:>9s} {a1:8.2f} {a2:8.2f} {a3:8.2f}")
    s1 = sum(d[3] for d in details)
    s2 = sum(d[4] for d in details)
    s3 = sum(d[5] for d in details)
    print(f"SOMME lignes : S1={s1:.2f} S2={s2:.2f} S3={s3:.2f} "
          f"vs totaux {tot_saved['S1']:.2f}/{tot_saved['S2']:.2f}/{tot_saved['S3']:.2f}")
    for sid, nom in (("S1", "JUSTE"), ("S2", "PRO demi-Kelly"), ("S3", "BAG")):
        print(f"{nom} : économisés au 28/10 = {tot_saved[sid]:.2f} $ "
              f"(exposés au crash en moins — le latent du 29-30/10 frappe une base réduite)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
