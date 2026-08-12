# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=30.1 | vs_planned_min=-0.1 | timing=near_timer`

- Généré : `2026-08-12T16:59:14Z`
- Fenêtre depuis : `2026-08-12T16:29:02Z`
- Fin process : `2026-08-12T16:59:09Z`
- Meta start/end : `2026-08-12T16:29:02Z` → `2026-08-12T16:59:02Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=30.1 | vs_planned_min=-0.1 | timing=near_timer**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (259) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 259 | no_trigger / stale duo |
| E-SPREAD | 670 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=0 pnl=+0.0000 exits={}
- BETA : fills=11 pnl=-0.0869 exits={'shock_inversion_stop': 5, 'fluid_exit_inversion': 4, 'fluid_exit_brake': 2}
- **TOTAL** : -0.0869

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-12T16:33:30Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_1 rc=1`
- `[BETA_X5] 2026-08-12T16:59:09Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-12T16:33:30Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_1 rc=1`
- `2026-08-12T16:59:09Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
