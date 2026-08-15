# DIAG FAMILLE DEEPSEEK — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777, j'applique la **Clause Permanente de Christophe** : prouver la meilleure logique par les faits du contexte et proposer un correctif mesurable, borné, sans toucher au noyau *genesis*.

---

### 1) CAUSE RACINE DU FAIBLE TAUX DE FILL (0.000000) ET RÉGLAGE PRÉCIS

*   **Cause racine prouvée :** Le décalage spatio-temporel entre le moteur et le testnet. 
    *   Le paramètre `IMPULSE_RESONANCE_DT_MS = 128` ms a été conçu pour un flux API rapide (~464 ms).
    *   Or, le serveur testnet accuse un temps de latence moyen de **1.35 s** par requête (allant jusqu'à 9.7 s) et le cycle complet du bot prend **~8 s** au lieu de ~1 s.
    *   **Le piège physique :** Une impulsion de liquidité (chute de mur du book) se produit sur une fenêtre de 128 ms, mais le snapshot suivant met plus d'une seconde à arriver. Résultat : le delta mesuré (`wall_drop`) est moyenné, lissé ou rate la fenêtre d'opportunité. La preuve est dans le log du superviseur : BETA capture une chute de 70% (tension 10.8) à 10:41:56, mais ALPHA, 1 seconde plus tard sur le snapshot suivant, ne voit plus que 6% (tension 0.95). 
*   **Réglage précis chiffré (Variables d'environnement) :**
    *   Puisque le testnet réagit par vagues lentes et que la latence d'aller-retour est de ~1.35 s, il faut élargir la fenêtre temporelle d'observation pour capturer le vrai gradient de tension sans l'annihiler par un $dt$ trop court.
    *   *Proposition :* 
        *   `IMPULSE_RESONANCE_DT_MS` : passer de `128` à **`1250`** (ou `1500`) ms pour s'aligner sur la latence réelle des requêtes testnet (~1.35 s).
        *   `IMPULSE_RESONANCE_WALL_DROP_PCT` : ajuster le diviseur (seuil) de `6.5` à **`4.0`** ou **`5.0`** pour compenser le fait que sur une durée plus longue de 1.25 s, l'érosion du mur est plus diffuse mais cumulée.

---

### 2) CAUSE PROBABLE DES MORTS RC=1 SILENCIEUSES ET CORRECTIF D'OBSERVATION

*   **Cause racine probable :** 
    *   L'absence totale de trace dans le `stderr` (0 octet), l'absence de déclenchement du trap `FATAL_RC1`, et le délai de 3 à 8 s après le dernier cycle loggé pointent vers une **rupture anormale de flux I/O (broken pipe / SIGPIPE)** ou un **blocage de thread bloquant (deadlock d'attente réseau/socket suspendu)** au moment où le système tente d'écrire ou de lire sur une socket TCP testnet figée, sans que Python ne lève une exception interceptable par les gestionnaires classiques, ou qu'un timeout système silencieux ne tue le worker. Le fait que le run détaché de 20 min ait fini en `rc=0` (quand le testnet était stable) corrobore une sensibilité extrême au gel de la socket réseau du testnet.
*   **Correctif court (Observation indubitable) :**
    *   Puisque les traps EXIT/DEBUG actuels n'ont pas pu intercepter le signal (car l'outil terminal du superviseur a tué les deux premiers runs de capture, et que le 3e s'est bien comporté), il faut forcer le trappage des signaux système durs au niveau du lanceur Bash sans modifier `genesis` :
    *   *Action :* Ajouter explicitement dans le lanceur master le trappage des signaux de mort violente pour identifier si le processus reçoit un `SIGKILL`, `SIGTERM` ou un `SIGPIPE` :
        ```bash
        trap 'echo "[CRITICAL_TRAP] $(date -u) - Processus tué par signal ou exit rc=$?" >> /tmp/ace777_morts_rc1.log' ERR EXIT SIGINT SIGTERM SIGPIPE
        ```
    *   Coupler cela avec un `strace` léger ou un `set -x` redirigé vers un fichier horodaté permanent pour figer la toute dernière syscall avant le silence.

---

### 3) MEILLEURE LOGIQUE PROUVÉE (CLASSE PER
