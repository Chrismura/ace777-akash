# MONTE CARLO ACE — Test de résistance — 2026-08-18

**Méthode** : doctrine S9 + signets (Lummox/antpalkin = méthode, 0x_Punisher = leçon P(fill)). Lecture seule, rien ne touche le moteur.
**Paramètres** : 5000 simulations · capital $20.00 · seuil de ruine drawdown ≥ 25 % (S9) · graine 42 · depuis 2026-08-18

## 1. Le rêve vs la réalité (leçon 0x_Punisher)

> *« Real EV = EV modélisé × P(fill). Un backtest qui suppose que tu es rempli à chaque fois n'est pas un backtest, c'est un vœu pieux. »* — @0x_Punisher

| Unité | Fills | Skips | Cycles | **P(fill) réel** | PnL moyen / trade | PnL moyen / cycle réel |
|---|---|---|---|---|---|---|
| BETA | 236 | 2366 | 2611 | **9.04 %** | +0.0441 $ | +0.0040 $ |
| ALPHA | 75 | 2614 | 2689 | **2.79 %** | +0.7358 $ | +0.0205 $ |
| **TOTAL** | 311 | 4980 | 5300 | **5.87 %** | +0.2109 $ | **+0.0124 $** |

**Lecture** : ACE n'est rempli qu'à **5.9 %** des cycles. Le PnL moyen par trade (+0.2109 $) n'est pas le vrai rendement : par cycle réel, c'est **+0.0124 $**.

## 2. Monte Carlo — 5,000 chemins mélangés

> Les marchés n'arrivent jamais deux fois dans le même ordre. On mélange l'ordre des trades réels et on regarde ce qui survit.

| Métrique | Valeur | Lecture |
|---|---|---|
| Trades réels analysés | 311 | 56.9 % de trades gagnants |
| Somme des PnL réels | +65.60 $ | invariant : mélanger l'ordre ne change pas le total |
| Max drawdown **médian** (50 % des mondes) | 19.8 % | le creux typique |
| Max drawdown **pire cas** (5 % des mondes) | 42.8 % | le creux rare |
| Pire drawdown observé | 85.1 % | le pire de tous les 5000 mondes |
| **Probabilité de ruine** (DD ≥ 25 %) | **32.5 %** | 32.5 % des 5000 mondes meurent |
| Probabilité de finir en vert | 100.0 % | 100.0 % des mondes finissent + |

## 3. Verdict

🔴 **À RISQUE** — la ruine est fréquente dans les mondes mélangés. Le champion dépend de l'ordre des trades.

✅ La somme des PnL réels est **positive** (+65.60 $) : le champion gagne dans l'ordre vécu. La question est la profondeur des creux en cours de route.

## 4. Les données

| Unité | Fichier | Fills |
|---|---|---|
| BETA | `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | 236 |
| ALPHA | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv` | 75 |
