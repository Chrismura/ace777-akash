# AVIS JUGE (task signets.juge) — AVANT FUSION

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**ACE777 – Juge indépendant – Analyse pré‑fusion (27 → 13 services)**  

---

## 1. Améliorations à faire **maintenant** (avant la fusion)  
| # | Action | Pourquoi ça simplifie la fusion | Effet attendu |
|---|--------|--------------------------------|---------------|
| 1 | **Désactiver les services « monitoring » redondants qui ne sont jamais vivants** (ex. `com.ace777.analyse-usage`, `com.ace777.analyste-cadence`, `com.ace777.graph-cerveau`, `com.ace777.observatoire`, `com.ace777.pulse-sous-loeil`, `com.ace777.qwen-btc`, `com.ace777.qwen-elabore`, `com.ace777.rotation-logs`, `com.ace777.surveillance-quotas`, `com.ace777.veille-hub`, `com.ace777.verif-setup`, `com.ace777.vigie`) | Ils sont chargés mais **jamais vivants** (voir liste des vivants). Les supprimer maintenant réduit le nombre de plists à gérer et évite de devoir les « fusionner » plus tard. | -12 services chargés → 15 services restants. |
| 2 | **Regrouper les deux services de backup** (`backup-check` + `backup-light_check.sh`) en un seul launchd qui exécute le script léger toutes les 30 min et le contrôle complet toutes les 3 h (via `StartInterval` ou `WatchPaths`). | Aujourd’hui deux déclencheurs séparés créent de la duplication logique et compliquent le suivi du `state.json`. Un seul service simplifie la gestion du flag `backup_ok`. | -1 service, logique de backup centralisée. |
| 3 | **Fusionner les deux services Cortana** (`cortana.horaire` + `cortana.urgent`) en un seul service qui lit un flag d’urgence dans `state.json` et adapte son comportement. | Les deux sont vivants actuellement ; ils partagent le même binaire/script et ne diffèrent que par un paramètre. Un seul service réduit la surface de configuration et évite les conflits d’accès au hub. | -1 service, unification de la logique vocale. |
| 4 | **Nettoyer le fichier `state.json`** : supprimer les clés obsolètes (ex. `last_analyse-usage`, `last_graph-cerveau`) qui ne sont plus utilisées après la désactivation des services ci‑dessus. | Un `state.json` plus léger diminue le risque de lecture/écriture concurrente pendant la fusion et rend le superviseur plus facile à auditer. | Aucun service supprimé, mais moins de bruit. |
| 5 | **Vérifier la cohérence des intervalles** : s’assurer que tous les services restants ont un `StartInterval` clairement défini (pas de `KeepAlive` inutile) afin que le superviseur unique puisse les remplacer sans créer de surcharge. | Évite les surprises de services qui se relancent en boucle après la désactivation de leur plist d’origine. | Stabilité du démarrage/arrêt. |

> **Résultat après ces améliorations** : on passe de **29 services chargés** à **≈15‑16 services chargés** (dont 4 actuellement vivants). Le terrain est nettement plus simple à fusionner.

---

## 2. Comment **simplifier la fusion** (ordre recommandé)

1. **Colonne vertébrale** – garder les services qui sont **vivants** et essentiels au fonctionnement quotidien :  
   - `com.ace777.cockpit-http`  
   - `com.ace777.cockpit-pont`  
   - `com.ace777.cortana.horaire` (fusionné avec urgent)  
   - `com.ace777.prise-ia`  

2. **Phase 1 – Désactivation sécurisée**  
   - Appliquer les améliorations du point 1 (désactiver les 12 services jamais vivants, fusionner backup, fusionner Cortana).  
   - Recharger les plists (`launchctl unload` puis `load`) et vérifier que `state.json` reste **STALE** mais sans erreurs de parsing.

3. **Phase 2 – Création du superviseur unique**  
   - Implémenter un nouveau launchd `com.ace777.superviseur-unique` qui :  
     * Lit `state.json` toutes les 30 s (ou via `WatchPaths`).  
     * Exécute les **tâches critiques** en séquence : génération d’état, vérification de backup léger, contrôle de quota, mise à jour du catalogue, heartbeat, journal du soir, brief matin, etc.  
     * Gère les **retries** et les **alertes** (ex. envoi d’un mail ou d’une notification si un step échoue > 2 fois).  
   - Ce service remplace les fonctions de : `state-generator`, `backup-check`, `surveillance-quotas`, `veille-hub`, `verif-setup`, `journal-soir`, `brief-matin`, `heartbeat`, `prise-ia` (en tant que déclencheur), `cockpit-http/pont` (en tant que relais HTTP si besoin), `cortana.*` (via lecture du flag d’urgence).

4. **Phase 3 – Migration progressive**  
   - Pour chaque fonction déplacée vers le superviseur :  
     a. Garder l’ancien plist actif **en mode “shadow”** (ex. `Disabled=true` mais laissé en place pour rollback).  
     b. Vérifier que le superviseur produit le même résultat (ex. même hash dans `state.json`).  
     c. Une fois validé, décharger définitivement l’ancien plist.  
   - Ordre suggéré (du moins critique au plus critique) :  
     1. `state-generator` → superviseur (génération de l’état).  
     2. `backup-check` → superviseur (backup léger).  
     3. `surveillance-quotas` → superviseur (vérification quotas).  
     4. `veille-hub` / `verif-setup` → superviseur (polling hub).  
     5. `journal-soir` / `brief-matin` → superviseur (tasks temporelles).  
     6. `heartbeat` → superviseur (keep‑alive interne).  
     7. `prise-ia` → superviseur (déclenchement IA selon état).  
     8. `cockpit-http/pont` → rester vivants (ils sont l’interface externe) ; le superviseur ne les remplace pas mais peut les notifier via un signal UNIX ou un fichier de commande.  
     9. `cortana.*` → superviseur (lecture du flag d’urgence et appel au script vocal).

