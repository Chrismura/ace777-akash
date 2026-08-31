# AUDIT — Usage Obsidian ACE777 + CLI officielle (étude à 100%)

**Date** : 31/08/2026 — **Auteur** : Buffy (chef scientifique)
**Déclencheur** : Christophe a trouvé par hasard (signet X @KanikaBK) la CLI officielle
Obsidian → demande d'auditer notre usage et d'étudier comment l'utiliser à 100%.

---

## 1. AUDIT DE NOTRE USAGE ACTUEL (mesuré, pas théorique)

### 1.1 Le vault
- **1733 notes markdown, 117 MB** — un vrai cerveau collectif.
- **Structure** : 151 notes à la racine (00_*, 01_*, journaux...) + dossiers :
  Signets_X (949 !), Index_Maison (143), Archives_Signets (143), Evaluations (94),
  Crypto_Projet (60), Cahier (60), A_Mon_Attention (58), hulk-mexc (23),
  Swarm_Bus (21), Hulk (11), AUTO_EVOL (8)...
- **2 plugins** : obsidian-git (backup auto toutes les ~10 min, vérifié : commits
  réguliers), x-bookmarks (signets X → Signets_X/).
- **Tags existants** : #signet/x (142), #veille (75), #ace777 (58), #swarm (34),
  #journal (34), #veille/outils-agents (32), #auto (31)...

### 1.2 Comment nos IA écrivent dans Obsidian (LE POINT FAIBLE)
- ~15+ scripts écrivent dans `Index_Maison/OUTBOX_OBSIDIAN/` (**323 fichiers en
  attente**) : consulter_famille_*, thermo_quotidien, superviseur_auto, cockpit_mission_feed...
- La synchro OUTBOX → vault est une **liste manuelle de `cp`** (`_sync_now.sh`,
  checkup_garage.sh) + un git auto-sync.
- **Bugs déjà vécus** : « Obsidian ne bouge pas », dossiers qui ne remontent jamais
  (A_Mon_Attention bloqué au 07/08, AUTO_EVOL...). Chaque ajout de fichier à la
  synchro = un `cp` de plus à maintenir à la main → fragile par construction.

### 1.3 État des lieux fonctionnel
- ✅ obsidian-git : backup auto fonctionnel.
- ✅ x-bookmarks : signets X en frontmatter structuré (id, author, url, tweet_date).
- ⚠️ **Daily notes : NON activé** (`tasks daily` → « plugin not enabled »).
- ⚠️ **Bases : 0 fichier .base** (la nouvelle fonctionnalité base de données).
- ⚠️ **1341 notes orphelines** (sur 1733 !) — aucune note entrante → graphe inexploité.
- ⚠️ Frontmatter utilisé de façon hétérogène (signets oui, fiches crypto parfois).

---

## 2. ÉTUDE DE LA CLI OFFICIELLE (v1.12+, installée et VÉRIFIÉE sur notre machine)

### 2.1 Ce qui est confirmé fonctionnel chez nous (testé à l'instant)
- `obsidian search query=... limit=N` → ✅ (rapide avec limit)
- `obsidian read / create / append / prepend` → ✅
- `obsidian property:set name=... value=...` → ✅ (frontmatter par CLI !)
- `obsidian tags counts` → ✅
- **`obsidian eval code="app.vault.getFiles().length"` → ✅ = 1807** — on exécute
  du JavaScript DANS Obsidian → accès à TOUTE l'API (vault, metadata, canvas, bases).
