# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 118.8s)

**AVIS FAMILLE — price_stasis**

---

### RÉPONSES AUX 4 QUESTIONS

1. **Seuils 1.0 bps / 30s** : **Raisonnables** pour un testnet calme. Sur BTC actif, 1 bps/30s est très bas (≈ 0.03 bps/s), donc le filtre ne bloquera pas les vrais mouvements. Sur testnet figé, il attrapera bien les périodes mortes. **GO sur ces valeurs.**

2. **Défaut TRUE** : Oui, **TRUE**. Le constat terrain (43% de fills flat) justifie une sécurité active par défaut. Le coût d'un faux positif (skip d'un trade potentiel) est bien inférieur au coût des frais + bruit sur 43% des trades.

3. **Compteur dédié** : Oui, **métrique dédiée** dans le rapport. Un skip `price_stasis` n'est pas un skip classique (pas un signal faible, mais un signal invalide). Le compter séparément permet de mesurer l'efficacité du garde-fou et d'ajuster les seuils.

4. **Exception wall collapse** : **Non, pas d'exception.** Un mur qui fond sans mouvement de prix = liquidité illusoire (c'est exactement le pattern observé). Si la tension est très haute ET le prix bouge, le garde-fou laisse passer. Si le prix ne bouge pas, c'est que le mur n'était pas réel. L'exception créerait une faille.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Réserve** : Le garde-fou est correct, mais il ne traite que le symptôme (prix figé). La cause racine est que le radar détecte des signaux de carnet sur un marché sans liquidité. Le `price_stasis` doit être un **filet de sécurité temporaire**, pas la solution finale.

---

### CONFIANCE : **82 %**

---

### HYPOTHÈSES

1. Le testnet reste calme (peu de liquidité) sur les prochains runs → le garde-fou sera activement sollicité.
2. Les 8 fills flat observés sont bien dus à un prix figé, pas à un problème de latence ou de spread.
3. Le coût d'un skip (opportunité manquée) est inférieur au coût des frais + bruit des trades nuls.

---

### CE QUI CHANGERAIT L'AVIS

- **Basculement NO-GO** : Si on découvre que les fills flat sont dus à un problème d'exécution (ordre non rempli, slippage), pas au prix figé → le garde-fou serait inutile.
- **Basculement GO sans réserve** : Si le run de nuit montre que le garde-fou élimine > 80% des fills flat sans réduire le nombre de trades gagnants.

---

### AMÉLIORATIONS PROPOSÉES

1. **Ajouter un log de diagnostic** : quand `price_stasis` skip, logger aussi `bid_drop` et `tension` pour corréler (permet de vérifier si le skip est bien lié aux murs fondus).
2. **Après 3 skips consécutifs `price_stasis`**, passer en mode "veille" (pause radar 60s) pour éviter de tourner en boucle sur un marché mort.
3. **À terme** : ajouter une condition de liquidité minimale (volume 1m > seuil) en amont du radar, pour ne plus dépendre du garde-fou.

---

### SYNTHÈSE (5 lignes max)

Diagnostic : le radar détecte des signaux de carnet sur un marché sans mouvement de prix → trades nuls. Action : implémenter `price_stasis` en défaut TRUE avec 1.0 bps/30s, métrique dédiée, sans exception. Surveiller le ratio de skips sur 24h pour ajuster les seuils. En parallèle, investiguer la liquidité réelle du testnet pour traiter la cause racine. Le fix `last_loss_ts` n'est pas impacté.
