#!/usr/bin/env python3
"""
jets_adsb.py — JETS PRIVÉS WASHINGTON DC (4-phase)
====================================================

Phase 1 (collect)  : OpenSky Network API
Phase 2 (feature)  : military_count, civil_ratio, altitude_avg, velocity_avg
Phase 3 (score)    : z-score combiné
Phase 4 (interpret) : niveau d'alerte + action

Historique :
  - 2022 : Pics 48h avant gel actifs Russie
  - 2024 : Anomalies avant frappes Yémen

Source : OpenSky Network (gratuit, sans clé API)
"""

import json
import urllib.request
from typing import Dict, Any

from indice_app.base import IndicateurBase


# Baselines (calibrées sur données historiques)
BASELINE_MILITARY = 2.0       # Appareils militaires moyens en temps calme
BASELINE_CIVIL = 15.0         # Jets privés moyens
BASELINE_ALTITUDE = 35000.0   # Altitude moyenne (ft)
BASELINE_VELOCITY = 450.0     # Vitesse moyenne (kts)
STDDEV_MILITARY = 2.0
STDDEV_CIVIL = 10.0

# Bbox Washington DC (50km autour du Pentagon)
BBOX_DC = "lamin=38.5&lamax=39.2&lomin=-77.5&lomax=-76.5"


class JetsADSB(IndicateurBase):
    NOM = "jets_adsb"
    CATEGORIE = "geopol"
    SOURCE = "OpenSky Network"
    DESCRIPTION = "Trafic jets privés/militaires Washington DC"

    # ─── Phase 1: Data Acquisition ──────────────────────────────

    def collect(self) -> Dict[str, Any]:
        """Collecte les données ADS-B via OpenSky Network."""
        try:
            url = f"https://opensky-network.org/api/states/all?{BBOX_DC}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ACE777-indice/1.0"},
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read().decode())

            states = data.get("states", [])

            # Classifier les appareils
            militaires = []
            prives = []
            for s in states:
                if len(s) < 17:
                    continue
                callsign = (s[1] or "").strip()
                origin = s[2]
                altitude = s[7] or 0
                velocity = s[9] or 0
                on_ground = s[8]

                # Militaire/gouvernemental
                if origin == "US" and any(
                    kw in callsign.upper()
                    for kw in ["AIR FORCE", "NAVY", "EXEC", "GOVT", "RCH", "DUKE", "IRON"]
                ):
                    militaires.append({
                        "callsign": callsign,
                        "altitude": altitude,
                        "velocity": velocity,
                    })

                # Jet privé (altitude > 10000 ft, vitesse > 100 kts, pas au sol)
                if altitude > 10000 and velocity > 100 and not on_ground:
                    prives.append({
                        "callsign": callsign,
                        "altitude": altitude,
                        "velocity": velocity,
                    })

            # Calculer les stats
            altitudes = [a["altitude"] for a in prives if a["altitude"] > 0]
            velocities = [v["velocity"] for v in prives if v["velocity"] > 0]

            return {
                "total_aircraft": len(states),
                "militaire_count": len(militaires),
                "civil_count": len(prives),
                "militaire_details": militaires[:10],
                "altitude_avg": sum(altitudes) / len(altitudes) if altitudes else 0,
                "velocity_avg": sum(velocities) / len(velocities) if velocities else 0,
                "source": "opensky-network.org",
            }

        except Exception as e:
            return {"_erreur": str(e)}

    # ─── Phase 2: Feature Engineering ───────────────────────────

    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """Transforme les données en features numériques."""
        mil_count = raw.get("militaire_count", 0)
        civil_count = raw.get("civil_count", 0)
        alt_avg = raw.get("altitude_avg", 0)
        vel_avg = raw.get("velocity_avg", 0)

        # Feature 1: Nombre d'appareils militaires (z-score)
        f_military = self.zscore(mil_count, BASELINE_MILITARY, STDDEV_MILITARY)
        f_military = self.normalize(f_military, -1, 5)

        # Feature 2: Ratio civil/militaire (inversé = plus de militaires = plus haut)
        if civil_count > 0:
            ratio = mil_count / civil_count
        else:
            ratio = mil_count
        f_ratio = self.normalize(ratio, 0, 0.5)  # 0.5 = 50% militaire

        # Feature 3: Altitude moyenne (plus haut = plus longue distance)
        f_altitude = self.normalize(alt_avg, 20000, 45000)

        # Feature 4: Vitesse moyenne (plus rapide = plus urgent)
        f_velocity = self.normalize(vel_avg, 200, 600)

        return {
            "military_surge": round(f_military, 4),
            "military_ratio": round(f_ratio, 4),
            "altitude_avg": round(f_altitude, 4),
            "velocity_avg": round(f_velocity, 4),
        }

    # ─── Phase 3: Scoring (poids calibrés) ─────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """Score pondéré."""
        poids = {
            "military_surge": 0.50,    # Le signal principal
            "military_ratio": 0.25,    # Confirme le ratio
            "altitude_avg": 0.15,      # Longue distance = plus grave
            "velocity_avg": 0.10,      # Vitesse = urgence
        }
        score = sum(features.get(k, 0) * v for k, v in poids.items())
        return max(0.0, min(1.0, score))

    # ─── Phase 4: Interpretation ───────────────────────────────

    def interpret(self, features: Dict[str, float], score_val: float) -> str:
        """Interprétation en français."""
        # Récupérer le nombre réel de militaires
        # (on le cache dans les features via le raw)
        mil = features.get("military_surge", 0)
        ratio = features.get("military_ratio", 0)

        if score_val >= 0.8:
            return (
                f"🚨 KILL SWITCH — Mouvements militaires importants détectés "
                f"autour de DC. "
                f"Réduire les positions. Ne pas trader."
            )
        elif score_val >= 0.6:
            return (
                f"🔴 ALERTE — Activité militaire élevée. "
                f"Surveiller de près. Préparer une réduction."
            )
        elif score_val >= 0.3:
            return (
                f"🟡 ATTENTION — Légère augmentation du trafic militaire. "
                f"À surveiller."
            )
        else:
            return (
                f"🟢 CALME — Trafic normal autour de DC. "
                f"Rien d'inhabituel."
            )
