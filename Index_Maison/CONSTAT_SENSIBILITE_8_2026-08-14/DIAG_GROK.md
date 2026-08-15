# DIAG FAMILLE GROK — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777 et en application stricte de la **Clause Permanente de Christophe** (*« Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible »*), voici mon diagnostic fondé sur les faits du contexte (14/08) et les réponses structurées aux quatre questions.

---

### 1) CAUSE RACINE DU 0.000000 (Faible taux de fill) ET RÉGLAGE PRÉCIS CHIFFRÉ

* **Cause racine prouvée :** Le décalage temporel entre la dynamique du Testnet (lenteur serveur à ~1.35 s/req, cycles bot à ~8 s) et l’hypothèse macro-structurelle du moteur (`IMPULSE_RESONANCE_DT_MS = 128` ms). Une fenêtre de 128 ms sur un serveur qui met plus d'une seconde à répondre et qui avance par vagues de liquidité provoque un **effet stroboscopique** : la rafale se produit et se résorbe entre deux snapshots depth, ou le bot capture le bruit de latence réseau plutôt que le vrai décrocheur de mur. C’est ce qui explique le paradoxe (BETA capture des ondes quand les vagues coïncident, mais ALPHA skippe massivement car le mur a déjà disparu 1 s plus tard).
* **Réglage précis et borné (variables d'environnement) :**
  * `IMPULSE_RESONANCE_DT_MS` : passer de `128` à **`1000` ms** (1.0 s). 
  * *Justification chiffrée :* Aligner la fenêtre d'observation sur le rythme réel des cycles du Testnet (~1 s à 1.35 s) permet d'englober la totalité d'une vague de liquidité au lieu de la sectionner aveuglément.
  * `IMPULSE_RESONANCE_WALL_DROP_PCT` : adapter le seuil de 6.5 à **`15.0` %** (ou proportionnel à la volatilité observée par vagues). 
  * *Justification chiffrée :* Sur une fenêtre élargie à 1000 ms, l'amplitude naturelle du bruit augmente ; un seuil de 6.5% générerait des faux positifs. Un seuil à 15% filtre le bruit de fond du Testnet tout en validant les véritables impulsions de rupture de carnet vues par BETA et ALPHA.

---

### 2) CAUSE RACINE PROBABLE DES MORTS RC=1 SILENCIEUSES ET CORRECTIF COURT

* **Hypothèse la plus probable :** Un **SIGKILL du noyau (OOM Killer ou timeout silencieux d'interpréteur)** ou un **blocage d'E/S bloquant (deadlock sur socket/pipe Bash)** lors d'une requête API Testnet en rupture de délai (rappel : pics de latence à 9.7 s sur le Testnet). Lorsque le processus dépasse le délai implicite du système ou que le tampon réseau sature sans renvoyer d'exception gérée dans la boucle principale, le processus disparaît proprement de l'espace utilisateur sans loguer de `stderr` ni déclencher de trap `ERR` standard (car l'arrêt est brutal ou externe).
* **Correctif court d'observation :** 
  * Activer l'instrumentation trap EXIT + DEBUG déjà validée, mais en y adjoutant **obligatoirement la journalisation du signal de fin (`SIGSEGV`, `SIGKILL`, `SIGTERM`)** dans un fichier externe hors-mémoire (ex: `echo $? > /tmp/last_exit_code`).
  * Forcer un `timeout` explicite au niveau de la commande de lancement Bash (ex: `timeout --signal=SIGABRT 15s python ...`) pour transformer tout gel silencieux en un `SIGABRT` visible qui dump la pile d'appels (`stderr` non nul garanti).

---

### 3) MEILLEURE LOGIQUE PROUVÉE (Amélioration mesurable et bornée)

* **Amélioration :** Introduire un **mécanisme de garde-fou adaptatif basé sur la latence mesurée du Testnet** (`latency_adaptive_gate`).
* **Preuve et mesure :** Plutôt que d'avoir un `DT_MS` statique qui devient obsolète dès que le Testnet tousse (1.35 s à 9.7 s), le paramètre temporel de résonance doit s'ajuster dynamiquement à la moyenne mobile des 5 derniers temps de réponse de l'API (`moving_avg_latency`).
* **Borne :** `DT_MS = clamp(moving_avg_latency, 500ms, 2000ms)`. Cela garantit que le bot ne rate plus les vagues en période de latence
