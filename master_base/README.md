# MASTER BASE ACE777

Ce dossier est la source claire et unique des modeles valides.

## Regle simple (2 temps)

1. **Validation**
   - On prend un modele.
   - On teste.
   - S'il est valide/rentable, il entre ici dans `models/`.

2. **Affinage**
   - On part d'un modele de `master_base/models/`.
   - On fait des variantes dans des dossiers de test (hors master base).
   - Si une variante est validee, on remplace/ajoute proprement ici.

## Structure

- `models/` : scripts validés (point de vérité)
- `pnl/` : résumés consolidés
- `tools/` : outils de synthèse

## Modèles validés (actuels)

- `models/DUO_HARMONIC_5813_V63_VALIDATED_30M.sh`
- `models/DUO_HARMONIC_5813_V63_VALIDATED_6H30.sh`
- `models/MODELE14_ORIGINAL_VALIDATED_30M.sh`

## Important

Les modèles validés de ce dossier sont des points d'entrée stables.
Les anciens dossiers restent en historique, mais la référence opérationnelle est ici.
