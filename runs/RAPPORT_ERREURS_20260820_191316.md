# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=22.6 | vs_planned_min=+217.4 | timing=early_stop`

- Généré : `2026-08-20T19:13:16Z`
- Fenêtre depuis : `2026-08-20T18:50:34Z`
- Fin process : `2026-08-20T19:13:12Z`
- Meta start/end : `2026-08-20T18:50:34Z` → `2026-08-20T22:50:34Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=22.6 | vs_planned_min=+217.4 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (484) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 484 | no_trigger / stale duo |
| E-SPREAD | 592 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=9 pnl=-1.1247 exits={'2.39915318': 2, '4.79444980': 1, '2.39943139': 1, '1.19427758': 1, '1.59829613': 1, '2.39650358': 1}
- BETA : fills=17 pnl=+2.2137 exits={'0.78966714': 1, '1.29410468': 1, '0.38849977': 1, '0.38841883': 1, '0.39416934': 1, '0.39416336': 1}
- **TOTAL** : +1.0889

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-20T19:11:26Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-20T19:13:12Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T19:11:26Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T19:13:12Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
