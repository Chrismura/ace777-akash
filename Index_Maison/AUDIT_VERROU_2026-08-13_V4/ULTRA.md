# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

En tant qu'**ULTRA**, membre expert de la famille ACE777, voici mon analyse approfondie et mon verdict concernant le code livré (`famille_session.py` v4).

---

### VERDICT : **GO AVEC RÉSERVES**

Le code fourni est de très haute qualité, élégant, strictement conforme aux spécifications de la **v4** et respecte à la lettre les consignes de la loi 1quinquies et du mode tempête (Python 3.9 stdlib, non fatal, gestion des fuites de descripteurs de fichiers, TTL au début, bypass du TTL en tempête).

Cependant, il reste **2 réserves chirurgicales** à lever ou à garder à l'esprit pour assurer une intégration hermétique sans casse dans le cockpit et avec `budget_hub.py`.

---

### ANALYSE DÉTAILLÉE & RÉSERVES

#### 1. Cohérence Spec / Code : **100% Conforme**
* **Correction 1 (Fuite FD)** : Implémentée correctement. Le bloc `finally` de `_thread_trio` appelle bien `fcntl.LOCK_UN` puis `os.close(lock_fd)` dans des blocs `try/except` isolés.
* **Correction 2 (Mode Tempête)** : Implémentée avec brio. 
  * `consulter_famille()` bypass le TTL si `mode_tempete_actif()` est vrai ou si `force=True`.
  * `_duree_anti-spam()` retourne bien `60.0` en tempête et `300.0` au calme.
  * `mode_tempete_actif()` balaie robustement les 3 sources (ADA ROUGE/PRENDS_LA_PERTE, alarme récente < 3600s, et `etat_tempete.json`).
* **Correction 3 (TTL immédiat)** : `_creer_etat_ttl()` est appelé juste après le succès de `fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)`, ce qui neutralise définitivement la race condition du 13/08.

#### 2. Intégration avec le flux existant (`cockpit`, `budget_hub.py`, `ada_gardienne`)
* **Attention au nettoyage du fichier d'état dans le `finally` (Ligne 156)** :
  Dans `_thread_trio`, le bloc `finally` supprime `FICHIER_ETAT` (`os.remove(FICHIER_ETAT)`). 
  * *Effet de bord potentiel* : `FICHIER_ETAT` (`famille_etat.json`) sert à la fois de **TTL anti-spam** (via son horodatage) et de **conteneur de données** (membres, dernière consultation). Si le thread supprime le fichier à la fin de son exécution, le TTL disparaît immédiatement, ce qui signifie que *dès la fin du thread, l'anti-spam tombe*, autorisant un nouveau déclenchement immédiat si un appel 10s survient (sauf si le mode tempête est actif, auquel cas c'est voulu, mais au calme cela casse l'anti-spam de 5 minutes).
  * *Correction recommandée* : Ne **jamais** supprimer `FICHIER_ETAT` dans le `finally`, car l'anti-spam repose sur la persistance de ce timestamp. Laisser l'horodatage s'périmer naturellement selon `_duree_anti_spam()`.

* **Intégration du Trio Réel vs Logique Minimale** :
  Le thread exécute une logique propre mais simulée (`etat_famille["derniere_consultation"] = time.time()`). Pour l'intégration finale dans le cockpit ACE777, il faudra s'assurer que l'appel aux trois modèles du hub (ex: Puter Grok, Inferx Coder, OpenRouter Ultra/Juge) est bien branché à la place ou à l'intérieur de ce thread si le cockpit l'attend de manière synchrone via le `t.join(timeout=90)`. Actuellement, le code bloque bien 90s max via `t.join()`, ce qui est parfait.

---

### PLAN D'ACTION POUR LE SUPERVISEUR (Avant intégration définitive)

1. **Retirer la ligne `os.remove(FICHIER_ETAT)`** dans le bloc `finally` de `_thread_trio` (ligne ~156) pour garantir que l'anti-spam de 5 minutes fonctionne correctement en temps calme (le TTL doit persister sur le disque, c'est son but).
2. Valider que `budget_hub.py` lit bien les capacités dynamiques sans conflit avec le verrouillage du fichier `famille.lock` (les deux mécanismes utilisent des fichiers séparés, donc pas de deadlock inter-module).

Le code est **prêt pour les tests hermétiques** dès application de la retouche sur le `finally`.
