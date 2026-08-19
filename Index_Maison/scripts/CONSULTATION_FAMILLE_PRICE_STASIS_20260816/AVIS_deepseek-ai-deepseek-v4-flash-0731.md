# AVIS deepseek-ai/deepseek-v4-flash-0731 (provider NVIDIA build.nvidia.com (100+ modeles), 97.7s) — remplaçant openrouter (juge/ultra HS)

**VERDICT : GO-AVEC-RÉSERVE**  
Implémenter le garde-fou `price_stasis` tel que spécifié, avec la réserve suivante : **le seuil de 1.0 bps/30s est trop strict pour le testnet calme** — il risque de bloquer quasi toutes les entrées BETA (le marché ne bouge pas assez). Recommandation : seuil à **0.5 bps/30s** en attendant des données réelles.

**CONFIANCE : 78%**

**HYPOTHÈSES :**  
1. Le testnet a une liquidité artificiellement basse → le prix figé est un artefact, pas un signal réel.  
2. Les 43% de fills flat sont bien dus à ce pattern (pas à un bug de spread ou de timing).  
3. Le check après toutes les gates ne dégrade pas la latence d’exécution (le calcul ruby est < 50ms).

**CE QUI CHANGERAIT L’AVIS :**  
- Si les logs montrent que les fills flat sont corrélés à des mouvements de prix > 1 bps sur 30s (donc le garde-fou ne les aurait pas bloqués).  
- Si le fix `last_loss_ts` du matin interagit mal avec le nouveau check (ex. double skip en cascade).

**AMÉLIORATION PROPOSÉE :**  
1. **Log enrichi** : ajouter `ref_px` et `p2` dans le CSV skip pour debug rapide.  
2. **Défaut TRUE** mais avec un **compteur dédié** dans le rapport (ex. `price_stasis_skips`) pour surveiller le taux de blocage.  
3. **Exception tension** : si `tension > 15` (très haute), autoriser l’entrée même si prix figé — car un mur qui fond sans mouvement de prix peut précéder une cassure violente.

**SYNTHÈSE :**  
Le diagnostic le plus probable est un marché testnet sans liquidité → le radar détecte des signaux de carnet non confirmés par le prix. Implémenter le garde-fou avec seuil 0.5 bps/30s, défaut TRUE, compteur dédié. Surveiller le taux de skip sur 24h avant d’ajuster.
