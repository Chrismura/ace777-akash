#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_GARDES_REFUS.py — « ce que chaque garde d'entrée nous coûte ou nous protège ».

Question (Christophe 21/09) : « comment savoir toutes les choses que je n'ai pas
vues et corriger ce qui améliore HULK ? »

Méthode — ON NE DEVINE PAS, ON LIT LE JOURNAL :
  le journal écrit, pour CHAQUE refus, la paire et le PRIX du moment. Il contient
  donc, gratuitement, un mois de série de prix par paire (~150 000 points). On peut
  alors répondre à la seule question qui compte pour une garde :
      « après avoir refusé, le prix est parti OÙ ? »
  Si le prix monte (+rip) la garde nous a coûté ; s'il chute (−stop) elle nous a protégé.

Ce qu'on simule (le setup PROPRE de chaque paire, lu dans universe_profils.json) :
  entrée = prix du refus · vente de RIP_SELL_FRAC à +rip_pct · STOP = tout à −stop_pct
  · à la fin de l'horizon, le reste est soldé au dernier prix connu
  · coût de passage = 2 × spread (entrée + sortie), bps du profil.
Un refus ne dit pas « j'aurais pris ce trade » — il dit « le prix, ici, allait faire ça ».

PRÉCAUTIONS (à lire avant tout go) :
  1. On déduplique en ÉPISODES (1 h d'écart mini par paire et par garde) : compter
     50 000 polls du même refus ne mesure rien.
  2. La mesure est une BORNE : elle suppose UNE entrée par épisode et ignore que
     retirer une garde change tout l'état du moteur (positions, cash, cooldowns).
     Donc : ça dit QUI mord et dans quel sens, jamais « supprime la garde ».
  3. Fail-open : une paire sans profil → on prend les seuils plancher de la config.
0 €, lecture seule, aucun ordre.
"""
import bisect
import csv
import glob
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE_DIR, "runs")
PROFILS = os.path.join(BASE_DIR, "strategie", "universe_profils.json")
DEFAUTS = os.path.join(BASE_DIR, "config", "defaults.env")

# Journaux de la LIGNE COURANTE (même machine d'état, repris par --resume).
#
# FIX 22/09/2026 — l'instrument lisait une liste de journaux ÉCRITE EN DUR et
# donc PÉRIMÉE : il ne voyait plus rien depuis le 21/09 13:22Z (les nouvelles
# gardes, dont FENETRE_ENTREE, étaient invisibles). Leçon « une seule vérité » :
# le journal canonique est celui du POINTEUR (chaque --resume copie le journal du
# précédent dans le nouveau → la chaîne est continue et le pointeur contient TOUT,
# cf. le même choix dans fusibles_paires.py). Repli : le CSV le plus récent.
def _journaux() -> list[str]:
    try:
        with open(os.path.join(RUNS, ".hulk_resume_pointer"), encoding="utf-8") as f:
            ptr = f.read().strip()
        if ptr:
            csv_ = os.path.join(RUNS, os.path.basename(ptr).replace("_state.json", ".csv"))
            if os.path.exists(csv_):
                return [csv_]
    except Exception:
        pass
    cands = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")),
                   key=os.path.getmtime, reverse=True)
    return cands[:1]


JOURNAUX = _journaux()

HORIZON_H = 24.0        # durée d'observation après un refus
ESPACEMENT_S = 3600     # un épisode = au moins 1 h d'écart (sinon c'est le même refus)
COUVERTURE_MIN = 0.60   # il faut au moins 60 % de l'horizon en données


def lire_config() -> dict:
    cfg = {"RIP_SELL_FRAC": 0.50, "DIP_FLOOR_PCT": 4.0,
           "RIP_FLOOR_PCT": 2.0, "STOP_FLOOR_PCT": 6.0}
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


def lire_profils() -> dict:
    """Seuils PROPRES à chaque paire (dip/rip/stop + coût de spread)."""
    out = {}
    try:
        d = json.load(open(PROFILS, encoding="utf-8"))
    except Exception:
        return out
    for k, v in d.items():
        if not isinstance(v, dict) or "calib" not in v:
            continue
        c = v.get("calib") or {}
        out[k.upper()] = {
            "rip": float(c.get("rip_pct") or 0.0),
            "stop": float(c.get("stop_pct") or 0.0),
            "dip": float(c.get("dip_pct") or 0.0),
            "spread_bps": float(v.get("spread_bps_med") or 0.0),
        }
    return out


def classer(reason: str) -> str:
    """Code de garde lisible — le VOL est éclaté en ses SEUILS (DEAD/DRY/OK)."""
    r = (reason or "").strip()
    code = r.split(":")[0].strip() or "?"
    if code == "VOL":
        if "_DEAD" in r:
            return "VOL vol_dry < VX_DEAD"
        if "_DRY" in r and "impulse" in r:
            return "VOL vol_dry (impulse_block)"
        if "_DRY" in r:
            return "VOL vol_dry < VX_DRY"
        if "_OK" in r:
            return "VOL vol_dry < VX_OK"
        return "VOL (autre)"
    return code


def charger_journal(chemins: list) -> tuple:
    """Série de prix par paire (numpy) + liste des refus à mesurer.

    DÉDOUBLONNAGE OBLIGATOIRE : le moteur COPIE son journal à chaque redémarrage
    (--resume). Lire deux fichiers sans filtrer compte chaque refus deux fois et
    gonfle tous les totaux (leçon du 21/09 : fidélité cassée de +20 $).
    """
    par_pair = defaultdict(list)      # pair -> [(ts, px)]
    refus = []                        # (pair, ts, px, code)
    vus = set()
    for rel in chemins:
        p = rel if os.path.isabs(rel) else os.path.join(BASE_DIR, rel)
        if not os.path.exists(p):
            continue
        with open(p, newline="", encoding="utf-8", errors="ignore") as f:
            for r in csv.DictReader(f):
                pair = (r.get("pair") or "").strip().upper()
                if not pair:
                    continue
                cle = (r.get("ts"), pair, (r.get("event") or "").strip().upper(),
                       r.get("price"), r.get("reason"))
                if cle in vus:
                    continue
                vus.add(cle)
                try:
                    ts = int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                             .replace(tzinfo=timezone.utc).timestamp())
                    px = float(r.get("price") or 0.0)
                except Exception:
                    continue
                if px <= 0:
                    continue
                par_pair[pair].append((ts, px))
                if (r.get("event") or "").strip().upper() == "SKIP":
                    refus.append({"pair": pair, "ts": ts, "px": px,
                                  "code": classer(r.get("reason"))})
    series = {}
    for pair, pts in par_pair.items():
        pts.sort()
        ts = np.array([t for t, _ in pts], dtype=np.int64)
        px = np.array([q for _, q in pts], dtype=np.float64)
        keep = np.concatenate(([True], np.diff(ts) > 0))
        series[pair] = (ts[keep], px[keep])
    return series, refus


def episodes(refus: list) -> list:
    """Un refus = un ÉPISODE (au moins ESPACEMENT_S depuis le dernier de même garde)."""
    dernier = {}
    out = []
    for r in sorted(refus, key=lambda x: x["ts"]):
        cle = (r["pair"], r["code"])
        if r["ts"] - dernier.get(cle, -10 ** 12) < ESPACEMENT_S:
            continue
        dernier[cle] = r["ts"]
        out.append(r)
    return out


def simuler(ts, px, i, rip, stop, frac, cout_bps, horizon_s):
    """Suit le setup PROPRE de la paire sur le chemin de prix qui a suivi le refus."""
    p0 = float(px[i])
    fin = int(ts[i]) + horizon_s
    j = int(np.searchsorted(ts, fin, side="right"))
    if j - i < 5:
        return None
    couv = (int(ts[j - 1]) - int(ts[i])) / horizon_s
    if couv < COUVERTURE_MIN:
        return None
    seg = px[i:j]
    haut, bas = float(seg.max()), float(seg.min())
    mfe = (haut / p0 - 1.0) * 100.0
    mae = (bas / p0 - 1.0) * 100.0
    # marche avant : qui est touché en premier, le rip ou le stop ?
    reste = 1.0
    pnl_pct = 0.0
    k = i + 1
    cible_rip, cible_stop = p0 * (1 + rip / 100.0), p0 * (1 - stop / 100.0)
    touche_rip = touche_stop = False
    while k < j and reste > 1e-9:
        q = float(px[k])
        if not touche_rip and rip > 0 and q >= cible_rip:
            pnl_pct += reste * frac * (q / p0 - 1.0) * 100.0
            reste -= reste * frac
            touche_rip = True
        if q <= cible_stop:
            pnl_pct += reste * (q / p0 - 1.0) * 100.0
            reste = 0.0
            touche_stop = True
            break
        k += 1
    if reste > 1e-9:                      # horizon atteint : on solde au dernier prix
        pnl_pct += reste * (float(px[j - 1]) / p0 - 1.0) * 100.0
    pnl_pct -= cout_bps / 100.0           # coût de passage entrée+sortie (bps → %)
    return {"mfe": mfe, "mae": mae, "pnl_pct": pnl_pct,
            "rip": touche_rip, "stop": touche_stop, "couv": couv}


def main():
    horizon_h = float(sys.argv[1]) if len(sys.argv) > 1 else HORIZON_H
    jours = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0   # 0 = tout le journal
    horizon_s = int(horizon_h * 3600)
    cfg = lire_config()
    profils = lire_profils()
    series, refus = charger_journal(JOURNAUX)
    eps = episodes(refus)
    # FILTRE DE PÉRIODE (garde anti-illusion n°1) : une fuite passée n'est pas un
    # chantier. On regarde ce que fait le MOTEUR ACTUEL, pas ce qu'il faisait il y
    # a trois semaines.
    if jours > 0:
        fin = max(e["ts"] for e in eps) if eps else 0
        debut = fin - int(jours * 86400)
        eps = [e for e in eps if e["ts"] >= debut]
        print(f"fenêtre : {jours:.0f} derniers jours (depuis "
              f"{datetime.fromtimestamp(debut, timezone.utc):%d/%m %H:%M}Z)")
    print(f"CHIFFRAGE DES GARDES D'ENTRÉE — horizon {horizon_h:.0f} h")
    print(f"journal : {len(refus)} refus bruts → {len(eps)} ÉPISODES (1 h d'écart mini)")
    print(f"paires avec série de prix : {len(series)} · profils par paire : {len(profils)}\n")

    par_garde = defaultdict(list)
    for e in eps:
        s = series.get(e["pair"])
        if s is None:
            continue
        ts, px = s
        i = int(np.searchsorted(ts, e["ts"], side="right")) - 1
        if i < 0:
            continue
        pr = profils.get(e["pair"]) or {}
        rip = pr.get("rip") or cfg["RIP_FLOOR_PCT"]
        stop = pr.get("stop") or cfg["STOP_FLOOR_PCT"]
        cout = 2.0 * (pr.get("spread_bps") or 0.0)
        r = simuler(ts, px, i, rip, stop, cfg["RIP_SELL_FRAC"], cout, horizon_s)
        if r:
            r["pair"] = e["pair"]
            r["ts"] = e["ts"]
            par_garde[e["code"]].append(r)

    notion = 30.0   # base_notional : sert à traduire un % en $
    total_n = sum(len(v) for v in par_garde.values())
    print("=" * 96)
    print(f"{'GARDE':34s} {'n':>6s} {'MFE%':>7s} {'MAE%':>7s} {'rip%':>6s} {'stop%':>6s}"
          f" {'E/trade%':>9s} {'$ simulés':>10s} {'1re paire':>12s}")
    print("=" * 96)
    lignes = []
    for code, lst in par_garde.items():
        n = len(lst)
        mfe = float(np.median([x["mfe"] for x in lst]))
        mae = float(np.median([x["mae"] for x in lst]))
        pr = 100.0 * sum(1 for x in lst if x["rip"]) / n
        ps = 100.0 * sum(1 for x in lst if x["stop"]) / n
        e = float(np.mean([x["pnl_pct"] for x in lst]))
        # GARDE ANTI-ILLUSION n°2 : quelle part du résultat porte UNE SEULE paire ?
        # Un « levier » qui vient à 80 % d'une paire à gros spread n'est pas un levier.
        par_pair = defaultdict(float)
        for x in lst:
            par_pair[x["pair"]] += x["pnl_pct"]
        conc = 0.0
        top_p = ""
        if par_pair and e != 0:
            p_tot = sum(abs(v) for v in par_pair.values())
            p_top = max(par_pair.values(), key=abs)
            conc = 100.0 * abs(p_top) / p_tot if p_tot else 0.0
            top_p = max(par_pair, key=lambda k: abs(par_pair[k]))
        lignes.append({"code": code, "n": n, "mfe": mfe, "mae": mae,
                       "p_rip": pr, "p_stop": ps, "e_pct": e,
                       "dollars": e / 100.0 * notion * n,
                       "concentration_pct": round(conc, 1),
                       "paire_dominante": top_p,
                       "premier_ts": min(x["ts"] for x in lst),
                       "dernier_ts": max(x["ts"] for x in lst),
                       "par_paire": {p: round(v, 1) for p, v in par_pair.items()}})
    lignes.sort(key=lambda x: -x["dollars"])
    for L in lignes:
        marque = ""
        if L["concentration_pct"] >= 70:
            marque = f"⚠ {L['concentration_pct']:.0f}% {L['paire_dominante'].replace('USDT','')}"
        d1 = datetime.fromtimestamp(L["premier_ts"], timezone.utc).strftime("%d/%m")
        d2 = datetime.fromtimestamp(L["dernier_ts"], timezone.utc).strftime("%d/%m")
        print(f"{L['code']:34s} {L['n']:6d} {L['mfe']:+7.2f} {L['mae']:+7.2f}"
              f" {L['p_rip']:6.0f} {L['p_stop']:6.0f} {L['e_pct']:+9.3f}"
              f" {L['dollars']:+10.2f} {d1}-{d2:>7s} {marque}")
    print("=" * 96)
    print(f"épisodes mesurés : {total_n} · notion de référence : {notion:.0f} $/trade\n")
    print("GARDES ANTI-ILLUSION (ce qui empêche de se tromper) :")
    print("  · colonne dates → une « fuite » qui s'arrête il y a une semaine n'est pas")
    print("    un chantier : c'est de l'histoire ;")
    print("  · ⚠ % → un effet porté à ≥70 % par UNE paire n'est pas un levier, c'est une")
    print("    anecdote (souvent une paire à gros spread qui fausse la simulation).")

    print("LECTURE — le signe de « $ simulés » dit le SENS de la garde :")
    print("  négatif = la garde NOUS PROTÈGE (les refus auraient perdu) ;")
    print("  positif = la garde NOUS COÛTE (les refus auraient gagné).")
    print("  ⚠ Ce n'est PAS « supprime la garde » : la mesure suppose 1 entrée par")
    print("    épisode et ignore que l'état du moteur change tout entier. C'est une")
    print("    CARTE DE PRIORITÉ : voilà les gardes qui méritent d'être chiffrées en vrai.")

    sortie = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "horizon_h": horizon_h, "notion": notion,
        "episodes": total_n, "refus_bruts": len(refus),
        "gardes": lignes,
    }
    fn = os.path.join(RUNS, "CHIFFRAGE_GARDES_"
                      + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M") + ".json")
    json.dump(sortie, open(fn, "w"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")


if __name__ == "__main__":
    main()
