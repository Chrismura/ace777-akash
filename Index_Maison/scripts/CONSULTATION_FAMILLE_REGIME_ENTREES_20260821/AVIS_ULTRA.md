# AVIS ULTRA (task inferx.analyse · Google Gemini · 2026-08-21T10:27Z)

VERDICT : GO-AVEC-RÉSERVES  
CONFIANCE : 95 %  

### HYPOTHÈSES
1. **La lecture IRM est exacte mais désynchronisée de l'exécution** : Le moteur évalue le marché en aval ou utilise un seuil d'activation statique qui se déclenche par défaut sur le bruit du régime COMPRESSÉ faute de gating actif.
2. **L'asymétrie des frais tue l'edge structurel** : Avec 88,5 % du temps passé en régime mort, le moteur agit en "market maker" subi ou en scalpeur à micro-marge qui paie le taker/maker sans capturer le déplacement directionnel.
3. **Le faux win rate brut cache un piège de liquidité** : Les sorties par `shock_inversion_stop` à 0-2 bps prouvent que le moteur entre dans le carnet sans profondeur et se fait aspirer par le spread dès le premier micro-souffle.

### CE QUI CHANGERAIT L'AVIS
- La démonstration que les régimes TRANSITOIRE et CLUSTER sont en réalité des zones de slippage massif où le PnL net serait pire à cause de la volatilité.
- Une preuve que la latence d'exécution rend impossible le filtrage par régime en temps réel sans rater les rares mouvements viables.

### AMÉLIORATION PROPOSÉE (Clause permanente)
1. **Gate d'entrée binaire couplée à un budget de volatilité dynamique (Recommandé)** : Interdire tout nouvel ordre si l'indicateur IRM est en régime COMPRESSÉ, mais *en plus*, exiger un seuil d'énergie minimale (Order Flow Imbalance > X) pour autoriser l'entrée en TRANSITOIRE, évitant ainsi le piège d'attendre le bon régime sans volume.
2. **Refonte de la mécanique de sortie (Trailing adaptatif au lieu du Shock Exit)** : Remplacer le `shock_inversion_stop` nerveux par un trailing stop basé sur l'ATR (Average True Range) pour laisser courir les gains au-delà du seuil de rentabilité des frais de 15 bps, plutôt de couper à 0-2 bps.

### SYNTHÈSE
Le diagnostic est irréfutable : ACE777 subit une hémorragie de frais en tradant un marché mort (88,5 % en COMPRESSÉ) avec un edge brut quasi nul. Appliquer un filtre d'entrée sur les régimes TRANSITOIRE/CLUSTER est indispensable mais insuffisant sans revoir la politique de sortie et de frais. Le statut quo conduit à la ruine certaine du capital par attrition lente. Valider le gating d'entrée en testnet strict avant tout déploiement sur le champion `64fb153f`.
