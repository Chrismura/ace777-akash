# AVIS codestral-latest (provider Mistral La Plateforme (essai gratuit), 2.3s)

**VERDICT** : GO-AVEC-RÉSERVE (réserve : délai et seuil à valider empiriquement).
**CONFIANCE** : 75 % (risque de surcharge API et de bruit sur small caps).
**HYPOTHÈSES** :
1. Les small caps MEXC ont des carnets volatils, mais l'aspiration capture des signaux utiles.
2. Le seuil 15% est trop élevé pour les petits marchés (ACE est calibré sur BTC futures).
3. Le fail-open est préférable pour éviter les fausses alertes sur des paires instables.

**CE QUI CHANGERAIT L'AVIS** :
- Si les tests montrent que l'aspiration génère trop de faux signaux ou des délais excessifs.
- Si le coût API devient critique (ex. : timeouts fréquents).

**AMÉLIORATION PROPOSÉE** :
1. Ajouter un filtre de stabilité : limiter l'aspiration aux paires avec une volatilité < X%.
2. Optimiser le délai (0.5s) et le seuil (10%) via backtest sur l'historique MEXC.
3. Ajouter un mode "aspiration passive" (lecture simple si le carnet est trop mince).

**SYNTHÈSE** :
L'aspiration est pertinente pour les small caps, mais le délai et le seuil doivent être ajustés. Prioriser les tests sur les paires les plus stables. Implémenter la spec avec les réserves mentionnées.
