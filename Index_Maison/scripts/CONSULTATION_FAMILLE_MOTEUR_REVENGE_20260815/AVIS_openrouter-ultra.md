# AVIS openrouter-ultra (OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 32.2s)

### ANALYSE TECHNIQUE
Le couple « shock_inversion_stop (~80%) → revenge 1.5x » **forme une boucle de churn structurelle**, pas une stratégie de récupération. Preuves :  
1. Taux de revenge explose (58 % → 89 %) alors que le marché est *plus calme* (tension 0.13 vs 0.19-0.45) : le scout (BETA) se fait stopper en noise, le hunter (ALPHA) surenchère 1.5× dans le même bruit.  
2. PnL revenge *très* volatil (+51 / –3.6 / +0.9) sans corrélation avec le %revenge → distribution à queue lourde, espérance mathématique non démontrée positive.  
3. 84 % des sorties = `shock_inversion_stop` : le scout sort sur inversion brutale ; le hunter rentre *dans* l’inversion (même sens ? sens inverse ? **information insuffisante** sur le côté revenge vs côté scout). Si même sens → double exposition au mauvais moment ; si sens inverse → mean-reversion non prouvée.

### RISQUE / IMPACT — MÉTRIQUES MANQUANTES POUR TRANCHER
1. **PnL net par séquence complète** (BETA entry → BETA stop → ALPHA revenge entry → ALPHA exit) frais *inclus* (maker/taker + funding si hold > 8 h).  
2. **Hold moyen revenge vs normal** : si revenge tient 3× plus longtemps → risque de gap / funding / slippage sortie.  
3. **Répartition des raisons de sortie revenge** : `shock_inversion_stop` aussi dominant côté ALPHA ?  
4. **Taille moyenne position revenge vs normale** (vérifier le 1.5× réel après arrondi lot/step).  
5. **Corrélation PnL revenge / latence feed** (E-STALE) : le 15/08, 1032 E-STALE → le bot skippe, mais les 72 revenge du jour ont-ils été remplis *avant* ou *pendant* la dégradation ?

### PRIORITÉ INFRA vs MOTEUR
**E-STALE 1032 + E-PROC 75 = priorité absolue AVANT tout toucher au revenge.**  
- Feed lag 8-12 s > `tension_stale gate 800 ms` → BETA/ALPHA décident sur des prix « fantômes » → `shock_inversion_stop` artificiels → revenge déclenchés sur bruit de latence.  
- E-PROC 75 (vs 4) = workers qui meurent sous charge → ordres orphelins, doubles fills, risk-engine désynchronisé.  
Corriger le revenge *maintenant* serait optimiser sur des données corrompues.

---

VERDICT : **OUVRIR CHANTIER INFRA EN PREMIER** (stabiliser feed + workers), puis audit complet séquences BETA+ALPHA avant toute modification du paramètre `revenge_mult` ou de la liste `revenge_reasons`.  
CONFIANCE : 85 %  
HYPOTHÈSES :  
1. La hausse du %revenge est un artefact de latence (E-STALE), pas une décision de marché.  
2. Le PnL revenge +51 du 14/08 est un coup de chance (quelques gros winners) masquant une espérance négative.  
3. Le côté (long/short) du revenge est identique au scout → double exposition adverse.  
CE QUI CHANGERAIT L'AVIS : Preuve que le PnL net par séquence (frais込み) est > 0 sur 500+ séquences *hors jours de latence* ET que le hold revenge ≤ hold normal.  
AMÉLIORATION PROPOSÉE :  
1. **Freeze revenge** (flag `revenge_enabled=false`) le temps de corriger l’infra.  
2. Ajouter `latency_guard` : bloquer toute entrée (scout + hunter) si `tension_stale_age > 500 ms` ou `E-PROC > 10`.  
3. Instrumenter `sequence_id` (UUID partagé BETA→ALPHA) pour mesurer PnL net séquentiel en temps réel.

SYNTHÈSE : Boucle revenge = churn amplifié par latence feed (E-STALE 1032) ; PnL revenge non significatif statistiquement. **Ordre : 1) Corriger feed/workers (E-STALE/E-PROC), 2) Freeze revenge, 3) Auditer séquences complètes frais inclus, 4) Décider garder/supprimer/calibrer revenge.**
