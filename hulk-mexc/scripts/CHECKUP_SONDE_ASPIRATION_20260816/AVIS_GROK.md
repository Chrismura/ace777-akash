# AVIS GROK (provider NVIDIA build.nvidia.com (100+ modeles))

1. **VERDICT** : **GO AVEC RÉSERVES** — le code est propre, fail-open correct, spoof bien pensé. Réserves : le seuil spoof à 15%/s est arbitraire, et le mode observation ne vérifie pas si l'aspiration prédit le mouvement réel du prix.

2. **ANGLES MORTS** :
   - **Spoof mal détecté** : tu compares le mur entre 2 lectures, mais un mur qui fond puis se reconstruit entre les 2 lectures (spoof rapide < 0.5s) passe inaperçu. Il faudrait 3 lectures espacées de 0.2s pour attraper ça.
   - **Rate-limit MEXC** : `ASPIRATION_PROBE_EVERY=3` avec 5 paires = 10 appels API par probe (2 lectures × 5 paires). Sur 1h = ~1200 appels. MEXC limite à 20 req/s — OK, mais si tu passes à 10 paires, ça devient limite.
   - **CSV non protégé** : si le fichier est ouvert par un autre process (Excel, tail), `open("a")` peut lever une exception et tuer le probe. Pas de try/except autour du write.

3. **AMÉLIORATION GO-SIZED** : Ajoute un champ `price_delta_pct` dans le retour de `aspiration_sense()` — compare le prix entre d1 et d2. Ça permet de corréler l'aspiration avec le mouvement réel du prix dans le CSV de calibration. En 48h, tu sauras si une aspiration BUY avec drop_ask > 5%/s prédit réellement un move haussier.

4. **CLAUSE PERMANENTE — AUTRE CHOSE** : Au lieu de sonder uniquement les paires en COOLING/IMPULSE, ajoute un mode **"aspiration opportuniste"** : quand une paire en régime CALM montre un spread qui se resserre brutalement (< 50% de sa moyenne mobile sur 20 échantillons), déclenche une sonde aspiration immédiate. Les murs se construisent souvent AVANT le régime IMPULSE — tu capturerais l'aspiration au moment où elle se forme, pas après. C'est un ajout de ~15 lignes dans `probe_aspiration()`, et ça transforme la sonde de réactive en proactive.
