# MONTE CARLO ACE — Test de résistance — 2026-08-18

**Méthode** : doctrine S9 + signets (Lummox/antpalkin = méthode, 0x_Punisher = leçon P(fill)). Lecture seule, rien ne touche le moteur.
**Paramètres** : 5000 simulations · capital $20.00 · seuil de ruine drawdown ≥ 25 % (S9) · graine 42

## 1. Le rêve vs la réalité (leçon 0x_Punisher)

> *« Real EV = EV modélisé × P(fill). Un backtest qui suppose que tu es rempli à chaque fois n'est pas un backtest, c'est un vœu pieux. »* — @0x_Punisher

| Unité | Fills | Skips | Cycles | **P(fill) réel** | PnL moyen / trade | PnL moyen / cycle réel |
|---|---|---|---|---|---|---|
| BETA | 4308 | 41712 | 46051 | **9.35 %** | +0.0067 $ | +0.0006 $ |
| ALPHA | 1147 | 36627 | 37967 | **3.02 %** | +0.1781 $ | +0.0054 $ |
| **TOTAL** | 5455 | 78339 | 84018 | **6.49 %** | +0.0427 $ | **+0.0028 $** |

**Lecture** : ACE n'est rempli qu'à **6.5 %** des cycles. Le PnL moyen par trade (+0.0427 $) n'est pas le vrai rendement : par cycle réel, c'est **+0.0028 $**.

## 2. Monte Carlo — 5,000 chemins mélangés

> Les marchés n'arrivent jamais deux fois dans le même ordre. On mélange l'ordre des trades réels et on regarde ce qui survit.

| Métrique | Valeur | Lecture |
|---|---|---|
| Trades réels analysés | 5455 | 40.3 % de trades gagnants |
| Somme des PnL réels | +233.12 $ | invariant : mélanger l'ordre ne change pas le total |
| Max drawdown **médian** (50 % des mondes) | 39.8 % | le creux typique |
| Max drawdown **pire cas** (5 % des mondes) | 103.9 % | le creux rare |
| Pire drawdown observé | 352.4 % | le pire de tous les 5000 mondes |
| **Probabilité de ruine** (DD ≥ 25 %) | **80.6 %** | 80.6 % des 5000 mondes meurent |
| Probabilité de finir en vert | 100.0 % | 100.0 % des mondes finissent + |

## 3. Verdict

🔴 **À RISQUE** — la ruine est fréquente dans les mondes mélangés. Le champion dépend de l'ordre des trades.

✅ La somme des PnL réels est **positive** (+233.12 $) : le champion gagne dans l'ordre vécu. La question est la profondeur des creux en cours de route.

## 4. Les données

| Unité | Fichier | Fills |
|---|---|---|
| BETA | `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | 4308 |
| ALPHA | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv` | 1147 |
