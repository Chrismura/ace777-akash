# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 35.0s)

**TECHNIQUE**  
Oui, confirmation formelle : `duo_touch_heartbeat` (L1545) met à jour `ts_ms` à **chaque cycle scout** (≈ 100-200 ms), donc `age` (L1027) reste < 20 s en permanence. Le garde-fou `stale_state` est **neutralisé par construction** ; le revenge reste armé indéfiniment tant que le scout tourne. C’est le **bug dominant** (cause racine), pas un symptôme : il explique la montée continue du %revenge (71 % → 89 %) alors que le marché se calme.

**RISQUE / IMPACT**  
Fix le plus **sûr & minimal** : **ne plus rafraîchir `ts_ms` si le dernier événement scout est une perte close** (stop_loss, shock_*, fluid_*, sentinel_cut).  
- Implémentation : dans `duo_touch_heartbeat_force`, lire `j["last_outcome"]` (ou champ équivalent) ; si `outcome == "loss"` → `return` sans `ts_ms=now`.  
- Effet : `ts_ms` fige à l’instant de la perte → TTL 20 s redevient opérant → revenge auto-désarmé après 20 s sans trade scout gagnant.  
- **Aucune cassure** : `cooldown_revenge` (L1091) et `boost` (L1094) ne lisent **jamais** `ts_ms` ; ils utilisent leurs propres timestamps. Risque de régression ≈ 0.

**PRIORITÉ**  
1. **Fix TTL/heartbeat** (blocage structurel du revenge, PnL volatil, exposition x13 non bornée).  
2. **Infra E-STALE/E-PROC** (feed lag 8-12 s + workers qui meurent) : critique pour la qualité d’exécution, mais **secondaire** tant que le revenge tire en aveugle sur des prix fantômes.  
3. **Gel du revenge** (flag d’urgence) : seulement si le fix 1 ne peut pas être déployé < 2 h.

---

**VERDICT : GO-AVEC-RÉSERVE** (réserve : déployer le fix heartbeat *avant* la prochaine session ; si impossible → gel revenge immédiat)  
**CONFIANCE : 92 %**  
**HYPOTHÈSES**  
1. Le heartbeat continu est une régression introduite pour « éviter stale_state entre trades scout » (commentaire L875), mais le dev a oublié le cas « perte close ».  
2. Les 1032 E-STALE d’aujourd’hui amplifient la casse : le revenge décide sur des prix 8-12 s en retard → PnL erratique.  
3. Le pic PnL +51 $ du 14/08 est un coup de chance (revenge aligné par hasard) ; l’espérance mathématique reste négative (shock_inversion_stop 68-84 %).

**CE QUI CHANGERAIT L’AVIS**  
- Preuve que `ts_ms` sert *aussi* à un autre garde-fou critique (ex. risk-engine global) → audit croisé obligatoire.  
- Mesure showing que le fix heartbeat fait chuter le %revenge < 10 % en shadow-mode → confirmation que le TTL redevient opérant.

**AMÉLIORATION PROPOSÉE**  
1. Patch `duo_touch_heartbeat_force` : `return if j["last_outcome"] == "loss"` (1 ligne, 0 risque).  
2. Ajouter métrique `revenge_ttl_expired_count` pour valider le fix en prod.  
3. Parallèle : corriger la source E-STALE (buffer/timeout feed) pour arrêter les décisions sur prix fantômes.

---

**SYNTHÈSE**  
Le heartbeat continu annule le TTL 20 s → revenge armé en permanence → exposition x13 non bornée sur pertes scout. Fix minimal : geler `ts_ms` sur perte close. Priorité absolue avant toute reprise ; infra E-STALE/E-PROC à traiter dans la foulée.
