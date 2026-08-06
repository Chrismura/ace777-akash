# Audit stack — post chantier 1

Rapport d'audit technique — Cockpit ACE777 :

1. **Cohérence et alimentation des indices** :
Les services répondent (200), mais la cohérence macro-structurelle présente des angles morts critiques. L'utilisation exclusive d'API gratuites sans clé génère une dépendance à des proxys approximatifs : le score global (89) contraste fortement avec un Fear & Greed à 25 (Extreme Fear), créant une divergence comportementale non expliquée par le moteur de décision.

2. **Faiblesses, biais et fragilités** :
- **Absence de redondance** : Sources uniques (Alternative.me, Bitbo, Deribit public) sans fallback en cas de rate-limit ou de panne.
- **Biais de proxy non pondérés** : D28 utilise un proxy rudimentaire pour l'Alt Season ; D33 utilise les strikes à fort OI de Deribit pour simuler le GEX, ignorant le delta réel et le gamma hedging des teneurs de marché.
- **Angles morts institutionnels** : D31 et D32 (ETF ETH/XRP) sont inactifs (`null`) car Bitbo gratuit ne couvre que BTC, appauvrissant l'analyse multi-actifs.

3. **Améliorations prioritaires** :
- **1.** Implémenter un système de *fallback* multi-sources pour les données critiques (ex: croiser OKX et Binance pour le taker ratio et les liquidations).
- **2.** Corriger l'indice de divergence (Score vs Fear & Greed) pour éviter les faux signaux de trading en période de panique de marché.
- **3.** Remplacer ou normaliser le proxy GEX (D33) en intégrant une estimation de la structure par options Binance/Bybit pour s'affranchir de la dépendance exclusive à Deribit.
