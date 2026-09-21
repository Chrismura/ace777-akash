#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_TIER_B.py — ce que vaut le levier TIER_B_POSITION_MULT, en DOLLARS.

Question (Christophe 21/09) : le sizing par tier est un levier VOULU (famille 16/08,
taille microscopique sur les paires illiquides). Il n'a JAMAIS été chiffré. Or il
coupe la mise par 4 sur des paires qu'on trade vraiment. Donc : on le mesure.

Méthode — contre-factuel à UNE SEULE VARIABLE, sur le journal réel :
  mêmes entrées, mêmes sorties, mêmes prix ; on ne change QUE le multiplicateur
  appliqué aux paires tier B. Le P&L d'une vente est linéaire en taille, donc :
      net(m) = Σ_ventes  pnl_réelle × k(m)
  avec, par lot d'entrée,
      k(m) = min(m × (notionnel_observé / TIER_B_POSITION_MULT), plafond_mur)
             / notionnel_observé
  Le PLAFOND DU MUR (mise_max_pct_mur × mur) est appliqué : c'est lui qui décide,
  pas la stratégie. Une paire déjà collée au plafond ne bougera pas d'un centime —
  on le prouve au lieu de le supposer.

Ce que ce script NE dit PAS : « monte le multiplicateur ». Il dit ce que la taille
a coûté ou protégé. Le risque est montré séparément (somme des ventes perdantes).

