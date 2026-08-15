# AUDIT FAMILLE — DEEPSEEK

_provider: Puter Grok (gratuit)_

**Verdict : GO AVEC RÉSERVES**

Le correctif est globalement solide et adresse directement la racine du problème (démarrage hub avant réseau). La distinction `ReseauIndisponible` + absence de `_register_result(False)` empêche efficacement la blacklist de providers sains. Le budget global de 120 s et le test `_reseau_disponible()` en entrée de `chat_completions` limitent drastiquement les durées aberrantes (12-80 min → max ~2 min). Les tests unitaires confirment le comportement attendu.

**Réserves principales :**
- La fiabilité de `_reseau_disponible()` n’est pas démontrée (test DNS unique ? latence ?).
- Le budget 120 s peut être trop court en mode dégradé avec plusieurs providers lents.
- Pas de mécanisme de sortie du mode dégradé une fois le réseau rétabli.

**Améliorations recommandées :**
1. Rendre `_reseau_disponible()` plus robuste (2-3 DNS + fallback HTTP 204 sur un endpoint stable, avec cache 30-60 s).
2. Ajouter un flag `reseau_ok` mis à jour périodiquement (thread ou événement) plutôt qu’un test unique par requête.
3. Allouer le budget de façon adaptative : 60-80 s en mode normal, 30-40 s en mode dégradé, avec possibilité de surcharge par provider dans routing.json.
4. Logger explicitement le passage en mode dégradé avec métrique (durée réseau KO) pour détection post-incident.

Ces ajustements renforcent la résilience sans complexifier excessivement le code.
