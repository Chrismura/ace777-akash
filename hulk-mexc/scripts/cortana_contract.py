#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrat JSON Cortana ↔ moteur Hulk (v1, ADVISORY).

Famille 15/08 (gemini 85%, nvidia 72%) : GO-AVEC-RÉSERVE.
  - ADVISORY : propositions validées + LOGGÉES, JAMAIS appliquées si justesse < 60%.
  - AUTO (futur, justesse ≥ 60% durable) : appliquées CLAMPÉES dans les bornes dures.
  - Fail-safe : fichier absent/corrompu → paramètres actuels GELÉS (aucun défaut silencieux).
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MIN_SCORE_AUTO = 0.60
BOUNDS = {
    "DIP_FLOOR_MULT": (0.85, 1.15),
    "RIP_FLOOR_MULT": (0.85, 1.15),
    "STOP_FLOOR_MULT": (0.90, 1.10),
    "NOTIONAL_MULT": (0.90, 1.10),
}
CONFIDENCES = ("faible", "moyenne", "haute")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_load(path: Path) -> dict[str, Any]:
    try:
        if not path.exists():
            return {}
        d = json.loads(path.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def load_proposals(path: Path) -> tuple[dict[str, Any], list[str]]:
    """Fail-safe : absent/corrompu → ({}, [warn])."""
    data = _safe_load(path)
    warns: list[str] = []
    if not data:
        warns.append("cortana_pilot absent/vide → paramètres actuels GELÉS (fail-safe)")
    elif not isinstance(data.get("proposals"), list):
        warns.append("cortana_pilot sans 'proposals'[] → rien à traiter")
        data = {}
    return data, warns


def validate_proposals(
    data: dict[str, Any], *, score: float = 0.0, mode: str = "ADVISORY"
) -> tuple[list[dict[str, Any]], list[str]]:
    """Valide chaque proposition (whitelist, bornes, expiry, confiance). Retourne (valides, rejets)."""
    valid: list[dict[str, Any]] = []
    rejects: list[str] = []
    for p in data.get("proposals") or []:
        param = str(p.get("param") or "")
        if param not in BOUNDS:
            rejects.append(f"{param}: hors liste blanche")
            continue
        if str(p.get("param_class") or "") != "threshold_multiplier":
            rejects.append(f"{param}: param_class != threshold_multiplier")
            continue
        try:
            value = float(p.get("value"))
        except Exception:
            rejects.append(f"{param}: valeur non numérique")
            continue
        lo, hi = BOUNDS[param]
        if not (lo <= value <= hi):
            rejects.append(f"{param}: {value} hors bornes [{lo},{hi}]")
            continue
        expiry = str(p.get("expiry") or "")
        if not expiry:
            rejects.append(f"{param}: expiry manquante")
            continue
        try:
            exp_ts = datetime.fromisoformat(expiry.replace("Z", "+00:00")).timestamp()
        except Exception:
            rejects.append(f"{param}: expiry invalide")
            continue
        if exp_ts <= time.time():
            rejects.append(f"{param}: expiry dépassée")
            continue
        conf = str(p.get("confidence") or "moyenne").lower()
        if conf not in CONFIDENCES:
            rejects.append(f"{param}: confiance '{conf}' invalide")
            continue
        if conf == "haute" and score < MIN_SCORE_AUTO:
            rejects.append(f"{param}: confiance 'haute' ignorée (score {score:.0%} < 60%)")
            continue
        valid.append(p)
    return valid, rejects


def apply_overrides(data: dict[str, Any], *, score: float = 0.0) -> dict[str, float]:
    """Mode AUTO uniquement : valeurs CLAMPÉES. Appelé SEULEMENT si mode=AUTO et score≥0.60."""
    if score < MIN_SCORE_AUTO:
        return {}
    overrides: dict[str, float] = {}
    for p in data.get("proposals") or []:
        param = str(p.get("param") or "")
        if param not in BOUNDS:
            continue
        try:
            value = float(p.get("value"))
        except Exception:
            continue
        lo, hi = BOUNDS[param]
        overrides[param] = round(max(lo, min(hi, value)), 4)
    return overrides


def process_pilot(
    path: Path, *, default_mode: str = "ADVISORY"
) -> tuple[list[dict[str, Any]], dict[str, float], list[str]]:
    """Point d'entrée du moteur : (pending, applied_overrides, warns).
    pending = propositions valides (ADVISORY : loggées, pas appliquées)."""
    data, warns = load_proposals(path)
    if not data:
        return [], {}, warns
    score = float(data.get("cortana_accuracy_score") or 0)
    mode = str(data.get("enforced_mode") or default_mode).strip().upper()
    pending, rejects = validate_proposals(data, score=score, mode=mode)
    applied: dict[str, float] = {}
    if mode == "AUTO" and score >= MIN_SCORE_AUTO:
        applied = apply_overrides(data, score=score)
    return pending, applied, warns + rejects
