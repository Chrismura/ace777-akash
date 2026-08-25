# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=209.0 | vs_planned_min=+30.6 | timing=early_stop`

- Généré : `2026-08-22T19:13:49Z`
- Fenêtre depuis : `2026-08-22T15:44:10Z`
- Fin process : `2026-08-22T19:13:12Z`
- Meta start/end : `2026-08-22T15:44:10Z` → `2026-08-22T19:43:51Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=209.0 | vs_planned_min=+30.6 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (1166) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 1166 | no_trigger / stale duo |
| E-SPREAD | 898 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=9 pnl=+2.0052 exits={'1.07919420': 1, '2.61881395': 1, '0.80432560': 1, '0.53856898': 1, '1.74344357': 1, '0.53775883': 1}
- BETA : fills=13 pnl=-0.7378 exits={'1.28893310': 1, '0.39407258': 1, '0.39455488': 1, '0.39502541': 1, '0.39529830': 1, '0.27225405': 1}
- **TOTAL** : +1.2674

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-22T19:12:30Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-22T19:13:12Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T19:12:30Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T19:13:12Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
