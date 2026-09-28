#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""backtest_regime.py — C3 (17/09, verdict JUGE O1, script jetable).

Avant de câbler UN SEUL filtre de régime dans le prompt de l'analyste, on mesure
son effet RÉEL sur l'historique noté. Le JUGE a tranché : la famille proposait
d'interdire LONG en régime baissier, mais l'audit a montré que Cortana est
CONTRARIAN (+19 pts si on avait pris le contre-pied) — le filtre pourrait donc
casser son seul edge. On ne commit un filtre QUE si son solde est > 0.

Méthode :
  * rejoue les analyses notées (statut HIT/MISS/FLAT de la V2, via score_justesse)
  * associe à chacune la couleur régime du jour (regime_couleur.jsonl, ligne la
    plus récente à la date de l'analyse, fallback jour le plus proche)
  * simule 4 variantes : (a) LONG interdit si NOIR, (b) LONG interdit si
    NOIR+ROUGE, (c) LONG et SHORT interdits si NOIR+ROUGE, (d) témoin (aucun filtre)
  * colonne CONTRARIAN : points si on avait systématiquement pris le contre-pied
  * verdict par variante : COMMITTABLE si solde > 0, sinon REJETÉ
  * exit 0 toujours : outil de mesure, pas un gate.

Usage : python3 backtest_regime.py [--json PATH]
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS)
from score_justesse import load_history, load_analyses, juger  # noqa: E402

THERMO = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
REGIME_JOURNAL = os.path.join(THERMO, "regime_couleur.jsonl")


def charger_regimes():
    """[(ts_unix, couleur)] triée par ordre chronologique."""
    out = []
    if not os.path.exists(REGIME_JOURNAL):
        return out
    with open(REGIME_JOURNAL, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
                ts = d.get("ts_unix") or d.get("ts_unix_ms")
                couleur = str(d.get("couleur") or "").strip().upper()
                if ts is None and d.get("ts"):
                    dt = datetime.fromisoformat(str(d["ts"]).replace("Z", "+00:00"))
                    ts = dt.timestamp()
                if ts and couleur:
                    out.append((float(ts), couleur))
            except Exception:
                continue
    out.sort(key=lambda x: x[0])
    return out


def regime_a(ts_unix, regimes):
    """Couleur en vigueur à ts_unix : dernière ligne <= ts (sinon première)."""
    couleur = None
    for ts, c in regimes:
        if ts <= ts_unix:
            couleur = c
        else:
            break
    return couleur or (regimes[0][1] if regimes else None)


def ecart_regime(couleur):
    """Noir/Rouge = baisse lourdement, Vert = hausse lourdement, le reste = neutre."""
    if couleur in ("NOIR", "ROUGE"):
        return -1
    if couleur == "VERT":
        return +1
    return 0


def main():
    ap = argparse.ArgumentParser(description="Backtest filtre régime (C3, jetable)")
    ap.add_argument("--json", metavar="PATH", help="écrire le résultat en JSON")
    a = ap.parse_args()

    history = load_history()
    analyses = load_analyses(None)
    regimes = charger_regimes()
    if not analyses:
        print("Aucune analyse à rejouer (thermo/analyses vide).")
        return 0

    from score_justesse import ts_of
    rejoue = []
    for an in analyses:
        v = juger(an, history)
        if v.get("statut") not in ("HIT ✅", "MISS ❌", "FLAT ➖"):
            continue  # zone morte, sans verdict, etc. : le filtre n'aurait rien changé
        t0 = ts_of(an)
        if t0 is None:
            continue
        couleur = regime_a(t0, regimes)
        rejoue.append({"ts": t0, "indice": an.get("indice", "?"), "avis": v.get("avis"),
                       "statut_v2": v["statut"], "couleur": couleur})

    # CONTRARIAN : +1 si inversion du verdict v2 aurait été mieux (HIT<->MISS)
    def pts_contrarian(r):
        if r["statut_v2"] == "HIT ✅":
            return -1
        if r["statut_v2"] == "MISS ❌":
            return +1
        return 0

    variantes = {
        "a_LONG_interdit_NOIR":  lambda r: r["avis"] == "LONG" and r["couleur"] == "NOIR",
        "b_LONG_interdit_NOIR_ROUGE": lambda r: r["avis"] == "LONG" and r["couleur"] in ("NOIR", "ROUGE"),
        "c_L_S_interdits_NOIR_ROUGE": lambda r: r["avis"] in ("LONG", "SHORT") and r["couleur"] in ("NOIR", "ROUGE"),
        "d_temoin":              lambda r: False,
    }

    print(f"=== BACKTEST FILTRE RÉGIME (C3) — {len(rejoue)} analyses rejouées ===")
    print(f"Période régimes : {len(regimes)} lignes | couleurs: "
          + ", ".join(f"{c}×{sum(1 for _, cc in regimes if cc == c)}" for c in sorted({cc for _, cc in regimes})))
    print()

    rapport = {"n_rejouees": len(rejoue), "variantes": {}}
    lignes_tab = []
    for nom, bloque in variantes.items():
        jouees = [r for r in rejoue if not bloque(r)]
        hit = sum(1 for r in jouees if r["statut_v2"] == "HIT ✅")
        scored = sum(1 for r in jouees if r["statut_v2"] in ("HIT ✅", "MISS ❌"))
        pct = round(hit / scored * 100, 1) if scored else None
        solde = sum(1 for r in rejoue if bloque(r) and r["statut_v2"] == "MISS ❌") \
            - sum(1 for r in rejoue if bloque(r) and r["statut_v2"] == "HIT ✅")
        verdict = "— (témoin)" if nom == "d_temoin" else ("COMMITTABLE si solde > 0" if solde > 0 else "REJETÉ (solde <= 0)")
        lignes_tab.append((nom, len(jouees), hit, scored, pct, solde, verdict))
        rapport["variantes"][nom] = {"jouees": len(jouees), "hit": hit,
                                     "scored": scored, "justesse_pct": pct,
                                     "solde": solde, "verdict": verdict}

    # colonne CONTRARIAN globale
    c_pts = sum(pts_contrarian(r) for r in rejoue)
    c_dir = [r for r in rejoue if r["avis"] in ("LONG", "SHORT")]
    c_dir_pts = sum(pts_contrarian(r) for r in c_dir)
    rapport["contrarian"] = {"pts_tous_avis": c_pts, "pts_directionnels_seuls": c_dir_pts,
                             "n_directionnels": len(c_dir)}

    w = max(len(x[0]) for x in lignes_tab)
    print(f"{'variante'.ljust(w)} | jouées | HIT  | notées | justesse | solde | verdict")
    print("-" * (w + 62))
    for nom, n, h, s, pct, solde, verdict in lignes_tab:
        print(f"{nom.ljust(w)} | {n:6} | {h:4} | {s:6} | "
              f"{('' if pct is None else f'{pct}%').rjust(7)} | {solde:+5} | {verdict}")
    print()
    print(f"CONTRARIAN (contre-pied systématique) : {c_pts:+d} pts sur tous les avis, "
          f"{c_dir_pts:+d} pts sur les {len(c_dir)} avis directionnels")
    print()
    print("Rappel JUGE : un filtre n'est COMMITTABLE que si son solde est strictement positif.")
    print("Solde = (MISS évités par le blocage) - (HIT perdus par le blocage).")

    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(rapport, f, ensure_ascii=False, indent=2)
        print(f"\n[JSON] {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
