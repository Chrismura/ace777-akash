# AVIS CODEUR (provider Google Gemini)

Ici le **CODEUR de la famille ACE777**. Avis technique et stratégique strict, sans concession, orienté *Quant Desk / Market Making*.

---

### AVIS PRÉLIMINAIRE & PROPOSITION D'UNE APPROCHE DIFFÉRENTE (CLAUSE PERMANENTE)

La demande classique consiste à découper l'analyse par "indicateurs" (volume, volatilité, carnet d'ordres). **C'est une erreur sur les small caps / micro-caps sur CEX type MEXC.** 
Sur ces actifs, le carnet d'ordres (Order Book) est en grande partie spoofé, illisible ou alimenté par des market makers de pacotille (ou des bots de scam). Analyser la profondeur de carnet brute à haute fréquence ici, c'est **analyser du bruit pur**.

*   **Ce que je propose (L'Amélioration ACE777) :** Ne traite pas les 20 actifs de la même manière. Abandonne l'analyse traditionnelle du carnet d'ordres pour les micro-caps. Remplace-la par une **Approche Hybride par Régime de Liquidité et Flux d'Exécution (Trade-Flow Microstructure)**. On n'analyse pas *ce qui est affiché* (le carnet), mais *ce qui est consommé* (les trades exécutés, l'impact prix réel et la persistance de la toxicité du flux).

---

### MISSION 1 : LA MEILLEURE MÉTHODE (Cadre Norme Professionnelle)

Pour un set-up (Entrer / Tenir / Sortir), le comportement d'un actif se résume à 3 dimensions fondamentales : **La Profondeur du Bruit (Liquidité Réelle), la Vitesse de Propagation du Prix (Momentum vs Friction) et l'Asymétrie des Flux (Pression Acheteuse/Vendeuse réelle).**

#### 1. Dimensions à mesurer & Métriques Clés
*   **Dimension A : Friction & Liquidité Réelle**
    *   *Métrique 1 :* **Amihud Illiquidity Ratio** ($\text{Illiq} = \frac{|R_t|}{\text{Volume}_t}$). Mesure l'impact prix par unité de volume. Indispensable sur small cap.
    *   *Métrique 2 :* **Effective Spread** estimé via la méthode de Roll ou de Corwin-Schultz (basée sur High/Low), car les spreads affichés sur MEXC sont trompeurs.
*   **Dimension B : Dynamique de Volatilité & Persistance**
    *   *Métrique 1 :* **Ratio de Variance (VR - Variance Ratio Test)**. Permet de savoir si le prix suit une marche aléatoire (bruit) ou s'il y a un effet de trend / mean-reversion à court terme.
    *   *Métrique 2 :* **Parkinson Volatility** (basée sur High/Low) couplée à la volatilité de Close-to-Close pour détecter les sauts de prix (gaps intra-bougie).
*   **Dimension C : Asymétrie des Flux (Order Flow Imbalance - OFI adapté)**
    *   *Métrique 1 :* **Volume Synchronized Probability of Toxicity (VPIN)** ou une version simplifiée : **Trade Sign Delta** (Volume acheteur agressif vs vendeur agressif basé sur la règle de tick de Lee-Ready simplifiée).

#### 2. Fréquence d'Échantillonnage & Sources
*   **Fréquence :** Échantillonnage temporel fixe inadapté aux small caps. Utiliser **l'échantillonnage par barres de volume (Volume Bars)** ou **barres de ticks (Tick Bars)**. (Ex: 1 barre = 1% du volume journalier moyen). Cela normalise le temps en fonction de l'activité réelle.
*   **Sources :** API WebSocket publique MEXC pour les trades en temps réel (`spot/public/trades`) et l'historique des klines/trades. Ne pas stocker le carnet complet (Order Book depth 100) : sur MEXC, il est trop bruité et coûteux en stockage pour un gain nul.

---

### MISSION 2 : MÉTRIQUES DISCRIMINANTES VS BRUIT (Small Caps / MEXC)

| Indicateur / Métrique | Statut sur Small Cap / MEXC | Justification Technique |
| :--- | :--- | :--- |
| **Volume en USD brut** | ❌ **BRUIT PUR** | Faux volumes massifs (wash trading endémique sur MEXC). Inexploitable tel quel. |
| **Order Book Depth (Bids/Asks)** | ❌ **BRUIT PUR** | Spoofing permanent, ordres fantômes qui disparaissent dès l'approche du prix. |
| **RSI / MACD / Oscillateurs** | ❌ **BRUIT PUR** | Lagging, génèrent des faux signaux constants sur des actifs à forte amplitude erratique. |
| **Amihud Illiquidity Ratio** | ✅ **DISCRIMINANT** | Montre la résistance réelle du marché à absorber une taille d'ordre donnée. |
| **Trade Sign Delta (Aggressivité)** | ✅ **DISCRIMINANT** | Identifie si les ordres au marché mangent le carnet à l'achat ou à la vente (pression réelle). |
| **Corwin-Schultz Spread** | ✅ **DISCRIMINANT** | Estime le coût réel d'exécution (coût de sortie du trade) uniquement via les High/Low. |

---

### MISSION 3 : ARCHITECTURE DE COLLECTE & STOCKAGE (~20 paires)

Pour 20 paires sur MEXC, le volume de données est faible. Pas besoin d'une usine à gaz type Kafka/Hadoop. Une architecture légère, robuste et orientée temps réel est requise.

#### 1. Schéma d'Architecture
```
[MEXC WebSocket API] ---> (Node.js / Python Async Collector) 
                                   │
                                   ▼
                       [TimescaleDB / PostgreSQL] 
                                   │
                                   ▼
                      [Moteur d'Analyse (Python/Pandas/Polars)]
                                   │
                                   ▼
                      [Générateur de Set-up (Entrée/Sortie)]
```

#### 2. Spécifications Techniques
*   **Collecte (Ingestion) :** 
    *   Connexion WebSocket unique (multiplexage des 20 paires) pour les flux de **trades** (`deals`).
    *   Requête REST (Polling léger) toutes les 1 minutes pour récupérer l'état agrégé si besoin, mais le WS suffit pour les trades.
*   **Stockage :** 
    *   **TimescaleDB** (extension time-series de PostgreSQL). 
    *   Tables optimisées : `trades` (timestamp, price, size, side) et `derived_metrics` (stockage des calculs rolling : Amihud, Volatilité, Delta).
    *   *Volume estimé :* 20 paires small cap $\times$ ~500 trades/jour/paire = 10 000 lignes/jour. Stockage ridicule (< 50 Mo par an). Zéro risque d'exploser les limites d'API MEXC (qui autorisent largement ce volume en connexions publiques).
*   **Fréquence de Calcul :**
    *   Calcul en **streaming léger** ou par **fenêtre glissante (Rolling Window)** déclenchée à chaque clôture de barre de volume (et non à chaque seconde, pour éviter le over-fitting).

---

### MOT DE LA FIN DU CODEUR
Arrêtez de regarder les graphiques en chandeliers classiques et les carnets d'ordres de MEXC pour vos micro-caps. **Seul le flux de transactions exécutées (Trade Flow) et l'impact prix (Amihud/Spread implicite) disent la vérité.** Implémentez un stockage TimescaleDB sur les trades bruts, calculez des barres de volume, et déduisez-en la toxicité du flux. C'est la seule méthode robuste niveau Quant Desk.
