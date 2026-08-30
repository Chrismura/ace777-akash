# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=90.8 | vs_planned_min=+90.7 | timing=early_stop`

- Généré : `2026-08-21T13:34:11Z`
- Fenêtre depuis : `2026-08-21T12:03:20Z`
- Fin process : `2026-08-21T13:34:06Z`
- Meta start/end : `2026-08-21T12:03:20Z` → `2026-08-21T15:04:45Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=90.8 | vs_planned_min=+90.7 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (1945) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 1945 | no_trigger / stale duo |
| E-SPREAD | 1551 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=11 pnl=+8.5782 exits={'7.76445875': 1, '8.31375138': 1, '3.19495154': 1, '3.87625210': 1, '1.59911573': 1, '1.59621710': 1}
- BETA : fills=21 pnl=-9.9141 exits={'0.39493990': 2, '0.79144390': 1, '0.39991536': 1, '0.39962052': 1, '0.64555680': 1, '0.39954616': 1}
- **TOTAL** : -1.3360

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-21T13:33:50Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-21T13:34:06Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-21T13:33:50Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-21T13:34:06Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