- `obsidian bases / base:create / base:query` → ✅ (0 base pour l'instant)
- `obsidian orphans total` → ✅ (1341)
- `obsidian recents` → ✅
- `obsidian commands filter=...` → ✅ (toutes les commandes, y compris plugins)
- `obsidian themes / theme:set` → ✅
- `obsidian plugin:install id=...` → ✅ (installer un plugin par CLI !)
- `obsidian diff / history` → ✅ (file recovery)
- `obsidian daily` → commandes dispo mais plugin Daily notes à activer.

### 2.2 La formation officielle : kepano/obsidian-skills (GitHub, 19.1k★)
Repo du CEO d'Obsidian (Steph Ango) : 5 skills officiels pour agents IA —
**obsidian-markdown** (wikilinks, callouts, embeds, properties, mermaid, footnotes),
**obsidian-bases** (bases de données .base : vues table/cards/list/map, filtres,
formules), **json-canvas** (graphes visuels .canvas), **obsidian-cli** (tout ce
qu'on a testé), **defuddle** (extraction markdown propre des pages web).

### 2.3 Les capacités qui changent la donne pour ACE777
| Capacité | Ce que ça débloque |
|---|---|
| `eval` (JS dans l'app) | Requêtes complexes (ex: compter les fiches par statut), génération de rapports, **tout** ce que l'API Obsidian permet |
| `property:set/read` | Frontmatter piloté par IA → fiches structurées, filtrables |
| `base:create/query` | Nos fiches crypto deviennent une **base de données** (colonne statut, tags, dates, PnL...) |
| `command id=...` | Déclencher n'importe quelle commande Obsidian (y compris plugins) |
| `plugin:install` | Installer des plugins depuis la CLI |
| `daily:append` | Journal quotidien alimenté par les agents |
| `orphans/deadends/unresolved` | Hygiène du graphe : trouver les notes mortes |
| `diff/history` | File recovery : comparer/restaurer des versions |

---

## 3. LES AMÉLIORATIONS CONCRÈTES POUR ACE777 (classées par gain)

### A. Structurel (le plus important) — Remplacer la synchro manuelle
**Problème** : les `cp` manuels OUTBOX → vault sont la source des bugs « Obsidian ne
bouge pas ».
**Solution** : le pont `obsidian_cli_bridge.py` (déjà implémenté et testé) écrit
DIRECTEMENT dans le vault via la CLI. La synchro manuelle devient inutile pour les
nouvelles écritures. **Objectif : basculer les ~15 scripts un par un** (additif,
réversible), puis supprimer `_sync_now.sh` quand tout est migré.

### B. Frontmatter structuré partout (fiches pilotables)
Nos fiches crypto (60 dans Crypto_Projet) et synthèses gagneraient un frontmatter
uniforme : `status`, `actif`, `date`, `source`, `tags`. → filtrables, requêtables,
lisibles par les bases et par les IA. La CLI `property:set` le rend trivial.

### C. Bases Obsidian (la nouvelle base de données) — le gros potentiel
Créer une base `Portefeuille.base` (ou `Veille.base`) qui agrège nos fiches :
colonne = statut (en_observation/tradé/delisté), actif, PnL, date de fiche.
→ le tableau « score Hulk vs Hold » du cockpit pourrait être alimenté par une
vraie base Obsidian, visible et filtrable dans l'app.

### D. Daily notes + journal des agents
Activer le plugin Daily notes → les agents appendent leur activité du jour
(`daily:append`) → journal central chronologique, au lieu des journaux dispersés.

### E. Hygiène du graphe
1341/1733 notes orphelines → les wikilinks entre fiches (actif ↔ synthèse ↔
événement) rendraient le graphe utilisable et la navigation par liens réelle.

### F. Skills officiels installés pour nos IA
Installer kepano/obsidian-skills (npx skills add) → nos agents savent écrire du
vrai markdown Obsidian (callouts, embeds, wikilinks) au lieu de markdown brut.

### G. Cockpit → Obsidian (inverse)
Le cockpit (index.html) pourrait lire l'état Obsidian via la CLI (eval) pour
afficher des stats « vivantes » (nb fiches par statut, derniers signets...).

---

## 4. MON AVIS DE CHEF SCIENTIFIQUE
Le hasard de Christophe tombe pile sur notre plus vieux point faible : la synchro
manuelle. La CLI + le pont déjà en place règlent ça structurellement. Les Bases et
le frontmatter uniforme sont le « 100% » — ça transforme notre Obsidian de
dépotoir de notes en **base de données vivante pilotable par nos IA**.

**Priorisation proposée** : A (structurel, déjà lancé) → B+C (frontmatter + bases,
le plus gros gain pour la veille) → D (journal) → E (graphe) → F-G (confort).
