#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_SORTIE_CALIBREE.py — ce que la sortie calibrée vaut en DOLLARS, sur les
MÊMES entrées réelles du moteur (aucune entrée inventée).

Question (GO Christophe 21/09 : « 1 ») : le replay_amplitude dit que la sortie à la
fenêtre de pic recalculée fait ~3× la règle fixe `+2 %`. Combien ça vaut, en $, sur
les VRAIS achats du moteur papier ?

Méthode :
  - entrées = les événements BUY du journal réel (ts, paire, prix, qty) — inchangés.
  - prix de sortie :
      S1 (ACTUEL fixe) : 1re bougie 1h après l'entrée où high ≥ entrée × 1,02 → +2 % ;
                         sinon dernière clôture connue.
      S2 (CALIBRÉ)     : fenêtre de pic recalée sur les 7 jours PRÉCÉDENTS (walk-forward),
                         h_pic = heure UTC au prix moyen le plus haut ; sortie à la
                         clôture de la 1re bougie après l'entrée dont l'heure ∈ h_pic ± 1.
                         Si la fenêtre est déjà passée ce jour-là → lendemain. Garde-fou :
                         détention max 48 h, sinon dernière clôture.
  - frais 10 bps aller-retour (5 bps/côté, tarif maison).
  - aucun ordre, aucun € — recherche pure.

Limite assumée et écrite : on remplace TOUTE la mécanique de sortie par une sortie
unique (le moteur réel fait des scale-outs partiels 2×/rip). Ce chiffrage isole donc
l'EFFET DE LA RÈGLE DE SORTIE sur des entrées identiques ; il ne prédit pas le PnL
exact du moteur patché.
"""
import csv
import json
import os
from datetime import datetime, timezone
from statistics import median

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
JOURNAL = os.path.join(RUNS, "PAPER_V1_20260918_165523.csv")
W_CAL_J = 7          # jours de calibration glissante avant chaque entrée
FEE = 0.0005         # 5 bps par côté
MAX_HOLD_H = 48      # garde-fou de détention pour S2


def jour(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def heure(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).hour


def charger_klines(pair):
    f = os.path.join(CACHE, f"{pair}_1h_45j.json")
    if not os.path.exists(f):
        return None
    return json.load(open(f))


def calibrer_fenetres(bars, t0_ms):
    """h_creux + h_pic sur les W_CAL_J jours PRÉCÉDENTS l'entrée (aucune fuite)."""
    debut = t0_ms - W_CAL_J * 86400 * 1000
    cal = [b for b in bars if debut <= b["t"] < t0_ms]
    if len(cal) < 24 * 3:
        return None
    par_h = {}
    for b in cal:
        par_h.setdefault(heure(b["t"]), []).append(b["c"])
    moy = {h: sum(v) / len(v) for h, v in par_h.items() if v}
    if len(moy) < 12:
        return None
    return {"h_creux": min(moy, key=moy.get), "h_pic": max(moy, key=moy.get)}


def entree_fenetre(bars, t0_ms, h, meme_jour=True):
    """Prix d'entrée à la 1re bougie dont l'heure ∈ h±1.
    meme_jour=True : reste sur le jour de t0 (substitut d'entrée) ; sinon 1re après t0."""
    fen = {(h - 1) % 24, h, (h + 1) % 24}
    if meme_jour:
        j0 = jour(t0_ms)
        cand = [b for b in bars if jour(b["t"]) == j0 and heure(b["t"]) in fen]
    else:
        cand = [b for b in bars if b["t"] > t0_ms and heure(b["t"]) in fen]
    return cand[0] if cand else None


def sortie_s1(apres, px_in):
    for b in apres:
        if b["h"] >= px_in * 1.02:
            return px_in * 1.02
    return apres[-1]["c"] if apres else px_in


def sortie_s2(apres, px_in, h_pic):
    fen = {(h_pic - 1) % 24, h_pic, (h_pic + 1) % 24}
    t_lim = apres[0]["t"] + MAX_HOLD_H * 3600 * 1000 if apres else 0
    for b in apres:
        if b["t"] > t_lim:
            break
        if heure(b["t"]) in fen:
            return b["c"]
    return apres[-1]["c"] if apres else px_in


def lire_achats():
    out = []
    with open(JOURNAL, newline="") as f:
        for r in csv.DictReader(f):
            if r["event"].strip() != "BUY":
                continue
            try:
                out.append({
                    "pair": r["pair"].strip(),
                    "t": int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                             .replace(tzinfo=timezone.utc).timestamp() * 1000),
                    "px": float(r["price"]),
                    "qty": float(r["qty"]),
                })
            except Exception:
                continue
    return out


