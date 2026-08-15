# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

En tant qu'**ULTRA**, membre expert de la famille ACE777, voici l'analyse approfondie, sans concession et brute du code soumis.

---

### VERDICT GLOBAL : **GO AVEC RÉSERVES**

Le code produit par le codeur du hub respecte rigoureusement la **Loi 1quinquies** et les volontés de Christophe :
1. **Zéro constante en dur pour les gratuits** : La liste des providers gratuits est totalement externalisée et dynamique via `providers.json` (`"free": true`).
2. **Principe de tempête respecté** : En mode tempête, les gardes-fous ne bloquent pas les tâches prioritaires, la réserve de 20 % est mobilisée et **aucune coupure brutale** n'est appliquée.
3. **Python 3.9 stdlib** respecté à la lettre, typage propre (`Optional`), code non fatal et robuste aux exceptions (try/except généralisés).

Cependant, il subsiste **deux points de vigilance critique** par rapport au contexte initial du 13/08 (la boucle famille incontrôlée) et à l'intégration dans `hub_prise_ia.py` / `famille_session.py` qu'il faut verrouiller avant le déploiement en production.

---

### ANALYSE DÉTAILLÉE ET RÉSERVES CONCRÈTES

#### 1. Le verrou anti-spam et la boucle famille (`famille_session.py` / `hub_prise_ia.py`)
* **Le risque (Rappel du bug du 13/08)** : Lors de l'incident du 13/08, l'anti-spam de 5 minutes était positionné à la *fin* de la consultation dans un thread détaché. Résultat : chaque déclenchement toutes les 10s relançait un trio de 30-60s en parallèle, explosant les compteurs.
* **Le code livré** : Le code fourni ici traite de la *dynamique budgétaire* et de la gestion de la liste `free` dans `hub_prise_ia.py`, mais il ne contient pas le code exact du verrou anti-spam (thread de verrouillage / écriture du fichier de lock au *début* de la fonction). 
* **Réserve 1** : S'assurer que dans le fichier réel `famille_session.py` ou `cockpit_mission_feed`, le verrou (`lock` ou fichier témoin d'exécution) est posé **avant** toute invocation du trio et qu'il ne se libère qu' *après* la fin effective du traitement (pas dans un `finally` prématuré avec un `time.sleep(0.1)` qui laisse passer une nouvelle itération launchd 10s plus tard).

#### 2. Intégration de `providers.json` dans `hub_prise_ia.py` (Performance / I/O)
* **Dans le bloc d'intégration de `hub_prise_ia.py`** :
  ```python
  providers: List[Dict[str, Any]] = []
  try:
      prov_path = os.path.join(P, 'providers.json')
      if os.path.exists(prov_path):
          with open(prov_path, 'r', encoding='utf-8') as f:
              providers = json.load(f).get('providers', [])
  except Exception:
      providers = []

  gratuits: Set[str] = {p.get("id") for p in providers if p.get("free") is True}
  ```
* **Réserve 2** : Ce bloc lit le fichier `providers.json` à *chaque* appel de routage/évaluation du hub. Si le hub traite des dizaines de requêtes à la minute, cela fait des I/O disque répétées. Bien que non fatal, il est recommandé de mettre en cache cette liste en mémoire (avec un TTL court ou un mécanisme de rechargement sur modification du fichier) pour garder la machine de tempête ultra-réactive.

---

### VALIDATION POUR LES TESTS HERMÉTIQUES

* **`test_budget_storm.py`** : Le fichier de test couvre parfaitement les cas demandés (capacités, calcul de budget, gratuits dynamiques depuis `providers.json`, non-coupure en tempête, écriture `--apply`). Il est exécutable immédiatement en l'état.
* **`budget_hub.py`** : Parfaitement autonome, intègre correctement `gratuits_actifs()` lisant le JSON. Prêt pour un cron quotidien ou un appel manuel avec `--apply`.

### INSTRUCTIONS POUR LE SUPERVISEUR (INTÉGRATION)
1. Intégrer `providers.json` avec les champs `"free": true` validés.
2. Remplacer le bloc budget dans `hub_prise_ia.py` par le bloc fourni.
3. **Vérification finale du verrou** : Inspecter `famille_session.py` pour valider que le verrou anti-spam est positionné en tête de ligne (avant le scan de la gardienne) et dure pendant toute la durée du trio (30-60s).

Le code est **prêt pour l'intégration** sous réserve de l'application de ces deux précautions chirurgicales.
