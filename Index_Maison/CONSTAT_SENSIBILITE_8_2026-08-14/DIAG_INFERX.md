# DIAG FAMILLE INFERX — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777 et en application stricte de la **Claude Permanente** (« Prouve la meilleure logique et applique-la dans la correction et l'amélioration »), voici le diagnostic rigoureux, fondé sur les faits et les métriques du contexte vivant (14/08/2026), ainsi que les recommandations bornées.

---

### 1) CAUSE RACINE DU FAIBLE TAUX DE FILL ET RÉGLAGE PRÉCIS

* **Cause racine prouvée :** Le décalage spatio-temporel (mismatch) entre la dynamique du Testnet et les paramètres d'impulsion. Le Testnet présente une latence serveur élevée (~1.35 s/requête) et se meut **par vagues** sur des fenêtres de temps macroscopiques. Le moteur utilise actuellement un delta temporel `IMPULSE_RESONANCE_DT_MS = 128` ms et un diviseur `IMPULSE_RESONANCE_WALL_DROP_PCT = 6.5`%. 
  * *Mécanique de l'échec :* Mesurer une chute de mur sur 128 ms dans un environnement où les cycles bouclent en ~8 s et où les requêtes prennent 1.35 s revient à échantillonner du vide la majeure partie du temps. Le décalage d'une seconde observé entre BETA et ALPHA (où BETA voit une chute de 70% et ALPHA, 1 s plus tard, ne voit plus que 6%) prouve que l'impulsion est réelle mais **manquée par sous-échantillonnage de la fenêtre temporelle**.

* **Réglage précis et chiffré (Variables d'environnement) :**
  Pour s'adapter à la latence mesurée du Testnet (~1.35 s par requête, cycles globaux de ~8 s), il faut élargir la fenêtre temporelle d'observation sans pour autant perdre la réactivité face aux vagues :
  1. `IMPULSE_RESONANCE_DT_MS` : Passer de `128` ms à **`1250` ms** (1.25 s, aligné sur la latence moyenne de la requête Testnet).
  2. `IMPULSE_RESONANCE_WALL_DROP_PCT` : Puisque la fenêtre est ~10 fois plus large, la chute cumulée du mur sur une vague sera mécaniquement plus importante et lissée. Pour éviter que le bruit ne déclenche des faux positifs tout en capturant les vagues observées (tensions 1 à 12), il faut ajuster le seuil de sensibilité de `6.5`% à **`15.0`%**.

---

### 2) CAUSE PROBABLE DES MORTS RC=1 SILENCIEUSES ET CORRECTIF COURT

* **Cause racine probable :** Un **Timeout d'I/O bloquant ou une saturation de buffer / SIGKILL implicite** (ex: OOM Killer ou blocage de socket réseau infini dans une requête `urllib`/`requests` vers le Testnet lent sans `timeout` explicite). 
  * *Preuve indirecte :* Le silence de 3 à 8 s après le dernier cycle loggé, l'absence de stderr (0 octet) et le `pipefail` du master qui s'arrête brutalement sur `rc=1` indiquent qu'une commande ou un appel bloquant au sein du cycle suivant a échoué silencieusement sans remonter d'exception interceptée par les traps `ERR` existants (parce que l'appel n'a pas retourné un code d'erreur bash, mais a été avorté ou a bloqué le processus au niveau de l'interpréteur Python/système).

* **Correctif court d'observation :**
  Ne pas toucher au genesis, mais renforcer l'interception au niveau du lanceur bash/enveloppe en forçant le traçage des descripteurs de fichiers et l'activation d'un timeout strict sur les boucles :
  * Ajouter `set -x` couplé à une redirection vers un fichier horodaté (`exec 2>> /tmp/ace777_stderr_debug.log`) dans l'enveloppe d'exécution du master.
  * Forcer un `timeout 15s` sur l'appel unitaire du cycle Python dans le lanceur pour transformer tout blocage silencieux (>15s) en un signal `SIGALRM` explicite capturable, plutôt qu'un `rc=1` fantôme.

---

### 3) MEILLEURE LOGIQUE PROUVÉE (CLASSE PERMANENTE)

* **Amélioration mesurable et bornée :** 
  Dissocier l'intervalle d'échantillonnage de l'impulsion (`IMPULSE_RESONANCE_DT_MS`) de la dureté de l'environnement d'exécution. 
  * *R
