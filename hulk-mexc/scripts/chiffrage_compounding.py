#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_COMPOUNDING.py — ce que le levier compounding vaut en DOLLARS sur le
journal RÉEL du moteur (aucun trade inventé, 0 €, lecture seule).

Question (Christophe 21/09) : « ne pas considérer le compounding c'est très grave
dans une stratégie ». Le compounding est un LEVIER VOULU (comme l'amplitude) :
ici on le MESURE, on ne le plafonne pas.

Ce que fait le moteur (paper_diprip.current_notional) :
    notional = base + 0.50 × max(0, pnl_total)          (le PnL réalisé regrossit la taille)
             = max(base×0.5, base + 0.25×pnl_total)     si pnl_total < 0  (défensif)
    borné à [base×0.5 ; base×3.0]

CE QUE CE SCRIPT A DÉCOUVERT (et qui change la lecture) :
    current_notional() est une taille ANNONCÉE, pas la taille ENGAGÉE. Entre les
    deux, buy() applique une CHAÎNE de multiplicateurs :
        × bag (0.5) · × tier B (0.25) · × mur adaptatif (0.6-1.2)
        × fusible étage 2 (0-1) · × slip gate (0.5)
        puis PLAFOND = 2 % du mur live de la paire (mise_max_pct_mur)
    Conséquence mesurée : les achats sortent en moyenne à ×0.33 du notional annoncé
    → le compounding n'est PAS le levier qui fixe la taille. Le facteur qui mord
    le plus souvent, c'est le PLAFOND DU MUR (preuve : les lignes « plafonnée »
    du log). On le mesure ici, on ne le juge pas.

