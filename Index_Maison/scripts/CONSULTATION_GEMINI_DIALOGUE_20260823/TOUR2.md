# TOUR 2 (4 s)

**AUDIT APPROFONDI : FAILLES DES GARDE-FOUS ET NIVEAU 3**

*   **R1 (Fraîcheur)** : *Faille* : `time.monotonic()` saute si la machine passe en veille (macOS M1). *Niveau 3* : `time.monotonic_ns()` combiné à un check de l'uptime du kernel via `sysctl kern.boottime`.
*   **R2 (Atomricité)** : *Faille* : Quarantaine sature le disque SSD (8 Go). *Niveau 3* : Rotation stricte, max 3 fichiers de secours, écrasement du plus ancien.
*   **R3 (Repli)** : *Faille* : DNS empoisonné ou TTL réseau infini bloquant la bascule. *Niveau 3* : Hardcoding des IPs primaires/secondaires des endpoints + timeout socket strict de 3.0 s.
*   **R4 (Anti-blocage)** : *Faille* : Un `multiprocessing.Process.terminate()` laisse un socket ouvert en état `CLOSE_WAIT`, sature les descripteurs de fichiers. *Niveau 3* : Fermeture explicite des sockets (`sys.modules`) dans le `finally` du worker avant le yield.
*   **R5 (Budget API)** : *Faille* : Fichier lock en RAM (`/tmp`) purgé par macOS au bout de 3 jours d'inactivité. *Niveau 3* : Stockage permanent dans le répertoire data local (`./state/backoff.json`).
*   **R6 (Canari)** : *Faille* : Le relecteur boucle sur un heartbeat valide mais l'application interne est morte (deadlock Python GIL). *Niveau 3* : Heartbeat actif nécessitant un `os.write()` sur un pipe validé par le worker, pas un simple fichier statique.
*   **R7 (Ressources)** : *Faille* : Fragmentation mémoire Python (malloc) non libérée sous 300 Mo. *Niveau 3* : Appel forcé à `ctypes.CDLL(None).malloc_zone_pressure_relief(None, 0)` pour purger les caches malloc macOS si RSS > 220 Mo.

---

### (A) FONCTIONNEMENT
- **Architecture** : Orchestrateur unique en Python stdlib, lancé par `launchd` (intervalle 30 s). Zero fork infini.
- **Cycle d'exécution** : 
  1. Check verrou global (`/tmp/ace.lock`, TTL 45 s, sinon purge PID).
  2. Ingestion mempool/dust avec socket timeout 3s strict, bascule API persistée.
  3. Écriture atomique (mkstemp + os.replace + checksum SHA-256).
  4. Analyse Cortana (budget 1 appel/2s, backoff persistant).
- **Kill-switch** : Fichier `./STOP_ALL` présent = arrêt immédiat de tous les sous-processus.

---

### (B) DÉTECTION (Seuils chiffrés & Qui surveille qui)
*   **Mort silencieuse** : Heartbeat age > 45 s (détecté par le Surcouche Watcher).
*   **Fichiers figés** : Hash SHA-256 identique sur 3 cycles cons
