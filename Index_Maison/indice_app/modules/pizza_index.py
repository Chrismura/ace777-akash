#!/usr/bin/env python3
"""
pizza_index.py — PENTAGON PIZZA INDEX (4-phase)
================================================

Phase 1 (collect)  : pizzint.watch + Google Maps
Phase 2 (feature)  : doughcon_level, spike_pct, location_count
Phase 3 (score)    : z-score combiné
Phase 4 (interpret) : niveau DOUGHCON + action recommandée

Historique :
  - 1990 : 21 pizzas CIA → invasion Koweït
  - 2024 : Spike → frappes Iran
  - 2026 : +1250% → capture Maduro

Source : pizzint.watch (OSINT gratuit)
"""

import json
import re
import urllib.request
from typing import Dict, Any

from indice_app.base import IndicateurBase


# Niveaux DOUGHCON
DOUGHCON = {
    1: {"nom": "COBALT", "desc": "Normal", "emoji": "🟢"},
    2: {"nom": "FAST ALERT", "desc": "Légère augmentation", "emoji": "🟢"},
    3: {"nom": "ROUND HOUSE", "desc": "Préparation au combat", "emoji": "🟡"},
    4: {"nom": "COCKED PISTOL", "desc": "Alerte élevée", "emoji": "🔴"},
    5: {"nom": "MAXIMUM FORCE", "desc": "Action imminente", "emoji": "🚨"},
}

# Baselines (calibrées sur les données historiques)
BASELINE_DOUGHCON = 2.0     # Doughcon moyen en temps calme
BASELINE_SPIKE = 50.0       # Spike moyen en % en temps calme
STDDEV_DOUGHCON = 1.0       # Écart-type du doughcon
STDDEV_SPIKE = 200.0        # Écart-type des spikes


class PizzaIndex(IndicateurBase):
    NOM = "pizza_index"
    CATEGORIE = "geopol"
    SOURCE = "pizzint.watch + Google Maps"
    DESCRIPTION = "Activité des pizzerias autour du Pentagon"

    def __init__(self):
        super().__init__()
        self.pizzerias_cache = {}

    # ─── Phase 1: Data Acquisition ──────────────────────────────

    def collect(self) -> Dict[str, Any]:
        """Collecte les données de pizzint.watch."""
        pizzint = self._scrape_pizzint()
        return {
            "pizzint": pizzint,
            "source": "pizzint.watch",
        }

    def _scrape_pizzint(self) -> Dict[str, Any]:
        """Scrape pizzint.watch pour le DOUGHCON actuel."""
        try:
            req = urllib.request.Request(
                "https://pizzint.watch/",
                headers={"User-Agent": "ACE777-indice/1.0"},
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                html = r.read().decode("utf-8", ignore=True)

            # Extraire DOUGHCON
            dc_match = re.search(r"DOUGHCON\s*(\d)", html)
            doughcon = int(dc_match.group(1)) if dc_match else 3

            # Extraire les spikes
            spikes = [int(s) for s in re.findall(r"(\d+)\s*%\s*SPIKE", html)]

            # Extraire le statut
            status_match = re.search(r"STATUS:\s*(\w+)", html)
            status = status_match.group(1) if status_match else "UNKNOWN"

            return {
                "doughcon": doughcon,
                "doughcon_nom": DOUGHCON.get(doughcon, {}).get("nom", "UNKNOWN"),
                "spikes": spikes,
                "max_spike": max(spikes) if spikes else 0,
                "avg_spike": sum(spikes) / len(spikes) if spikes else 0,
                "nb_locations": len(spikes),
                "status": status,
            }
        except Exception as e:
            return {"_erreur": str(e)}

    # ─── Phase 2: Feature Engineering ───────────────────────────

    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """Transforme les données en features numériques."""
        pizzint = raw.get("pizzint", {})

        # Feature 1: DOUGHCON level (z-score)
        dc = pizzint.get("doughcon", 3)
        f_doughcon = self.zscore(dc, BASELINE_DOUGHCON, STDDEV_DOUGHCON)
        f_doughcon = self.normalize(f_doughcon, -2, 4)  # Mapper en 0-1

        # Feature 2: Spike maximum (z-score)
        max_spike = pizzint.get("max_spike", 0)
        f_spike = self.zscore(max_spike, BASELINE_SPIKE, STDDEV_SPIKE)
        f_spike = self.normalize(f_spike, -1, 5)

        # Feature 3: Nombre de locations actives
        nb_loc = pizzint.get("nb_locations", 0)
        f_locations = self.normalize(nb_loc, 0, 8)

        # Feature 4: Spike moyen (consistance)
        avg_spike = pizzint.get("avg_spike", 0)
        f_consistency = self.normalize(avg_spike, 0, 300)

        return {
            "doughcon_level": round(f_doughcon, 4),
            "spike_max": round(f_spike, 4),
            "location_count": round(f_locations, 4),
            "spike_consistency": round(f_consistency, 4),
        }

    # ─── Phase 3: Scoring (poids calibrés) ─────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """Score pondéré : DOUGHCON compte plus que les spikes."""
        poids = {
            "doughcon_level": 0.40,    # Le niveau DOUGHCON est le signal principal
            "spike_max": 0.30,         # Le spike max confirme
            "location_count": 0.15,    # Plus de lieux = plus fiable
            "spike_consistency": 0.15, # Consistance = pas un faux positif
        }
        score = sum(features.get(k, 0) * v for k, v in poids.items())
        return max(0.0, min(1.0, score))

    # ─── Phase 4: Interpretation ───────────────────────────────

    def interpret(self, features: Dict[str, float], score_val: float) -> str:
        """Interprétation en français avec action recommandée."""
        # Récupérer les données originales
        dc = features.get("doughcon_level", 0)
        spike = features.get("spike_max", 0)

        # Mapper le score en niveau DOUGHCON
        if score_val >= 0.8:
            dc_level = 5
        elif score_val >= 0.6:
            dc_level = 4
        elif score_val >= 0.3:
            dc_level = 3
        elif score_val >= 0.1:
            dc_level = 2
        else:
            dc_level = 1

        info = DOUGHCON.get(dc_level, DOUGHCON[3])

        if score_val >= 0.8:
            return (
                f"{info['emoji']} KILL SWITCH — DOUGHCON {dc_level} ({info['nom']}). "
                f"{info['desc']}. "
                f"Réduire les positions de 50%. Ne pas trader."
            )
        elif score_val >= 0.6:
            return (
                f"{info['emoji']} ALERTE — DOUGHCON {dc_level} ({info['nom']}). "
                f"{info['desc']}. "
                f"Préparer une réduction de 25%."
            )
        elif score_val >= 0.3:
            return (
                f"{info['emoji']} ATTENTION — DOUGHCON {dc_level} ({info['nom']}). "
                f"{info['desc']}. "
                f"Surveiller de près."
            )
        else:
            return (
                f"{info['emoji']} CALME — DOUGHCON {dc_level} ({info['nom']}). "
                f"{info['desc']}. "
                f"Rien d'inhabituel."
            )
