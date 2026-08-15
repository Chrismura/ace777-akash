# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 28.6s)

**ANALYSE TECHNIQUE**  
Chemin VORTEX : la garde `VORTEX_JSON_MAX_AGE_SEC` (valeur non fournie, mais typiquement ≥ 1–5 s) est **largement supérieure** à la latence observée en alpage (quelques centaines de ms). Le trou de fraîcheur est **inexistant** pour le run test ; le mécanisme « pas de gate tension_stale » est sûr ici.  
Chemin NUAGE : le seuil **fixe 800 ms** est **trop bas** pour du WiFi/4G instable (pics > 1 s fréquents). Les 1 811 `tension_stale` (1–8 % des skips) sont des **faux positifs** : la tension est fraîche, mais le paquet arrive après 800 ms. Le bot « s'endort » par prudence excessive, pas par absence de signal.

**RISQUE / IMPACT**  
Garder le skip prudent (800 ms) = **sécurité maximale, occasions manquées** (spreads serrés non joués en marché calme).  
Gate **adaptative** (ex. `max(800 ms, 3 × médiane_derniers_100_ts)` ou EMA latence) = **dégradation gracieuse** : on joue si la latence est « dans la norme du moment », on skip seulement si elle dérive anormalement. Requis pour « vivre sur WiFi/alpage » sans sacrifier l'alpha.

**PRIORITÉ**  
1. Heartbeat corrigé → **fait**.  
2. **Chantier robustesse latence NUAGE** (gate adaptative + métriques latence continue).  
3. Vérifier `VORTEX_JSON_MAX_AGE_SEC` (info manquante) et l’aligner sur la même logique adaptative par cohérence.  
4. Replay historique NUAGE avec gate adaptative pour quantifier le gain d’occasions vs risque.

---

VERDICT : GO-AVEC-RÉSERVE (ouvrir chantier robustesse latence : gate adaptative NUAGE + métriques ; vérifier Vortex)  
CONFIANCE : 85 %  
HYPOTHÈSES :  
1. `VORTEX_JSON_MAX_AGE_SEC` ≥ 2 s (sinon Vortex devient fragile).  
2. La latence alpage suit une distribution à queue lourde (pics > 1 s réguliers).  
3. Le marché calme (15/08) masque le coût d’opportunité des skips 800 ms.  
CE QUI CHANGERAIT L'AVIS :  
• `VORTEX_JSON_MAX_AGE_SEC` < 1 s → NO-GO Vortex.  
• Preuve que les 1 811 skips NUAGE correspondent à de vraies tensions périmées (pas latence) → garder 800 ms.  
AMÉLIORATION PROPOSÉE :  
1. Remplacer `NUAGE_TENSION_MAX_AGE_MS` fixe par seuil adaptatif (EMA latence × 3, plancher 800 ms).  
2. Logger `feed_latency_ms` à chaque cycle (percentiles 50/95/99) pour piloter le seuil.  
3. Appliquer la même logique adaptative à `VORTEX_JSON_MAX_AGE_SEC` (secondes) par symétrie.

SYNTHÈSE :  
Vortex test sain (0 stale) ; Nuage prod sur-skippe (800 ms trop bas pour WiFi alpage).  
Ordre : 1) Gate adaptative Nuage + métriques latence, 2) Vérifier/aligner Vortex, 3) Replay gain/perte.
