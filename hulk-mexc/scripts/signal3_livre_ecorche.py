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

  FIX 3 (famille, 29/08 soir — GO Christophe) : corrections de l'audit
        famille (6 membres, AVIS_FAMILLE_OEUVRES_20260829) :
    - CONTAGION β_asset DYNAMIQUE : au lieu d'abaisser les seuils de 20 %
      aveuglément, la contagion BTC n'est appliquée à une paire QUE si la
      corrélation glissante 1h (Pearson) entre btc_delta_pct et
      price_delta_pct de la paire ≥ β_MIN (0.3). Paire découplée
      (β < 0.3) → contagion ignorée à 100 % (seuils nominaux).
    - ASYMÉTRIE DIRECTIONNELLE : la contagion ne s'applique qu'en phase
      BAISSIÈRE (delta_btc < 0). Spoof haussier (delta_btc ≥ 0) → pas de
      contagion (la panique de contagion n'opère qu'en cassure baissière,
      cf. arXiv 2504.15908).
    - FILTRE MAD (jitter) : le drop d'une paire n'est retenu que s'il
      dépasse la médiane des 10 dernières mesures + 3 × MAD (median
      absolute deviation) — tue les faux positifs des micro-retraits HFT.
    - ÉCRITURE ATOMIQUE : .tmp + os.replace() pour tous les JSON (fin des
      fichiers tronqués en cas de crash).

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
import math
import os
import statistics
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constantes & chemins
# ---------------------------------------------------------------------------

ROOT: Path = Path(__file__).resolve().parent.parent  # hulk-mexc

# PathRegistry (FIX famille n°4) : valide les chemins au démarrage, avant tout
# calcul — sys.exit(1) si un chemin obligatoire manque (pas de plantage
# silencieux 5 lignes plus loin). Import sûr : module optionnel.
try:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent
                           / "Index_Maison" / "scripts"))
    import path_registry as _pr
    _pr.verifier("signal3")
except ImportError:
    pass  # hors environnement maison (test/CI) → on continue sans validation

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

# β_asset (FIX 3 famille) : seuil de corrélation 1h BTC↔altcoin en dessous
# duquel la contagion BTC est ignorée à 100 % (paire découplée).
BETA_MIN: float = 0.3
BETA_MIN_ECHANTILLONS: int = 5  # fail-open : < 5 échantillons → β = 1.0

# Filtre MAD (FIX 3 famille) : drop retenu seulement si > médiane + 3 × MAD
# sur les 10 dernières mesures brutes de la paire.
MAD_FENETRE: int = 10
MAD_K: float = 3.0

# Dynamic Spread Percentile (FIX famille n°4, 29/08 suite GO) : au lieu du
# seuil fixe SEUIL_SPREAD_BPS (70 bps), le seuil spread de chaque paire est le
# PERCENTILE 30 de sa distribution de spread sur les dernières 24h. Un carnet
# "écorché" = spread dans le décile le plus serré (p30) de SON propre historique,
# pas une valeur absolue (une small cap illiquide vit naturellement à 150+ bps,
# une large cap à 5 bps). P_SPREAD_PERCENTILE = 30 (3e décile).
P_SPREAD_PERCENTILE: float = 30.0
P_SPREAD_FENETRE: timedelta = timedelta(hours=24)
P_SPREAD_MIN_ECH: int = 8   # < 8 mesures → fallback seuil nominal fixe

# HYBRIDE FAMILLE/CORTANA (29/08 litté — consensus tripartite) : le seuil spread
# n'est plus le p30-24h PUR (jugé "miroir rétroviseur" par Cortana, trop lent sur
# les small caps dont la liquidité s'évapore en minutes), mais la combinaison
#   0.7 × p30_24h  +  0.3 × p30_4h
# On garde l'amortisseur anti-bruit 24h ET on gagne la réactivité < 60 min grâce
# au p30-4h. Calibrage DEEPSEEK/JUGE (0.7/0.3), validé par GEMINI (hybride),
# GROK (fenêtre 4h), INFERX (EMA 4h/20h) et Cortana round 2 (EWMA borné).
P_SPREAD_FENETRE_COURTE: timedelta = timedelta(hours=4)
P_SPREAD_POIDS_LONG: float = 0.7   # poids du p30_24h
P_SPREAD_POIDS_COURT: float = 0.3   # poids du p30_4h
P_SPREAD_MIN_ECH_COURT: int = 4    # < 4 mesures 4h → on retombe sur le p30_24h pur

