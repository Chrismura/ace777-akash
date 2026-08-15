# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 159.2s)

**ANALYSE**

**• Technique**  
Oui, le couple L1545 + L1027 neutralise le `stale_state` : le heartbeat rafraîchit `ts_ms` à chaque cycle scout, donc `age` reste toujours < 20s. Le revenge devient quasi-permanent.  
C'est **le bug dominant** (cause racine), pas un symptôme : il explique la montée du %revenge (71→89%) et la volatilité du PnL ALPHA (le revenge s'active sur des signaux périmés, y compris sur des pertes déjà consommées).  
Le `shock_inversion_stop` élevé (68-84%) est cohérent : ALPHA entre en revenge sur des états de tension obsolètes, puis sort immédiatement en inversion.

**• Risque/Impact**  
Fix le plus sûr et minimal : **ne rafraîchir `ts_ms` que si l'état scout est en pnl >= 0** (ou ne pas toucher `ts_ms` après une perte fermée). Cela préserve le heartbeat pour les trades sains, mais laisse vieillir les pertes → `stale_state` se déclenche après 20s.  
Risque de casse : le TTL est utilisé par `cooldown_revenge` (L1091) et `boost` (L1094) ? **Information insuffisante** — le code exact de ces lignes n'est pas fourni. Si ces mécanismes lisent `ts_ms` pour d'autres décisions, un fix ciblé (condition pnl) est plus sûr qu'un retrait global du heartbeat.  
Un fix du TTL seul (ex. augmenter à 60s) ne résout pas le problème : il retarde l'échéance mais ne désarme pas le revenge sur états périmés.

**• Priorité**  
1. **Geler le revenge** (désactiver ALPHA revenge) immédiatement — risque de pertes continues sur signaux périmés.  
2. **Fix TTL/heartbeat** (condition pnl >= 0) — chantier correctif ciblé, testable en testnet.  
3. **Infra** (E-STALE/E-PROC) — important mais secondaire : le bot décide sur prix fantômes, mais le fix TTL réduit déjà l'exposition à ces états.

---

**VERDICT** : **GO-AVEC-RÉSERVE**  
Réserve : le fix doit être conditionnel (pnl >= 0) et non un retrait global du heartbeat ; vérifier l'impact sur `cooldown_revenge` et `boost` avant déploiement.

**CONFIANCE** : 82 %

**HYPOTHÈSES**  
1. Le heartbeat L1545 est exécuté à chaque cycle scout non-pausé, sans condition de pnl.  
2. `cooldown_revenge` et `boost` ne dépendent pas de `ts_ms` de manière critique (sinon fix à adapter).  
3. Les E-STALE (1032) sont corrélés aux entrées revenge sur prix fantômes, mais le fix TTL réduira leur impact.

**CE QUI CHANGERAIT L'AVIS**  
- Si le code de L1091/L1094 montre que `ts_ms` est utilisé pour d'autres décisions (cooldown, boost) → basculer en NO-GO tant que le fix n'est pas adapté.  
- Si les E-STALE proviennent d'une source indépendante du heartbeat (ex. feed tension) et non des entrées revenge → priorité infra remonte, mais le fix TTL reste nécessaire.

**AMÉLIORATION PROPOSÉE**  
1. Ajouter un flag `last_loss_ts` dans le duo_state, mis à jour à chaque perte scout ; le TTL revenge compare `age` à ce timestamp, pas à `ts_ms`.  
2. Logger systématiquement `age` et `reason` à chaque décision revenge pour monitorer l'efficacité du fix.  
3. Ajouter un kill-switch manuel (variable d'env) pour désactiver le revenge sans redéploiement.

---

**SYNTHÈSE**  
Le heartbeat L1545 neutralise le TTL 20s → revenge quasi-permanent, expliquant la hausse du %revenge et la volatilité PnL. Action immédiate : geler le revenge. Ensuite : fix conditionnel (pnl >= 0) sur le heartbeat, testé en testnet. Infra (E-STALE/E-PROC) traitée en parallèle mais non bloquante.
