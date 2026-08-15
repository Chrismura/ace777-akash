# AVIS GEMINI (task audit.protocol)

provider: Google Gemini

En tant qu'auditeur de protocole de la famille ACE777 (GEMINI), voici mon audit technique et chirurgical du code soumis (`famille_session.py` v4).

---

### VERDICT : **GO AVEC RÉSERVES MINEURES**

Le code livre est extrêmement propre, respecte scrupuleusement la loi de l'art (Python 3.9 stdlib, non fatal, typage correct, gestion des exceptions robuste) et **intègre parfaitement les 3 corrections demandées** (fermeture du descripteur de fichier pour fuite FD, branchement du mode tempête avec bypass TTL, et création immédiate de l'état TTL après le flock réussi).

Il reste cependant **deux réserves d'intégration** à lever par le superviseur avant le commit final :

---

### ANALYSE DES POINTS CLÉS DU CONTRAT

1. **Verrou anti-doublon & Position de l'anti-spam :**
   * **Conforme.** L'anti-spam (`_verifier_etat_ttl`) est vérifié **au tout début** de `consulter_famille()`.
   * **Conforme (Correction 3).** L'état TTL est créé immédiatement après l'obtention du `flock` et avant de lancer le thread. Cela neutralise définitivement la faille du 13/08 où un appel à 10s pouvait se faufiler pendant que le thread s'initialisait.

2. **Mode tempête :**
   * **Conforme (Correction 2).** Le mode tempête (`mode_tempete_actif()`) lit correctement les états critiques (`ada_gardienne_live.json` sur les zones `ROUGE` / `PRENDS_LA_PERTE`, l'alarme récente, et `etat_tempete.json`).
   * Il réduit l'anti-spam à **60 secondes** et **bypasse le TTL** lorsque la tempête fait rage, garantissant que la machine ne se laisse pas paralyser par ses propres garde-fous.

3. **Fuite de descripteur de fichier (FD) :**
   * **Conforme (Correction 1).** `os.close(lock_fd)` est bien présent dans le bloc `finally` après le `LOCK_UN`, prévenant l'erreur fatale *« Too many open files »* sur un démon 24/7.

---

### RÉSERVES CONCRÈTES (À ajuster par le superviseur)

* **Réserve 1 (Fichier d'état supprimé dans le `finally` - Ligne 151) :**
  Dans `_thread_trio` (bloc `finally`), le code supprime `FICHIER_ETAT` :
  ```python
  if os.path.exists(FICHIER_ETAT):
      os.remove(FICHIER_ETAT)
  ```
  *Conséquence :* En fin de thread, le fichier TTL est effacé. Si la consultation se termine rapidement (en 2-3 secondes), l'anti-spam saute immédiatement, ce qui risque de relancer un nouveau tour de piste instantanément lors du prochain tick de 10s. 
  *Recommandation :* Ne pas supprimer `FICHIER_ETAT` dans le `finally`. L'état TTL doit expirer naturellement via son timestamp (`time.time() - etat["timestamp"] < duree`), c'est précisément son rôle de régulateur anti-spam.

* **Réserve 2 (Timeout du thread - Ligne 178) :**
  `t.join(timeout=90)` est appelé dans le thread principal de `consulter_famille()`. Si la consultation prend plus de 90 secondes, le thread principal rend la main tandis que le thread trio continue en arrière-plan (étant `daemon=True`). C'est acceptable, mais il faut s'assurer que le verrou `lock_fd` ne sera pas fermé prématurément par le thread principal si celui-ci s'échappe du `join()`. Actuellement, le verrou est passé au thread et géré dans son propre `finally`, ce qui est correct, mais le `join(timeout=90)` bloquera l'appelant pendant 90s en cas de freeze réseau d'un provider. À surveiller sous Mac 8 Go.

---

### CONCLUSION
Le code est **intégrable** et résout avec brio la crise du 13/08. Applique la correction de la réserve 1 (laisser le TTL expirer par le temps plutôt que de supprimer le fichier d'état dans le `finally`), et le module sera prêt pour le front de mer d'ACE777.
