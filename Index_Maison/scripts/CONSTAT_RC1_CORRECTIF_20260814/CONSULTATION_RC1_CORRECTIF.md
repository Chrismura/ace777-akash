# CONSULTATION RC=1 CORRECTIF


## Question
CONTEXTE (fait verifie par superviseur, 14/08/2026, run 4h testnet en cours) :

PROBLEME : le moteur ACE777 (bash genesis, set -euo pipefail) meurt en rc=1 SILENCIEUX
en plein cycle : zero FATAL_RC1, zero stderr, trap ERR jamais declenche. 4 morts
capturees aujourd'hui (12:06, 12:07, 12:14, 12:17 UTC) + 4 ce matin.

CAUSE RACINE PROUVEE (3 preuves) :
1) PREUVE MACHINE : la fonction swarm_neighbor_load() se termine par un SI dont la
   derniere commande peut retourner 1 :
     [ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1
   Quand la grace post-shockwave (20 cycles) est depassee, cette commande retourne 1
   -> la FONCTION retourne 1. Reproduit en harnais : cycle dans la grace = survit,
   cycle au-dela = meurt rc=1 SANS trap ERR (le genesis n'a pas set -E / errtrace,
   donc un echec DANS une fonction ne declenche pas le trap ERR du shell parent).
2) PREUVE CINETIQUE : crash dump 12:14 -> perte -8.60 -> "shockwave alpha->beta
   until_cycle=49" -> ALPHA meurt ~1 min apres, BETA meurt quand son cycle depasse
   until+grace(20). Timing cohérent.
3) PREUVE CONTRASTE : le run actuel tourne depuis 20+ min avec 0 shockwave -> 0 mort
   (les morts arrivent a 8-17 min quand des shockwaves sont broadcastées).

CHAINE DE LA MORT :
- perte/stop_loss -> swarm_broadcast_shockwave (ligne 2477) arme shockwave_until_cycle
- le voisin lit la telemetrie -> swarm_shockwave_until_cycle > 0
- quand cycle > until + grace -> le SI final retourne 1 -> swarm_neighbor_load retourne 1
- swarm_apply_coupling l'appelle SANS || (ligne 621) -> set -e tue rc=1
- pas de set -E -> trap ERR muet -> mort silencieuse

IMPORTANT : ce SI existe dans le VRAI champion scelle 37fca367 (md5 verifie) -> ce
n'est PAS un ajout exterieur, c'est un BUG LATENT : le champion gagnait -> pas de
pertes -> pas de shockwaves -> jamais declenche. Le testnet lent d'aujourd'hui
provoque des pertes -> le bug se reveille.

CORRECTIF PROPOSE (le plus propre) : ajouter "return 0" explicite a la fin de
swarm_neighbor_load() (la fonction fait du bookkeeping, elle ne doit JAMAIS etre
une source d'erreur). Alternative : "swarm_neighbor_load "$cycle" || true" a la
ligne 621. Option complementaire : set -E pour rendre les futures erreurs LOUD.

QUESTION : validez-vous le correctif "return 0" en fin de swarm_neighbor_load ?
Donnez : GO / GO AVEC RESERVES / NON + justification technique courte + meilleure
logique si vous en voyez une (contrainte : NE PAS casser le moteur rentable +126$).








## [gemini] (Google Gemini, 2.4s)
**GO AVEC RÉSERVES**

### Justification technique courte
Le correctif `return 0` en fin de `swarm_neighbor_load()` est le plus chirurgical et le plus sûr pour respecter la contrainte absolue (**ne pas casser le moteur rentable**). Il neutralise le piège du `set -e` sur la dernière évaluation booléenne d'une fonction de *bookkeeping* dont la valeur de retour n'a sémantiquement aucune portée logique sur la poursuite du cycle.

### Réserve(s) et Recommandation de déploiement
1. **La réserve (Défense en profondeur) :** Un simple `return 0` masque les erreurs réelles si la fonction venait à échouer pour une autre raison interne (ex: corruption de variable, division par zéro, etc.). Cependant, dans ce contexte bash sans typage strict, c'est le compromis acceptable pour stopper l'hémorragie immédiate.
2. **Le "Meilleur des deux mondes" (Option recommandée) :** 
   Pour blinder définitivement le moteur sans altérer sa cinétique rentable, appliquez **double protection** :
   * Ajoutez le `return 0` à la fin de `swarm_neighbor_load()`.
   * En même temps, sécurisez l'appel à la ligne 621 avec un `|| true` (ou un traitement d'erreur explicite) : 
     ```bash
     swarm_neighbor_load "$cycle" || true
   * *Optionnel (à étudier hors run critique)* : Activer `set -E` (errtrace) dans l'en-tête du genesis pour qu'à l'avenir, aucune erreur dans une fonction ne soit plus jamais silencieuse.


## [deepseek] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [juge] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [ultra] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [inferx] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [grok] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [nvidia] (NVIDIA build.nvidia.com (100+ modeles), 70.2s)
**GO AVEC RESERVES**

**Justification technique :**  
Le correctif `return 0` est valide et minimal, mais il masque le symptôme sans traiter la cause structurelle. La vraie faille est le pattern `[ condition ] && action` en fin de fonction, qui transforme un état métier (grace dépassée) en code retour d'erreur. 

**Meilleure logique (recommandée) :**  
```bash
# Dans swarm_neighbor_load(), remplacer le SI final par :
if [ "$post_delta" -le "$post_grace_i" ]; then
    swarm_shockwave_post_solo=1
