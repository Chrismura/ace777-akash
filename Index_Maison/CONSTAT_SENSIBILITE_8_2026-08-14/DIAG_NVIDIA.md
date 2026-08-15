# DIAG FAMILLE NVIDIA — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777, j'applique la **Claude Permanente** (« Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible »). Voici notre diagnostic rigoureux, fondé exclusivement sur les faits et les métriques du contexte vivant de ce 14 août 2026.

---

### 1) CAUSE RACINE DU 0.000000 (FAIBLE TAUX DE FILL) & RÉGLAGE PRÉCIS

* **Diagnostic & Preuve :** 
  Le moteur calcule la tension selon la formule $\text{chute de mur} / \text{IMPULSE\_RESONANCE\_WALL\_DROP\_PCT}$ (où le diviseur actuel est $6.5\%$) sur un delta temporel $\text{IMPULSE\_RESONANCE\_DT\_MS} = 128\text{ ms}$. 
  Or, le serveur Testnet présente une latence moyenne de $1.35\text{ s}$ par requête (allant jusqu'à $9.7\text{ s}$), allongeant les cycles du bot à ~8 s. 
  *Conséquence mathématique implacable :* Observer une variation de carnet sur une fenêtre de $128\text{ ms}$ sur un flux réseau/serveur dont le battement réel est de l'ordre de la seconde (vagues) revient à échantillonner du bruit ou à regarder une image fixe entre deux mouvements majeurs. C'est pourquoi BETA attrape par chance des vagues larges (15 fills), tandis qu'ALPHA (fenêtre plus rigide ou retardée de 1 s) ne voit plus que 6% au lieu de 70% et skippe systématiquement. Le $0.000000$ dans les CSV correspond aux périodes d'accalmie combinées à cet anachronisme d'échantillonnage.

* **Réglage chiffré et borné (variables d'environnement) :**
  Puisque le testnet bouge par vagues lentes et que les cycles tournent en ~8 s, il faut réaligner la fenêtre temporelle et le seuil sur la réalité physique mesurée du serveur :
  * `IMPULSE_RESONANCE_DT_MS` : passer de `128` à **`1000`** (1 seconde, ce qui correspond au battement minimal cohérent avec la latence testnet sans lisser excessivement les micro-chocs).
  * `IMPULSE_RESONANCE_WALL_DROP_PCT` : passer de `6.5` à **`4.0`** (abaisser légèrement le seuil de déclenchement pour compenser l'atténuation naturelle de la profondeur sur une période d'observation plus longue de 1 s).

---

### 2) CAUSE RACINE PROBABLE DES MORTS RC=1 SILENCIEUSES & CORRECTIF COURT

* **Diagnostic & Preuve :**
  Le profil des morts est univoque : 
  1. Dernier cycle loggé normal.
  2. Silence de 3 à 8 secondes (correspondant exactement à la durée d'une requête réseau bloquante ou d'un timeout sur le serveur testnet lent).
  3. Mort avec `rc=1` sans message sur `stderr` (`0` octet), sans trace dans `FATAL_RC1`, ni « Done. ».
  
  *Hypothèse la plus probable :* Il ne s'agit ni d'une exception Python non interceptée (qui écrirait sur `stderr`), ni d'une erreur de syntaxe, mais d'un **SIGKILL (signal 9) externe ou d'un OOM (Out Of Memory) discret du kernel**, ou plus vraisemblablement d'un **timeout de socket Python non géré** qui fait s'interrompre brutalement l'interpréteur sans remonter de stacktrace propre, combiné au `pipefail` du bash qui propage un code de retour non nul (`rc=1`). Le run détaché de 20 min ayant fini propre (`rc=0`) prouve que le code lui-même est sain : c'est l'interaction entre les latences extrêmes du testnet (> 9s max) et une primitive d'E/S bloquante sans timeout global qui provoque cette asphyxie.

* **Correctif court d'observation :**
  Ajouter un wrapper `timeout` explicite au niveau de l'appel de la commande de cycle dans le lanceur bash, et rediriger explicitement le flux pour ne rater aucun signal système :
  * Forcer l'interpréteur Python en mode unbuffered (`PYTHONUNBUFFERED=1`) pour que chaque `print`/log flush immédiatement avant un éventuel gel.
  * Ajouter un intercepteur de signaux système (`SIGTERM`, `SIGINT`, `SIGQUIT`) dans le script maître pour capturer l'origine exacte du kill s'il provient
