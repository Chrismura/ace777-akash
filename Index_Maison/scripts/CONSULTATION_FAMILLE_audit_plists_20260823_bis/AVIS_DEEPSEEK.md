# AVIS DEEPSEEK (task deepseek.analyse · Mistral La Plateforme (essai gratuit) · 2026-08-23T11:56Z)

### VERDICT : GO-AVEC-RÉSERVES
### CONFIANCE : 85 %
### HYPOTHÈSES :
1. La règle « one-shot → pas de KeepAlive » est correcte et suffisante pour éviter les boucles infinies.
2. Le retrait de `KeepAlive` sur les jobs one-shot ne casse pas leur cadence, car `StartInterval` ou `StartCalendarInterval` assure le déclenchement régulier.
3. Le superviseur-core, avec sa boucle `while` interne, ne nécessite pas `KeepAlive` pour être relancé après un crash, car `StartInterval` assure la relance périodique.

### CE QUI CHANGERAIT L'AVIS :
- Découverte d'un job one-shot qui ne se relance pas après le retrait de `KeepAlive`.
- Identification d'un cas où `StartInterval` ou `StartCalendarInterval` n'assure pas la cadence attendue.
- Preuve que le superviseur-core ne se relance pas après un crash sans `KeepAlive`.

### AMÉLIORATION PROPOSÉE :
1. **Mécanisme de détection automatique** : Ajouter une vérification dans `veille_degradation.py` pour détecter les plists avec `KeepAlive` et un intervalle de déclenchement, afin d'éviter les boucles infinies.
2. **Documentation des règles de configuration** : Documenter explicitement les règles de configuration des plists pour éviter les erreurs futures.
3. **Tests de robustesse** : Ajouter des tests pour vérifier que les jobs one-shot se relancent correctement après le retrait de `KeepAlive`.

### SYNTHÈSE :
Les correctifs appliqués sont globalement adéquats et évitent les boucles infinies. Cependant, des mécanismes de détection et de documentation supplémentaires seraient bénéfiques pour assurer la robustesse du système. Les jobs one-shot conservent leur cadence, et le superviseur-core semble être correctement configuré.
