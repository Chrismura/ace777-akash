#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GARDIEN DU DÉLAI DE LECTURE DU PRIX (classe E19) — 23/09/2026
==============================================================
POURQUOI IL EXISTE
------------------
La famille (jury permanent, tours 1 et 2, 3 voix) a classé **« la latence de lecture du prix »**
comme le défaut n°1 : barre exigée **< 1 s**, mesure annoncée **1,057 s**.
En produisant la remédiation j'ai trouvé **deux fautes de plus, les miennes** :

  E19a  j'ai publié « 9 328 lectures live, médiane 1,057 s » — or la colonne `delay_s` du corpus
        du satellite n'est écrite QUE pour les lectures en mode COMPLET (2 lectures du carnet).
        Les lectures en mode LÉGER (1 lecture) laissent la colonne VIDE : **le chiffre publié
        portait sur 86 % des lignes et je l'ai présenté comme la médiane de toutes**.
  E19b  la latence du mode LÉGER n'est mesurée NULLE PART → c'est un **angle mort** : impossible
        de prouver la barre < 1 s sur 14 % des lectures, quoi qu'on fasse.

CE QUE CE GARDIEN MESURE (et rend impossible à ignorer)
-------------------------------------------------------
  R1  le délai des lectures COMPLETES : médiane, p90, part < 1 s — la barre de la famille
  R2  la part et le NOMBRE de lectures LÉGERES dont le délai n'est PAS mesuré → ANGLE MORT nommé
  R3  la barre : médiane < 1 s sur les lectures MESURABLES (dit OUI/NON, jamais « conforme »)
  R4  le plancher physique : latence brute d'un appel MEXC (depth + price), échantillon réel
      → si le plancher dépasse la barre, la barre est inatteignable et il faut le DIRE
  R5  autotest : la garde sait échouer (données synthétiques)

Il ne répare rien : il rend la barre MESURABLE, ce qu'elle n'était pas. Lecture seule · 0 ordre · 0 €.
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics as st
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RUNS = Path(__file__).resolve().parent.parent / "runs"
BARRE_S = 1.0


def lire_corpus(fichier: Path | None = None) -> tuple[list[float], int]:
    """(délais MESURÉS, nombre de lignes SANS mesure de délai)."""
    p = fichier or (sorted(RUNS.glob("CORPUS_ASP_*.csv"))[-1] if list(RUNS.glob("CORPUS_ASP_*.csv")) else None)
    if p is None:
        return [], 0
    mes, aveugle = [], 0
    with p.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            v = (r.get("delay_s") or "").strip()
            if not v:
                aveugle += 1
                continue
            try:
                mes.append(float(v))
            except Exception:
                aveugle += 1
    return mes, aveugle


def plancher_physique(n=10) -> dict:
    """Latence brute d'un appel MEXC — le plancher que personne ne peut franchir."""
    out = {}
    for nom, url in (("depth", "https://api.mexc.com/api/v3/depth?symbol=RIZEUSDT&limit=20"),
                     ("price", "https://api.mexc.com/api/v3/ticker/price")):
        v = []
        for _ in range(n):
            t0 = time.time()
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "hulk-garde/1.0"})
                with urllib.request.urlopen(req, timeout=10) as r:
                    r.read()
                v.append((time.time() - t0) * 1000)
            except Exception:
                pass
            time.sleep(0.15)
        if v:
            out[nom] = {"n": len(v), "median_ms": round(st.median(v)), "min_ms": round(min(v))}
    return out


def mesurer(fichier=None, plancher=True) -> dict:
    mes, aveugle = lire_corpus(fichier)
    res: dict = {"ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "barre_s": BARRE_S}
    if not mes:
        res.update({"conforme": False, "verdict": "AUCUNE MESURE — le corpus ne porte aucun délai",
                    "lectures_mesurees": 0, "lectures_sans_mesure": aveugle})
        return res
    tri = sorted(mes)
    res.update({
        "lectures_mesurees": len(mes),
        "lectures_sans_mesure": aveugle,
        "median_s": round(st.median(mes), 3),
        "p90_s": round(tri[int(0.9 * len(tri)) - 1], 3),
        "max_s": round(max(mes), 3),
        "pct_sous_barre": round(100 * sum(1 for x in mes if x < BARRE_S) / len(mes), 1),
        "angle_mort_pct": round(100 * aveugle / max(1, len(mes) + aveugle), 1),
    })
    # R3 — la barre, dite telle qu'elle est
    res["conforme"] = res["median_s"] < BARRE_S
    res["verdict"] = (f"médiane {res['median_s']} s — BARRE {BARRE_S} s "
                      f"{'TENUE' if res['conforme'] else 'NON TENUE'} sur les lectures mesurables ; "
                      f"{res['angle_mort_pct']} % des lectures ({aveugle}) n'ont AUCUN délai mesuré")
    if plancher:
        ph = plancher_physique()
        res["plancher_physique"] = ph
        d = (ph.get("depth") or {}).get("median_ms")
        if d:
            res["plancher_note"] = (f"un seul appel /depth coûte {d} ms : une lecture COMPLÈTE "
                                    f"(2 appels + {0.5} s d'écart voulu pour mesurer la CHUTE) "
                                    f"ne peut pas descendre sous {d + 500} ms par construction")
            if (d + 500) / 1000.0 > BARRE_S:
                res["verdict"] += (" — et la barre < 1 s est INATTEIGNABLE pour une lecture "
                                   "complète à ce plancher réseau : c'est un ARBITRAGE, pas "
                                   "un retard à corriger")
    return res


def autotest() -> int:
    import tempfile
    ok = 0
    total = 3

    def cas(nom, lignes, attendu_sous, attendu_aveugle):
        nonlocal ok
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "CORPUS_ASP_TEST.csv"
            with p.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["ts", "pair", "delay_s"])
                for l in lignes:
                    w.writerow(l)
            mes, aveugle = lire_corpus(p)
            bon = (len(mes) == attendu_sous and aveugle == attendu_aveugle)
            print(f"  [{'OK ' if bon else 'RATÉ'}] {nom} → mesurées={len(mes)} aveugles={aveugle}")
            ok += 1 if bon else 0

    cas("délais présents lus, vides comptés", [["t", "A", "1.0"], ["t", "B", "0.5"],
                                              ["t", "C", ""]], 2, 1)
    cas("tout vide = tout aveugle", [["t", "A", ""], ["t", "B", ""]], 0, 2)
    cas("délai non numérique = aveugle", [["t", "A", "abc"]], 0, 1)
    print(f"  AUTOTEST {ok}/{total}")
    return 0 if ok == total else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--autotest", action="store_true")
    ap.add_argument("--json", metavar="FICHIER")
    ap.add_argument("--sans-plancher", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return autotest()
    r = mesurer(plancher=not a.sans_plancher)
    print(f"Gardien délai de lecture (E19) — {r['verdict']}")
    if r.get("plancher_note"):
        print(f"  plancher : {r['plancher_note']}")
    if a.json:
        Path(a.json).write_text(json.dumps(r, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0 if r.get("conforme") else 1


if __name__ == "__main__":
    sys.exit(main())
