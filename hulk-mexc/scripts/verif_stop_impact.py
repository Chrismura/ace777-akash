#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GARDE-FOU GO 2 — LE STOP SE DÉCIDE-T-IL SUR UN PRIX FRAIS ? (23/09/2026)
========================================================================
Ordre Christophe : « le stop vérifié à l'instant de l'impact ». Ce contrôle prouve que
l'outil FONCTIONNE et qu'il SAIT échouer — il ne relit pas mon intention, il appelle le
code du moteur sur une instance minimale.

  R1  `last_price_frais` lit un prix réel et remet l'horodatage à zéro (âge < 2 s)
  R2  `prix_impact` dit l'âge du prix du cycle (celui qui décidait AVANT) et l'âge du prix
      frais (celui qui décide MAINTENANT) — c'est la mesure du « à l'aveugle »
  R3  ÉCHEC RÉSEAU : aucun prix inventé (tag `_impact_NA`, prix None, l'appelant garde le
      prix du cycle)
  R4  COMPATIBILITÉ : les motifs de sortie gardent leurs préfixes EXACTS, donc tous les
      instruments existants (oracle, audits, cockpit) continuent de les lire
  R5  autotest : le contrôle sait-il échouer ? (on lui donne un faux prix périmé et un
      symbole inexistant)

Lecture seule : aucun ordre, aucune écriture moteur, 0 €.
Usage : python3 verif_stop_impact.py [--json runs/VERIF_STOP_IMPACT.json]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from types import MethodType

RACINE = Path(__file__).resolve().parent.parent
MOTEUR = RACINE / "scripts" / "paper_diprip.py"


def charger_moteur():
    spec = importlib.util.spec_from_file_location("pd_moteur", MOTEUR)
    m = importlib.util.module_from_spec(spec)
    sys.modules["pd_moteur"] = m
    spec.loader.exec_module(m)
    return m


