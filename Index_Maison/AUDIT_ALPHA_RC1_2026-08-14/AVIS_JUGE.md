# JUGE — juge.tranche

**VERDICT DU JUGE : GO AVEC RESERVES**

**Raison :** Le diagnostic forensique est précis et l'utilisation du piège `ERR` est la seule méthode saine pour capturer un `set -euo pipefail` sous Bash sans poser de pansement aveugle. La réserve porte sur l'urgence : il faut impérativement activer l'auto-relance pour BETA qui tourne à une jambe, en attendant le prochain crash capturé par le log.

---

### 1. Verdict diagnostic
**GO AVEC RESERVES** (voir motif ci-dessus).

### 2. Commande / mécanisme fautif le plus probable
Un **helper JSON / extraction numérique** (`json_get`, `num_*` ou un `ruby`/`python` d'évaluation rapide) exécuté lors du parsing de la réponse de l'API post-fill (ou pendant le calcul du shock_inversion_stop). 
* **Mécanisme :** Sous `set -euo pipefail`, si l'API renvoie un corps vide ou un JSON malformé pendant 1 seconde (ou un timeout partiel de curl), la substitution de commande `val=$(get_data ...)` ou la commande de parsing interne échoue, renvoie un code non nul, lève `set -e` et tue le script instantanément sans log d'erreur explicite (le stderr étant étouffé dans un `$(...)`).

### 3. Amélioration concrète de stabilité
**Implémenter un superviseur de processus robuste dans le lanceur (`launch_test_master...sh`) avec auto-relance immédiate et plafonnée (ex: max 5 restarts par session), couplé à un mode dégradé « 1 jambe » si un bot meurt définitivement.** 
* *Pourquoi :* Plutôt que de tolérer bêtement l'erreur (ce qui masque la dette technique), le lanceur doit agir en filet de sécurité pour que la mort d'ALPHA ne laisse pas BETA orphelin pendant 2 heures de run (neutralisant l'E-DUO).
