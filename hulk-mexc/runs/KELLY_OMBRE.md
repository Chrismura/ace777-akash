# Kelly ombre — 2026-08-18 07:15:03

- **win_rate** : 87.50% (7/8 wins)
- **n** : 8 trades clos
- **avg_win** : 0.2579$
- **avg_loss** : 0.3149$
- **b** : 0.8190
- **kelly_plein** : 0.7224
- **kelly_1_4** : 0.0200
- **mise_recommandee** : 0.4$ (sur capital de 20.0$)
- **justesse_cortana** : 44.3%
- **motif** : Kelly valide en mode ombre — pénalité petit échantillon (n=8 < 20) — plafonné à 2% max

## AVIS
Le Kelly calculé est de 0.0200 (soit 0.4$ par trade). En mode actif,
cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode
OMBRE pur par prudence de supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20
trades ET justesse Cortana ≥ 50% (validation humaine). »
