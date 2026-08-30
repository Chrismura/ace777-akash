# TOUR 1 (3 s)

En tant qu'auditrice en chef de la famille ACE777, voici le passage au crible du protocole sur Mac M1 (8 Go, Python stdlib, zero dépendance externe) et le protocole final incassable.

---

### AUDIT FORENSIQUE : FAILLES ET GARDE-FOUS DE NIVEAU 2

*   **R1 (Fraîcheur)**
    *   *Point faible* : Décalage d’horloge système (`os.system('ntpdate')` absent sur M1 hors réseau), rendant le TTL invalide.
    *   *Garde-fou N2* : Utilisation exclusive de `time.monotonic()` pour les deltas et horodatage UTC via `time.time()` validé par `os.stat().st_mtime`.
*   **R2 (Écriture atomique)**
    *   *Point faible* : `os.replace()` peut échouer sur macOS si le fichier cible est verrouillé par un autre processus en lecture.
    *   *Garde-fou N2* : Capture de `PermissionError`, retry unique à 50 ms, puis écriture dans un dossier de quarantaine avec flag d'alerte.
*   **R3 (Repli multi-source)**
    *   *Point faible* : Fichier de bascule corrompu par une écriture interrompue au kill-switch, bloquant toutes les requêtes.
    *   *Garde-fou N2* : Validation JSON obligatoire du fichier d'état et fallback hardcodé vers `mempool.space` si le fichier est illisible.
*   **R4 (Ceinture anti-blocage)**
    *   *Point faible* : `SIGALRM` ne fonctionne pas dans les threads multiples (Python `threading`), or le hub utilise potentiellement des workers.
    *   *Garde-fou N2* : Utilisation exclusive de `socket.settimeout()` synchrone et de `multiprocessing.Process` avec `join(timeout=35)` pour tuer net les runs bloqués.
*   **R5 (Budget API)**
    *   *Point faible* : Le compteur de backoff en mémoire vive est effacé à chaque redémarrage par launchd (erreur 1 : plists en boucle).
    *   *Garde-fou N2* : État du backoff persisté dans `/tmp/ace777_backoff.lock` avec verrouillage atomique.
*   **R6 (Canari du surveillant)**
    *   *Point faible* : Le PID du heartbeat est réattribué trop vite par macOS (PID reuse), fausseté de l'unicité.
    *   *Garde-fou N2* : Le heartbeat intègre le `os.getppid()` et un UUID de session généré au démarrage du daemons.
*   **R7 (Budget ressources)**
    *   *Point faible* : `resource.setrlimit` mal géré sur macOS pour la mémoire RSS, provoquant des crashs inopinés (Kernel Panic léger / OOM killer).
    *   *Garde-fou N2* : Surveillance interne légère via `sys.getsizeof()` et `gc.collect()`, couplée à un max RSS de 250 Mo vérifié à chaque cycle.

---

### PROTOCOLE FINAL INCASSABLE (ACE777)
