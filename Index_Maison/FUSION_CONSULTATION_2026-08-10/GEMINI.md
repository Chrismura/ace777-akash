# AVIS GEMINI (task audit.protocol) — AVANT FUSION

provider: Google Gemini

En tant que GEMINI, membre de la famille ACE777, j'applique la **loi 1quinquies** (mieux vaut améliorer AVANT que réparer APRÈS) au vu de l'état réel mesuré (rappel critique : *state.json : STALE 29 5* et seulement 4 services vivants sur 29 pour 8 Go de RAM).

Voici mon analyse structurée, concrète et priorisée.

---

### 1. Améliorations à faire MAINTENANT (avant la fusion) pour la simplifier

*   **Purger les doublons de monitoring inactifs :** 
    *   *Action :* Déscharger immédiatement les services de surveillance redondants (`com.ace777.observatoire`, `com.ace777.vigie`, `com.ace777.pulse-sous-loeil`).
    *   *Pourquoi :* Sur 29 services, 25 sont morts ou zombies. Nettoyer les plists obsolètes évite de polluer le futur superviseur unique avec des dépendances fantômes.
*   **Corriger la source de vérité (`state.json` STALE) :**
    *   *Action :* Forcer un run de `system_state_generator.py` pour valider que le heartbeat et la génération atomique fonctionnent *avant* de basculer la logique vers les 13 services.
*   **Geler le périmètre vocal :**
    *   *Action :* Isoler formellement les 2 services vocaux (`cockpit-http`, `cockpit-pont` ou `cortana`) pour qu'ils ne soient **jamais** touchés par la réduction 27->13.

---

### 2. Comment SIMPLIFIER la fusion (Stratégie et Ordre)

*   **Colonne vertébrale unique :** Le futur `com.ace777.superviseur` doit devenir le **seul** orchestrateur, consommant le `state.json` et pilotant un sous-ensemble de tâches planifiées en interne (threads ou boucles légères) plutôt que 13 processus launchd distincts si possible, ou 13 plists ultra-propres.
*   **Ordre des désactivations :**
    1. **Phase 1 :** Couper tous les services d'analyse/veille non essentiels (`analyste-cadence`, `analyse-usage`, `qwen-btc`, `eval-offres`).
    2. **Phase 2 :** Fusionner les services de maintenance (`rotation-logs`, `gitpush`, `backup-check`) en un script de maintenance global appelé par le superviseur.
    3. **Phase 3 :** Activer le nouveau superviseur 13 services et décharger définitivement les 16 plists restants.

---

### 3. Les 3 Risques principaux (et comment les éviter)

1.  **Risque 1 : La saturation RAM / Concurrence sur le Mac 8 Go.**
    *   *Impact :* Lancer trop de LLM locaux en même temps via les 9 providers du hub (port 11435).
    *   *Évitement :* Imposer un sémaphore strict dans le superviseur : **1 seul appel LLM lourd à la fois**.
2.  **Risque 2 : Le blocage du superviseur unique (Single Point of Failure).**
    *   *Impact :* Si le superviseur plante, tout s'arrête.
    *   *Évitement :* Garder `KeepAlive` strict sur le plist du superviseur et un log de secours minimaliste totalement indépendant de Python (via bash/stderr).
3.  **Risque 3 : Effet "zombie" des anciens plists launchd.**
    *   *Impacts :* Conflits de ports ou double écriture dans `state.json`.
    *   *Évitement :* Script de nettoyage `launchctl unload` obligatoire pour les 16 services supprimés avant de charger les 13 nouveaux.

---

### 4. Le superviseur unique doit absorber quels services en priorité ?

Le superviseur doit absorber et remplacer par des fonctions internes :
1.  **Le monitoring de santé :** `surveillance-quotas`, `veille-hub`, `heartbeat`.
2.  **La maintenance système :** `rotation-logs`, `gitpush`, `backup-check`.
3.  **Le reporting périodique :** `brief-matin`, `journal-soir`, `propose-ameliorations`.

*(Les services interactifs/vocaux comme `cortana` ou `cockpit` restent des entités séparées mais communiquent exclusivement via le `state.json`).*

---

### 5. VERDICT FINAL

> **AMELIORER D'ABORD**

**Justification (Loi 1quinquies) :** Le `state.json` est actuellement `STALE` et 25 services sur 29 dorment ou posent problème. Tenter une fusion 27->13 sur une base instable garantit des bugs en cascade. 

*   *À faire avant la conception de la fusion :* 
    1. Unload propre des services obsolètes pour redescendre à un état stable mesurable.
    2. Valider que `system_state_generator.py` repasse le `state.json` au statut `ok`.
    Une fois ces 10 minutes de nettoyage faites, nous serons **PRÊT POUR CONCEPTION**.
