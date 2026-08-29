#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hulk-mexc/scripts/sonde_volume_panier.py
=========================================
SONDE VOLUME PANIER (29/08, GO Christophe — après le débat famille vs Cortana).

POURQUOI cette sonde existe :
Le débat famille vs Cortana (affinage n°4) a fait émerger une proposition
récurrente : remplacer la plage horaire UTC fixe (02-06) par un « volume
glissant » (élargir les seuils si le volume du panier s'effondre de -50/-60 %
vs MM24h). PROBLÈME : personne n'avait vérifié qu'on a les données — on n'a
AUCUN volume de traded dans nos CSV (ts, spread, walls, spoof, price, mais
pas de volume). Toute la discussion était donc théorique.

Cette sonde capture DÈS MAINTENANT le volume traded réel (24h + quoteVolume +
count) pour CHAQUE paire du panier, dans un JSONL d'historique + un état
live. Objectif : dans 48h-72h, on aura la base pour CONSTRUIRE le déclencheur
« volume glissant » avec de vraies données et le comparer honnêtement à la
plage 02-06.

ENTRÉES :
  - hulk-mexc/strategie/paires_croisement.json  (deepdive_validees + observation_setup)
  - API MEXC /api/v3/ticker/24hr (1 appel batch pour TOUTES les paires)

SORTIES :
  - hulk-mexc/runs/volume_panier_hist.jsonl   (une ligne JSON par run, par paire)
  - hulk-mexc/runs/volume_panier_etat.json    (état live : ts, paires, somme panier)
  - Index_Maison/data/alertes/ALERTE_volume_panier.json (si le volume panier
    chute de -50 % vs sa moyenne mobile 24h — WARNING informatif, PAS bloquant,
    tant que la plage 02-06 reste la référence)

CONTRAINTES : Python 3.9 stdlib, fail-open (une paire absente de MEXC = QAIT
est simplement notée absente, jamais un crash), écriture atomique, commentaires
en français. PathRegistry validé au démarrage.

Le fichier d'état expose aussi la METRIQUE « volume glissant 3h » calculée sur
l'historique (si assez de points) — c'est la brique qui permettra de trancher
le débat 02-06 vs volume dans quelques jours.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent          # hulk-mexc
RUNS = ROOT / "runs"
STRATEGIE = ROOT / "strategie" / "paires_croisement.json"
HIST = RUNS / "volume_panier_hist.jsonl"
ETAT = RUNS / "volume_panier_etat.json"
INDEX = ROOT.parent / "Index_Maison"
ALERTE_DIR = INDEX / "data" / "alertes"
ALERTE_PATH = ALERTE_DIR / "ALERTE_volume_panier.json"

# Seuils d'avertissement (informatifs, PAS bloquants — la plage 02-06 reste la
# référence tant que le débat n'est pas tranché avec nos données).
SEUIL_CHUTE_ALERTE = -50.0   # % vs MM24h → warning informatif
FENETRE_MM = 24              # heures pour la moyenne mobile
FENETRE_GLISSANT = 3         # heures du « volume glissant » à exposer
MIN_POINTS_MM = 6            # < 6 points → pas de MM fiable (pas d'alerte)

API_URL = "https://api.mexc.com/api/v3/ticker/24hr"


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