Mesures :
  1. DILUTION  — notionnel annoncé (current_notional) vs notionnel réellement engagé.
  2. LEVIER    — contre-factuel à UNE SEULE VARIABLE : mêmes tours, mêmes %, même
                 chaîne de multiplicateurs, seul COMPOUND_ON passe de 1 à 0
                 (facteur = base / notional_annoncé de l'entrée).
  3. BORNE HAUTE NON EXÉCUTABLE — si la mise pleine (notional annoncé) passait sans
                 être rabotée par le mur : borne théorique, PAS une consigne.
  4. RISQUE    — drawdown des deux courbes (le levier amplifie les deux sens).

Limites assumées : health_mult non journalisé (facteur commun) ; un tour avec
DCA/2× est scalé d'un bloc (approximation) ; marché paper, aucun impact de marché.
"""
import bisect
import csv
import json
import os
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE_DIR, "runs")
DEFAUTS = os.path.join(BASE_DIR, "config", "defaults.env")
JOURNAL_DEFAUT = os.path.join(RUNS, "PAPER_V1_20260918_165523.csv")


def lire_config() -> dict:
    """Lit les bornes RÉELLES du compounding dans la config du moteur."""
    cfg = {"NOTIONAL_USDT": 30.0, "COMPOUND_FRAC": 0.50, "COMPOUND_MAX_MULT": 3.0}
    if os.path.exists(DEFAUTS):
        with open(DEFAUTS, encoding="utf-8", errors="ignore") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#") or "=" not in ligne:
                    continue
                k, v = ligne.split("=", 1)
                if k.strip() in cfg:
                    try:
                        cfg[k.strip()] = float(v.strip())
                    except ValueError:
                        pass
    return cfg


def lire_journal(chemin: str) -> list:
    out = []
    with open(chemin, newline="", encoding="utf-8", errors="ignore") as f:
        for r in csv.DictReader(f):
            ev = (r.get("event") or "").strip().upper()
            if not ev:
                continue
            try:
                ts = int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                         .replace(tzinfo=timezone.utc).timestamp())
                out.append({
                    "ts": ts, "pair": (r.get("pair") or "").strip(), "ev": ev,
                    "px": float(r.get("price") or 0.0), "qty": float(r.get("qty") or 0.0),
                    "pnl": float(r.get("pnl_usdt") or 0.0),
                    "pnl_total": float(r.get("pnl_total") or 0.0),
                })
            except Exception:
                continue
    out.sort(key=lambda x: x["ts"])
    return out


def notional_annonce(base: float, frac: float, mult: float, pnl_total: float) -> float:
    """Reproduit EXACTEMENT current_notional() du moteur (sans health_mult)."""
    grown = base + max(0.0, pnl_total) * frac
    if pnl_total < 0:
        grown = max(base * 0.5, base + pnl_total * 0.25)
    return min(max(grown, base * 0.5), base * mult)


def ventes(rows: list, base: float, frac: float, mult: float) -> list:
    """Chaque VENTE réelle du journal, appariée FIFO à ses lots d'entrée.

    On renvoie, par vente, les facteurs qui isolent UNE variable :
      - f_fixe  = la taille passe de annonce(t) à `base` (COMPOUND_ON 0/1)
      - f_plein = la taille passe de l'engagé réel à l'annoncé (effet du mur)
    Le pnl de la vente reste EXACTEMENT celui du journal → le total reconstruit
    doit égaler le réalisé (contrôle de fidélité).
    """
    lots = defaultdict(deque)
    out = []
    for r in rows:
        if r["qty"] <= 0 or r["px"] <= 0:
            continue
        if r["ev"] in ("BUY", "DCA"):
            ann = notional_annonce(base, frac, mult, r["pnl_total"])
            lots[r["pair"]].append({"ts": r["ts"], "qty": r["qty"],
                                    "obs": r["px"] * r["qty"], "ann": ann})
        elif r["ev"].startswith(("SELL", "STOP", "BAG")):
            reste, qte = r["qty"], r["qty"]
            f_fixe, f_plein, poids = 0.0, 0.0, 0.0
            while reste > 1e-12 and lots[r["pair"]]:
                lot = lots[r["pair"]][0]
                pris = min(lot["qty"], reste)
                part = pris / qte
                f_fixe += part * (base / lot["ann"] if lot["ann"] else 0.0)
                f_plein += part * (lot["ann"] / lot["obs"] if lot["obs"] else 0.0)
                poids += part
                lot["qty"] -= pris
                reste -= pris
                if lot["qty"] <= 1e-12:
                    lots[r["pair"]].popleft()
            if poids < 0.999:   # vente orpheline (bag créé hors lot) → facteur neutre
                manque = 1.0 - poids
                ann = notional_annonce(base, frac, mult, r["pnl_total"])
                f_fixe += manque * (base / ann)
                f_plein += manque
            out.append({"pair": r["pair"], "ts": r["ts"], "ev": r["ev"],
                        "qty": r["qty"], "px": r["px"],
                        "pnl": r["pnl"], "f_fixe": f_fixe, "f_plein": f_plein})
    out.sort(key=lambda t: t["ts"])
    return out


def drawdown(serie: list) -> float:
    pic, pire = 0.0, 0.0
    for v in serie:
        pic = max(pic, v)
        pire = min(pire, v - pic)
    return pire


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else JOURNAL_DEFAUT
    cfg = lire_config()
    base, frac, mult = cfg["NOTIONAL_USDT"], cfg["COMPOUND_FRAC"], cfg["COMPOUND_MAX_MULT"]
    rows = lire_journal(chemin)
    ts_list = ventes(rows, base, frac, mult)
    print(f"CHIFFRAGE COMPOUNDING — {os.path.basename(chemin)}")
    print(f"base={base:.0f} $ · frac={frac:.2f} · plafond compounding={base*mult:.0f} $ "
          f"({base:.0f}×{mult:.1f})\n")
    print(f"lignes journal : {len(rows)} · ventes réelles appariées : {len(ts_list)}\n")

    # ---- 1. DILUTION : annoncé vs réellement engagé ----
    print("1) DILUTION — le notionnel ENGAGÉ n'est pas le notionnel ANNONCÉ")
    idx_ts = [r["ts"] for r in rows]

    def pnl_avant(t: int) -> float:
        i = bisect.bisect_right(idx_ts, t) - 1
        return rows[i]["pnl_total"] if i >= 0 else 0.0

    obs_n, ann_n = [], []
    for r in rows:
        if r["ev"] in ("BUY", "DCA") and r["px"] > 0 and r["qty"] > 0:
            obs_n.append(r["px"] * r["qty"])
            ann_n.append(notional_annonce(base, frac, mult, pnl_avant(r["ts"])))
    if obs_n:
        ratios = sorted(o / a for o, a in zip(obs_n, ann_n) if a > 0)
        med = ratios[len(ratios) // 2]
        print(f"   achats comparés : {len(obs_n)}")
        print(f"   notionnel ANNONCÉ : {min(ann_n):6.2f} → {max(ann_n):6.2f} $ "
              f"(moy {sum(ann_n)/len(ann_n):.2f} $)")
        print(f"   notionnel ENGAGÉ  : {min(obs_n):6.2f} → {max(obs_n):6.2f} $ "
              f"(moy {sum(obs_n)/len(obs_n):.2f} $)")
        print(f"   ratio engagé/annoncé — médiane {med:.3f} · "
              f"moyenne ×{(sum(obs_n)/len(obs_n))/(sum(ann_n)/len(ann_n)):.3f}")
        print("   → le compounding n'est donc PAS ce qui fixe la taille : une CHAÎNE")
        print("     de multiplicateurs (bag · tier B · mur adaptatif · fusible · slip)")
        print("     rabote la mise avant l'exécution. Aucun de ces 5 leviers n'est")
        print("     mesuré (cf. audit_leviers_moteur.py : 63 leviers monétaires aveugles).\n")

    # ---- 2. LEVIER : une seule variable change (COMPOUND_ON 1 → 0) ----
    net_reel, net_fixe, net_plein = 0.0, 0.0, 0.0
    c_reel, c_fixe = [], []
    agg = agg_f = 0.0
    par_pair = defaultdict(lambda: [0.0, 0.0])
    for t in ts_list:
        fixe = t["pnl"] * t["f_fixe"]       # seule la taille change : base au lieu de compound
        plein = t["pnl"] * t["f_plein"]     # taille annoncée au lieu de l'engagée
        net_reel += t["pnl"]
        net_fixe += fixe
        net_plein += plein
        agg += t["pnl"]
        agg_f += fixe
        c_reel.append(agg)
        c_fixe.append(agg_f)
        par_pair[t["pair"]][0] += t["pnl"]
        par_pair[t["pair"]][1] += fixe
    n = len(ts_list)
    print("2) LEVIER COMPOUNDING — contre-factuel à UNE variable (COMPOUND_ON=0)")
    print(f"   AVEC compounding (réel)          : {net_reel:+8.2f} $")
    print(f"   SANS compounding (taille = base) : {net_fixe:+8.2f} $")
    delta = net_reel - net_fixe
    print(f"   DELTA du levier                  : {delta:+8.2f} $"
          + (f"  ({delta/abs(net_fixe)*100:+.1f} % du net fixe)" if net_fixe else ""))
    if net_fixe:
        print(f"   amplification du résultat        : ×{net_reel/net_fixe:.3f}")
    print()

    # ---- 3. BORNE HAUTE NON EXÉCUTABLE ----
    print("3) BORNE HAUTE NON EXÉCUTABLE (si le mur ne rabotait rien)")
    print(f"   mise pleine = notional annoncé   : {net_plein:+8.2f} $")
    print(f"   coût de la dilution (plein−réel) : {net_plein-net_reel:+8.2f} $")
    print(f"   contrôle de fidélité — total reconstruit vs journal : "
          f"{net_reel:+.2f} $ vs {rows[-1]['pnl_total']:+.2f} $")
    print("   ⚠ Cette borne N'EST PAS une consigne : le plafond 2 % du mur existe")
    print("     parce que le carnet ne peut pas absorber plus (slippage garanti).")
    print("     Elle dit seulement QUI mord en premier : la liquidité, pas le compounding.\n")

    # ---- 3bis. QUI FIXE LA TAILLE ? (le plafond du mur, ou la stratégie ?) ----
    profils_p = os.path.join(BASE_DIR, "strategie", "universe_profils.json")
    murs = {}
    try:
        _d = json.load(open(profils_p, encoding="utf-8"))
        _p = _d.get("paires") or _d
        for _k, _v in _p.items():
            if isinstance(_v, dict) and _v.get("mur_bid_med"):
                murs[_k] = float(_v["mur_bid_med"])
    except Exception:
        pass
    au_plafond, sous_plafond, sans_mur = 0, 0, 0
    debrides = []
    for r in rows:
        if r["ev"] not in ("BUY", "DCA") or r["px"] <= 0 or r["qty"] <= 0:
            continue
        med = murs.get(r["pair"])
        if not med:
            sans_mur += 1
            continue
        cap = med * 0.02          # mise_max_pct_mur (défaut du moteur)
        obs = r["px"] * r["qty"]
        if cap > 0 and obs >= cap * 0.95:
            au_plafond += 1
            debrides.append((r["pair"], obs, cap, med))
        else:
            sous_plafond += 1
    tot = au_plafond + sous_plafond
    if tot:
        print("3bis) QUI FIXE LA TAILLE ? (plafond = 2 % du mur médian de la paire)")
        print(f"   achats COLLÉS au plafond du mur : {au_plafond}/{tot} "
              f"({au_plafond/tot*100:.0f} %)")
        print(f"   achats sous le plafond          : {sous_plafond}/{tot} "
              f"({sous_plafond/tot*100:.0f} %)")
        pr = defaultdict(int)
        for p, o, c, m in debrides:
            pr[p] += 1
        top = ", ".join(f"{p.replace('USDT','')}×{n}" for p, n in
                        sorted(pr.items(), key=lambda x: -x[1])[:8])
        print(f"   → paires contraintes par le mur : {top}")
        print(f"   → {au_plafond/tot*100:.0f} % des achats butent sur le mur ; pour les autres,")
        print("     c'est la CHAÎNE de multiplicateurs qui rabote (aucun n'est mesuré).")
        print("     Dans les deux cas, la taille n'est pas décidée par la stratégie :")
        print("     elle est subie. C'est ICI qu'est la plus-value non prise.\n")

    # ---- 4. RISQUE ----
    dd_reel, dd_fixe = drawdown(c_reel), drawdown(c_fixe)
    print("4) RISQUE (le levier amplifie les deux sens)")
    print(f"   pire repli AVEC compounding : {dd_reel:+8.2f} $")
    print(f"   pire repli SANS compounding : {dd_fixe:+8.2f} $")
    if dd_fixe:
        print(f"   net/repli — AVEC {net_reel/abs(dd_reel):.2f} · SANS {net_fixe/abs(dd_fixe):.2f}")
    print()

    # ---- 5. CARTE PAR PAIRE ----
    print("5) PAR PAIRE (réel → sans compounding)")
    for p in sorted(par_pair, key=lambda k: -par_pair[k][0]):
        reel, fixe = par_pair[p]
        print(f"   {p:11s} réel {reel:+7.2f} $ → fixe {fixe:+7.2f} $  (delta {reel-fixe:+6.2f})")

    sortie = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "journal": os.path.basename(chemin), "base": base, "frac": frac, "max_mult": mult,
        "plafond_compounding": base * mult, "n_tours": n,
        "notional_annonce_moyen": round(sum(ann_n) / len(ann_n), 4) if ann_n else None,
        "notional_engage_moyen": round(sum(obs_n) / len(obs_n), 4) if obs_n else None,
        "ratio_engage_annonce": (round((sum(obs_n) / len(obs_n)) / (sum(ann_n) / len(ann_n)), 4)
                                 if obs_n and ann_n else None),
        "net_reel": round(net_reel, 4), "net_sans_compound": round(net_fixe, 4),
        "delta_levier": round(delta, 4), "delta_pct": (round(delta / abs(net_fixe) * 100, 2)
                                                       if net_fixe else None),
        "net_mise_pleine_NON_EXECUTABLE": round(net_plein, 4),
        "cout_dilution": round(net_plein - net_reel, 4),
        "dd_reel": round(dd_reel, 4), "dd_sans_compound": round(dd_fixe, 4),
        "par_paire": {p: [round(v[0], 4), round(v[1], 4)] for p, v in par_pair.items()},
    }
    fn = os.path.join(RUNS, "CHIFFRAGE_COMPOUNDING_"
                      + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M") + ".json")
    json.dump(sortie, open(fn, "w"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")


if __name__ == "__main__":
    main()
