# AUDIT FAMILLE — GROK

_provider: Puter Grok (gratuit)_

**Verdict : GO AVEC RÉSERVES**

Le correctif est globalement solide et adresse efficacement le fléau principal (panne réseau transformée en attente longue + blacklist injustifiée). La distinction `ReseauIndisponible` + budget global + mode dégradé constitue une bonne architecture défensive.

### Points forts
- Séparation claire des erreurs réseau (pas de `_register_result(False)` ni retry PATIENCE).
- Budget temps strict (120 s) qui protège contre les scénarios 12-80 min.
- Tests unitaires pertinents et rapides.

### Améliorations recommandées

1. **Distinction réseau vs lenteur** : `ReseauIndisponible` ne capture que `socket.gaierror` et `ConnectionError`. Les timeouts de lecture (ex. DeepSeek 129 s) restent traités comme pannes provider. Ajouter un wrapping spécifique sur les timeouts bas-niveau pour les router vers le même chemin réseau.

2. **Test `_reseau_disponible()`** : Le check DNS unique est fragile (cache local, DNS local prêt mais pas de route). Remplacer par un test HTTP HEAD léger (ex. `1.1.1.1` ou `dns.google`) avec timeout 2-3 s, et mettre en cache le résultat 30-60 s.

3. **Budget 120 s** : Correct en nominal, mais serré si 4-5 providers + filet de dernier recours. Proposer `request_max_seconds = 180` en valeur par défaut, avec surcharge possible par provider.

4. **Démarrage hub** : Ajouter un mécanisme optionnel de "wait-for-network" au boot (max 20-30 s) plutôt que de basculer systématiquement en mode dégradé après coupure batterie.

5. **Observabilité** : Logger le temps de disponibilité réseau au démarrage et le nombre de bascules réseau vs provider.

Ces réserves sont mineures et ne bloquent pas le déploiement. Le risque résiduel principal est une sous-détection des pannes réseau partielles.
