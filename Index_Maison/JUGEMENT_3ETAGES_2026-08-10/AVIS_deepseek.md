# AVIS DEEPSEEK (via NVIDIA build.nvidia.com (100+ modeles)) — mission

**ANALYSE CRITIQUE DU SETUP DES 3 ÉTAGES — ACE777**

---

### 1. CORRECT, COMPLET, SÛR ?

**Points corrects :**
- Hub intouchable : respecté (aucune commande ne touche port 11435 ni providers).
- Réduction 27 → 13 services : cohérente avec la cible 12-14.
- Mode probatoire C6 : 1 action/jour, double signature, seuil rollback 3 échecs `/health` : mécanismes de sécurité corrects.
- Fichiers plist + script superviseur : structure standard launchd, RAM < 80 Mo combinés : réaliste sur Mac 8 Go.

**Points incomplets ou manquants :**
- **Aucune mention de la sauvegarde/restauration des plists avant désactivation** (Étape 4). Si un service redondant est en réalité critique pour un autre (dépendance cachée), le rollback sera impossible sans backup.
- **Pas de test de charge réel** : le superviseur boucle toutes les 30 min, mais aucune mesure de l'impact CPU/RAM sur un cycle complet (lecture `launchctl list` + `ps` + `vm_stat` + requêtes `/health` sur 9 providers). Sur Mac 8 Go, chaque requête provider consomme de la RAM. Il faut un test de charge avant activation pleine.
- **Pas de gestion des conflits de ports** : si `cockpit.py` lit les sorties de `cockpit-http` et `cockpit-pont`, il doit vérifier qu'il n'écrase pas leurs fichiers de sortie. Sinon, corruption de données.
- **Pas de plan de reprise si le superviseur lui-même meurt** : `KeepAlive: false` + lancement via `launchctl` toutes les 30 min. Si le superviseur plante, qui le relance ? Il faut un mécanisme de relance automatique (ex: `launchd` avec `KeepAlive: true` sur un script wrapper, ou cron).
- **Pas de vérification de l'intégrité des fichiers avant chmod 444** : si `superviseur.py` est corrompu, le chmod 444 le rend illisible et impossible à corriger sans intervention manuelle.

**Verdict partiel : correct mais incomplet. Manque : backup plists, test de charge, gestion crash superviseur, vérification intégrité fichiers.**

---

### 2. SUPERVISEUR UNIQUE — BONNE CONCEPTION ?

**Points positifs :**
- Fusionner jauge + surveillance-quotas + heartbeat en un seul service : réduction de charge, moins de processus, moins de RAM.
- Applique C1-C6 mécaniquement : cohérent avec la loi 1quinquies.
- Ne touche jamais au hub : respecte la contrainte critique.

**Points critiques :**
- **`KeepAlive: false` est une erreur de conception** : un superviseur qui n'est pas gardé en vie par launchd peut mourir silencieusement. Il faut `KeepAlive: true` avec un script wrapper qui vérifie que le superviseur tourne, sinon on perd la supervision elle-même.
- **Boucle 30 min est trop lente pour C5 (sanction auto)** : si un service fautif doit être unloadé, 30 min de latence est acceptable en mode probatoire, mais en production, c'est trop long. Il faut une boucle plus rapide (5 min) ou un mécanisme d'événement.
- **Fusionner 13-15 services en un seul** : risque de point unique de défaillance. Si `superviseur.py` plante, tout le monitoring s'arrête. Il faut un mécanisme de relance automatique (voir point 1).
- **Services à fusionner/supprimer** : la liste n'est pas détaillée. Il faut identifier précisément :
  - Services de monitoring redondants : `surveillance-quotas`, heartbeat, jauge remnants → fusionner dans superviseur.
  - Services de tri/logique : à évaluer un par un, ne pas supprimer aveuglément.
  - Services métier : conserver (4 agents métier + mémoire + observabilité).
  - **Risque** : si un service "redondant" est en réalité utilisé par un autre (dépendance), sa suppression casse tout. Il faut un audit des dépendances avant suppression.

**Verdict : conception globalement bonne, mais `KeepAlive: false` est dangereux, boucle 30 min trop lente pour C5, et la liste des services à fusionner doit être précisée avec audit des dépendances.**

---

### 3. COCKPIT.PY — BONNE APPROCHE ?

**Points positifs :**
- 1 commande unique : simple, lisible, maintenable.
- Lit les sorties de `cockpit-http` et `cockpit-pont` si présents : compatibilité avec l'existant.
- Mesure RAM/disque/latence : observabilité complète.

**Points critiques :**
- **Pas de service launchd dédié** : le cockpit est intégré au superviseur. Si le superviseur est down, plus d'observabilité. Il faut un mécanisme de secours (ex: script autonome exécutable manuellement).
- **Latence par provider** : mesurer 9 providers en séquence peut prendre du temps et consommer de la RAM. Il faut un timeout par provider (ex: 2 s max) pour éviter de bloquer le cockpit.
- **Alertes C1-C6 violations** : comment le cockpit détecte-t-il une violation ? Il doit lire les logs du superviseur. Si les logs sont corrompus ou absents, fausses alertes. Il faut vérifier l'intégrité des logs avant de générer des alertes.
- **Compatibilité avec cockpit-http et cockpit-pont** : si ces services écrivent dans des fichiers, le cockpit doit lire ces fichiers sans les verrouiller. Risque de conflit d'écriture/lecture.

