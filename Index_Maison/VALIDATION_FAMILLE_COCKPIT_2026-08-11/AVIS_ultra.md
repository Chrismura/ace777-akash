# AVIS ULTRA (via Google Gemini, task ultra.analyse) — 2026-08-11T14:23:55

En tant que membre senior de la famille ACE777, voici mon analyse critique, factuelle et sans complaisance des setups livrés pour le cockpit et son écosystème. Ici, de l'argent réel est en jeu : chaque point de défaillance doit être anticipé, car l'optimisme n'est pas une stratégie de trading ou de gestion d'infrastructure.

---

### 1. INcASSABLE : Analyse des scénarios de pannes et comportements actuels

*   **Bridge Down (Port 17777 injoignable ou planté) :** 
    *   *Scénario :* Le processus Python du bridge s'arrête (SIGKILL, exception non catchée).
    *   *Comportement actuel :* Le cockpit affiche une erreur de chargement ou des cartes vides, la bannière passe au rouge/gris d'erreur, et le bouton DÉCOLLER devient inopérant. C'est inacceptable si l'interface reste figée sans instruction claire.
    *   *Verdict :* Partiellement correct (l'UI réagit), mais il manque un mode "offline/dégradé" clair côté client JavaScript.
*   **Hub Down (LLM local ou routeur 11435 injoignable) :**
    *   *Scénario :* `veille_hub.py` ou `brief_offres.py` tente d'appeler le Hub et reçoit un `ECONNREFUSED`.
    *   *Comportement actuel :* `veille_hub.py` isole chaque source avec des try/except et un timeout (20-25s), ce qui est **très bien**. Cependant, si le LLM local utilisé pour la synthèse du brief est mort, `brief_offres.py` peut planter ou générer un fichier vide.
    *   *Verdict :* Résilient au niveau des sources externes, mais fragile si le cœur local (Gemini/Nvidia via proxy) ne répond plus lors du brief vocal.
*   **Fichier veille absent ou corrompu (`VEILLE_HUB_<date>.md`) :**
    *   *Scénario :* Le script de 07:00 a échoué (disque plein, crash), le fichier n'existe pas ou contient du JSON/Markdown tronqué.
    *   *Comportement actuel :* `GET /offres` renvoie un payload vide géré par le bridge, et le cockpit affiche « veille pas encore passée ».
    *   *Verdict :* **Correct et sûr.** Le système ne crashe pas sur un fichier manquant, il adopte un comportement neutre.
*   **Exception JavaScript dans le Cockpit :**
    *   *Scénario :* Une mise à jour de structure JSON inattendue fait planter le parsing dans le navigateur (ex: `undefined is not a function`).
    *   *Comportement actuel :* L'onglet Stratégie se fige, la boucle de rendu meurt.
    *   *Verdict :* **Dangereux.** Il manque un bloc `try/catch` global autour du rendu dynamique de l'onglet Stratégie pour afficher un message d'alerte UI au lieu d'une page blanche.
*   **Quota épuisé (API Free OpenRouter / Nvidia / etc.) :**
    *   *Scénario :* Erreur 429 (Too Many Requests) ou 402 sur les providers.
    *   *Comportement actuel :* `veille_hub.py` gère le try/except, mais `eval_offres.py` lors du DÉCOLLAGE peut échouer silencieusement ou bloquer la file d'attente.
    *   *Verdict :* Insuffisant. Il faut un mécanisme de blacklist temporaire (cooldown de 1h) pour les providers en erreur 429.

---

### 2. RÉSILIENT : Ce qui manque pour qu'une panne ne bloque JAMAIS la journée

1.  **Cache de secours (Fallback Data) :** Si `VEILLE_HUB` du jour échoue à 07:00, le bridge doit automatiquement servir le dernier `VEILLE_HUB` valide disponible (avec un avertissement visuel orange "MODE CACHE - J-1"). Une information ancienne vaut mieux que pas d'information du tout.
2.  **Disjoncteur (Circuit Breaker) sur le TTS :** Si Vivienne (`edge_tts`) ou `afplay` bloque (problème audio macOS, processus zombie), `brief_offres.py` ne doit **jamais** bloquer l'exécution globale. Un timeout strict de 10s sur la lecture audio avec abandon immédiat est obligatoire.
3.  **Heartbeat et Watchdog externe :** Ne pas se reposer uniquement sur `launchd` (qui parfois oublie de relancer si les clés `KeepAlive` sont mal configurées). Un script cron ultra-léger toutes les 5 minutes doit vérifier que le port 17777 (Bridge) et le port 17800 (Cockpit) répondent, sinon il kill et relance.

---

### 3. AUTO-RÉPARANT : Ce qui doit se réparer seul et comment

1.  **Processus zombies et ports bloqués :** 
    *   *Mécanisme :* Au démarrage du bridge (`cortana_cockpit_bridge.py`), le script doit lui-même exécuter un `lsof -ti :17777 | xargs kill -9` pour s'assurer qu'aucun ancien démon zombie ne bloque le port. Zéro intervention de Christophe requise.
2.  **Nettoyage des fichiers temporaires orphelins :**
    *   *Mécanisme :* `CHOIX_OFFRES.json.tmp` ou autres fichiers transitoires générés lors des écritures atomiques doivent être purgés automatiquement par le bridge au démarrage s'ils datent de plus de 10 minutes.
3.  **Intégrité de launchd :**
    *   *Mécanisme :* Un script `doctor.py` exécuté au boot de la session vérifie la présence des plists dans `~/Library/LaunchAgents/` et les recharge (`launchctl load -w`) si un fichier a été modifié ou corrompu.

---

### 4. AUTO-ADAPTATIF : La veille et les nouveaux fournisseurs

*   **La veille s'adapte-t-elle ?** Oui pour la *détection* (grâce aux scans GitHub, HuggingFace et RSS), mais **non pour l'intégration technique**.
*   **Le maillon manquant :** Un provider découvert par la veille (ex: un nouveau endpoint sur OpenRouter ou un nouveau modèle sur une liste GitHub) est affiché dans le panneau "exploration" ou dans les listes, **mais il n'est pas testable immédiatement**. Pourquoi ? Parce que `eval_offres.py` ne sait pas instancier dynamiquement un client API pour un provider dont il ne connaît pas le schéma exact d'appel (payload, headers, auth).
*   **Solution mécanique :** Les nouveaux providers doivent passer par une phase obligatoire de "Stub d'intégration" (généré par le Hub via LLM) avant de devenir cliquables dans le cockpit. Tant que le schéma d'appel n'est pas validé par un test unitaire automatique, le modèle reste en zone "Exploration" (gris), et non "Testable" (vert).

---

### 5. AUTO-INTELLIGENT : Les 3 améliorations à plus forte valeur

1.  **Le Bouton "Panic / Reset Global" dans le Cockpit :** Un bouton rouge unique dans la bannière du cockpit qui envoie un `POST /reset` au bridge : tue tous les processus d'évaluation en cours (`eval_offres.py`), vide les fichiers temporaires, purge la mémoire et redémarre les services propres. En cas de doute, Christophe clique une fois, tout redevient propre en 2 secondes.
2.  **Scoring de Confiance Automatique des Offres :** Avant d'afficher les offres dans l'onglet Stratégie, un mini-script évalue la stabilité historique du provider (taux de succès des 7 derniers jours). Les offres sont triées par *fiabilité réelle* et non par ordre alphabétique ou chronologique brut. L'argent va vers le plus sûr, pas vers le plus récent.
3.  **Auto-Diagnostic Visuel au Survol :** Dans la bannière d'état globale, le survol (tooltip) de chaque pastille fournisseur doit afficher la dernière latence mesurée et le taux d'erreur sur 24h, calculé à partir des logs locaux. Zéro opacité : on sait immédiatement quel fournisseur tousse.

---

VERDICT FINAL : GARDER AVEC GARDE-FOUS RENFORCES  
CONFIANCE : moyenne