# Heures creuses UTC (02-06) — le spread s'élargit naturellement (peu de MM).
# En heures creuses, le seuil spread est ÉLARGI (× COEFF_HEURE_CREUSE) pour ne
# pas confondre manque de market-maker avec un vrai squeeze du livre.
HEURE_CREUSE_DEBUT: int = 2
HEURE_CREUSE_FIN: int = 5     # inclusif
COEFF_HEURE_CREUSE: float = 1.8

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
                        "drop_val": _safe_float(row.get("drop_bid_pct_per_s")),
                        "spread_bps": _safe_float(row.get("spread_bps")),
                        "btc_delta_pct": _safe_float(row.get("btc_delta_pct")),
                        "price_delta_pct": _safe_float(row.get("price_delta_pct")),
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


def _ecriture_atomique(path: Path, donnees: Any) -> None:
    """Écrit un JSON de façon atomique : fichier temporaire .tmp dans le même
    dossier puis os.replace() (garantie POSIX). FIX 3 famille — fin des
    fichiers tronqués en cas de crash en pleine écriture."""
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


# ---------------------------------------------------------------------------
# β_asset — corrélation glissante 1h BTC ↔ altcoin (FIX 3 famille)
# ---------------------------------------------------------------------------

def _correlation_pearson(xs: List[float], ys: List[float]) -> float:
    """Corrélation de Pearson entre deux séries de même longueur.
    Retourne 0.0 si impossible (division par zéro, trop peu de points)."""
    if len(xs) != len(ys) or len(xs) < 2:
        return 0.0
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs)
    dy = sum((y - my) ** 2 for y in ys)
    if dx <= 0.0 or dy <= 0.0:
        return 0.0
    return num / ((dx * dy) ** 0.5)


def beta_asset(mesures_btc: List[Dict[str, Any]], mesures_pair: List[Dict[str, Any]],
               fenetre: timedelta = timedelta(hours=1)) -> float:
    """β_asset : corrélation de Pearson sur 1h entre btc_delta_pct et
    price_delta_pct de la paire (mesures alignées par horodatage proche).

    Fail-open : moins de BETA_MIN_ECHANTILLONS paires alignées → β = 1.0
    (on conserve le comportement de contagion historique par prudence,
    et on le signale dans le JSON via beta_n).
    """
    if not mesures_btc or not mesures_pair:
        return 1.0, 0
    now = max(m[-1]["ts"] for m in (mesures_btc, mesures_pair) if m)
    debut = now - fenetre

    # Séries (ts, delta) filtrées sur la fenêtre 1h
    btc_series = [(m["ts"], m.get("btc_delta_pct") or 0.0) for m in mesures_btc
                  if debut <= m["ts"] <= now]
    pair_series = [(m["ts"], m.get("price_delta_pct") or 0.0) for m in mesures_pair
                   if debut <= m["ts"] <= now]
    if len(btc_series) < 2 or len(pair_series) < 2:
        return 1.0, 0

    # Alignement : pour chaque mesure paire, on prend le btc_delta le plus
    # proche en temps (≤ 5 s d'écart).
    import bisect
    btc_times = [t for t, _ in btc_series]
    alignes_btc: List[float] = []
    alignes_pair: List[float] = []
    for t, pd in pair_series:
        idx = bisect.bisect_left(btc_times, t)
        candidats = []
        for i in (idx - 1, idx):
            if 0 <= i < len(btc_series):
                candidats.append((abs(btc_times[i] - t), btc_series[i][1]))
        if not candidats:
            continue
        _, bd = min(candidats, key=lambda c: c[0])
        alignes_btc.append(bd)
        alignes_pair.append(pd)

    if len(alignes_btc) < BETA_MIN_ECHANTILLONS:
        return 1.0, len(alignes_btc)
    return _correlation_pearson(alignes_btc, alignes_pair), len(alignes_btc)


def delta_btc_directionnel(mesures_btc: List[Dict[str, Any]],
                           fenetre: timedelta = timedelta(hours=1)) -> float:
    """Delta BTC directionnel cumulé sur la fenêtre 1h (somme des
    btc_delta_pct). Positif = phase haussière, négatif = baissière.
    Retourne 0.0 par défaut (pas de données → pas de contagion baissière)."""
    if not mesures_btc:
        return 0.0
    now = max(m["ts"] for m in mesures_btc)
    debut = now - fenetre
    vals = [m.get("btc_delta_pct") or 0.0 for m in mesures_btc
            if debut <= m["ts"] <= now]
    if not vals:
        return 0.0
    return float(sum(vals))