Limites assumées : plafond lu sur mur_bid_med du profil 10/09 (le mur live n'est pas
journalisé) ; les sorties ne sont pas rejouées (on tient le calendrier réel) ; le
marché est paper, sans impact de marché.
0 €, lecture seule, aucun ordre.
"""
import csv
import json
import os
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE_DIR, "runs")
PROFILS = os.path.join(BASE_DIR, "strategie", "universe_profils.json")
INVENTAIRE = os.path.join(BASE_DIR, "data", "universe_mexc_inventory.csv")
DEFAUTS = os.path.join(BASE_DIR, "config", "defaults.env")
JOURNAUX = ["runs/PAPER_V1_20260918_165523.csv", "runs/PAPER_V1_20260921_075626.csv"]


def lire_env(cles: set) -> dict:
    out = {}
    with open(DEFAUTS, encoding="utf-8", errors="ignore") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            k, v = ligne.split("=", 1)
            if k.strip() in cles:
                try:
                    out[k.strip()] = float(v.strip())
                except ValueError:
                    pass
    return out


def lire_tiers() -> dict:
    out = {}
    with open(INVENTAIRE, newline="", encoding="utf-8", errors="ignore") as f:
        for r in csv.DictReader(f):
            p = (r.get("pair") or "").strip().upper()
            if p:
                out[p] = (r.get("tier") or "A").strip().upper()
    return out


def lire_plafonds() -> dict:
    """plafond_mur = mur_bid_med × mise_max_pct_mur (le vrai limiteur d'ordre)."""
    out = {}
    try:
        d = json.load(open(PROFILS, encoding="utf-8"))
    except Exception:
        return out
    for k, v in d.items():
        if not isinstance(v, dict):
            continue
        cal = v.get("calib") or {}
        mur = v.get("mur_bid_med")
        pct = cal.get("mise_max_pct_mur")
        if mur and pct:
            out[k.upper()] = float(mur) * float(pct)
    return out


def lire_journal() -> list:
    """Tous les journaux, DÉDOUBLONNÉS : le moteur COPIE son CSV à chaque
    redémarrage (--resume), donc lire deux fichiers compte l'histoire deux fois.
    Le contrôle de fidélité ci-dessous l'aurait attrapé, mais autant ne pas mentir."""
    out = []
    vus = set()
    for rel in JOURNAUX:
        p = os.path.join(BASE_DIR, rel)
        if not os.path.exists(p):
            continue
        with open(p, newline="", encoding="utf-8", errors="ignore") as f:
            for r in csv.DictReader(f):
                cle = (r.get("ts"), (r.get("pair") or "").strip().upper(),
                       (r.get("event") or "").strip().upper(),
                       r.get("price"), r.get("qty"), r.get("pnl_usdt"))
                if cle in vus:
                    continue
                vus.add(cle)
                ev = (r.get("event") or "").strip().upper()
                if not ev:
                    continue
                try:
                    ts = int(datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ")
                             .replace(tzinfo=timezone.utc).timestamp())
                except Exception:
                    continue
                out.append({"ts": ts, "pair": (r.get("pair") or "").strip().upper(),
                            "ev": ev,
                            "px": float(r.get("price") or 0.0),
                            "qty": float(r.get("qty") or 0.0),
                            "pnl": float(r.get("pnl_usdt") or 0.0),
                            "pnl_total": float(r.get("pnl_total") or 0.0)})
    out.sort(key=lambda x: x["ts"])
    return out


def par_vente(rows, tiers, plafonds, m_new, m_actuel):
    """k = facteur appliqué au P&L de chaque vente (FIFO sur les lots d'entrée)."""
    lots = defaultdict(deque)
    out = []
    for r in rows:
        if r["px"] <= 0 or r["qty"] <= 0:
            continue
        if r["ev"] in ("BUY", "DCA"):
            obs = r["px"] * r["qty"]
            est_b = tiers.get(r["pair"]) == "B"
            cap = plafonds.get(r["pair"])
            if est_b and m_actuel > 0:
                # le notionnel AVANT le multiplicateur tier, reconstruit depuis l'observé
                avant = obs / m_actuel
                obs_new = min(m_new * avant, cap) if cap else m_new * avant
                k = obs_new / obs
            else:
                k = 1.0                      # tier A (ou paire inconnue) : inchangé
            lots[r["pair"]].append([r["qty"], k])
        elif r["ev"].startswith(("SELL", "STOP", "BAG")):
            reste, qte, k_moy = r["qty"], r["qty"], 0.0
            poids = 0.0
            while reste > 1e-12 and lots[r["pair"]]:
                lot = lots[r["pair"]][0]
                pris = min(lot[0], reste)
                part = pris / qte
                k_moy += part * lot[1]
                poids += part
                lot[0] -= pris
                reste -= pris
                if lot[0] <= 1e-12:
                    lots[r["pair"]].popleft()
            if poids < 0.999:
                k_moy += (1.0 - poids) * 1.0
            out.append({"pair": r["pair"], "ev": r["ev"], "ts": r["ts"],
                        "pnl": r["pnl"], "k": k_moy})
    out.sort(key=lambda t: t["ts"])
    return out


def drawdown(serie):
    pic, pire = 0.0, 0.0
    for v in serie:
        pic = max(pic, v)
        pire = min(pire, v - pic)
    return pire


def main():
    env = lire_env({"TIER_B_POSITION_MULT"})
    m_actuel = env.get("TIER_B_POSITION_MULT", 0.25)
    tiers = lire_tiers()
    plafonds = lire_plafonds()
    rows = lire_journal()
    tier_b = sorted(p for p, t in tiers.items() if t == "B")
    traitees = sorted({r["pair"] for r in rows if tiers.get(r["pair"]) == "B"})
    print("CHIFFRAGE DU LEVIER TIER B — contre-factuel à UNE variable, journal réel")
    print(f"TIER_B_POSITION_MULT actuel = {m_actuel}\n")
    print(f"inventaire : {len(tier_b)} paire(s) tier B au total")
    print(f"parmi elles, réellement tradées dans le journal : {traitees or '—'}\n")
    if not traitees:
        print("Aucune paire tier B tradée → le levier est INERTE aujourd'hui.")
        return

    resultats = {}
    for m_new in (m_actuel, 0.5, 1.0):
        vs = par_vente(rows, tiers, plafonds, m_new, m_actuel)
        net = sum(v["pnl"] * v["k"] for v in vs)
        gains = sum(v["pnl"] * v["k"] for v in vs if v["pnl"] > 0)
        pertes = sum(v["pnl"] * v["k"] for v in vs if v["pnl"] < 0)
        cum, serie, par_pair = 0.0, [], defaultdict(float)
        for v in vs:
            cum += v["pnl"] * v["k"]
            serie.append(cum)
            par_pair[v["pair"]] += v["pnl"] * v["k"]
        resultats[m_new] = {"net": net, "gains": gains, "pertes": pertes,
                            "dd": drawdown(serie), "par_pair": dict(par_pair)}
        print(f"TIER_B_POSITION_MULT = {m_new:<4} → net {net:+8.2f} $ · "
              f"gains {gains:+8.2f} $ · pertes {pertes:+8.2f} $ · "
              f"pire repli {drawdown(serie):+8.2f} $")

    ref = resultats[m_actuel]
    print("\nDELTA vs aujourd'hui (une seule variable a changé) :")
    for m_new in (0.5, 1.0):
        r = resultats[m_new]
        d = r["net"] - ref["net"]
        print(f"  ×{m_new:<4} : {d:+8.2f} $  "
              f"(gains {r['gains']-ref['gains']:+.2f} $ · "
              f"pertes {r['pertes']-ref['pertes']:+.2f} $ · "
              f"repli {r['dd']-ref['dd']:+.2f} $ — positif = MOINS profond)")
    # Le levier n'est intéressant que si les GAINS progressent plus vite que les
    # PERTES : augmenter la taille sur des paires illiquides, c'est acheter du
    # gain ET du glissement de stop.
    for m_new in (0.5, 1.0):
        r = resultats[m_new]
        dg = r["gains"] - ref["gains"]
        dp = abs(r["pertes"] - ref["pertes"])
        if dg > 0:
            print(f"  ratio gains/pertes ajoutés ×{m_new} : {dg/dp:.2f} : 1"
                  f"{'' if dg/dp >= 1.5 else '  ← insuffisant pour justifier le risque'}")

    print("\nPAR PAIRE (le levier ne touche que les tier B tradées) :")
    for p in traitees:
        a = ref["par_pair"].get(p, 0.0)
        b = resultats[1.0]["par_pair"].get(p, 0.0)
        cap = plafonds.get(p)
        print(f"  {p:11s} réel {a:+7.2f} $ → ×1.0 {b:+7.2f} $  "
              f"(plafond mur {cap:,.2f} $)")
    print("  ⚠ Une paire COLLÉE au plafond du mur ne bouge pas : le limiteur est la")
    print("    liquidité, pas le multiplicateur. Le levier ne vaut que sur l'autre.")

    # Contrôle de fidélité : à multiplicateur inchangé, la reconstruction DOIT
    # retrouver le réalisé du journal. Sinon le modèle ne vaut rien.
    # On prend le DERNIER pnl_total (le réalisé), pas le maximum (un pic d'équité).
    realise = rows[-1]["pnl_total"] if rows else 0.0
    print(f"\nCONTRÔLE DE FIDÉLITÉ — reconstruction vs réalisé du journal : "
          f"{ref['net']:+.2f} $ vs {realise:+.2f} $")
    if abs(ref['net'] - realise) > 0.05 * max(1.0, abs(realise)):
        print("  ⚠ écart > 5 % : le modèle de taille ne reproduit PAS le réel —")
        print("    aucune conclusion de ce chiffrage n'est utilisable en l'état.")
    else:
        print("  OK — le modèle reproduit le réalisé, les contre-factuels sont lisibles.")

    sortie = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "tier_b_position_mult_actuel": m_actuel,
        "paires_tier_b_tradees": traitees,
        "plafonds_mur": {p: plafonds.get(p) for p in traitees},
        "scenarios": {str(k): v for k, v in resultats.items()},
    }
    fn = os.path.join(RUNS, "CHIFFRAGE_TIER_B_"
                      + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M") + ".json")
    json.dump(sortie, open(fn, "w"), ensure_ascii=False, indent=1)
    print(f"\nsortie : {fn}")


if __name__ == "__main__":
    main()
