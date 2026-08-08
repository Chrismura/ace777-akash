# Organisation Master Qwen Base

- `master_qwen_base/models/` : modeles Qwen valides.
- `master_qwen_base/pnl/` : index PnL (date, heure, tag, resultat).
- `master_qwen_base/tools/` : outils de verification/audit Qwen.

## Regle de validation

Un modele Qwen enregistre ici doit garder:

- description cycle identique aux runs
- date/heure (`Start UTC`, `End UTC`)
- tag de cycle
- PnL total du cycle
