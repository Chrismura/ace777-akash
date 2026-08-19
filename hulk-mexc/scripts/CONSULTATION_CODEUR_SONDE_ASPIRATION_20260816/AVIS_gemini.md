# AVIS gemini (provider NVIDIA build.nvidia.com (100+ modeles), 166.4s)

**AVIS CONSULTATION CODEUR — SONDE ASPIRATION HULK**

---

### RÉPONSES AUX 5 QUESTIONS

1. **Fiabilité double lecture ~1s** : **Risquée mais acceptable en fail-open**. Sur small caps MEXC, le carnet peut se vider/remplir en <500ms. Un délai de 1s capture un mouvement réel, mais 2s augmente le bruit (spread qui s'élargit, annulations). **Délai optimal : 1.0s** (compromis signal/bruit). Timeouts fréquents → le fail-open est indispensable.

2. **Seuil 15%** : **Raisonnable comme valeur initiale**, mais à calibrer sur 2-3 jours de paper trading. Sur small caps, un mur de 200 USDT qui fond de 15% en 1s est un signal faible (carnet mince). ACE sur futures BTC a des murs 100× plus épais. **Proposer 20%** pour éviter les faux positifs, ajustable.

3. **Fail-open** : **Bon choix**. Une 2e lecture échouée ne doit pas bloquer une entrée déjà validée par `entry_gate()`. Le fail-closed pénaliserait les paires volatiles (les plus intéressantes).

4. **Entrée uniquement** : **Correct pour la v1**. La sortie anticipée sur aspiration SELL est une feature complexe (risque de sortie trop précoce sur un mur bid qui se reforme). À ajouter en v2, après validation de la fiabilité du signal.

5. **Coût API** : **Limiter aux paires en régime COOLING/IMPULSE** (prêtes à trader). 15 paires × 2 lectures × 3 cycles/min = 90 requêtes/min, proche des limites MEXC. Réduire à ~5 paires actives = 30 req/min, sûr.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Réserve** : Implémenter en mode observation (log uniquement, pas d'action sur `entry_gate`) pendant 48h, puis activer le boost tension seulement si le taux de signal correct > 60% (vérifiable via le paper trading).

**CONFIANCE : 72%**

---

### HYPOTHÈSES

1. Le carnet MEXC small caps est suffisamment liquide (>80 USDT de profondeur) pour qu'une chute de mur de 15% en 1s soit un signal exploitable.
2. Les timeouts API sont <5% des appels (sinon le fail-open dégrade la qualité du signal).
3. L'aspiration haussière (mur ask fond) corrèle avec une hausse de prix à 2-5 min sur ces paires.

---

### CE QUI CHANGERAIT L'AVIS

- **Basculement GO** : Si les logs montrent >60% de précision prédictive (aspiration BUY → prix monte) sur 48h.
- **Basculement NO-GO** : Si le taux de timeout >15% ou si les faux signaux (aspiration BUY suivie d'une baisse) dépassent 50%.

---

### AMÉLIORATIONS PROPOSÉES

1. **Ajouter un 3e point de mesure** (t+2s) pour confirmer la tendance du mur (évite les faux mouvements ponctuels).
2. **Pondérer l'aspiration par la taille absolue du mur** : un mur de 500 USDT qui fond de 15% est plus significatif qu'un mur de 80 USDT.
3. **Logger systématiquement** `drop_bid_pct`, `drop_ask_pct`, `side` et le prix à t+5min pour calibration future.

---

### SYNTHÈSE

Diagnostic : la double lecture est pertinente mais le seuil de 15% est trop sensible pour small caps. Actions : (1) implémenter en mode observation 48h, (2) calibrer le seuil à 20%, (3) limiter aux paires actives, (4) activer l'effet sur `entry_gate` après validation.
