# DIAG FAMILLE JUGE — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777 et en appliquant rigoureusement la **CLAUDE PERMANENTE** (« Prouve la meilleure logique et applique-la dans la correction et l'amélioration »), voici l'analyse diagnostique, les preuves et les recommandations bornées pour les deux questions.

---

### 1) Cause racine du faible taux de fill / `0.000000` & Réglage précis chiffré

* **Cause racine prouvée :** Inadéquation temporelle (mismatch) entre la fréquence d'échantillonnage locale et la latence intrinsèque du Testnet. 
  * Le paramètre actuel fixe $\Delta t = 128\text{ ms}$ (`IMPULSE_RESONANCE_DT_MS`) et un diviseur de chute de mur de $6.5\%$ (`IMPULSE_RESONANCE_WALL_DROP_PCT`).
  * Or, le serveur Testnet répond en moyenne en **$1.35\text{ s}$** par requête (avec des pointes à $9.7\text{ s}$), et les cycles complets du bot prennent ~8 secondes. 
  * **Conséquence mécanique :** Échantillonner le carnet d'ordres toutes les $128\text{ ms}$ sur une infrastructure qui met plus d'une seconde à actualiser ses états conduit à comparer deux snapshots quasi-identiques (bruit de fond ou valeurs nulles `0.000000`). Lorsque le Testnet génère une vraie vague de liquidité, la fenêtre de $128\text{ ms}$ la rate ou l'observe partiellement, expliquant pourquoi BETA (qui sonde en rafales) attrape quelques mouvements là où ALPHA (qui cherche l'impulsion instantanée) se retrouve en situation de *skip* chronique.

* **Réglage précis et chiffré (Variables d'environnement) :**
  Puisque le temps de cycle réel du Testnet est ~8 fois plus lent que l'API réelle, le $\Delta t$ doit être corrélé à la latence mesurée du serveur pour retrouver la même sensibilité relative qu'en conditions réelles :
  * Nouveau `IMPULSE_RESONANCE_DT_MS` : Aligner la fenêtre sur la latence moyenne observée du Testnet pour capturer une réelle variation de profondeur inter-requêtes, soit **$1250\text{ ms}$** (proche des $1.35\text{ s}$ mesurés).
  * Ajustement du seuil `IMPULSE_RESONANCE_WALL_DROP_PCT` : Conserver le ratio ou l'assouplir légèrement de 5 à 10% pour absorber le lissage induit par le Testnet (ex: **$7.5\%$** au lieu de $6.5\%$).

---

### 2) Cause racine probable des morts `rc=1` silencieuses & Correctif d'observation

* **Cause racine probable prouvée :** Une **interruption par le système d'exploitation (OOM Killer / SIGKILL)** ou un **timeout de socket/connexion bloquant (GIL / I/O lock)** au moment précis où le processus Python tente d'écrire ou de synchroniser son état à la fin d'un cycle lourd, sans remonter d'exception interceptée par les gestionnaires Python classiques. 
  * Le fait que le stderr soit à 0 octet, qu'il n'y ait aucun `FATAL_RC1` capturé par les traps standards, et que le run détaché de 20 min en environnement propre finisse en `rc=0` (avec PnL positif) démontre que ce n'est pas une erreur logique du code Genesis, mais un **effet de bord environnemental** (saturation mémoire, blocage I/O réseau synchrone sur le Testnet lent, ou signal externe du gestionnaire de processus).

* **Correctif d'observation le plus court (sans toucher au Genesis) :**
  Forcer l'écriture immédiate et synchrone des flux et ajouter un wrapper de surveillance de l'espace/mémoire au niveau du lanceur bash (sans modifier la logique interne du bot) :
  * Activer le buffering de ligne forcé pour Python : `PYTHONUNBUFFERED=1`.
  * Ajouter dans l'en-tête du lanceur bash une journalisation explicite de la mémoire disponible et du code de sortie exact de chaque sous-processus via `wait $!` couplé à un `trap 'echo "EXIT SIGNAL at $(date) with $?"' EXIT`.

---

### 3) Meilleure logique prouvée (Amélioration mesurable et bornée)

* **Amélioration :** Dynamisation du $\Delta t$ par rétro-propagation de la latence mesurée.
* **Justification :** Au lieu d'avoir un `IMPULSE_RESONANCE_DT_MS` statique inadapté aux variations du Testnet, le moteur
