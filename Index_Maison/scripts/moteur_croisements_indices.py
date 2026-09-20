#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moteur_croisements_indices.py — P2 du chantier CORTANA_ANALYSTE (GO Christophe 12/09)
Rôle : croiser plusieurs indices indépendants (règle maison des 2 sources)
       et n'émettre un avis QUE quand 2 sources tirer dans le même sens.

Croisements implémentés (tous documentés au corpus de leçons) :
  C1 "régime × levier"      : régime de fond (P1, LECON-032) × funding/oi
                              - HAUSSIER + funding > fundingAvg30  → levier suit la tendance
                              - HAUSSIER + takerRatio < 1          → divergence vendeurs agressifs
  C2 "levier × purge"       : funding × liquidations 24h
                              - funding < seuil zone morte (règle 31/08) → signal inexistant
                              - funding ≥ zone morte + liqLong >> liqShort → purge des longs
  C3 "onchain × prix"       : flux nets baleines 48h (flux_nets_latest) × variation prix 24h
                              - flux opposé au prix = divergence (LECON onchain : biais observable)

Honnêteté :
  - 0 croisement ne tire  → AUCUN avis écrit (le scoreur note "sans_verdict", c'est voulu)
  - 1 source seule tire   → pas d'avis (règle des 2 sources), juste une ligne historique
  - 2 sources tirent      → AVIS STRICT LONG/SHORT/NEUTRE noté par le scoreur comme les autres

Produits :
  - data/croisements_indices_hist.jsonl   (append-only, rotation [C5] 50 Mo)
  - data/croisements_indices_etat.json    (anti-figage md5 3 cycles, zéro sirène [C4])
  - 1 ligne dans thermo/analyses/<jour>.jsonl quand un avis est émis (canal standard du scoreur)

Lecture seule partout ailleurs. Jamais d'alarme, jamais d'écriture moteur/profils/config.
"""

import json
import hashlib
import os
import re
from datetime import datetime, timezone, timedelta

BASE = os.path.expanduser("~/ace777-test-day1")
DATA = os.path.join(BASE, "Index_Maison", "data")
THERMO = os.path.join(BASE, "Index_Maison", "thermo")
ANALYSES_DIR = os.path.join(THERMO, "analyses")

HIST = os.path.join(DATA, "croisements_indices_hist.jsonl")
ETAT = os.path.join(DATA, "croisements_indices_etat.json")
LIVE = os.path.join(THERMO, "live.json")
P1_HIST = os.path.join(DATA, "paternes_btc_hist.jsonl")
FLUX_NETS = os.path.join(DATA, "flux_nets_latest.json")
JUSTESSE = os.path.join(BASE, "Index_Maison", "scripts", "justesse_cockpit.json")

SEUIL_LIQ_RATIO = 2.0   # liqLong > 2x liqShort = purge unilatérale des longs
SEUIL_FLUX_BTC = 5.0    # ±5 BTC en 48h sur adresses surveillées = mouvement notable


def now_z():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def charger_json(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def charger_p1():
    """Dernière ligne du moteur P1 (régime de fond, MACD filtre)."""
    try:
        with open(P1_HIST, encoding="utf-8") as f:
            lignes = [l for l in f.read().splitlines() if l.strip()]
        return json.loads(lignes[-1]) if lignes else None
    except Exception:
        return None


def val_num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def croisements(live, p1, flux, seuil_zone_morte):
    """Calcule les 3 croisements. Retourne (liste, sources_actives)."""
    res = []

    mark = val_num(live.get("mark"))
    chg24 = val_num(live.get("chg24"))
    funding = val_num(live.get("funding"))
    funding_avg30 = val_num(live.get("fundingAvg30"))
    taker = val_num(live.get("takerRatio"))
    liq_long = val_num(live.get("liqLongUsd"))
    liq_short = val_num(live.get("liqShortUsd"))

    regime = (p1 or {}).get("regime_fond", {}).get("regime")

    # ---- C1 : régime de fond × levier -------------------------------------
    c1 = {"id": "C1", "nom": "régime × levier", "sources": [], "sens": None, "preuve": ""}
    if regime == "HAUSSIER" and funding is not None and funding_avg30:
        if funding > funding_avg30:
            c1["sources"].append("P1:HAUSSIER")
            c1["sources"].append("funding>avg30")
            c1["sens"] = "LONG"
            c1["preuve"] = "funding %.1e > avg30 %.1e" % (funding, funding_avg30)
        elif taker is not None and taker < 1.0:
            c1["sources"].append("P1:HAUSSIER")
            c1["sources"].append("taker<1")
            c1["sens"] = "NEUTRE"
            c1["preuve"] = "vendeurs agressifs (taker %.2f) contre tendance haussière" % taker
    res.append(c1)

    # ---- C2 : levier × purge ----------------------------------------------
    c2 = {"id": "C2", "nom": "levier × purge", "sources": [], "sens": None, "preuve": ""}
    if funding is not None and seuil_zone_morte:
        if funding < seuil_zone_morte:
            c2["sources"].append("funding<zone_morte")
            c2["sens"] = "NEUTRE"
            c2["preuve"] = "zone morte (règle 31/08) : funding %.1e < %.1e, signal inexistant" % (funding, seuil_zone_morte)
        elif liq_long is not None and liq_short is not None and liq_short > 0:
            ratio = liq_long / liq_short
            if ratio > SEUIL_LIQ_RATIO:
                c2["sources"].append("funding>=zone_morte")
                c2["sources"].append("liqLong>2x liqShort")
                c2["sens"] = "SHORT"
                c2["preuve"] = "purge unilatérale des longs : %.0f$ vs %.0f$ (x%.1f)" % (liq_long, liq_short, ratio)
    res.append(c2)

    # ---- C3 : onchain × prix ----------------------------------------------
    c3 = {"id": "C3", "nom": "onchain × prix", "sources": [], "sens": None, "preuve": ""}
    if flux:
        f48 = flux.get("fenetre_48h") or {}
        net = val_num(f48.get("net_btc"))
        if net is not None and chg24 is not None and abs(net) >= SEUIL_FLUX_BTC and abs(chg24) >= 1.0:
            sortie = net < 0  # BTC quitte les exchanges surveillés
            prix_baisse = chg24 < 0
            if sortie and prix_baisse:
                c3["sources"] = ["flux48h:%+.1f BTC" % net, "prix:%+.1f%%" % chg24]
                c3["sens"] = "NEUTRE"  # cohérent, rien à dire
                c3["preuve"] = "flux et prix d'accord : sortie d'exchange + baisse (déjà intégré)"
            elif (not sortie) and prix_baisse:
                c3["sources"] = ["flux48h:%+.1f BTC" % net, "prix:%+.1f%%" % chg24]
                c3["sens"] = "LONG"
                c3["preuve"] = "divergence : entrée %.1f BTC sur exchanges pendant baisse %.1f%% (achat possible)" % (net, chg24)
            elif sortie and (not prix_baisse):
                c3["sources"] = ["flux48h:%+.1f BTC" % net, "prix:%+.1f%%" % chg24]
                c3["sens"] = "SHORT"
                c3["preuve"] = "divergence : sortie %.1f BTC des exchanges pendant hausse %.1f%% (distribution possible)" % (abs(net), chg24)
    res.append(c3)

    return res


def ecrire_ligne_hist(ligne):
    nouveau = not os.path.exists(HIST)
    os.makedirs(DATA, exist_ok=True)
    with open(HIST, "a", encoding="utf-8") as f:
        if nouveau:
            f.write("")  # le fichier naît vide, rotation gérée par rotation_jsonl.py
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")


def ecrire_avis_analyses(faits, crois_actifs, ts_iso):
    """Écrit l'avis au canal standard du scoreur (thermo/analyses/<jour>.jsonl)."""
    jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    chemin = os.path.join(ANALYSES_DIR, jour + ".jsonl")
    os.makedirs(ANALYSES_DIR, exist_ok=True)

    noms = " ; ".join("%s (%s)" % (c["id"], c["nom"]) for c in crois_actifs)
    preuves = " | ".join("%s : %s" % (c["id"], c["preuve"]) for c in crois_actifs)
    avis = crois_actifs[0]["sens"]

    texte = (
        "FAITS : croisement multi-indices — %d source(s) par croisement, règle des 2 sources respectée.\n"
        "Croisements actifs : %s.\n"
        "PREUVES : %s.\n\n"
        "MISE EN RELATION : deux familles d'instruments indépendants pointent dans le même sens "
        "en même temps — c'est la définition d'un croisement exploitable (règle maison des 2 sources).\n\n"
        "AVIS STRICT : %s\nHORIZON : 24h\nCONFIANCE : moyenne" % (2, noms, preuves, avis)
    )

    ligne = {
        "ts": ts_iso,
        "indice": "croisements",
        "provider": "Buffy-P2",
        "faits": {"croisements": {c["id"]: c["preuve"] for c in crois_actifs},
                  "nb_actifs": len(crois_actifs)},
        "faits_bruts": faits,
        "analyse": texte,
        "avis_ok": True,
    }
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    return chemin


def main():
    ts = now_z()
    live = charger_json(LIVE) or {}
    p1 = charger_p1()
    flux = charger_json(FLUX_NETS) or {}
    jm = charger_json(JUSTESSE) or {}
    seuil_zone_morte = val_num((jm.get("zone_morte") or {}).get("seuil_funding")) or 0.0002

    crois = croisements(live, p1, flux, seuil_zone_morte)
    actifs = [c for c in crois if len(c["sources"]) >= 2 and c["sens"] is not None]

    faits_bruts = {k: live.get(k) for k in
                   ("mark", "chg24", "funding", "fundingAvg30", "takerRatio",
                    "liq24Usd", "liqLongUsd", "liqShortUsd")}

    ligne_hist = {
        "ts": ts,
        "prix_btc": faits_bruts["mark"],
        "croisements": {c["id"]: {"nom": c["nom"], "sources": c["sources"],
                                  "sens": c["sens"], "preuve": c["preuve"]} for c in crois},
        "nb_actifs": len(actifs),
        "avis_emis": actifs[0]["sens"] if actifs else None,
        "note_lecons": "C1=LECON-032 (régime) · C2=règle zone morte 31/08 · C3=LECON onchain (biais observable)",
        "sources": ["thermo/live.json", "paternes_btc_hist.jsonl (P1)", "flux_nets_latest.json", "justesse_cockpit.json"],
    }
    ecrire_ligne_hist(ligne_hist)

    # avis au canal du scoreur SEULEMENT si croisement confirmé
    chemin_avis = None
    if actifs:
        ts_iso = datetime.now(timezone.utc).isoformat()
        chemin_avis = ecrire_avis_analyses(faits_bruts, actifs, ts_iso)

    # anti-figage : md5 du CONTENU (croisements), pas du timestamp
    payload = json.dumps(ligne_hist["croisements"], sort_keys=True)
    md5 = hashlib.md5(payload.encode()).hexdigest()
    etat = charger_json(ETAT) or {}
    fige = etat.get("fige_consecutifs", 0)
    if etat.get("md5_payload") == md5:
        fige += 1
    else:
        fige = 0
    etat_nouveau = {
        "ts": ts,
        "md5_payload": md5,
        "fige_consecutifs": fige,
        "alerte_figee": fige >= 3,
        "avis_emis": actifs[0]["sens"] if actifs else None,
        "nb_actifs": len(actifs),
        "note": "fige_consecutifs = payload identique sur cycles consécutifs (3 = source potentiellement morte); lu à l'analyse, jamais de sirène",
    }
    with open(ETAT, "w", encoding="utf-8") as f:
        json.dump(etat_nouveau, f, ensure_ascii=False, indent=2)

    print("[%s] croisements: C1=%s C2=%s C3=%s | actifs=%d | avis=%s | fige=%d/3"
          % (ts,
             crois[0]["sens"] or "-", crois[1]["sens"] or "-", crois[2]["sens"] or "-",
             len(actifs), (actifs[0]["sens"] if actifs else "aucun"), fige))
    if chemin_avis:
        print("avis écrit ->", os.path.relpath(chemin_avis, BASE))


if __name__ == "__main__":
    main()
