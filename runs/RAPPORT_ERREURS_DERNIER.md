# RAPPORT ERREURS SESSION — MASTER_BASE_V8_6_FORTRESS_6H00

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=unknown | ran_min=217.3 | vs_planned_min=+142.7 | timing=early_stop`

- Généré : `2026-09-08T03:13:58Z`
- Fenêtre depuis : `2026-09-07T23:36:39Z`
- Fin process : `2026-09-08T03:13:58Z`
- Meta start/end : `2026-09-07T23:36:39Z` → `2026-09-08T05:36:39Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=unknown | ran_min=217.3 | vs_planned_min=+142.7 | timing=early_stop**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Issues duo (84) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 4 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 84 | no_trigger / stale duo |
| E-SPREAD | 28 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=17 gross=-1.2512 fees=+20.5696 net=-21.8208 exits={'timeout': 12, 'exit_fatigue': 4, 'trailing_stop': 1}
- BETA : fills=46 gross=+0.2709 fees=+23.6631 net=-23.3921 exits={'timeout': 38, 'exit_fatigue': 7, 'stop_loss': 1}
- **TOTAL** : gross=-0.9802 fees=+44.2327 net=-45.2129

## Derniers PROCESS_DIE / EXIT

- `[BETA_X5] 2026-09-08T03:13:55Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `[ALPHA_X13_BURST13] 2026-09-08T03:13:58Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-08T03:13:55Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-09-08T03:13:58Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`

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
