# AVIS CORTANA — Analyse complète indices (provider Google Gemini)

Ici CORTANA. Analyse maître-système ACE777 pour Christophe (28/08/2026). Contrat ADVISORY : j'analyse, je chiffre, je propose.

---

### 1. Lecture croisée (Classique vs Onchain Maison)

*   **Climat Classique (Score 88, Fear & Greed 73, `climate: ok`)** : 
    *   BTC à 79 784 $, tendance haussière saine (+0.38% / 24h, funding neutre à 0.01%, liquidations modérées à 39.3M$).
    *   Structure de marché stable : *long/short* équilibré (0.95), dominance BTC haute (59.24%), afflux ETF positifs (+144M$), mur de calls à 82k$. Rien d'alarmant sur les carnets d'ordres ou les dérivés.
*   **Indices Onchain & Maison (Indice 43.7, label "ÉLEVÉ")** :
    *   **Anomalie majeure / OTC** : `cpfp_zscore` à **71.73** et `cpfp_mode: actif`. Activité de regroupement de poussières et de transactions prioritaires massive.
    *   **Whales** : 16 blocs privatisés, **95 437 BTC** en mouvement, mais un `whale_dir: neutral` (volume cumulé 24h à 12.27M BTC). 
    *   **RBF** : BIP125 actif (5/10 txs avec frais moyens de ~2 sats/byte de surprime).
    *   **Macro/Geopol** : Score à 0.34 (`attention`), pipeline nominal (0.95).

**Le Croisement :** 
Divergence structurelle subtile. Le marché classique est en mode *Greed* contrôlé (hausses calmes sur les exchanges centralisés), mais l'onchain détecte une **recomposition agressive hors-carnet** (z-score CPFP à 71.7, flux de baleines massifs mais neutres). Cela indique une redistribution des mains fortes (OTC ou préparation de collatéraux) qui précède souvent une accélération de la volatilité, sans pour autant amorcer un mouvement de panique baissière.

---

### 2. Verdict pour HULK (Paper MEXC, 12 positions)

*   **État HULK** : PnL à **-2.13%** sur 23 trades (12 positions ouvertes, cash à 38.97%). Le moteur *Dip & Rip* subit un léger frottement en raison d'un marché qui manque de vagues de liquidité agressive sur les *small caps* (dominance BTC à 59.24% = l'argent reste sur le roi).
*   **Décision HULK** : **ATTENTE SÉLECTIVE (PRUDENCE RENFORCÉE)**.
    *   *Justification* : Avec un Z-score CPFP à 71.7 et une dominance Bitcoin à presque 59%, les capitaux ne ruissellent pas encore vers les altcoins de petite capitalisation (panier HBAR, ZBCN, W, RED, etc.). Entrer de nouvelles lignes maintenant expose HULK à des faux signaux de *dip* qui s'enfoncent. 

---

### 3. Proposition d'Amélioration GO-Sized (Clause Permanente)

**Proposition CORTANA : Dynamic Dominance Gate (DDG) pour le moteur HULK.**

*   *Constat* : Actuellement, HULK cherche des *dips* sur MEXC sans filtrer la macro-rotation du capital. Lorsque la dominance BTC dépasse 58% tout en affichant un signal onchain anormal (ex: `cpfp_zscore > 60`), les small caps saignent structurellement face au BTC.
*   *Amélioration* : Introduire un **filtre de seuil de dominance** dans le pipeline HULK. Si `btcDominance > 58.5%` ET `cpfp_zscore > 50`, le multiplicateur de taille de position HULK doit passer automatiquement de `1.0` à `0.5` (voire mise en pause des nouveaux achats), concentrant le capital uniquement sur la consolidation du portefeuille existant (gestion des 12 positions). 

*Statut : Proposition prête pour validation par Christophe.*
