#!/usr/bin/env python3
"""
news_sentiment.py — NEWS SENTIMENT (4-phase)
=============================================

Phase 1 (collect)  : Google News RSS + DuckDuckGo
Phase 2 (feature)  : negative_ratio, keyword_hits, source_diversity
Phase 3 (score)    : z-score combiné
Phase 4 (interpret) : niveau d'alerte + action

Historique :
  - Les pics de sentiment négatif précèdent les crashs de 24-72h
  - Les keywords géopolitiques (war, sanctions, strike) = signal fort

Source : Google News RSS (gratuit) + DuckDuckGo
"""

import json
import re
import urllib.parse
import urllib.request
from typing import Dict, Any

from indice_app.base import IndicateurBase


# Keywords géopolitiques négatifs (signal de crise)
KEYWORDS_NEGATIFS = [
    "war", "guerre", "strike", "frappe", "attack", "attaque",
    "sanctions", "embargo", "blockade", "blocus",
    "nuclear", "nucléaire", "missile", "bombing",
    "invasion", "escalation", "crisis", "crise",
    "recession", "default", "défaut", "collapse", "effondrement",
    "crash", "plunge", "tumble", "chute",
    "military", "militaire", "troops", "troupes",
    "deploy", "déploy", "alert", "vigilance",
]

# Keywords positifs (signal de retour au calme)
KEYWORDSPOSITIFS = [
    "peace", "paix", "deal", "accord", "agreement",
    "ceasefire", "cessez-le-feu", "negotiation", "négociation",
    "recovery", "récupération", "rally", "hausse",
    "cooperation", "coopération", "summit", "sommert",
]

# Baselines
BASELINE_NEGATIVE_RATIO = 0.3    # 30% de titres négatifs en temps calme
STDDEV_NEGATIVE_RATIO = 0.15


class NewsSentiment(IndicateurBase):
    NOM = "news_sentiment"
    CATEGORIE = "geopol"
    SOURCE = "Google News RSS"
    DESCRIPTION = "Sentiment des actualités géopolitiques"

    # ─── Phase 1: Data Acquisition ──────────────────────────────

    def collect(self) -> Dict[str, Any]:
        """Collecte les titres d'actualité."""
        try:
            # Recherche sur les sujets géopolitiques
            queries = [
                "bitcoin geopolitical crisis",
                "US military deployment",
                "sanctions crypto",
                "war escalation",
                "economic crisis",
            ]

            all_titres = []
            for q in queries:
                titres = self._search_news(q)
                all_titres.extend(titres)

            # DuckDuckGo pour le contexte
            ddg_data = self._search_ddg("bitcoin geopolitical risk today")

            return {
                "titres": all_titres,
                "nb_titres": len(all_titres),
                "ddg": ddg_data,
                "source": "google-news-rss + duckduckgo",
            }
        except Exception as e:
            return {"_erreur": str(e)}

    def _search_news(self, query: str) -> list:
        """Recherche via Google News RSS."""
        try:
            url = (
                f"https://news.google.com/rss/search"
                f"?q={urllib.parse.quote(query)}&hl=en&gl=US&ceid=US:en"
            )
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ACE777-indice/1.0"},
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                xml = r.read().decode("utf-8", errors="ignore")

            # Extraire les titres
            titres = re.findall(r"<title>(.*?)</title>", xml, re.DOTALL)
            titres = [re.sub(r"<[^>]+>", "", t).strip() for t in titres[1:]]
            return [t for t in titres if t][:8]
        except Exception:
            return []

    def _search_ddg(self, query: str) -> Dict[str, Any]:
        """Recherche via DuckDuckGo."""
        try:
            url = (
                f"https://api.duckduckgo.com/"
                f"?q={urllib.parse.quote(query)}&format=json&no_html=1"
            )
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ACE777-indice/1.0"},
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())

            abstract = data.get("AbstractText", "")
            topics = [
                t.get("Text", "")
                for t in data.get("RelatedTopics", [])[:5]
                if t.get("Text")
            ]
            return {"abstract": abstract[:300], "topics": topics}
        except Exception:
            return {}

    # ─── Phase 2: Feature Engineering ───────────────────────────

    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """Transforme les données en features numériques."""
        titres = raw.get("titres", [])
        ddg = raw.get("ddg", {})

        # Feature 1: Ratio de mots-clés négatifs
        nb_neg = 0
        nb_pos = 0
        for t in titres:
            t_lower = t.lower()
            for kw in KEYWORDS_NEGATIFS:
                if kw in t_lower:
                    nb_neg += 1
                    break
            for kw in KEYWORDSPOSITIFS:
                if kw in t_lower:
                    nb_pos += 1
                    break

        total = len(titres) if titres else 1
        neg_ratio = nb_neg / total
        f_negative = self.zscore(neg_ratio, BASELINE_NEGATIVE_RATIO, STDDEV_NEGATIVE_RATIO)
        f_negative = self.normalize(f_negative, -2, 4)

        # Feature 2: Nombre de keywords négatifs uniques
        unique_neg = set()
        for t in titres:
            t_lower = t.lower()
            for kw in KEYWORDS_NEGATIFS:
                if kw in t_lower:
                    unique_neg.add(kw)
        f_keyword_hits = self.normalize(len(unique_neg), 0, 10)

        # Feature 3: Diversité des sources (plus de sources = plus fiable)
        nb_titres = raw.get("nb_titres", 0)
        f_diversity = self.normalize(nb_titres, 0, 40)

        # Feature 4: Abstract DuckDuckGo (si négatif)
        abstract = ddg.get("abstract", "").lower()
        abstract_neg = sum(1 for kw in KEYWORDS_NEGATIFS if kw in abstract)
        f_abstract = self.normalize(abstract_neg, 0, 5)

        return {
            "negative_ratio": round(f_negative, 4),
            "keyword_hits": round(f_keyword_hits, 4),
            "source_diversity": round(f_diversity, 4),
            "abstract_negativity": round(f_abstract, 4),
        }

    # ─── Phase 3: Scoring ──────────────────────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """Score pondéré."""
        poids = {
            "negative_ratio": 0.40,       # Signal principal
            "keyword_hits": 0.25,          # Confirme
            "source_diversity": 0.15,      # Fiabilité
            "abstract_negativity": 0.20,   # Contexte
        }
        score = sum(features.get(k, 0) * v for k, v in poids.items())
        return max(0.0, min(1.0, score))

    # ─── Phase 4: Interpretation ───────────────────────────────

    def interpret(self, features: Dict[str, float], score_val: float) -> str:
        """Interprétation en français."""
        neg_ratio = features.get("negative_ratio", 0)
        keyword_hits = features.get("keyword_hits", 0)

        if score_val >= 0.8:
            return (
                f"🚨 KILL SWITCH — Sentiment extrêmement négatif. "
                f"{int(keyword_hits * 10)} mots-clés de crise détectés. "
                f"Réduire les positions. Ne pas trader."
            )
        elif score_val >= 0.6:
            return (
                f"🔴 ALERTE — Sentiment très négatif. "
                f"Risque de crash imminent. "
                f"Surveiller de près."
            )
        elif score_val >= 0.3:
            return (
                f"🟡 ATTENTION — Sentiment légèrement négatif. "
                f"À surveiller."
            )
        else:
            return (
                f"🟢 CALME — Sentiment neutre ou positif. "
                f"Rien d'inhabituel."
            )
