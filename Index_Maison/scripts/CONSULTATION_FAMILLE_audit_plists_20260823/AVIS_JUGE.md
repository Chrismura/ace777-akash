# AVIS JUGE (task juge.tranche · Mistral La Plateforme (essai gratuit) · 2026-08-23T11:47Z)

### VERDICT : GO-AVEC-RÉSERVES
### CONFIANCE : 90 %
### HYPOTHÈSES :
1. La règle « one-shot → pas de KeepAlive » est correcte et suffisante pour éviter les boucles infinies.
2. Le retrait de KeepAlive sur superviseur-core ne casse pas la relance du superviseur car le script a une boucle while interne.
3. Un mécanisme de détection automatique de ce pattern dans veille_degradation.py est nécessaire pour éviter des cas similaires en silence.

### CE QUI CHANGERAIT L'AVIS :
- Découverte de cas où le retrait de KeepAlive casse effectivement la relance d'un job.
- Information sur les impacts potentiels de la suppression de KeepAlive sur d'autres jobs.
- Besoin de tests supplémentaires pour confirmer que le mécanisme de détection automatique fonctionne correctement.

### AMÉLIORATION PROPOSÉE :
1. **Mécanisme de détection automatique** : Intégrer une vérification dans veille_degradation.py pour détecter les plists avec KeepAlive et un intervalle de démarrage, et générer un rapport d'audit.
2. **Documentation des règles** : Ajouter une section dans le README du dépôt pour documenter clairement les règles de configuration des plists launchd.
3. **Tests de non-régression** : Mettre en place des tests automatisés pour vérifier que les jobs se relancent correctement après le retrait de KeepAlive.

### SYNTHÈSE :
Les correctifs appliqués sont globalement efficaces et respectent les bonnes pratiques de configuration des plists launchd. Cependant, des réserves persistent concernant le retrait de KeepAlive sur superviseur-core et la nécessité d'un mécanisme de détection automatique pour éviter des cas similaires. Des améliorations sont proposées pour renforcer la robustesse du système.
