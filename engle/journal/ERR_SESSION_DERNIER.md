# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=27.8 | vs_planned_min=+188.5 | timing=early_stop`

- Généré : `2026-08-20T19:42:08Z`
- Fenêtre depuis : `2026-08-20T19:14:14Z`
- Fin process : `2026-08-20T19:42:04Z`
- Meta start/end : `2026-08-20T19:14:14Z` → `2026-08-20T22:50:33Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=27.8 | vs_planned_min=+188.5 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (433) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 433 | no_trigger / stale duo |
| E-SPREAD | 375 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=15 pnl=+5.2772 exits={'4.79765722': 1, '3.87914030': 1, '2.39562137': 1, '2.39698592': 1, '2.39803329': 1, '3.87847747': 1}
- BETA : fills=21 pnl=-0.9346 exits={'0.79381965': 1, '0.79386458': 1, '0.39415357': 1, '0.38858928': 1, '0.38872650': 1, '0.38871363': 1}
- **TOTAL** : +4.3426

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-20T19:41:51Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-20T19:42:04Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T19:41:51Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T19:42:04Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

## Derniers WATCHDOG

- *(aucun)*

## Échantillon E-STALE (max 8)

- *(aucun)*

## Suite hygiène

1. Si E-WATCHDOG dominant → axe #3 (heartbeat / stale / relaunch), pas un knob storm.
2. Si E-PROC `last_cmd=` clair → bug bash / set -e (comme E11).
3. Si E-STALE seul sans mort → surveiller ; élargir gate seulement avec preuve.
4. Append manuel dans `engle/JOURNAL_ERREURS.md` si nouvel ID (E15…).

---
*scripts/rapport_erreurs_session.py — zéro ordre, zéro genesis.*
