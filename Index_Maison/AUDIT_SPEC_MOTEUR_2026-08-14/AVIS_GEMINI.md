# GEMINI — gemini.analyse

**1. Verdict**  
**GO + RESERVES** – la SPEC est globalement cohérente mais comporte des angles morts qui doivent être comblés avant mise en production.

**2. Angles morts / limites**  
- **Non‑déterminisme du plantage** : le log FATAL_RC1 ne garantit pas que la même commande échoue sur chaque exécution (intermittence réseau, timing).  
- **Absence de test d’idempotence** : la correction n’est pas obligatoirement vérifiée pour ne pas introduire de nouveaux plantages lorsqu’elle est appliquée plusieurs fois.  
- **Pas de capture structurée des commandes** : on ne sait pas quel appel exact a échoué sans re‑exécuter le script.  
- **Pas de vérification de rollback** : aucune preuve que l’état précédent est restaurable après la correction.

**3. Amélioration concrète (GO‑sized)**  
1. **Wrapper de log de commande**  
   - Implémenter un wrapper (`exec_cmd`) qui, avant d’exécuter chaque commande, écrit dans un fichier JSON :  
     ```json
     {"cmd":"<commande>", "args":[...], "status":<exit_code>, "timestamp":<ts>}
     ```  
   - Modifier le script de lancement pour appeler toutes les commandes via ce wrapper.  
2. **Spécifier dans la SPEC B** :  
   - Le test de correction doit inclure une assertion que le même `cmd` avec `status=1` apparaît exactement une fois dans le log JSON, et que la suite du script se poursuit sans crash.  
   - Exiger un test d’idempotence : exécuter le script corrigé 3 fois de suite et vérifier que le log JSON ne contient aucune nouvelle entrée `status=1`.  

Cette amélioration donne une traçabilité fiable du plantage, élimine la dépendance à un seul exécution, et garantit que la correction est stable avant validation finale.
