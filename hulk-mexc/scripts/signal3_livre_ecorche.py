#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hulk-mexc/scripts/signal3_livre_ecorche.py
==========================================

Signal 3 — Squeeze du livre écorché (order-book void / vacuuming).
SPEC : Index_Maison/SPEC_SIGNAL3_LIVRE_ECORCHE_20260829.md
Code : codeur du hub (minimax-m3), CORRIGÉ par supervision Buffy (29/08) :

  FIX 1 (chemin) : les CSVs bruts sont dans hulk-mexc/runs/ (comme
        observer_murs.py), pas hulk-mexc/data/ → DATA_DIR = ROOT/"runs".
  FIX 2 (logique drop) : drop_n de murs_observations.json est un CUMUL
        (ex. XRP=968 sur 63 611 mesures) — il se compare au seuil 100.
        Le drop_cumul des 3 dernières mesures (max 3) rendait l'alerte
        impossible. On prend donc spoof_pct / drop_n / spread_avg_bps de
        l'agrégat observer_murs, et la persistance (≥ 2 spoof sur les 3
        dernières mesures) depuis les CSVs bruts.

Mécanique détectée : mur iceberg fictif, retrait discret de liquidité,
suppression du mur → trou d'air → décrochage instantané (vacuuming).
Source : arXiv 2504.15908 (31 % des grosses ordres spoofent), session
Cortana manip-3signaux-20260829-152046.

Entrées :
  - hulk-mexc/runs/murs_observations.json  (agrégat observer_murs)
  - hulk-mexc/runs/{ASPIRATION_CALIB,OBSERVATION_MURS}_*.csv (brut, persistance)

Sorties :
  - hulk-mexc/runs/signal3_livre_ecorche.json
  - Index_Maison/data/alertes/ALERTE_signal3_livre_ecorche.json (si ≥ 1 alerte)

Contraintes : Python 3.9 stdlib, fail-open, commentaires en français.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constantes & chemins
# ---------------------------------------------------------------------------

ROOT: Path = Path(__file__).resolve().parent.parent  # hulk-mexc

# Fichier agrégé produit par observer_murs.py
MURS_OBS_PATH: Path = ROOT / "runs" / "murs_observations.json"

# CSVs bruts (mêmes emplacements que observer_murs.py)
DATA_DIR: Path = ROOT / "runs"

OUT_JSON: Path = ROOT / "runs" / "signal3_livre_ecorche.json"

# Alerte (Index_Maison) — écrite seulement si alerte(s)
ALERTE_DIR: Path = ROOT.parent / "Index_Maison" / "data" / "alertes"
ALERTE_PATH: Path = ALERTE_DIR / "ALERTE_signal3_livre_ecorche.json"

# Seuils nominaux (small caps) — calibrés sur nos données + arXiv 2504.15908
SEUIL_SPOOF_PCT: float = 5.0
SEUIL_DROP: float = 100.0
SEUIL_SPREAD_BPS: float = 70.0

# Contagion BTC : seuils abaissés de 20 % si BTC spoof > 5 %
BTC_CONTAGION_SPOOF_PCT: float = 5.0
FACTEUR_CONTAGION: float = 0.80  # 20 % de baisse → multiplicateur 0.80

# Persistance : ≥ 2 spoofs sur les 3 dernières mesures (filtre faux positifs)
PERSISTENCE_MIN: int = 2
FENETRE: int = 3

# Nombre minimal de mesures agrégées par paire pour alerter
N_MESURES_MIN: int = 5

# Seuil de chute par mesure (même valeur que observer_murs SPOOF_DROP_PCT_S)
SPOOF_DROP_PCT_S: float = 15.0

BTC_PAIR: str = "BTCUSDT"

