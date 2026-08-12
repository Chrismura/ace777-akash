# RAPPORT ERREURS SESSION — NUAGE_PROD_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=timer_nominal | STOP_REASON.txt=2026-08-03T02:18:13Z reason=timer_nominal duration_sec=28800 | ran_min=1429.2 | vs_planned_min=-1189.2 | timing=late_or_overrun`

- Généré : `2026-08-10T21:21:50Z`
- Fenêtre depuis : `2026-08-01T20:04:48Z`
- Fin process : `2026-08-02T19:54:03Z`
- Meta start/end : `2026-08-01T20:04:48Z` → `2026-08-02T00:04:48Z`
- Watchdog meta : stale=60s max_relaunch=5
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=timer_nominal | STOP_REASON.txt=2026-08-03T02:18:13Z reason=timer_nominal duration_sec=28800 | ran_min=1429.2 | vs_planned_min=-1189.2 | timing=late_or_overrun**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Beaucoup de `tension_stale` (167) = signal latence feed NUAGE (gate 800ms). Sur alpage/WiFi/SIM : possible pic réseau — **à corréler**, pas à conclure seul.
- Issues duo (167) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 10 | mort process / signal |
| E-STALE | 167 | tension/NUAGE age (signal latence) |
| E-DUO | 167 | no_trigger / stale duo |
| E-SPREAD | 279 | spread trop large |
| I-HUNTER | 71 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=5 pnl=-4.8917 exits={'shock_inversion_stop': 3, 'fluid_exit_inversion': 2}
- BETA : fills=100 pnl=-1.5554 exits={'shock_inversion_stop': 69, 'fluid_exit_inversion': 20, 'fluid_exit_brake': 11}
- **TOTAL** : -6.4471

## Derniers PROCESS_DIE / EXIT

- `2026-08-02T00:04:52Z PROCESS_EXIT unit=BETA_X5 wrapper=15680 genesis=15687 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T00:04:56Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=15804 genesis=15811 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T10:02:45Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=57069 genesis=57077 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T10:02:46Z PROCESS_EXIT unit=BETA_X5 wrapper=56945 genesis=56952 how=exit0 why=clean_end_or_self_exit_0 rc=0`
- `2026-08-02T18:05:37Z PROCESS_EXIT unit=BETA_X5 wrapper=19321 genesis=19328 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T18:05:41Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=19455 genesis=19461 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T19:53:42Z PROCESS_EXIT unit=BETA_X5 wrapper=93491 genesis=93496 how=exit0 why=clean_end_or_self_exit_0 rc=0`
- `2026-08-02T19:54:03Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=93623 genesis=93632 how=exit0 why=clean_end_or_self_exit_0 rc=0`

## Derniers WATCHDOG

- *(aucun)*

## Échantillon E-STALE (max 8)

- `[ALPHA_X13_BURST13] 22:06:07 x13 #587 SKIP | tension_stale age=4947ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:06:15 x13 #588 SKIP | tension_stale age=5835ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:09:16 x13 #609 SKIP | tension_stale age=5963ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:09:25 x13 #610 SKIP | tension_stale age=7220ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:14:12 x13 #643 SKIP | tension_stale age=2512ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:14:21 x13 #644 SKIP | tension_stale age=996ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:14:51 x13 #647 SKIP | tension_stale age=3306ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 22:15:00 x13 #648 SKIP | tension_stale age=3660ms>800ms (NUAGE)`

## Suite hygiène

1. Si E-WATCHDOG dominant → axe #3 (heartbeat / stale / relaunch), pas un knob storm.
2. Si E-PROC `last_cmd=` clair → bug bash / set -e (comme E11).
3. Si E-STALE seul sans mort → surveiller ; élargir gate seulement avec preuve.
4. Append manuel dans `engle/JOURNAL_ERREURS.md` si nouvel ID (E15…).

---
*scripts/rapport_erreurs_session.py — zéro ordre, zéro genesis.*