def http_json(url: str, timeout: float = 15.0) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "hulk-sonde-volume/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def charger_paires() -> Dict[str, str]:
    """Paires à sonder = deepdive_validees + observation_setup, avec la note."""
    if not STRATEGIE.exists():
        print(f"[sonde-volume] WARN stratégie absente: {STRATEGIE}", file=sys.stderr)
        return {}
    try:
        data = json.loads(STRATEGIE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[sonde-volume] WARN paires_croisement illisible: {exc}", file=sys.stderr)
        return {}
    paires: Dict[str, str] = {}
    for section in ("deepdive_validees", "observation_setup"):
        bloc = data.get(section) or {}
        if isinstance(bloc, dict):
            for pair, note in bloc.items():
                if isinstance(pair, str) and pair.endswith("USDT"):
                    paires[pair] = str(note)
    return paires


def charger_historique() -> List[Dict[str, Any]]:
    """Lit le JSONL d'historique (fail-open)."""
    if not HIST.exists():
        return []
    lignes: List[Dict[str, Any]] = []
    try:
        with HIST.open("r", encoding="utf-8") as fh:
            for ln in fh:
                ln = ln.strip()
                if not ln:
                    continue
                try:
                    lignes.append(json.loads(ln))
                except json.JSONDecodeError:
                    continue
    except OSError:
        return []
    return lignes


def main() -> int:
    # PathRegistry (barrière erreurs répétées) : valide au démarrage
    try:
        sys.path.insert(0, str(INDEX / "scripts"))
        import path_registry as _pr
        _pr.verifier("signal3")  # même famille de chemins (hulk-mexc/runs)
    except ImportError:
        pass

    now = datetime.now(timezone.utc)
    ts = int(now.timestamp())
    paires = charger_paires()
    if not paires:
        print("[sonde-volume] aucune paire à sonder → sortie propre (exit 0).", file=sys.stderr)
        return 0

    # 1) Un seul appel batch MEXC pour toutes les paires
    try:
        batch = http_json(API_URL)
    except Exception as exc:
        print(f"[sonde-volume] ERR batch MEXC: {exc}", file=sys.stderr)
        # Écrit un état d'échec (fail-open visible, pas silencieux)
        _ecriture_atomique(ETAT, {
            "ts": ts, "utc": now.isoformat(), "ok": False,
            "erreur": f"{type(exc).__name__}: {exc}",
        })
        return 1

    par_symbole = {x.get("symbol"): x for x in batch if isinstance(x, dict) and x.get("symbol")}

    mesures: Dict[str, Dict[str, Any]] = {}
    total_quote = 0.0
    n_presentes = 0
    for pair in sorted(paires):
        raw = par_symbole.get(pair)
        if not raw:
            mesures[pair] = {
                "presente": False, "volume": None, "quoteVolume": None,
                "count": None, "note": "paire absente de MEXC spot (ex: QAIT)",
            }
            continue
        try:
            vol = float(raw.get("volume") or 0.0)
            qv = float(raw.get("quoteVolume") or 0.0)
            cnt = raw.get("count")
            mesures[pair] = {
                "presente": True, "volume": round(vol, 2),
                "quoteVolume": round(qv, 2),
                "count": cnt,
                "priceChangePercent": raw.get("priceChangePercent"),
                "note": paires[pair][:60],
            }
            total_quote += qv
            n_presentes += 1
        except (TypeError, ValueError):
            mesures[pair] = {"presente": False, "volume": None, "quoteVolume": None,
                             "count": None, "note": "parsing échoué"}

    # 2) Journalise l'historique (une ligne par paire, batch horodaté)
    batch_id = now.strftime("%Y%m%dT%H%MZ")
    with HIST.open("a", encoding="utf-8") as fh:
        for pair, m in sorted(mesures.items()):
            fh.write(json.dumps({
                "batch": batch_id, "ts": ts, "utc": now.isoformat(),
                "pair": pair, **m,
            }, ensure_ascii=False) + "\n")

    # 3) Métriques panier : total quote + « volume glissant 3h » vs MM24h
    historique = charger_historique()
    # Série du total panier par batch (pour la MM)
    total_par_batch: Dict[str, float] = {}
    for ligne in historique:
        b = ligne.get("batch")
        if not b:
            continue
        qv = ligne.get("quoteVolume")
        if isinstance(qv, (int, float)) and qv is not None:
            total_par_batch[b] = total_par_batch.get(b, 0.0) + float(qv)

    # Fenêtre 3h du volume glissant : somme des quoteVolume des batchs < 3h
    seuil_3h = now - timedelta(hours=FENETRE_GLISSANT)
    seuil_24h = now - timedelta(hours=FENETRE_MM)
    vol_3h = 0.0
    vol_24h = 0.0
    n_3h = n_24h = 0
    for ligne in historique:
        if not isinstance(ligne.get("quoteVolume"), (int, float)):
            continue
        try:
            t = datetime.fromisoformat(ligne["utc"].replace("Z", "+00:00"))
        except (KeyError, ValueError):
            continue
        if t >= seuil_3h:
            vol_3h += float(ligne["quoteVolume"])
            n_3h += 1
        if t >= seuil_24h:
            vol_24h += float(ligne["quoteVolume"])
            n_24h += 1

    # MM horaire 24h ≈ vol_24h / heures couvertes
    heures_24 = max(1.0, (now - seuil_24h).total_seconds() / 3600.0)
    mm24h_horaire = vol_24h / heures_24
    ratio_glissant = None
    chute_pct = None
    if n_3h >= 1 and mm24h_horaire > 0:
        ratio_glissant = round(vol_3h / (FENETRE_GLISSANT * mm24h_horaire), 3)
        chute_pct = round((ratio_glissant - 1.0) * 100.0, 1)

    # 4) Alerte informative si chute ≥ -50 % (NON bloquante — c'est un warning)
    alerte = None
    if chute_pct is not None and chute_pct <= SEUIL_CHUTE_ALERTE and n_24h >= MIN_POINTS_MM:
        alerte = {
            "ts": ts, "utc": now.isoformat(),
            "chute_pct": chute_pct, "vol_3h": round(vol_3h, 2),
            "mm24h_horaire": round(mm24h_horaire, 2),
            "message": f"Volume panier en chute {chute_pct}% vs MM24h (fenêtre 3h) — "
                       f"info: la plage 02-06 restera la référence tant que le débat n'est pas tranché.",
        }
        _ecriture_atomique(ALERTE_PATH, alerte)

    # 5) État live
    etat = {
        "ts": ts, "utc": now.isoformat(), "ok": True,
        "n_paires": len(paires), "n_presentes_mexc": n_presentes,
        "paires_absentes": [p for p, m in mesures.items() if not m["presente"]],
        "total_quote_24h_usd": round(total_quote, 2),
        "volume_glissant_3h": {
            "ratio_vs_mm24h": ratio_glissant,
            "chute_pct": chute_pct,
            "vol_3h_usd": round(vol_3h, 2),
            "n_batchs_3h": n_3h,
            "n_batchs_24h": n_24h,
            "note": "Métrique EXPÉRIMENTALE — capture en cours pour trancher 02-06 vs volume.",
        },
        "alerte": alerte,
        "paires": mesures,
    }
    _ecriture_atomique(ETAT, etat)

    print(f"[sonde-volume] {now.isoformat()} panier={len(paires)} présentes={n_presentes} "
          f"total_quote_24h={total_quote:.0f}$ vol3h_ratio={ratio_glissant} "
          f"chute={chute_pct}%", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())