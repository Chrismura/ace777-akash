# AVIS JUGE (task juge.tranche · Google Gemini · 2026-08-29T18:40Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %
HYPOTHÈSES :
1. La fenêtre de 24h lisse excessivement les chocs de liquidité brusques propres aux small caps ACE777 (ZBCN, PYTH), créant un retard de phase opérationnel.
2. Une plage horaire fixe (UTC 02-06) constitue un angle mort institutionnel rigide, contournable par une activation pilotée par la baisse relative du volume panier.
3. La synchronisation inter-paires de Cortana (corrélation croisée lourde) est sur-ingéniérée pour l'état actuel de notre infrastructure et générerait de la latence inutile.

CE QUI CHANGERAIT L'AVIS :
Un rapport de l'observatoire montrant que l'hybridation EWMA/24h augmente le taux de faux positifs de plus de 20% sur les faux murs des small caps en régime calme.

AMÉLIORATION PROPOSÉE :
1. **Hybridation asymétrique du seuil de spread (Critique A) :** Combiner le p30_24h (amortisseur anti-bruit) avec un p30_4h ou une EMA courte pour capter les accélérations subites sans sacrifier la stabilité.
2. **Déclencheur de volume glissant (Critique B) :** Remplacer définitivement la plage UTC 02-06 par un déclencheur dynamique : si le volume panier chute de $\ge 60\%$ par rapport à la MM24h sur une fenêtre glissante de 3h, l'élargissement s'active.
3. **Compteur d'essaim léger (Critique C) :** Écarter la matrice croisée complexe de Cortana et la remplacer par un simple compteur booléen (si $\ge 3$ small caps affichent un $CV \le 15\%$ simultanément, appliquer un malus macro global de $+0.20$ au SAPI).

SYNTHÈSE :
Cortana a raison sur la rigidité des fenêtres temporelles (24h et UTC 02-06) qui créent des angles morts sur nos small caps. Valider le code actuel (14/14) mais injecter immédiatement l'hybridation EWMA 4h/24h et le déclencheur de volume glissant 3h. Rejeter la matrice de corrélation lourde au profit d'un compteur d'essaim minimaliste.
