# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=16.9 | vs_planned_min=+462.9 | timing=early_stop`

- Généré : `2026-08-13T07:18:23Z`
- Fenêtre depuis : `2026-08-13T07:01:25Z`
- Fin process : `2026-08-13T07:18:21Z`
- Meta start/end : `2026-08-13T07:01:25Z` → `2026-08-13T15:01:16Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=16.9 | vs_planned_min=+462.9 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (798) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 798 | no_trigger / stale duo |
| E-SPREAD | 1083 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=5 pnl=+0.4031 exits={'shock_inversion_stop': 3, 'fluid_exit_inversion': 2}
- BETA : fills=10 pnl=+0.0088 exits={'shock_inversion_stop': 8, 'fluid_exit_inversion': 2}
- **TOTAL** : +0.4119

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-13T07:17:11Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_1 rc=1`
- `[BETA_X5] 2026-08-13T07:18:21Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_1 rc=1`
- `2026-08-13T07:17:11Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_1 rc=1`
- `2026-08-13T07:18:21Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_1 rc=1`

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
