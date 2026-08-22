# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=240.3 | vs_planned_min=-0.3 | timing=near_timer`

- Généré : `2026-08-22T07:32:16Z`
- Fenêtre depuis : `2026-08-22T03:31:42Z`
- Fin process : `2026-08-22T07:32:02Z`
- Meta start/end : `2026-08-22T03:31:42Z` → `2026-08-22T07:31:42Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=240.3 | vs_planned_min=-0.3 | timing=near_timer**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (3533) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 3533 | no_trigger / stale duo |
| E-SPREAD | 2890 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=15 pnl=-8.4095 exits={'0.86933486': 1, '0.80519373': 1, '1.61375029': 1, '0.80624640': 1, '1.61421700': 1, '0.40184664': 1}
- BETA : fills=23 pnl=+5.9114 exits={'0.79336152': 1, '0.39613190': 1, '0.39630629': 1, '0.64066200': 1, '0.39507955': 1, '0.39502159': 1}
- **TOTAL** : -2.4981

## Derniers PROCESS_DIE / EXIT

- `[BETA_X5] 2026-08-22T07:31:47Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `[ALPHA_X13_BURST13] 2026-08-22T07:32:02Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T07:31:47Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-22T07:32:02Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`

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
