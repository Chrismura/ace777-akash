# AVIS gemini (provider Google Gemini, 4.9s)

**1. Technique**
* **Confirmation du bug :** Oui, la contradiction est formelle et avérée. `duo_touch_heartbeat` (appelé à chaque cycle scout L1545) écrase en permanence `ts_ms` avec l'horodatage courant. Par conséquent, l'âge calculé à la ligne 1026 (`age = now - ts_ms`) est toujours quasi-nul (< 1 seconde). La condition `age > ttl*1000` (20s) n'est mathématiquement jamais remplie, ce qui rend le TTL inopérant et laisse le mode *revenge* armé en permanence.
* **Bug dominant ou symptôme ?** C'est le **bug logique dominant** du moteur de décision ACE777. Il explique directement pourquoi le taux de *revenge* d'ALPHA reste anormalement élevé (jusqu'à 89% le 15/08) alors que le marché se calme. Cependant, il est aggravé par un **symptôme infra critique** : l'apparition massive d'erreurs `E-STALE` (1032 occurrences) liée à un feed de tension qui lag (8-12s). Le bot prend donc des décisions *revenge* permanentes sur des prix et des tensions fantômes.

**2. Risque / Impact**
* **Le fix le plus sûr et minimal :** Dissocier le heartbeat de l'état de perte. Ne plus appeler `duo_touch_heartbeat` lorsqu'un signal de perte scout est actif ou enclenché (ex. ne rafraîchir `ts_ms` que si le dernier PnL scout est $\ge 0$ ou si l'état n'est pas en phase de déclenchement *revenge*).
* **Impact sur les autres mécanismes :** Modifier imprudemment le TTL ou le heartbeat risque de casser le `cooldown_revenge` (L1091) et les multiplicateurs de boost (L1094) si ces derniers dépendent de la même horodatage `ts_ms`. C'est pourquoi un fix chirurgical ciblant uniquement l'actualisation de `ts_ms` lors des pertes est préférable pour ne pas perturber les timers de cooldown.

**3. Priorité**
1. **Urgence Absolue (Infra) :** Traiter les `E-STALE` (feed de tension) et `E-PROC` (workers qui meurent) avant toute modification logique. Un correctif logique sur un bot qui tourne sur des données de tension avec 12s de retard mènera directement au crash.
2. **Secondaire (Logique) :** Appliquer le fix minimal sur `duo_touch_heartbeat` pour réactiver le TTL de 20s du *revenge*.
3. **Tertiaire (Sécurité) :** Gel temporaire du *revenge* tant que l'intégrité infra et le correctif du TTL ne sont pas validés en testnet.

---

* **VERDICT :** GO-AVEC-RÉSERVE (sur « ouvrir un chantier correctif TTL/heartbeat », avec réserve absolue de geler le trading en live et de traiter d'abord les E-STALE/E-PROC).
* **CONFIANCE :** 95 %
* **HYPOTHÈSES :** 
  1. Le code du genesis fourni est l'exact reflet du comportement en production.
  2. L'explosion des `E-STALE` (1032) fausse la pertinence des métriques PnL du 15/08 en raison de décisions prises sur des données obsolètes.
* **CE QUI CHANGERAIT L'AVIS :** La preuve que `duo_touch_heartbeat` est contourné par une autre condition non visible dans l'extrait, ou que les `E-STALE` ont une origine purement cosmétique (ce qui est peu probable vu les 75 crashs workers E-PROC).
* **AMÉLIORATION PROPOSÉE :** 
  1. Conditionner `duo_touch_heartbeat` à une validation de fraîcheur du feed de tension (`tension_stale < 800ms`).
  2. Isoler la variable de temps du *revenge* (`ts_revenge_start`) de celle du heartbeat général (`ts_ms`).

---

**SYNTHÈSE :** 
Le rafraîchissement continu de `ts_ms` par le heartbeat scout (L1545) invalide définitivement le TTL de 20s, verrouillant ALPHA en mode *revenge* permanent. Couplé à l'explosion des `E-STALE` (feed de tension obsolète) et des crashs workers (`E-PROC`), le système opère à l'aveugle. L'ordre des actions impératif est : stopper le bot, corriger l'infrastructure (feed de tension/workers), puis découpler le heartbeat du statut de perte pour réactiver le TTL du *revenge*.
