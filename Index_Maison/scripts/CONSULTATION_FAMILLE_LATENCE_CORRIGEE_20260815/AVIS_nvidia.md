# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 56.4s)

**ANALYSE SOUS 3 ANGLES**

**Technique**  
- Chemin VORTEX : la garde `VORTEX_JSON_MAX_AGE_SEC` protège contre la fraîcheur du fichier, mais **ne mesure pas la latence réseau réelle** (elle vérifie l'âge du fichier local, pas le temps de transmission). Sous WiFi/alpage, si le fichier est écrit localement mais que la lecture est retardée par le réseau, la garde peut être contournée. **Trou potentiel** : pas de timestamp réseau côté serveur.  
- Chemin NUAGE : gate fixe 800ms = **faux positifs massifs** sous latence alpine (1811 skips historiques). Le seuil est arbitraire et ne s'adapte pas à la cadence réelle. Sur-skip = occasions manquées, mais **sûr** (pas de risque de trading sur données périmées).

**Risque/Impact**  
- Gate adaptive (seuil = médiane glissante de la latence observée + marge) : réduit les faux positifs, mais **complexifie** le code et introduit un risque de dérive si la latence varie fortement.  
- Garder le SKIP prudent : sûr, mais **coûte des opportunités** (1-8% des skips = pertes de trades potentiels).  
- **Recommandation** : gate adaptive avec **plancher de sécurité** (ex: max(800ms, médiane×2)) pour éviter les dérives.

**Priorité**  
1. Heartbeat corrigé (fait)  
2. **Corriger le rapport d'erreurs** (tag NUAGE_PROD_4H → run réel) pour éviter de fausses conclusions  
3. **Tester la robustesse latence** sur le chemin VORTEX (le plus critique car pas de gate réseau)  
4. **Adapter la gate NUAGE** (adaptive) seulement après validation sur données réelles

---

**VERDICT** : **GO-AVEC-RÉSERVE**  
Ouvrir un chantier robustesse latence, **mais** :  
- Prioriser la correction du rapport d'erreurs (sinon on répète les erreurs de diagnostic)  
- Ne pas toucher à la gate NUAGE avant d'avoir des données de latence réelles (logs timestampés)

**CONFIANCE** : 78%

**HYPOTHÈSES**  
1. La latence alpine est principalement due au réseau montant (upload) et non à la lecture des fichiers locaux.  
2. Le run vortex du 15/08 est représentatif d'un marché calme, pas d'un problème de code.  
3. Les logs NUAGE_PROD_4H (1811 tension_stale) sont fiables et reflètent la vraie latence.

**CE QUI CHANGERAIT L'AVIS**  
- Si les logs montrent que la latence est **stable** (< 200ms) sur 24h → gate fixe 800ms acceptable, pas besoin d'adaptive.  
- Si le chemin VORTEX a un **timestamp réseau** dans vortex_control.json → le trou de fraîcheur est comblé, priorité réduite.

**AMÉLIORATION PROPOSÉE**  
1. **Ajouter un timestamp réseau** dans vortex_control.json (côté serveur) pour mesurer la vraie latence.  
2. **Gate adaptive** sur NUAGE : seuil = max(800ms, médiane glissante 1h × 1.5) avec log des dépassements.  
3. **Dashboard latence** : visualiser tension_stale vs spread_too_wide sur 7 jours pour calibrer.

---

**SYNTHÈSE**  
Le run vortex 15/08 était sain (0 stale, 0 process_die) ; l'endormissement = marché calme. Le vrai problème est la latence alpine sur le chemin NUAGE (gate 800ms trop stricte). Ordre : corriger le rapport d'erreurs → ajouter timestamp réseau → gate adaptive → surveiller. Pas d'urgence à toucher le code avant ces étapes.
