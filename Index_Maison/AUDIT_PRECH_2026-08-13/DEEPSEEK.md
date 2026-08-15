# AVIS DEEPSEEK (task mission)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RESERVES**

Le code est globalement conforme à la SPEC du préchauffage (Python 3.9 stdlib, zéro appel réseau, non fatal, structure C1-C4, rapport JSON, `--test`, commentaires en français). Il est intégrable tel quel pour la partie préchauffage (aucun placeholder, `main()` complet, exit code correct). Cependant, plusieurs faiblesses concrètes existent, surtout sur la robustesse des tests et la fidélité à la simulation exigée.

### Réserves concrètes (fichier + points critiques)

**1. verifier_c2() – logique de détection "référencé dans routing" fragile**  
Ligne ~140 :
```python
if p.get("free") is True and (p.get("enabled") is True or p.get("name") in str(data)):
```
`p.get("name") in str(data)` est une astuce douteuse qui dépend de la structure exacte de `providers.json`. Si le routing est dans un fichier séparé (ce qui est probable), cette condition échoue ou donne des faux positifs. À corriger pour vraiment vérifier la présence dans `routing.json` ou un champ explicite.

**2. executer_tests() – mutation de variables globales (problème d’hermétisme)**  
Lignes ~195-230 (dans le `with tempfile.TemporaryDirectory()`).  
Le code fait :
```python
global ROUTING_JSON
ancien_routing = ROUTING_JSON
ROUTING_JSON = mauvais_routing
...
ROUTING_JSON = ancien_routing
```
C’est fragile, non thread-safe, et polluant. Un test peut laisser l’état global dans un état incohérent si une exception survient avant la restauration. Les tests C1 OK / C2 KO enchaînent les réaffectations de manière peu lisible. À remplacer par des injections de dépendance ou des mocks de fonctions `lire_json`.

**3. verifier_c3() – simulation trop superficielle (ne respecte pas vraiment l’esprit de la SPEC C3)**  
Lignes ~165-185.  
Le code crée un dict avec des `True` en dur puis vérifie qu’ils sont `True`. Il ne simule **aucune** logique réelle de bascule (budget calme atteint → mode tempête → tâche prioritaire `signets.juge` qui passe via la réserve vs tâche non prioritaire coupée). C’est un test de forme, pas de comportement. La SPEC demande explicitement de vérifier que « la réserve passe la tâche » et que « une tâche non prioritaire en calme reste coupée ». Actuellement, ce check passe toujours.

**4. Points mineurs mais à noter**
- `afficher_console()` (lignes ~260-270) n’affiche que C1 et C2 en cas de succès, ignore C3/C4.
- Le script ne contient **aucun** des éléments critiques mentionnés dans le contexte d’audit (verrou flock au début, anti-spam écrit avant le trio, mode tempête avec cap horaire désactivé, table CAPACITES avec puter-grok/inferx-coder/etc., réserve 20 %). Ces éléments sont absents car ce fichier est uniquement le préchauffage. Si `famille_session.py` et `budget_hub.py` n’ont pas encore été livrés ou contiennent encore l’ancien anti-spam en fin de consultation + lock relâché dans le `finally` après `time.sleep(0.1)`, le bug racine (boucle 10 s) reste possible.

### Synthèse
Le préchauffage lui-même est **fonctionnel et déployable** après corrections mineures sur les tests et la détection C2. Il respecte l’esprit « non fatal + zéro consommation ».  

En revanche, ce livrable ne traite **pas** les problèmes de verrouillage et d’anti-spam au début qui ont causé l’explosion du 13/08. Tant que les deux autres livrables (`famille_session.py` et `budget_hub.py`) ne sont pas audités avec les mêmes critères (lock posé au tout début et tenu pendant les 30-60 s du trio, anti-spam même en échec, mode tempête prioritaire), le système reste vulnérable.

**Recommandation** : corrige les 3 points ci-dessus, puis fournis `famille_session.py` + `budget_hub.py` pour audit complet du verrou + anti-spam + mode tempête.
