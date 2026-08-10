# AVIS GEMINI (task audit.protocol)

provider: Google Gemini

En tant qu'auditeur de protocole de la famille ACE777, voici mon audit critique de la fusion des services de monitoring, menée selon la « loi du brut ».

### VERDICT : **GO AVEC RESERVES**

La fusion est techniquement impressionnante, rigoureusement documentée par la `FUSION_MAP.md` et respecte globalement la règle d'or (le core lit `state.json` sans jamais l'écrire, les cadences par timestamps fonctionnent, et la réversibilité est garantie par le dossier `DESACTIVES_2026-08-10/`). 

Cependant, l'analyse minutieuse du code brut soulève **3 réserves concrètes** qui nécessitent un ajustement pour éviter des effets de bord en production.

---

### 🔍 Réserves Concrètes

#### 1. Divergences dans le nettoyage et la liste des `JOBS_ATTENDUS` (`superviseur_auto.py`)
* **Constat** : Le dossier `DESACTIVES_2026-08-10/` contient **10 plists désactivés** (dont `com.ace777.mirofish.plist`, `mirofish-front.plist`, `qwen-btc.plist`, `qwen-elabore.plist` qui n'étaient pas explicitement gérés dans le scope initial de fusion du core, mais liés à la pause Qwen / Mirofish). Cependant, `JOBS_ATTENDUS` dans `superviseur_auto.py` a bien été nettoyé pour retirer les pulses/vigies et ajouter `com.ace777.superviseur-core` (passant à 11 jobs), mais il ne vérifie pas si les autres services désactivés génèrent des alertes de « job manquant » si le cerveau les cherche encore.
* **Risque** : Le cerveau `superviseur_auto.py` pourrait lever de fausses alertes sur la disparition de certains jobs non déclarés ou mal purgés de sa logique interne.
* **Correction recommandée** : Vérifier que le dictionnaire/liste des jobs surveillés par le cerveau ne contient plus de référence orpheline aux 10 services présents dans `DESACTIVES_2026-08-10/`.

#### 2. Gestion des erreurs non bloquantes (Non-fatalité) dans `superviseur_core.sh`
* **Constat** : Dans la boucle d'orchestration de `superviseur_core.sh` :
  ```bash
  if check_due "heartbeat" 3600; then R_HEARTBEAT=$(check_heartbeat); fi
  ```
  Si une fonction de check (`check_heartbeat`, `check_pulse`, etc.) échoue ou plante en interne sans retourner proprement "OK", "WARN" ou "NOK" (par exemple, si un script Python intégré lève une exception non interceptée comme `sys.exit(1)` vu dans le code quotas), la variable `R_QUOTAS` risque de se retrouver vide (`""`), ce qui fausse l'évaluation globale de `ALL` et du compteur `NOK_COUNT`.
* **Risque** : Un crash d'un sous-script Python fait planter la chaîne d'affectation de la variable, compromettant le contrat de sortie `CORE=OK|WARN|NOK`.
* **Correction recommandée** : S'assurer que chaque appel de fonction encapsule son retour avec un fallback par défaut (ex: `R_QUOTAS=$(check_quotas || echo "NOK")`).

#### 3. Droits et persistance des fichiers de timestamps (`~/.superviseur_core/`)
* **Constat** : Les fonctions `check_due` et `mark_done` écrivent des timestamps epoch dans `~/.superviseur_core/*.last`. 
* **Risque** : En cas de changement de contexte utilisateur ou de permissions sur le dossier `~/.superviseur_core`, le script bascule par défaut à l'état « dû » (`return 0`), ce qui forcerait l'exécution de tous les checks à chaque intervalle de 15 minutes du plist, augmentant inutilement la charge CPU.
* **Correction recommandée** : Ajouter un test de validation `[ -w "$STATE_DIR" ]` dans l'initialisation du core pour garantir l'écriture des états.

---

### 🛡️ Conclusion et Validation
Malgré ces réserves qui doivent être corrigées rapidement pour parfaire la robustesse, **la non-régression est avérée** : les sorties fraîches sont bien là (`SOUS_L_OEIL.md`, `heartbeat.json`, `SECURITE_VIGIE.md`, etc.), le hub tourne à 9 providers, et la colonne vertébrale pulse correctement toutes les 15 minutes. 

Le protocole de fusion passe l'audit avec un **GO AVEC RESERVES**. Vous pouvez procéder aux ajustements mineurs sur `superviseur_core.sh` (encapsulation des retours de checks) avant le déploiement définitif de la flotte.
