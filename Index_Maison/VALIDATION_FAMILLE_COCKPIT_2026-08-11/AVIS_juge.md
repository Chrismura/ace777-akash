# AVIS JUGE (via Google Gemini, task signets.juge) — 2026-08-11T14:23:44

En tant que membre senior de la famille ACE777, voici mon audit critique, factuel et sans complaisance des setups livrés. Nous gérons de l'argent réel : le code ne doit pas seulement "fonctionner par beau temps", il doit survivre aux tempêtes, aux pannes réseau, aux corruptions de fichiers et à la stupidité des APIs tierces.

---

### 1. INcASSABLE — Analyse des scénarios de panne

*   **Scénario A : Bridge down (port 17777 injoignable)**
    *   *Comportement actuel :* Le JS du cockpit (onglet stratégie) fait des `fetch` asynchrones. Si le bridge est mort, les requêtes échouent, la bannière d'état bascule en erreur ou reste figée, et les actions (bouton DÉCOLLER) lèvent une exception JS non gérée dans la console, laissant l'interface bloquée.
    *   *Est-ce correct ?* **Non.** Le JS doit wrapper chaque `fetch` dans un bloc de repli gracieux et afficher une pastille rouge explicite "BRIDGE HORS LIGNE" sans bloquer le rendu du reste de la page.
*   **Scénario B : Hub local down ou KO (127.0.0.1:11435)**
    *   *Comportement actuel :* `brief_offres.py` ou `eval_offres.py` tente d'appeler le LLM local (Gemini/Nvidia). Si le hub est mort, l'appel lève une exception. Pour la veille matinale, le try/except global évite le crash du script, mais la voix de Vivienne reste muette.
    *   *Est-ce correct ?* **Partiellement.** Le silence d'or est respecté pour éviter un vocal vide, mais il manque un log critique d'alerte immédiat dans le canal d'alerte du cockpit.
*   **Scénario C : Fichier veille absent, vide ou corrompu (`VEILLE_HUB_<date>.md`)**
    *   *Comportement actuel :* `GET /offres` gère l'absence de fichier (payload vide, bannière "veille pas encore passée"). En revanche, si le fichier est partiellement corrompu (écriture disque interrompue), le parseur Python peut lever une exception de parsing.
    *   *Est-ce correct ?* **Incomplet.** Le parsing Markdown doit être ultra-tolérant (regex défensives) : si une ligne ne matche pas le format attendu, on l'ignore au lieu de planter la route API.
*   **Scénario D : Exception JavaScript dans le client**
    *   *Comportement actuel :* Si une modification du DOM échoue ou si le JSON reçu du bridge a un champ inattendu (`undefined`), tout le script s'arrête (Error Boundary absent en JS vanilla).
    *   *Est-ce correct ?* **Non.** Un `try/catch` global sur le rendu des composants UI est impératif pour éviter la page blanche.
*   **Scénario E : Quota épuisé sur les APIs gratuites (OpenRouter, Nvidia, etc.)**
    *   *Comportement actuel :* Le scan passe (timeout géré), mais les évaluations ultérieures (`eval_offres.py`) peuvent échouer en cascade.
    *   *Est-ce correct ?* Le bridge ne gère pas le retour d'erreur 429 (Rate Limit) de manière proactive dans l'affichage des cartes fournisseurs.

---

### 2. RÉSILIENT — Ce qui manque pour ne jamais bloquer la journée

1.  **Cache persistant (Fallback-on-Stale) :** Si `VEILLE_HUB` du jour échoue ou n'existe pas à 08:00, le bridge doit automatiquement servir le dernier `VEILLE_HUB` valide disponible sur le disque, étiqueté avec un badge "🟡 MODE DÉGRADÉ (DONNÉES HIER)". Une vieille info vaut mieux que pas d'info du tout.
2.  **Timeouts stricts et disjoncteurs (Circuit Breakers) côté Bridge :** Tout appel externe (ou même interne vers le hub) doit posséder un timeout strict (max 3s) avec un compteur d'échecs consécutifs. Au bout de 3 échecs, le service est mis en "pause" temporaire pour éviter d'asphyxier la boucle d'événements.
3.  **Auto-relance des daemons via Launchd (KeepAlive) :** S'assurer que chaque service critique (`cortana_cockpit_bridge.py`, `cockpit_http_server.py`) possède `KeepAlive: true` dans son fichier `.plist` pour redémarrer instantanément en cas de crash système.

---

### 3. AUTO-RÉPARANT — Ce qui doit se réparer seul

1.  **Nettoyage automatique des fichiers temporaires orphelins :** Les écritures atomiques (via fichier `.tmp` puis `replace`) laissent parfois des orphelins si le processus est tué au mauvais moment. Un script ou une routine au démarrage du bridge doit purger le dossier de tous les fichiers `.tmp` de plus de 5 minutes.
2.  **Auto-correction des permissions et des chemins :** Au démarrage, le bridge doit vérifier l'existence des dossiers indispensables (`Index_Maison/data`, `logs`, etc.) et les recréer silencieusement s'ils ont été supprimés par erreur.
3.  **Purge des logs volumineux :** Empêcher la saturation du disque en appliquant une rotation des logs basée sur la taille (max 10 Mo par fichier log).

---

### 4. AUTO-ADAPTATIF — La réalité de la veille et des fournisseurs

*   **La veille s'adapte-t-elle ?** Oui, elle détecte de nouveaux noms via les sources configurées.
*   **Le maillon manquant :** Un fournisseur découvert dans un README GitHub ou un flux RSS (affiché dans le "Panneau exploration") reste une simple *chaîne de caractères*. **Il n'est pas testable automatiquement** car `providers.json` ne contient pas sa structure d'API, son endpoint, ni son mode d'authentification.
*   **Solution mécanique :** Le panneau exploration doit proposer un bouton "Générer un template de provider" qui utilise le LLM local pour analyser l'URL de la doc découverte et rédiger une proposition d'intégration standardisée dans `providers.json` soumise à validation.

---

### 5. AUTO-INTELLIGENT — Les 3 améliorations à plus forte valeur

1.  **Le Disjoncteur de Quota (Rate-Limit Shield) :** Un mécanisme simple dans le bridge qui intercepte les erreurs 429 / 403 des providers et désactive automatiquement leur sélection dans l'onglet stratégie pendant 1 heure, évitant de gaspiller des cycles CPU et de polluer les logs.
2.  **Le Snapshot de Santé au Démarrage (Pre-flight strict) :** Une vérification exécutée à chaque lancement du bridge qui teste l'intégrité de tous les fichiers JSON critiques (`providers.json`, derniers rapports). Si un JSON est mal formé (erreur de syntaxe), le système renomme le corrompu en `.corrupt` et restaure instantanément la dernière sauvegarde `.bak` valide.
3.  **L'Indicateur de Fraîcheur Temporel :** Dans l'UI du cockpit, chaque donnée affichée doit porter son âge exact (ex: *"mis à jour il y a 12 min"*). Si l'âge dépasse 24h sans nouvelle veille, la bannière passe au rouge vif pour alerter Christophe qu'un pipeline est bloqué en amont.

---

VERDICT FINAL : GARDER AVEC GARDE-FOUS RENFORCES
CONFIANCE : moyenne
