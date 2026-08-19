# AVIS ULTRA (provider Mistral La Plateforme (essai gratuit))

### VERDICT
GO AVEC RESERVES

### Points manquants ou mal bornés
1. **Délai 2e lecture** : 0.5s semble trop court pour capturer des mouvements de marché significatifs. 1s est plus robuste.
2. **Seuil de percussion** : 10-15% semble raisonnable, mais doit être calibré sur des données réelles.
3. **Limitation aux paires actives** : Nécessaire pour éviter les rate-limits, mais doit être configuré dynamiquement en fonction du régime de trading (COOLING/IMPULSE).

### Amélioration concrète
Ajouter un mécanisme de filtrage des signaux aspirés en utilisant une moyenne mobile exponentielle (EMA) pour lisser les données et réduire le bruit. Cela aidera à identifier les tendances réelles plutôt que les fluctuations momentanées.
