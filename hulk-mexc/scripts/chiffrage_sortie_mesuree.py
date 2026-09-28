#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_SORTIE_MESUREE.py — R17 : « la mesure décide », pas une horloge ni un % en dur.

QUESTION (ordre Christophe 22/09/2026 : « aucun bricolage », « les chiffres déterminent ») :
  Les paliers de SORTIE du moteur sont des pourcentages FIXES, identiques pour une paire
  qui bouge 1,3 %/jour et pour une qui bouge 150 % : RIP_EARLY +2 %/+6 %, RIP_LATE +6 %/+8 %.
  Si on les relis dans l'unité MESURÉE de chaque paire (sa CADENCE, le range journalier
  médian que le moteur journalise déjà), est-ce que ça rapporte plus — ou moins ?

MÉTHODE (aucune entrée inventée : on rejoue les VRAIS achats du journal) :
  - entrées = événements BUY réels (ts, paire, prix, qty) + la CADENCE réellement mesurée
    par le moteur, telle qu'elle est écrite dans la colonne `cadence` du journal ;
  - on rejoue la MÊME mécanique d'échelle (2 paliers, moitié/moitié) sur les bougies 1 h
    qui suivent l'entrée, jusqu'à 48 h :
      A  ACTUEL (fixe)  : +2 % puis +6 %
      A2 ACTUEL (fixe)  : +6 % puis +8 %      (l'autre branche du ladder en place)
      B  MESURÉ         : (2 % , 6 %) × r,  où r = cadence_de_la_paire / cadence_de_référence
  - r est SANS réglage nouveau : c'est le rapport entre la cadence de la paire et la
    cadence MÉDIANE des paires réellement tradées (imprimée). La règle reste la même
    règle — on la lit simplement dans l'unité de la paire au lieu du pourcent universel.
  - frais 10 bps aller-retour (5 bps/côté, tarif maison), sur le notionnel réel.
  - pattes non touchées en 48 h → sortie à la dernière clôture connue (aucun prix inventé).

LIMITES ÉCRITES (règle #8 — une limite non déclarée est une bombe) :
  1. On isole L'EFFET DU CHANGEMENT D'ÉCHELLE DU LADDER : on ne rejoue PAS la chaîne
     complète du moteur (stop cadencé, trailing, scale-outs partiels, sortie de bag).
     Le $ ici ne prédit donc pas le PnL du moteur patché — il compare deux échelles.
  2. On ne juge pas sur un seul horizon (R17.3) : le verdict est rendu sur 2 moitiés
     de l'échantillon ET par paire. Un résultat qui change de signe d'une moitié à
     l'autre n'est pas un résultat.

SORTIE : hulk-mexc/runs/CHIFFRAGE_SORTIE_MESUREE_<ts>.json + imprimé.
0 €, aucun ordre, aucune écriture ailleurs que le rapport.
"""
import csv
import glob
import json
import os
import statistics as st
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
FEE = 0.0005          # 5 bps par côté
MAX_HOLD_H = 48       # garde-fou de détention (déclaré, identique aux deux échelles)
SPLIT = 0.5           # moitié sur chaque palier (forme du ladder actuel)

# Le ladder EN PLACE aujourd'hui, en % (source : config/defaults.env).
LADDER_FIXE = {
    "A_actuel_early": (2.0, 6.0),     # RIP_EARLY_P1_PCT / RIP_EARLY_P2_PCT
    "A2_actuel_late": (6.0, 8.0),     # RIP_LATE_P1_PCT / RIP_LATE_P2_PCT
}
LADDER_MESURE = (2.0, 6.0)            # même règle, relue dans l'unité de la paire (r ×)


def journal_le_plus_recent():
    fs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")))
    return fs[-1] if fs else None


def charger_klines(pair):
    f = os.path.join(CACHE, f"{pair}_1h_45j.json")
    if not os.path.exists(f):
        return None
    try:
        return json.load(open(f))
    except Exception:
        return None


def lire_entrees(chemin):
    """Les VRAIS achats + la cadence MESURÉE par le moteur (colonne du journal)."""
    out = []
    with open(chemin, newline="") as f:
        for r in csv.DictReader(f):
            if (r.get("event") or "").strip() != "BUY":
                continue
            try:
                ts = int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                         .replace(tzinfo=timezone.utc).timestamp() * 1000)
                px = float(r["price"])
                qty = float(r["qty"])
            except Exception:
                continue
            cad = None
            try:
                c = (r.get("cadence") or "").strip()
                cad = float(c) if c else None
            except Exception:
                cad = None
            out.append({"pair": r["pair"].strip(), "t": ts, "px": px, "qty": qty,
                        "cadence": cad})
    return out


def rejouer(bars, t0, px, niveaux):
    """Rend (pct_net, pct_MFE, pct_MAE). Deux paliers, moitié/moitié, 48 h max, sinon clôture.

    MAE = pire excursion défavorable atteinte : c'est le CÔTÉ RISQUE de la règle (R18 —
    fonds d'épargne). Une sortie plus large se juge sur le gain ET sur ce qu'elle laisse
    encaisser en route."""
    apres = [b for b in bars if b["t"] > t0]
    seuil_ms = t0 + MAX_HOLD_H * 3600 * 1000
    fen = [b for b in apres if b["t"] <= seuil_ms]
    if not apres:
        return None, None, None
    fen = fen or [apres[0]]
    (l1, l2) = niveaux
    rempli = [False, False]
    sortie = [None, None]
    mfe = 0.0
    mae = 0.0
    for b in fen:
        mfe = max(mfe, (b["h"] / px - 1.0) * 100.0)
        mae = min(mae, (b["l"] / px - 1.0) * 100.0)
        if not rempli[0] and b["h"] >= px * (1 + l1 / 100.0):
            rempli[0], sortie[0] = True, px * (1 + l1 / 100.0)
        if not rempli[1] and b["h"] >= px * (1 + l2 / 100.0):
            rempli[1], sortie[1] = True, px * (1 + l2 / 100.0)
        if rempli[0] and rempli[1]:
            break
    cl = fen[-1]["c"]
    for i in (0, 1):
        if not rempli[i]:
            sortie[i] = cl                       # non touché → clôture réelle, pas un prix inventé
    pct = SPLIT * (sortie[0] / px - 1) + SPLIT * (sortie[1] / px - 1)
    return (pct - 2 * FEE) * 100.0, mfe, mae


def main():
    j = journal_le_plus_recent()
    if not j:
        print("aucun journal PAPER_V1_*.csv")
        return 1
    entrees = lire_entrees(j)
    cad_ok = [e["cadence"] for e in entrees if e["cadence"] and e["cadence"] > 0]
    if not cad_ok:
        print("aucune cadence mesurée dans le journal : rien à mesurer (on ne devine pas)")
        return 1
    c_ref = st.median(cad_ok)

    print(f"CHIFFRAGE SORTIE MESURÉE — journal {os.path.basename(j)}")
    print(f"  entrées réelles          : {len(entrees)} dont {len(cad_ok)} avec cadence mesurée")
    print(f"  cadence de référence     : {c_ref:.2f} %/jour (médiane des paires tradées)")
    print(f"  cadences vues            : min {min(cad_ok):.2f} · médiane {c_ref:.2f} · "
          f"max {max(cad_ok):.2f}  → une paire vit {max(cad_ok)/max(min(cad_ok),0.01):.0f}× "
          f"plus large qu'une autre\n")

    kl = {}
    res = []
    for e in entrees:
        if not e["cadence"] or e["cadence"] <= 0:
            continue                      # sans cadence mesurée : on ne devine pas (R17)
        p = e["pair"]
        if p not in kl:
            kl[p] = charger_klines(p)
        bars = kl[p]
        if not bars:
            continue
        r = e["cadence"] / c_ref
        lignes = {}
        mfe, mae = None, None
        for nom, (a, b) in LADDER_FIXE.items():
            pct, m, q = rejouer(bars, e["t"], e["px"], (a, b))
            if pct is None:
                continue
            lignes[nom] = pct
            mfe, mae = m, q
        # B — échelle SYMÉTRIQUE (2 %, 6 %) × r : peut ABBAISSER un palier sous le fixe.
        a, b = LADDER_MESURE
        pct, m, q = rejouer(bars, e["t"], e["px"], (a * r, b * r))
        if pct is not None:
            lignes["B_mesure"] = pct
            mfe, mae = m, q
        # C — PLANCHER MESURÉ : jamais en dessous du fixe ; on n'ÉLARGIT que sur la mesure
        # de la paire (elle est plus large que la médiane → on lui laisse sa place).
        pct, m, q = rejouer(bars, e["t"], e["px"], (max(a, a * r), max(b, b * r)))
        if pct is not None:
            lignes["C_plancher_mesure"] = pct
            mfe, mae = m, q
        # C2 — idem sur la branche LATE (+6/+8) : le plancher y est déjà plus haut.
        (la, lb) = LADDER_FIXE["A2_actuel_late"]
        pct, m, q = rejouer(bars, e["t"], e["px"], (max(la, la * r), max(lb, lb * r)))
        if pct is not None:
            lignes["C2_plancher_late"] = pct
            mfe, mae = m, q
        res.append({"pair": p, "t": e["t"], "cadence": e["cadence"], "r": r,
                    "notional": e["px"] * e["qty"], "mfe_pct": mfe, "mae_pct": mae,
                    **lignes})

    if not res:
        print("aucune entrée rejouable (bougies absentes) — mesure impossible, on ne conclut pas")
        return 1

    def total(cle, v):
        """$ nets de la variante `cle` sur le sous-ensemble v."""
        return sum(x["notional"] * x[cle] / 100.0 for x in v if cle in x)

    n = len(res)
    notion = sum(x["notional"] for x in res)
    print(f"  entrées rejouées         : {n}  · notionnel cumulé {notion:,.0f} $")
    print(f"  r (cadence/paire / réf)  : min {min(x['r'] for x in res):.2f} · "
          f"médiane {st.median([x['r'] for x in res]):.2f} · max {max(x['r'] for x in res):.2f}\n")

    def bloc(titre, v):
        print(f"  --- {titre} (n={len(v)}) ---")
        for cle, libelle in (("A_actuel_early", "A  ACTUEL fixe  +2 %/+6 %"),
                             ("A2_actuel_late", "A2 ACTUEL fixe  +6 %/+8 %"),
                             ("B_mesure", "B  MESURÉ sym. (r ×)      "),
                             ("C_plancher_mesure", "C  PLANCHER mesuré 2/6      "),
                             ("C2_plancher_late", "C2 PLANCHER mesuré 6/8     ")):
            d = total(cle, v)
            print(f"    {libelle:26s} {d:+9.2f} $   "
                  f"({d / notion * 100:+.3f} % du notionnel)")
        da, db = total("A_actuel_early", v), total("B_mesure", v)
        print(f"    → DELTA B − A : {db - da:+9.2f} $")
        return da, db

    print("VERDICT\n")
    da_all, db_all = bloc("TOUT l'échantillon", res)

    # R17.3 — deux horizons : les deux moitiés chronologiques
    res_t = sorted(res, key=lambda x: x["t"])
    cut = len(res_t) // 2
    h1, h2 = res_t[:cut], res_t[cut:]
    print()
    bloc("1re MOITIÉ (horizon 1)", h1)
    print()
    bloc("2e MOITIÉ (horizon 2)", h2)

    # par paire : où l'échelle mesurée gagne-t-elle ?
    par_p = {}
    for x in res:
        par_p.setdefault(x["pair"], []).append(x)
    print("\n  -- carte par paire (B − A, en $) --")
    gains = []
    for p in sorted(par_p, key=lambda k: -st.median([x["cadence"] for x in par_p[k]])):
        v = par_p[p]
        da, db = total("A_actuel_early", v), total("B_mesure", v)
        gains.append(db - da)
        print(f"    {p:12s} cad={st.median([x['cadence'] for x in v]):6.2f} %/j  "
              f"r={st.median([x['r'] for x in v]):5.2f}  n={len(v):2d}  "
              f"A {da:+7.2f} $  B {db:+7.2f} $  Δ {db - da:+7.2f} $")
    pos = sum(1 for g in gains if g > 0)
    print(f"\n    paires où B gagne : {pos}/{len(gains)}")

    # ── R18 — FONDS D'ÉPARGNE : le CÔTÉ RISQUE de chaque échelle ────────────────
    # Une sortie plus large ne se juge pas seulement sur ce qu'elle rapporte : elle se
    # juge sur ce qu'elle laisse encaisser en route. Ici, la perte par trade (borne du
    # capital) et la pire excursion défavorable (MAE).
    print("\n  -- RISQUE (R18 : la perte par trade est la borne qui protège l'épargne) --")
    mae_tous = [x["mae_pct"] for x in res if x["mae_pct"] is not None]
    if mae_tous:
        print(f"     MAE de la période (toutes entrées) : médiane {st.median(mae_tous):.2f} % · "
              f"pire {min(mae_tous):.2f} %")
    risque = {}
    for cle, libelle in (("A_actuel_early", "A  ACTUEL        "),
                         ("C_plancher_mesure", "C  PLANCHER 2/6  "),
                         ("C2_plancher_late", "C2 PLANCHER 6/8  ")):
        v = [x for x in res if cle in x]
        if not v:
            continue
        nets = [x["notional"] * x[cle] / 100.0 for x in v]
        pertes = [n for n in nets if n < 0]
        risque[cle] = {"pire_trade": min(nets), "somme_pertes": sum(pertes),
                       "n_perdants": len(pertes), "gain": sum(nets)}
        print(f"     {libelle} pire trade {min(nets):+6.2f} $ · perdants {len(pertes):2d}/{len(nets)} "
              f"· somme des pertes {sum(pertes):+7.2f} $ · gain {sum(nets):+7.2f} $")
    # Critère R18, sans chiffre inventé : le risque SUPPLÉMENTAIRE doit être PAYÉ par le
    # gain supplémentaire (couverture 1:1 = la simple condition de rentabilité), ET le pire
    # trade ne doit pas empirer. Un pire trade qui empire = interdit, sans discussion :
    # c'est la borne du capital. Sinon : la mesure dit ce qu'on paie et ce qu'on reçoit.
    if "A_actuel_early" in risque:
        ref = risque["A_actuel_early"]
        print("\n     → R18 (critère écrit : couverture 1:1, pire trade non dégradé) :")
        for cle, lib in (("C_plancher_mesure", "C "), ("C2_plancher_late", "C2")):
            if cle not in risque:
                continue
            v = risque[cle]
            d_gain = v["gain"] - ref["gain"]
            d_perte = -(v["somme_pertes"] - ref["somme_pertes"])   # >0 = plus de pertes
            d_pire = v["pire_trade"] - ref["pire_trade"]
            if d_pire < -0.01:
                jug = f"⛔ INTERDIT — le pire trade empire de {d_pire:+.2f} $"
            elif d_perte <= 0:
                jug = "✅ conforme — aucune perte supplémentaire"
            elif d_perte <= d_gain:
                jug = (f"✅ le risque est PAYÉ — {d_perte:+.2f} $ de pertes en plus pour "
                       f"{d_gain:+.2f} $ de gain en plus (ratio 1:{d_gain/d_perte:.1f})")
            else:
                jug = (f"⛔ NE SE PAIE PAS — {d_perte:+.2f} $ de pertes en plus pour "
                       f"{d_gain:+.2f} $ de gain en plus")
            print(f"        {lib} : gain {d_gain:+7.2f} $ · pertes suppl. {d_perte:+7.2f} $ · "
                  f"pire trade {d_pire:+.2f} $ → {jug}")

    # le fait brut qui explique : jusqu'où le prix monte-t-il vraiment (MFE) ?
    mfe = [x["mfe_pct"] for x in res if x["mfe_pct"] is not None]
    if mfe:
        mfe_s = sorted(mfe)
        print(f"\n  -- excursion favorable max (MFE, 48 h) -- médiane {st.median(mfe_s):.2f} % · "
              f"q75 {mfe_s[int(len(mfe_s)*0.75)]:.2f} % · max {max(mfe_s):.2f} %")
        print(f"     part des entrées n'atteignant PAS +2 % : "
              f"{sum(1 for m in mfe if m < 2)/len(mfe)*100:.0f} %  · "
              f"pas +6 % : {sum(1 for m in mfe if m < 6)/len(mfe)*100:.0f} %")

    # R17.3 : une variante ne compte QUE si son signe tient sur les 2 horizons.
    jugement = {}
    for cle in ("B_mesure", "C_plancher_mesure", "C2_plancher_late"):
        d1 = total(cle, h1) - total("A_actuel_early", h1)
        d2 = total(cle, h2) - total("A_actuel_early", h2)
        jugement[cle] = {"d1": d1, "d2": d2, "total": total(cle, res) - da_all,
                         "coherent": d1 > 0 and d2 > 0}
        print(f"  {cle:20s} Δ1re={d1:+7.2f} $  Δ2e={d2:+7.2f} $  Δtot={jugement[cle]['total']:+7.2f} $"
              f"  → {'SIGNE STABLE' if jugement[cle]['coherent'] else 'SIGNE INSTABLE (pas un résultat)'}")
    gagnants = [k for k, v in jugement.items() if v["coherent"] and v["total"] > 0]
    verdict = ("MESURE NON CONCLUANTE — ON NE TOUCHE PAS LA SORTIE" if not gagnants
               else f"CANDIDAT SOUTENU PAR LA MESURE : {', '.join(gagnants)}")
    print(f"\n  DÉCISION : {verdict}")
    print("  (un candidat n'est PAS câblé le jour de sa mesure — E9 : on empile pas.)")

    out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "journal": os.path.basename(j), "n": n, "notionnel": notion,
           "cadence_reference": c_ref, "fee_per_side": FEE, "max_hold_h": MAX_HOLD_H,
           "A_net": round(da_all, 4), "B_net": round(db_all, 4),
           "delta_B_moins_A": round(db_all - da_all, 4),
           "delta_h1": round(total("B_mesure", h1) - total("A_actuel_early", h1), 4),
           "delta_h2": round(total("B_mesure", h2) - total("A_actuel_early", h2), 4),
           "jugement": jugement, "risque": risque, "verdict": verdict,
           "mae_mediane": (st.median(mae_tous) if mae_tous else None),
           "mae_pire": (min(mae_tous) if mae_tous else None),
           "cadences": {"min": min(cad_ok), "mediane": c_ref, "max": max(cad_ok)},
           "par_paire": {p: {"n": len(v),
                             "cadence_med": st.median([x["cadence"] for x in v]),
                             "A": round(total("A_actuel_early", v), 4),
                             "B": round(total("B_mesure", v), 4)}
                         for p, v in par_p.items()},
           "detail": res}
    fn = os.path.join(RUNS, f"CHIFFRAGE_SORTIE_MESUREE_{datetime.now(timezone.utc):%Y%m%d_%H%M}.json")
    json.dump(out, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
