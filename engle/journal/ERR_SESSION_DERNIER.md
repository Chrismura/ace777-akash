# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=463.1 | vs_planned_min=+5296.9 | timing=early_stop`

- Généré : `2026-08-19T20:57:10Z`
- Fenêtre depuis : `2026-08-19T13:13:56Z`
- Fin process : `2026-08-19T20:57:04Z`
- Meta start/end : `2026-08-19T13:13:56Z` → `2026-08-23T13:13:56Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=463.1 | vs_planned_min=+5296.9 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (1694) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 1694 | no_trigger / stale duo |
| E-SPREAD | 1339 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=119 pnl=-44.4402 exits={'shock_inversion_stop': 112, 'shock_exit_10bps': 4, 'trailing_stop': 3}
- BETA : fills=255 pnl=-4.2185 exits={'shock_inversion_stop': 235, 'trailing_stop': 12, 'shock_exit_10bps': 8}
- **TOTAL** : -48.6587

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-19T20:57:00Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-19T20:57:04Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-19T20:57:00Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-19T20:57:04Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
