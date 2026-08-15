# DIAG FAMILLE OSS20 — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777, j'applique la **Claude Permanente** (« Prouve la meilleure logique et applique-la dans la correction et l'amélioration ») avec rigueur, en m'appuyant strictement sur le contexte vivant et les faits physiques du testnet fournis.

Voici mon diagnostic, mes preuves et mes recommandations bornées :

---

### 1. Cause racine du faible taux de fill (0.000000 / skips massifs) et réglage précis chiffré

* **Constat et Preuve :** 
  - La configuration actuelle impose un delta temporel `IMPULSE_RESONANCE_DT_MS = 128` ms et un diviseur de chute de mur `IMPULSE_RESONANCE_WALL_DROP_PCT = 6.5`.
  - Le serveur testnet est intrinsèquement lent (latence moyenne de 1.35 s par requête, pics à 9.7 s). Les cycles réels du bot prennent ~8 s.
  - *Conséquence mécanique :* Mesurer une variation de carnet d'ordres (`depth`) sur une fenêtre de **128 ms** alors que l'intervalle effectif entre deux lectures (cycles) est de **~8 000 ms** revient à introduire un sous-échantillonnage massif. Le bot cherche un battement de cœur de colibri avec un stroboscope bloqué à une image toutes les minutes. Entre deux snapshots espacés de 8 secondes, la vague de liquidité passe, le mur s'effondre puis se reconstruit, et la variation instantanée est lissée à quasi-zéro (d'où les 0.000000 et le décalage observé à 10:41 entre BETA et ALPHA).
* **Réglage précis et chiffré (Variables d'environnement) :**
  - Puisque le testnet impose un rythme de cycle de ~8 s, la fenêtre de comparaison doit être alignée sur la cadence réelle d'ingestion des snapshots, et non sur une utopie de carnet ultra-rapide (réservée à l'API réelle).
  - **Proposition de réglage :**
    - `IMPULSE_RESONANCE_DT_MS = 2000` (monter de 128 ms à 2000 ms pour intégrer la viscosité du testnet tout en restant sensible aux vagues constatées le 13/08).
    - `IMPULSE_RESONANCE_WALL_DROP_PCT = 15.0` (élargir légèrement le seuil de chute de 6.5% à 15% pour compenser l'effet cumulé sur 2 secondes et éviter les faux positifs dus à la lenteur du réseau).

---

### 2. Cause racine probable des morts `rc=1` silencieuses et correctif court

* **Hypothèse la plus probable :**
  - Les symptômes (silence de 3 à 8 s après le dernier log, stderr à 0 octet, pas de `FATAL_RC1`, pas de `Done.`, code de sortie `1` sec sans trace) pointent vers **un timeout ou un SIGKILL/SIGPIPE silencieux au niveau de la couche réseau/socket (TCP socket hang / keep-alive timeout)** lors d'une requête HTTP bloquante vers l'API testnet ralentie (qui peut atteindre 9.7 s). 
  - Si le client HTTP sous-jacent (ou le runtime Python/Bash) atteint une limite de temps mort bloquante sans lever d'exception gérée proprement par le try/except global, le processus est avorté brutalement par le système ou le runtime avec un code `rc=1`, court-circuitant les gestionnaires de sortie standard (`atexit` ou `trap EXIT`).
* **Correctif d'observation le plus court pour capturer la cause :**
  - Activer le mode verbeux bas niveau des sockets Python et rediriger explicitement le flux d'erreur standard vers un fichier horodaté distinct dans le lanceur, plutôt que de compter uniquement sur le pipe global :
    - Ajouter dans l'environnement de lancement : `PYTHONTRACEMALLOC=1` et `PYTHONASYNCIODEBUG=1`.
    - Isoler la sortie d'erreur dans le wrapper bash : `exec 2> >(while read line; do echo "[$(date -u +'%T')] STDERR: $line"; done >> /tmp/ace777_stderr_debug.log)`.

---

### 3. Meilleure logique prouvée (Amélioration mesurable et bornée)

* **Principe prouvé :** La robustesse d'un système asynchrone face à un réseau tiers instable ou lent repose sur **l'élasticité des timeouts**, et non sur la rigidité des seuils.
* **Amélioration (bornée et sans toucher au genesis
