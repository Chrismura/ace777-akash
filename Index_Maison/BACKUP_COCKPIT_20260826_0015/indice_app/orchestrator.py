#!/usr/bin/env python3
"""
orchestrator.py — ORCHESTRATEUR DE L'INDICE APP (v2)
=====================================================

Architecture 4-phase (inspirée War-Probability-OSINT) :
  Phase 1: Data Acquisition  → chaque module collect()
  Phase 2: Feature Engineering → chaque module feature()
  Phase 3: Scoring            → chaque module score() + score unifié
  Phase 4: Interpretation     → chaque module interpret()

Modules :
  1. Pizza Index     → Pizzerias Pentagon (pizzint.watch)
  2. Jets ADS-B      → Trafic aérien Washington DC (OpenSky)
  3. Oil Price       → Prix du pétrole (API gratuite)
  4. Defense Stocks  → Actions défense (Yahoo Finance)

Usage :
  python3 orchestrator.py              # Tous les modules
  python3 orchestrator.py --pizza      # Pizza Index seulement
  python3 orchestrator.py --jets       # Jets ADS-B seulement
  python3 orchestrator.py --oil        # Oil Price seulement
  python3 orchestrator.py --defense    # Defense Stocks seulement
  python3 orchestrator.py --status     # Statut
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ajouter le chemin parent pour les imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from indice_app.modules.pizza_index import PizzaIndex
from indice_app.modules.jets_adsb import JetsADSB
from indice_app.modules.oil_price import OilPrice
from indice_app.modules.defense_stocks import DefenseStocks
from indice_app.modules.news_sentiment import NewsSentiment
from indice_app.ml_classifier import GeoRiskClassifier


# ══════════════════════════════════════════════════════════════
# REGISTRE DES MODULES
# ══════════════════════════════════════════════════════════════

MODULES = {
    "pizza_index": PizzaIndex,
    "jets_adsb": JetsADSB,
    "oil_price": OilPrice,
    "defense_stocks": DefenseStocks,
    "news_sentiment": NewsSentiment,
}

# Poids par catégorie (pour le score unifié)
POIDS_CATEGORIES = {
    "geopol": 0.60,    # Les indicateurs géopol comptent plus
    "market": 0.40,    # Les indicateurs de marché complètent
}


def run_all():
    """Exécute tous les modules et retourne le scoring unifié."""
    resultats = {}
    all_features = {}
    scores_par_categorie = {}

    for nom, classe in MODULES.items():
        try:
            module = classe()
            result = module.run()
            resultats[nom] = result

            # Collecter les features pour le ML
            features = result.get("features", {})
            for k, v in features.items():
                all_features[f"{nom}_{k}"] = v

            # Regrouper par catégorie
            cat = result.get("categorie", "general")
            if cat not in scores_par_categorie:
                scores_par_categorie[cat] = []
            scores_par_categorie[cat].append(result.get("score", 0.5))

        except Exception as e:
            resultats[nom] = {
                "nom": nom,
                "score": 0.5,
                "interpretation": f"Erreur module: {e}",
                "_erreur": str(e),
            }

    # Score unifié : moyenne pondérée par catégorie
    score_total = 0.0
    poids_total = 0.0
    for cat, scores in scores_par_categorie.items():
        poids = POIDS_CATEGORIES.get(cat, 0.5)
        avg_cat = sum(scores) / len(scores) if scores else 0.5
        score_total += avg_cat * poids
        poids_total += poids

    if poids_total > 0:
        score_unifie = score_total / poids_total
    else:
        score_unifie = 0.5

    # ─── ML CLASSIFIER ───────────────────────────────────────
    ml_result = None
    try:
        clf = GeoRiskClassifier()
        clf.train()
        ml_result = clf.predict(all_features)
        ml_result["feature_importances"] = clf.get_feature_importances()
    except Exception as e:
        ml_result = {"erreur": str(e)}

    # Niveau global (ML si disponible, sinon heuristique)
    if ml_result and not ml_result.get("erreur"):
        niveau = ml_result.get("label_nom", "calme")
        emoji = ml_result.get("label_emoji", "🟢")
        ml_score = ml_result.get("risk_score", 0.5)
    else:
        # Fallback heuristique
        if score_unifie >= 0.8:
            niveau = "critique"
            emoji = "🚨"
        elif score_unifie >= 0.6:
            niveau = "alerte"
            emoji = "🔴"
        elif score_unifie >= 0.3:
            niveau = "attention"
            emoji = "🟡"
        else:
            niveau = "calme"
            emoji = "🟢"
        ml_score = score_unifie

    # Alerte (le premier module qui dépasse 0.8)
    alerte = None
    for nom, res in resultats.items():
        if res.get("score", 0) >= 0.8:
            alerte = f"{emoji} {nom}: {res.get('interpretation', '')}"
            break

    # Stats
    nb_ok = sum(1 for r in resultats.values() if not r.get("_erreur"))
    nb_total = len(MODULES)

    out = {
        "geopol": {
            "score": round(score_unifie, 4),
            "ml_score": round(ml_score, 4) if ml_result else None,
            "niveau": niveau,
            "emoji": emoji,
            "ml": ml_result,
            "indicateurs": {
                nom: {
                    "score": res.get("score", 0.5),
                    "categorie": res.get("categorie", "general"),
                    "source": res.get("source", "inconnu"),
                    "interpretation": res.get("interpretation", ""),
                    "features": res.get("features", {}),
                }
                for nom, res in resultats.items()
            },
            "alerte": alerte,
            "nb_modules": nb_total,
            "nb_ok": nb_ok,
            "scores_par_categorie": {
                cat: round(sum(s) / len(s), 4) if s else 0.5
                for cat, s in scores_par_categorie.items()
            },
            "ts": datetime.now(timezone.utc).isoformat(),
        }
    }

    return out


def save_scores(data):
    """Sauvegarde les scores dans scores_geopol.json."""
    dest = Path(__file__).resolve().parent / "data" / "scores_geopol.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return dest


def show_status(data):
    """Affiche le statut de l'indice app."""
    geo = data.get("geopol", {})
    print(f"\n🍕 INDICE APP v2 — STATUT")
    print("=" * 60)
    print(f"📅 {geo.get('ts', 'N/A')}")
    print(f"🎯 Score unifié: {geo.get('score', 0.5)} {geo.get('emoji', '')}")
    print(f"📊 Niveau: {geo.get('niveau', 'inconnu').upper()}")
    print(f"🔧 Modules: {geo.get('nb_ok', 0)}/{geo.get('nb_modules', 0)} actifs")

    if geo.get("alerte"):
        print(f"\n🚨 ALERTE: {geo['alerte']}")

    # Scores par catégorie
    print(f"\n📋 Scores par catégorie:")
    for cat, score in geo.get("scores_par_categorie", {}).items():
        print(f"   {cat}: {score}")

    # Détail par indicateur
    print(f"\n📋 Détail par indicateur:")
    for nom, ind in geo.get("indicateurs", {}).items():
        score = ind.get("score", 0.5)
        cat = ind.get("categorie", "?")
        interp = ind.get("interpretation", "")[:70]
        print(f"   [{cat}] {nom}: {score}")
        print(f"      {interp}")

    print()


if __name__ == "__main__":
    if "--status" in sys.argv:
        dest = Path(__file__).resolve().parent / "data" / "scores_geopol.json"
        if dest.exists():
            data = json.loads(dest.read_text())
            show_status(data)
        else:
            print("Aucun score disponible. Lancez sans --status d'abord.")
    elif "--pizza" in sys.argv:
        module = PizzaIndex()
        result = module.run()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif "--jets" in sys.argv:
        module = JetsADSB()
        result = module.run()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif "--oil" in sys.argv:
        module = OilPrice()
        result = module.run()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif "--defense" in sys.argv:
        module = DefenseStocks()
        result = module.run()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif "--news" in sys.argv:
        module = NewsSentiment()
        result = module.run()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif "--ml" in sys.argv:
        from indice_app.ml_classifier import GeoRiskClassifier
        clf = GeoRiskClassifier()
        clf.train(force=True)
        importances = clf.get_feature_importances()
        print(json.dumps(importances, indent=2))
    else:
        print("🍕 INDICE APP v2 — Exécution de tous les modules...")
        data = run_all()
        dest = save_scores(data)
        show_status(data)
        print(f"💾 Sauvegardé: {dest}")
