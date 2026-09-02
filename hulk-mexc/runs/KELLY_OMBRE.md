# Kelly ombre — 2026-09-02 07:15:07

- **win_rate** : 55.81% (24/43 wins)
- **n** : 43 trades clos
- **avg_win** : 0.3594$
- **avg_loss** : 0.7115$
- **b** : 0.5051
- **kelly_plein** : -0.3167
- **kelly_1_4** : 0.0000
- **mise_recommandee** : 0.0$ (sur capital de 20.0$)
- **justesse_cortana** : 51.6%
- **motif** : win_rate < 50% ou Kelly ≤ 0 — pas de sizing adaptatif tant que la preuve n'est pas là

## AVIS
Le Kelly calculé est de 0.0000 (soit 0.0$ par trade). En mode actif,
cela ajusterait dynamiquement l'exposition au risque. Cependant, le moteur reste en mode
OMBRE pur par prudence de supervision.

## Règle
« mode ombre — rien d'appliqué. On passe à l'application quand : win_rate ≥ 50% sur ≥ 20
trades ET justesse Cortana ≥ 50% (validation humaine). »