def drop_filtre_mad(mesures: List[Dict[str, Any]]) -> bool:
    """Filtre MAD (FIX 3 famille) : le drop de la dernière mesure n'est
    retenu QUE s'il dépasse médiane + 3 × MAD sur les MAD_FENETRE dernières
    mesures de la paire. Tue les faux positifs des micro-retraits HFT
    (un bot retire et remet un ordre en 200 ms → la moyenne glisse à tort).
    Fail-open : < 3 mesures → pas de filtre (True)."""
    drops = [m.get("drop_val") or 0.0 for m in mesures]
    if len(drops) < 3:
        return True
    derniers = drops[-MAD_FENETRE:]
    derniere = derniers[-1]
    if len(derniers) < 3:
        return True
    med = statistics.median(derniers)
    deviations = [abs(v - med) for v in derniers]
    mad = statistics.median(deviations) if deviations else 0.0
    seuil = med + MAD_K * mad
    return derniere >= seuil


def _percentile(valeurs: List[float], p: float) -> float:
    """Percentile simple (méthode nearest-rank). Retourne 0.0 si vide."""
    if not valeurs:
        return 0.0
    tri = sorted(valeurs)
    if len(tri) == 1:
        return tri[0]
    idx = max(1, min(len(tri), int(math.ceil(p / 100.0 * len(tri)))))
    return tri[idx - 1]


def _p30_fenetre(mesures: List[Dict[str, Any]], fenetre: timedelta,
                 min_ech: int) -> Dict[str, Any]:
    """p30 des spread_bps d'une paire sur une fenêtre glissante donnée.
    Fail-open : < min_ech mesures → {"ok": False}. Retourne aussi n."""
    if not mesures:
        return {"ok": False, "p": 0.0, "n": 0}
    last = max(m["ts"] for m in mesures)
    debut = last - fenetre
    spreads = [m.get("spread_bps") or 0.0 for m in mesures
               if debut <= m["ts"] <= last and (m.get("spread_bps") or 0.0) > 0.0]
    if len(spreads) < min_ech:
        return {"ok": False, "p": 0.0, "n": len(spreads)}
    return {"ok": True, "p": _percentile(spreads, P_SPREAD_PERCENTILE), "n": len(spreads)}


def spread_seuil_dynamique(mesures: List[Dict[str, Any]],
                           seuil_nominal: float) -> Dict[str, float]:
    """Seuil spread HYBRIDE (FIX famille n°4 + amendement famille/Cortana,
    29/08 litté — consensus tripartite) :
        seuil = 0.7 × p30_24h  +  0.3 × p30_4h
    Le p30-24h est l'amortisseur anti-bruit (une small cap vit à 150+ bps, une
    large cap à 5 bps — un seuil absolu est incomparable). Le p30-4h apporte la
    réactivité < 60 min aux chocs de liquidité (la fenêtre 24h pure était le
    "miroir rétroviseur" dénoncé par Cortana).

    Fail-open hiérarchique :
      - si p30_4h non calculable (< 4 mesures 4h) → seuil = p30_24h pur ;
      - si p30_24h non calculable (< 8 mesures 24h) → seuil nominal fixe.
    Retourne {seuil, p30_24h, p30_4h, n24, n4}."""
    if not mesures:
        return {"seuil": seuil_nominal, "p30_24h": 0.0, "p30_4h": 0.0,
                "n24": 0, "n4": 0, "mode": "nominal"}
    long = _p30_fenetre(mesures, P_SPREAD_FENETRE, P_SPREAD_MIN_ECH)
    if not long["ok"]:
        return {"seuil": seuil_nominal, "p30_24h": 0.0, "p30_4h": 0.0,
                "n24": long["n"], "n4": 0, "mode": "nominal"}
    court = _p30_fenetre(mesures, P_SPREAD_FENETRE_COURTE, P_SPREAD_MIN_ECH_COURT)
    if not court["ok"]:
        # Pas assez de mesures 4h → on reste sur le p30_24h pur (comportement
        # de l'affinage n°4 d'origine, déjà validé).
        seuil = long["p"] if long["p"] > 0.0 else seuil_nominal
        return {"seuil": round(seuil, 2), "p30_24h": round(long["p"], 2),
                "p30_4h": 0.0, "n24": long["n"], "n4": court["n"],
                "mode": "24h_seul"}
    hyb = P_SPREAD_POIDS_LONG * long["p"] + P_SPREAD_POIDS_COURT * court["p"]
    seuil = hyb if hyb > 0.0 else seuil_nominal
    return {"seuil": round(seuil, 2), "p30_24h": round(long["p"], 2),
            "p30_4h": round(court["p"], 2), "n24": long["n"], "n4": court["n"],
            "mode": "hybride"}


