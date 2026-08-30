# RÉPONSE HUB (task code.ia · via minimax/minimax-m3:free) — 2026-08-29T17:34:14

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hulk-mexc/scripts/signal3_livre_ecorche.py
==========================================

Signal 3 — Squeeze du livre écorché (order-book void / vacuuming).

Mission unique : détecter, sur les pières MEXC du projet Hulk, les paires
dont le carnet d'ordres présente les caractéristiques d'un "livre écorché" :

  * forte proportion de murs spoof (spoof_pct cumulé > seuil)
  * effondrements fréquents du carnet (drop > seuil)
  * liquidité de surface conservée (spread_bps <= 70.0 — garde-fou)

Avec règle de contagion BTC : si BTCUSDT dépasse 5 % de spoof, on abaisse
les seuils de 20 % pour toutes les paires (origine="contagion_btc").

Entrées :
  - hulk-mexc/runs/murs_observations.json
        Produit par observer_murs.py : {pair: {spoof_pct, drop_n,
        spread_avg_bps, n, ...}}
  - hulk-mexc/data/OBSERVATION_MURS_*.csv et ASPIRATION_CALIB_*.csv
        Source brute (mêmes colonnes, header OBS_HEADER), utilisée pour
        reconstruire les 3 dernières mesures triées par timestamp.

Sorties :
  - hulk-mexc/runs/signal3_livre_ecorche.json
        Synthèse horodatée : btc_spoof_pct, contagion_active, seuils,
        paires_risque (top 5), alertes, lecture.
  - Index_Maison/data/alertes/ALERTE_signal3_livre_ecorche.json
        Écrit UNIQUEMENT si au moins une paire est en alerte (pas de
        fausse alerte).

Contraintes :
  - Python 3.9 stdlib uniquement (pas de pandas).
  - Fail-open : une paire en erreur n'arrête pas les autres.
  - Commentaires en français.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constantes & chemins
# ---------------------------------------------------------------------------

# Racine du projet Hulk (hulk-mexc/), calculée depuis scripts/signal3_...
ROOT: Path = Path(__file__).resolve().parent.parent

# Fichier agrégé produit par observer_murs.py
MURS_OBS_PATH: Path = ROOT / "runs" / "murs_observations.json"

# Dossier où observer_murs.py range les CSV bruts (par convention projet)
DATA_DIR: Path = ROOT / "data"

# Sortie principale du signal 3
OUT_JSON: Path = ROOT / "runs" / "signal3_livre_ecorche.json"

# Sortie alerte (Index_Maison) — écrite seulement si alerte(s)
ALERTE_DIR: Path = ROOT.parent / "Index_Maison" / "data" / "alertes"
ALERTE_PATH: Path = ALERTE_DIR / "ALERTE_signal3_livre_ecorche.json"

# Seuils nominaux (small caps) — calibrés sur nos données + arXiv 2504.15908
SEUIL_SPOOF_PCT: float = 5.0
SEUIL_DROP: int = 100
SEUIL_SPREAD_BPS: float = 70.0

# Contagion BTC : on abaisse les seuils de 20 % si BTC dépasse 5 %
BTC_CONTAGION_SPOOF_PCT: float = 5.0
FACTEUR_CONTAGION: float = 0.80  # 20 % de baisse → multiplicateur 0.80

# Persistance : la formule Cortana "rolling(3).sum() >= 2" est traduite ici
# par : on prend les 3 dernières mesures triées par timestamp, on calcule le
# cumul (spoof_pct cumulé, drop cumulé, spread moyen), et on retient
# l'alerte si les seuils sont dépassés avec une persistance >= 2 mesures
# (cf. doc en tête de module — SIMPLIFICATION AUTORISÉE par la spec).
PERSISTENCE_MIN: int = 2
FENETRE: int = 3

# Nombre minimal de mesures par paire pour alerter (évite les faux positifs
# sur paires très peu observées)
N_MESURES_MIN: int = 5

