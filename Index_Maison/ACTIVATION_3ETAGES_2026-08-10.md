# 🏗️ ACTIVATION DU SETUP 3 ÉTAGES — 10/08/2026 15:00

Décision Christophe : « go set up 3 etages » (fusion terminée + validée famille 4/4).

## Ce qui a été activé
| Service | Avant | Après |
|---|---|---|
| superviseur-core | par cycles (StartInterval 900, KeepAlive=False) | **EN CONTINU** (KeepAlive=True + boucle interne while true, contrat CORE=OK à chaque cycle) |
| **watchdog** (NOUVEAU) | absent | **actif** (toutes les 2 min : si superviseur-core mort → relance + vérification 3 s) |

## Preuves de fonctionnement (tests réels)
- ✅ superviseur-core : state=running en continu, PID stable, « never exited »
- ✅ Contrat CORE : 5 checks actifs (heartbeat/pulse/vigie/quotas/rotation, timestamps à jour)
- ✅ **TEST DÉCISIF** : kill du superviseur-core → KeepAlive relance immédiat + watchdog confirme
  « Relance CONFIRMÉE (processus actif après 3 s) » (log ~/.superviseur_core/watchdog.log)
- ✅ Hub : OK 9 providers · Cockpit : OK · Cerveau (superviseur intelligent) : OK
- ✅ Au reboot : les 2 plists sont sur disque → tout se relance automatiquement

## Fichiers
- Plist V2 : ~/Library/LaunchAgents/com.ace777.superviseur-core.plist (KeepAlive=True)
- Plist watchdog : ~/Library/LaunchAgents/com.ace777.watchdog.plist (StartInterval 120)
- Scripts : superviseur_core.sh (boucle) + watchdog_superviseur.sh (relance) — audités famille

## Rollback (2 min)
- Backup : ~/Backups/ace777/avant_activation_3etages_20260810_1459/ + PRETS_ETAPE2 (ORIGINAL + V2)
- Procédure : recopier le plist ORIGINAL (KeepAlive=False) → bootout + bootstrap → supprimer watchdog

## Historique
- Étape 2 préparée le 10/08 matin (codeur code → famille audit → corrections validées → intégré)
- Mise en attente (décision Christophe : rien avant fin de fusion) → PRETS_ETAPE2
- Fusion terminée + audit famille GO 4/4 → activation GO 15:00