# Seuils "à risque" (proches mais pas en alerte) pour la synthèse
RISQUE_SPOOF_PCT: float = 3.0
RISQUE_DROP: float = 50.0


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def _now_iso_z() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _parse_ts(ts_raw: str) -> Optional[datetime]:
    if not ts_raw:
        return None
    ts_raw = ts_raw.strip()
    for fmt in (
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
    ):
        try:
            return datetime.strptime(ts_raw, fmt)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def _truthy(val: Any) -> bool:
    if val is None:
        return False
    return str(val).strip().lower() in ("true", "1", "oui", "yes", "y")


def _safe_float(val: Any, default: float = 0.0) -> float:
    try:
        if val is None or val == "":
            return default
        return float(val)
    except (TypeError, ValueError):
        return default


def _safe_int(val: Any, default: int = 0) -> int:
    try:
        if val is None or val == "":
            return default
        return int(float(val))
    except (TypeError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Lecture des CSV bruts (mesures horodatées, pour la persistance)
# ---------------------------------------------------------------------------

def charger_mesures_brutes(data_dir: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Charge les CSVs OBSERVATION_MURS_*.csv + ASPIRATION_CALIB_*.csv de
    hulk-mexc/runs/ → {pair: [mesures triées par ts]}.

    Fail-open : un fichier corrompu est ignoré, on continue.
    """
    mesures_par_paire: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    if not data_dir.exists():
        return mesures_par_paire

    patterns = ("OBSERVATION_MURS_*.csv", "ASPIRATION_CALIB_*.csv")
    fichiers: List[Path] = []
    for pattern in patterns:
        try:
            fichiers.extend(sorted(data_dir.glob(pattern)))
        except OSError:
            continue

    for fpath in fichiers:
        try:
            with fpath.open("r", encoding="utf-8", newline="") as fh:
                reader = csv.DictReader(fh)
                for row in reader:
                    if not row:
                        continue
                    pair = (row.get("pair") or "").strip()
                    if not pair:
                        continue
                    ts = _parse_ts(row.get("ts") or "")
                    if ts is None:
                        continue
                    mesures_par_paire[pair].append({
                        "ts": ts,
                        "spoof": _truthy(row.get("spoof")),
                        "drop": _safe_float(row.get("drop_bid_pct_per_s")) >= SPOOF_DROP_PCT_S,
                        "spread_bps": _safe_float(row.get("spread_bps")),
                    })
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            print(f"[signal3] WARN lecture CSV ignoree: {fpath.name} ({exc})", file=sys.stderr)
            continue

    for pair in mesures_par_paire:
        mesures_par_paire[pair].sort(key=lambda m: m["ts"])

    return dict(mesures_par_paire)


def persistance_spoof(mesures: List[Dict[str, Any]]) -> int:
    """Nombre de spoofs sur les 3 dernières mesures (triées par ts)."""
    if not mesures:
        return 0
    fenetre = mesures[-FENETRE:]
    return sum(1 for m in fenetre if m.get("spoof"))


# ---------------------------------------------------------------------------
# Chargement de l'agrégat observer_murs
# ---------------------------------------------------------------------------

def charger_murs_observations(path: Path) -> Dict[str, Any]:
    """Charge runs/murs_observations.json et le normalise : les paires sont
    dans top_murs (liste de dicts {pair, spoof_pct, drop_n, spread_avg_bps,
    n, ...}) → retourne {pair: info}."""
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            return {}
        top = data.get("top_murs")
        if not isinstance(top, list):
            return {}
        par_pair: Dict[str, Any] = {}
        for item in top:
            if isinstance(item, dict) and item.get("pair"):
                par_pair[str(item["pair"]).upper()] = item
        return par_pair
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[signal3] WARN murs_observations illisible: {exc}", file=sys.stderr)
        return {}


# ---------------------------------------------------------------------------
# Fonction principale
# ---------------------------------------------------------------------------

def main() -> int:
    ts_maintenant = _now_iso_z()
    murs_obs = charger_murs_observations(MURS_OBS_PATH)

    # 1) spoof_pct BTCUSDT depuis l'agrégat (fallback 0.0)
    btc_info = murs_obs.get(BTC_PAIR, {}) if isinstance(murs_obs, dict) else {}
    btc_spoof_pct = _safe_float(btc_info.get("spoof_pct"), 0.0)

    # 2) Décision de contagion
    contagion_active = bool(btc_spoof_pct > BTC_CONTAGION_SPOOF_PCT)
    if contagion_active:
        seuils = {
            "spoof_pct": round(SEUIL_SPOOF_PCT * FACTEUR_CONTAGION, 2),  # 4.0
            "drop": round(SEUIL_DROP * FACTEUR_CONTAGION, 1),            # 80.0
            "spread_bps": SEUIL_SPREAD_BPS,
        }
    else:
        seuils = {
            "spoof_pct": SEUIL_SPOOF_PCT,
            "drop": SEUIL_DROP,
            "spread_bps": SEUIL_SPREAD_BPS,
        }

    # 3) Mesures brutes (persistance : ≥ 2 spoofs sur les 3 dernières)
    mesures_brutes = charger_mesures_brutes(DATA_DIR)

    # 4) Paires : union (murs_obs ∪ CSV bruts)
    paires: List[str] = sorted(
        set(murs_obs.keys()) | set(mesures_brutes.keys())
    )

    resultats: List[Dict[str, Any]] = []
    for pair in paires:
        try:
            mi = murs_obs.get(pair) if isinstance(murs_obs, dict) else None
            if not isinstance(mi, dict):
                continue  # pas d'agrégat → rien à évaluer

            n_mesures = _safe_int(mi.get("n"), 0)
            spoof_pct = _safe_float(mi.get("spoof_pct"), 0.0)
            drop = _safe_float(mi.get("drop_n"), 0.0)
            spread = _safe_float(mi.get("spread_avg_bps"), 0.0)

            # Persistance depuis les CSVs bruts (≥ 2 spoofs sur 3 dernières)
            pers = persistance_spoof(mesures_brutes.get(pair, []))

            alerte = bool(
                n_mesures >= N_MESURES_MIN
                and spoof_pct > seuils["spoof_pct"]
                and drop > seuils["drop"]
                and (spread <= seuils["spread_bps"] or spread == 0.0)
                and pers >= PERSISTENCE_MIN
            )

            resultats.append({
                "pair": pair,
                "spoof_pct": round(spoof_pct, 2),
                "drop": int(drop),
                "spread_bps": round(spread, 2),
                "persistance": pers,
                "n_mesures": n_mesures,
                "alerte": alerte,
                "origine": ("contagion_btc" if (alerte and contagion_active)
                            else ("directe" if alerte else None)),
            })
        except Exception as exc:  # noqa: BLE001 — fail-open strict
            print(f"[signal3] WARN evaluation paire {pair} ignoree: {exc}", file=sys.stderr)
            continue

    # 5) Séparation alertes / paires à risque
    alertes = [r for r in resultats if r["alerte"]]
    candidats_risque = [
        r for r in resultats
        if (not r["alerte"])
        and r["n_mesures"] > 0
        and (r["spoof_pct"] > RISQUE_SPOOF_PCT or r["drop"] > RISQUE_DROP)
    ]
    candidats_risque.sort(key=lambda r: (r["spoof_pct"], r["drop"]), reverse=True)
    paires_risque = candidats_risque[:5]

    # 6) Lecture synthèse
    if alertes:
        lecture = (
            f"ALERTE : {len(alertes)} paire(s) en squeeze du livre ecorche "
            f"(btc_spoof_pct={btc_spoof_pct:.2f}%, contagion="
            f"{'active' if contagion_active else 'inactive'})."
        )
    elif paires_risque:
        lecture = (
            f"Marche sous tension : {len(paires_risque)} paire(s) a risque, "
            f"btc_spoof_pct={btc_spoof_pct:.2f}%, "
            f"contagion={'active' if contagion_active else 'inactive'}."
        )
    else:
        lecture = (
            f"Marche calme : aucune paire a risque, "
            f"btc_spoof_pct={btc_spoof_pct:.2f}%, "
            f"contagion={'active' if contagion_active else 'inactive'}."
        )

    # 7) Écriture du JSON principal
    sortie: Dict[str, Any] = {
        "ts": ts_maintenant,
        "btc_spoof_pct": round(btc_spoof_pct, 2),
        "contagion_active": contagion_active,
        "seuils": {k: (int(v) if k == "drop" else round(v, 2))
                   for k, v in seuils.items()},
        "paires_risque": paires_risque,
        "alertes": alertes,
        "lecture": lecture,
    }

    try:
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        with OUT_JSON.open("w", encoding="utf-8") as fh:
            json.dump(sortie, fh, ensure_ascii=False, indent=2)
    except OSError as exc:
        print(f"[signal3] ERREUR ecriture {OUT_JSON}: {exc}", file=sys.stderr)
        return 1

    # 8) Console
    print(f"[signal3] ts={ts_maintenant} btc_spoof_pct={btc_spoof_pct:.2f}% "
          f"contagion={'ON' if contagion_active else 'off'}")
    if alertes:
        print(f"[signal3] ALERTES ({len(alertes)}) :")
        for a in alertes:
            print(f"  - {a['pair']:<12} spoof={a['spoof_pct']:.2f}% "
                  f"drop={a['drop']} spread={a['spread_bps']:.2f}bps "
                  f"persistance={a['persistance']} origine={a['origine']}")
    else:
        print("[signal3] aucune alerte.")
    if paires_risque:
        print(f"[signal3] top {len(paires_risque)} paire(s) a risque :")
        for r in paires_risque:
            print(f"  - {r['pair']:<12} spoof={r['spoof_pct']:.2f}% "
                  f"drop={r['drop']} spread={r['spread_bps']:.2f}bps "
                  f"n={r['n_mesures']}")
    print(f"[signal3] JSON ecrit -> {OUT_JSON}")

    # 9) Alerte Index_Maison — UNIQUEMENT si ≥ 1 alerte
    if alertes:
        try:
            ALERTE_DIR.mkdir(parents=True, exist_ok=True)
            alerte_doc = {
                "id": "signal3_livre_ecorche",
                "message": (
                    f"Squeeze du livre ecorche detecte sur {len(alertes)} paire(s) : "
                    + ", ".join(a["pair"] for a in alertes)
                    + (f" (contagion BTC active, btc_spoof_pct={btc_spoof_pct:.2f}%)"
                       if contagion_active
                       else f" (manipulation directe, btc_spoof_pct={btc_spoof_pct:.2f}%)")
                ),
                "ts": ts_maintenant,
                "status": "actif",
                "paires": [
                    {
                        "pair": a["pair"],
                        "spoof_pct": a["spoof_pct"],
                        "drop": a["drop"],
                        "spread_bps": a["spread_bps"],
                        "persistance": a["persistance"],
                        "origine": a["origine"],
                    }
                    for a in alertes
                ],
                "source": "hulk-mexc/scripts/signal3_livre_ecorche.py",
            }
            with ALERTE_PATH.open("w", encoding="utf-8") as fh:
                json.dump(alerte_doc, fh, ensure_ascii=False, indent=2)
            print(f"[signal3] ALERTE ecrite -> {ALERTE_PATH}")
        except OSError as exc:
            print(f"[signal3] ERREUR ecriture alerte: {exc}", file=sys.stderr)
            return 1
    else:
        # Pas de fausse alerte : on retire un éventuel vieux fichier
        if ALERTE_PATH.exists():
            try:
                ALERTE_PATH.unlink()
            except OSError:
                pass
        print(f"[signal3] aucune alerte, pas de fichier {ALERTE_PATH.name} ecrit.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
