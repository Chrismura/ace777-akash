# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=26.4 | vs_planned_min=+4293.6 | timing=early_stop`

- Généré : `2026-08-20T14:32:55Z`
- Fenêtre depuis : `2026-08-20T14:06:28Z`
- Fin process : `2026-08-20T14:32:50Z`
- Meta start/end : `2026-08-20T14:06:28Z` → `2026-08-23T14:06:28Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=26.4 | vs_planned_min=+4293.6 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (1517) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 1517 | no_trigger / stale duo |
| E-SPREAD | 1065 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=12 pnl=-3.8409 exits={'4.79983046': 1, '4.78911490': 1, '3.19818260': 1, '3.88234371': 1, '3.88276013': 1, '2.38897818': 1}
- BETA : fills=18 pnl=+0.2532 exits={'0.79188264': 1, '0.39030314': 1, '0.39046634': 1, '0.39048429': 1, '0.39045926': 1, '0.39057350': 1}
- **TOTAL** : -3.5877

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-20T14:32:44Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-20T14:32:50Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T14:32:44Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-20T14:32:50Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