# Seuil "drop" par mesure pour considérer une chute (cf. observer_murs.py
# qui utilise SPOOF_DROP_PCT_S ; on garde la même valeur pour rester
# comparable à l'agrégat drop_n de observer_murs).
SPOOF_DROP_PCT_S: float = 15.0

# Paire de référence pour la contagion
BTC_PAIR: str = "BTCUSDT"


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def _now_iso_z() -> str:
    """Horodatage ISO 8601 UTC, suffixé 'Z' comme dans la spec."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _parse_ts(ts_raw: str) -> Optional[datetime]:
    """Tente de parser un timestamp CSV en datetime; None si échec."""
    if not ts_raw:
        return None
    ts_raw = ts_raw.strip()
    # Formats attendus (cf. observer_murs.py) : ISO 8601 avec ou sans Z
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
    # Dernier recours : fromisoformat (Python 3.9 gère peu — on tente)
    try:
        return datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def _truthy(val: str) -> bool:
    """Interprète une valeur textuelle comme booléen (cf. observer_murs)."""
    if val is None:
        return False
    return str(val).strip().lower() in ("true", "1", "oui", "yes", "y")


def _safe_float(val: Any, default: float = 0.0) -> float:
    """Conversion float défensive — jamais fatale."""
    try:
        if val is None or val == "":
            return default
        return float(val)
    except (TypeError, ValueError):
        return default


def _safe_int(val: Any, default: int = 0) -> int:
    """Conversion int défensive — jamais fatale."""
    try:
        if val is None or val == "":
            return default
        return int(float(val))
    except (TypeError, ValueError):
        return default


# ---------------------------------------------------------------------------
# Lecture des CSV bruts (mesures horodatées)
# ---------------------------------------------------------------------------

def charger_mesures_brutes(data_dir: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Charge tous les CSV OBSERVATION_MURS_*.csv et ASPIRATION_CALIB_*.csv,
    retourne {pair: [mesures triées par ts]}.

    Chaque mesure conserve : ts (datetime), spoof (bool), drop (bool),
    spread_bps (float), et le dict brut pour d'éventuels usages futurs.

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
            # Pas fatal : on continue avec ce qu'on a
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
                    ts = _parse_ts(row.get("ts") or row.get("timestamp") or "")
                    if ts is None:
                        # Sans timestamp on ne peut pas calculer la persistance
                        continue
                    mesure = {
                        "ts": ts,
                        "ts_raw": row.get("ts") or row.get("timestamp") or "",
                        "spoof": _truthy(row.get("spoof") or row.get("is_spoof") or ""),
                        "drop": _safe_float(
                            row.get("drop_bid_pct_per_s")
                            or row.get("drop_pct_per_s")
                            or 0.0
                        ) >= SPOOF_DROP_PCT_S,
                        "spread_bps": _safe_float(
                            row.get("spread_bps") or row.get("spread") or 0.0
                        ),
                    }
                    mesures_par_paire[pair].append(mesure)
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            # Fail-open : on loggue sur stderr mais on continue
            print(
                f"[signal3] WARN lecture CSV ignoree: {fpath.name} ({exc})",
                file=sys.stderr,
            )
            continue

    # Tri par timestamp pour chaque paire
    for pair in mesures_par_paire:
        mesures_par_paire[pair].sort(key=lambda m: m["ts"])

    return dict(mesures_par_paire)


# ---------------------------------------------------------------------------
# Calcul du cumul sur les 3 dernières mesures
# ---------------------------------------------------------------------------

def calcul_cumul_3_dernieres(mesures: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Calcule les agrégats sur les 3 dernières mesures triées par ts.

    Retourne un dict :
        {
          "n_mesures": int,        # nb de mesures total dispo pour la paire
          "n_prises": int,         # nb de mesures effectivement prises (≤ 3)
          "spoof_count": int,      # nb de mesures où spoof == True
          "spoof_pct_cumul": float,# 100 * spoof_count / n_prises
          "drop_cumul": int,       # nb de mesures où drop == True
          "spread_moy": float,     # moyenne spread_bps sur la fenêtre
          "persistance": int,      # nb de mesures où spoof == True (=spoof_count)
                                   # sert à vérifier la règle "≥ 2 sur 3"
        }

    Retourne None si moins de 1 mesure dispo (rien à dire).
    """
    if not mesures:
        return None

    n_total = len(mesures)
    fenetre = mesures[-FENETRE:]  # 3 dernières après tri par ts

    spoof_count = sum(1 for m in fenetre if m.get("spoof"))
    drop_cumul = sum(1 for m in fenetre if m.get("drop"))
    n_prises = len(fenetre)
    spoof_pct_cumul = (100.0 * spoof_count / n_prises) if n_prises else 0.0
    spread_moy = (
        sum(_safe_float(m.get("spread_bps")) for m in fenetre) / n_prises
        if n_prises
        else 0.0
    )

    return {
        "n_mesures": n_total,
        "n_prises": n_prises,
        "spoof_count": spoof_count,
        "spoof_pct_cumul": spoof_pct_cumul,
        "drop_cumul": drop_cumul,
        "spread_moy": spread_moy,
        # La persistance est définie comme le nombre de mesures (sur 3) où
        # spoof == True. Avec la simplification autorisée par la spec, on
        # alerte si cumul_spoof et drop_cumul dépassent les seuils ET que
        # cette persistance est ≥ PERSISTENCE_MIN.
        "persistance": spoof_count,
    }


