# AVIS gemini (provider Google Gemini, 3.7s)

### 1. Réponses aux 4 questions

1. **TIER_B_POSITION_MULT=0.25 :** Raisonnable. À 0.10 (2$), les frais de transaction fixes sur MEXC risquent de ronger toute marge sur les small caps illiquides. 0.25 (5$) offre un compromis sain entre exposition au risque de spread et viabilité du test paper trading.
2. **RIP_SELL_FRAC=0.50 au 1er franchissement :** Suffisant pour l'état actuel du système. La vente par paliers complexifie la logique de gestion des états (tracking de multiples niveaux de rip) alors que le bug critique actuel est l'absence totale de prise de profit sur les rebonds court terme.
3. **Application du rip aux tier B :** Oui, à condition que le sizing réduit (0.25) soit actif. Les tier B spikent fort mais ont des spreads élevés ; sécuriser 50% de la position dès le premier rebond protège contre les retours de bâton constatés sur RIZE et EDEL.
4. **REENTRY_MAX=1 + cooldown 4h :** Bons et nécessaires. Le comportement précédent (racheter 3 fois d'affilée une position en chute libre comme EDEL) était une aberration logique sur un système de dip&rip court terme.

---

### VERDICT & ÉVALUATION

* **VERDICT :** GO-AVEC-RÉSERVE (Réserve : valider que `PAPER_EXTRA_PAIRS` est explicitement initialisé dans la config pour éviter un blocage total au boot si `PAPER_PAIRS` filtre trop agressivement).
* **CONFIANCE :** 90 %
* **HYPOTHÈSES :** 
  1. L'API MEXC supporte correctement les ventes partielles (`sell_trade` avec `SELL_PARTIAL`) sans désynchroniser le calcul du stop.
  2. Le compteur `REENTRY_MAX` est correctement réinitialisé ou purgé en fin de cycle de vie de la paire pour ne pas bloquer définitivement le trading sur une valeur après plusieurs jours.
* **CE QUI CHANGERAIT L'AVIS :** La découverte que le spread moyen des paires Tier B dépasse systématiquement le `rip_pct` visé, rendant toute sortie par rip mathématiquement impossible en net de frais.
* **AMÉLIORATION PROPOSÉE :** 
  1. Ajouter un filtre de spread maximal (ex: rejeter l'achat si spread > 50 bps, comme observé sur RIZE à 59 bps).
  2. Implémenter un timeout global sur les bags pour éviter l'enlisement du capital au-delà de l'horizon de la classe.

---

### SYNTHÈSE
Le système souffre d'une fuite de capital chronique sur les small caps illiquides (Tier B) due à un sizing inadapté, une absence de prise de profit sur les rebonds (`rip_pct`), et un acharnement en re-entry. Les 4 blocs de la spec corrigent directement ces failles béantes. **Ordre des actions :** 1. Fixer le sizing Tier B ; 2. Activer le filtre d'inventaire pick_pairs ; 3. Implémenter le take-profit sur rip ; 4. Encadrer strictement le re-entry.
