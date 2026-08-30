#!/usr/bin/env python3
"""
defense_stocks.py — DEFENSE STOCK MOVE (4-phase)
==================================================

Phase 1 (collect)  : API bourse gratuite (Yahoo Finance, etc.)
Phase 2 (feature)  : price_change, volume_surge, sector_correlation
Phase 3 (score)    : z-score combiné
Phase 4 (interpret) : niveau d'alerte + action

Historique :
  - 2022 : Actions défense +20% avant invasion Ukraine
  - 2024 : +15% avant frappes Iran
  - 2025 : +10% avant Mer Rouge

Source : Yahoo Finance API (gratuit)
"""

import json
import urllib.request
from typing import Dict, Any

from indice_app.base import IndicateurBase


# Actions de défense à surveiller
DEFENSE_TICKERS = [
    "LMT",   # Lockheed Martin
    "RTX",   # Raytheon
    "NOC",   # Northrop Grumman
    "BA",    # Boeing
    "GD",    # General Dynamics
    "LHX",   # L3Harris
]

# Baselines
BASELINE_CHANGE_1D = 0.0     # Changement normal en 1j (%)
STDDEV_1D = 3.0              # Écart-type


class DefenseStocks(IndicateurBase):
    NOM = "defense_stocks"
    CATEGORIE = "geopol"
    SOURCE = "Yahoo Finance"
    DESCRIPTION = "Mouvements des actions de défense"

    # ─── Phase 1: Data Acquisition ──────────────────────────────

    def collect(self) -> Dict[str, Any]:
        """Collecte les prix des actions de défense."""
        try:
            stocks = {}
            for ticker in DEFENSE_TICKERS:
                data = self._get_stock(ticker)
                if data:
                    stocks[ticker] = data

            # Calculer la moyenne du secteur
            changes = [s.get("change_pct", 0) for s in stocks.values()]
            avg_change = sum(changes) / len(changes) if changes else 0

            return {
                "stocks": stocks,
                "sector_avg_change": round(avg_change, 2),
                "nb_stocks": len(stocks),
                "source": "yahoo-finance",
            }
        except Exception as e:
            return {"_erreur": str(e)}

    def _get_stock(self, ticker: str) -> Dict[str, Any]:
        """Récupère le prix d'une action via Yahoo Finance."""
        try:
            url = (
                f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
                f"?interval=1d&range=2d"
            )
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ACE777-indice/1.0"},
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())

            result = data.get("chart", {}).get("result", [{}])[0]
            meta = result.get("meta", {})
            price = meta.get("regularMarketPrice", 0)
            prev_close = meta.get("chartPreviousClose", 0)

            if prev_close > 0:
                change_pct = ((price - prev_close) / prev_close) * 100
            else:
                change_pct = 0

            return {
                "ticker": ticker,
                "price": round(price, 2),
                "prev_close": round(prev_close, 2),
                "change_pct": round(change_pct, 2),
            }
        except Exception:
            return {"ticker": ticker, "price": 0, "change_pct": 0}

    # ─── Phase 2: Feature Engineering ───────────────────────────

    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """Transforme les données en features numériques."""
        stocks = raw.get("stocks", {})
        avg_change = raw.get("sector_avg_change", 0)

        # Feature 1: Changement moyen du secteur (z-score)
        f_sector = self.zscore(avg_change, BASELINE_CHANGE_1D, STDDEV_1D)
        f_sector = self.normalize(f_sector, -3, 5)

        # Feature 2: Nombre d'actions en hausse
        nb_up = sum(1 for s in stocks.values() if s.get("change_pct", 0) > 0)
        nb_total = len(stocks) if stocks else 1
        f_breadth = self.normalize(nb_up / nb_total, 0, 1)

        # Feature 3: Plus gros mouvement
        max_change = max(
            [abs(s.get("change_pct", 0)) for s in stocks.values()],
            default=0
        )
        f_max_move = self.normalize(max_change, 0, 10)

        # Feature 4: Corrélation sectorielle (tous bougent ensemble = signal fort)
        if len(stocks) >= 3:
            changes = [s.get("change_pct", 0) for s in stocks.values()]
            all_positive = all(c > 0 for c in changes)
            all_negative = all(c < 0 for c in changes)
            f_correlation = 1.0 if (all_positive or all_negative) else 0.3
        else:
            f_correlation = 0.5

        return {
            "sector_avg_change": round(f_sector, 4),
            "sector_breadth": round(f_breadth, 4),
            "max_stock_move": round(f_max_move, 4),
            "sector_correlation": round(f_correlation, 4),
        }

    # ─── Phase 3: Scoring ──────────────────────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """Score pondéré."""
        poids = {
            "sector_avg_change": 0.40,    # Signal principal
            "sector_breadth": 0.25,        # Toutes les actions bougent
            "max_stock_move": 0.20,        # Plus gros mouvement
            "sector_correlation": 0.15,    # Corrélation = signal fort
        }
        score = sum(features.get(k, 0) * v for k, v in poids.items())
        return max(0.0, min(1.0, score))

    # ─── Phase 4: Interpretation ───────────────────────────────

    def interpret(self, features: Dict[str, float], score_val: float) -> str:
        """Interprétation en français."""
        sector_change = features.get("sector_avg_change", 0)
        breadth = features.get("sector_breadth", 0)

        if score_val >= 0.8:
            return (
                f"🚨 KILL SWITCH — Secteur défense en hausse brutale. "
                f"Préparation militaire détectée. "
                f"Réduire les positions. Ne pas trader."
            )
        elif score_val >= 0.6:
            return (
                f"🔴 ALERTE — Actions défense en hausse significative. "
                f"Stress géopolitique en cours. "
                f"Surveiller de près."
            )
        elif score_val >= 0.3:
            return (
                f"🟡 ATTENTION — Légère hausse du secteur défense. "
                f"À surveiller."
            )
        else:
            return (
                f"🟢 CALME — Secteur défense stable. "
                f"Rien d'inhabituel."
            )
