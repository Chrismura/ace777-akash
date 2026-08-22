# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=240.4 | vs_planned_min=-0.4 | timing=near_timer`

- Généré : `2026-08-22T11:33:08Z`
- Fenêtre depuis : `2026-08-22T07:32:28Z`
- Fin process : `2026-08-22T11:32:51Z`
- Meta start/end : `2026-08-22T07:32:28Z` → `2026-08-22T11:32:28Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=240.4 | vs_planned_min=-0.4 | timing=near_timer**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (2938) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 2938 | no_trigger / stale duo |
| E-SPREAD | 2299 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=14 pnl=-2.3637 exits={'1.07844086': 1, '0.80465216': 1, '0.53837270': 1, '1.30494722': 1, '1.74672581': 1, '0.53693268': 1}
- BETA : fills=22 pnl=+0.0114 exits={'0.55751472': 1, '0.79281766': 1, '0.39580416': 1, '0.39605658': 1, '0.39601715': 1, '0.39583590': 1}
- **TOTAL** : -2.3523

## Derniers PROCESS_DIE / EXIT

- `[ALPHA_X13_BURST13] 2026-08-22T11:32:49Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `[BETA_X5] 2026-08-22T11:32:51Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T11:32:49Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T11:32:51Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

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
