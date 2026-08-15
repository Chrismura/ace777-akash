# AVIS gemini (provider Google Gemini, 9.0s)

Reçu 5 sur 5, Superviseur Buffy. Ici la flottille, les moteurs chauffent et les sondes mempool sont prêtes. On plonge direct dans le vif du sujet avec le protocole anti-hallucination activé.

---

### 1) Entités et adresses clés à surveiller (Exemples concrets)

Pour capter le flux sans noyer le cockpit, voici les cibles prioritaires à cartographier :

*   **Grands Exchanges (Inflows = Pression vendeuse potentielle / Outflows = Accumulation) :**
    *   *Binance Cold/Hot Wallets* : Indispensable, c'est le cœur de la liquidité mondiale.
    *   *Coinbase Prime* : Le baromètre institutionnel US et des ETF.
    *   *Bitfinex* : Historiquement lié aux mouvements de gros volumes et au market making.
    *   *À surveiller* : Leurs adresses de dépôt et de retrait connues. *(Vérification obligatoire via les étiquettes Arkham/Bitinfocharts avant insertion).*
*   **Les ETF Spot (Le nouveau grand driver) :**
    *   *BlackRock (iShares - IBIT)* : Custodié par Coinbase Prime. Leurs mouvements dictent souvent la tendance institutionnelle US.
    *   *Fidelity (FBTC)* : Custodie interne/hybride importante.
    *   *Grayscale (GBTC)* : Historiquement sujet à des sorties massives (arbitrage/faillites passées), à surveiller de près.
*   **Trésoreries d'entreprises & Acteurs majeurs :**
    *   *MicroStrategy (Strategy)* : Leurs achats massifs impactent directement le prix. Leurs adresses de custody doivent être pistées.
    *   *Tether (Treasury)* : Les mints/burns et transferts vers les exchanges soutiennent souvent le market.
*   **Gouvernements & Saisies (Ventes "forcées" imprévisibles) :**
    *   *États-Unis (USMS / DOJ)* et *Allemagne (BKA)* : Leurs transferts vers les exchanges annoncent des ventes de liquidations judiciaires qui font plier le marché.
*   **Mineurs majeurs (Capitulation ou thésaurisation) :**
    *   *Pools de minage (F2Pool, AntPool, Foundry)* : Des transferts soudains de leurs wallets vers les exchanges signalent souvent des besoins de trésorerie (frais de बिजली/électricité) ou une capitulation imminente.

---

### 2) Où trouver ces adresses gratuitement et sans clé payante ?

Pas besoin de casser la tirelire ni d'acheter des abonnements Arkham à 1000 $/mois pour démarrer. Les sources open-source gratuites :

*   **Arkacom / Arkham Intelligence (Version gratuite web)** : Même sans API payante, l'explorateur public permet de chercher "Binance Cold Storage", "BlackRock Bitcoin ETF", etc., et de copier les clusters d'adresses identifiés.
*   **BitInfoCharts (Top 100 Richest Bitcoin Addresses)** : Gratuit, public. Permet d'identifier les plus grosses adresses non étiquetées et de croiser avec les alertes de gros volumes.
*   **DeFiLlama & Bitbo** : Suivi des réserves des ETF Bitcoin en temps réel (donne une idée des volumes globaux bougés quotidiennement).
*   **GitHub / Repos open-source communautaires** : Des développeurs publient régulièrement des listes JSON/CSV d'adresses d'exchanges maintenues par la communauté (ex: listes utilisées par des outils de privacy ou d'analytics on-chain open-source).
*   *Règle d'or de la flottille* : **Aucune adresse trouvée en ligne ne rentre en dur sans un double check** sur mempool.space pour valider l'activité récente de l'adresse.

---

### 3) Détection des mouvements et traque de la fragmentation

*   **Inflow vs Outflow vs Interne :**
    *   *Inflow (Exchange)* : Une adresse connue de notre base (client) envoie vers une adresse étiquetée "Exchange". $\rightarrow$ Alerte rouge : risque de vente.
    *   *Outflow (Exchange)* : Un exchange envoie vers une adresse externe (froid/institution). $\rightarrow$ Alerte verte : sortie du marché, accumulation.
    *   *Interne* : Transfert entre deux adresses de la *même* entité (ex: rebrassage de cold wallets par Binance). *Piège classique à filtrer pour éviter les fausses alertes.*
*   **Détecter la fragmentation (Le "Sybil/Cluster Splitting" des baleines malines) :**
    *   Puisque les baleines éclatent leurs gros montants en 10-50 transactions (ex: 20 tx de 5 BTC à 50 BTC au lieu d'un bloc de 1000 BTC), **l'analyse séquentielle dans le mempool s'impose**.
    *   *Méthode* : Surveiller les flux entrants/sortants d'un même cluster d'adresses dans une fenêtre glissante courte (ex: 10 à 30 minutes). Si 20 transactions distinctes proviennent de la même entité source ou partent vers le même exchange, notre script doit agréger ces flux pour reconstituer la "vraie" taille du mouvement global (ex: $20 \times 3$, $5$ BTC $= 700$ BTC groupés).
    *   *Heuristique Bitcoin* : Analyser les inputs/outputs (notamment les transactions avec de multiples destinataires ou le co-spending) pour lier des adresses non étiquetées à nos entités connues.

---

### 4) Quel seuil retenir pour 2026 ?

L'intuition de Christophe (autour de **100 M$**) est chirurgicale pour 2026. 

*   En prenant un BTC à ~63 000 $ (ou plus selon le cycle actuel), **100 M$ représente environ 1 500 à 1 600 BTC**.
*   **Recommandation de la flottille** : 
    *   Fixer le seuil d'alerte brut (pour une seule transaction) à **1 000 BTC** (ce qui couvre la zone 60M$-100M$+ selon la volatilité du cours).
    *   **Pour la fragmentation** : Activer un *seuil cumulé* (Rolling Window) : si une entité connue éclate ses fonds en plusieurs tx atteignant un cumul de **1 500 BTC / 100 M$** sur une fenêtre de 1 heure, le signal "Gros Mouvement / Baleine Maline" s'active dans ADA et le cockpit.

---

### 5) Recommandation d'architecture (De zéro à l'infinité)

Pour démarrer vite, bien, et sans usine à gaz :

1.  **Phase 1 : Le MVP Local (JSON / CSV + Python)**
    *   Un simple fichier `whales_db.json` structuré proprement :
        ```json
        {
          "entity_name": "Binance Cold Storage",
          "category": "exchange",
          "addresses": ["bc1q...", "1P5Z..."],
          "verified": true
        }
        ```
    *   Un script Python qui interroge l'API gratuite de **mempool.space** (`/api/mempool/recent` ou le polling des adresses cibles) pour checker les flux en temps réel.
    *   Stockage des logs d'alertes dans un fichier CSV ou une mini base SQLite locale.
2.  **Phase 2 : Évolution propre**
    *   Quand le JSON montrera ses limites (trop d'adresses, requêtes lentes), bascul
