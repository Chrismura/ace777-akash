# AVIS openrouter-juge (provider OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 17.1s)

Technique : Le chemin VORTEX s’appuie uniquement sur la garde `VORTEX_JSON_MAX_AGE_SEC`. Sans connaître sa valeur exacte, on ne peut garantir qu’elle couvre les pics de latence Wi‑Fi/alpage ; si le seuil est trop élevé, on risque d’utiliser une tension obsolète (trou de fraîcheur). Le chemin NUAGE applique un seuil fixe de 800 ms sur `duo_state.ts_ms`. En environnement alpin, la latence dépasse souvent cette valeur, ce qui provoque des SKIP « tension_stale » même quand les données sont encore utilisables (faux positifs).

Risque/Impact : Vivre en Wi‑Fi/alpage exige une tolérance à la latence plutôt qu’une élimination. Un seuil trop rigide (NUAGE) entraîne des occasions manquées, tandis qu’un garde trop laxiste (VORTEX) peut déclencher des trades sur des données périmées. Un seuil adaptatif, qui suit la RTT observée, permettrait de réduire les faux positifs tout en maintenant la fraîcheur acceptable.

Priorité : Après le heartbeat (mise à jour du `ts_ms`), le système doit d’abord vérifier la fraîcheur de la tension avant toute logique de déclenchement. Si la donnée est considérée trop vieille, le chemin doit soit attendre un nouveau rafraîchissement, soit utiliser la dernière valeur connue avec une décrue de confiance, puis passer à l’évaluation du spread et du duo no_trigger/stale.

VERDICT : GO‑AVEC‑RÉSERVE (ouvrir un chantier « robustesse latence » pour ajouter un seuil adaptatif et/ou un mécanisme de fallback)
CONFIANCE : 70 %
HYPOTHÈSES : 
1. `VORTEX_JSON_MAX_AGE_SEC` est actuellement fixé à une valeur supérieure à la latence typique observée (≥ 2 s). 
2. La latence alpine dépasse régulièrement 800 ms, provoquant des SKIP inutiles dans NUAGE. 
3. Un seuil adaptatif basé sur la moyenne glissante du RTT réduirait les faux positifs sans sacrifier la réactivité.
CE QUI CHANGERAIT L'AVIS : 
- Mesure montrant que la latence réelle dépasse rarement le seuil actuel de VORTEX (confirmant sa suffisance). 
- Ou, au contraire, preuve que la latence dépasse fréquemment 800 ms et que le taux de SKIP dépasse 20 % (justifiant un changement immédiat).
AMÉLIORATION PROPOSÉE : 
1. Implémenter un seuil adaptatif pour NUAGE (ex. `NUAGE_TENSION_MAX_AGE_MS = moyenne_RTT_last_5min * facteur`). 
2. Ajouter dans VORTEX une vérification de fraîcheur avec hysteresis (ex. accepter les données si âge < seuil*1,2 sinon attendre). 
3. Prévoir un fallback utilisant la dernière tension connue avec un facteur de confiance décroissant lorsqu’on dépasse le seuil.
SYNTHÈSE : Le run vortex du 15/08 n’avait aucun problème d’infrastructure ; l’observed « endormissement » provient d’un marché férié calme. Toutefois, la latence réseau réelle en Wi‑Fi/alpage n’est pas suffisamment maîtrisée par les gardes fixes actuelles. Il faut introduire un mécanisme de seuil adaptatif et/ou de fallback pour garantir la robustesse sans sacrifier les opportunités de trading.
