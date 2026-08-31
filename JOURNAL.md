
## 31/08 — FIX refresh cockpit en boucle (Buffy)
Symptôme : la page se rechargeait sans arrêt. Cause : le feed tamponnait la meta version avec un epoch à CHAQUE run → l'auto-éjection du cockpit (reload si le code change) tirait dès que le feed tournait, même sans changement de code.
Fix (cockpit_mission_feed.py) : la meta version = hash SHA256 du contenu du cockpit (hors version et ?v=) → ne change QUE si le code est édité. Le ?v= reste epoch (fraîcheur des données mission.js, ne déclenche pas de reload). Vérifié : 2 runs successifs → version stable ; édition du code → version change (reload). Version actuelle cockpit : 3003108738.
