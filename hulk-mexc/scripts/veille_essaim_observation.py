#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hulk-mexc/scripts/veille_essaim_observation.py
===============================================
VEILLE D'ESSAIM — OBSERVATION 48h (29/08, GO Christophe — suite logique du
débat famille vs Cortana).

POURQUOI : la meilleure trouvaille de Cortana (round 1, tour 3) — « le vrai
danger n'est pas qu'UN script soit régulier mais que PLUSIEURS paires
indépendantes subissent EN MÊME TEMPS la même signature rythmique = signature
d'une même ferme de serveurs ou d'un market making coordonné sur tout le
panier small cap » (résonance harmonique inter-actifs).

La famille a REJETÉ la matrice de corrélation croisée lourde (latence,
deadlock, coût CPU) mais a adopté l'idée de fond sous forme d'un COMPTEUR
D'ESSAIM LÉGER : si ≥ N paires affichent un CV ≤ 15 % (rythme quasi-robotique)
dans la même fenêtre, c'est un signal macro-manipulateur.

MODE : OBSERVATION STRICTE (48h). Ce script NE DÉCIDE RIEN, ne modifie AUCUN
seuil, ne déclenche AUCUNE alerte bloquante. Il :
  1. calcule le CV du spread_bps de chaque paire sur une fenêtre glissante
     (régularité du carnet — un script robotique laisse un CV très bas),
  2. compte combien de paires sont « régulières » SIMULTANÉMENT,
  3. journalise tout dans un JSONL + un état live,
  4. affiche le top « essaim » détecté pour qu'on puisse le VALIDER sur les
     données AVANT de le brancher en décision.

Après 48h de capture, on confrontera ces essaims aux vrais mouvements du marché
pour calibrer le seuil N (2 ou 3 paires ?) et le bonus SAPI (+0.20 ?) — puis on
décidera de le passer en prod.

ENTRÉES :
  - hulk-mexc/runs/OBSERVATION_MURS_*.csv + ASPIRATION_CALIB_*.csv (brut, spread_bps)
SORTIES :
  - hulk-mexc/runs/essaim_hist.jsonl        (une ligne par run)
  - hulk-mexc/runs/essaim_etat.json         (état live : paires régulières, essaim)
  - AUCUNE alerte, AUCUNE décision.