# ---------------------------------------------------------------------------
# Évaluation d'une paire
# ---------------------------------------------------------------------------

def evaluer_paire(
    pair: str,
    cumul: Optional[Dict[str, Any]],
    seuils: Dict[str, float],
) -> Dict[str, Any]:
    """Évalue une paire et retourne un dict prêt pour le JSON de sortie.

    Champs garantis (même si cumul=None) : pair, alerte, origine, spoof_pct,
    drop, spread_bps, persistance, n_mesures.
    """
    if cumul is None:
        return {
            "pair": pair,
            "spoof_pct": 0.0,
            "drop": 0,
            "spread_bps": 0.0,
            "persistance": 0,
            "n_mesures": 0,
            "alerte": False,
            "origine": None,
        }

    alerte = (
        cumul["n_mesures"] >= N_MESURES_MIN
        and cumul["spoof_pct_cumul"] > seuils["spoof_pct"]
        and cumul["drop_cumul"] > seuils["drop"]
        and cumul["spread_moy"] <= seuils["spread_bps"]
        and cumul["persistance"] >= PERSISTENCE_MIN
    )

    return {
        "pair": pair,
        "spoof_pct": round(cumul["spoof_pct_cumul"], 2),
        "drop": int(cumul["drop_cumul"]),
        "spread_bps": round(cumul["spread_moy"], 2),
        "persistance": int(cumul["persistance"]),
        "n_mesures": int(cumul["n_mesures"]),
        "alerte": bool(alerte),
        "origine": "contagion_btc" if (alerte and seuils.get("contagion")) else ("directe" if alerte else None),
    }


# ---------------------------------------------------------------------------
# Chargement de l'agrégat observer_murs (pour récupérer btc_spoof_pct et
# la liste de référence des paires)
# ---------------------------------------------------------------------------

def charger_murs_observations(path: Path) -> Dict[str, Any]:
    """Charge runs/murs_observations.json. Retourne {} si absent ou corrompu."""
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            return {}
        return data
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[signal3] WARN murs_observations illisible: {exc}", file=sys.stderr)
        return {}


# ---------------------------------------------------------------------------
# Fonction principale
# ---------------------------------------------------------------------------

