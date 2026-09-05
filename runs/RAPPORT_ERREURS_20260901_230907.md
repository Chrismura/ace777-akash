# RAPPORT ERREURS SESSION — ACE_RADAR_ALIGNED_V3_15M

## WHY_ARRET (ligne obligatoire)

`WHY_ARRET=no_process_exit_logged`

- Généré : `2026-09-01T23:09:07Z`
- Fenêtre depuis : `2026-09-01T22:59:57Z`
- Fin process : ``
- Meta start/end : `2026-09-01T22:59:57Z` → `2026-09-01T23:14:57Z`
- Watchdog meta : stale=?s max_relaunch=?
- NET_RETRY (fenêtre) : 0

## Contexte site (rappel)

Alpage · groupe électrogène · 2 lignes (téléphone + surf) · WiFi. Le bot **tient** souvent malgré ça. Les compteurs réseau sont des **signaux** à croiser avec PROCESS_DIE / logique storm — **ne pas tout attribuer au setup terrain.**

## Verdict court

- **WHY_ARRET=no_process_exit_logged**
- Issues duo (5) — scout/hunter désynchro.

## Compteurs

| Code | Nb | Sens |
|------|----|------|
| E-WATCHDOG | 0 | heartbeat / max relaunch |
| E-PROC | 0 | mort process / signal |
| E-STALE | 0 | tension/NUAGE age (signal latence) |
| E-DUO | 5 | no_trigger / stale duo |
| E-SPREAD | 0 | spread trop large |
| I-HUNTER | 0 | STORM_HUNTER arm (info) |

## PnL fills (fenêtre)

- ALPHA : fills=1 gross=+0.4263 fees=+1.0757 net=-0.6494 exits={'timeout': 1}
- BETA : fills=2 gross=-0.5472 fees=+1.1935 net=-1.7406 exits={'timeout': 2}
- **TOTAL** : gross=-0.1209 fees=+2.2692 net=-2.3901

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
