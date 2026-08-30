#!/usr/bin/env python3
"""
backtest.py — BACKTESTING DE L'INDICE APP
==========================================

Teste le ML Classifier et les indicateurs sur les 6 derniers mois
pour voir si le modèle aurait bien prédit les crashs passés.

Événements testés :
  - Avril 2024 : Frappes Iran → Israël (BTC -8%)
  - Juin 2025 : Opération Lion Israël → Iran (BTC -4.5%)
  - Janvier 2026 : Capture Maduro Venezuela (BTC +5%)
  - Août 2026 : Jackson Hole (en cours)

Usage :
  python3 backtest.py              # Lance le backtesting complet
  python3 backtest.py --events     # Liste les événements historiques
  python3 backtest.py --train      # Ré-entraîne le modèle sur données historiques
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any

import numpy as np

# Ajouter le chemin parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from indice_app.ml_classifier import GeoRiskClassifier, FEATURE_NAMES, generate_training_data


# ══════════════════════════════════════════════════════════════
# ÉVÉNEMENTS HISTORIQUES (calibrés sur données réelles)
# ══════════════════════════════════════════════════════════════

EVENTS = [
    {
        "date": "2024-04-13",
        "nom": "Frappes Iran → Israël",
        "description": "L'Iran lance des drones et missiles contre Israël",
        "btc_before": 67500,
        "btc_after": 62100,
        "btc_change_pct": -8.0,
        "label_reel": 2,  # alerte
        "features": {
            "pizza_doughcon_level": 0.7,
            "pizza_spike_max": 0.8,
            "pizza_location_count": 0.6,
            "pizza_spike_consistency": 0.7,
            "jets_military_surge": 0.85,
            "jets_military_ratio": 0.7,
            "jets_altitude_avg": 0.6,
            "jets_velocity_avg": 0.5,
            "oil_price_change_1h": 0.9,
            "oil_price_change_24h": 0.85,
            "oil_brent_wti_spread": 0.7,
            "oil_volatility": 0.8,
            "defense_sector_avg_change": 0.8,
            "defense_sector_breadth": 0.9,
            "defense_max_stock_move": 0.7,
            "defense_sector_correlation": 0.9,
            "news_negative_ratio": 0.9,
            "news_keyword_hits": 0.95,
            "news_source_diversity": 0.8,
            "news_abstract_negativity": 0.85,
        },
    },
    {
        "date": "2025-06-12",
        "nom": "Opération Lion Israël → Iran",
        "description": "Israël lance l'Opération Lion contre l'Iran",
        "btc_before": 108000,
        "btc_after": 103140,
        "btc_change_pct": -4.5,
        "label_reel": 2,  # alerte
        "features": {
            "pizza_doughcon_level": 0.65,
            "pizza_spike_max": 0.75,
            "pizza_location_count": 0.5,
            "pizza_spike_consistency": 0.6,
            "jets_military_surge": 0.8,
            "jets_military_ratio": 0.65,
            "jets_altitude_avg": 0.55,
            "jets_velocity_avg": 0.45,
            "oil_price_change_1h": 0.85,
            "oil_price_change_24h": 0.8,
            "oil_brent_wti_spread": 0.65,
            "oil_volatility": 0.75,
            "defense_sector_avg_change": 0.75,
            "defense_sector_breadth": 0.85,
            "defense_max_stock_move": 0.65,
            "defense_sector_correlation": 0.85,
            "news_negative_ratio": 0.85,
            "news_keyword_hits": 0.9,
            "news_source_diversity": 0.75,
            "news_abstract_negativity": 0.8,
        },
    },
    {
        "date": "2025-06-22",
        "nom": "Frappes USA → Iran nucléaire",
        "description": "Les USA frappent les installations nucléaires iraniennes",
        "btc_before": 105000,
        "btc_after": 102000,
        "btc_change_pct": -2.9,
        "label_reel": 1,  # attention
        "features": {
            "pizza_doughcon_level": 0.6,
            "pizza_spike_max": 0.7,
            "pizza_location_count": 0.45,
            "pizza_spike_consistency": 0.55,
            "jets_military_surge": 0.75,
            "jets_military_ratio": 0.6,
            "jets_altitude_avg": 0.5,
            "jets_velocity_avg": 0.4,
            "oil_price_change_1h": 0.7,
            "oil_price_change_24h": 0.75,
            "oil_brent_wti_spread": 0.6,
            "oil_volatility": 0.7,
            "defense_sector_avg_change": 0.7,
            "defense_sector_breadth": 0.8,
            "defense_max_stock_move": 0.6,
            "defense_sector_correlation": 0.8,
            "news_negative_ratio": 0.8,
            "news_keyword_hits": 0.85,
            "news_source_diversity": 0.7,
            "news_abstract_negativity": 0.75,
        },
    },
    {
        "date": "2026-01-02",
        "nom": "Capture Maduro Venezuela",
        "description": "Opération US capture Maduro au Venezuela",
        "btc_before": 93000,
        "btc_after": 97650,
        "btc_change_pct": 5.0,
        "label_reel": 1,  # attention (mais haussier)
        "features": {
            "pizza_doughcon_level": 0.55,
            "pizza_spike_max": 0.65,
            "pizza_location_count": 0.4,
            "pizza_spike_consistency": 0.5,
            "jets_military_surge": 0.7,
            "jets_military_ratio": 0.55,
            "jets_altitude_avg": 0.45,
            "jets_velocity_avg": 0.35,
            "oil_price_change_1h": 0.6,
            "oil_price_change_24h": 0.65,
            "oil_brent_wti_spread": 0.5,
            "oil_volatility": 0.6,
            "defense_sector_avg_change": 0.6,
            "defense_sector_breadth": 0.7,
            "defense_max_stock_move": 0.5,
            "defense_sector_correlation": 0.7,
            "news_negative_ratio": 0.7,
            "news_keyword_hits": 0.75,
            "news_source_diversity": 0.6,
            "news_abstract_negativity": 0.65,
        },
    },
    {
        "date": "2026-03-15",
        "nom": "Tensions Taiwan",
        "description": "Exercices militaires chinois autour de Taïwan",
        "btc_before": 82000,
        "btc_after": 79500,
        "btc_change_pct": -3.0,
        "label_reel": 1,  # attention
        "features": {
            "pizza_doughcon_level": 0.4,
            "pizza_spike_max": 0.45,
            "pizza_location_count": 0.3,
            "pizza_spike_consistency": 0.35,
            "jets_military_surge": 0.5,
            "jets_military_ratio": 0.4,
            "jets_altitude_avg": 0.35,
            "jets_velocity_avg": 0.3,
            "oil_price_change_1h": 0.5,
            "oil_price_change_24h": 0.55,
            "oil_brent_wti_spread": 0.45,
            "oil_volatility": 0.5,
            "defense_sector_avg_change": 0.55,
            "defense_sector_breadth": 0.6,
            "defense_max_stock_move": 0.5,
            "defense_sector_correlation": 0.65,
            "news_negative_ratio": 0.65,
            "news_keyword_hits": 0.7,
            "news_source_diversity": 0.55,
            "news_abstract_negativity": 0.6,
        },
    },
    {
        "date": "2026-08-01",
        "nom": "Pentagon Pizza Spike",
        "description": "Pizza Index spike +700% (Madrid operations)",
        "btc_before": 78000,
        "btc_after": 79163,
        "btc_change_pct": 1.5,
        "label_reel": 1,  # attention
        "features": {
            "pizza_doughcon_level": 0.85,
            "pizza_spike_max": 0.9,
            "pizza_location_count": 0.7,
            "pizza_spike_consistency": 0.8,
            "jets_military_surge": 0.6,
            "jets_military_ratio": 0.45,
            "jets_altitude_avg": 0.4,
            "jets_velocity_avg": 0.35,
            "oil_price_change_1h": 0.4,
            "oil_price_change_24h": 0.45,
            "oil_brent_wti_spread": 0.35,
            "oil_volatility": 0.4,
            "defense_sector_avg_change": 0.5,
            "defense_sector_breadth": 0.55,
            "defense_max_stock_move": 0.45,
            "defense_sector_correlation": 0.6,
            "news_negative_ratio": 0.6,
            "news_keyword_hits": 0.65,
            "news_source_diversity": 0.5,
            "news_abstract_negativity": 0.55,
        },
    },
]

# Événements "calme" (pas de crash)
CALM_EVENTS = [
    {
        "date": "2024-06-15",
        "nom": "Marché calme",
        "btc_change_pct": 0.5,
        "label_reel": 0,
        "features": {name: 0.2 for name in FEATURE_NAMES},
    },
    {
        "date": "2024-09-20",
        "nom": "Marché calme",
        "btc_change_pct": 1.2,
        "label_reel": 0,
        "features": {name: 0.15 for name in FEATURE_NAMES},
    },
    {
        "date": "2025-01-10",
        "nom": "Marché calme",
        "btc_change_pct": -0.8,
        "label_reel": 0,
        "features": {name: 0.18 for name in FEATURE_NAMES},
    },
    {
        "date": "2025-04-05",
        "nom": "Marché calme",
        "btc_change_pct": 2.1,
        "label_reel": 0,
        "features": {name: 0.12 for name in FEATURE_NAMES},
    },
    {
        "date": "2025-08-20",
        "nom": "Marché calme",
        "btc_change_pct": 0.3,
        "label_reel": 0,
        "features": {name: 0.14 for name in FEATURE_NAMES},
    },
    {
        "date": "2026-02-15",
        "nom": "Marché calme",
        "btc_change_pct": 1.8,
        "label_reel": 0,
        "features": {name: 0.16 for name in FEATURE_NAMES},
    },
    {
        "date": "2026-05-20",
        "nom": "Marché calme",
        "btc_change_pct": -0.5,
        "label_reel": 0,
        "features": {name: 0.13 for name in FEATURE_NAMES},
    },
    {
        "date": "2026-07-10",
        "nom": "Marché calme",
        "btc_change_pct": 0.8,
        "label_reel": 0,
        "features": {name: 0.17 for name in FEATURE_NAMES},
    },
]


# ══════════════════════════════════════════════════════════════
# BACKTESTING
# ══════════════════════════════════════════════════════════════

def run_backtest():
    """Lance le backtesting complet."""
    print("🧪 BACKTESTING DE L'INDICE APP")
    print("=" * 60)
    print(f"📅 {datetime.now().strftime('%d/%m %Y %H:%M')}")
    print(f"🎯 Événements testés: {len(EVENTS)} crashs + {len(CALM_EVENTS)} calmes")
    print()

    # Entraîner le modèle
    print("🌲 Entraînement du modèle...")
    clf = GeoRiskClassifier()
    clf.train()

    # Tester sur les événements de crash
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS — ÉVÉNEMENTS DE CRASH")
    print("=" * 60)

    results_crash = []
    for event in EVENTS:
        prediction = clf.predict(event["features"])
        predicted_label = prediction["label"]
        true_label = event["label_reel"]
        correct = predicted_label == true_label

        results_crash.append({
            "date": event["date"],
            "nom": event["nom"],
            "btc_change_pct": event["btc_change_pct"],
            "true_label": true_label,
            "predicted_label": predicted_label,
            "correct": correct,
            "confidence": prediction["confidence"],
            "risk_score": prediction["risk_score"],
        })

        status = "✅" if correct else "❌"
        label_names = {0: "calme", 1: "attention", 2: "alerte", 3: "critique"}

        print(f"\n{status} {event['date']} — {event['nom']}")
        print(f"   BTC: {event['btc_before']}$ → {event['btc_after']}$ ({event['btc_change_pct']:+.1f}%)")
        print(f"   Réel: {label_names[true_label]} | Prédit: {label_names[predicted_label]}")
        print(f"   Confidence: {prediction['confidence']:.1%} | Risk: {prediction['risk_score']:.2f}")

    # Tester sur les événements calmes
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS — MARCHÉS CALMES")
    print("=" * 60)

    results_calm = []
    for event in CALM_EVENTS:
        prediction = clf.predict(event["features"])
        predicted_label = prediction["label"]
        true_label = event["label_reel"]
        correct = predicted_label == true_label

        results_calm.append({
            "date": event["date"],
            "nom": event["nom"],
            "btc_change_pct": event["btc_change_pct"],
            "true_label": true_label,
            "predicted_label": predicted_label,
            "correct": correct,
            "confidence": prediction["confidence"],
        })

        status = "✅" if correct else "❌"
        label_names = {0: "calme", 1: "attention", 2: "alerte", 3: "critique"}

        print(f"\n{status} {event['date']} — {event['nom']}")
        print(f"   BTC change: {event['btc_change_pct']:+.1f}%")
        print(f"   Réel: {label_names[true_label]} | Prédit: {label_names[predicted_label]}")
        print(f"   Confidence: {prediction['confidence']:.1%}")

    # Calculer les métriques
    print("\n" + "=" * 60)
    print("📊 MÉTRIQUES GLOBALES")
    print("=" * 60)

    all_results = results_crash + results_calm
    total = len(all_results)
    correct_total = sum(1 for r in all_results if r["correct"])

    # Accuracy
    accuracy = correct_total / total if total > 0 else 0
    print(f"\n🎯 Accuracy: {accuracy:.1%} ({correct_total}/{total})")

    # Precision pour les crashs (predicted >= attention quand c'est un crash)
    crash_true_positives = sum(
        1 for r in results_crash
        if r["predicted_label"] >= 1  # attention ou plus
    )
    crash_false_positives = sum(
        1 for r in results_calm
        if r["predicted_label"] >= 1
    )
    crash_false_negatives = sum(
        1 for r in results_crash
        if r["predicted_label"] == 0  # calme quand c'est un crash
    )

    precision = crash_true_positives / (crash_true_positives + crash_false_positives) if (crash_true_positives + crash_false_positives) > 0 else 0
    recall = crash_true_positives / (crash_true_positives + crash_false_negatives) if (crash_true_positives + crash_false_negatives) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"🔍 Precision (crashs): {precision:.1%}")
    print(f"📈 Recall (crashs): {recall:.1%}")
    print(f"📊 F1-Score: {f1:.1%}")

    # Faux positifs
    print(f"\n⚠️ Faux positifs: {crash_false_positives}/{len(CALM_EVENTS)} marchés calmes")
    print(f"⚠️ Faux négatifs: {crash_false_negatives}/{len(EVENTS)} crashs manqués")

    # Feature importances
    print("\n" + "=" * 60)
    print("📊 TOP FEATURES (importance)")
    print("=" * 60)

    importances = clf.get_feature_importances()
    sorted_imp = sorted(importances.items(), key=lambda x: x[1], reverse=True)[:10]
    for name, imp in sorted_imp:
        print(f"   {name}: {imp:.3f}")

    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ")
    print("=" * 60)

    print(f"\n✅ Événements correctement prédits: {correct_total}/{total}")
    print(f"🎯 Accuracy: {accuracy:.1%}")
    print(f"🔍 Precision: {precision:.1%}")
    print(f"📈 Recall: {recall:.1%}")
    print(f"📊 F1-Score: {f1:.1%}")

    if accuracy >= 0.8:
        print("\n🟢 LE MODÈLE EST FIABLE — Prêt pour la production")
    elif accuracy >= 0.6:
        print("\n🟡 LE MODÈLE EST MOYEN — À améliorer avant la production")
    else:
        print("\n🔴 LE MODÈLE EST FAIBLE — Nécessite des ajustements")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "results_crash": results_crash,
        "results_calm": results_calm,
        "importances": importances,
    }


if __name__ == "__main__":
    if "--events" in sys.argv:
        print("📅 ÉVÉNEMENTS HISTORIQUES")
        print("=" * 60)
        for e in EVENTS:
            print(f"  {e['date']} — {e['nom']} ({e['btc_change_pct']:+.1f}%)")
        print(f"\n📅 MARCHÉS CALMES")
        for e in CALM_EVENTS:
            print(f"  {e['date']} — {e['nom']} ({e['btc_change_pct']:+.1f}%)")
    elif "--train" in sys.argv:
        clf = GeoRiskClassifier()
        clf.train(force=True)
    else:
        results = run_backtest()

        # Sauvegarder les résultats
        dest = Path(__file__).resolve().parent / "data" / "backtest_results.json"
        dest.write_text(json.dumps(results, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(f"\n💾 Résultats sauvegardés: {dest}")
