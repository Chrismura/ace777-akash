# RAPPORT ERREURS SESSION — ACE_RADAR_ALIGNED_V4_60M

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=timer_normal | stop_class=normal_timer_window | ran_min=60.1 | vs_planned_min=-0.1 | timing=near_timer`

- Généré : `2026-09-02T01:04:32Z`
- Fenêtre depuis : `2026-09-02T00:04:23Z`
- Fin process : `2026-09-02T01:04:31Z`
- Meta start/end : `2026-09-02T00:04:23Z` → `2026-09-02T01:04:23Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=timer_normal | stop_class=normal_timer_window | ran_min=60.1 | vs_planned_min=-0.1 | timing=near_timer**
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

- ALPHA : fills=5 gross=-3.3131 fees=+4.9776 net=-8.2907 exits={'timeout': 2, 'trailing_stop': 1, 'stop_loss': 1, 'kill_switch': 1}
- BETA : fills=9 gross=-5.8093 fees=+4.7056 net=-10.5149 exits={'stop_loss': 5, 'timeout': 3, 'trailing_stop': 1}
- **TOTAL** : gross=-9.1224 fees=+9.6832 net=-18.8056

## Derniers PROCESS_DIE / EXIT

- `[BETA_X5] 2026-09-02T01:04:27Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `[ALPHA_X13_BURST13] 2026-09-02T01:04:31Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-02T01:04:27Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-02T01:04:31Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`

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