fi
return 0  # Toujours succès pour le bookkeeping
```

**Pourquoi c'est mieux :**  
- Le `if` explicite rend l'intention claire (pas de dépendance au code retour de `[ ]`)  
- Le `return 0` devient redondant mais reste une ceinture de sécurité  
- Préserve la logique métier (la variable `swarm_shockwave_post_solo` est bien positionnée)  
- Ne change AUCUN comportement quand la grace est respectée (le champion scellé reste intact)

**Réserves :**  
1. **Ajouter `set -E`** en complément (ligne ~5 du genesis) pour que les futures erreurs dans les fonctions déclenchent le trap ERR → rend les bugs LOUD  
2. **Auditer les autres fonctions** se terminant par `[ condition ] && action` (grep `&&.*=1$` sur le code) — probablement 2-3 autres cas latents  
3. **Tester en harnais** : cycle dans grace + cycle au-delà + shockwave active → vérifier que le moteur survit et que `swarm_shockwave_post_solo` est bien positionné

**Impact rentabilité :**  
Aucun — le correctif ne touche que la fin de fonction, pas la logique de trading. Le champion scellé 37fca367 reste fonctionnel, on corrige juste un bug latent qui ne se déclenche qu'en conditions de pertes.


## [oss20] (ERR, 0s)
ERROR: HTTP Error 502: Bad Gateway


## [puter-grok] (Puter Grok (gratuit), 14.1s)
**GO**

### Justification technique courte

Le diagnostic est correct. Le pattern :

```bash
[ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1
```

retourne le code de sortie du test (`1`) quand la condition est fausse. Comme cette ligne est la dernière de `swarm_neighbor_load()`, la fonction retourne 1. Avec `set -e` et sans `set -E`, cet échec n’est ni piégé ni visible, ce qui explique la mort silencieuse.

Ajouter `return 0` en fin de fonction est la correction la plus propre et la plus sûre dans ce contexte :

- La fonction fait du *bookkeeping* / chargement d’état, pas une opération dont le code de retour a une sémantique métier.
- Elle ne doit donc **jamais** pouvoir faire planter le shell appelant via `set -e`.

### Recommandation d’implémentation (légèrement meilleure)

Plutôt que d’ajouter seulement `return 0` à la fin, je recommande de neutraliser explicitement le risque sur cette ligne :

```bash
if [ "$post_delta" -le "$post_grace_i" ]; then
    swarm_shockwave_post_solo=1
fi

return 0
```

Ou, version plus compacte mais tout aussi sûre :

```bash
[ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1 || true
return 0
```

### Points complémentaires (optionnels mais recommandés)

1. **Ajouter `set -E`** (errtrace) en plus du `return 0` est une bonne idée de défense en profondeur. Ça rendra les futures erreurs à l’intérieur de fonctions visibles via le trap ERR.
2. Sur la ligne 621 (`swarm_apply_coupling`), je mettrais quand même un `|| true` ou un `|| return 0` explicite sur l’appel de `swarm_neighbor_load`. C’est une ceinture + bretelles qui protège si jamais la fonction est modifiée plus tard.

Le correctif `return 0` ne change pas la logique rentable du moteur. Il supprime simplement un effet de bord involontaire de `set -e`.
