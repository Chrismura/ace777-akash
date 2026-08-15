# AVIS gemini-direct (provider Google Gemini)

Reçu, superviseur Buffy. La flottille a apparemment le nez creux : Christophe a totalement raison, les grosses baleines splittent leurs flux pour noyer le poisson dans la *mempool*. 

Voici nos réponses directes, factuelles et calibrées pour actionner `mempool.space` sans frais.

---

### 1) Entités prioritaires et pourquoi les suivre (avec exemples)

Pour traquer le vrai flux sans se noyer dans le bruit, il faut cartographier les poids lourds :

*   **Exchanges Majeurs (Hot/Cold Wallets)** :
    *   *Binance (Cold/Hot)* : Le plus gros volume de liquidité spot. Une entrée massive = pression vendeuse imminente ; une sortie = assèchement du carnet d'ordres.
    *   *Coinbase Prime / Custody* : Le cœur institutionnel US. Indispensable pour capter le rééquilibrage institutionnel.
    *   *Bitfinex / OKX / Kraken* : Historiquement liés aux mouvements de collatéral produits par les gros fonds ou les desks OTC.
*   **ETF Spot (Gardiens de la brique institutionnelle)** :
    *   *BlackRock (iShares - IBIT)* : Le mastodonte. Leurs flux d'entrées/sorties dictent souvent la tendance US de la journée.
    *   *Fidelity (FBTC)* & *Grayscale (GBTC)* : GBTC reste un baromètre de sortie historique, FBTC d'accumulation organique. *(Note : les adresses exactes changent ou sont masquées par les dépositaires comme Coinbase Custody, mais les clusters de transactions de création/rachat sont repérables).*
*   **Gouvernements & Saisies (Les "vendeurs forcés" imprévisibles)** :
    *   *États-Unis (USMS / DOJ)* : Connus pour déplacer périodiquement des milliers de BTC saisis (Silk Road, etc.) vers des exchanges. Impact psychologique et prix immédiat (dump brutal).
    *   *Allemagne / UK* : Même logique, réveil brutal des portefeuilles étatiques.
*   **Trésoreries d'entreprises & Acteurs systémiques** :
    *   *MicroStrategy (Strategy)* : Leurs achats massifs (via des UTXO spécifiques souvent regroupés) marquent les points d'inflexion du cycle.
    *   *Tether Operations* : Leurs réserves et mints/burns se reflètent on-chain par des mouvements de collateral BTC.

> **⚠️ RÈGLE ANTI-HALLUCINATION (Crucial)** : *Ne jamais stocker une adresse d'exchange ou d'ETF sans vérification croisée. Les adresses étiquetées "Binance" ou "BlackRock" sur les blogs changent constamment (roulement des hot/cold wallets). Il faut valider via les tags étiquetés par les explorers communautaires ou les rapports de transparence avant de sceller l'adresse dans la DB.*

---

### 2) Où trouver ces adresses gratuitement et sans clé ?

Pas besoin d'API payante à 500$/mois pour démarrer. Les sources open-source gratuites :

1.  **BitcoinAbuse & BitInfoCharts** : Listes publiques historiques des adresses de ransomwares, hackers, et top 100 wealthiest addresses (souvent étiquetées "Binance cold storage", etc.).
2.  **Arkham Intelligence (Version gratuite / Interface Web)** : Même sans API payante, leur explorateur visuel public permet de copier-coller les adresses mères des entités labellisées (ETF, exchanges, gouvernements).
3.  **GitHub & Repos Open-Source (ex: *bitcoin-whale-tracker* ou listes de clusters d'addresses)** : Des développeurs partagent régulièrement des listes JSON d'adresses d'exchanges validées. (À croiser systématiquement).
4.  **Exploration directe via mempool.space** : En partant d'une transaction connue d'un exchange (ex: une sortie documentée de Coinbase), on remonte les entrées/sorties (clustering heuristique basique : co-spending inputs).

---

### 3) Méthode de détection et traque de la fragmentation

*   **Entrée vs Sortie vs Interne** :
    *   *Entrée Exchange (Vente potentielle)* : Une adresse connue (ou un cluster non-identifié) envoie des fonds vers une adresse **connue et étiquetée** d'un exchange.
    *   *Sortie Exchange (Accumulation)* : Un exchange envoie des fonds vers une adresse externe (souvent multi-sig ou fraîchement créée).
    *   *Transfert interne* : Mouvement entre deux hot/cold wallets de la même entité (bruit à filtrer).
*   **Détecter la fragmentation (Le "Syndrome de la pieuvre")** :
    Les baleines malines n'envoient plus 1 000 BTC d'un coup. Elles font **10 à 50 transactions de 20 à 100 BTC** en l'espace de quelques blocs (1 à 2 heures).
    *   *Algorithme simple* : Au lieu de chercher *une* grosse tx, surveiller les **agrégations par bloc** sur `mempool.space/api/mempool/recent`. 
    *   Si un même cluster (ou des adresses au comportement similaire/nouvelles créées en même temps) émet 20 transferts distincts vers une même entité ou de multiples adresses relais dans une fenêtre de 3 blocs, lever une alerte **"Fragmentation détectée / Whale Stealth Move"**.

---

### 4) Le seuil idéal en 2026

*   **Proposition de Christophe : 100 M$**
*   **Notre avis de flottille** : 100 M$ est un excellent filtre anti-bruit pour 2026 (avec un BTC oscillant potentiellement haut, 100 M$ représente grosso modo 1 000 à 1 500 BTC). 
*   **Recommandation double seuil** :
    *   **Seuil absolu (Gros bloc unique)** : **1 000 BTC** (ou équivalent ~70-100 M$ selon le cours).
    *   **Seuil composite (Fragmentation)** : Cumul de **> 500 BTC** émis par la même source/cluster en moins de 3 blocs. C'est là qu'on attrape les "malins".

---

### 5) Architecture : Comment démarrer et faire évoluer ?

*   **Pour démarrer (Jour 1)** :
    *   Une base locale **JSON ou SQLite** suffit largement. 
    *   Structure simple : 
        `table_addresses (addr TEXT, entity_name TEXT, category TEXT, verified BOOLEAN)`
        `table_alerts (txid TEXT, timestamp INT, amount_btc FLOAT, source TEXT, dest TEXT, type TEXT)`
    *   Un script Python minimaliste qui interroge `mempool.space` via ses endpoints publics (gratuit, pas de clé) sur une liste watch-list d'adresses toutes les X minutes, ou qui écoute les blocs récents.
*   **Pour faire évoluer proprement (Étape 2)** :
    *   Migrer de SQLite vers **PostgreSQL** pour gérer la volumétrie des transactions et faire des requêtes de clustering plus fines.
    *   Ajouter un moteur de notification (Webhook pour le cockpit, bot Telegram/Discord pour ADA).
    *   Implémenter un début de **clustering heuristique** (regroupement automatique d'adresses basées sur les entrées multi-sig communes) pour découvrir *soi-même* les nouvelles adresses des baleines sans dépendre de listes figées.

La flottille a le cap. On commence à scripter les premiers tests sur SQLite. Prêts pour les ordres du cockpit, Buffy.
