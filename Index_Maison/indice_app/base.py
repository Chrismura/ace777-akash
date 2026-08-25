#!/usr/bin/env python3
"""
base.py — Classe de base pour les indicateurs non-mainstream
=============================================================

Architecture 4-phase (inspirée de War-Probability-OSINT) :
  Phase 1: Data Acquisition  → collect()
  Phase 2: Feature Engineering → feature()
  Phase 3: Scoring            → score()
  Phase 4: Interpretation     → interpret()

Chaque indicateur est un plugin indépendant.
Si un plante, les autres continuent.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, Optional
import json


class IndicateurBase(ABC):
    """Classe de base pour tous les indicateurs non-mainstream."""

    # Nom de l'indicateur (overridé par chaque module)
    NOM: str = "unknown"
    # Catégorie (geopol, market, onchain, etc.)
    CATEGORIE: str = "general"
    # Source principale
    SOURCE: str = "unknown"
    # Description courte
    DESCRIPTION: str = ""

    def __init__(self):
        self.derniere_collecte: Optional[datetime] = None
        self.dernier_score: Optional[float] = None
        self.derniere_feature: Optional[Dict] = None
        self.erreur: Optional[str] = None
        self.historique: list = []  # Dernières 24 mesures

    # ─── Phase 1: Data Acquisition ──────────────────────────────

    @abstractmethod
    def collect(self) -> Dict[str, Any]:
        """
        Phase 1: Collecte les données brutes depuis la source.
        Retourne un dict avec les données brutes.
        En cas d'erreur, retourne {"_erreur": "..."}.
        """
        pass

    # ─── Phase 2: Feature Engineering ───────────────────────────

    @abstractmethod
    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """
        Phase 2: Transforme les données brutes en features numériques.
        Chaque feature est un float normalisé (0.0 = calme, 1.0 = alerte).
        Retourne un dict {feature_name: value}.
        """
        pass

    # ─── Phase 3: Scoring ──────────────────────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """
        Phase 3: Calcule le score unifié à partir des features.
        Par défaut : moyenne pondérée. Peut être overridé.
        Retourne un float entre 0.0 et 1.0.
        """
        if not features:
            return 0.5
        # Moyenne simple par défaut
        vals = [v for v in features.values() if isinstance(v, (int, float))]
        return sum(vals) / len(vals) if vals else 0.5

    # ─── Phase 4: Interpretation ───────────────────────────────

    @abstractmethod
    def interpret(self, features: Dict[str, float], score_val: float) -> str:
        """
        Phase 4: Retourne l'interprétation en français.
        Claire, concise, actionnable.
        """
        pass

    # ─── Pipeline complet ──────────────────────────────────────

    def run(self) -> Dict[str, Any]:
        """
        Exécute le pipeline complet : collect → feature → score → interpret.
        Retourne un dict structuré pour live.json.
        """
        try:
            # Phase 1: Collect
            raw = self.collect()
            if "_erreur" in raw:
                self.erreur = raw["_erreur"]
                return self._fallback()

            # Phase 2: Feature
            features = self.feature(raw)
            self.derniere_feature = features

            # Phase 3: Score
            score_val = self.score(features)
            self.dernier_score = score_val

            # Phase 4: Interpret
            interp = self.interpret(features, score_val)

            # Métadonnées
            self.derniere_collecte = datetime.now(timezone.utc)
            self.erreur = None

            # Historique (garder 24 mesures)
            self.historique.append({
                "ts": self.derniere_collecte.isoformat(),
                "score": round(score_val, 4),
            })
            if len(self.historique) > 24:
                self.historique = self.historique[-24:]

            return {
                "nom": self.NOM,
                "categorie": self.CATEGORIE,
                "source": self.SOURCE,
                "description": self.DESCRIPTION,
                "score": round(score_val, 4),
                "features": features,
                "interpretation": interp,
                "historique": self.historique,
                "ts": self.derniere_collecte.isoformat(),
                "_erreur": None,
            }

        except Exception as e:
            self.erreur = str(e)
            return self._fallback()

    def _fallback(self) -> Dict[str, Any]:
        """Retourne un score neutre en cas d'erreur."""
        now = datetime.now(timezone.utc)
        return {
            "nom": self.NOM,
            "categorie": self.CATEGORIE,
            "source": self.SOURCE,
            "description": self.DESCRIPTION,
            "score": 0.5,
            "features": {},
            "interpretation": f"Erreur: {self.erreur}",
            "historique": [],
            "ts": now.isoformat(),
            "_erreur": self.erreur,
        }

    def zscore(self, value: float, baseline: float, stddev: float) -> float:
        """
        Utilitaire: calcule le z-score d'une valeur.
        Utilisé par les modules pour normaliser les features.
        """
        if stddev == 0:
            return 0.0
        return (value - baseline) / stddev

    def normalize(self, value: float, min_val: float, max_val: float) -> float:
        """
        Utilitaire: normalise une valeur entre 0.0 et 1.0.
        """
        if max_val == min_val:
            return 0.5
        return max(0.0, min(1.0, (value - min_val) / (max_val - min_val)))
