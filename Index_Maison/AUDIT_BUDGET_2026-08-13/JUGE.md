# AVIS JUGE (task signets.juge)

provider: Google Gemini

En tant que JUGE, vérificateur indépendant ACE777, j'ai analysé le code soumis par le codeur en croisant les exigences du cahier des charges (budget dynamique, réserve storm, gratuits jamais coupés, robustesse Python 3.9) avec le contexte vivant ACE777 (Saison CALME 🧊, structure du hub).

### VERDICT : **GO AVEC RÉSERVES**

---

### Analyse détaillée

1. **Cause racine de l'incident du 13/08 (rappel & vérification) :**
   * *Rappel du problème :* Boucle de la famille déclenchée toutes les 10s par launchd (`cortana.urgent`) sans verrou persistant au démarrage de la consultation, provoquant une explosion des appels pendant que le trio tournait.
   * *Ce code résout-il la cause racine ?* Le code soumis ici traite la **couche budget et politique de tempête** (`budget_hub.py`, intégration du hub pour la réserve et les gratuits). Il ne réécrit pas le mécanisme de verrouillage de la boucle de famille (qui relève de `ada_gardienne.py` ou du gestionnaire de mission). Toutefois, l'intégration des règles de tempête et de la distinction `GRATUITS` / `PAYANTS` empêche proprement les coupures abusives du hub en cas de forte sollicitation.

2. **Respect du principe « tempête vs calme » :**
   * **Respecté.** Le budget journalier est séparé en un seuil *calme* et une *réserve storm* (20 %). En mode tempête, les tâches prioritaires (`signets.juge`, `audit.protocol`, etc.) piochent dans la réserve au lieu d'être bloquées, et les providers gratuits ne sont jamais coupés.

3. **Conformité des livrables :**
   * **`budget_hub.py` :** Parfaitement conforme. Table `CAPACITES` complète (gemini, openrouter-free, ultra, juge, nvidia, inferx-coder, puter-grok, groq), calcul propre, typage `typing` correct, gestion non fatale des exceptions (`try/except`), et écriture de `cloud_daily_budget` et `cloud_daily_reserve` lors de l'appel `--apply`.
   * **Intégration `hub_prise_ia.py` :** Propre, isole bien les providers gratuits (`GRATUITS`) et gère l'autorisation de la réserve storm si `mode_tempete_actif()` est vrai.
   * **Tests (`test_budget_storm.py`) :** Hermétiques, utilisent un répertoire temporaire (`tempfile`), couvrent l'ensemble des cas demandés et s'exécutent avec des assertions claires.

---

### Réserves concrètes (Points de vigilance pour l'intégration)

1. **Intégration du bloc B2 / B5 dans `hub_prise_ia.py` :** 
   * Dans le bloc d'intégration fourni, la boucle de filtrage des gratuits :
     ```python
     for pid in target_ids:
         if pid in GRATUITS:
             nouveaux_target.append(pid)
         else:
             pass
     ```
     Laisse passer tous les gratuits présents dans `target_ids`. Veillez à ce que l'ordre de priorité initial des providers configurés dans `routing.json` soit préservé pour ne pas dégrader le routage nominal des tâches.
2. **Vérification du verrou amont :**
   * Rappel pour le superviseur lors de l'intégration finale : s'assurer que le verrou anti-doublon (visé par la consigne sur le bug du 13/08) est bien positionné au *début* de la fonction `consulter_famille()` dans le code appelant (hors de ce scope de budget, mais critique pour éviter la récurrence de la tempête de requêtes).