def main() -> int:
    """Orchestre la détection du signal 3 et écrit les sorties.

    Étapes :
      1. Charger murs_observations.json (référence : btc_spoof_pct + paires).
      2. Charger les CSV bruts pour reconstruire les 3 dernières mesures
         par paire (persistance).
      3. Décider du mode contagion selon BTC.
      4. Évaluer chaque paire (fail-open par paire).
      5. Écrire signal3_livre_ecorche.json.
      6. Écrire l'alerte Index_Maison si ≥ 1 alerte, sinon ne rien écrire.
    """
    ts_maintenant = _now_iso_z()
    murs_obs = charger_murs_observations(MURS_OBS_PATH)

    # 1) spoof_pct BTCUSDT depuis l'agrégat observer_murs (fallback 0.0)
    btc_info = murs_obs.get(BTC_PAIR, {}) if isinstance(murs_obs, dict) else {}
    btc_spoof_pct = _safe_float(btc_info.get("spoof_pct"), 0.0)

    # 2) Décision de contagion
    contagion_active = bool(btc_spoof_pct > BTC_CONTAGION_SPOOF_PCT)
    if contagion_active:
        seuils = {
            "spoof_pct": SEUIL_SPOOF_PCT * FACTEUR_CONTAGION,   # 4.0
            "drop": SEUIL_DROP * FACTEUR_CONTAGION,            # 80.0 → 80
            "spread_bps": SEUIL_SPREAD_BPS,
            "contagion": True,
        }
    else:
        seuils = {
            "spoof_pct": SEUIL_SPOOF_PCT,
            "drop": SEUIL_DROP,
            "spread_bps": SEUIL_SPREAD_BPS,
            "contagion": False,
        }

    # 3) Mesures brutes (pour la persistance sur 3 dernières)
    mesures_brutes = charger_mesures_brutes(DATA_DIR)

    # 4) Liste de paires : union (murs_obs ∪ CSV bruts)
    paires: List[str] = sorted(
        set(list(murs_obs.keys()) if isinstance(murs_obs, dict) else [])
        | set(mesures_brutes.keys())
    )

    resultats: List[Dict[str, Any]] = []
    for pair in paires:
        try:
            mesures = mesures_brutes.get(pair, [])
            cumul = calcul_cumul_3_dernieres(mesures)
            # Si pas de CSV bruts mais murs_obs dispo, on construit un
            # pseudo-cumul à partir de l'agrégat (sans persistance fine)
            if cumul is None and isinstance(murs_obs.get(pair), dict):
                mi = murs_obs[pair]
                cumul = {
                    "n_mesures": _safe_int(mi.get("n"), 0),
                    "n_prises": 0,  # pas de fenêtre triée
                    "spoof_count": 0,
                    "spoof_pct_cumul": _safe_float(mi.get("spoof_pct"), 0.0),
                    "drop_cumul": _safe_int(mi.get("drop_n"), 0),
                    "spread_moy": _safe_float(mi.get("spread_avg_bps"), 0.0),
                    "persistance": 0,
                }
            res = evaluer_paire(pair, cumul, seuils)
            # Si l'agrégat observer_murs est plus riche que les CSV bruts,
            # on l'utilise en complément (sans écraser la persistance).
            if isinstance(murs_obs.get(pair), dict) and cumul is not None:
                mi = murs_obs[pair]
                if cumul.get("n_prises", 0) == 0:
                    res["spoof_pct"] = round(_safe_float(mi.get("spoof_pct"), res["spoof_pct"]), 2)
                    res["drop"] = int(_safe_int(mi.get("drop_n"), res["drop"]))
                    res["spread_bps"] = round(
                        _safe_float(mi.get("spread_avg_bps"), res["spread_bps"]), 2
                    )
                    res["n_mesures"] = max(res["n_mesures"], _safe_int(mi.get("n"), 0))
            resultats.append(res)
        except Exception as exc:  # noqa: BLE001 — fail-open strict
            print(
                f"[signal3] WARN evaluation paire {pair} ignoree: {exc}",
                file=sys.stderr,
            )
            continue

    # 5) Séparation alertes / paires à risque
    alertes = [r for r in resultats if r["alerte"]]
    # "paires à risque" = proches mais pas en alerte : spoof_pct > 3.0
    # OU drop > 50, triées par spoof_pct desc puis drop desc (top 5)
    candidats_risque = [
        r for r in resultats
        if (not r["alerte"])
        and r["n_mesures"] > 0
        and (r["spoof_pct"] > 3.0 or r["drop"] > 50)
    ]
    candidats_risque.sort(key=lambda r: (r["spoof_pct"], r["drop"]), reverse=True)
    paires_risque = candidats_risque[:5]

    # 6) Lecture synthèse
    if alertes:
        if contagion_active:
            lecture = (
                f"ALERTE : {len(alertes)} paire(s) en squeeze du livre ecorche "
                f"(contagion BTC active, btc_spoof_pct={btc_spoof_pct:.2f}%)."
            )
        else:
            lecture = (
                f"ALERTE : {len(alertes)} paire(s) en squeeze du livre ecorche "
                f"(manipulation directe, btc_spoof_pct={btc_spoof_pct:.2f}%)."
            )
    elif paires_risque:
        lecture = (
            f"Marche sous tension : {len(paires_risque)} paire(s) a risque "
            f"detectee(s), btc_spoof_pct={btc_spoof_pct:.2f}%, "
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
        "seuils": {
            "spoof_pct": round(seuils["spoof_pct"], 2),
            "drop": int(seuils["drop"]),
            "spread_bps": round(seuils["spread_bps"], 2),
        },
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

    # 8) Console : alertes + top 5 paires à risque (style observer_murs)
    print(f"[signal3] ts={ts_maintenant} btc_spoof_pct={btc_spoof_pct:.2f}% "
          f"contagion={'ON' if contagion_active else 'off'}")
    if alertes:
        print(f"[signal3] ALERTES ({len(alertes)}) :")
        for a in alertes:
            print(
                f"  - {a['pair']:<12} spoof={a['spoof_pct']:.2f}% "
                f"drop={a['drop']} spread={a['spread_bps']:.2f}bps "
                f"persistance={a['persistance']} origine={a['origine']}"
            )
    else:
        print("[signal3] aucune alerte.")
    if paires_risque:
        print(f"[signal3] top {len(paires_risque)} paire(s) a risque :")
        for r in paires_risque:
            print(
                f"  - {r['pair']:<12} spoof={r['spoof_pct']:.2f}% "
                f"drop={r['drop']} spread={r['spread_bps']:.2f}bps "
                f"n={r['n_mesures']}"
            )
    print(f"[signal3] JSON ecrit -> {OUT_JSON}")

    # 9) Alerte Index_Maison — UNIQUEMENT si ≥ 1 alerte
    if alertes:
        try:
            ALERTE_DIR.mkdir(parents=True, exist_ok=True)
            alerte_doc = {
                "id": "signal3_livre_ecorche",
                "message": (
                    f"Squeeze du livre ecorche detecte sur "
                    f"{len(alertes)} paire(s) : "
                    + ", ".join(a["pair"] for a in alertes)
                    + (
                        f" (contagion BTC active, btc_spoof_pct={btc_spoof_pct:.2f}%)"
                        if contagion_active
                        else f" (manipulation directe, btc_spoof_pct={btc_spoof_pct:.2f}%)"
                    )
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
        # Pas de fausse alerte : ne pas écrire le fichier d'alerte.
        # Si un vieux fichier existe, on le supprime pour éviter le bruit.
        if ALERTE_PATH.exists():
            try:
                ALERTE_PATH.unlink()
            except OSError:
                pass
        print(f"[signal3] aucune alerte, pas de fichier {ALERTE_PATH.name} ecrit.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
```
