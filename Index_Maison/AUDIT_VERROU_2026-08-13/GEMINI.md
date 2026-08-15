# AVIS GEMINI (task audit.protocol)

provider: Google Gemini

**VERDICT : GO AVEC RÉSERVES**

En tant qu'auditeur de protocole ACE777, j'ai analysé le code soumis à la lumière du contexte vivant (machine active, boucles de la gardienne, contrainte Mac 8Go, et surtout l'incident du 13/08 avec les 900 appels/h).

Voici mon audit détaillé et les réserves impératives avant l'intégration finale par le superviseur :

---

### 1. Analyse du Verrou & Point de Vigilance du Superviseur (Modification 1)

* **Le verrou tient-il pendant toute la consultation ?** 
  * **OUI et NON.** C'est ici que se loge la principale réserve. Dans le code produit (`famille_session.py`), le verrou `lock_fd` est acquis au début (`_obtenir_lock()`), mais il est relâché dans le bloc `finally` *immédiatement* après un `time.sleep(0.1)` et après avoir lancé le thread détaché du trio (`thread.start()`). 
  * *Pourquoi c'est un risque :* Le thread du trio effectue les appels réseau vers le hub (ce qui prend 30 à 60 secondes). Si le verrou est relâché au bout de 0,1 seconde dans le `finally`, **le verrou file system saute pendant que le trio tourne encore**. Une nouvelle exécution de `cortana_urgent_poll.sh` (toutes les 10 secondes) pourra donc repasser le verrou, relancer un `consulter_famille()`, et recréer la tempête de doublons constatée le 13/08.
  * *Correction attendue :* Le verrou doit rester actif **pendant toute la durée de vie du thread trio**, ou l'anti-spam (`deja_consulte()`) basé sur le timestamp doit agir comme un mur infranchissable tant que le trio n'a pas fini. Heureusement, le point **1b** (marquage anti-spam *au début*, avant les threads) sauve la mise : même si le verrou fichier se relâche trop tôt, `deja_consulte()` verra le timestamp à `time.now()` et bloquera les appels suivants pendant 5 min (ou 60s en tempête).

### 2. Anti-spam (Modification 1c)
* **Conforme.** `marquer_consulte(raison)` est bien exécuté *avant* le lancement du trio. Même si le trio crash ou que le hub est injoignable, le compteur est mis à jour. Plus de boucle auto-alimentée sur échec.

### 3. Mode Tempête (Modification 2)
* **Conforme.** Les déclencheurs (zone ADA ROUGE/PRENDS_LA_PERTE, alarme récente, vortex force >= 2) sont bien implémentés dans `est_tempete()`. L'anti-spam passe à 60s et le cap horaire est contourné, tout en respectant la machine (pas de ralentissement en cas de crise).

### 4. Budget & Réserve Storm (Modification 3)
* **Conforme.** La table `CAPACITES` intègre les nouveaux providers (`puter-grok`, `inferx-coder`, `openrouter-*`). La distinction `gratuit` vs `payant` protège les gratuits d'une coupure arbitraire. La réserve storm (20%) est isolée pour les tâches critiques en cas de dépassement du budget calme. Le message trompeur sur le "local" est éliminé (respect de la contrainte C9 : jamais de local Qwen).

### 5. Intégrabilité & Tests (Placeholders)
* **Réserve sur les tests :** Les tests fournis dans `test_famille_verrou.py` (T1, T2, T4, T6) sont en grande partie **simulés** (`# Simulation simplifiée du lock`, `print("OK - ... validé")`). Ils ne testent pas réellement le comportement asynchrone des threads du code produit. 
* *Le trio hub :* Dans `famille_session.py`, le bloc du trio est bien un placeholder (`# ... appels cloud ... / pass`). C'est normal et attendu car le superviseur doit y brancher la vraie fonction de consultation existante de l'ACE777 sans casser le codeur.

---

### VERDICT FINAL : GO AVEC RÉSERVES

**Le code est intégrable**, mais le superviseur (toi) doit appliquer **deux correctifs impératifs** lors de l'intégration :

1. **Correction du verrou (Sécurité absolue) :** Ne pas relâcher le verrou fichier dans un `finally` immédiat à 0.1s si le thread tourne, **OU** s'assurer que `deja_consulte()` (basé sur le fichier `famille_derniere.json` écrit au début) est l'unique source de vérité anti-spam infaillible. Pour ma part, je conseille de garder le verrou fichier posé le temps que le thread tourne (en gérant le lock dans le thread ou via un fichier d'état `en_cours.lock` distinct du `famille_lock` d'anti-spam).
2. **Implémentation réelle du trio :** Remplacer le `pass` du thread `_exec_trio` par l'appel réel au trio hub déjà en place dans l'architecture ACE777.
