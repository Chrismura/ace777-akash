# Kelly ombre — 2026-08-17 07:15:04

- **win_rate** : 100.00% (2/2 wins)
- **n** : 2 trades clos
- **avg_win** : 0.2368$
- **avg_loss** : 0.0000$
- **b** : 0.0000
- **kelly_plein** : 0.0000
- **kelly_1_4** : 0.0000
- **mise_recommandee** : 0.0$ (sur capital de 20.0$)
- **justesse_cortana** : 46.2%
- **motif** : win_rate < 50% ou Kelly ≤ 0 — pas de sizing adaptatif tant que la preuve n'est pas là — pénalité petit échantillon (n=2 < 20)

## AVIS
Le Kelly calculé est de 0.0000 (soit 0.0$ par trade). En mode actif,
cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode
OMBRE pur par prudence de supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20
trades ET justesse Cortana ≥ 50% (validation humaine). »
