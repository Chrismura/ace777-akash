# RAPPORT ERREURS SESSION — NUAGE_PROD_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=stop_files_clean_exit | ran_min=3943.2 | vs_planned_min=-3703.2 | timing=late_or_overrun`

- Généré : `2026-08-15T12:47:53Z`
- Fenêtre depuis : `2026-08-12T12:01:34Z`
- Fin process : `2026-08-15T05:44:46Z`
- Meta start/end : `2026-08-12T12:01:34Z` → `2026-08-12T16:01:34Z`
- Watchdog meta : stale=60s max_relaunch=5
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=stop_files_clean_exit | ran_min=3943.2 | vs_planned_min=-3703.2 | timing=late_or_overrun**
- Morts process journalisées (PROCESS_DIE/EXIT) — lire `last_cmd` / `how=signal`.
- Beaucoup de `tension_stale` (1032) = signal latence feed NUAGE (gate 800ms). Sur alpage/WiFi/SIM : possible pic réseau — **à corréler**, pas à conclure seul.
- Issues duo (1106) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 75 | mort process / signal |
| E-STALE | 1032 | tension/NUAGE age (signal latence) |
| E-DUO | 1106 | no_trigger / stale duo |
| E-SPREAD | 2080 | spread trop large |
| I-HUNTER | 364 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=8 pnl=-12.2579 exits={'shock_inversion_stop': 7, 'fluid_exit_inversion': 1}
- BETA : fills=164 pnl=+1.7439 exits={'shock_inversion_stop': 131, 'fluid_exit_inversion': 25, 'fluid_exit_brake': 5, 'shock_exit_10bps': 3}
- **TOTAL** : -10.5140

## Derniers PROCESS_DIE / EXIT

- `2026-08-14T19:35:46Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-14T19:35:48Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-14T19:53:47Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-14T19:53:48Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-14T20:24:29Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-14T20:24:32Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-15T05:44:43Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0`
- `2026-08-15T05:44:46Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0`

## Derniers WATCHDOG

- *(aucun)*

## Échantillon E-STALE (max 8)

- `[ALPHA_X13_BURST13] 13:56:01 x13 #214 SKIP | tension_stale age=8251ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 13:59:59 x13 #241 SKIP | tension_stale age=1451ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:00:34 x13 #245 SKIP | tension_stale age=11752ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:01:25 x13 #249 SKIP | tension_stale age=3716ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:01:34 x13 #250 SKIP | tension_stale age=12838ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:01:52 x13 #252 SKIP | tension_stale age=9932ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:08:25 x13 #297 SKIP | tension_stale age=1823ms>800ms (NUAGE)`
- `[ALPHA_X13_BURST13] 14:11:39 x13 #319 SKIP | tension_stale age=1770ms>800ms (NUAGE)`

## Suite hygiène

1. Si E-WATCHDOG dominant → axe #3 (heartbeat / stale / relaunch), pas un knob storm.
2. Si E-PROC `last_cmd=` clair → bug bash / set -e (comme E11).
3. Si E-STALE seul sans mort → surveiller ; élargir gate seulement avec preuve.
4. Append manuel dans `engle/JOURNAL_ERREURS.md` si nouvel ID (E15…).

---
*scripts/rapport_erreurs_session.py — zéro ordre, zéro genesis.*
