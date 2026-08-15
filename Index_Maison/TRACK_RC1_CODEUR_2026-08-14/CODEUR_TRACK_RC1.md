# CODEUR — traque ligne exacte rc=1 (14/08)

Provider: Puter Grok (gratuit)

**Réponse structurée (1-2-3-4)**

**1) Ligne / combinaison exacte probable + raisonnement ligne par ligne**

D’après les preuves (trap ERR jamais déclenché, stderr vide, « Done. » absent, 3-8 s après un SKIP, rc=1 explicite validé par TEST D), la sortie ne peut pas provenir d’une commande simple qui échoue sous `set -e`. Elle provient d’un **exit/retour explicite** (builtin `exit` ou `return 1` propagé au niveau top-level du script) exécuté pendant le cycle suivant le SKIP.

La zone la plus probable est **dans le bloc de calcul tension/momentum (≈1560-1660)**, plus précisément :

- un appel à un helper ruby (ou un sous-shell `$(ruby ...)` / `ruby helper.rb`) qui, sur certaines réponses API (réponse vide, JSON invalide, ou condition « tension trop faible »), fait un `exit 1` interne ;
- cet appel est placé **après** un `safe_call` qui a fait `set +e`, donc le rc=1 du ruby n’est pas intercepté par le trap ERR ;
- immédiatement après, ou dans le même bloc, une ligne du type `if [ $? -ne 0 ]; then exit 1; fi` (ou `return 1` dans une fonction appelée sans `|| true`) est atteinte.

Cette ligne n’est pas l’une des deux `exit 1` connues (367 BASE_URL et 1492 leverage) car celles-ci sont dans l’INIT. Elle se trouve dans la boucle (2146-2520) et n’a pas encore été instrumentée explicitement.

Preuves qui collent :
- 3-8 s de silence = temps typique d’un appel API + ruby + sleep court avant le log suivant ;
- rc=1 silencieux = comportement exact de `exit 1` (contrairement à une commande qui déclenche ERR) ;
- trap ERR jamais tiré = le chemin passe par un `set +e` temporaire ou par un `exit` builtin direct ;
- le pipeline master (`tail | bash -s | while read`) avec pipefail actif capte bien ce rc=1 et le remonte dans PROCESS_EXIT.log.

Le `while read` du master n’est pas la cause racine ; il est seulement le collecteur. Un SIGPIPE masqué ou un `read` sur stdin n’explique pas non plus un rc=1 propre.

**2) Correctif d’observation le plus court (à poser sans toucher la logique)**

Ajoute ceci juste après le `trap ERR` existant (vers la ligne 90, dans la partie exécutée par `tail -n +85`) :

```bash
trap 'rc=$?; echo "[EXIT] rc=$rc line=${BASH_LINENO:-?} cmd=${BASH_COMMAND:-?} func=${FUNCNAME[0]:-main} ts=$(date +%T)" >> /tmp/ace777_exit_trace.log; exit $rc' EXIT
```

Optionnel (très léger) pour la fenêtre du cycle :
```bash
shopt -s extdebug
trap 'echo "[DEBUG] line=$LINENO cmd=$BASH_COMMAND" >> /tmp/ace777_cycle_debug.log' DEBUG
```

Côté master (dans le lanceur, sans modifier le pipeline lui-même) :
```bash
set +e
tail -n +85 genesis | bash -s 2>&1 | while read line; do ...; done
BASH_RC=${PIPESTATUS[1]:-0}
echo "bash-s real_rc=$BASH_RC" >> /tmp/ace777_pipe_rc.log
```

Ces trois lignes captureront la ligne exacte + le vrai rc du `bash -s` au prochain incident. Pas de modification de flux, pas de `set -e` supplémentaire.

**3) Meilleure logique prouvée (clause permanente)**

La logique la plus solide et mesurable est : **rendre tout chemin de sortie explicite et traçable plutôt que de compter sur set -e + trap ERR**. Preuve : les 4 morts rc=1 sont toutes passées au travers du mécanisme actuel sans laisser de trace. Une seule amélioration bornée et mesurable :

- Objectif : 0 sortie rc=1 non tracée sur 7 jours consécutifs de run (mesuré par le compteur dans PROCESS_EXIT.log + /tmp/ace777_exit_trace.log).
- Moyen : le trap EXIT ci-dessus + un log unique « CYCLE_START #xxx » en tout début de boucle (avant tout appel réseau). Cela donne une borne temporelle et une ligne précise sans changer la logique PNL ni les safe_call.

C’est mesurable (nombre de rc=1 silencieux / jour), borné (ajout de <10 lignes d’observation), et prouvé par les 4 incidents du 14/08 qui n’ont laissé aucune trace dans le trap ERR.

**4) Réserves**

- Sans le fichier genesis complet (lignes 1560-1660 et les helpers ruby), je ne peux pas pointer le numéro de ligne exact ; l’analyse repose sur la structure et les preuves fournies.
- Le bug est intermittent (le run de 20 min à 10:32Z est sorti rc=0). Il est probablement lié à une condition rare sur les réponses API (volatilité, réponse vide, etc.).
- Le périmètre « genesis et lanceur intacts » est respecté : seules des lignes d’observation ont été proposées.
- Le moteur reste rentable (+126 USDT+ sur ~9 jours). On ne touche à rien d’autre tant que la ligne exacte n’est pas re-capturée.

Prêt à analyser le contenu de `/tmp/ace777_exit_trace.log` dès le prochain incident.
