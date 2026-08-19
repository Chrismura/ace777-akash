# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 147.5s)

**AVIS CONSULTATION FAMILLE — 16/08/2026**

---

### RÉPONSES AUX 4 QUESTIONS

**1. TIER_B_POSITION_MULT=0.25**  
Raisonnable. 0.1 serait trop restrictif (rend la paire non pertinente pour un test paper), watch-only strict est une option valable mais moins informative. 0.25 = 5$ par trade, perte max théorique ~0.30$ (stop gapé ~12% sur 5$). Acceptable pour du paper trading.

**2. RIP_SELL_FRAC=0.50**  
GO pour vente unique à 50% au 1er franchissement. Les paliers (30% + 30%) ajoutent de la complexité et du risque de manquer la liquidité (spike peut être un one-shot). Pour du paper, la simplicité prime. Réévaluer après 10 signaux.

**3. RIP sur tier B**  
OUI, mais avec prudence. C'est LE cas d'usage du tier B (spike fort). Le sizing réduit (0.25) protège déjà. Si le spread est > 100 bps au moment du signal, le sell_trade doit être exécuté en limit (pas market) — sinon risque de slippage massif. À préciser dans le code.

**4. REENTRY_MAX=1 + cooldown 4h**  
Correct. Le cooldown de 2h était trop court (EDEL racheté 3× en chute). 4h + max 1 est un bon compromis. Attention : le compteur doit être reset après un gain (pas seulement après une perte) pour ne pas bloquer une paire redevenue saine.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Réserve** : le bloc 2 (pick_pairs) doit être implémenté en PRIORITÉ et vérifié au boot. C'est le bug racine (PAPER_PAIRS en dur). Sans lui, les blocs 1, 3, 4 ne font que limiter les dégâts sur des paires qui n'auraient jamais dû être tradées.

---

### CONFIANCE : **72%**

---

### HYPOTHÈSES

1. L'inventaire MEXC (tier) est fiable et à jour — sinon le filtre pick_pairs exclura des paires valides.
2. Le rip_pct (~2%) est un signal pertinent pour ces small caps — non vérifié sur historique long.
3. Le give-back (RED, CHIP) est dû à l'absence de vente partielle, pas à un problème de cible — hypothèse à confirmer.

---

### CE QUI CHANGERAIT L'AVIS

- **Bascule NO-GO** : si l'inventaire MEXC s'avère incohérent avec les spreads réels (QAIT à 327 bps classé A).
- **Bascule GO+** : si un backtest rapide sur les 10 dernières campagnes montre que le rip_pct aurait capturé ≥ 50% des gains manqués (RED, CHIP).

---

### AMÉLIORATIONS PROPOSÉES

1. **Ajouter un check spread au moment du buy()** : si spread > 100 bps, skip (même tier A) — protège contre les paires mal classées.
2. **Log systématique du tier et du spread à chaque buy/sell** — pour audit post-campagne.
3. **Après 10 trades avec les 4 blocs** : comparer le PnL vs. l'ancien système, et ajuster RIP_SELL_FRAC si besoin.

---

### SYNTHÈSE (5 lignes max)

Diagnostic : le système trade des paires illiquides (tier B) à pleine taille, sans vente partielle sur rebond, et avec re-entries trop fréquents. Ordre d'actions : (1) corriger pick_pairs (bloc 2), (2) implémenter le sizing tier B (bloc 1), (3) ajouter le rip (bloc 3), (4) borner les re-entries (bloc 4). Le RIP_SELL_FRAC=0.50 est un bon point de départ. Surveiller les 10 prochains trades pour valider.
