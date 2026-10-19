# Kelly ombre — 2026-10-19 09:24:51

- **win_rate** : 52.42% (184/351 wins)
- **n** : 351 trades clos
- **avg_win** : 1.0345$
- **avg_loss** : 0.8656$
- **b** : 1.1952
- **kelly_plein** : 0.1261
- **kelly_1_4** : 0.0200
- **mise_recommandee** : 0.4$ (sur capital de 20.0$)
- **justesse_cortana** : 29.2%
- **motif** : Kelly valide en mode ombre — plafonné à 2% max

## AVIS
Le Kelly calculé est de 0.0200 (soit 0.4$ par trade). En mode actif,
cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode
OMBRE pur par prudence de supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20
trades ET justesse Cortana ≥ 50% (validation humaine). »
