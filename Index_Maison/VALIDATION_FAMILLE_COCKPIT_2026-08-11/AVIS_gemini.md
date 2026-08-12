# AVIS GEMINI (via Google Gemini, task audit.protocol) — 2026-08-11T14:22:02

En tant que membre senior de la famille ACE777, voici mon audit critique, factuel et sans complaisance des setups actuels du cockpit (11/08/2026). Nous gérons de l'argent réel : la moindre défaillance silencieuse ou le moindre blocage d'interface est inacceptable.

---

### 1. INCASSABLE : Scénarios de pannes et comportements actuels

*   **Bridge Down (Port 17777 injoignable) :** 
    *   *Scénario :* Le processus `cortana_cockpit_bridge.py` plante (crash mémoire, exception non interceptée).
    *   *Comportement actuel :* Le front-end du cockpit (JS) tente de fetcher `GET /offres`. Si la requête échoue ou timeout, l'interface affiche une erreur générique ou se fige sur un état de chargement infini. 
    *   *Évaluation :* **Incorrect pour l'argent.** Le cockpit doit basculer immédiatement en mode "OFFLINE / DÉGRADÉ" visuel et afficher un avertissement rouge clignotant, sans bloquer le rendu du DOM.
*   **Hub Down (Local LLM / API LLM injoignable) :**
    *   *Scénario :* `brief_offres.py` ou `eval_offres.py` tente d'appeler le hub (ex: Gemini/Nvidia) et reçoit un timeout ou un HTTP 500/503.
    *   *Comportement actuel :* Le bloc `try/except` protège l'exécution immédiate, mais l'action de décollage peut échouer silencieusement ou laisser l'utilisateur sans retour.
    *   *Évaluation :* **Moyen.** Les scripts gèrent les exceptions, mais l'impact sur l'utilisateur n'est pas toujours explicitement tracé dans l'onglet Stratégie.
*   **Fichier veille absent ou corrompu (`VEILLE_HUB_<date>.md`) :**
    *   *Scénario :* Le cron `veille_hub.py` a échoué à 07:00, le fichier n'existe pas ou est tronqué/vide au moment où le bridge lit `GET /offres`.
    *   *Comportement actuel :* Le bridge gère le cas (payload vide, bannière "veille pas encore passée"). 
    *   *Évaluation :* **Correct.** C'est un comportement résilient et non bloquant.
*   **Exception JavaScript Front-End :**
    *   *Scénario :* Une modification du DOM ou une structure JSON inattendue lève une erreur dans le script JS du cockpit.
    *   *Comportement actuel :* Stoppe l'exécution du script (Uncaught Exception) et gèle l'interface utilisateur.
    *   *Évaluation :* **Inacceptable.** Absence de `try/except` global dans le code d'injection JS de l'onglet Stratégie.
*   **Quota épuisé (API tierces - OpenRouter, Nvidia, etc.) :**
    *   *Scénario :* Le compte ou la clé arrive à saturation (HTTP 429 Rate Limit / Quota Exceeded).
    *   *Comportement actuel :* Le scan continue, mais les évaluations ou briefs vocaux échouent. Si le brief vocal plante sur un quota, Vivienne risque de rester muette ou de lever une exception non gérée dans le pipeline matinal.
    *   *Évaluation :* **Faible.** Pas de gestion explicite du code HTTP 429 avec bascule vers un provider de secours ("fallback").

---

### 2. RÉSILIENT : Ce qui manque pour qu'une panne ne bloque JAMAIS la journée

*   **Cache de dernier secours (Fallback Cache) :** Si `VEILLE_HUB_<date>.md` est absent ou corrompu, le bridge doit automatiquement servir le dernier `VEILLE_HUB` valide disponible sur le disque (avec un bandeau jaune "MODE CACHE ACTIF"). Une vieille information vaut mieux que pas d'information du tout.
*   **Timeouts stricts et non-bloquants côté Bridge :** Tous les appels réseaux externes et les lectures de fichiers du bridge doivent être enserrés dans des timeouts stricts (max 3 secondes) pour ne jamais faire pendre une requête HTTP du cockpit.
*   **Circuit Breaker sur le TTS (Vivienne) :** Si `edge_tts` ou `afplay` échoue (problème audio macOS, absence de réseau), le script `brief_offres.py` doit logger l'erreur et **sortir proprement en code 0** sans planter la chaîne de lancement matinale. La voix est un confort, l'exécution est un dû.

---

### 3. AUTO-RÉPARANT : Ce qui doit se réparer seul et comment

*   **Surveillance des processus critiques (Launchd KeepAlive strict) :** Le bridge (`cortana_cockpit_bridge.py`) et le serveur HTTP du cockpit doivent posséder des fichiers `.plist` configurés avec `<key>KeepAlive</key><true/>` et `<key>ThrottleInterval</key><integer>5</integer>` pour garantir une résurrection automatique en moins de 5 secondes en cas de crash.
*   **Nettoyage des fichiers temporaires orphelins :** À chaque démarrage, le bridge doit purger les fichiers temporaires de type `*.tmp` ou `CHOIX_OFFRES.json.tmp` de plus d'une heure pour éviter les verrous de fichiers bloquants (locks).
*   **Auto-guérison des permissions :** Un script de health-check exécuté par le hub doit vérifier et rétablir automatiquement les permissions d'écriture sur les dossiers de logs et de data (`~/ace777-test-day1/`).

---

### 4. AUTO-ADAPTATIF : La veille et les nouveaux fournisseurs

*   **La réalité du mécanisme :** La veille actuelle (`veille_hub.py`) détecte bien les nouveautés textuelles via des patterns et des listes, mais **un provider découvert par scraping/RSS ne devient PAS testable automatiquement le lendemain**. 
*   **Le maillon manquant :** Il manque une couche de "génération de connecteur dynamique" ou une phase de validation manuelle obligatoire (sandbox) pour qu'un endpoint brut devienne un client API exécutable par `eval_offres.py`. Actuellement, la découverte est automatique, mais l'intégration technique reste humaine ou statique dans `providers.json`. Tant que ce pont n'est pas automatisé, un provider découvert reste une "simple ligne textuelle d'exploration".

---

### 5. AUTO-INTELLIGENT : Les 3 améliorations à plus forte valeur (mécaniques)

1.  **Le Cache de Survie Intelligent (Fallback Cache) :** Si une source de veille ou le bridge rencontre une anomalie critique, bascule automatique sur le dernier état sain connu pour maintenir l'interface active et exploitable.
2.  **Le Disjoncteur de Quota API (API Circuit Breaker) :** Détection instantanée des codes HTTP 429 / erreurs de quota, avec désactivation automatique du provider défaillant pour la session en cours et notification immédiate dans les alertes du cockpit.
3.  **L'Indicateur de Santé Global (Watchdog Visuel) :** Un widget permanent dans le coin supérieur du cockpit interrogeant un endpoint `/health` consolidé toutes les 30 secondes (Bridge, Hub, Dernier Cron) pour afficher une pastille globale unique (Vert/Orange/Rouge).

---

VERDICT FINAL : GARDER AVEC GARDE-FOUS RENFORCES
CONFIANCE : moyenne
