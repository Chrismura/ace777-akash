# AVIS puter-grok(task) (provider Puter Grok (gratuit))

**Réponses factuelles — Flotille mode baleine watch**

### 1. Entités prioritaires à suivre (sans adresses inventées)

**Exchanges (flux entrée/sortie les plus critiques)**
- Binance (hot wallets + cold wallets) : volume le plus élevé du marché. Les entrées massives sur hot wallets signalent souvent des dépôts utilisateurs avant vente.
- Coinbase (Prime + hot wallets) : très utilisé par les institutionnels et ETF. Les sorties vers cold storage sont souvent des signaux d’accumulation.
- Kraken, Bitfinex, OKX, Bybit : volumes secondaires mais bons indicateurs régionaux (Europe, Asie).
- À chaque fois : étiqueter séparément hot (dépôts) et cold (réserves).

**ETF (nouveaux gros joueurs depuis 2024)**
- BlackRock IBIT, Fidelity FBTC, Grayscale GBTC, ARK, Invesco, VanEck : ces entités publient régulièrement leurs adresses ou sont trackées par des analystes on-chain. Les mouvements sont généralement plus lents et plus "propres" que les exchanges.

**Fonds & sociétés cotées**
- MicroStrategy : disclosures via SEC (10-K/10-Q). Ils bougent parfois de très gros volumes en une seule fois.
- Tether (réserves BTC) : mouvements souvent liés à des opérations de stablecoin.

**Gouvernements**
- Adresses saisies par le gouvernement américain (Silk Road, Bitfinex, etc.) : publiées par le DOJ ou le Trésor. Ces adresses font parfois des mouvements très gros et inattendus.
- Allemagne (anciennes saisies Bitfinex) : historique connu de ventes importantes.

**Mineurs & pools**
- Foundry, AntPool, F2Pool, Mara, Riot : les adresses de payout des pools sont relativement stables et les flux peuvent précéder des ventes de mineurs.

**Règle stricte** : toute adresse doit être vérifiée sur au moins deux sources indépendantes avant d’entrer dans la base (anti-hallucination).

### 2. Sources gratuites et fiables (sans API payante)

- **GitHub** : dépôts communautaires "bitcoin-exchange-addresses", "known-btc-addresses", "etf-bitcoin-treasury". Toujours croiser avec une deuxième source.
- **Explorers avec labels** : Blockchair.com (labels assez fiables), mempool.space (labels partiels), BTC.com explorer.
- **Filings officiels** : 
  - MicroStrategy → documents SEC (EDGAR)
  - ETF → rapports trimestriels et parfois pages dédiées "transparency" sur leurs sites
- **Gouvernement US** : publications DOJ / US Marshals / OFAC (listes de seized addresses).
- **Analyses publiques** : articles de recherche (ex. "Binance cold wallet" sur des sites comme Arkham, Nansen, ou analyses indépendantes) → à vérifier manuellement.
- **Twitter/X + archives** : comptes comme @whale_alert, @lookonchain (ils donnent souvent les adresses) → toujours revérifier sur un explorer.

**Méthode recommandée** : créer une colonne `source` + `verification_status` (single / double / triple) dans la base.

### 3. Détection des mouvements significatifs

**Règles de base** :
- **Entrée exchange** (signal vente probable) : transaction vers une adresse étiquetée "hot wallet" ou "deposit" d’un exchange.
- **Sortie exchange** (signal accumulation) : transaction depuis une cold wallet vers une adresse non étiquetée ou vers une autre cold wallet du même exchange.
- **Transfert interne** : mouvement entre deux adresses du même cluster (même exchange ou même entité).

**Fragmentation (baleines qui splitent)** :
- Surveiller les adresses connues + leurs change addresses probables.
- Détecter plusieurs transactions de taille similaire (ex. 50-200 BTC) émises dans un laps de temps court (quelques heures) depuis des adresses qui ont un historique commun (même input dans le passé ou même pattern de change).
- Heuristique simple et gratuite : si 8-15 transactions de ~80-150 BTC arrivent sur un exchange dans les 2-3 heures et proviennent d’adresses qui n’ont jamais interagi avec des exchanges avant, c’est suspect de fragmentation.
- Outil gratuit : utiliser l’API mempool.space sur les adresses surveillées + regarder les transactions récentes via `/api/mempool/recent` et `/api/address/<addr>`.

### 4. Seuil recommandé (2026)

100 M$ (proposition Christophe) est un bon seuil pour les **très gros mouvements** (vraies baleines institutionnelles).  
Cependant, pour une surveillance utile, je recommande **deux seuils** :

- **Seuil principal** : **50-70 M$** (environ 400-600 BTC selon le prix en 2026)
- **Seuil "alerte forte"** : **100 M$+**

Raison : beaucoup de baleines fragmentent maintenant entre 300 et 800 BTC. Un seuil unique à 100 M$ risque de rater des mouvements significatifs. Ajuster dynamiquement tous les 3 mois en fonction du prix du BTC et de la liquidité des exchanges.

### 5. Architecture recommandée

**Phase 1 (démarrage)** : JSON/CSV est largement suffisant.
- Fichier `whales.json` ou CSV avec colonnes : `address`, `label`, `entity`, `type` (exchange_hot, etf, seized, miner…), `source`, `verification_status`, `last_checked`, `notes`.
- Script Python simple qui boucle sur les adresses et interroge l’API mempool.space.

**Évolution propre (quand ça grossit)** :
1. Passer sur **SQLite** (local) → tables : `addresses`, `transactions`, `labels`, `clusters`.
2. Ajouter une table `movements` pour logger les gros flux détectés.
3. Plus tard : PostgreSQL + simple script de clustering basique (common input ownership + change address heuristic).
4. Garder toujours une colonne `manual_verification` car l’automatisation des labels reste faillible.

**Stack minimale conseillée** : Python + `requests` + SQLite + un petit dashboard Streamlit ou Flask pour visualiser les derniers mouvements.

Tu veux que je te sorte un schéma de table SQLite minimal + le squelette du script de scraping mempool.space ?
