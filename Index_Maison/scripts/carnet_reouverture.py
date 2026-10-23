#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""carnet_reouverture.py — LE PARTENAIRE MÉCANIQUE (GO Christophe 24/10).

Christophe ne sera pas toujours là : ce que Buffy a fait à la main (carnet des
8 bloquées + distance à réouverture) devient un script qui tourne seul.
LECTURE SEULE : lit state + seuils + thermo live, écrit
Index_Maison/thermo/carnet_reouverture_live.json. ZÉRO effet trading
(aucun import moteur, aucune écriture runs/, aucun ordre).
Règles verrouillées : seuils = 2x range7j MESURÉ par paire (jamais de fixe) ;
contexte bear = mêmes 4 votes pré-enregistrés que chiffrage_devil_bear
(L/S>=2, funding>1.5xavg, chg24<=-1, climat hot), >= 2 votes = bear ;
déblocage = prix seul (jamais d'horloge). Fail-open : paire sans données =
« inconnue », jamais bloquée par ce carnet (il n'est qu'un avis).
"""
import json
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
STATE = ROOT + "/hulk-mexc/runs/PAPER_V1_20261018_100103_state.json"
SEUILS = ROOT + "/hulk-mexc/runs/seuils_paires_live.json"
THERMO = ROOT + "/Index_Maison/thermo/live.json"
OUT = ROOT + "/Index_Maison/thermo/carnet_reouverture_live.json"
EXCL = {"FLUIDUSDT", "HBARUSDT", "CHIPUSDT"}  # mesurées (tue-amplitude / edge+)


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def contexte_bear():
    """Contexte macro actuel (thermo live) — mêmes 4 votes pré-enregistrés."""
    try:
        t = json.load(open(THERMO, encoding="utf-8"))
    except Exception as e:
        return None, f"thermo illisible: {e}"
    votes, why = [], []
    try:
        ls = float(t.get("longShort") or 0)
    except Exception:
        ls = 0.0
    if ls >= 2.0:
        votes.append(f"L/S {ls:.2f}>=2")
    try:
        f, fa = float(t.get("funding") or 0), float(t.get("fundingAvg30") or 0)
    except Exception:
        f, fa = 0.0, 0.0
    if fa > 0 and f > 1.5 * fa:
        votes.append("funding>1.5xavg")
    try:
        c24 = float(t.get("chg24") or 0)
    except Exception:
        c24 = 0.0
    if c24 <= -1.0:
        votes.append(f"chg24 {c24:.2f}<=-1")
    if (t.get("climate") or "") == "hot":
        votes.append("climat hot")
    return (len(votes) >= 2), ("+".join(votes) if votes else "calme")


def main():
    try:
        st = json.load(open(STATE, encoding="utf-8"))
        seuils = json.load(open(SEUILS, encoding="utf-8"))["paires"]
    except Exception as e:
        print(f"lecture impossible : {e}")
        return 2
    sc = st.get("scores", {}) or {}
    bear, why = contexte_bear()
    lignes = []
    for pair in sorted(set(list(sc.keys()) + list(seuils.keys()))):
        v = seuils.get(pair) or {}
        s = sc.get(pair) or {}
        seuil = float(v.get("seuil_interrupt_pct") or 0.0)
        try:
            dd = float(s.get("dd15_pct"))
            dd_ok = True
        except Exception:
            dd, dd_ok = 0.0, False
        px = s.get("price") or 0.0
        peak = s.get("peak15") or 0.0
        if pair in EXCL:
            statut = "exclue (amplitude protégée, mesuré)"
            manque = None
        elif not seuil or not dd_ok:
            statut = "inconnue (fail-open : jamais bloquée par ce carnet)"
            manque = None
        elif dd >= seuil and peak > 0 and px > 0:
            cible = peak * (1 - seuil / 100.0)
            manque = round((cible / px - 1) * 100.0, 1) if cible > px else 0.0
            statut = "BLOQUEE"
        else:
            statut = "ouverte"
            manque = None
        lignes.append({"pair": pair, "prix": px, "dd15": dd if dd_ok else None,
                       "seuil": seuil or None, "statut": statut,
                       "manque_pct_reouvrir": manque,
                       "contexte": ("bear" if bear else "calme") if bear is not None else "thermo HS",
                       "contexte_pourquoi": why})
    bloquees = [l for l in lignes if l["statut"] == "BLOQUEE"]
    bloquees.sort(key=lambda l: (l["manque_pct_reouvrir"] if l["manque_pct_reouvrir"] is not None else 1e9))
    if bloquees:
        top3 = ", ".join("%s +%s%%" % (l["pair"], l["manque_pct_reouvrir"]) for l in bloquees[:3])
    else:
        top3 = "aucune"
    ctx = "bear" if bear else "calme"
    out = {"ts": utc(), "contexte_macro": {"bear": bear, "pourquoi": why},
           "n_bloquees": len(bloquees),
           "file_reouverture": [{"pair": l["pair"], "dd15": l["dd15"], "seuil": l["seuil"],
                                 "manque_pct": l["manque_pct_reouvrir"]} for l in bloquees],
           "toutes": lignes,
           "lecture": ("%d paire(s) en tempête, contexte %s (%s). "
                       "Les plus proches de la réouverture : %s"
                       % (len(bloquees), ctx, why, top3))}
    try:
        json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    except Exception as e:
        print(f"écriture impossible : {e}")
        return 2
    print(out["lecture"])
    print(f"-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
