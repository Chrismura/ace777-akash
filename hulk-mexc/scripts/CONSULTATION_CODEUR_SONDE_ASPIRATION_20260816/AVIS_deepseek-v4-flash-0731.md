# AVIS deepseek-ai/deepseek-v4-flash-0731 (provider NVIDIA build.nvidia.com (100+ modeles), 90.1s)

**AVIS CONSULTATION CODEUR — SONDE ASPIRATION HULK**

---

### RÉPONSES AUX 5 QUESTIONS

1. **Fiabilité double lecture ~1s** : Risquée sur small caps MEXC. Le carnet peut bouger de 10-20% en 1s sur ces paires. Un délai de **0.5s** est plus adapté (compromis entre pertinence et coût). Timeouts fréquents → fail-open obligatoire.

2. **Seuil 15%** : **Raisonnable** pour small caps. ACE utilise ~10-20% selon volatilité. Sur MEXC spot, un mur qui fond de 15% en 0.5s est un signal fort. Ne pas descendre sous 10% (faux positifs).

3. **Fail-open** : **Bon choix**. Une lecture simple vaut mieux que rien. Le fail-closed bloquerait toutes les entrées en cas de timeout réseau (fréquent sur MEXC).

4. **Entrée + Sortie** : **Entrée d'abord, sortie ensuite**. L'aspiration SELL sur position ouverte est un signal de sortie anticipée précieux. Mais l'intégrer maintenant complexifie le moteur. Prioriser l'entrée, ajouter la sortie en V2.

5. **Coût API** : **Limiter aux paires en régime COOLING/IMPULSE**. 15 paires × 2 lectures = 30 appels/cycle → risque de rate-limit MEXC. Filtrer d'abord par tension_score() > seuil, puis aspiration uniquement sur les candidates.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Réserve** : Implémenter avec délai 0.5s (pas 1s), limiter aux paires pré-filtrées par tension, et NE PAS intégrer la sortie anticipée dans cette version.

**CONFIANCE : 78%**

---

### HYPOTHÈSES

1. Le carnet MEXC small caps est suffisamment liquide (>80 USDT) pour que les murs soient significatifs sur 0.5s.
2. La latence réseau (appel HTTP) est <200ms, sinon la double lecture mesure du bruit.
3. Le rate-limit MEXC permet 30 lectures/20s sans blocage (à vérifier).

---

### CE QUI CHANGERAIT L'AVIS

- **Basculement NO-GO** : Si les tests montrent que >30% des double lectures échouent (timeout) ou que le drop moyen sans signal est >15% (bruit).
- **Basculement GO plein** : Si le backtest sur 48h montre que side=BUY avec drop>15% précède une hausse >2% dans les 5 min.

---

### AMÉLIORATIONS PROPOSÉES

1. **Délai adaptatif** : 0.5s si spread <50bps, 1s si spread >50bps (carnet plus stable).
2. **Triple lecture** : 3 lectures à 0.3s d'intervalle, prendre la médiane des drops (filtre le bruit).
3. **Logging systématique** : Journaliser drop_bid/drop_ask par paire pendant 48h pour calibrer le seuil réel.

---

### SYNTHÈSE

Diagnostic : la double lecture est pertinente mais le délai 1s est trop long pour small caps MEXC. Implémenter en GO-AVEC-RÉSERVE avec 0.5s, filtrage par tension préalable, et sortie anticipée en V2. Calibrer le seuil 15% sur données réelles avant activation complète.
