# AVIS JUGE (task juge.tranche · Google Gemini · 2026-09-01T07:20Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 75 %
HYPOTHÈSES : 
1. Le PnL réalisé négatif (-6.24 USDT) est imputable au coût d'opportunité des filtres stricts (99.6% de SKIP) combiné à un échantillon de trades trop faible (40 trades) pour lisser la variance.
2. La divergence sémantique entre le runtime (0 bags) et le cockpit (15 bags) provient d'un héritage de nomenclature ACE/Vortex non nettoyé, sans impact direct sur l'exécution pure de Hulk mais toxique pour la supervision humaine.

CE QUI CHANGERAIT L'AVIS :
- Passage au VERDICT « NON » : Une dégradation du PnL paper en deçà de -15 USDT ou une persistance du taux de SKIP > 99.5% après 200 trades supplémentaires sans justification de liquidité.
- Passage au VERDICT « GO » : L'unification prouvée du contrat d'état runtime/cockpit et l'obtention d'un PnL paper positif sur un échantillon de 100 trades validé sans intervention manuelle.

AMÉLIORATION PROPOSÉE : 
Remplacement du fallback inline par une **bascule fail-safe explicite** : si le satellite est *stale* (> 60s), interdiction stricte de toute nouvelle entrée (mode *no-new-entries*) au lieu de multiplier les requêtes réseau. De plus, purger purement et simplement les profils de paires illiquides (comme EDEL) qui forcent des régimes `IMPULSE` non viables.

SYNTHÈSE (5 lignes max) :
Hulk tourne techniquement sur MEXC mais souffre d'un PnL négatif, d'un taux de SKIP excessif (99.6%) et d'une confusion sémantique persistante avec le cockpit. Le paper actuel est validé sous réserves strictes pour corriger ces incohérences d'affichage et de flux. Tout passage en live ou activation de Kelly/Cortana est formellement interdit en l'état actuel des métriques.
