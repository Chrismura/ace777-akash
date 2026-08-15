# AUDIT FAMILLE — INFERX

_provider: Google Gemini_

### 1. Verdict : **GO AVEC RÉSERVES**

**Argumentation (Standards ACE777 / Hedge Fund) :**
Le diagnostic est chirurgical et la remédiation touche aux causes racines (faille systémique du boot `launchd` vs réseau). 
* **Points forts :** L’isolation de `ReseauIndisponible` évite le poison de la blacklist injustifiée sur les providers sains (zéro faux positifs d'indisponibilité). Le budget temps global (`REQUEST_MAX_SECONDS = 120`) tranche radicalement avec les dérives à 80 min. Les tests unitaires (4/4 en 0,11s) valident la robustesse immédiate.
* **Réserves :** Un budget global de 120s peut s'avérer juste si la cascade de bascule (`providers`) comporte 4 ou 5 acteurs lents mais joignables. De plus, `_reseau_disponible()` introduit une latence bloquante au premier appel de `chat_completions`.

---

### 2. Améliorations & Optimisations (Stabilité & Performance)

1. **Cache pour `_reseau_disponible()` :**
   * *Risque :* Si le réseau bascule fréquemment au boot, appeler un test DNS à *chaque* `chat_completions` initial va surcharger la boucle d'événements.
   * *Fix :* Mettre en cache le résultat de `_reseau_disponible()` pendant 5 à 10 secondes maximum (TTL court) pour éviter les requêtes DNS en cascade si plusieurs clients attaquent le hub simultanément au démarrage.

2. **Affinement du Budget Temps par Provider :**
   * *Risque :* `timeout_eff = min(budget_restant, 15 if not reseau_ok else budget_restant)`. Si `reseau_ok` est faux au démarrage, limiter à 15s est sage, mais pour un provider lourd (ex: DeepSeek en lecture), 15s peuvent couper net une réponse valide en mode dégradé.
   * *Fix :* Assurer un plancher minimal de timeout (ex: `max(5, timeout_eff)`) pour ne pas rejeter un provider qui répondrait en 12s malgré un réseau instable.

3. **Intégration avec le Mode Storm / Réserve :**
   * Le mécanisme actuel traite l'absence réseau comme un état externe. Il conviendrait de logger un événement spécifique (`ERROR_NETWORK_BOOT_DEGRADED`) interceptable par le moniteur de santé du hedge fund pour déclencher un statut "Jaune" (Degraded) plutôt que "Rouge" (Panne complète).

---
*ACE777 Validation Engine — Signé numériquement par l'Auditeur Senior, 13/08.*
