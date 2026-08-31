# ÉTUDE COMPLÈTE — Obsidian dans son ensemble (pas seulement la CLI)

**Date** : 31/08/2026 — **Auteur** : Buffy (chef scientifique)
**Demande Christophe** : « étudier obsidian dans son ensemble pas que les cli ».
Complète `AUDIT_OBSIDIAN_CLI_20260831.md` (qui couvrait la CLI) par l'étude de
TOUT Obsidian : fonctionnalités core, Bases, Canvas, Properties, Templates,
Graph view, plugin ecosystem, Sync/Publish.

---

## 1. LES FONCTIONNALITÉS CORE D'OBSIDIAN (et notre état)

| Fonctionnalité | Rôle | Notre état | Potentiel ACE777 |
|---|---|---|---|
| **Éditeur Markdown + liens** | La base : notes .md reliées par wikilinks `[[note]]`, embeds `![[note]]`, callouts `> [!tip]` | ✅ utilisé | Standards à imposer dans nos fiches IA |
| **Properties (frontmatter YAML)** | Métadonnées structurées en tête de note (tags, statut, dates...) | ⚠️ partiel (signets oui, fiches crypto hétérogènes) | **Uniformiser : statut, actif, date, source, tags** → tout devient requêtable |
| **Bases (.base)** | Base de données intégrée : vues table/cards/list/map, filtres, formules, agrégats | ✅ plugin activé mais **0 base** | **Le gros potentiel** : portefeuille, veille, fiches en tableaux filtrables |
| **Canvas (.canvas)** | Toile visuelle : nœuds texte/fichier/lien/groupes reliés par arêtes | ❌ désactivé | Cartes mentales des connexions entre actifs, événements, institutions |
| **Graph view** | Visualisation des relations entre notes | ✅ activé (snippet ace777-graph-galactique) | **1341 notes orphelines** → graphe quasi vide, à relier |
| **Backlinks / Outgoing links** | Navigation par liens entrants/sortants | ✅ activé | Sera utile quand les fiches seront reliées |
| **Templates** | Modèles de notes réutilisables (variables date, titre...) | ❌ désactivé, **aucun template.json** | Modèles « Fiche actif », « Synthèse consultation », « Veille » |
| **Daily notes** | Note du jour automatique | ❌ désactivé | Journal des agents (daily:append) |
| **Command palette / Hotkeys** | Exécuter des commandes | ✅ activé | Accessible via CLI `command id=...` |
| **File recovery** | Historique local des versions | ✅ activé | `diff`/`history` via CLI — sauvegarde anti-catastrophe |
| **Sync (Obsidian Sync)** | Synchronisation chiffrée multi-appareils | ✅ activé (local) | Headless Sync possible (serveur sans GUI) |
| **Publish** | Publier un vault en site web | ❌ désactivé | Partager des fiches publiques ? |
| **Bookmarks** | Signets internes | ❌ désactivé | — |
| **Tag pane / Outline / Word count** | Panneaux auxiliaires | ❌ désactivés | Tag pane utile une fois les tags uniformisés |
| **Webviewer / Slides / Audio** | Divers | ❌ désactivés | — |

### Ce que j'ai appris sur les Bases (skill officiel kepano — la partie la plus riche)
Une base .base est un fichier YAML avec :
- **filters** : sélectionner les notes (par tag, dossier, propriété, date) avec
  opérateurs (==, !=, >, <, &&, ||, !) et fonctions (file.hasTag, file.inFolder,
  file.hasLink).
- **formulas** : propriétés calculées (ex: `days_until_due: '(date(due) - today()).days'`,
  `is_overdue: 'if(due, date(due) < today() && status != "done", false)'`).
- **views** : table, cards, list, map — avec order (colonnes), groupBy, summaries
  (Sum, Average, Min, Max, Median, Stddev, Earliest, Latest...).
- **Embed** : `![[MaBase.base]]` dans n'importe quelle note → la base s'affiche
  partout (ex: dans le cockpit des fiches !).

→ C'est un **Dataview natif**, sans plugin, pilotable par IA (la CLI sait
`base:create` et `base:query`).

### Ce que j'ai appris sur Canvas (skill officiel json-canvas)
Un .canvas est un JSON `{nodes, edges}` : nœuds text/file/link/group, arêtes avec
fromSide/toSide, couleurs preset 1-6. **Pilotable par IA** (écrire le JSON) →
cartes visuelles des connexions entre actifs/événements/institutions, actualisées
par nos agents.

---

## 2. LE PLUGIN ECOSYSTEM (communautaire) — ce qui nous manque

Installés : **obsidian-git** ✅ (backup auto) + **x-bookmarks** ✅ (signets X).

