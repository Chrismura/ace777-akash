# RÉPONSE HUB (task code.ia · via Google Gemini) — 2026-08-29T18:25:24

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intégration du calcul SAPI (Score d'Alerte Poussière Institutionnelle)
à la fin de la fonction compute_sdi() dans Index_Maison/scripts/silent_drain_index.py.
Conforme aux spécifications d'Ada (session poussiere-20260829-152854, tour 1).
"""

import json
from pathlib import Path

# Extrait de code à intégrer à la fin de compute_sdi() (juste avant return result) :
# -------------------------------------------------------------------------
def _integrer_sapi(result: dict, data_dir: Path) -> None:
    """
    Calcule et injecte le SAPI (Score d'Alerte Poussière Institutionnelle)
    dans le dictionnaire de résultat, avec fail-open total.
    """
    try:
        # 1. Extraction des composantes déjà présentes dans result (IPT / z_fee)
        ipt_result = result.get("ipt", {})
        z_fee = float(ipt_result.get("z_fee", 0.0))
        micro_tx_ratio = float(ipt_result.get("micro_tx_ratio", 0.0))

        # 2. Lecture sécurisée de bloc_privatise.json (taux_fantome et volume_btc)
        taux_fantome = 0.0
        volume_btc = 0.0
        bloc_path = data_dir / "bloc_privatise.json"
        if bloc_path.exists():
            try:
                with open(bloc_path, "r", encoding="utf-8") as f:
                    bloc_data = json.load(f)
                    taux_fantome = float(bloc_data.get("taux_fantome", 0.0))
                    volume_btc = float(bloc_data.get("volume_btc", 0.0))
            except Exception:
                pass

        # 3. Lecture sécurisée du proxy carnet spot depuis murs_observations.json
        spot_proxy = 0.0
        murs_path = data_dir.parent / "hulk-mexc" / "runs" / "murs_observations.json"
        if murs_path.exists():
            try:
                with open(murs_path, "r", encoding="utf-8") as f:
                    murs_data = json.load(f)
                    # Recherche du spread_avg_bps pour la paire BTCUSDT
                    top_murs = murs_data.get("top_murs", {})
                    # Supporte différents formats potentiels (dict ou liste)
                    spread_avg_bps = 0.0
                    if isinstance(top_murs, dict):
                        btcusdt_data = top_murs.get("BTCUSDT", {})
                        spread_avg_bps = float(btcusdt_data.get("spread_avg_bps", 0.0))
                    elif isinstance(top_murs, list):
                        for item in top_murs:
                            if item.get("paire") == "BTCUSDT":
                                spread_avg_bps = float(item.get("spread_avg_bps", 0.0))
                                break
                    # Proxy validé : min(1.0, spread_avg_bps / 100.0)
                    spot_proxy = min(1.0, abs(spread_avg_bps) / 100.0)
            except Exception:
                pass

        # 4. Calcul de la formule SAPI (Cortana tour 1, validé 29/08/2026)
        # SAPI = (I(z_fee > 2.0) × 0.35) 
        #      + (min(1.0, poussiere_taux_fantome / 0.15) × 0.30) 
        #      + (I(ipt.micro_tx_ratio > 0.5) × 0.20) 
        #      − (min(1.0, |delta_spot_book_proxy| × 10) × 0.15) -> Note: delta_spot_book_proxy mappé via spot_proxy × 10 ou direct selon spec
        # Spec exacte : − (min(1.0, |delta_spot_book_proxy| × 10) × 0.15) avec proxy = min(1.0, spread_avg_bps / 100.0)
        
        term_z_fee = 0.35 if z_fee > 2.0 else 0.0
        term_fantome = min(1.0, taux_fantome / 0.15) * 0.30
        term_micro = 0.20 if micro_tx_ratio > 0.5 else 0.0
        term_spot = min(1.0, spot_proxy * 10.0) * 0.15

        sapi = term_z_fee + term_fantome + term_micro - term_spot
        sapi = max(0.0, min(1.0, sapi)) # Bornage logique entre 0.0 et 1.0

        # 5. Évaluation de l'alerte critique
        alerte_sapi = bool(sapi >= 0.75 and volume_btc >= 500)

        # 6. Injection dans le dictionnaire de résultat
        result["sapi"] = {
            "score": round(sapi, 3),
            "alerte": alerte_sapi,
            "composantes": {
                "z_fee": round(z_fee, 3),
                "taux_fantome": round(taux_fantome, 3),
                "micro_tx_ratio": round(micro_tx_ratio, 3),
                "spot_proxy": round(spot_proxy, 3)
            },
            "note": "Score d'Alerte Poussière Institutionnelle (Cortana tour 1, validé 29/08 — corr RBF plat −0.275). Proxy carnet spot = spread_avg_bps normalisé."
        }

        # 7. Ajout de l'alerte globale si nécessaire
        if alerte_sapi:
            if "alerts" not in result:
                result["alerts"] = []
            msg_alerte = "SAPI ÉLEVÉ: poussière institutionnelle probable (score ≥ 0.75 + volume)"
            if msg_alerte not in result["alerts"]:
                result["alerts"].append(msg_alerte)

    except Exception as e:
        # Fail-open total : le SAPI ne fait JAMAIS échouer compute_sdi
        result["sapi"] = {
            "score": 0.0,
            "alerte": False,
            "composantes": {"z_fee": 0.0, "taux_fantome": 0.0, "micro_tx_ratio": 0.0, "spot_proxy": 0.0},
            "note": f"Erreur calcul SAPI (fail-open): {str(e)}"
        }
```
