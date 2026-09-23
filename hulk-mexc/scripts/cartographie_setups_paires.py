#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CARTOGRAPHIE DES SET-UPS, PAIRE PAR PAIRE (23/09/2026)
=====================================================
Demande Christophe, DEPUIS LE PREMIER JOUR : « FAIRE LE SET-UP SUR CHAQUE PAIRE ».
Jusqu'ici je répondais par des autopsies d'épisode (RIZE, EDEL). Ici je pose les 20 paires
CÔTE À CÔTE, chacune avec SES chiffres, et je nomme pour chacune CE QUI LA BLOQUE.

RÈGLE DE MÉTHODE (payée aujourd'hui) : aucun chiffre n'est recalculé de mémoire. Chaque
grandeur est SOIT lue dans le journal du moteur (il les écrit lui-même), SOIT mesurée
(carnet, série), SOIT lue dans le profil de la paire. La provenance est affichée colonne
par colonne. Aucun seuil n'est inventé : les « conventions de présentation » sont déclarées.

Trois blocs, parce qu'un set-up c'est trois choses :
  A. ENTRÉE  — régime, repli RÉELLEMENT exigé (dip = max(dip_pct ; 0,50 × cadence moteur)),
               jambes ≥ 20 % structurellement inaccessibles, porte qui refuse le plus.
  B. SORTIE  — ce qui se passe vraiment : PnL, motifs, et le STOP RÉALISÉ vs le stop ANNONCÉ.
  C. TAILLE  — le plafond actuel, le spread MESURÉ, et ce que le carnet absorbe vraiment.

LECTURE SEULE · 0 ordre · 0 € · aucune écriture moteur.
Usage : python3 cartographie_setups_paires.py [--json runs/SETUPS_PAIRES.json]
"""
import argparse
import json
import os
import statistics as st
import sys
from collections import defaultdict

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from chiffrage_pump_manque import (  # noqa: E402
    PROFILS, cadences_toutes, cadence_a, charger_tout, charger_tout_m6, csv_actuel,
    detecter_legs, seuil_repli, lire_env, parse)

SERIE = os.path.join(ICI, "..", "runs", "PROFONDEUR_CARNET_SERIE.jsonl")
# CONVENTION DE PRÉSENTATION (déclarée, ce n'est PAS un seuil de moteur) : la mise
# « absorbable » affichée = 10 % de la profondeur mesurée sous −0,5 %. On n'écrit pas de
# règle tant que la série n'est pas longue (R17) : on donne l'ordre de grandeur mesuré.
FRACTION_PRESENTATION = 0.10


def lire_serie():
    """Médianes de la série de profondeur (le seul usage légitime d'un carnet périsable)."""
    par = defaultdict(list)
    if not os.path.exists(SERIE):
        return {}
    for l in open(SERIE, encoding="utf-8", errors="ignore"):
        try:
            d = json.loads(l)
        except Exception:
            continue
        if d.get("erreur"):
            continue
        par[d["paire"]].append(d)
    out = {}
    for p, v in par.items():
        if len(v) < 2:
            continue
        d05 = [x["bid_deep_usd"].get("0.5", x["bid_deep_usd"].get(0.5)) for x in v]
        out[p] = {"n": len(v), "med_05": st.median(d05),
                  "med_2": st.median([x["profondeur_2pct_usd"] for x in v]),
                  "med_spread": st.median([x["spread_bps"] for x in v]),
                  "med_cap": st.median([x["plafond_actuel_2pct_usd"] for x in v]),
                  "ratio": st.median([x["plafond_sur_profondeur_pct"] for x in v
                                      if x.get("plafond_sur_profondeur_pct") is not None])}
    return out


def journal_paire(paire):
    """Tout ce que le JOURNAL du moteur dit de la paire (aucun recalcul)."""
    pnl, motifs, stops, refus, n_sell = 0.0, defaultdict(lambda: [0, 0.0]), [], defaultdict(int), 0
    deja = set()
    for l in open(csv_actuel(), encoding="utf-8", errors="ignore"):
        c = l.rstrip("\n").split(",")
        if len(c) < 11 or c[1] != paire:
            continue
        if c[2] in ("SELL", "SELL_PARTIAL", "BAG_SELL", "DUST_SWEEP"):
            p = float(c[7] or 0)
            pnl += p
            n_sell += 1
            r = c[10]
            cat = ("STOP/GUARD" if r.startswith("stop-") else
                   "DUST_SWEEP" if r.startswith("dust_sweep") else
                   "TRAILING" if r.startswith("trailing") else
                   "RIP/palier" if r.startswith("rip_") else "autre")
            motifs[cat][0] += 1
            motifs[cat][1] += p
            if r.startswith("stop-"):
                try:
                    stops.append(float(r.split("stop-")[1].split("%")[0]))
                except Exception:
                    pass
        elif c[2] == "SKIP":
            # dédup honnête : le journal déduplique déjà les SKIP identiques, on compte les
            # motifs par fenêtre de 1 h (sinon un même refus répété pèse 1000×)
            cle = (c[10].split(" ")[0], c[0][:13])
            if cle in deja:
                continue
            deja.add(cle)
            refus[c[10].split(" ")[0].split(":")[0]] += 1
    return {"pnl": pnl, "n_sell": n_sell, "motifs": dict(motifs),
            "stops_realises": sorted(stops), "refus": dict(refus)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default="")
    a = ap.parse_args()
    cfg = lire_env()
    profs = json.load(open(PROFILS, encoding="utf-8"))
    profs = {k: v for k, v in profs.items() if isinstance(v, dict)}
    cads = cadences_toutes()
    serie = lire_serie()
    par_paire = charger_tout_m6(charger_tout())
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.50") or 0.50)

    lignes = []
    for paire in sorted(profs):
        pr = profs[paire]
        cal = pr.get("calib") or {}
        cs = sorted(c for _, c in cads.get(paire, []))
        cad = cs[len(cs) // 2] if cs else 0.0
        need, dip = seuil_repli(cal, cfg, cad, 0.0)
        j = journal_paire(paire)
        motifs = j["motifs"]
        annee = float(cal.get("stop_pct") or 0.0)
        stops = j["stops_realises"]
        top_refus = sorted(j["refus"].items(), key=lambda kv: -kv[1])[:2]
        ser = serie.get(paire)
        # m6 TYPIQUE de la paire (médiane du m6 que le moteur a écrit) : sans lui, le « seuil »
        # affiché n'est que le PLANCHER (m6=0) et ne dit rien de ce que la paire subit vraiment.
        m6s = sorted(p[3] for p in (par_paire.get(paire) or []))
        m6_med = m6s[len(m6s) // 2] if m6s else 0.0
        need_med, _d = seuil_repli(cal, cfg, cad, m6_med)
        mur = float(pr.get("mur_bid_med") or 0.0)
        cap = mur * float(cal.get("mise_max_pct_mur") or 0.0)
        legs = detecter_legs(par_paire.get(paire) or [])
        inacc = sum(1 for lg in legs
                    if lg["repli_max"] < seuil_repli(cal, cfg,
                                                     cadence_a(cads.get(paire, []), lg["t_lo"], cad),
                                                     lg.get("m6_lo") or 0.0)[0])
        lignes.append({
            "paire": paire, "archetype": pr.get("archetype"), "mode": pr.get("mode_entree") or "—",
            "cadence": cad, "dip_exige": dip, "seuil": need * 0.85, "dip_profil": cal.get("dip_pct"),
            "m6_med": m6_med, "seuil_reel": need_med * 0.85,
            "jambes": len(legs), "inaccessibles": inacc,
            "pnl": j["pnl"], "n_sell": j["n_sell"], "motifs": motifs,
            "stop_annonce": annee, "stops_realises": stops,
            "stop_med": (st.median(stops) if stops else None),
            "stop_max": (max(stops) if stops else None),
            "dust": motifs.get("DUST_SWEEP", [0, 0])[0],
            "top_refus": top_refus,
            "mur": mur, "cap": cap, "spread_profil": pr.get("spread_bps_med"),
            "serie": ser,
            "misable": (FRACTION_PRESENTATION * ser["med_05"]) if ser else None,
        })

    print("SOURCE : journal du run (chiffres écrits par le moteur) · profils de paire · "
          "série de profondeur du carnet")
    print(f"CONVENTION DÉCLARÉE (présentation, pas un seuil de moteur) : « misable » = "
          f"{FRACTION_PRESENTATION:.0%} de la profondeur mesurée sous −0,5 %\n")
    print("== A. ENTRÉE — le repli RÉELLEMENT exigé (cadence ÉCRITE par le moteur) ==")
    print(f"{'paire':10}{'archétype':18}{'cadence':>9}{'dip exigé':>11}{'m6 méd':>8}"
          f"{'seuil réel':>12}{'jambes':>7}{'inacc':>6}  refus dominant")
    print("  (seuil réel = 0,85 × max(dip ; 5 % ; 0,30 × m6 médian ÉCRIT par le moteur))")
    for l in sorted(lignes, key=lambda x: -x["dip_exige"]):
        f = ", ".join("%s=%s" % (k, v) for k, v in l["top_refus"]) or "—"
        print(f"{l['paire'].replace('USDT', ''):10}{str(l['archetype'])[:17]:18}"
              f"{l['cadence']:>8.1f}%{l['dip_exige']:>10.2f}%{l['m6_med']:>7.1f}%"
              f"{l['seuil_reel']:>11.2f}%{l['jambes']:>7}{l['inaccessibles']:>6}  {f[:40]}")

    print("\n== B. SORTIE — ce qui se passe VRAIMENT (stop ANNONCÉ vs stop RÉALISÉ) ==")
    print(f"{'paire':10}{'clôtures':>9}{'PnL $':>9}{'stop ann.':>10}{'stop méd':>9}"
          f"{'stop max':>9}{'dust':>6}  motifs (n, $)")
    for l in sorted(lignes, key=lambda x: x["pnl"]):
        m = " · ".join("%s %d/%+.2f" % (k, v[0], v[1]) for k, v in
                       sorted(l["motifs"].items(), key=lambda kv: -kv[1][0])[:3])
        smed = ("%.2f%%" % l["stop_med"]) if l["stop_med"] else "—"
        smax = ("%.2f%%" % l["stop_max"]) if l["stop_max"] else "—"
        print(f"{l['paire'].replace('USDT', ''):10}{l['n_sell']:>9}{l['pnl']:>+9.2f}"
              f"{l['stop_annonce']:>9.1f}%{smed:>9}{smax:>9}{l['dust']:>6}  {m[:52]}")

    print("\n== C. TAILLE — le plafond actuel face au carnet MESURÉ ==")
    print(f"{'paire':10}{'mur profil':>12}{'cap 2%':>11}{'spread prof':>12}"
          f"{'spread MESURÉ':>14}{'profondeur <−0,5%':>18}{'plafond/prof':>13}{'misable':>10}")
    for l in sorted(lignes, key=lambda x: -(x["serie"]["ratio"] if x["serie"] else -1)):
        s = l["serie"]
        murm = ("%11.0f$" % l["mur"]) if l["mur"] > 0 else "   mur LIVE"
        capm = ("%10.2f$" % l["cap"]) if l["mur"] > 0 else "   (repli)"
        print(f"{l['paire'].replace('USDT', ''):10}{murm}{capm}"
              f"{float(l['spread_profil'] or 0):>10.1f}b"
              f"{(s['med_spread'] if s else float('nan')):>12.1f}b"
              f"{(s['med_05'] if s else float('nan')):>16.0f}$"
              f"{(s['ratio'] if s else float('nan')):>12.1f}%"
              f"{(l['misable'] if l['misable'] else float('nan')):>8.0f}$")
    print("\n  ⚠️ PORTÉE (E8) : « jambes/inacc » vient du chemin dense (log + archives) et d'un")
    print("     seuil d'AFFICHAGE (jambe ≥ 20 %) ; les stops réalisés sont les pertes ÉCRITES par")
    print("     le moteur ; la profondeur n'est mesurée que sur les paires de la série (les autres")
    print("     sont affichées « nan » = NON MESURÉES, jamais estimées). Rien n'est câblé ici.")
    if a.json:
        json.dump({"convention_presentation": FRACTION_PRESENTATION, "paires": lignes},
                  open(a.json, "w"), ensure_ascii=False, indent=2)
        print(f"  (détail écrit : {a.json})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