def main():
    achats = lire_achats()
    print(f"CHIFFRAGE SORTIE CALIBRÉE — {len(achats)} entrées réelles du journal\n")
    kl = {}
    res, sautes = [], 0
    for a in achats:
        pair = a["pair"]
        if pair not in kl:
            kl[pair] = charger_klines(pair)
        bars = kl[pair]
        if not bars:
            sautes += 1
            continue
        cal = calibrer_fenetres(bars, a["t"])
        apres = [b for b in bars if b["t"] > a["t"]]
        if not cal or not apres:
            sautes += 1
            continue
        h_pic, h_creux = cal["h_pic"], cal["h_creux"]
        px1 = sortie_s1(apres, a["px"])
        px2 = sortie_s2(apres, a["px"], h_pic)
        notional = a["px"] * a["qty"]
        net1 = (px1 / a["px"] - 1 - 2 * FEE) * notional
        net2 = (px2 / a["px"] - 1 - 2 * FEE) * notional
        # variante ENTRÉE AU CREUX (le même jour) + sorties S1/S2
        e_creux = entree_fenetre(bars, a["t"], h_creux)
        net3 = net4 = None
        if e_creux:
            px_e = e_creux["c"]
            ap2 = [b for b in bars if b["t"] > e_creux["t"]]
            x1 = sortie_s1(ap2, px_e)
            x2 = sortie_s2(ap2, px_e, h_pic)
            net3 = (x1 / px_e - 1 - 2 * FEE) * notional
            net4 = (x2 / px_e - 1 - 2 * FEE) * notional
        res.append({"pair": pair, "jour": jour(a["t"]), "notional": notional,
                    "pct1": (px1 / a["px"] - 1) * 100, "pct2": (px2 / a["px"] - 1) * 100,
                    "net1": net1, "net2": net2, "net3": net3, "net4": net4,
                    "h_pic": h_pic, "h_creux": h_creux})

    n = len(res)
    if not n:
        print("aucune entrée exploitable")
        return
    s1 = sum(x["net1"] for x in res)
    s2 = sum(x["net2"] for x in res)
    eng = sum(x["notional"] for x in res)
    print(f"entrées exploitées : {n}  (sautées faute de klines : {sautes})")
    print(f"notionnel cumulé   : {eng:,.0f} $\n")
    print(f"  S1  entrée réelle + sortie +2 % : {s1:+8.2f} $  "
          f"(moy {s1/n:+.3f} $/entrée · {sum(x['pct1'] for x in res)/n:+.2f} %/entrée)")
    print(f"  S2  entrée réelle + sortie pic  : {s2:+8.2f} $  "
          f"(moy {s2/n:+.3f} $/entrée · {sum(x['pct2'] for x in res)/n:+.2f} %/entrée)")
    print(f"  DELTA S2−S1                     : {s2-s1:+8.2f} $")
    # variantes entrée au creux (uniquement les entrées où une fenêtre de creux existe)
    cr = [x for x in res if x["net3"] is not None and x["net4"] is not None]
    if cr:
        m = len(cr)
        s3 = sum(x["net3"] for x in cr)
        s4 = sum(x["net4"] for x in cr)
        s1c = sum(x["net1"] for x in cr)
        s2c = sum(x["net2"] for x in cr)
        print(f"\n  -- sous-ensemble avec fenêtre de creux dispo ({m}/{n} entrées) --")
        print(f"  A entrée réelle + +2 %  : {s1c:+8.2f} $")
        print(f"  B entrée réelle + pic   : {s2c:+8.2f} $")
        print(f"  C entrée creux  + +2 %  : {s3:+8.2f} $")
        print(f"  D entrée creux  + pic   : {s4:+8.2f} $")
        print(f"  → meilleure combinaison : "
              f"{max((('A',s1c),('B',s2c),('C',s3),('D',s4)), key=lambda t:t[1])[0]}")
    # walk-forward : 1re moitié vs 2e
    cut = n // 2
    for lbl, part in (("1re moitié", res[:cut]), ("2e moitié", res[cut:])):
        if part:
            print(f"  {lbl:12s} S1 {sum(x['net1'] for x in part):+7.2f} $ · "
                  f"S2 {sum(x['net2'] for x in part):+7.2f} $")
            pc = [x for x in part if x['net3'] is not None]
            if pc:
                print(f"  {'':12s} creux+2% {sum(x['net3'] for x in pc):+7.2f} $ · "
                      f"creux+pic {sum(x['net4'] for x in pc):+7.2f} $")

    # carte par paire
    par_p = {}
    for x in res:
        par_p.setdefault(x["pair"], []).append(x)
    print("\n  -- carte par paire (net $ · %moy S1 → %moy S2) --")
    for p in sorted(par_p, key=lambda k: -sum(y["net2"] for y in par_p[k])):
        v = par_p[p]
        print(f"  {p:11s} n={len(v):2d}  S1 {sum(y['net1'] for y in v):+7.2f} $  "
              f"S2 {sum(y['net2'] for y in v):+7.2f} $  "
              f"({sum(y['pct1'] for y in v)/len(v):+.2f} % → {sum(y['pct2'] for y in v)/len(v):+.2f} %)")

    # carte datée par paire (h_pic médian observé sur la période)
    carte = {}
    for p, v in par_p.items():
        vc = [y for y in v if y["net3"] is not None]
        carte[p] = {"h_pic_median": median([y["h_pic"] for y in v]),
                    "h_creux_median": median([y["h_creux"] for y in v]),
                    "n_entrees": len(v),
                    "net_s1": round(sum(y["net1"] for y in v), 4),
                    "net_s2": round(sum(y["net2"] for y in v), 4),
                    "net_creux_2pct": round(sum(y["net3"] for y in vc), 4) if vc else None,
                    "net_creux_pic": round(sum(y["net4"] for y in vc), 4) if vc else None}
    out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "n_entrees": n, "borne": eng, "fee_per_side": FEE, "max_hold_h": MAX_HOLD_H,
           "S1_net": round(s1, 4), "S2_net": round(s2, 4), "delta": round(s2 - s1, 4),
           "par_paire": carte, "detail": res}
    fn = os.path.join(RUNS, f"CHIFFRAGE_SORTIE_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.json")
    json.dump(out, open(fn, "w"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")


if __name__ == "__main__":
    main()