CONTRAINTES : Python 3.9 stdlib, fail-open (CSV corrompu ignoré), écriture
atomique, commentaires en français, PathRegistry au démarrage.
"""
from __future__ import annotations

import csv
import json
import os
import statistics
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent          # hulk-mexc
RUNS = ROOT / "runs"
DATA_DIR = RUNS
HIST = RUNS / "essaim_hist.jsonl"
ETAT = RUNS / "essaim_etat.json"
INDEX = ROOT.parent / "Index_Maison"

# Fenêtre de régularité (CV) — le rythme quasi-robotique d'un script
FENETRE_CV: timedelta = timedelta(hours=1)   # 1h de mesures par paire
CV_MIN_ECH: int = 10                         # < 10 mesures 1h → paire non jugée
CV_SEUIL_REGULIER: float = 0.15              # CV ≤ 15 % = quasi-robotique (même
                                             # seuil que le SAPI)

# Compteur d'essaim : combien de paires régulières simultanées = essaim ?
# EN OBSERVATION : on journalise TOUT (de 2 à N paires) pour calibrer le seuil.
MIN_PAIRES_ESSAIM: int = 2                   # à partir de 2 on regarde

# Fenêtre de simultanéité : les paires régulières doivent l'être dans la même
# fenêtre temporelle (leurs dernières mesures alignées sur < 5 min)
SIMULTANEITE_MAX: timedelta = timedelta(minutes=5)


def _ecriture_atomique(path: Path, donnees: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(donnees, fh, ensure_ascii=False, indent=2)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, path)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def _parse_ts(ts_raw: str) -> datetime | None:
    if not ts_raw:
        return None
    ts_raw = ts_raw.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(ts_raw, fmt)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def _safe_float(val: Any, default: float = 0.0) -> float:
    try:
        if val is None or val == "":
            return default
        return float(val)
    except (TypeError, ValueError):
        return default


def charger_mesures() -> Dict[str, List[Dict[str, Any]]]:
    """CSV bruts → {pair: [mesures triées par ts]} (spread_bps + ts)."""
    par_paire: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    if not DATA_DIR.exists():
        return dict(par_paire)
    fichiers: List[Path] = []
    for pattern in ("OBSERVATION_MURS_*.csv", "ASPIRATION_CALIB_*.csv"):
        try:
            fichiers.extend(sorted(DATA_DIR.glob(pattern)))
        except OSError:
            continue
    for fpath in fichiers:
        try:
            with fpath.open("r", encoding="utf-8", newline="") as fh:
                for row in csv.DictReader(fh):
                    pair = (row.get("pair") or "").strip()
                    ts = _parse_ts(row.get("ts") or "")
                    if not pair or ts is None:
                        continue
                    par_paire[pair].append({
                        "ts": ts,
                        "spread_bps": _safe_float(row.get("spread_bps")),
                    })
        except (OSError, UnicodeDecodeError, csv.Error):
            continue
    for pair in par_paire:
        par_paire[pair].sort(key=lambda m: m["ts"])
    return dict(par_paire)


def cv_paire(mesures: List[Dict[str, Any]]) -> Dict[str, Any]:
    """CV du spread_bps sur la fenêtre glissante 1h. Fail-open propre."""
    if len(mesures) < CV_MIN_ECH:
        return {"ok": False, "cv": None, "n": len(mesures), "ts_dernier": None}
    last = mesures[-1]["ts"]
    debut = last - FENETRE_CV
    spreads = [m["spread_bps"] for m in mesures
               if debut <= m["ts"] <= last and m["spread_bps"] > 0.0]
    if len(spreads) < CV_MIN_ECH:
        return {"ok": False, "cv": None, "n": len(spreads), "ts_dernier": last}
    m = sum(spreads) / len(spreads)
    if m <= 0.0:
        return {"ok": False, "cv": None, "n": len(spreads), "ts_dernier": last}
    sigma = statistics.stdev(spreads) if len(spreads) >= 2 else 0.0
    return {"ok": True, "cv": sigma / m, "n": len(spreads), "ts_dernier": last}


def main() -> int:
    try:
        sys.path.insert(0, str(INDEX / "scripts"))
        import path_registry as _pr
        _pr.verifier("signal3")
    except ImportError:
        pass

    now = datetime.now(timezone.utc)
    mesures = charger_mesures()
    if not mesures:
        print("[essaim] aucune mesure CSV → sortie propre.", file=sys.stderr)
        return 0

    # 1) CV par paire
    cv_par_paire: Dict[str, Dict[str, Any]] = {}
    regulieres: List[Dict[str, Any]] = []
    for pair, ms in sorted(mesures.items()):
        r = cv_paire(ms)
        cv_par_paire[pair] = r
        if r["ok"] and r["cv"] is not None and r["cv"] <= CV_SEUIL_REGULIER:
            regulieres.append({
                "pair": pair, "cv": round(r["cv"], 3), "n": r["n"],
                "ts_dernier": r["ts_dernier"].isoformat() if r["ts_dernier"] else None,
            })

    # 2) Détection d'essaim : ≥ MIN_PAIRES_ESSAIM paires régulières avec
    #    dernières mesures alignées dans SIMULTANEITE_MAX
    essaim = []
    if len(regulieres) >= MIN_PAIRES_ESSAIM:
        # alignement : ts_dernier proches les uns des autres
        dates = [datetime.fromisoformat(r["ts_dernier"].replace("Z", "+00:00"))
                 for r in regulieres if r["ts_dernier"]]
        if dates:
            ref = max(dates)
            alignees = [r for r in regulieres
                        if r["ts_dernier"] and
                        (ref - datetime.fromisoformat(r["ts_dernier"].replace("Z", "+00:00")))
                        <= SIMULTANEITE_MAX]
            if len(alignees) >= MIN_PAIRES_ESSAIM:
                essaim = sorted(alignees, key=lambda r: r["cv"])
                # ordre : les plus régulières en premier

    # 3) Journalisation (observation)
    ligne = {
        "ts": int(now.timestamp()), "utc": now.isoformat(),
        "n_paires_jugees": sum(1 for r in cv_par_paire.values() if r["ok"]),
        "n_regulieres": len(regulieres),
        "n_essaim": len(essaim),
        "paires_regulieres": [r["pair"] for r in regulieres],
        "essaim": essaim,
        "note": "OBSERVATION 48h — aucun seuil modifié, aucune décision. Capture pour calibrer le compteur d'essaim (≥2-3 paires CV≤15% simultanées).",
    }
    with HIST.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(ligne, ensure_ascii=False) + "\n")

    _ecriture_atomique(ETAT, {
        "ts": int(now.timestamp()), "utc": now.isoformat(),
        "n_paires_jugees": ligne["n_paires_jugees"],
        "n_regulieres": len(regulieres),
        "n_essaim": len(essaim),
        "essaim": essaim,
        "paires_regulieres": [r["pair"] for r in regulieres],
        "note": ligne["note"],
    })

    print(f"[essaim-obs] {now.isoformat()} jugées={ligne['n_paires_jugees']} "
          f"régulières={len(regulieres)} essaim={len(essaim)} "
          f"{[p['pair'] for p in essaim][:8]}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())