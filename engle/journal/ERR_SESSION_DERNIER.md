# RAPPORT ERREURS SESSION — ${tag}

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=timer_nominal | STOP_REASON.txt=2026-08-12T16:01:34Z reason=timer_nominal duration_sec=14400 | ran_min=29775841.6`

- Généré : `2026-08-12T16:01:36Z`
- Fenêtre depuis : `1970-01-01T00:00:00Z`
- Fin process : `2026-08-12T16:01:36Z`
- Meta start/end : `?` → `?`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=timer_nominal | STOP_REASON.txt=2026-08-12T16:01:34Z reason=timer_nominal duration_sec=14400 | ran_min=29775841.6**
- Signaux watchdog (sémantique ou duo PID) — voir section WATCHDOG.
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 37 | heartbeat / max relaunch |
| E-PROC | 115 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 0 | no_trigger / stale duo |
| E-SPREAD | 0 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=0 pnl=+0.0000 exits={}
- BETA : fills=0 pnl=+0.0000 exits={}
- **TOTAL** : +0.0000

## Derniers PROCESS_DIE / EXIT

- `2026-08-02T00:04:56Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=15804 genesis=15811 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T10:02:45Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=57069 genesis=57077 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T10:02:46Z PROCESS_EXIT unit=BETA_X5 wrapper=56945 genesis=56952 how=exit0 why=clean_end_or_self_exit_0 rc=0`
- `2026-08-02T18:05:37Z PROCESS_EXIT unit=BETA_X5 wrapper=19321 genesis=19328 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T18:05:41Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=19455 genesis=19461 how=signal why=killed_by_signal_15 rc=143`
- `2026-08-02T19:53:42Z PROCESS_EXIT unit=BETA_X5 wrapper=93491 genesis=93496 how=exit0 why=clean_end_or_self_exit_0 rc=0`
- `2026-08-02T19:54:03Z PROCESS_EXIT unit=ALPHA_X13_BURST13 wrapper=93623 genesis=93632 how=exit0 why=clean_end_or_self_exit_0 rc=0`
- `2026-08-12T16:01:36Z PROCESS_EXIT unit=BETA_X5 wrapper=7382 genesis=7389 how=exit0 why=clean_end_or_self_exit_0 rc=0`

## Derniers WATCHDOG

- `2026-07-31T19:01:58Z WATCHDOG_DUO: BETA mort — relance #3/8`
- `2026-07-31T19:02:46Z WATCHDOG_DUO: BETA mort — relance #4/8`
- `2026-07-31T19:03:34Z WATCHDOG_DUO: BETA mort — relance #5/8`
- `2026-07-31T19:04:23Z WATCHDOG_DUO: BETA mort — relance #6/8`
- `2026-07-31T19:05:11Z WATCHDOG_DUO: BETA mort — relance #7/8`
- `2026-07-31T19:05:59Z WATCHDOG_DUO: BETA mort — relance #8/8`
- `2026-07-31T19:06:47Z WATCHDOG_DUO: BETA mort — relance #9/8`
- `2026-07-31T19:06:47Z WATCHDOG_DUO: max BETA → STOP session`

## Échantillon E-STALE (max 8)

- *(aucun)*

## Suite hygiène

1. Si E-WATCHDOG dominant → axe #3 (heartbeat / stale / relaunch), pas un knob storm.
2. Si E-PROC `last_cmd=` clair → bug bash / set -e (comme E11).
3. Si E-STALE seul sans mort → surveiller ; élargir gate seulement avec preuve.
4. Append manuel dans `engle/JOURNAL_ERREURS.md` si nouvel ID (E15…).

---
*scripts/rapport_erreurs_session.py — zéro ordre, zéro genesis.*
