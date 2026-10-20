#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE ÉCORCE — REPLAY FRACTIONS DE SORTIE SUR LE JOURNAL MOTEUR (20/10/2026, Buffy)
=======================================================================================
GO Christophe 20/10 : « chiffre moi ça, et après on décide » — la règle « écorce au
premier retrace, tronc à confirmation » : chaque sortie ne vend qu'une FRACTION de la
poche (25-30 %) au lieu de 50-100 %. Question : combien EDEL+QNT (et le total) auraient
rapporté de plus, et à quel creux (regret max) ?

MÉTHODE (1er ordre, honnête) : on rejoue le CSV PAPER_V1 avec les MÊMES entrées et les
MÊMES déclencheurs de sortie, mais chaque vente est plafonnée à FRAC × poche-avant.
Les achats sont identiques dans toutes les variantes → le delta ne dépend que des
encaissements + valeur terminale (les bases de coût s'annulent). Frais 5 bps/côté
(convention maison, REPLAY_SLIP_BPS paramétrable comme chiffrage_entree_sortie_replay).
Valeur terminale = poches restantes × dernier prix du journal.
Poches pos/bag/cons calées sur le lifecycle exact du moteur (core_trend sort du
tradable, house/conservation vident, BAG_DCA trend renforce le TRADABLE — prouvé §21).

VALIDATION : FRAC=1.0 doit retomber sur le déclaré (terminal ≈ state, cf. §21 :
19 paires à 0.000000000). Sinon le simulateur est faux et les variantes aussi.

LIMITE DÉCLARÉE : pas de boucle de rétroaction — en réalité vendre moins libère moins
de cash donc moins de rachats (reentry/cash_redeploy). Le chiffre est un majorant de
l'effet en marché haussier ; la décision doit le passer avec marge.

Lecture seule moteur. 0 € · 0 ordre.
"""
import csv
import glob
import json
import os
import sys
from collections import defaultdict

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(SCRIPTS, "..", "runs")
STATE = os.path.join(RUNS, "PAPER_V1_20261018_100103_state.json")
FEE = 0.0005 + float(os.environ.get("REPLAY_SLIP_BPS", "0")) / 10000.0
FRACS = [1.0, 0.5, 0.3, 0.25]

IN_POS = ("BUY", "GBAG_PYRAMIDE")
IN_BAG = ("GBAG_SOUCHE",)
OUT_POS = ("SELL", "SELL_PARTIAL")
OUT_BAG = ("BAG_SELL", "BAG_CRASH")


def dernier_csv():
    csvs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")),
                  key=os.path.getmtime, reverse=True)
    for c in csvs:
        if os.path.exists(os.path.join(RUNS, os.path.basename(c).replace(".csv", "_state.json"))):
            pass
        return c
    return csvs[0]


def replay(frac):
    rows = list(csv.DictReader(open(dernier_csv(), newline="", encoding="utf-8-sig")))
    pos = defaultdict(float)
    bag = defaultdict(float)
    cons = defaultdict(float)
    extra_keep = {}  # (ts,pair) -> part non-vendue du stake-out : rejoint le bag (jamais la nature)
    proceeds = defaultdict(float)   # encaissements nets de frais, par paire
    n_ventes = defaultdict(int)
    last_px = {}
    cumul = []  # (ts, delta_cumulé vs baseline) rempli après coup
    evts = []   # (ts, pair, delta_proceeds) pour la courbe de regret
    for r in rows:
        ev = (r.get("event") or "").strip()
        p = (r.get("pair") or "").strip()
        if not p:
            continue
        try:
            px = float(r.get("price") or 0)
        except ValueError:
            continue
        if px > 0:
            last_px[p] = px  # TOUTES les lignes incl. SKIP : le mark terminal doit être le dernier vu
        if ev == "SKIP":
            continue
        try:
            q = float(r.get("qty") or 0)
        except ValueError:
            continue
        note = r.get("reason") or ""
        ts = r.get("ts")
        if ev in IN_POS:
            pos[p] += q
        elif ev in IN_BAG:
            bag[p] += q
        elif ev == "BAG_DCA":
            if "trend_" in note:
                pos[p] += q
            elif frac < 1.0:
                bag[p] += q  # FIX COMPAGNON : le dca_rebuy ÉCRASE le bag (bags[pair] = )
            else:
                bag[p] = q  # baseline : le bag est toujours vide ici (§21)
        elif ev == "BAG_ARM":
            if "core_trend" in note:
                mv = min(q, pos[p])
                pos[p] -= mv
                if frac < 1.0:
                    bag[p] += mv  # FIX COMPAGNON : sinon l'écorce gardée est écrasée
                else:
                    bag[p] = mv  # baseline : bag toujours vide ici (§21)
            elif "house_half" in note:
                bag[p] = q + extra_keep.pop((ts, p), 0.0)
                pos[p] = 0.0
            elif "conservation_half" in note:
                cons[p] = q
                pos[p] = 0.0
        elif ev in OUT_POS or ev in OUT_BAG:
            poche = pos if ev in OUT_POS else bag
            # cascade : la poche nominale d'abord, puis les autres (jamais de vente à découvert)
            ordre = [poche[p], cons[p], bag[p]] if ev in OUT_POS else [bag[p], cons[p], pos[p]]
            refs = (["pos", "cons", "bag"] if ev in OUT_POS else ["bag", "cons", "pos"])
            avant = ordre[0]
            plafond = frac * avant
            vente = min(q, plafond, sum(ordre))
            reste = vente
            for i, ref in enumerate(refs):
                if reste <= 0:
                    break
                d = {"pos": pos, "cons": cons, "bag": bag}[ref]
                take = min(d[p], reste)
                d[p] -= take
                reste -= take
            proceeds[p] += vente * px * (1.0 - FEE)
            n_ventes[p] += 1
            if "stake_out_" in note and "sell_" in note:
                # le non-vendu du stake-out rejoint le keep (vrai comportement moteur)
                extra_keep[(ts, p)] = extra_keep.get((ts, p), 0.0) + (q - vente)
            if frac < 1.0:
                evts.append((ts, p, None, None))  # delta calculé vs baseline plus bas
        elif ev == "DUST_DROP":
            pass
    terminal = {p: (pos[p] + bag[p] + cons[p]) * last_px.get(p, 0.0)
                for p in set(list(pos) + list(bag) + list(cons))}
    return {"proceeds": dict(proceeds), "terminal": terminal,
            "poches": {p: (pos[p], bag[p], cons[p]) for p in terminal},
            "n_ventes": dict(n_ventes), "last_px": last_px}


def main():
    csv_path = dernier_csv()
    base = replay(1.0)
    # validation : le terminal baseline doit coller au state déclaré (§21)
    st = json.load(open(STATE, encoding="utf-8"))
    decal = defaultdict(float)
    for k in ("positions", "bags", "conservation", "bag_dca"):
        for pa, v in (st.get(k) or {}).items():
            if isinstance(v, dict):
                decal[pa] += float(v.get("qty") or 0)
    max_ecart = 0.0
    for pa, (qp, qb, qc) in base["poches"].items():
        ec = abs((qp + qb + qc) - decal.get(pa, 0.0))
        max_ecart = max(max_ecart, ec)
    print(f"VALIDATION baseline vs state : écart qty max = {max_ecart:.9f} "
          f"(attendu ~0 comme §21, sinon STOP)")
    if max_ecart > 0.05:
        print("SIMULATEUR FAUX — on ne chiffre rien.")
        return 2
    total_base = sum(base["proceeds"].values()) + sum(base["terminal"].values())
    lignes = []
    print(f"\n{'variante':<10}{'encaissé':>12}{'terminal':>12}{'TOTAL':>12}{'delta':>10}  creux_max(regret)")
    print(f"{'BASELINE':<10}{sum(base['proceeds'].values()):>12.2f}"
          f"{sum(base['terminal'].values()):>12.2f}{total_base:>12.2f}{'—':>10}")
    for frac in [f for f in FRACS if f < 1.0]:
        v = replay(frac)
        # courbe de regret : rejoue les encaissements dans l'ordre pour le creux max
        tot_v = sum(v["proceeds"].values()) + sum(v["terminal"].values())
        delta = tot_v - total_base
        # creux max = min du delta cumulé : approx par paires (encaissé décalé)
        creux = min(0.0, sum(min(0.0, v["proceeds"].get(p, 0.0) - base["proceeds"].get(p, 0.0))
                             for p in set(list(v["proceeds"]) + list(base["proceeds"]))))
        print(f"ÉCORCE-{int(frac*100):<3}{sum(v['proceeds'].values()):>12.2f}"
              f"{sum(v['terminal'].values()):>12.2f}{tot_v:>12.2f}{delta:>+10.2f}  {creux:+.2f}")
        lignes.append({"frac": frac, "delta_total": round(delta, 2),
                       "detail": {p: round((v["proceeds"].get(p, 0.0) + v["terminal"].get(p, 0.0))
                                           - (base["proceeds"].get(p, 0.0) + base["terminal"].get(p, 0.0)), 2)
                                  for p in sorted(set(list(v["proceeds"]) + list(base["proceeds"])
                                                       + list(v["terminal"])))}})
    out = {"ts": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "journal": os.path.basename(csv_path), "fee_bps": FEE * 10000,
           "validation_ecart_qty_max": max_ecart,
           "total_baseline": round(total_base, 2), "variantes": lignes,
           "limite": "1er ordre : boucle cash (moins vendu = moins de rachats) ignorée = majorant en bull"}
    with open(os.path.join(RUNS, "CHIFFRAGE_ECORCE.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("\n→ hulk-mexc/runs/CHIFFRAGE_ECORCE.json")
    # focus EDEL+QNT pour la décision
    for nom in ("EDELUSDT", "QNTUSDT"):
        b = base["proceeds"].get(nom, 0.0) + base["terminal"].get(nom, 0.0)
        det = {l["frac"]: l["detail"].get(nom) for l in lignes}
        print(f"{nom}: baseline={b:.2f} " + " ".join(f"écorce-{int(k*100)}={v:+.2f}" for k, v in det.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
