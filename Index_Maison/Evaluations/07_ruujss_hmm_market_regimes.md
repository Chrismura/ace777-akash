# Éval #7 — @RuujSs « Factor investing + HMM régimes »

- **Date :** 2026-07-28
- **Compte :** [@RuujSs](https://x.com/RuujSs)
- **Post :** *Factor investing works until the regime changes* + framework HMM pour détecter les régimes et allouer dynamiquement au facteur « historiquement meilleur » dans chaque régime.
- **Famille de sources :** litterature / tutos connus (ex. MDPI 2020 *Regime-Switching Factor Investing with HMM* ; Medium Matthew Wang / DataDave ; repos GitHub factor-rotation) — packaging Twitter « Bookmark this! », pas une invention 2026.

## Analyse classique + lecture

| | |
|--|--|
| Idée centrale | Les facteurs (value, momentum, …) **marchent par épisodes** ; un modèle fixe casse quand le « temps » change. |
| HMM | États **cachés** (régimes) ; on voit seulement des **empreintes** (retours, vol, spreads…). |
| Claim | Rotation dynamique > n’importe quel facteur **statique** — souvent vrai *en backtest* si walk-forward propre. |
| Non-claim | Ce n’est **pas** prédire le prochain tick ; c’est classer le climat. |

### Vulgarisé
1. Le marché a quelques « météos » (calme haussier, panique, range…).  
2. Tu ne vois pas l’étiquette ; tu vois pluie/vent (vol, DD, returns).  
3. HMM = machine qui estime *dans quelle météo on est* + chances de rester / changer.  
4. Ensuite tu choisis la strat/facteur qui a *souvent* bien marché **dans cette météo**.  

→ Aligné avec Index **A#6** (range vs tendance) — version stats plus riche, pas magique.

### Pièges (à coller sur le post)
| Piège | Pourquoi |
|-------|----------|
| Look-ahead / labels | Les états HMM sont des numéros ; les renommer « bull/bear » *après* coup biaise. |
| Overfit | Trop d’états / trop de features → joli backtest, merde live. |
| Lag | Le régime se détecte **souvent en retard** (empreintes après le crash). |
| Frais / churn | Rotation facteurs = turnover. |
| Equity ≠ crypto | Facteurs Fama-French / SPX ≠ panier alts ACE/Hulk. |
| « Higher Sharpe » tweet | Sans période OOS, coûts, et protocole walk-forward → **méfiance**. |

## Pour ACE / Index / swarm

| Prendre | Laisser |
|---------|---------|
| Idée **régime → adapter le book** (pas prédire le prix) | Brancher un HMM 3-états sur le champion ACE demain |
| Empreintes = vol, DD, returns, spreads — close de A1–A6 + B | Croire « meilleur que tout facteur statique » sans retest crypto paper |
| Soft gate : régime stress → réduire size / frein Hulk | Copier rotation Value↔Growth actions US |

**Piste Index :** C#17 candidate = *score régime (HMM ou proxy simple)* branché sur A#6 — d’abord proxy MA/vol/DD, HMM plus tard si paper prouve.

## Décision

- **VRAI (cadre)** — facteurs régime-dépendants + HMM = boîte à outils **sérieuse**, ancienne.  
- **SEMI** sur le marketing « delivered higher risk-adjusted returns » (étude OOS limitée / equity).  
- **Utile** pour le thermomètre maison (météo fond).  
- **Pas** de code ACE / pas de remplacement champion. Watchlist : framework, pas alpha tweet.
