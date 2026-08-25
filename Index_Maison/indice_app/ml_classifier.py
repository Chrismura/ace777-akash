#!/usr/bin/env python3
"""
ml_classifier.py — CLASSIFICATEUR ML POUR RISQUE GÉOPOLITIQUE
=============================================================

Utilise un RandomForest pour prédire le risque à partir des features
des 5 modules (pizza, jets, oil, defense, news).

Entraînement :
  - Si pas de modèle → entraîne sur des données simulées (baselines)
  - Si modèle existe → charge et utilise

Usage :
  python3 ml_classifier.py                  # Entraîne + prédit
  python3 ml_classifier.py --predict FILE   # Prédit depuis un fichier
  python3 ml_classifier.py --retrain        # Ré-entraîne le modèle

Inspiré de War-Probability-OSINT (RandomForestClassifier).
"""

import json
import os
import pickle
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


# ══════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════

DATA_DIR = Path(__file__).resolve().parent / "data"
MODEL_FILE = DATA_DIR / "ml_model.pkl"
SCALER_FILE = DATA_DIR / "ml_scaler.pkl"
TRAINING_DATA = DATA_DIR / "ml_training_data.json"

# Noms des features (doivent correspondre aux modules)
FEATURE_NAMES = [
    # Pizza Index (4 features)
    "pizza_doughcon_level",
    "pizza_spike_max",
    "pizza_location_count",
    "pizza_spike_consistency",
    # Jets ADS-B (4 features)
    "jets_military_surge",
    "jets_military_ratio",
    "jets_altitude_avg",
    "jets_velocity_avg",
    # Oil Price (4 features)
    "oil_price_change_1h",
    "oil_price_change_24h",
    "oil_brent_wti_spread",
    "oil_volatility",
    # Defense Stocks (4 features)
    "defense_sector_avg_change",
    "defense_sector_breadth",
    "defense_max_stock_move",
    "defense_sector_correlation",
    # News Sentiment (4 features)
    "news_negative_ratio",
    "news_keyword_hits",
    "news_source_diversity",
    "news_abstract_negativity",
]

# Labels (0=calme, 1=attention, 2=alerte, 3=critique)
LABELS = {
    0: {"nom": "calme", "emoji": "🟢"},
    1: {"nom": "attention", "emoji": "🟡"},
    2: {"nom": "alerte", "emoji": "🔴"},
    3: {"nom": "critique", "emoji": "🚨"},
}


# ══════════════════════════════════════════════════════════════
# DONNÉES D'ENTRAÎNEMENT SIMULÉES
# ══════════════════════════════════════════════════════════════

def generate_training_data(n_samples: int = 500) -> Tuple[np.ndarray, np.ndarray]:
    """
    Génère des données d'entraînement simulées.
    Basé sur les patterns historiques réels.
    """
    np.random.seed(42)
    X = []
    y = []

    for _ in range(n_samples):
        label = np.random.choice([0, 1, 2, 3], p=[0.5, 0.25, 0.15, 0.10])

        if label == 0:  # Calme
            features = np.random.normal(0.2, 0.1, len(FEATURE_NAMES))
        elif label == 1:  # Attention
            features = np.random.normal(0.4, 0.15, len(FEATURE_NAMES))
        elif label == 2:  # Alerte
            features = np.random.normal(0.65, 0.15, len(FEATURE_NAMES))
        else:  # Critique
            features = np.random.normal(0.85, 0.1, len(FEATURE_NAMES))

        features = np.clip(features, 0, 1)
        X.append(features)
        y.append(label)

    return np.array(X), np.array(y)


# ══════════════════════════════════════════════════════════════
# CLASSIFICATEUR
# ══════════════════════════════════════════════════════════════

