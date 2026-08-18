# Archives — Setups du 17/08/2026

Rien n'est supprimé, tout est conservé (loi de la maison).
Ces fichiers sont des **étapes de construction** du champion, pas des stratégies concurrentes.
Le champion actif est le **Setup D** (scellé via `Index_Maison/strategie/CHAMPION_ACTIF` = `5a0a6797`).

| Fichier | Rôle |
|---|---|
| `...BAK_avant_setupA_20260817-101453` | État AVANT le Setup A — avec garde-fous (price_stasis + revenge TTL) |
| `...BAK_avant_setupC_20260817-101453` | État AVANT le Setup C — version allégée (garde-fous retirés) |
| `...BAK_setupC_fix_last_loss_20260817` | Setup C + fix last-loss (revenge TTL) |

## Règle d'or

- **Base officielle = Setup D uniquement** (le champion actif).
- Toute variation = **variable au lancement** (ex. `FLUID_EXIT_ENABLED`), jamais de recopie du moteur.
- Le champion est scellé : `GO_VORTEX_V2.sh` refuse de lancer si le md5 ne correspond plus à `CHAMPION_ACTIF`.
