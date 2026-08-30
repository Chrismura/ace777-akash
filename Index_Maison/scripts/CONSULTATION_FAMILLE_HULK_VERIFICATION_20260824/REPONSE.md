# VÉRIF CODEUR — PASSAGE HULK AU RÉEL — 2026-08-24T17:06Z
> provider : Google Gemini · 8.6s

### A. VERDICT PAR CHANTIER

#### 1. Tableau Cockpit Hulk
- **Verdict** : À CORRIGER
- **Quoi exactement** : Le calcul de `BAG LIVE` doit explicitement dissocier `seedQty` (quantité initiale figée au démarrage) et `qty` (quantité actuelle après exécution des *partial sells*). Si le tableau fait un simple `qty_actuel - seedQty`, le résultat sera négatif à cause des ventes partielles (ex: cas RWA : 1327 / 5310). Il faut afficher deux colonnes distinctes : `Seed` (quantité d'origine) et `Live` (quantité restante en portefeuille) pour éviter l'effet d'optique d'un "bag qui fond".
- **Risque** : Confusion de Christophe sur l'état réel du capital pendant le live, faussant l'évaluation de la performance brute vs capital investi.

#### 2. Persistance Coupures (`--resume`)
- **Verdict** : À CORRIGER
- **Quoi exactement** : 
  1. *Paires obsolètes* : Si une paire est retirée du fichier de config entre un crash et un `--resume`, le script doit lever une exception ou ignorer proprement la position sans bloquer la boucle principale.
  2. *Double-run (Race Condition)* : Le mécanisme ne vérifie pas l'existence d'un verrou (`lock file` ou PID actif). Si le watchdog relance une instance alors que l'ancienne est bloquée (zombie), double exécution sur le même MEXC real account = double ordres, double risque.
- **Risque** : Corruption de l'état si le fichier JSON est partiellement écrit lors d'une coupure brutale (ajouter une écriture atomique via fichier temporaire + `os.replace`).

#### 3. Cas RWA (Rip Scale-Out & Accumulation)
- **Verdict** : RISQUE / COMPATIBILITÉ STRATÉGIQUE
- **Quoi exactement** : Le mécanisme actuel de vente partielle (25% à +7%) **perd mécaniquement une fraction du bag** si le prix ne redescend pas pour déclencher le rachat (*re-entry*). La promesse « *sans jamais perdre les bags accumulés* » est mathématiquement fausse si la baisse attendue ne se produit pas, car on se retrouve avec moins de tokens (même si on a du cash en plus).
- **Risque** : Asymétrie en marché haussier (bull run) : Hulk vend ses morceaux de bags, le prix continue de monter, Hulk rate la hausse et ne peut racheter qu'plus haut (ou pas du tout). Pour du réel, il faut impérativement un mécanisme de *Trailing Take Profit* ou un ré-achat dynamique si le prix repart à la hausse.

#### 4. Observateur Murs (`observer_murs.py`)
- **Verdict** : OK (mais brut)
- **Quoi exactement** : Le rapport agrège 35k+ mesures et identifie les spoofs/drops. Cependant, les données ne sont **pas injectées en temps réel** dans la décision de Hulk (`paper_diprip.py`). Tant que le JSON/MD généré reste un rapport statique lu par l'humain, il est inutile pour un bot en production.
- **Risque** : Fausse impression de sécurité. Avoir des stats sur XRP ou RWA ne sert à rien si Hulk trade aveuglément sans consommer `murs_observations.json` pour filtrer ses ordres (ex: interdire d'acheter si le taux de spoofing dépasse 5% sur la paire).

---

### B. LES 3 PIÈgES LES PLUS DANGEREUX POUR LE PASSAGE AU RÉEL

1. **La divergence d'arrondi et de taille minimale de lot (MEXC precision limits)** : En *paper*, le simulateur accepte des fractions arbitraires de tokens. En *réel*, l'API MEXC rejettera les ordres si la quantité ou le montant notionnel (min. souvent 5$ ou 10$) ne respecte pas les filtres de la paire (`stepSize`, `minQty`, `minNotional`). 
   *Conséquence* : Blocage silencieux des ordres de rachat (*re-entry*) ou des ventes partielles, désynchronisant l'état du bot et l'exchange.
2. **Le piège de la liquidité réelle vs Murs de façade (Spoofing)** : Les chiffres de l'observateur montrent un taux de spoofing non négligeable (jusqu'à 6.9% sur PYTH). En mode réel, un faux mur BID qui s'effondre de 15%/s (1507 occurrences détectées) pendant que Hulk tente d'acheter ou de couper sa position entraîne un glissement de prix (*slippage*) destructeur.
3. **La gestion des fonds (`walletReelCash`) et des commissions (Frais Taker/Maker)** : En *paper*, les frais sont souvent simulés à plat ou ignorés. En *réel*, chaque aller-retour (surtout avec les *partial sells* fréquents) grignote le capital via les frais de taker. Si le cash réel disponible est mal calculé en cas de pertes en cascade, le bot va tenter d'ouvrir des positions avec un solde insuffisant et lever des erreurs API non gérées.

---

### C. CE QUI MANQUE AVANT LE PASSAGE RÉEL (Checklist)

- [ ] **Contrôle d'unicité (Lockfile)** : Empêcher strictement le lancement de deux instances du bot sur le même compte/paire.
- [ ] **Écriture atomique des états** : Sécuriser `*_state.json` via écriture `.tmp` puis `os.replace()` pour éviter les corruptions de données en cas coupure d'électricité.
- [ ] **Filtre API MEXC (Lot Size / Min Notional)** : Valider que chaque quantité calculée par Hulk respecte les contraintes de l'exchange avant l'appel `create_order`.
- [ ] **Consommation des Murs** : Injecter un check rapide de l'observateur dans Hulk : interdire l'achat si un mur subit un drop ≥ 15%/s ou un taux de spoof > seuil critique.
- [ ] **Kill-switch global de secours** : Un script externe simple (ou une commande Telegram/CLI) capable d'annuler tous les ordres ouverts et de vendre au marché l'intégralité des positions en 1 clic.

---

### D. PLAN 3 JOURS : VALIDATION PENDANT L'OBSERVATION (PAPER / PRÉ-RÉEL)

#### Jour 1 : Stabilité de l'État et Persistance
- **Action** : Simuler une coupure franche (kill -9 du processus Hulk) en plein milieu d'un cycle de trade actif.
- **À valider** : L'utilisation de `--resume` restaure-t-elle 100% des positions sans doublon d'ordre sur MEXC ? Le fichier d'état JSON est-il intègre ?

#### Jour 2 : Cohérence des Flux Financiers & PnL
- **Action** : Auditer les *partial sells* (comme le cas RWA) sur 24h.
- **À valider** : Comparer le `BAG LIVE` affiché dans le cockpit avec le solde réel retourné par l'API de l'exchange. Vérifier que les frais réels n'annulent pas le `comboPnl`.

#### Jour 3 : Stress Test des Signaux & Murs
- **Action** : Croiser les alertes de l'observateur de murs (`murs_observations.json`) avec les déclenchements de trades réels de Hulk.
- **À valider** : Est-ce que Hulk évite les paires à fort taux de spoofing (> 5%) ? Le bot réagit-il correctement aux chutes brutales de murs (drops ≥ 15%/s) sans bloquer la boucle d'exécution ?