def _en_heure_creuse(dt_utc: Optional[datetime] = None) -> bool:
    """Vrai si l'heure UTC est dans la fenêtre creuse [DEBUT, FIN] (02-06)."""
    heure = (dt_utc or datetime.now(timezone.utc)).hour
    if HEURE_CREUSE_DEBUT <= HEURE_CREUSE_FIN:
        return HEURE_CREUSE_DEBUT <= heure <= HEURE_CREUSE_FIN
    return heure >= HEURE_CREUSE_DEBUT or heure <= HEURE_CREUSE_FIN


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

    # 1bis) Mesures brutes (persistance, β_asset, MAD, delta directionnel)
    mesures_brutes = charger_mesures_brutes(DATA_DIR)

    # 2) Décision de contagion (FIX 3 famille — β_asset + asymétrie)
    #    La contagion n'est plus binaire : elle devient un FACTEUR par paire,
    #    calculé dans la boucle (contagion_par_pair[pair] = seuils abaissés ou non).
    mesures_btc = mesures_brutes.get(BTC_PAIR, [])
    delta_btc = delta_btc_directionnel(mesures_btc)
    # Asymétrie directionnelle : la panique de contagion n'opère qu'en phase
    # BAISSIÈRE. Spoof haussier (delta_btc ≥ 0) → pas de contagion du tout.
    direction_baissiere = bool(delta_btc < 0.0)
    contagion_candidate = bool(btc_spoof_pct > BTC_CONTAGION_SPOOF_PCT and direction_baissiere)

    # Seuils nominaux (référence, avant application du β_asset par paire)
    seuils_nominaux = {
        "spoof_pct": SEUIL_SPOOF_PCT,
        "drop": SEUIL_DROP,
        "spread_bps": SEUIL_SPREAD_BPS,
    }
    seuils_contagion = {
        "spoof_pct": round(SEUIL_SPOOF_PCT * FACTEUR_CONTAGION, 2),  # 4.0
        "drop": round(SEUIL_DROP * FACTEUR_CONTAGION, 1),            # 80.0
        "spread_bps": SEUIL_SPREAD_BPS,
    }

    # 3) Paires : union (murs_obs ∪ CSV bruts)
    paires: List[str] = sorted(
        set(murs_obs.keys()) | set(mesures_brutes.keys())
    )

    resultats: List[Dict[str, Any]] = []
    n_contagion_appliquee = 0
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
            mesures_pair = mesures_brutes.get(pair, [])
            pers = persistance_spoof(mesures_pair)

            # FIX 3 famille : β_asset dynamique — calculé TOUJOURS (pour
            # l'audit/analyse), appliqué seulement si contagion candidate ET
            # corrélation 1h avec BTC ≥ BETA_MIN (paire découplée = ignorée).
            beta, beta_n = 1.0, 0
            if pair != BTC_PAIR:
                beta, beta_n = beta_asset(mesures_btc, mesures_pair)
            seuils = seuils_nominaux
            contagion_pair = False
            if contagion_candidate and pair != BTC_PAIR and beta >= BETA_MIN:
                seuils = seuils_contagion
                contagion_pair = True
                n_contagion_appliquee += 1

            # FIX 3 famille : filtre MAD — le drop cumulé doit être significatif
            # vs la distribution des mesures récentes (anti-jitter HFT).
            drop_mad_ok = drop_filtre_mad(mesures_pair)

            # FIX famille n°4 + amendement : Dynamic Spread Percentile HYBRIDE
            # (0.7×p30_24h + 0.3×p30_4h) + heures creuses.
            # 1) Le seuil spread n'est plus fixe (70 bps) : c'est l'hybride des
            #    p30 24h/4h de la paire (amortisseur anti-bruit + réactivité <60
            #    min — le "miroir rétroviseur" de Cortana est corrigé).
            dyn = spread_seuil_dynamique(mesures_pair, seuils["spread_bps"])
            seuil_spread_pair = dyn["seuil"]
            # 2) En heures creuses UTC (02-06), le spread s'élargit
            #    naturellement (peu de MM) : on élargit le seuil pour ne pas
            #    confondre manque de market-maker avec un vrai squeeze.
            heure_creuse = _en_heure_creuse()
            if heure_creuse:
                seuil_spread_pair = round(seuil_spread_pair * COEFF_HEURE_CREUSE, 2)

            alerte = bool(
                n_mesures >= N_MESURES_MIN
                and spoof_pct > seuils["spoof_pct"]
                and drop > seuils["drop"]
                and (spread <= seuil_spread_pair or spread == 0.0)
                and pers >= PERSISTENCE_MIN
                and drop_mad_ok
            )

            resultats.append({
                "pair": pair,
                "spoof_pct": round(spoof_pct, 2),
                "drop": int(drop),
                "spread_bps": round(spread, 2),
                "spread_seuil_dyn": seuil_spread_pair,
                "spread_seuil_mode": dyn["mode"],
                "spread_p30_24h": dyn["p30_24h"],
                "spread_p30_4h": dyn["p30_4h"],
                "spread_p30_n24": dyn["n24"],
                "spread_p30_n4": dyn["n4"],
                "heure_creuse": heure_creuse,
                "persistance": pers,
                "drop_mad_ok": drop_mad_ok,
                "n_mesures": n_mesures,
                "beta_asset": round(beta, 2),
                "beta_n": beta_n,
                "contagion_appliquee": contagion_pair,
                "alerte": alerte,
                "origine": ("contagion_btc" if (alerte and contagion_pair)
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
    contagion_texte = (
        f"{n_contagion_appliquee} paire(s) sous contagion" if contagion_candidate
        else (f"spoof btc {btc_spoof_pct:.2f}% mais phase haussiere (delta_btc={delta_btc:+.2f}) -> pas de contagion"
              if btc_spoof_pct > BTC_CONTAGION_SPOOF_PCT else "contagion inactive")
    )
    if alertes:
        lecture = (
            f"ALERTE : {len(alertes)} paire(s) en squeeze du livre ecorche "
            f"(btc_spoof_pct={btc_spoof_pct:.2f}%, {contagion_texte})."
        )
    elif paires_risque:
        lecture = (
            f"Marche sous tension : {len(paires_risque)} paire(s) a risque, "
            f"btc_spoof_pct={btc_spoof_pct:.2f}%, {contagion_texte}."
        )
    else:
        lecture = (
            f"Marche calme : aucune paire a risque, "
            f"btc_spoof_pct={btc_spoof_pct:.2f}%, {contagion_texte}."
        )

    # 7) Écriture du JSON principal (atomique — FIX 3 famille)
    sortie: Dict[str, Any] = {
        "ts": ts_maintenant,
        "btc_spoof_pct": round(btc_spoof_pct, 2),
        "delta_btc_directionnel": round(delta_btc, 3),
        "contagion_candidate": contagion_candidate,
        "direction_baissiere": direction_baissiere,
        "n_contagion_appliquee": n_contagion_appliquee,
        "seuils_nominaux": {k: (int(v) if k == "drop" else round(v, 2))
                            for k, v in seuils_nominaux.items()},
        "seuils_contagion": {k: (int(v) if k == "drop" else round(v, 2))
                             for k, v in seuils_contagion.items()},
        "beta_min": BETA_MIN,
        "paires_risque": paires_risque,
        "alertes": alertes,
        "lecture": lecture,
    }

    try:
        _ecriture_atomique(OUT_JSON, sortie)
    except OSError as exc:
        print(f"[signal3] ERREUR ecriture {OUT_JSON}: {exc}", file=sys.stderr)
        return 1

    # 8) Console
    print(f"[signal3] ts={ts_maintenant} btc_spoof_pct={btc_spoof_pct:.2f}% "
          f"delta_btc={delta_btc:+.2f} contagion_candidate={contagion_candidate} "
          f"appliquee={n_contagion_appliquee} paire(s)")
    if alertes:
        print(f"[signal3] ALERTES ({len(alertes)}) :")
        for a in alertes:
            print(f"  - {a['pair']:<12} spoof={a['spoof_pct']:.2f}% "
                  f"drop={a['drop']} spread={a['spread_bps']:.2f}bps "
                  f"pers={a['persistance']} mad={a['drop_mad_ok']} "
                  f"beta={a['beta_asset']:.2f} origine={a['origine']}")
    else:
        print("[signal3] aucune alerte.")
    if paires_risque:
        print(f"[signal3] top {len(paires_risque)} paire(s) a risque :")
        for r in paires_risque:
            print(f"  - {r['pair']:<12} spoof={r['spoof_pct']:.2f}% "
                  f"drop={r['drop']} spread={r['spread_bps']:.2f}bps "
                  f"beta={r['beta_asset']:.2f} n={r['n_mesures']}")
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
            _ecriture_atomique(ALERTE_PATH, alerte_doc)
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
