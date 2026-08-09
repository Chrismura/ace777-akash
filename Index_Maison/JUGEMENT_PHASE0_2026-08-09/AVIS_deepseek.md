# AVIS DEEPSEEK (via NVIDIA build.nvidia.com (100+ modeles)) — mission

**ANALYSE CRITIQUE DU PLAN PHASE 0 — VERDICT FAMILLE**

---

## 1. CORRECT ET COMPLET ? — PARTIELLEMENT, 2 ÉTAPES CRITIQUES MANQUENT

**Ce qui est bon :**
- Backup complet avant toute action : indispensable, bien pensé.
- Vérification `/health` après chaque étape : non-négociable, bien intégré.
- Rollback immédiat si hub ne répond plus : règle d'or, correcte.
- Étape 1 (timeout superviseur) : nécessaire, le hub doit survivre aux lenteurs.
- Étape 4 (rotation logs) : utile, mais pas critique pour la stabilité.

**Ce qui manque (critique) :**
1. **Aucune vérification de l'intégrité des 28 services après chaque étape.** Le hub répond `/health`, mais cela ne prouve pas que les 28 services sont toujours actifs et fonctionnels. Il faut un test de non-régression complet : `curl` sur chaque service ou au minimum un script de vérification des processus.
2. **Aucune étape de validation du backup avant de commencer.** Le backup est fait, mais personne ne vérifie qu'il est complet et restaurable. Si le backup est corrompu, le rollback est impossible. Il faut tester la restauration sur un répertoire temporaire avant de toucher au système.

**Verdict partiel :** Le plan est correct dans sa structure, mais **incomplet**. Il manque 2 étapes critiques : validation du backup et vérification complète des 28 services.

---

## 2. ORDRE DES 5 ÉTAPES — BON, SAUF UNE INVERSION

**Analyse :**
- **Étape 1 (timeout superviseur)** : correct en premier. C'est le socle, rien d'autre ne doit bouger avant.
- **Étape 2 (suppression jauge)** : correct en deuxième. Elle est isolée, ne touche pas au hub.
- **Étape 3 (git test-freebuff)** : correct en troisième. C'est un bac à sable, aucun risque.
- **Étape 4 (rotation logs)** : correct en quatrième. Touche le superviseur, mais après le timeout, c'est plus sûr.
- **Étape 5 (repo unique)** : **FAUX en dernier.** Créer un repo git à la racine de référence est une action structurante. Si elle échoue, elle peut corrompre l'arborescence. Elle doit être faite **avant** les étapes 3 et 4, car ces étapes créent des fichiers qui devront être versionnés. Sinon, on devra refaire le repo après.

**Correction :** Inverser l'ordre : 1 → 2 → 5 → 3 → 4. Le repo unique doit être créé avant de versionner quoi que ce soit.

---

## 3. SUPPRIMER LA JAUGE — OUI, MAIS AVEC UNE CONDITION STRICTE

**Analyse factuelle :**
- La jauge surveille l'énergie/quota par provider. Sa fonction est critique pour éviter les dépassements de quota.
- Le superviseur unique en Phase 1 doit reprendre cette fonction. **Mais la Phase 1 n'est pas encore planifiée ni datée.**
- Si on supprime la jauge maintenant, on perd la surveillance pendant la période entre Phase 0 et Phase 1. **C'est un trou de sécurité.**

**Décision :**
- **OUI, supprimer la jauge** car elle est instable et peut casser le hub (c'est la raison de sa suppression).
- **MAIS** : Ada doit immédiatement mettre en place un **script de surveillance minimal** (cron ou launchd) qui vérifie les quotas par provider et écrit dans un log. Ce script est temporaire, en attendant la Phase 1. Il ne doit pas toucher au hub, juste surveiller et alerter.

**Condition stricte :** Si ce script de surveillance n'est pas en place dans les 24h suivant la suppression de la jauge, la suppression est annulée et la jauge est rebranchée.

---

## 4. RYTHME D'EXÉCUTION — GROUPER, MAIS EN 2 BLOCS

**Analyse :**
- Le mode probatoire C6 impose 1 action autonome/jour. C'est une contrainte de sécurité, pas une recommandation.
- Étaler sur 5 jours : risque de laisser le système dans un état intermédiaire instable pendant 5 jours. C'est pire que tout.
- Grouper tout en 1 journée : risque de ne pas détecter une régression subtile.

**Décision :**
- **Grouper en 2 blocs sur 2 jours** :
  - **Jour 1** : Backup + validation backup + Étape 1 (timeout) + Étape 2 (suppression jauge) + mise en place du script de surveillance.
  - **Jour 2** : Étape 5 (repo unique) + Étape 3 (git test-freebuff) + Étape 4 (rotation logs) + vérification complète des 28 services.
- Chaque bloc est testé intégralement avant de passer au suivant.
- **Exception C6** : la famille autorise 2 actions autonomes par jour pour cette opération, car c'est une stabilisation d'urgence. Cette exception est temporaire et ne s'applique qu'à la Phase 0.

---

## 5. RISQUE PRINCIPAL PAR ÉTAPE + VÉRIFICATION SPÉCIFIQUE

| Étape | Risque principal | Vérification spécifique à ajouter |
|---|---|---|
| **Backup** | Backup incomplet ou corrompu | Tester la restauration sur un répertoire temporaire, vérifier que tous les fichiers critiques sont présents (taille, nombre) |
| **1. Timeout superviseur** | Le superviseur ne redémarre pas correctement après modification | Vérifier que le processus superviseur est relancé, pas seulement le hub. `ps aux \| grep superviseur` |
| **2. Suppression jauge** | Un service dépend encore de la jauge et plante | Vérifier les logs de chaque service pendant 10 minutes après suppression. Si un service écrit une erreur liée à la jauge → rollback immédiat |
| **3. Git test-freebuff** | Le repo git corrompt les fichiers existants | Vérifier que `git status` ne montre aucun fichier modifié après le commit initial. Vérifier que les fichiers 444 sont toujours intacts |
| **4. Rotation logs** | Le superviseur écrit dans un fichier verrouillé et plante | Vérifier que le superviseur continue d'écrire dans le nouveau fichier de log après rotation. Simuler une rotation manuelle et vérifier `/health` |
| **5. Repo unique** | Le repo git à la racine capture des fichiers sensibles (clés, tokens) | Vérifier le `.gitignore` avant le commit. S'assurer que les fichiers 444 et les secrets ne sont pas versionnés |

---

## 6. VERDICT — VALIDÉ AVEC MODIFICATIONS

**Le plan est bon dans son esprit, mais il doit être corrigé avant exécution.**

**Modifications obligatoires :**
1. **Ajouter l'étape 0** : validation du backup (test de restauration).
2. **Ajouter l'étape 6** : vérification complète des 28 services après chaque étape (pas seulement `/health`).
3. **Inverser l'ordre** : 1 → 2 → 5 → 3 → 4.
4. **Mettre en place un script de surveillance temporaire** immédiatement après la suppression de la jauge.
5. **Grouper en 2 blocs sur 2 jours** avec autorisation exceptionnelle de 2 actions/jour.

**Ce que Ada doit faire :**
1. Corriger le plan selon les modifications ci-dessus.
2. Le soumettre à Grok pour re-signature (double signature obligatoire).
3. Présenter le plan corrigé à Christophe pour validation finale.
4. **Ne rien exécuter avant cette validation.**

---

VERDICT FINAL : VALIDE AVEC MODIFICATIONS
CONFIANCE : moyenne
