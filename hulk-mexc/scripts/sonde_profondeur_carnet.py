#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONDE DE PROFONDEUR DU CARNET — LA TAILLE MESURÉE (GO 3, 23/09/2026)
=====================================================================
LE PROBLÈME, tel qu'il est posé aujourd'hui
  La mise annoncée traverse une chaîne de multiplicateurs puis bute sur un plafond
  ARBITRAIRE : `cap = 2 % du mur bid` (paper_driprip.buy, l.2060). Ce « 2 % » est un
  seuil SANS MESURE (règle #17 : un seuil qui n'est pas mesuré ne décide pas, il subit).
  Conséquence chiffrée le 23/09 : ZBCN raboté de −67 %, RIZE de −31 % — et sur RIZE le
  plafond vaut 4,88 $, donc **même un pump de +81,8 % rapporte quelques dollars**.

CE QUE CETTE SONDE MESURE (lecture seule, 0 ordre, 0 €)
  Elle interroge le carnet PUBLIC de MEXC (même endpoint que `poussiere_paire.py` et
  `observer_murs.py` : `/api/v3/depth`) et répond à LA seule question qui compte pour
  remplacer un « 2 % » par une mesure :

      COMBIEN de dollars le carnet absorbe-t-il AVANT que le prix ne bouge de 0,5 % / 1 % / 2 % ?

  Elle donne, par paire :
    · le spread (coût d'entrée immédiat, en bps) ;
    · la profondeur CUMULÉE disponible sous −0,5 / −1 / −2 % (et symétriquement les asks) ;
    · la part du carnet qui disparaîtrait si on prenait la taille actuelle du moteur ;
    · le plus gros niveau (le mur) et ce que représente le plafond actuel (`2 % du mur`)
      FACE à cette profondeur → le plafond est-il prudent, ou ridiculement bas ?

LIMITES DÉCLARÉES (E8) — non négociables
  · Un instantané de carnet est PÉRISSABLE : il bouge en secondes (les niveaux « fantômes »
    de la maison, mesurés à 8,8 % de la valeur affichée, le prouvent). Ce chiffre est une
    PHOTO, pas une moyenne : il faut le répéter pour en tirer une règle.
  · Le carnet AFFICHÉ n'est pas le carnet EXÉCUTABLE (spoofing, annulations).
  · Cette sonde ne prend AUCUN ordre et ne modifie RIEN : elle mesure.
Usage :
  python3 sonde_profondeur_carnet.py                       # les paires du moteur
  python3 sonde_profondeur_carnet.py --paires RIZEUSDT,TELUSDT --json runs/PROF.json
"""
import argparse
import json
import os
import urllib.parse
import urllib.request

CORE = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT", "WUSDT",
        "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT", "TELUSDT", "CHIPUSDT",
        "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT", "RWAUSDT", "MNSRYUSDT"]
PALIERS = (0.5, 1.0, 2.0)   # déplacements de prix mesurés (en %), symétriques
RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")


def gj(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def carnet(paire, limite=1000):
    q = urllib.parse.urlencode({"symbol": paire, "limit": limite})
    try:
        return gj(f"https://api.mexc.com/api/v3/depth?{q}")
    except Exception as e:
        return {"_err": str(e)}


def cote(niveaux, paliers, sens):
    """sens=+1 : bids (on descend depuis le meilleur bid) · sens=-1 : asks.
    Renvoie, pour chaque palier, la valeur USD cumulée accessible DANS le palier."""
    if not niveaux:
        return None
    best = float(niveaux[0][0])
    niveaux = [(float(p), float(q)) for p, q in niveaux if float(p) > 0 and float(q) > 0]
    if not niveaux:
        return None
    niveaux.sort(key=lambda x: -x[0] if sens > 0 else x[0])
    lim = {"best": best, "paliers": {}, "mur": max(v for _p, v in niveaux),
           "n_niveaux": len(niveaux)}
    for pct in paliers:
        borne = best * (1 - pct / 100) if sens > 0 else best * (1 + pct / 100)
        cum = 0.0
        for p, q in niveaux:
            if (sens > 0 and p >= borne) or (sens < 0 and p <= borne):
                cum += p * q
            else:
                break
        impact = (abs(best / (niveaux[-1][0] or best) - 1) * 100) if len(niveaux) > 1 else 0
        lim["paliers"][pct] = round(cum, 1)
    return lim


def mesure(paire):
    d = carnet(paire)
    if d.get("_err") or not d.get("bids") or not d.get("asks"):
        return {"paire": paire, "erreur": d.get("_err", "carnet vide")}
    bids, asks = cote(d["bids"], PALIERS, +1), cote(d["asks"], PALIERS, -1)
    mid = (bids["best"] + asks["best"]) / 2
    spread_bps = (asks["best"] - bids["best"]) / mid * 10000
    mur = bids["mur"]
    cap_2pct = mur * 0.02                      # LE plafond actuel du moteur
    p = bids["paliers"][2.0]                   # profondeur mesurée sous −2 %
    return {"paire": paire, "spread_bps": round(spread_bps, 1),
            "bid_deep_usd": bids["paliers"], "ask_deep_usd": asks["paliers"],
            "mur_top_usd": round(mur, 1), "plafond_actuel_2pct_usd": round(cap_2pct, 2),
            "profondeur_2pct_usd": round(p, 1),
            "plafond_sur_profondeur_pct": round(cap_2pct / p * 100, 2) if p else None}


def analyser_serie(chemin):
    """LIT la série et sort LA mesure utilisable : une MÉDIANE, pas une photo.
    C'est la seule forme sous laquelle un carnet périsable peut servir à décider."""
    import statistics as st
    par = {}
    with open(chemin, encoding="utf-8", errors="ignore") as f:
        for l in f:
            try:
                d = json.loads(l)
            except Exception:
                continue
            if d.get("erreur"):
                continue
            par.setdefault(d["paire"], []).append(d)
    print(f"SÉRIE : {chemin}")
    print(f"{'paire':10}{'n':>5}{'méd −0,5%':>12}{'méd −2%':>11}{'spread méd':>12}"
          f"{'plafond méd':>13}{'plaf/prof méd':>15}  stabilité −2%")
    for p, v in sorted(par.items(), key=lambda kv: -len(kv[1])):
        if len(v) < 2:
            continue
        d05 = [x["bid_deep_usd"]["0.5"] if "0.5" in x["bid_deep_usd"] else x["bid_deep_usd"][0.5]
               for x in v]
        d2 = [x["profondeur_2pct_usd"] for x in v]
        sp = [x["spread_bps"] for x in v]
        cap = [x["plafond_actuel_2pct_usd"] for x in v]
        rat = [x["plafond_sur_profondeur_pct"] for x in v
               if x.get("plafond_sur_profondeur_pct") is not None]
        stab = ("stable" if len(d2) > 2 and st.median(d2) > 0 and
                (max(d2) - min(d2)) / st.median(d2) < 1.0 else "INSTABLE (min-max > 100 %)")
        print(f"{p.replace('USDT', ''):10}{len(v):>5}{st.median(d05):>11.0f}$"
              f"{st.median(d2):>10.0f}${st.median(sp):>10.1f}b"
              f"{st.median(cap):>11.2f}${st.median(rat):>13.2f}%  {stab}")
    print("\n  ⚠️ Une MÉDIANE de carnet reste une mesure d'AFFICHAGE : elle ne prouve pas le"
          "\n     remplissage. Elle sert à fixer un ordre de grandeur de taille, jamais un P&L.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paires", default="")
    ap.add_argument("--json", default="")
    ap.add_argument("--serie", default="",
                    help="append d'un instantané en JSONL (la SÉRIE, seule base d'une règle)")
    ap.add_argument("--serie-analyse", default="", metavar="FICHIER",
                    help="lit la série et sort les MÉDIANES par paire")
    a = ap.parse_args()
    if a.serie_analyse:
        return analyser_serie(a.serie_analyse)
    paires = [p.strip() for p in a.paires.split(",") if p.strip()] or CORE
    res = []
    for p in paires:
        res.append(mesure(p))
    ok = [r for r in res if not r.get("erreur")]
    print("SOURCE : carnet public MEXC (/api/v3/depth, limit=1000) — LECTURE SEULE, 0 ordre")
    print("MESURE : dollars absorbables AVANT que le prix ne bouge de 0,5 / 1 / 2 %\n")
    print(f"{'paire':10}{'spread':>8}{'<−0,5%':>11}{'<−1%':>10}{'<−2%':>10}"
          f"{'mur(top)':>11}{'plafond 2%':>12}{'plaf/prof':>10}")
    for r in sorted(ok, key=lambda x: -(x["bid_deep_usd"].get(2.0) or 0)):
        d = r["bid_deep_usd"]
        print(f"{r['paire'].replace('USDT', ''):10}{r['spread_bps']:>7.1f}b"
              f"{d[0.5]:>10.0f}${d[1.0]:>9.0f}${d[2.0]:>9.0f}$"
              f"{r['mur_top_usd']:>10.0f}${r['plafond_actuel_2pct_usd']:>11.2f}$"
              f"{r['plafond_sur_profondeur_pct']:>9.2f}%")
    for r in res:
        if r.get("erreur"):
            print(f"  ⚠️ {r['paire']} : {r['erreur']} (aucune mesure — on ne déclare pas)")
    if ok:
        pct = [r["plafond_sur_profondeur_pct"] for r in ok if r["plafond_sur_profondeur_pct"]]
        if pct:
            print(f"\n  → le plafond actuel (2 % du mur) mord en moyenne "
                  f"{sum(pct) / len(pct):.2f} % de la profondeur mesurée sous −2 %")
            print(f"     min {min(pct):.2f} % · max {max(pct):.2f} %  → "
                  f"{'LE PLAFOND EST TRÈS CONSERVATEUR' if max(pct) < 50 else 'le plafond est proche du carnet'}")
    print("\n  ⚠️ PORTÉE (E8) : photo instantanée d'un carnet PÉRISSABLE (les niveaux fantômes"
          "\n     mesurés par la maison valent 8,8 % de la valeur affichée) — à répéter avant"
          "\n     d'en tirer une règle. Le carnet affiché n'est pas le carnet exécutable.")
    if a.json and ok:
        json.dump({"paliers_pct": list(PALIERS), "mesures": res},
                  open(a.json, "w"), ensure_ascii=False, indent=2)
        print(f"  (mesures écrites : {a.json})")
    if a.serie:
        import time as _t
        from datetime import datetime as _dt, timezone as _tz
        ts = _dt.now(_tz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        os.makedirs(os.path.dirname(a.serie) or ".", exist_ok=True)
        with open(a.serie, "a", encoding="utf-8") as f:
            for r in res:
                f.write(json.dumps({"ts": ts, "ts_epoch": _t.time(), **r},
                                   ensure_ascii=False) + "\n")
        print(f"  (série : +{len(res)} ligne(s) → {a.serie})")
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
