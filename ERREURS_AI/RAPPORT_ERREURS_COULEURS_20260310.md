# Rapport d'erreurs — Couleurs cycles (10 mars 2026)

## Contexte
Demande : toutes les couleurs sur les cycles, comme dans le setup.

## Erreurs commises

### 1. Couleur unique par ligne
- **Fait** : Une seule couleur par ligne (ex: toute la ligne en jaune pour SKIP)
- **Attendu** : Plusieurs couleurs par ligne (Cycle en bleu, SKIP/ORDER en jaune/vert, détails en cyan, etc.)

### 2. Une seule ligne colorée visible
- **Symptôme** : L'utilisateur ne voyait qu'une ligne jaune
- **Cause probable** : Format monochrome par type de message au lieu de segments colorés par élément

### 3. Correction apportée
- Chaque ligne a maintenant plusieurs segments colorés :
  - `Cycle N` → bleu
  - `SKIP` / `ORDER` / `OBSERVE` → jaune / vert / cyan
  - Détails (après `|`) → cyan
  - Préfixe `[BETA_X5]` → jaune, `[ALPHA_X13_BURST13]` → cyan
