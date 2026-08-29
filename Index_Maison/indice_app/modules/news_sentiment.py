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
        """Collecte les titres d'actualité.

        Correction 29/08 (Buffy + famille + Christophe) : avant, les 5 requêtes
        étaient TOUTES négatives ('crisis','war','sanctions') -> le ratio négatif
        était biaisé à ~82% en permanence, donc alerte 🔴 même quand le monde
        n'est pas plus tendu que d'habitude.

        Maintenant on collecte DEUX groupes :
          - geo_titres   : sujets géopolitiques (le signal qu'on surveille)
          - neutre_titres: actualité générale sans mot de crise (le NIVEAU DE BASE)
        L'alerte mesure la tension RELATIVE : geo_beaucoup_plus_negatif_que_neutre
        = vraie tension géopolitique ; à égalité = le monde est comme d'habitude.
        """
        try:
            # Sujets géopolitiques (signal) — on garde l'intention de surveiller
            # les crises, mais leur ratio sera comparé au bruit de fond neutre.
            geo_queries = [
                "bitcoin geopolitical crisis",
                "US military deployment",
                "sanctions crypto",
                "war escalation",
                "economic crisis",
            ]
            # Actualité générale NEUTRE (contrôle = niveau de base du monde).
            neutre_queries = [
                "bitcoin news today",
                "crypto market update",
                "US economy today",
                "global markets news",
            ]

            geo_titres = []
            for q in geo_queries:
                geo_titres.extend(self._search_news(q))
            neutre_titres = []
            for q in neutre_queries:
                neutre_titres.extend(self._search_news(q))

            # DuckDuckGo pour le contexte
            ddg_data = self._search_ddg("bitcoin geopolitical risk today")

            return {
                "titres": geo_titres,
                "geo_titres": geo_titres,
                "neutre_titres": neutre_titres,
                "nb_titres": len(geo_titres),
                "nb_geo": len(geo_titres),
                "nb_neutre": len(neutre_titres),
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

    @staticmethod
    def _ratio_neg(titres) -> float:
        """Fraction de titres contenant au moins un mot-clé négatif."""
        if not titres:
            return 0.0
        nb = 0
        for t in titres:
            tl = t.lower()
            for kw in KEYWORDS_NEGATIFS:
                if kw in tl:
                    nb += 1
                    break
        return nb / len(titres)

    def feature(self, raw: Dict[str, Any]) -> Dict[str, float]:
        """Transforme les données en features numériques.

        Correction 29/08 : la tension est mesurée en RELATIF. On calcule
        neg_ratio_geo (sujets géopolitiques) ET neg_ratio_neutre (actualité
        générale). Le signal = le DÉPASSEMENT du géopolitique sur le bruit de
        fond du monde : si le geopol est aussi négatif que l'actualité générale,
        c'est une journée normale (pas d'alerte). L'alerte ne monte que quand
        le négatif géopolitique est nettement SUPÉRIEUR au détail général.
        """
        geo_titres = raw.get("geo_titres") or raw.get("titres") or []
        neutre_titres = raw.get("neutre_titres") or []
        ddg = raw.get("ddg", {})

        neg_geo = self._ratio_neg(geo_titres)          # ex 0.82 avant
        neg_neutre = self._ratio_neg(neutre_titres)    # ex 0.15
        # Dépassement relatif : combien le geopol est PLUS négatif que le monde.
        # neutre=0.15, geo=0.82 -> depassement 0.67 (forte tension).
        # neutre=0.15, geo=0.15 -> depassement 0.00 (journée normale, pas d'alerte).
        depassement = max(0.0, neg_geo - neg_neutre)
        f_negative = self.normalize(depassement, 0.0, 0.6)

        # Feature 2: Nombre de keywords négatifs uniques (sur les sujets geo, confirme)
        unique_neg = set()
        for t in geo_titres:
            tl = t.lower()
            for kw in KEYWORDS_NEGATIFS:
                if kw in tl:
                    unique_neg.add(kw)
        f_keyword_hits = self.normalize(len(unique_neg), 0, 10)

        # Feature 3: Diversité des sources (plus de sources = plus fiable)
        nb_titres = len(geo_titres)
        f_diversity = self.normalize(nb_titres, 0, 40)

        # Feature 4: Abstract DuckDuckGo (si négatif — contexte seulement)
        abstract = ddg.get("abstract", "").lower()
        abstract_neg = sum(1 for kw in KEYWORDS_NEGATIFS if kw in abstract)
        f_abstract = self.normalize(abstract_neg, 0, 5)

        return {
            "negative_ratio": round(f_negative, 4),
            "keyword_hits": round(f_keyword_hits, 4),
            "source_diversity": round(f_diversity, 4),
            "abstract_negativity": round(f_abstract, 4),
            # diagnostics lisibles (pour les apps / debug)
            "neg_geo_raw": round(neg_geo, 3),
            "neg_neutre_raw": round(neg_neutre, 3),
        }

    # ─── Phase 3: Scoring ──────────────────────────────────────

    def score(self, features: Dict[str, float]) -> float:
        """Score pondéré — axé sur la TENSION RELATIVE (correction 29/08).

        negative_ratio domine (0.60) car c'est le dépassement geo vs neutre.
        Les autres features sont des CONFIRMATIONS secondaires, pas des
        signaux principaux — sinon keyword_hits/diversity créaient un plancher
        fixe (~0.38) même quand le monde est calme.
        """
        poids = {
            "negative_ratio": 0.60,       # Signal PRINCIPAL : dépassement geo vs neutre
            "keyword_hits": 0.20,          # Confirme (mais cherche des mots crise -> secondaire)
            "source_diversity": 0.10,      # Fiabilité (faible : nb titres géo assez stable)
            "abstract_negativity": 0.10,   # Contexte DDG (secondaire)
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
