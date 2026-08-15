# AVIS openrouter-juge (provider OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 21.5s)

**Technique**  
Le heartbeat appelé à chaque cycle scout (L1545) remet à zéro `ts_ms`. Comme la vérification du TTL (L1027) compare l’âge actuel à ce timestamp, l’âge ne dépasse jamais 20 s tant que le scout reste actif. Ainsi le mécanisme `stale_state` est neutralisé et le revenge reste armé en permanence ; ce n’est pas un symptôme mais la cause directe du bug.

**Risque/Impact**  
Le fix le plus sûr et le plus minimal consiste à ne rafraîchir le heartbeat que lorsque le scout n’est pas en état de perte fermée (ex. : `pnl_scout >= 0` ou pas de drapeau `revenge_armed`). Cela préserve le heartbeat pour les périodes normales tout en permettant au TTL de s’exécuter après une perte. Ce changement n’interfère pas avec les variables `cooldown_revenge` (L1091) ou `boost` (L1094), qui dépendent uniquement du flag de revenge et non du timestamp.

**Priorité**  
1. **Fix TTL/heartbeat** – élimine la source de pertes récurrentes et réduit la volatilité du PnL.  
2. **Gel du revenge** (désactiver temporairement le mode revenge) – mesure de secours si le fix ne peut être déployé immédiatement.  
3. **Infra (E‑STALE/E‑PROC)** – bien que critique (workers qui meurent, prix fantômes), ces symptômes sont en partie aggravés par le revenge perpétuel qui génère des trades erratiques ; résoudre le bug réduit la charge sur les workers et les erreurs de feed.

**VERDICT** : GO‑AVEC‑RÉSERVE (ouvrir un chantier correctif TTL/heartbeat, réserve : validation en environnement de test avec surveillance du revenge et des métriques workers)  
**CONFIANCE** : 85 %  
**HYPOTHÈSES** :  
1. Le heartbeat est appelé uniquement dans les cycles scout non‑pausés.  
2. Le PnL du scout est disponible au moment du heartbeat (ou un drapeau indiquant une perte fermée).  
3. Le désarmement du revenge basé sur le TTL n’est pas utilisé ailleurs que dans la décision de revenge.  

**CE QUI CHANGERAIT L’AVIS** :  
- Si des tests montrent que le heartbeat est également nécessaire pour d’autres mécanismes (ex. : détection de reconnexion) et que son conditionnement provoque des regressions.  
- Si les métriques E‑STALE/E‑PROC restent élevées même après le fix, indiquant un problème infra indépendant.  

**AMÉLIORATION PROPOSÉE** :  
1. Conditionner le heartbeat sur `pnl_scout >= 0` (ou absence de drapeau `revenge_armed`).  
2. Ajouter un compteur de revenge consécutif avec un plafond (ex. : max 3 tentatives) pour limiter l’exposition même si le TTL échoue.  
3. Mettre en place un watchdog qui relance les workers morts et alerte sur un taux élevé de `E‑STALE`.  

**SYNTHÈSE** (5 lignes max)  
Le heartbeat rafraîchi à chaque scout empêche le déclenchement du stale_state, laissant le revenge armé en permanence et générant des PnL extrêmement volatils. Le fix le plus sûr consiste à ne mettre à jour le timestamp que lorsque le scout n’est pas en perte fermée, préservant les autres fonctions tout restaurant le TTL de 20 s. Cette correction doit être déployée en priorité, suivie d’une surveillance des workers et, si nécessaire, d’un gel temporaire du revenge. Une validation en test confirmera l’absence de régressions infra.
