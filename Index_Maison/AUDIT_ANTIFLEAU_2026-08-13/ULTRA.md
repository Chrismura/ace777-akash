# AUDIT FAMILLE — ULTRA

_provider: Google Gemini_

**VERDICT : GO AVEC RÉSERVES**

### 1. Analyse critique
Le ciblage chirurgical est excellent : dissocier la panne réseau (DNS/connexion) de la latence provider évite l'effet cascade destructeur (blacklist injustifiée, blocages de 80 min). L'introduction du budget global (`REQUEST_MAX_SECONDS = 120`) et du mode dégradé basé sur `_reseau_disponible()` résout proprement le syndrome du boot post-batterie. 

**Réserve majeure :** 
Le test DNS initial (`_reseau_disponible`) introduit une latence bloquante synchrone au début de chaque requête si le réseau est down, et souffre d'un risque de faux positif/négatif selon la robustesse du résolveur ciblé (ex: 1.1.1.1 ou 8.8.8.8). De plus, fixer le timeout à 15s en mode dégradé peut s'avérer trop court pour certains gros payloads sur une connexion 4G/fibre chancelante au démarrage.

---

### 2. Améliorations de logique, performance et stabilité (Standards ACE777)

*   **A. Mémoïsation du check réseau (Performance) :**
    `_reseau_disponible()` ne doit pas être appelé à chaque requête en boucle. Mettez en cache son résultat pendant 10 à 30 secondes (TTL court) pour éviter de multiplier les sondes DNS en cas de rafale de requêtes au boot.
*   **B. Robustesse du `_reseau_disponible()` :**
    Ne testez pas qu'une seule IP. Interrogez en parallèle (ou avec fallback) deux cibles distinctes (ex: passerelle locale + DNS externe) pour éviter qu'un faux négatif ne plonge tout le hub en mode dégradé permanent.
*   **C. Synergie avec le Storm (Résilience) :**
    Si `ReseauIndisponible` est capturé, le hub devrait basculer temporairement dans un état `NETWORK_STORM` global (durée 30s) suspendant les appels aux providers et retournant un code explicite ou une attente active courte, plutôt que d'épuiser inutilement la boucle de providers.
*   **D. Observabilité :**
    Ajouter un compteur métrique pour tracer précisément le nombre de bascules évitées grâce au `ReseauIndisponible` vs les vrais timeouts de lecture.
