# DIAG FAMILLE ULTRA — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777, j'applique la **Claude Permanente** (prouver la meilleure logique et l'appliquer de manière mesurable et bornée). Voici le diagnostic rigoureux, appuyé sur les faits du contexte et l'architecture vivante, pour répondre aux deux questions liées et fournir l'amélioration attendue.

---

### 1) CAUSE RACINE DU FAIBLE TAUX DE FILL (0.000000 / skippage) & RÉGLAGE PRÉCIS

* **Cause racine :** 
  Le désalignement entre la cinétique du serveur Testnet (latence moyenne de **1.35 s/requête**, pics à 9.7 s, cycles de bot s'allongeant à ~8 s) et l'hyper-finesse des paramètres d'impulsion prévus pour un réseau rapide (API réel ~464 ms). 
  * Avec `IMPULSE_RESONANCE_DT_MS = 128 ms`, la fenêtre d'observation est plus courte que le temps de réponse brut du serveur Testnet. 
  * Résultat : l'instantanéité mesurée est un artéfact du délai de transport/réponse plutôt qu'une réalité de carnet. Lorsqu'une vague arrive, BETA l'attrape par chance (15 fills, +0.56$), mais 1 seconde plus tard, ALPHA se prend un mur virtuel vide ou un décalage de snapshot, menant systématiquement à un `0.000000` / `SKIP`.

* **Réglage précis et chiffré (Variables d'environnement) :**
  Puisque le Testnet tourne par vagues et présente une latence de ~1.35 s, les fenêtres temporelles doivent être dilatées proportionnellement pour capturer la véritable dynamique du carnet sans l'asphyxier :
  1. **`IMPULSE_RESONANCE_DT_MS`** : Passer de `128` à **`1200`** (1.2 s). Justification : cela se cale sur la latence moyenne réelle du serveur Testnet (1.35 s) pour garantir que deux snapshots consécutifs comparent bien deux états de carnet distincts et non le même retour en cache ou en timeout.
  2. **`IMPULSE_RESONANCE_WALL_DROP_PCT`** : Ajuster de `6.5` à **`12.0`** (ou 10.0). Justification : sur une fenêtre plus large (1.2 s), le volume de chute du mur lissé est naturellement plus grand. Doubler le seuil évite les faux positifs dus au bruit du Testnet tout en laissant passer les vraies impulsions fortes vues ce matin (tensions 6 à 11).

---

### 2) CAUSE RACINE PROBABLE DES MORTS RC=1 SILENCIEUSES & CORRECTIF COURT

* **Hypothèse la plus probable :**
  Une **interruption par signal externe de type SIGKILL (9)** ou une **erreur silencieuse de désallocation mémoire (OOM Killer / SIGSEGV)** au niveau du sous-processus python/bash, ou plus vraisemblablement un **timeout bloquant non intercepté** dans une requête bloquante (ex: appel `requests` ou socket sans `timeout` strict) qui finit par déclencher le `pipefail` ou un arrêt brutal sans laisser le temps au gestionnaire `trap` d'écrire sur `stderr`. Le fait que le run détaché de 20 min ait fini proprement à `rc=0` disculpe une faille intrinsèque du code métier, pointant vers une **saturation d'I/O ou un verrouillage de thread bloqué par la latence Testnet**.

* **Correctif d'observation le plus court (borné) :**
  Ne touchez pas au genesis. Injecter dans l'enveloppe du lanceur bash une redirection explicite et un tracing global du descripteur d'erreur et des signaux système :
  ```bash
  # Dans le lanceur master, forcer la capture du signal et de l'état avant la mort
  trap 'echo "[CRITICAL_TRAP] $(date -u +%FT%T) - Exit code: $?, Last command: $BASH_COMMAND" >> /tmp/ace777_rc1_postmortem.log' ERR
  ```
  Et s'assurer que l'appel Python lance le script avec un timeout global strict (`timeout 120s python ...`) pour convertir un blocage silencieux de 8s en un code de sortie explicite `rc=124` identifiable instantanément.

---

### 3) MEILLEURE LOGIQUE PROUVÉE (CLAUDE PERMANENTE)

* **Amélioration mesurable et bornée :**
  Implémenter un **Adaptateur de Latence Dynamique** basé sur la mesure empirique du