**Verdict : bonne approche, mais il faut un timeout par provider, un mécanisme de secours si superviseur down, et vérification de l'intégrité des logs avant alertes.**

---

### 4. ORDRE D'EXÉCUTION EN 6 ÉTAPES — CORRECT ?

**Points positifs :**
- Mode probatoire C6 : 1 action/jour, double signature, seuil rollback 3 échecs `/health` : sécurité renforcée.
- Étapes progressives : validation → création → intégration → désactivation → activation → audit : logique.

**Points critiques :**
- **Étape 2 (création superviseur minimal C1-C3)** : risque que le superviseur minimal ne soit pas assez robuste pour gérer C1-C3 correctement. Il faut tester chaque condition séparément avant de les activer toutes.
- **Étape 3 (intégration C4-C6)** : risque que C4 (double signature) bloque l'exécution si Ada ou Christophe est absent. Il faut un mécanisme de délégation (ex: Ada + Grok si Christophe absent, comme proposé, mais avec validation écrite).
- **Étape 4 (désactivation progressive)** : risque principal = dépendance cachée. Un service supprimé peut être requis par un autre. Il faut un audit des dépendances AVANT désactivation, et un backup des plists.
- **Étape 5 (activation pleine)** : risque que le superviseur ne gère pas la charge réelle (9 providers + 13 services). Il faut un test de charge avant activation pleine.
- **Étape 6 (audit famille diff)** : risque que l'audit ne détecte pas une régression subtile (ex: latence accrue, RAM plus élevée). Il faut des métriques de référence avant/après.

**Risque principal global : la désactivation des services (Étape 4) sans audit des dépendances. C'est l'étape la plus risquée.**

**Verdict : ordre correct, mais il manque un audit des dépendances avant l'Étape 4, et un test de charge avant l'Étape 5.**

---

### 5. LES 3 PREMIÈRES ÉTAPES — BONNES ?

**Étape 1 (validation spec par Christophe)** : correcte. Lecture seule, aucune commande, rollback N/A. Aucun risque.

**Étape 2 (création plist + superviseur minimal C1-C3)** : correcte en principe, mais :
- Risque : le superviseur minimal ne gère pas correctement C1-C3 (ex: chmod 444 sur un fichier déjà verrouillé, ou lecture `stat` sur un fichier inexistant).
- Il faut tester chaque condition séparément avant de les activer toutes.
- Il faut vérifier que le superviseur ne consomme pas trop de RAM (< 25 Mo comme spécifié).

**Étape 3 (test cockpit + 1 cycle superviseur)** : correcte, mais :
- Risque : le cockpit lit les sorties de `cockpit-http` et `cockpit-pont` et les écrase accidentellement.
- Il faut vérifier que le cockpit ne bloque pas les services existants.
- Il faut un timeout par provider pour éviter de bloquer le cockpit.

**Verdict : les 3 premières étapes sont correctes, mais il faut ajouter des tests de robustesse (test C1-C3 séparément, timeout provider, vérification non-écrasement des fichiers cockpit-http/pont).**

---

### 6. VERDICT + CE QUE ADA DOIT FAIRE

**Verdict global : le setup est réalisable, mais incomplet et avec des risques identifiés.**

**Ce que Ada doit faire :**

1. **Exiger un backup complet des plists avant toute désactivation** (Étape 4). Copier tous les plists dans un dossier `~/Library/LaunchAgents/backup_2026-08-10/` avec checksums.

2. **Exiger un audit des dépendances** avant l'Étape 4 : pour chaque service à supprimer, vérifier qu'aucun autre service ne le référence (via `launchctl list` + lecture des plists).

3. **Exiger `KeepAlive: true`** sur le superviseur avec un script wrapper qui relance automatiquement `superviseur.py` s'il meurt. Sinon, le superviseur peut mourir silencieusement et on perd toute supervision.

4. **Exiger un test de charge** avant l'Étape 5 : exécuter le superviseur pendant 1 heure avec les 13 services actifs, mesurer RAM/CPU, vérifier que le hub `/health` reste OK.

5. **Exiger un timeout par provider** dans `cockpit.py` (2 s max) pour éviter de bloquer le cockpit.

6. **Exiger la vérification de l'intégrité des fichiers** avant chmod 444 : `shasum -a 256 superviseur.py` avant et après chmod, pour détecter toute corruption.

7. **Exiger un mécanisme de délégation de signature** si Christophe est absent : Ada + Grok avec validation écrite (email ou fichier signé), sinon C4 bloque l'exécution.

8. **Exiger des métriques de référence** avant l'Étape 6 : mesurer RAM, latence, taux succès hub AVANT le setup, pour comparer APRÈS et détecter toute régression.

---

**VERDICT FINAL : VALIDE AVEC MODIFICATIONS**  
**CONFIANCE : moyenne**
