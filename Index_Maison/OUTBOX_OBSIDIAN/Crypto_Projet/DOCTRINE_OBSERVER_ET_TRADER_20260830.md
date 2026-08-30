# 🗿 DOCTRINE — OBSERVER ET TRADER EN MÊME TEMPS (gravée 30/08/2026 par Christophe)

> **RÈGLE PERMANENTE. À lire AVANT toute décision sur un actif du portefeuille.**
> Ce document ne se supprime pas. Toute IA qui reprend le système doit le lire et l'appliquer.

---

## 1. LA RÉALITÉ (ce que Christophe dit, sans filtre)

**TOUS les actifs du portefeuille de Hulk sont SOUS OBSERVATION. C'est LE but du portefeuille.**

On n'arrive pas à avoir des données propres et suffisantes pour faire un **set-up définitif**.
Et c'est peut-être normal : **le set-up ne sera jamais statique** — le marché change, et les
actifs changent de comportement avec lui.

## 2. LA CONSÉQUENCE : on fait LES DEUX en même temps

| On fait | Pourquoi |
|---|---|
| **ON TRADE** | Impossible de garder les actifs en observation pure avec tout ce qu'il faut — on trade pendant qu'on observe |
| **ON OBSERVE** | On capte les données complètes (prix, murs, poussière, régimes, corrélations) pour comprendre chaque actif |
| **ON MODIFIE AU FUR ET À MESURE** | Le set-up de chaque actif évolue avec son comportement observé — jamais figé |

→ **C'est pareil pour TOUS les actifs.** Chaque actif a sa fiche avec son étude de cas
particulier, mise à jour en continu.

## 3. CE QUE ÇA CHANGE CONCRÈTEMENT (les règles qui en découlent)

1. **Aucun actif n'est « hors observation »** : être tradé par Hulk ≠ ne pas être observé.
   Un actif en position est AUSSI un actif en observation (on mesure son comportement réel).
2. **Aucun set-up n'est définitif** : chaque fiche d'actif documente son set-up ACTUEL +
   l'historique des mesures (jour 1, jour 2, jour 3...) pour voir l'évolution.
   La fiche de RED (`SETUP_OPERATIONNEL_RED`) est le MODÈLE : mesure du jour, comparaison
   jour par jour, ajustement au fur et à mesure.
3. **La donnée complète de qualité est ESSENTIELLE** : c'est ce qui permet d'adapter les
   set-ups au comportement réel au lieu de les figer sur 3 jours de données.
4. **On ne bloque pas un trade par manque de set-up** : on trade avec le set-up du moment,
   on observe, on améliore. L'observation n'est pas un préalable au trading — c'est un
   compagnon permanent du trading.
5. **Chaque actif = une étude de cas unique** : pas de copier-coller de set-up entre actifs
   (chaque token a sa structure de carnet, son teneur de marché, son cycle horaire).

## 4. LE PROTOCOLE (comment on l'applique)

- **Fiche par actif** dans `Crypto_Projet/` (ex : FICHE_PATTERN_SETUP_RED, SETUP_OPERATIONNEL_RED).
- **Mesure répétée** : script `suivi_setup_red.py` + plist quotidienne (même heure = comparable).
- **Comparaison jour par jour** : on ne supprime jamais les lignes passées — l'évolution fait foi.
- **Révision périodique** : point ensemble sur chaque actif (ex : 7 jours) pour ajuster le set-up.
- **Tout est journalisé** dans `Journal_*.md` + archivé git.

## 5. RAPPEL (ce que Christophe a dit mot pour mot)

> « Tout les actifs que nous avons dans le portefeuille de hulk sont sous observation, c le
> but, car on arrive pas a avoir des données propre suffisante pour faire un set up définitif,
> et peut-être en fait que le set up ne sera pas statique car le marché change et les actifs
> aussi de comportement. Donc on fait les deux : on trade (car impossible de les avoir en
> observation avec tout ce qu'il faut), et on observe, et on modifie au fur et a mesure. Et
> c pareil pour TOUS les autres actifs. Chaque actif aura sa fiche avec son étude de cas
> particulier. Les données complètes de qualité sont essentielles et nous servent. »

---

*Grave le 30/08/2026. À relire à chaque session. Ne pas supprimer.*