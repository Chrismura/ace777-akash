# AVIS JUGE (task signets.juge) — PAUSE QWEN

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**Analyse du JUGE (ACE777 – indépendant)**  

1. **Impact de la pause réversible**  
   - *Avantage* : supprimer une variable (Qwen‑Ollama) simplifie la phase de fusion et réduit le nombre de points de défaillance locaux.  
   - *Risque* : le modèle Qwen consomme seulement ~17 Mo au repos ; le retirer entièrement élimine un filet de secours gratuit et immédiat en cas de défaillance du hub ou d’un des providers externes (nvidia/grok, gemini, etc.).  

2. **Basculement des 4 fallbacks Gemini → nvidia/grok**  
   - nvidia/grok fait partie des 9 providers gratuits du hub et est généralement plus performant que qwen3.5:4b pour les tâches de type « brief », « analyse », « protocol » et « coffre.ask ».  
   - Toutefois, il convient de vérifier :  
     a) que nvidia/grok est bien marqué comme *gratuit* et *disponible 24/7* dans le hub ;  
     b) que son temps de réponse et son taux d’erreur sont compatibles avec les SLA actuels (tests de charge recommandés avant la bascule définitive).  

3. **Temporalité de la ré‑introduction (après fusion + banc d’essai C6)**  
   - Le mode C6 (ajout après validation) est cohérent avec la décision familiale d’« AMÉLIORER D’ABORD ».  
   - La ré‑introduction doit être conditionnée à :  
     - validation du hub sur le banc d’essai (aucune dégradation de latence ou de taux d’erreur) ;  
     - un test de bascule délibérée Qwen → hub pour s’assurer que le retour en arrière fonctionne sans perte de données ou de configuration.  

4. **Verdict**  

**GO AVEC RESERVES**  

- **Réserve 1** : conserver au moins un service Qwen‑Ollama (ex. `qwen-local`) en tant que *fallback local* pour une tâche critique (par ex. `ada.sanity` ou `chat.local`) afin de disposer d’un secours immédiat en cas d’indisponibilité du hub.  
- **Réserve 2** : effectuer un test de bascule complet des 4 fallbacks Gemini vers nvidia/grok sur un environnement de staging (mesure de latence, taux d’erreur, consommation réseau) avant de le pousser en production.  
- **Réserve 3** : documenter précisément la procédure de rollback (ré‑activation des deux services launchd, rétablissement du provider qwen-local dans le routing) et la tester une fois avant la fusion réelle.  

Si ces réserves sont respectées, la pause réversible de Qwen‑Ollama constitue une étape saine qui simplifie la fusion sans exposer le système à un risque de perte de secours gratuit.
