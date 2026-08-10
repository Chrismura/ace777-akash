# AVIS JUGE (task signets.juge)

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**Verdict : GO AVEC RESERVES**

**Réserves concrètes à lever avant de considérer le système comme totalement conforme :**

| # | Point de contrôle | Observation actuelle | Pourquoi c’est une réserve | Action corrective recommandée |
|---|-------------------|----------------------|----------------------------|------------------------------|
| 1 | **Absence de lancement non valide au reboot** | Le relevé indique *« plists ace777 sur DISQUE (se chargeraient au reboot) : 23 »*. Même si les plists v2 sont rangés dans `PRETS_ETAPE2` (hors `LaunchAgents`), la présence de 23 plists `ace777` qui seraient chargés au démarrage contredit l’exigence *« zero lancement non valide au reboot »*. | Tant que ces plists restent dans un dossier de lancement (`LaunchAgents`/`LaunchDaemons`), un reboot les activerait, ce qui pourrait perturber la fusion en cours ou laisser tourner des composants non validés. | - Vérifier le contenu exact de ces 23 plists (sont‑ils réellement des plists `ace777` ou d’autres éléments ?). <br> - Si ce sont bien des plists `ace777`, les déplacer hors de tout répertoire de lancement (ex. : les placer dans un dossier `DISABLED` ou les renommer en `.plist.disabled`). <br> - Après déplacement, relancer un inventaire pour confirmer que le compte de plists `ace777` susceptibles de se charger au reboot est tombé à 0. |
| 2 | **Réversibilité** | Backup de l’étape 1 intact (25 fichiers). Aucun signe de corruption. | OK – aucune réserve ici. | Aucun action nécessaire. |
| 3 | **Décision d’attendre la fin de la fusion avant activation** | Le superviseur‑core est actuellement **en mémoire** (`state = running`) mais son plist sur disque est revenu à l’original (`KeepAlive=False`, `StartInterval=900`). Le watchdog n’est pas chargé. Aucun composant ne est configuré pour se lancer automatiquement au reboot. | Le fait que le superviseur‑core tourne déjà en mémoire n’est pas interdit tant qu’il est réversible (il s’arrêtera au prochain reboot tant que son plist ne demande pas de `KeepAlive=true`). Toutefois, il convient de s’assurer que son exécution en mémoire n’interfère pas avec la fusion (ex. : accès exclusif à des fichiers, consommation CPU/ram excessive). | - Surveiller brièvement l’usage CPU/RAM du processus `superviseur-core` (ex. : `top` ou `activity monitor`). <br> - Si l’impact est négligeable (< 5 % CPU, < 50 Mo RAM), laisser tel quel ; sinon, l’arrêter provisoirement (`launchctl unload …` ou `kill`) jusqu’à la fin de la fusion. |
| 4 | **Mise en place de la règle « ETAT REEL »** | Le dossier soumis comporte effectivement une section « ETAT REEL » détaillant les plists disque, les configs chargées et ce qui se lancerait au reboot. | La règle est respectée pour ce dossier. | Aucun action nécessaire. |

### Synthèse
- **Point bloquant** : la présence de 23 plists `ace777` susceptibles d’être chargés au démarrage viole la contrainte « zero lancement non valide au reboot ». Tant que ces plists restent dans un répertoire de lancement, le système n’est pas totalement sûr.
- **Points secondaires** : le superviseur‑core tournant en mémoire est acceptable s’il reste léger et réversible ; la reversibilité et la règle « ETAT REEL » sont satisfaites.

**Conclusion** : Le système peut être considéré comme **GO** *à condition* de lever la réserve n°1 (déplacer ou désactiver les 23 plists `ace777` qui seraient lancés au reboot) et, éventuellement, de vérifier l’impact du superviseur‑core en mémoire. Une fois ces actions effectuées et re‑validées, le verdict pourra passer à **GO** sans réserves.