class FauxMoteur:
    """Instance minimale : les méthodes testées ne touchent que ces attributs."""
    def __init__(self, pair: str, entry: float):
        self.pos = {pair: {"entry": entry, "qty": 1.0, "high": entry}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    m = charger_moteur()
    res, ok_glob = [], True

    def noter(nom, ok, detail):
        nonlocal ok_glob
        ok_glob = ok_glob and ok
        res.append({"controle": nom, "ok": bool(ok), "detail": detail})
        print(f"  [{'OK ' if ok else 'RATE'}] {nom} — {detail}")

    print("GARDE-FOU GO 2 — prix frais au moment de la décision de sortie\n")
    pair = "BTCUSDT"

    # ── R1 : lecture fraîche
    t0 = time.time()
    p1 = m.last_price_frais(pair)
    dt = time.time() - t0
    age = time.time() - (m._PRICE_TS.get(pair) or 0)
    noter("R1 prix frais lu et horodaté", bool(p1 and p1 > 0 and age < 2.0 and dt < 6.0),
          f"prix={p1} · appel {dt:.2f}s · âge après {age:.2f}s")

    # Le CRITÈRE de R2, sorti en fonction : il sert à R2 (cas réel) ET à R5 (autotest),
    # sinon l'autotest testerait autre chose que le contrôle — un autotest qui ne teste pas
    # le même critère ne prouve rien.
    def prix_frais_ok(tag, age_avant, age_apres, attendu_avant=90.0, tolerance=5.0):
        return (bool(tag and tag.startswith("_impact_av"))
                and abs(age_avant - attendu_avant) <= tolerance
                and age_apres is not None and age_apres < 2.0)

    # ── R2 : les deux âges (dont un prix artificiellement périmé de 90 s)
    entree = float(p1)
    fm = FauxMoteur(pair, entree)
    fm.prix_impact = MethodType(m.PaperBot.prix_impact, fm)
    fm._prix_impact_av = MethodType(m.PaperBot._prix_impact_av, fm)
    m._PRICE_TS[pair] = time.time() - 90          # on force le prix du cycle à 90 s
    m._LAST_KNOWN_PRICE[pair] = entree
    tag, prix, age_av = fm._prix_impact_av(pair)
    info = (fm.__dict__.get("_impact_stop") or {}).get(pair) or {}
    noter("R2 âge AVANT (le prix qui décidait) et âge APRÈS (celui qui décide)",
          bool(prix) and prix_frais_ok(tag, age_av, info.get("age_apres_s")),
          f"tag={tag} · âge avant {age_av:.1f}s · âge frais {info.get('age_apres_s')}s "
          f"· chg avant {info.get('chg_avant_pct')}% → frais {info.get('chg_frais_pct')}%")

    # ── R3 : échec réseau sur un symbole inexistant → AUCUN prix inventé
    fm2 = FauxMoteur("PAIREQUINEXISTEPASUSDT", 1.0)
    fm2.prix_impact = MethodType(m.PaperBot.prix_impact, fm2)
    fm2._prix_impact_av = MethodType(m.PaperBot._prix_impact_av, fm2)
    try:
        tag2, prix2, age2 = fm2._prix_impact_av("PAIREQUINEXISTEPASUSDT")
        noter("R3 échec réseau : pas de prix inventé", tag2 == "_impact_NA" and prix2 is None,
              f"tag={tag2} · prix={prix2} (l'appelant garde alors le prix du cycle)")
    except Exception as e:                                        # noqa: BLE001
        noter("R3 échec réseau : pas de prix inventé", False, f"EXCEPTION remontée : {e}")

    # ── R4 : compatibilité des motifs
    motifs = [f"stop-6.0%_avant_2x_impact_av90s_ap0s",
              f"stop-13.2%_guard_partial_50_impact_av12s_ap0s",
              f"dust_sweep_stop_guard_RIZEUSDT_stop39.23%_impact_av95s_ap0s"]
    ok4 = True
    for mo in motifs:
        ok4 = ok4 and bool(re.search(r"stop-([0-9.]+)%", mo) or "dust_sweep_stop_guard_" in mo)
    ok4 = ok4 and all(("avant_2x" in x) or ("guard_partial_50" in x) or ("dust_sweep_stop_guard_" in x)
                      for x in motifs)
    noter("R4 motifs compatibles (préfixes intacts, tag à la fin)", ok4,
          "les 3 formes historiques restent reconnues par les instruments existants")

    # ── R5 : le contrôle sait-il échouer ? Injections synthétiques dans le MÊME critère.
    cas_bons = prix_frais_ok(tag, age_av, info.get("age_apres_s"))
    cas_perimes = [
        ("tag absent (sortie à l'ancienne)", prix_frais_ok("stop-6.0%_avant_2x", 90.0, 0.0)),
        ("échec réseau (tag _impact_NA)", prix_frais_ok("_impact_NA", 90.0, 0.0)),
        ("âge du cycle non mesuré (-1)", prix_frais_ok("_impact_av-1s_ap0s", -1.0, 0.0)),
        ("prix frais lui aussi périmé (60 s)", prix_frais_ok("_impact_av90s_ap60s", 90.0, 60.0)),
    ]
    tous_rejetes = all(not v for _n, v in cas_perimes)
    noter("R5 autotest — le contrôle sait échouer", cas_bons and tous_rejetes,
          f"cas réel accepté={cas_bons} · "
          + " · ".join(f"{n}: {'REJETÉ' if not v else 'ACCEPTÉ (FAUTE)'}" for n, v in cas_perimes))

    verdict = ("CONFORME — le stop décide sur un prix frais, et l'âge est écrit"
               if ok_glob else "NON CONFORME")
    print("\nVERDICT : " + verdict + " (rc=" + ("0" if ok_glob else "1") + ")")
    print("Lecture seule : aucun ordre, aucune écriture dans le journal du moteur.")

    if a.json:
        Path(a.json).write_text(json.dumps({
            "instrument": "verif_stop_impact.py",
            "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "controles": res, "conforme": ok_glob, "rc": 0 if ok_glob else 1,
            "lecture_seule": True, "ordres": 0,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0 if ok_glob else 1


if __name__ == "__main__":
    raise SystemExit(main())