class GeoRiskClassifier:
    """Classificateur ML pour le risque géopolitique."""

    def __init__(self):
        self.model = None
        self.scaler = None
        self.is_trained = False

    def train(self, force: bool = False):
        """Entraîne le modèle (ou charge si déjà entraîné)."""
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        # Charger si existe et pas force
        if not force and MODEL_FILE.exists() and SCALER_FILE.exists():
            try:
                with open(MODEL_FILE, "rb") as f:
                    self.model = pickle.load(f)
                with open(SCALER_FILE, "rb") as f:
                    self.scaler = pickle.load(f)
                self.is_trained = True
                print("✅ Modèle chargé depuis le disque")
                return
            except Exception:
                print("⚠️ Modèle corrompu → ré-entraînement")

        # Générer les données d'entraînement
        print("📊 Génération des données d'entraînement...")
        X, y = generate_training_data(500)

        # Normaliser
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)

        # Entraîner le RandomForest
        print("🌲 Entraînement du RandomForest...")
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
        )
        self.model.fit(X_scaled, y)
        self.is_trained = True

        # Sauvegarder
        with open(MODEL_FILE, "wb") as f:
            pickle.dump(self.model, f)
        with open(SCALER_FILE, "wb") as f:
            pickle.dump(self.scaler, f)

        # Accuracy
        accuracy = self.model.score(X_scaled, y)
        print(f"✅ Modèle entraîné (accuracy: {accuracy:.2%})")

        # Feature importances
        importances = self.model.feature_importances_
        top_features = sorted(
            zip(FEATURE_NAMES, importances),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        print("\n📊 Top 10 features:")
        for name, imp in top_features:
            print(f"   {name}: {imp:.3f}")

    def predict(self, features: Dict[str, float]) -> Dict[str, Any]:
        """
        Prédit le niveau de risque à partir des features.
        Retourne {label, probability, confidence, risk_level}.
        """
        if not self.is_trained:
            self.train()

        # Construire le vecteur de features
        vector = []
        for name in FEATURE_NAMES:
            # Extraire la valeur depuis le dict (avec préfixe module)
            parts = name.split("_", 1)
            module = parts[0]
            feature = parts[1]

            # Chercher dans les features du module
            val = 0.5  # défaut
            for key, value in features.items():
                if module in key and feature in key:
                    val = value
                    break
            vector.append(val)

        X = np.array([vector])
        X_scaled = self.scaler.transform(X)

        # Prédiction
        probas = self.model.predict_proba(X_scaled)[0]
        label = int(np.argmax(probas))
        confidence = float(probas[label])

        # Risk level
        risk_score = float(np.dot(probas, [0, 1, 2, 3]) / 3)

        return {
            "label": label,
            "label_nom": LABELS[label]["nom"],
            "label_emoji": LABELS[label]["emoji"],
            "probability": round(float(probas[label]), 4),
            "confidence": round(confidence, 4),
            "risk_score": round(risk_score, 4),
            "probas": {
                LABELS[i]["nom"]: round(float(p), 4)
                for i, p in enumerate(probas)
            },
        }

    def get_feature_importances(self) -> Dict[str, float]:
        """Retourne l'importance de chaque feature."""
        if not self.is_trained:
            return {}
        importances = self.model.feature_importances_
        return {
            name: round(float(imp), 4)
            for name, imp in zip(FEATURE_NAMES, importances)
        }


# ══════════════════════════════════════════════════════════════
# INTERFACE
# ══════════════════════════════════════════════════════════════

def run_classifier(features: Dict[str, float]) -> Dict[str, Any]:
    """Lance le classificateur avec les features données."""
    clf = GeoRiskClassifier()
    clf.train()
    result = clf.predict(features)
    result["feature_importances"] = clf.get_feature_importances()
    result["ts"] = datetime.now(timezone.utc).isoformat()
    return result


if __name__ == "__main__":
    import sys

    if "--retrain" in sys.argv:
        clf = GeoRiskClassifier()
        clf.train(force=True)
        print(json.dumps(clf.get_feature_importances(), indent=2))

    elif "--predict" in sys.argv:
        idx = sys.argv.index("--predict")
        if idx + 1 < len(sys.argv):
            features_file = sys.argv[idx + 1]
            features = json.loads(Path(features_file).read_text())
            result = run_classifier(features)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print("Usage: python3 ml_classifier.py --predict features.json")

    else:
        # Entraîner et tester avec des features simulées
        print("🌲 ML CLASSIFIER — Entraînement + test")
        print("=" * 50)

        clf = GeoRiskClassifier()
        clf.train()

        # Test avec des features simulées
        test_features = {name: 0.3 for name in FEATURE_NAMES}
        test_features["pizza_doughcon_level"] = 0.8
        test_features["jets_military_surge"] = 0.7

        result = clf.predict(test_features)
        print(f"\n📊 Test avec features élevées:")
        print(f"   Label: {result['label_emoji']} {result['label_nom']}")
        print(f"   Confidence: {result['confidence']:.2%}")
        print(f"   Risk Score: {result['risk_score']:.2f}")
        print(f"   Probas: {result['probas']}")
