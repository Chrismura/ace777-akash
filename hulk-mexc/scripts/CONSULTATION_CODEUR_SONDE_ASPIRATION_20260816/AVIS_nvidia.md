# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 88.4s)

**ANALYSE (5 questions)**

1. **Fiabilité double lecture ~1s** : Sur small caps MEXC, le carnet peut bouger en <500ms. Un délai de 1s est un compromis raisonnable mais risque de rater des micro-mouvements. 0.5s serait plus réactif mais augmente le risque de timeout. **Recommandation : 1s est acceptable, 0.5s si les timeouts restent <5%.**

2. **Seuil 15%** : Pour du small caps avec murs souvent <500 USDT, une chute de 15% en 1s est significative mais pas rare. ACE utilise un seuil plus bas (~10%) sur futures BTC. **15% est prudent, mais envisager 10-12% pour capter plus de signaux.**

3. **Fail-open** : Correct. Une 2e lecture échouée ne doit pas bloquer une entrée potentielle. Le fail-closed serait trop restrictif sur un marché volatil.

4. **Entrée seulement** : Insuffisant. L'aspiration SELL (mur bid fond) sur une position ouverte est un signal de sortie anticipée précieux. **À intégrer en sortie si le moteur évolue.**

5. **Coût API** : +15 lectures/cycle = +45 lectures/min (vs 15 actuellement). MEXC tolère ~200 req/min. **Acceptable, mais limiter aux paires en régime COOLING/IMPULSE est plus efficace.**

---

**VERDICT : GO-AVEC-RÉSERVE**  
Réserve : implémenter en sortie également (question 4) et ajuster le seuil à 12% après backtest.

**CONFIANCE : 72%**

**HYPOTHÈSES :**
- Le carnet MEXC small caps est suffisamment liquide pour que les murs soient significatifs (>80 USDT).
- La double lecture à 1s ne génère pas de timeouts >10% des appels.
- L'aspiration est corrélée aux mouvements de prix à 2-5 minutes.

**CE QUI CHANGERAIT L'AVIS :**
- Si les timeouts dépassent 15% en test → passer à 2s ou fail-closed.
- Si le backtest montre que l'aspiration n'améliore pas le win rate → NO-GO.
- Si MEXC rate-limite les appels → limiter aux paires actives.

**AMÉLIORATIONS PROPOSÉES :**
1. **Backtest offline** : Rejouer 48h de données historiques pour valider le seuil de 15% avant déploiement.
2. **Sortie anticipée** : Si drop_bid > 20% sur position ouverte → déclencher sortie partielle (25%).
3. **Délai adaptatif** : 0.5s si spread < 30bps, 1.5s si spread > 50bps (carnet plus lent).

---

**SYNTHÈSE** : L'aspiration est pertinente mais doit servir à l'entrée ET la sortie. Implémenter en mode test sur 3 paires pendant 24h, valider le seuil, puis généraliser. Coût API acceptable.
