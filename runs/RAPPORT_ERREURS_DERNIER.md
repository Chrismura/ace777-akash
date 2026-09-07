# RAPPORT ERREURS SESSION — MASTER_BASE_V8_6_FORTRESS_1H30

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=timer_normal | stop_class=normal_timer_window | ran_min=90.1 | vs_planned_min=-0.1 | timing=near_timer`

- Généré : `2026-09-07T22:30:18Z`
- Fenêtre depuis : `2026-09-07T21:00:13Z`
- Fin process : `2026-09-07T22:30:18Z`
- Meta start/end : `2026-09-07T21:00:13Z` → `2026-09-07T22:30:13Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=timer_normal | stop_class=normal_timer_window | ran_min=90.1 | vs_planned_min=-0.1 | timing=near_timer**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 0 | no_trigger / stale duo |
| E-SPREAD | 0 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=6 gross=-3.0685 fees=+6.4615 net=-9.5300 exits={'exit_fatigue': 3, 'timeout': 3}
- BETA : fills=18 gross=+2.1619 fees=+9.5209 net=-7.3590 exits={'timeout': 9, 'exit_fatigue': 8, 'kill_switch': 1}
- **TOTAL** : gross=-0.9066 fees=+15.9824 net=-16.8890

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-09-07T22:30:17Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-09-07T22:30:18Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-07T22:30:17Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-07T22:30:18Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
