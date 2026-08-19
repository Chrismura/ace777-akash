# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=no_process_exit_logged`

- Généré : `2026-08-17T06:59:02Z`
- Fenêtre depuis : `2026-08-16T19:08:26Z`
- Fin process : ``
- Meta start/end : `2026-08-16T19:08:26Z` → `2026-08-20T19:08:14Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=no_process_exit_logged**
- Issues duo (329) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 0 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 329 | no_trigger / stale duo |
| E-SPREAD | 389 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=0 pnl=+0.0000 exits={}
- BETA : fills=303 pnl=+0.4979 exits={'shock_inversion_stop': 167, 'fluid_exit_inversion': 87, 'fluid_exit_brake': 47, 'shock_exit_10bps': 2}
- **TOTAL** : +0.4979

## Derniers PROCESS_DIE / EXIT

- *(aucun)*

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
