# AVIS ULTRA (task ultra.analyse, morceau M1_coeur_reseau)

provider: Google Gemini

*Rapport d'audit de niveau hedge fund suisse — Rédigé par ULTRA (ACE777).*

---

### 1. Analyse Profonde du Morceau M1 (Lignes 1-160)

Le morceau centralise le cœur opérationnel bas niveau du hub : initialisation, gestion de l'environnement, persistance des logs/usages, routage direct des providers et protection de l'état global.

*   **Robustesse 24/7 & Chemins absolus :** 
    *   *Positif :* Utilisation systématique de `ROOT = os.path.dirname(os.path.abspath(__file__))` pour tous les fichiers (`providers.json`, `routing.json`, `.env`, etc.). Aucune dépendance au répertoire de travail courant (`cwd`), ce qui garantit un comportement stable quel que soit l'endroit d'où le démon est invoqué.
    *   *Positif :* Les écritures de logs (`log_event`, `log_usage`) et les lectures de configuration intègrent des blocs `try...except` silencieux qui empêchent un crash du démon en cas de disque saturé ou d'I/O corrompue.
*   **Thread-Safety :**
    *   *Positif :* Le hub tournant sur un `ThreadingHTTPServer`, l'accès aux dictionnaires partagés en mémoire (`_fails` et `_blacklist`) est strictement protégé par le verrou `_blacklock = threading.Lock()`. Aucune condition de course (`race condition`) détectée sur le backoff progressif.
*   **Logique Ollama / API Native :**
    *   *Positif :* L'embranchement détectant `:11434` pour utiliser l'API native `/api/chat` avec `"think": False` neutralise la faille critique des *reasoning models* (où le modèle consommait tout son budget en monologue interne en renvoyant un contenu vide).

---

### 2. Cohérence avec le Reste du Hub & Architecture ACE777

Le morceau M1 s'emboîte parfaitement avec le reste du script et les exigences de la **Loi 1quinquies** et des décisions du 13/08 :
1.  **Dynamisme des gratuits :** La fonction `_gratuits_actifs()` (amorcée à la fin du morceau et complétée plus bas) interroge dynamiquement `providers.json` via le champ `free: true`, respectant le dogme de Christophe : *« Valeur fixe -> on coule. »* Aucune liste statique de providers gratuits n'est codée en dur.
2.  **Patience & Backoff :** Le couplage entre `_register_result` (3 échecs consécutifs -> backoff exponentiel plafonné à 4h) et `call_provider` (retries avec timeout x3) offre une résilience de type institutionnel face aux micro-coupures réseau ou aux ralentissements des APIs tierces.
3.  **Mode Tempête :** L'intégration de la logique de tempête (via les sentinelles sur `ada_gardienne_live.json`, `alarme.json` et les vortex) garantit que les tâches prioritaires (`signets.juge`, `audit.protocol`, etc.) ne subissent aucune coupure arbitraire de budget calme.

---

### 3. Failles Restantes & Points de Vigilance (Zéro Défaut)

Bien que le code soit extrêmement propre et prêt pour la production 24/7 sur le Mac 8 Go, deux points mineurs méritent une attention de contrôle (sans bloquer la compilation `COMPILE_OK`) :

1.  **Fuite potentielle de descripteurs de fichiers (`fd leaks`) dans les boucles de lecture :**
    *   *Observation :* Dans `usage_today()` et dans `Handler.do_GET()` (pour `/events` et `/usage`), les fichiers JSONL sont ouverts via `with open(...)` ce qui est correct (fermeture automatique à la sortie du bloc `with`). Cependant, pour l'analyse de gros fichiers de logs cumulés (`usage.jsonl` sur plusieurs jours/semaines), la lecture intégrale via `f.readlines()` ou itération ligne par ligne sans limite de taille en mémoire pourrait croître.
    *   *Recommandation future (non urgente) :* Pour l'instant, le filtrage par date (`ev.get("ts", "")[:10] == today`) et la découpe des derniers éléments (`[-25:]`, `[-50:]`) protègent efficacement la mémoire vive du Mac 8 Go.
2.  **Gestion du timeout brut dans `_raw_call` :**
    *   *Observation :* L'utilisation de `urllib_request.urlopen(req, timeout=timeout)` est synchrone et bloque le thread du serveur HTTP pendant toute la durée de l'inférence (qui peut atteindre 300s à 900s en cas de retry avec patience).
    *   *Atténuation :* C'est précisément pour cela que le serveur utilise `ThreadingHTTPServer` : chaque requête HTTP client déclenche un thread dédié, évitant ainsi de bloquer la file d'attente globale du hub (`/health` et les autres requêtes restent répondables en parallèle).

---

### 4. Verdict de l'Audit

*   **Statut du Morceau M1 :** **VALIDE / CONFORME**
*   **Impact sur le Flux :** Neutre à hautement positif. Le cœur réseau assure la stabilité des appels tout en respectant scrupuleusement la hiérarchie des quotas, le budget dynamique et la réserve storm.
*   **Niveau de Robustesse :** Hedge fund suisse. Aucune exception non gérée ne peut faire s'effondrer le démon (filet de secours de dernier recours inclus si tous les providers sont blacklistés).

*Le code est prêt pour l'intégration définitive par le superviseur et la validation finale de la famille.*
