# 🔍 SNIFFER — Obsidian : dernières perles (31/08/2026)

**Mission Christophe** : « envoyer snifer pour dénicher dernières perles qui
intéressent obsidian et ce qu'on fait ». Sources : roadmap officiel, changelog,
forum/Reddit, guides d'automation de référence.

---

## 1. LE ROADMAP OFFICIEL (obsidian.md/roadmap) — ce qui arrive

| Fonctionnalité | Statut | Intérêt ACE777 |
|---|---|---|
| **Kanban view pour Bases** | ACTIF | Nos chantiers/portefeuille en colonnes visuelles |
| **Calendar view pour Bases** | PLANIFIÉ | Veille/événements en calendrier |
| **Headless client pour Sync** | **LANCÉ (fév. 2026)** | **Sync sans app ouverte** → nos agents synchronisent le vault même si l'app est fermée — LA pièce qui complète la CLI |
| **Multiplayer** (notes partagées collaboratives) | PLANIFIÉ | Collaboration famille/agents en direct |
| **PDF annotation** | PLANIFIÉ (attend PDF.js) | Annotation de rapports PDF |
| **Bases support pour Publish** | PLANIFIÉ | Publier nos bases en site web |
| **Canvas support pour Publish** | PLANIFIÉ | Idem canvas |
| **Airtable import** | LANCÉ (août 2026) | Importer des tableaux externes → Bases |
| **Obsidian for Work** (contrôle plugins pour entreprises) | ACTIF | Si on industrialise |
| **Background Sync mobile** | PLANIFIÉ | — |

**La perle n°1** : le **Headless Sync** existe déjà (février 2026) — la CLI exige
l'app ouverte, mais Headless Sync permettrait de synchroniser le vault sur un
serveur/automatisé SANS l'interface graphique. Exactement le scénario « nos
agents écrivent même quand Obsidian est fermé ».

## 2. LE CHANGELOG RÉCENT (1.13 → 1.13.8, août 2026)

- **1.13 (juillet)** : Settings revampés (recherche + navigation clavier), zoom
  image plein écran, **URIs sécurisés** (confirmation avant action), Bases :
  redimensionner colonnes, drag de liens Base → file explorer.
- **1.13.6** : l'app attend la fin d'écriture des configs avant de quitter (anti-
  corruption), gestion des liens internes améliorée.
- **1.13.7 (12 août)** : fixes macOS (fichiers à caractères spéciaux), Electron
  v43.3.
- **1.13.8 (20 août)** : fix mobile.

→ Rien de bloquant pour nous ; la stabilité s'améliore. On est sur 1.13.7 ✅.

## 3. LE GUIDE D'AUTOMATION DE RÉFÉRENCE (Sébastien Dubois, août 2026) — les perles

Guide complet « Obsidian Automation → AI Operating System » (vault 20 000 notes,
400 AI Skills). **Confirme exactement notre architecture en 3 couches** :

```
Couche 1 — dans l'app : Templates, Daily notes, Bases, queries, boards
Couche 2 — autour du vault : git, CLI, REST, cron, sync, pipelines
Couche 3 — agents IA sur le vault : skills, hooks, MCP, multi-agents
```

**Les principes qui nous concernent DIRECTEMENT :**
1. **« Use exactly ONE sync mechanism »** — deux sync + un agent qui écrit =
   conflits et travail perdu. ⚠️ **Nous avons aujourd'hui 3 mécanismes** (OUTBOX
   manuel + obsidian-git + la CLI). Le plan A (basculer sur le pont) est la bonne
   direction : **un seul canal d'écriture (CLI), git en backup dessous**.
2. **« Automate the plumbing, not the thinking »** — les agents doivent classer,
   formater, croiser, résumer, nettoyer ; pas remplacer la réflexion. C'est notre
   modèle (les IA produisent, Hulk décide, Christophe valide).
3. **« Properties turn your vault into a database »** — frontmatter uniforme =
   tout requêtable (notre chantier B).
4. **« Start with three things »** : Templater (création de notes), filing
   automatique, Linter (propreté/cohérence) → couvre 80% de la friction.
5. **« The pattern that matters is a coding agent with your vault as its working
   directory, guided by an AGENTS.md and a library of AI Skills »** — exactement
   ce que kepano/obsidian-skills formalise (notre chantier H).
6. **« Git under everything before you let anything write to your vault »** — on
   l'a déjà (obsidian-git) ✅.
7. **« Automating too early is the biggest mistake »** — on a 1733 notes, donc on
   a la matière ; l'automation est légitime.

## 4. PATTERNS AGENTS DANS LE VAULT (Reddit r/ObsidianMD, 2026)

- **« Agent work needs visible process, not just final answers »** : dans Obsidian,
  un agent doit laisser une trace de CE QU'IL A FAIT (commande exécutée, fichier
  modifié), pas juste le résultat final → conforte notre journal d'audit du pont
  (`.ace777_bridge_audit.jsonl`) et les journaux de la maison.
- **« I moved the agents into my vault (open source) »** (juil. 2026) : des agents
  qui tournent DANS le vault (leur working directory = le vault), patterns
  reproductibles.
- **Vault comme « base layer d'un AI Operating System »** : le vault = mémoire
  persistante des agents (le chat oublie, le vault non) — c'est exactement notre
  philosophie ACE777 (Obsidian = cerveau collectif).

## 5. SYNTHÈSE — CE QUE ÇA CHANGE POUR NOUS

1. **Le plan A est validé par la communauté** : un seul canal d'écriture (CLI),
   git en backup. On est sur la bonne voie.
2. **Headless Sync** (existe déjà) : à explorer pour que nos agents écrivent même
   app fermée — complète la CLI.
3. **Kanban + Calendar views pour Bases** arrivent : ça rend la base Portefeuille
   (chantier C) encore plus attractive — colonnes de statut, calendrier de veille.
4. **Templater + Linter** : les 2 plugins à ajouter à notre stack (après Bases) —
   création de notes conforme + nettoyage automatique.
5. **Trace visible des agents** : notre pont a déjà l'audit — généraliser ce
   réflexe aux autres écritures IA.
6. **AGENTS.md + skills** : formaliser notre fonctionnement (la maison a déjà ses
   protocoles ; les skills kepano les rendraient portables).
