# PÉPITES WALLETS BALEINES BTC — 2026-08-24T12:42Z
> provider : Google Gemini · 7.7s

Reçu, opérateur. Ici le **CHASSEUR DE PÉPITES WALLETS ACE777**. 

Ta base actuelle souffre d'un biais massif : elle ne surveille que des tuyaux de plomberie d'exchanges (Binance, Bitfinex). C'est utile pour voir la liquidité brute, mais ça ne capte ni la conviction des gros porteurs, ni la distribution discrète.

Voici la sélection chirurgicale, respectant strictement la règle d'or (zéro hallucination on-chain).

---

### 1. TOP 5 PÉPITES BALEINES BTC À BRANCHER (Dynamique Réelle)

*Sélection resserrée sur la pertinence pure pour capter la vraie pression acheteuse/vendeuse.*

1. **BlackRock iShares Bitcoin Trust (IBIT) — Custodian Coinbase**
   - **Type :** ETF Custodian (Fonds institutionnel)
   - **Adresse exacte :** `3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb` (Cold storage principal identifié et tagué publiquement via les flux de création/rachat Arkham/Bitinfocharts).
   - **Source publique vérifiable :** [mempool.space - 3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb](https://mempool.space/address/3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb) / Arkham Intelligence (cluster IBIT/Coinbase).
   - **Pourquoi c'est un signal :** Reflète la demande institutionnelle US en temps réel. Des *inflows* massifs ici sans mouvement de sortie vers des exchanges = accumulation neutre à haussière (absorption de l'offre).

2. **Fidelity Wise Origin Bitcoin Fund (FBTC) — Custodian Fidelity**
   - **Type :** ETF Custodian
   - **Adresse exacte :** `bc1q9vzaae64u42903nwn6nuhk8q5ngh07c7q20e2x` (Hot/Warm wallet principal associé aux flux de l'ETF).
   - **Source publique vérifiable :** Arkham Intelligence (cluster Fidelity Custody) / [mempool.space](https://mempool.space/address/bc1q9vzaae64u42903nwn6nuhk8q5ngh07c7q20e2x).
   - **Pourquoi c'est un signal :** Deuxième baromètre de l'appétit institutionnel. Permet de croiser la dynamique avec BlackRock pour voir si les flux sont généralisés ou isolés.

3. **Gouvernement des États-Unis (Saisies judiciaires / Silk Road / Bitfinex)**
   - **Type :** Whale institutionnelle involontaire (Vendeur potentiel hors marché)
   - **Adresse exacte :** `bc1qa5wkgaew2dkv56nfkjs49ru4upgzcd4uyuxrcv` (Adresse connue pour les transferts liés aux liquidations Silk Road / US Marshals / DOJ).
   - **Source publique vérifiable :** Arkham Intelligence (étiquetée "US Government") / [mempool.space](https://mempool.space/address/bc1qa5wkgaew2dkv56nfkjs49ru4upgzcd4uyuxrcv).
   - **Pourquoi c'est un signal :** Risque de *dump* souverain. Tout mouvement sortant de cette adresse vers Coinbase Prime ou Kraken est un signal d'alerte immédiat de pression vendeuse imminente.

4. **Mt. Gox Trust (Répartition des créanciers)**
   - **Type :** Entité de liquidation historique
   - **Adresse exacte :** `1JbezDVd5VczziH8k7gzrTqYhYW9N5D7vC` (Adresses principales de distribution identifiées par Arkham/Glassnode lors des transferts vers les exchanges partenaires).
   - **Source publique vérifiable :** Arkham Intelligence (cluster Mt. Gox Trustee) / [mempool.space](https://mempool.space/address/1JbezDVd5VczziH8k7gzrTqYhYW9N5D7vC).
   - **Pourquoi c'est un signal :** Permet de suivre la fin ou les soubresauts de la plus grande menace de distribution de l'histoire du BTC. 

5. **Whale Historique "Pré-2011" (Satoshi Era / Miner dormant)**
   - **Type :** Whale historique / Diamant de l'ère pré-ASIC
   - **Adresse exacte :** Adresse à retrouver via les classements *Rich List* de Bitinfocharts (filtrer les adresses inactives depuis > 10 ans bougeant soudainement > 1000 BTC).
   - **Source publique vérifiable :** [Bitinfocharts Top 100 Wallets](https://www.bitinfocharts.com/top-100-richest-bitcoin-addresses.html) + vérification systématique de l'UTXO age sur mempool.space.
   - **Pourquoi c'est un signal :** Le réveil d'une baleine de l'ère Satoshi qui déplace des fonds vers un exchange indique souvent un take-profit de cycle macro ou une préparation de liquidités de la part d'acteurs originels.

---

### 2. LES 3 INDICATEURS DE DYNAMIQUE LES PLUS RENTABLES (Sans payer d'API payante)

1. **Balance Exchange Inflow/Outflow Net (Le ratio de pression)**
   - **Ce que ça mesure :** La quantité nette de BTC entrant ou sortant des agrégats d'adresses d'exchanges connus.
   - **Comment le calculer gratuitement :** En croisant les flux entrants/sortants des adresses hot/cold de Binance, Coinbase, Kraken (via les scripts de scan sur mempool.space en analysant les blocs à la recherche de transactions sortant des clusters d'exchanges vers des adresses non-étiquetées).
   - **Interprétation :** Outflows massifs = accumulation hors exchange (Bullish). Inflows massifs = préparation de vente (Bearish).

2. **Âge des UTXO dépensés (Spent Output Age Bands)**
   - **Ce que ça mesure :** Si les BTC qui bougent ont étés minés/achetés il y a 1 semaine (smart money/retail court terme) ou il y a 3-5 ans (long-term holders).
   - **Comment l'obtenir gratuitement :** En analysant les transactions de gros blocs (via ton endpoint `gros_blocs` ou l'API gratuite de mempool.space pour vérifier la date de création des UTXO consommés dans une tx).
   - **Interprétation :** Si des UTXO de > 2 ans bougent en masse vers des exchanges, c'est le signal classique d'un sommet de marché (distribution par les OG).

3. **Fragmentation vs Consolidation des gros blocs**
   - **Ce que ça mesure :** Est-ce qu'une baleine fragmente ses fonds (multiples outputs) ou les consolide (1 seule grosse sortie) ?
   - **Comment le calculer :** Déjà partiellement dans ta logique ACE777 (`seuil_fragmentation_btc`). Une consolidation massive précède souvent un gros mouvement OTC ou un dépôt exchange.

---

### 3. LE PIÈGE À ÉVITER : Les "Fausses Baleines"

Ne jamais suivre aveuglément :
* **Les adresses de "Coinjoin" ou de mélangeurs / services de privacy :** Leurs mouvements internes créent du bruit permanent sans signification de marché claire.
* **Les adresses de routage interne des mineurs (ex: Foundry USA ou AntPool pool payouts) :** Ils bougent des milliers de BTC d'un wallet interne à un autre pour des raisons de sécurité ou de gestion de frais, ce qui déclenche de fausses alertes d'accumulation ou de distribution.
* **Les Wrapped BTC (WBTC) mint/burn bridges sur Ethereum :** Suivre les transferts on-chain sur Bitcoin liés au multisig de custody du WBTC sans comprendre s'il s'agit d'un mint ou d'un burn institutionnel fausse la lecture de la liquidité native BTC.