| Plugin | Rôle | Utile pour nous ? |
|---|---|---|
| **Dataview** | Requêtes SQL-like sur les notes (ex: `TABLE statut FROM #crypto`) | OUI — mais **Bases le remplace nativement** → privilégier Bases |
| **Templater** | Templates avancés avec scripts (vs Templates core simple) | OUI — modèles de fiches avec variables |
| **Tasks** | Gestion de tâches `- [ ]` avec requêtes | OUI — si on standardise les tâches des agents |
| **QuickAdd** | Capturer/ajouter des notes rapidement | Moyen — nos IA font déjà ça via scripts |
| **Periodic Notes** | Notes quotidiennes/hebdo/mensuelles | OUI — complète Daily notes |
| **Calendar** | Vue calendrier des notes périodiques | Confort |
| **Kanban** | Tableaux de bord (chantiers) | OUI — visualiser nos chantiers (CHANTIERS.md) |
| **Excalidraw** | Dessins/diagrammes dans le vault | Moyen — Canvas natif suffit |
| **Advanced Tables** | Édition de tableaux | Confort |
| **Local REST API** | API HTTP locale pour agents (mentionné par la famille) | À réévaluer si la CLI montre ses limites |
| **Advanced Graph View** | Graphe performant pour gros vaults (5k-50k notes) | Plus tard (vault 1733 notes) |
| **Metadata Menu** | Édition avancée des properties | Confort |

---

## 3. NOTRE CARTOGRAPHIE ACE777 → OBSIDIAN (usage à 100%)

### A. Nos 4 mondes actuels et leur meilleur support Obsidian
| Monde | Actuellement | Support Obsidian idéal |
|---|---|---|
| **Fiches actifs crypto** (60 dans Crypto_Projet) | .md hétérogènes | **Bases** : portefeuille filtrable (statut, actif, PnL, date fiche) + frontmatter uniforme |
| **Synthèses famille/Cortana** | .md dans OUTBOX → vault | Pont CLI (déjà fait) + **Templates** (modèle synthèse) + tags uniformes |
| **Signets X** (949) | x-bookmarks ✅ structuré | **Bases** : filtre par mois/veille/auteur |
| **Journal / veille** | journaux dispersés | **Daily notes** activé + `daily:append` des agents |

### B. Le plan « usage à 100% » (7 chantiers, mis à jour)
1. **A — Pont CLI** (fait, reste la bascule des ~15 scripts) → supprimer la synchro manuelle
2. **B — Frontmatter uniforme** partout (fiches, synthèses, journaux) : statut/actif/date/source/tags
3. **C — Bases Obsidian** : `Portefeuille.base` + `Veille.base` + `Signets.base` → tableaux vivants, embeds dans le cockpit
4. **D — Templates** : modèles « Fiche actif », « Synthèse consultation », « Veille » → les agents créent des notes conformes
5. **E — Daily notes + journal agents** : chaque agent append son activité du jour
6. **F — Hygiène du graphe** : wikilinks entre fiches (1341 orphelines → relier), tag pane activé
7. **G — Canvas cartes** : cartes visuelles actifs ↔ événements ↔ institutions (générées par IA via json-canvas)
8. **H — Skills kepano installés** : nos agents savent écrire du vrai markdown Obsidian (callouts, embeds, bases)

### C. L'architecture cible (simple)
```
Nos IA (Cortana, famille, agents)
   │  pont obsidian_cli_bridge.py (fait) + skills officiels (à installer)
   ▼
Obsidian ACE777 (vault 1733 notes)
   ├── Frontmatter uniforme (B) → tout requêtable
   ├── Bases (C) → tableaux vivants portefeuille/veille/signets
   ├── Templates (D) → notes conformes
   ├── Daily notes (E) → journal central chronologique
   ├── Wikilinks (F) → graphe utilisable
   └── Canvas (G) → cartes visuelles
   ▲
   │  obsidian-git (backup auto, déjà là) + file recovery
```

---

## 4. MON AVIS DE CHEF SCIENTIFIQUE
La CLI (déjà en place) est le **bras** — mais Obsidian complet est le **cerveau**.
Le saut qualitatif vient de **Bases + frontmatter uniforme** : nos fiches cessent
d'être des .md isolés et deviennent une base de données requêtable, visible en
tableaux dans l'app, embeds dans le cockpit. Ensuite Templates + Daily notes
standardisent la production des agents. Le graphe (1341 orphelines) se répare
tout seul quand les fiches sont reliées par wikilinks — c'est un symptôme, pas
une cause.

**Priorité révisée** : A (basculer les scripts, en cours) → C (la base
portefeuille — le premier tableau vivant) → B (frontmatter, en même temps que C)
→ D (templates) → E (journal) → F (wikilinks) → G (canvas) → H (skills).
