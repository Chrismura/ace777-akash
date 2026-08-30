# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=82.9 | vs_planned_min=+157.1 | timing=early_stop`

- Généré : `2026-08-22T12:56:44Z`
- Fenêtre depuis : `2026-08-22T11:33:19Z`
- Fin process : `2026-08-22T12:56:15Z`
- Meta start/end : `2026-08-22T11:33:19Z` → `2026-08-22T15:33:19Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=82.9 | vs_planned_min=+157.1 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (2171) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 2171 | no_trigger / stale duo |
| E-SPREAD | 1645 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=7 pnl=+4.6264 exits={'1.61707029': 1, '0.40106508': 1, '0.80890928': 1, '0.80937145': 1, '0.80382952': 1, '1.30973261': 1}
- BETA : fills=9 pnl=-0.1959 exits={'0.78858547': 1, '0.39489485': 1, '0.39493478': 1, '0.39535974': 1, '0.64270918': 1, '0.39567718': 1}
- **TOTAL** : +4.4305

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-22T12:55:20Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-22T12:56:15Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T12:55:20Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T12:56:15Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
