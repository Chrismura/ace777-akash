#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flux_nets_exchanges.py — SUIVI GRATUIT DES FLUX NETS EXCHANGES (08/09/2026).

Pourquoi : le sniffer du vrai (SNIFF_bitcoin_*) manque d'une donnée pour trancher
accumulation vs distribution — les flux nets in/out des exchanges (payante chez
les pros). Réponse maison : agrégation HORS LIGNE du ledger existant
whales_mouvements.jsonl (29k+ mouvements labellisés depuis le 14/08, produit par
surveiller_whales.py), donc 100 % gratuit, zéro API, zéro clé.

Méthode (honnête, biais documentés) :
  1. Un mouvement du ledger = un txid détecté via une adresse surveillée.
     Le MÊME txid peut apparaître plusieurs fois (les deux extrémités labellisées,
     re-scans) → DÉDUP par txid (on garde la ligne la plus informative : celle
     dont l'adresse surveillée est source OU cible connue du registre).
  2. Direction par rapport à l'ECOSYSTÈME EXCHANGE (registre whales.json) :
     - source exchange → cible NON-exchange  = SORTANT (retrait = biais accumulation)
     - source NON-exchange → cible exchange  = ENTRANT (dépôt = biais distribution)
     - exchange → exchange (interne/changeroom) = NEUTRE (exclu du net, compté à part)
     - source ET cible inconnues (adresse_surveillee dormante par ex.) = NEUTRE
  3. BTC du mouvement = champ "btc" (volume du tx impliquant l'adresse surveillée).
     BIAIS CONNU : c'est le volume OBSERVABLE côté adresses surveillées, pas le
     flux total onchain de l'exchange — indicateur de TENDANCE, pas une balance.
  4. Fenêtre glissante 48h + comparaison 7j → verdict :
     net < -seuil = ACCUMULATION (retraits dominent) ; net > +seuil = DISTRIBUTION ;
     entre les deux = ÉQUILIBRE. Seuil par défaut = 20 % du volume total 48h.

Usage : python3 flux_nets_exchanges.py [--seuil 0.20] [--silencieux]
Sorties : data/flux_nets_latest.json + data/flux_nets_historique.jsonl
Stdlib uniquement, lecture seule sur le ledger, idempotent, fail-open.
"""
import json
import os
import sys
import argparse
from datetime import datetime, timezone, timedelta

HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, "ace777-test-day1")
INDEX = os.path.join(REPO, "Index_Maison")
DATA = os.path.join(INDEX, "data")
LEDGER = os.path.join(DATA, "whales_mouvements.jsonl")
REGISTRE = os.path.join(DATA, "whales.json")
OUT_LATEST = os.path.join(DATA, "flux_nets_latest.json")
OUT_HIST = os.path.join(DATA, "flux_nets_historique.jsonl")

EXCHANGE_TYPES = {"exchange_hot", "exchange_cold", "exchange_reserve"}
SEUIL_RATIO_DEF = 0.20


def charger_registre():
    """Ensemble des adresses labellisées EXCHANGE (tous types exchange_*)."""
    try:
        d = json.load(open(REGISTRE, encoding="utf-8"))
        return {p["address"] for p in d.get("portefeuilles", [])
                if p.get("type") in EXCHANGE_TYPES}
    except Exception:
        return set()


def charger_ledger_dedup():
    """Lit le ledger, déduplique par txid.

    DÉCOUVERTE 08/09 : le ledger est un log de DÉTECTIONS, pas d'événements —
    29 185 lignes pour 36 txid uniques (le scanner re-détecte les mêmes tx
    récentes à chaque passage, jusqu'à 1 917 fois le même txid).
    → On déduplique par txid et on date l'événement à la PREMIÈRE détection
    (min ts), en gardant la ligne la plus informative pour le contenu."""
    par_txid = {}
    n_lignes = n_dup = 0
    try:
        with open(LEDGER, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                n_lignes += 1
                txid = o.get("txid") or ""
                if not txid:
                    continue
                entry = par_txid.get(txid)
                if entry is None:
                    par_txid[txid] = {"ts": o.get("ts", ""), "score": 0, "ligne": o}
                    entry = par_txid[txid]
                else:
                    n_dup += 1
                    if o.get("ts", "") < entry["ts"]:
                        entry["ts"] = o.get("ts", "")
                score = (1 if o.get("sources_type") else 0) + \
                        (1 if o.get("label") else 0)
                if score > entry["score"]:
                    entry["score"] = score
                    entry["ligne"] = o
    except FileNotFoundError:
        return [], {"lignes": 0, "dups": 0, "txid_uniques": 0}
    mouvements = []
    for e in par_txid.values():
        m = dict(e["ligne"])
        m["ts"] = e["ts"]  # date d'événement = première détection
        mouvements.append(m)
    return mouvements, {"lignes": n_lignes, "dups": n_dup,
                        "txid_uniques": len(par_txid)}


def direction(m, exchanges):
    """SORTANT / ENTRANT / NEUTRE par rapport à l'écosystème exchange."""
    src = set(m.get("sources") or [])
    dst = {c.get("adresse") for c in (m.get("cibles") or []) if c.get("adresse")}
    src_ex = bool(src & exchanges)
    dst_ex = bool(dst & exchanges)
    if src_ex and not dst_ex:
        return "SORTANT"
    if dst_ex and not src_ex:
        return "ENTRANT"
    return "NEUTRE"  # exchange→exchange, inconnu→inconnu, etc.


def btc_du_mouvement(m):
    try:
        return max(float(m.get("btc") or 0.0), 0.0)
    except (TypeError, ValueError):
        return 0.0


def _agreger(mouvements, exchanges, t0, t1=None):
    res = {"n": 0, "n_sortant": 0, "n_entrant": 0,
           "btc_sortant": 0.0, "btc_entrant": 0.0, "btc_neutre": 0.0,
           "sortant_vers": {}, "entrant_depuis": {}}
    for m in mouvements:
        ts = m.get("ts") or ""
        if ts < t0 or (t1 and ts >= t1):
            continue
        btc = btc_du_mouvement(m)
        if btc <= 0:
            continue
        res["n"] += 1
        d = direction(m, exchanges)
        if d == "SORTANT":
            res["n_sortant"] += 1
            res["btc_sortant"] += btc
            for c in (m.get("cibles") or []):
                a = c.get("adresse")
                if a and a not in exchanges:
                    res["sortant_vers"][a] = res["sortant_vers"].get(a, 0.0) + float(c.get("btc") or 0.0)
        elif d == "ENTRANT":
            res["n_entrant"] += 1
            res["btc_entrant"] += btc
            for s in (m.get("sources") or []):
                if s not in exchanges:
                    res["entrant_depuis"][s] = res["entrant_depuis"].get(s, 0.0) + btc
        else:
            res["btc_neutre"] += btc
    for k in ("sortant_vers", "entrant_depuis"):
        res[k] = dict(sorted(res[k].items(), key=lambda x: -x[1])[:5])
    return res


def verdict(net_btc, total_btc, seuil_ratio):
    """Verdict honnête : seuil proportionnel au volume observé."""
    if total_btc <= 0:
        return "DONNEES_INSUFFISANTES", "aucun volume observable sur la fenêtre"
    if abs(net_btc) < seuil_ratio * total_btc:
        return "EQUILIBRE", f"|net| {abs(net_btc):.0f} < {seuil_ratio:.0%} du total {total_btc:.0f} BTC"
    if net_btc < 0:
        return "ACCUMULATION", f"retraits dominent : net {net_btc:.0f} BTC (≤ -{seuil_ratio:.0%} du total)"
    return "DISTRIBUTION", f"dépôts dominent : net +{net_btc:.0f} BTC (≥ +{seuil_ratio:.0%} du total)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seuil", type=float, default=SEUIL_RATIO_DEF,
                    help="seuil de verdict en ratio du volume total 48h (déf 0.20)")
    ap.add_argument("--silencieux", action="store_true")
    args = ap.parse_args()

    exchanges = charger_registre()
    mouvements, stats = charger_ledger_dedup()
    now = datetime.now(timezone.utc)

    t48 = (now - timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M")
    t7j = (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M")

    w48 = _agreger(mouvements, exchanges, t48)
    w7j = _agreger(mouvements, exchanges, t7j, t48)  # semaine précédente pour tendance

    net48 = w48["btc_sortant"] - w48["btc_entrant"]
    total48 = w48["btc_sortant"] + w48["btc_entrant"]
    net7j = w7j["btc_sortant"] - w7j["btc_entrant"]
    total7j = w7j["btc_sortant"] + w7j["btc_entrant"]

    v, detail = verdict(net48, total48, args.seuil)

    out = {
        "ts": now.strftime("%Y-%m-%dT%H:%MZ"),
        "methode": "agrégation hors ligne ledger whales_mouvements + dédup txid + registre exchange_*",
        "biais": "volume observable côté adresses surveillées uniquement — tendance, pas balance",
        "stats_ledger": stats,
        "nb_adresses_exchange": len(exchanges),
        "fenetre_48h": {**w48, "net_btc": round(net48, 2), "total_btc": round(total48, 2)},
        "fenetre_7j_precedente": {**w7j, "net_btc": round(net7j, 2), "total_btc": round(total7j, 2)},
        "verdict": v,
        "detail_verdict": detail,
        "seuil_ratio": args.seuil,
    }

    with open(OUT_LATEST, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(OUT_HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False) + "\n")

    if not args.silencieux:
        print(f"[flux_nets] verdict 48h : {v} — {detail}")
        print(f"  SORTANT (retraits)  : {w48['n_sortant']:4d} mvts / {w48['btc_sortant']:12.1f} BTC")
        print(f"  ENTRANT  (dépôts)   : {w48['n_entrant']:4d} mvts / {w48['btc_entrant']:12.1f} BTC")
        print(f"  NEUTRE (intra/obs.) : {w48['btc_neutre']:12.1f} BTC")
        print(f"  NET 48h : {net48:+.1f} BTC | semaine préc. : {net7j:+.1f} BTC")
        print(f"  → {OUT_LATEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
