# AVIS ULTRA (via NVIDIA build.nvidia.com (100+ modeles)) — ultra.analyse

**ANALYSE CRITIQUE DU PLAN PHASE 0 — VERDICT FAMILLE ACE777**

---

## 1. CORRECT ET COMPLET ? — NON, IL MANQUE UNE ÉTAPE CRITIQUE

Le plan est **structurellement correct** mais **incomplet**. Il manque :

- **Étape 0.5 — Vérification de l'intégrité du hub AVANT backup** : le plan suppose que le hub est sain. Or, si le hub est déjà corrompu, le backup capture un état corrompu. Il faut vérifier `/health` + `journal_erreurs.md` AVANT le backup.
- **Étape 4.5 — Test de reprise après rotation** : le plan teste que la rotation fonctionne, mais pas que le superviseur **relit** correctement les logs après rotation. Il faut un test de relecture.
- **Étape 5.5 — Vérification de non-régression globale** : après le repo unique, il faut vérifier que **tous les chemins de référence** pointent vers le nouveau repo, pas seulement `/health`.

**Manque critique** : le plan ne prévoit pas de **test de charge** du hub après chaque étape. Avec 28 services actifs, une modification du timeout superviseur (étape 1) peut avoir un impact sur la file d'attente. Il faut un test de charge léger (10 requêtes simultanées) après chaque étape.

---

## 2. ORDRE DES 5 ÉTAPES — BON, AVEC UNE CORRECTION

L'ordre est **logique** (du plus risqué au moins risqué), mais :

- **Étape 1 (timeout) et Étape 2 (jauge) devraient être inversées** : la jauge est un service actif qui peut envoyer des données au hub. Si on augmente le timeout AVANT de supprimer la jauge, on risque de masquer un problème de la jauge pendant 600 secondes au lieu de 15. **Supprimer la jauge d'abord** rend le système plus prévisible.
- **Étape 3 (git test-freebuff) est indépendante** : elle ne touche pas le hub. Elle peut être faite en parallèle ou en dernier.
- **Étape 4 (rotation logs) et 5 (repo unique) sont correctes en fin de chaîne** : elles sont les moins risquées.

**Ordre recommandé** : 2 (jauge) → 1 (timeout) → 4 (rotation) → 5 (repo) → 3 (git test-freebuff, en dernier car indépendant).

---

## 3. SUPPRIMER LA JAUGE — OUI, MAIS AVEC UNE CONDITION STRICTE

**Le choix est correct** : rebrancher une jauge défaillante sans comprendre pourquoi elle a échoué est risqué. La supprimer proprement (launchctl unload + rm plist) est la bonne approche.

**MAIS** : il faut **documenter précisément** :
- Pourquoi la jauge a échoué (lire `journal_erreurs.md` avant suppression)
- Ce qu'elle surveillait exactement (quels providers, quels quotas)
- Comment le superviseur unique reprendra cette fonction en Phase 1

**Condition stricte** : la suppression est **irréversible** (le plist est supprimé). Il faut **conserver une copie du plist** dans `/Backups/ace777/phase0/` avant suppression, au cas où la Phase 1 échouerait.

---

## 4. RYTHME D'EXÉCUTION — GROUPER EN 1 JOURNÉE, MAIS AVEC DES GARDES-FOUS

**Grouper est le bon choix** pour 3 raisons :
1. **Risque de dérive** : étaler sur 5 jours laisse 5 fenêtres de risque où le système est en état intermédiaire.
2. **Testabilité** : en 1 journée, on peut faire un test de non-régression global à la fin.
3. **Contexte** : Christophe est disponible aujourd'hui pour superviser.

**MAIS** : il faut respecter le mode probatoire C6 (1 action autonome/jour). Donc :
- **Ada exécute 1 étape, puis Christophe valide, puis Ada exécute la suivante** — dans la même journée.
- **Chaque étape doit être validée par Christophe avant la suivante** (pas de validation groupée en fin de journée).

**Si une étape échoue** : arrêt immédiat, rollback, et report à demain.

---

## 5. RISQUES PAR ÉTAPE + VÉRIFICATIONS SPÉCIFIQUES

| Étape | Risque principal | Vérification spécifique |
|---|---|---|
| **1. Timeout** | Le superviseur ne relit pas la nouvelle valeur (cache) | Vérifier que `TIMEOUT_HUB` est bien lu au démarrage : `grep TIMEOUT_HUB superviseur_auto.py` + redémarrer le superviseur et vérifier `/health` |
| **2. Jauge** | Le hub dépend de la jauge pour des données (crash en cascade) | Avant suppression : vérifier que le hub fonctionne sans la jauge (`/health` OK + `journal_erreurs.md` sans erreur jauge). Après suppression : vérifier que le hub ne tente plus de contacter la jauge (`grep jauge superviseur_auto.py`) |
| **3. Git test-freebuff** | Le repo est créé dans un mauvais répertoire (chemins) | Vérifier que `~/test-freebuff` est bien le bon chemin (pas `~/ace777-test-day1/test-freebuff`) |
| **4. Rotation logs** | Le superviseur écrit dans un fichier verrouillé pendant la rotation | Vérifier que la rotation se fait sans erreur : `ls -la ~/prise-ia/reports/` + vérifier que le superviseur continue d'écrire après rotation |
| **5. Repo unique** | Les services pointent vers l'ancien chemin | Vérifier que tous les services référencent le nouveau repo : `grep -r "ace777-test-day1" ~/prise-ia/` + vérifier que le hub est toujours accessible |

---

## 6. VERDICT — VALIDÉ AVEC MODIFICATIONS

**Le plan est applicable** après les corrections suivantes :

1. **Inverser étapes 1 et 2** (jauge d'abord, timeout ensuite)
2. **Ajouter étape 0.5** : vérification intégrité hub avant backup
3. **Ajouter étape 4.5** : test de relecture des logs après rotation
4. **Ajouter étape 5.5** : vérification globale des chemins de référence
5. **Ajouter test de charge léger** (10 requêtes simultanées) après chaque étape
6. **Conserver une copie du plist jauge** dans `/Backups/ace777/phase0/` avant suppression
7. **Respecter le mode C6** : 1 étape à la fois, validation Christophe entre chaque

**Ce que Ada doit faire** :
- Corriger le plan avec ces 7 modifications
- Soumettre la version corrigée à Christophe pour validation
- Exécuter uniquement après validation explicite de Christophe
- Documenter chaque étape dans `journal_erreurs.md` avec horodatage

---

VERDICT FINAL : VALIDE AVEC MODIFICATIONS
CONFIANCE : moyenne