5. **Phase 4 – Nettoyage final**  
   - Supprimer les plists shadow, vérifier que `launchctl list` ne montre plus que le superviseur + les 4 services vivants essentiels.  
   - Faire un test de charge (simuler une perte de provider, un backup qui dépasse la taille, etc.) pour s’assurer que le superviseur gère les erreurs sans bloquer le système.

---

## 3. Trois **risques principaux** de la fusion & parades

| Risque | Conséquence | Parade / Mitigation |
|--------|-------------|---------------------|
| **R1 – Perte de visibilité / état incohérent** | Si le superviseur ne met pas à jour correctement `state.json` (ou omet une clé), les autres services pourraient prendre des décisions basées sur un état périmé → dysfonctionnements en chaîne. | - Implémenter une **validation atomique** du JSON (write to temp file + rename). <br>- Ajouter un **hash de contrôle** dans le fichier et le comparer à chaque lecture. <br>- Garder un **fallback** : si l’écriture échoue, conserver le dernier `state.json` valide et alerter. |
| **R2 – Surcharge du superviseur (CPU / RAM)** | En regroupant plusieurs tâches périodiques, le superviseur pourrait devenir trop gourmand sur un Mac 8 Go, provoquant du swap ou des ralentissements. | - Utiliser `StartInterval` adapté (ex. génération d’état toutes les 2 min, backup léger toutes les 30 min, quotas toutes les 15 min). <br>- Déléguer les tâches lourdes (ex. analyse de logs, appel à des modèles IA) à des **helpers** lancés en arrière‑plan avec `nice`/ionice. <br>- Surveiller la consommation via un petit script qui écrit dans `state.json` une clé `supervisor_load`. |
| **R3 – Difficulté de rollback** | Si une erreur est découverte après la désactivation de plusieurs plists, revenir en arrière pourrait être fastidieux (plists manquants, états corrompus). | - Avant chaque désactivation, **copier** le plist dans un répertoire de backup (`~/Library/LaunchAgents/backup/`). <br>- Conserver un **script de restauration** qui recharge tous les plists backupés et recharge le dernier `state.json` connu bon. <br>- Effectuer la fusion en **fenêtre de maintenance** (ex. nuit) avec un point de restauration snapshotté via Time Machine ou un clone du disque. |

---

## 4. Services que le **superviseur unique** doit remplacer/absorber en priorité

| Priorité | Service(s) à absorber | Raison |
|----------|----------------------|--------|
| **1** | `com.ace777.state-generator` | Source unique de vérité (`state.json`). Sans cela, aucune autre décision ne peut être fiable. |
| **2** | `com.ace777.backup-check` + script léger | Fonction de sauvegarde critique ; doit être déclenchée à partir de l’état connu. |
| **3** | `com.ace777.surveillance-quotas` | Dépend directement des valeurs de `state.json` (usage disque, nombre de providers). |
| **4** | `com.ace777.veille-hub` + `com.ace777.verif-setup` | Polling du hub et vérification du setup ; peuvent être fusionnés en une tâche de “health‑check”. |
| **5** | `com.ace777.journal-soir` + `com.ace777.brief-matin` | Tâches temporelles simples à exécuter séquentiellement dans le superviseur. |
| **6** | `com.ace777.heartbeat` | Peut être remplacé par un ping interne du superviseur (écriture d’un timestamp dans `state.json`). |
| **7** | `com.ace777.prise-ia` | Déclencheur d’IA basé sur l’état ; le superviseur peut appeler le même script lorsqu’une condition est détectée. |
| **8** | `com.ace777.cortana.horaire` + `com.ace777.cortana.urgent` (fusionnés) | Lecture du flag d’urgence dans `state.json` et exécution du script vocal. |
| **9** (optionnel) | `com.ace777.cockpit-http` / `com.ace777.cockpit-pont` | **Ne pas remplacer** : ils constituent l’interface externe ; le superviseur peut seulement leur envoyer des commandes via un fichier de requête ou un signal UNIX. |

---

## 5. Verdict final  

**AMELIORER D’ABORD**  

- Les services actuellement chargés comportent de nombreuses redondances qui ne sont jamais vivantes et qui compliquent la logique de supervision.  
- En appliquant les améliorations listées (désactivation des services inutiles, fusion des backups et des Cortana, nettoyage de `state.json`), on réduit la charge de travail de la fusion et on diminue les risques d’incohérence ou de surcharge.  
- Après ces préparatifs, le terrain sera suffisamment dégagé pour concevoir un superviseur unique fiable, testable et réversible.  

> **Prochaine étape** : exécuter les actions d’amélioration (point 1), vérifier que le système reste stable, puis lancer la conception du superviseur unique suivant l’ordre de simplification proposé (point 2).  

---  

*Fin de l’analyse.*
