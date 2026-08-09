# AVIS JUGE (via NVIDIA build.nvidia.com (100+ modeles)) — signets.juge

**ANALYSE CRITIQUE DU PLAN PHASE 0 — VERDICT FAMILLE**

---

## 1. CORRECT ET COMPLET ?

**OUI, avec réserves.** Le plan couvre les 5 points de stabilisation identifiés dans l'architecture V2.0. Les corrections de chemins d'Ada sont exactes et nécessaires.

**CE QUI MANQUE (critique) :**
- **Aucune vérification de l'état du hub AVANT l'étape 1.** Le plan suppose que le hub est vivant au départ. Il faut un `/health` initial documenté.
- **Pas de test de charge après chaque étape.** Un simple `/health` ne suffit pas. Il faut vérifier que les 28 services répondent toujours (au moins un échantillon de 5 services critiques).
- **Pas de plan de communication en cas d'échec.** Qui prévient Christophe ? Dans quel délai ? Avec quel rapport ?
- **Pas de seuil de rollback explicite.** « Si le hub ne répond plus » est vague. Il faut définir : 3 échecs `/health` consécutifs = rollback immédiat.

**Verdict partiel :** Correct mais incomplet. Ajouter ces 4 points.

---

## 2. ORDRE DES 5 ÉTAPES — BON ?

**OUI, l'ordre est logique et sûr.** Justification :

| Ordre | Pourquoi c'est bon |
|---|---|
| 1. Timeout superviseur | Augmente la tolérance avant toute modification. Réduit le risque de faux positifs. |
| 2. Jauge | Suppression propre avant de toucher au reste. Élimine une source de conflit. |
| 3. Git test-freebuff | Versionne un composant isolé. Teste le processus git sans risque. |
| 4. Rotation logs | Améliore la robustesse sans changer la logique. |
| 5. Repo unique | Consolide à la fin, quand tout est stable. |

**Point d'attention :** L'étape 2 (jauge) est la plus risquée. La faire en premier après le timeout est correct car le superviseur a maintenant 600s de marge pour absorber un éventuel problème.

---

## 3. SUPPRIMER LA JAUGE — BON CHOIX ?

**OUI, supprimer est le bon choix, MAIS avec une condition.**

**Pourquoi supprimer plutôt que rebrancher :**
- La jauge actuelle est probablement cassée ou incohérente (sinon on ne la supprimerait pas).
- La rebrancher maintenant = ajouter une dépendance non testée pendant la stabilisation.
- La fonction sera reprise par le superviseur unique en Phase 1, qui sera conçu pour ça.

**Condition impérative :** Documenter précisément CE QUE la jauge surveillait (quels providers, quels seuils, quelles alertes) AVANT suppression. Ce savoir ne doit pas être perdu. Créer un fichier `jauge_specs.md` dans le repo de référence.

**Risque si on ne documente pas :** La Phase 1 devra réinventer la fonction sans référence.

---

## 4. RYTHME D'EXÉCUTION — ÉTALER OU GROUPER ?

**RECOMMANDATION : GROUPER en 1 journée, MAIS avec 2 sessions distinctes.**

| Session | Étapes | Justification |
|---|---|---|
| **Session 1 (matin)** | 1 (timeout) + 3 (git test-freebuff) | Les 2 moins risquées. Testent le processus. |
| **Session 2 (après-midi)** | 2 (jauge) + 4 (rotation) + 5 (repo unique) | Les 3 plus risquées. Après validation de la session 1. |

**Pourquoi pas 1 étape/jour :**
- 5 jours de risque prolongé = 5 occasions de régression non détectée.
- Le mode probatoire C6 limite à 1 action autonome/jour, mais ces étapes sont des **actions supervisées** (Ada exécute, Christophe valide). Elles ne comptent pas comme « autonomes ».
- Grouper permet de détecter les interactions entre étapes (ex : rotation logs + repo unique).

**Condition :** Backup complet avant chaque session. `/health` vérifié après chaque étape. Arrêt immédiat si 2 échecs consécutifs.

---

## 5. RISQUE PRINCIPAL PAR ÉTAPE + VÉRIFICATION SPÉCIFIQUE

| Étape | Risque principal | Vérification spécifique |
|---|---|---|
| **1. Timeout** | Le superviseur plante au rechargement (syntaxe, import) | `python -c "import superviseur_auto; print(superviseur_auto.TIMEOUT_HUB)"` → doit afficher 600. Puis `/health` 3 fois à 30s d'intervalle. |
| **2. Jauge** | Le `launchctl unload` échoue silencieusement, ou le plist est mal supprimé | Vérifier `launchctl list \| grep jauge` = vide. Vérifier `ls ~/Library/LaunchAgents/com.ace777.jauge-energie.plist` = absent. Vérifier qu'aucun processus jauge tourne (`ps aux \| grep jauge`). |
| **3. Git test-freebuff** | Le `git init` crée un repo dans le mauvais dossier | Vérifier `cd ~/test-freebuff && git status` → « On branch master » + `git log --oneline` → 1 commit. Vérifier que le dossier `~/ace777-test-day1` n'a PAS de `.git` (pas de pollution). |
| **4. Rotation logs** | Le `RotatingFileHandler` écrase les logs existants ou ne tourne pas | Créer un log > 5 Mo (test manuel), vérifier que `log.1` apparaît. Vérifier que les logs existants sont préservés (comparer avant/après). |
| **5. Repo unique** | Le `git init` à la racine de référence capture des fichiers sensibles (444, WORM) | Vérifier `git status` → aucun fichier 444 modifié. Vérifier `git ls-files` → liste propre, pas de secrets. Vérifier que le `.gitignore` exclut les backups et les logs. |

**Risque transversal :** Le hub peut répondre `/health` OK mais avoir des services internes dégradés. Ajouter un test de 5 services critiques après chaque étape (ex : `curl http://127.0.0.1:11435/service/xxx/health`).

---

## 6. VERDICT + ACTIONS POUR ADA

**VERDICT : VALIDE AVEC MODIFICATIONS**

**Modifications exigées avant exécution :**

1. **Ajouter un `/health` initial documenté** (état de référence avant toute action).
2. **Créer `jauge_specs.md`** documentant la fonction de la jauge avant suppression.
3. **Définir le seuil de rollback** : 3 échecs `/health` consécutifs = rollback immédiat + arrêt.
4. **Ajouter le test des 5 services critiques** après chaque étape (pas seulement `/health`).
5. **Grouper en 2 sessions** (matin : étapes 1+3, après-midi : étapes 2+4+5) avec backup avant chaque session.
6. **Ajouter un `.gitignore`** au repo unique pour exclure backups, logs, et fichiers 444.

**Actions pour Ada :**
- Intégrer ces 6 modifications dans le plan Phase 0.
- Présenter le plan modifié à Christophe pour validation finale.
- Après validation, exécuter la Session 1 (étapes 1+3) avec backup complet.
- Documenter chaque étape dans le journal avec horodatage et résultat des tests.
- En cas d'échec : rollback immédiat, rapport à Christophe, arrêt.

**Confiance :** Haute sur la méthode, moyenne sur l'exécution (dépend de l'état réel de la machine).

---

VERDICT FINAL : VALIDE AVEC MODIFICATIONS
CONFIANCE : haute
