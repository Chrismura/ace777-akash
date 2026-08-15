# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

En tant qu'expert de la famille ACE777 (ULTRA), voici mon analyse profonde du code et de la spec fournis, à la lumière de la loi du brut, des exigences de la tempête du 13/08 et du contrat d'autogestion.

---

### VERDICT : **GO AVEC RÉSERVES**

Le code fourni par le codeur du hub est de très bonne facture, propre, conforme à Python 3.9 (stdlib), respecte la structure non-fatale et implémente avec précision le calcul dynamique, la réserve storm (20%) et la protection absolue des providers gratuits. Les tests hermétiques dans `/tmp` sont solides.

Cependant, il reste **deux points critiques** à valider/corriger avant l'intégration définitive dans le flux réel du cockpit et de `famille_session.py` / `hub_prise_ia.py`.

---

### ANALYSE DÉTAILLÉE & RÉSERVES CONCRÈTES

#### 1. Le verrou anti-doublon et la tempête (Point de vigilance du superviseur)
* **Contexte de la consigne** : *« Le verrou doit être posé AU DEBUT et TENIR PENDANT TOUTE la consultation (le trio prend 30-60s). POINT DE VIGILANCE DU SUPERVISEUR : dans le code livre, le lock est relache dans finally apres time.sleep(0.1) alors que le thread trio tourne encore... »*
* **Constat dans le code fourni** : Le code soumis concerne `budget_hub.py`, `hub_prise_ia.py` (bloc d'intégration) et `test_budget_storm.py`. Il ne contient pas directement le code de `famille_session.py` gérant le `threading.Lock` ou le `time.sleep(0.1)` mentionné dans l'avertissement.
* **Réserve 1** : Le superviseur **doit impérativement s'assurer** dans `famille_session.py` que le verrou global de consultation (ex: `lock_famille.acquire(blocking=False)`) englobe l'intégralité du cycle de consultation du trio et ne se libère pas prématurément par un `finally` mal placé pendant que les threads tournent. Si ce correctif n'est pas déjà présent dans `famille_session.py`, la boucle de 10s (cortana launchd) continuera de saturer le hub.

#### 2. Intégration du bloc B dans `hub_prise_ia.py` (Ordre d'évaluation)
* **Constat dans le code fourni** : Le bloc d'intégration traite le budget atteint, puis applique la réserve storm ensuite. 
* **Risque logique** : Si `budget_atteint` passe à `True`, le code filtre les `target_ids` pour ne garder que les `GRATUITS`. Juste après, il vérifie si `mode_tempete_actif()` et si la tâche est prioritaire pour consommer la `cloud_reserve`. 
* **Problème potentiel** : Si la tâche prioritaire (ex: `cortana.analyse`) comptait utiliser un provider qui n'est pas strictement dans `GRATUITS` (ou si l'ordre des `target_ids` est réordonné), elle risque de se voir bloquer ou filtrer par la première condition des gratuits avant d'atteindre la condition de la réserve storm.
* **Recommandation (Correction mineure)** : La vérification de la **réserve storm** doit être évaluée **en premier** (avant le filtrage des gratuits) :
  ```python
  # Ordre correct suggéré pour hub_prise_ia.py :
  taches_prioritaires = {"signets.juge", "audit.protocol", "mission", "cortana.analyse", "supervise.decision"}
  
  if mode_tempete_actif() and cloud_budget and usage.get("cloud", 0) >= cloud_budget and cloud_reserve > 0 and task in taches_prioritaires:
      log_event("reserve-storm", f"Consommation réserve storm pour {task}", task)
      # On laisse passer la tâche sans toucher aux target_ids
  elif cloud_budget and usage.get("cloud", 0) >= cloud_budget:
      # Filtrage normal des gratuits...
  ```

#### 3. Conformité de la table `CAPACITES` et des dictionnaires
* **Constat** : `CAPACITES` intègre bien `puter-grok`, `inferx-coder`, `openrouter-ultra`, `openrouter-juge` avec des valeurs non nulles. `GRATUITS` contient l'ensemble des providers gratuits de la flotte.
* **Verdict** : Conforme à la spec. Aucun provider gratuit ne sera coupé, la bascule de même famille fonctionnera même en cas de dépassement du budget "calme".

---

### CONCLUSION POUR L'INTÉGRATION

Le code est **prêt pour l'intégration** sous réserve d'ajuster l'ordre d'évaluation dans `hub_prise_ia.py` (mettre la réserve storm *avant* le filtrage strict des gratuits pour les tâches prioritaires en tempête) et de vérifier que le verrou dans `famille_session.py` protège bien toute la durée du trio (30-60s).

*Signé : ULTRA (Famille ACE777)*
