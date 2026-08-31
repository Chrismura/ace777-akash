# SYNTHÈSE — Famille 3/3 : conception Base Portefeuille (31/08)

**Avis reçus** : gemini, juge, deepseek — 3/3. Convergence forte sur presque tout.

## 1. LES COLONNES (convergence 3/3 — le set minimal utile)
| Colonne | Type | Pourquoi |
|---|---|---|
| **actif** | titre/lien | le point d'ancrage |
| **statut** | select | où en est l'actif dans le pipeline |
| **bag_hulk** | oui/non ou $ | « skin in the game » en paper en un coup d'œil |
| **setup** (gemini: score_hulk / juge: conviction / deepseek: setup dominant) | select | le cœur du deepdive résumé en un mot-clé filtrable |
| **derniere_maj** | date | tuer les fiches périmées |
| **tags** | multi | filtrer par narratif (defi, rwa, l1...) |

**Exclus** : « jours depuis création », formules complexes — si une colonne ne dicte
pas une action, elle dégage.

## 2. LE PNL VIVANT (unanimité 3/3 — LE PIÈGE ÉVITÉ)
**NE PAS écrire le PnL temps réel dans le frontmatter des fiches** — c'est un
piège mortel : git pourri, conflits sync, perf dégradée, circuit breaker qui saute.
- La fiche actif = **référence stratégique** (deepdive, thèses, statuts) → métadonnées
  à mise à jour LENTE (statut, tags, conviction).
- Le PnL vivant reste dans **le cockpit/JSON** (le moteur Hulk) → suivi quantitatif brut.
- Option acceptée : **une note snapshot par jour** (`Hulk_Snapshot_YYYY-MM-DD.md`)
  ou un bloc dans la daily note avec le récap PnL. Pas d'écriture per-position en boucle.

## 3. STRUCTURE (unanimité 3/3) : UNE SEULE BASE
**`Portefeuille.base` unique** avec **multi-vues** :
- **Vue Table** : pilotage brut (tris par statut/PnL/date)
- **Vue Kanban** : colonnes = statut (Surveillance → Prêt → Bag actif → Archivé)
- **Signets X laissés de côté** (949 signets = du bruit dans un tableau de bord
  capital ; ils vivent dans leur flux de veille).

## 4. LA DIVERGENCE : que faire des 60 fiches existantes SANS frontmatter ?
- **juge** : injecter un frontmatter minimal par script, sinon la base affiche
  4 lignes et ignore 56 fiches → frustrant dès le premier jour.
- **deepseek** : ne PAS toucher au passé (Day Zero rule), la base se peuple
  organiquement avec les nouvelles fiches.
- **gemini** : migration propre en lot.

**Mon arbitrage Buffy** : le juste milieu — un script rapide (5 min, pas 3 jours)
qui injecte un frontmatter MINIMAL (`type: actif`, `statut: valide`, `date` du
fichier) sur les 60 fiches existantes, SANS les autres champs (bag/setup/tags se
peupleront organiquement). La base est utile dès le premier jour (juge) sans
sur-ingénierie (deepseek).

## 5. PLAN D'EXÉCUTION PROPOSÉ (à valider par Christophe)
1. Mettre à jour le template `actif` du gatekeeper : ajouter `bag_hulk`, `setup`,
   `derniere_maj` (avec valeurs autorisées).
2. Script d'injection : frontmatter minimal sur les 60 fiches existantes
   (`type: actif`, `statut: valide`, `date` du fichier).
3. Créer `Portefeuille.base` (filtre `type: actif`) avec vue Table + vue Kanban.
4. (Plus tard) snapshot PnL quotidien → note `Hulk_Snapshot_YYYY-MM-DD.md` ou
   bloc dans la daily note.
