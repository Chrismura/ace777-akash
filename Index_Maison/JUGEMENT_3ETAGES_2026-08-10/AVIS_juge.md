# AVIS JUGE (via OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant) — signets.juge

**1. SETUP DES 3 ÉTAGES – correction, complétude, sécurité**  
- Le plan global (validation → création superviseur minimal → test cockpit → désactivation progressive → activation complète → audit) couvre les étapes nécessaires.  
- **Manque critique** : aucune étape de **sauvegarde/rétablissement** des fichiers launchd actuels avant toute modification, ni de **vérification à froid** (launchctl list / dry‑run) du nouveau plist. Sans cela, un erreur de chargement pourrait laisser le système dans un état partiellement dégradé.  
- Aucun point de contrôle explicitement dédié à la **vérification de la consommation RAM** du superviseur après chargement (seuil < 80 Mo annoncé mais non mesuré).  
- Aucun test de **réversibilité** complet (restore des plists sauvegardés + reload) avant de passer à l’étape suivante.  

**2. Superviseur unique – conception et services à fusionner**  
- La’idée d’un superviseur unique qui regroupe heartbeat, surveillance‑quotas, jauge et les services de monitoring redondants est pertinente, à condition qu’il reste **léger** (< 80 Mo) et **stateless** entre les cycles.  
- **Défaut de conception** : le plist proposé utilise `KeepAlive:false` + `ThrottleInterval:1800` avec `RunAtLoad:true`. Avec `KeepAlive:false`, launchd ne **re‑lancera pas** le processus après sa sortie ; le superviseur ne s’exécutera donc qu’une seule fois au chargement. Il faut remplacer cela par un `StartInterval:1800` (ou un launchd timer séparé) pour garantir l’exécution toutes les 30 min.  
- **Services à conserver (cible 12‑14)** :  
  1. hub (intouchable)  
  2. com.ace777.prise-ia  
  3. com.ace777.cockpit-http  
  4. com.ace777.cockpit-pont  
  5‑8. 4 agents métier (ex. com.ace777.agent‑{1..4})  
  9. service mémoire (ex. com.ace777.mem‑watch)  
 10. service observabilité (ex. com.ace777.obs‑metrics)  
 11. **com.ace777.superviseur-unique** (nouveau)  
 12. **cockpit.py** (exécuté manuellement ou appelé par le superviseur, pas de launchd dédié)  
- Tout le reste (surveillance‑quotas, heartbeat, jauge remnants, ainsi que ~10‑12 services de monitoring/tri redondants) doit être **unloadé** après validation que le superviseur assure leurs fonctions.  

**3. Cockpit.py – approche d’observabilité**  
- Un script unique lancé sur demande (`python3 cockpit.py --etat`) est adapté : il ne introduit aucun daemon supplémentaire, réutilise les sorties existantes de cockpit‑http/pont lorsqu’ils sont présents, et fournit les métriques demandées (état services, taux succès hub, latence provider, RAM/disque, alertes C1‑C6).  
- Risque mineur : si le script est appelé trop fréquemment, il pourrait ajouter une charge CPU négligeable mais à surveiller en mode probatoire.  
- **Compatibilité** : oui, tant que le script ne modifie pas les fichiers de configuration du hub ni ne lance de processus persistants.  

**4. Ordre d’exécution en 6 étapes – pertinence et risques**  
| Étape | Objectif | Risque principal | Mitigation |
|------|----------|------------------|------------|
| 1 – Validation spec | Accord famille | Aucun (lecture seule) | Double signature Ada+Christophe |
| 2 – Création plist + superviseur minimal (C1‑C3) | Chargement du superviseur | **Mauvaise configuration du timer** → superviseur ne s’exécute pas ou s’exécute trop souvent → violation C6 | Utiliser `StartInterval:1800`; tester avec `launchctl start` manuel avant de compter sur le lancement automatique |
| 3 – Intégration C4‑C6 + test cockpit | Première exécution réelle | Action non autorisée (>1 action/jour) si le script effectue plus qu’un healthcheck | Limiter le script à lecture seule + journalisation; vérifier le journal après exécution |
| 4 – Désactivation progressive des services redondants | Réduction à 12‑14 services | Désactivation d’un service encore nécessaire → perte de fonction | Unload un par un, vérifier `/health` et les métriques cockpit après chaque unload; rollback immédiat si dégradation |
| 5 – Activation pleine du superviseur | Passage en mode heartbeat continu | Défaillance du superviseur → perte de surveillance | Garder les services de secours chargés jusqu’à confirmation de 3 cycles réussis du superviseur |
| 6 – Audit famille diff + validation Christophe | Confirmation finale | Oubli d’un changement non autorisé | Comparer la liste des plists avant/après avec `diff`; exiger double signature avant clôture |

Le **seuil de rollback** (3 échecs consécutifs du `/health` du hub) est raisonnable, mais il doit être accompagné d’une **vérification de l’état du superviseur** (processus présent, journaux) avant de déclencher le rollback.  

**5. Trois premières étapes proposées – pertinence**  
- **Étape 1** (validation spec) : correcte, indispensable.  
- **Étape 2** (plist + superviseur minimal C1‑C3) : correcte **à condition** de corriger le mécanisme de périodicité (StartInterval) et de s’assurer que le script ne fait aucune modification (lecture seule, chmod 444, journalisation).  
- **Étape 3** (test cockpit + 1 cycle superviseur) : correcte, mais il faut ajouter une vérification explicite que le superviseur n’a effectué **qu’une seule action** (ex. un healthcheck) et que le journal respecte la limite C6.  

**6. Verdict et actions pour Ada**  

- **Verdict** : le setup est globalement valide mais nécessite **des modifications mineures critiques** (timer du superviseur, sauvegarde/rétablissement, vérification de la périodicité et de la limite C6).  
- **Actions immédiates** :  
  1. Faire valider cette spécification corrigée par Christophe (double signature Ada+Christophe).  
  2. Préparer une sauvegarde de `~/Library/LaunchAgents/` (copie tar) avant toute modification.  
  3. Réviser le plist du superviseur pour utiliser `StartInterval:1800` (ou un launchd timer séparé) et retirer `KeepAlive:false`/`ThrottleInterval`.  
  4. Rédiger le script `superviseur.py` en mode lecture‑seule + journalisation stricte, en s’assurant qu’il ne réalise qu’un healthcheck et éventuellement une écriture de `state.json` atomique.  
  5. Tester le chargement avec `launchctl load` puis `launchctl start com.ace777.superviseur-unique` pour confirmer l’exécution périodique, vérifier la RAM (`ps -o rss -p <pid>`) et le nombre d’actions journalisées.  
  6. Une fois ces vérifications réussies, passer à l’étape 2 telle que décrite (plist + superviseur minimal C1‑C3).  

**VERDICT FINAL : VALIDE AVEC MODIFICATIONS**  
**CONFIANCE : moyenne** (les modifications nécessaires sont identifiées et simples à appliquer, mais tant qu’elles ne sont pas intégrées, le plan comporte un risque de non‑respect du mode probatoire C6 et de défaillance du timer de supervision).
