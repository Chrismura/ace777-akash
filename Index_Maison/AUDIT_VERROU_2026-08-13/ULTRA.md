# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

### VERDICT ACE777 : **GO AVEC RÉSERVES**

En tant qu'expert de la famille ACE777, j'ai audité le code produit par le hub face à la spec, au contexte du drame du 13/08 (boucle de 900 appels/h) et aux principes fondateurs de la machine de tempête. 

Le code est **très bien orienté** : l'anti-spam et le marquage sont bien déplacés au début, le verrou fichier utilise `fcntl.LOCK_NB`, et la distinction entre providers gratuits et payants répond au cahier des charges de Christophe.

Cependant, **4 réserves techniques majeures** doivent être corrigées par le superviseur avant l'intégration finale pour éviter des régressions subtiles ou des faux positifs en production (Mac 8 Go).

---

### RÉSERVES CONCRÈTES & CORRECTIONS REQUISES

#### 1. CRITIQUE : Le piège du `finally` avec le thread détaché (`famille_session.py`, lignes 117-142)
* **Le problème** : Dans `consulter_famille`, le verrou est relâché dans un bloc `finally` après un `time.sleep(0.1)`. Comme le trio hub prend **30 à 60 secondes** à tourner, le verrou est libéré alors que les 3 appels cloud sont **toujours en cours**. Un appel suivant (10s plus tard via launchd) va donc acquérir le verrou et lancer *un nouveau trio en parallèle*, recréant exactement la boucle du 13/08 !
* **Correction** : Le verrou fichier ne doit **pas** être libéré après 0,1s. Soit il reste posé pendant toute la durée de vie du thread (ce qui est compliqué avec des threads détachés en Python), soit on utilise un flag fichier `strategie/famille_en_cours.lock` (ou un state JSON avec timestamp de début) qui bloque tant que le trio n'a pas fini ou tant que le TTL n'a pas expiré.

#### 2. BUG DE CHEMIN : Incohérence des dossiers de stratégie (`famille_session.py`)
* **Le problème** : La constante `STRATEGIE_DIR = "Index_Maison/strategie"` est définie en chemin relatif. Si le script est exécuté depuis un autre répertoire (ce qui arrive souvent avec les daemons `launchd` ou les crons), les fichiers `famille_lock` et `famille_derniere.json` seront écrits au mauvais endroit, rendant le verrou inopérant.
* **Correction** : Rendre le chemin absolu basé sur la racine du projet ACE777 :
  ```python
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  STRATEGIE_DIR = os.path.join(BASE_DIR, "Index_Maison", "strategie")
  ```

#### 3. TEST HERMÉTIQUE : Simulation insuffisante (`test_famille_verrou.py`)
* **Le problème** : Le fichier de test fourni ne teste pas vraiment le code réel de `famille_session.py` (il réécrit des fonctions mockées en /tmp). 
* **Correction** : Le test doit importer directement les fonctions de `Index_Maison/scripts/famille_session.py` en patchant `STRATEGIE_DIR` via un `monkeypatch` ou une variable d'environnement pour garantir l'hermétisme sans dupliquer le code.

#### 4. INTÉGRATION COCKPIT / BUDGET (`budget_hub.py`)
* **Le problème** : Le code de `budget_hub.py` fourni est un extrait. Il manque l'appel d'intégration qui fait le pont entre le calcul quotidien du budget et le déclenchement de la réserve storm dans le flux existant du hub (`hub_prise_ia.py`).
* **Correction** : Veiller à ce que `calculer_budget_journalier` soit bien invoqué au démarrage journalier du hub et que la clé `payant_utilise` soit proprement incrémentée à chaque appel payant.

---

### PLAN D'INTÉGRATION POUR LE SUPERVISEUR (Prêt à l'emploi)

1. **Appliquer la correction du chemin absolu** dans `famille_session.py`.
2. **Remplacer le verrou fichier par un verrou à expiration (TTL)** ou s'assurer que le verrou ne se libère pas prématurément pendant que le trio tourne (pour tenir les 30-60s de la tempête).
3. **Copier `famille_session.py`** dans `Index_Maison/scripts/`.
4. **Mettre à jour `budget_hub.py`** dans `~/prise-ia/`.
5. **Lancer les tests** pour valider la non-régression.
