# AUDIT FAMILLE — GEMINI

_provider: Google Gemini_

### 1. Verdict : **GO AVEC RÉSERVES** (Niveau Hedge Fund Suisse)

L'architecture de ce correctif attaque le problème à la racine. Le couplage pernicieux entre panne réseau initiale (DNS/Errno 8 au boot) et pénalisation artificielle des providers sains (via les 3 échecs et le backoff) est enfin rompu par l'exception `ReseauIndisponible` (C1) et la disjonction des compteurs de faille. 

Le budget global `REQUEST_MAX_SECONDS = 120` (C2) et le test préventif (C3) éliminent le risque de blocage systémique pendant 80 minutes. Les tests unitaires (4/4 en 0,11s) valident la robustesse immédiate.

**Réserves :**
* **Faux positifs réseau :** Une instabilité de passerelle intermittente (coupure fibre de 2 secondes en pleine session) pourrait être interceptée à tort comme un problème DNS/Connexion au milieu d'un appel long, provoquant une bascule précipitée au lieu d'une simple ré-évaluation PATIENCE.
* **Budget de 120s vs LLMs lourds :** Certains providers gratuits ou chargés (comme ceux utilisés en repli) peuvent mettre plus de 120 secondes à répondre sous forte charge. Un timeout global strict risque de couper net des requêtes sur le point d'aboutir.

---

### 2. Améliorations & Optimisations requises

* **Affinement de la distinction Réseau vs Lenteur :** Ne déclencher `ReseauIndisponible` que sur les erreurs d'initialisation de socket (`gaierror`, `ECONNREFUSED`, `ENETDOWN`). Si une connexion est établie mais expire (`timeout`), il faut conserver la logique de PATIENCE.
* **Dynamisme du budget selon la saison/charge :** Le contexte actuel indique une saison *CALME 🧊* (PnL +2.61 $). Le budget de 120s est adapté, mais il conviendrait de le lier dynamiquement à l'état du *feed mission* ou du niveau d'alerte (ex: tolérance 180s en mode `storm`, 90s en mode `calme`).
* **Hystérésis pour le mode dégradé (`_reseau_disponible`) :** Plutôt de tester à chaque `chat_completions`, mémoriser le dernier état réseau réussi pendant une fenêtre de 30 secondes pour éviter de saturer le resolver DNS local à chaque requête.
