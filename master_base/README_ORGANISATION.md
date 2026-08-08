# Organisation Master Base

## Regle de rangement

- `master_base/models/`: uniquement les modeles qui fonctionnent.
- `master_base/pnl/`: index PnL par modele (date, heure, tag, resultat).
- `master_base/tools/`: outils utilitaires lies a l'audit/verification.

## Convention obligatoire pour chaque modele

Chaque script enregistre dans `master_base/models/` doit contenir:

- date/heure de debut et de fin du cycle (`Start UTC`, `End UTC`)
- tag du cycle (`MASTER_BASE_...`)
- description cycle identique au run
- PnL total du cycle (ou `A_VERIFIER` si en attente)

## Workflow voulu

1. Un setup tourne en test/variation.
2. Si la plus-value est positive et confirmee, le setup va dans `master_plus_value/`.
3. Si le modele est valide sur plusieurs cycles, il est enregistre dans `master_base/models/`.
4. L'original est conserve pour pouvoir faire des variations ensuite.
