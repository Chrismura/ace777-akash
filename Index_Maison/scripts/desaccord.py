#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desaccord.py — le DÉSACCORD comme mesure et comme signal (30/10, GO Christophe).

Idée maison : le rapide (Cortana/sirène/corr) voit l'instant, le lent
(saison/zone/plancher) voit le régime. Quand ils divergent, le marché HÉSITE —
et l'hésitation elle-même est un signal mesurable, jugé après-coup comme tout
le reste (même doctrine que le scorer).

3 axes (tous lus, aucun calculé sur le moteur) :
  D1 Cortana vs saison : verdicts bullish/bearish (5 min) contre direction
     de saison (long/short/neutre). Accord si même sens, désaccord sinon.
  D2 Sirène vs zone : sirène ON pendant zone VERT (le rapide crie, le lent
     lisse) — le R19 écrit en continu.
  D3 Short vs plancher : corr d'entrée (≤ −0,50) pendant plancher ACHETÉ
     (fond confirmé) — entrer short sur un fond qui se forme.

Sorties (lecture seule, jamais une décision) :
  Index_Maison/data/desaccord_live.json  (état courant + les 3 axes)
  Index_Maison/data/desaccord_hist.jsonl (1 ligne/scan pour le jugement +24h)

Usage : python3 desaccord.py [--once]  (boucle sans --once, 300 s)
"""
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
DATA = os.path.join(BASE, "Index_Maison", "data")
STRAT = os.path.join(BASE, "Index_Maison", "strategie")
RUNS = os.path.join(BASE, "hulk-mexc", "runs")
LIVE_OUT = os.path.join(DATA, "desaccord_live.json")
HIST = os.path.join(DATA, "desaccord_hist.jsonl")
LOOP_SEC = 300


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
            return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def _verdict(txt):
    m = re.search(r'"signal"\s*:\s*"(\w+)"', txt or "")
    return m.group(1).lower() if m else "?"


def scan() -> dict:
    """Lit les états, calcule les 3 axes. Ne lève jamais."""
    try:
        cort = _load(os.path.join(DATA, "cortana_analysis.json"))
        anals = cort.get("analyses") or []
        bull = sum(1 for a in anals if _verdict(str((a.get("signal") or {}).get("analysis", ""))) == "bullish")
        bear = sum(1 for a in anals if _verdict(str((a.get("signal") or {}).get("analysis", ""))) == "bearish")
        cort_dir = "bullish" if bull > bear else ("bearish" if bear > bull else "neutre")

        saison = _load(os.path.join(STRAT, "ada_saison_live.json"))
        saison_dir = str(saison.get("direction") or "neutre").lower()
        saison_nom = str(saison.get("saison") or "?")

        gard = _load(os.path.join(STRAT, "ada_gardienne_live.json")).get("gardienne", {}) or {}
        zone = str(gard.get("zone") or "?")
        sirene = bool(gard.get("sirene", False))

        shorts = {}
        for tag, sym in (("btc", "BTCUSDT"), ("eth", "ETHUSDT"), ("xrp", "XRPUSDT")):
            lv = _load(os.path.join(RUNS, f"short_{tag}_live.json"))
            sig = lv.get("signal") or {}
            try:
                c = sig.get("corr_dir_btc")
                c = float(c) if c is not None else None
            except Exception:
                c = None
            murs = lv.get("plancher") or {}
            shorts[tag] = {"corr": c, "phase": murs.get("phase"),
                           "arme": bool(c is not None and c <= -0.50)}

        planch = _load(os.path.join(DATA, "plancher_confirme_etat.json")).get("paires") or {}
        achete = [k for k, v in planch.items() if (v or {}).get("phase") == "ACHETE"]

        # --- les 3 axes ---
        # D1 : Cortana (rapide) vs saison (lent)
        sens_cort = {"bullish": "long", "bearish": "short"}.get(cort_dir, "neutre")
        d1 = {"cortana": cort_dir, "saison": f"{saison_nom}/{saison_dir}",
              "accord": sens_cort == saison_dir or "neutre" in (sens_cort, saison_dir),
              "bull": bull, "bear": bear}
        # D2 : sirène (rapide) vs zone (lent)
        d2 = {"sirene": sirene, "zone": zone,
              "desaccord": bool(sirene and zone == "VERT")}
        # D3 : short armé (rapide) vs fond plancher (lent), par paire
        d3 = {}
        for tag, sym in (("btc", "BTCUSDT"), ("eth", "ETHUSDT"), ("xrp", "XRPUSDT")):
            ph = (planch.get(sym) or {}).get("phase")
            arme = shorts[tag]["arme"]
            d3[tag] = {"arme": arme, "fond": ph,
                       "desaccord": bool(arme and ph == "ACHETE")}
        n_des = (0 if d1["accord"] else 1) + (1 if d2["desaccord"] else 0) \
            + sum(1 for v in d3.values() if v["desaccord"])
        phrases = []
        phrases.append(f"D1 Cortana {cort_dir} ({bull}B/{bear}b) vs saison {saison_nom}/{saison_dir} → "
                       + ("accord" if d1["accord"] else "DÉSACCORD"))
        phrases.append(f"D2 sirène {'ON' if sirene else 'off'} + zone {zone} → "
                       + ("DÉSACCORD (R19)" if d2["desaccord"] else "accord"))
        for tag, v in d3.items():
            phrases.append(f"D3 short {tag.upper()} {'armé' if v['arme'] else 'éteint'} vs fond {v['fond']} → "
                           + ("DÉSACCORD" if v["desaccord"] else "accord"))
        out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "d1_cortana_vs_saison": d1, "d2_sirene_vs_zone": d2,
               "d3_short_vs_plancher": d3, "fonds_achetes": achete,
               "n_desaccords": n_des, "phrases": phrases}
        return out
    except Exception as e:
        return {"ts": "", "erreur": str(e)[:120], "n_desaccords": 0, "phrases": []}


def ecrire(out: dict) -> None:
    try:
        tmp = LIVE_OUT + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        os.replace(tmp, LIVE_OUT)
    except Exception:
        pass
    try:
        with open(HIST, "a", encoding="utf-8") as f:
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main() -> int:
    if "--once" in sys.argv:
        ecrire(scan())
        return 0
    while True:
        try:
            ecrire(scan())
        except Exception:
            pass
        time.sleep(LOOP_SEC)
    return 0


if __name__ == "__main__":
    sys.exit(main())
