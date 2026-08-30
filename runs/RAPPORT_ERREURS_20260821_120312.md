# RAPPORT ERREURS SESSION — MASTER_VORTEX_V2_COLLAB_4H

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=no_process_exit_logged`

- Généré : `2026-08-21T12:03:12Z`
- Fenêtre depuis : `2026-08-21T11:04:45Z`
- Fin process : ``
- Meta start/end : `2026-08-21T11:04:45Z` → `2026-08-21T15:04:45Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=no_process_exit_logged**
- Issues duo (2099) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 0 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 2099 | no_trigger / stale duo |
| E-SPREAD | 1661 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=6 pnl=+13.3590 exits={'5.17742950': 1, '5.16785098': 1, '3.19492622': 1, '2.58640508': 1, '1.19899572': 1, '1.59961360': 1}
- BETA : fills=11 pnl=+3.0041 exits={'0.78996540': 1, '0.39844147': 1, '0.39674317': 1, '0.39683072': 1, '0.39688090': 1, '0.39614003': 1}
- **TOTAL** : +16.3631

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
