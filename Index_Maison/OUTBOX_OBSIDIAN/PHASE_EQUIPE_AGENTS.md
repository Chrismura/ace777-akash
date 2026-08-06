# Phase — Vraie équipe (troupeau d’agents)

**Statut :** 🟡 **chemin préparé** — pas d’install, pas de GO technique.  
**Pourquoi :** l’agora (Christophe · Cursor · Punk · Cortana · Gemini · Kimi…) tend vers une **équipe nombreuse**. C’est dans l’air du temps ; on prépare le rail **avant** d’empiler les process sur un Mac Air 8 Go.

Réf. : éval [[Evaluations/13_lumendriada_herdr]] · mindsets **M3 / P-Graph** · [[BRIEF_IA_SNIFF]] (vivant).

---

## Opinion (une phrase)
Oui, viser une vraie équipe est **juste** — à condition que le **coffre + coutumes + bus** restent la loi, et que le multiplexeur (herdr ou autre) ne soit qu’un **outil**, jamais le cerveau du trading.

---

## Ce qu’on a déjà (équipe embryo)
| Rôle | Qui | Canal |
|------|-----|-------|
| GO / risque | Humain | chat + Terminal |
| Code / plans | Cursor (± Gemini/Kimi) | workspace |
| Veille / sniff | Punk | `veille-punk` + BRIEF |
| Voix / attention | Cortana / `speak_attention` | bus Attention |
| Mémoire commune | Obsidian + `MEMOIRE_COLLAB` | coffre |
| Trading | ACE / Hulk | **hors** équipe froide — GO seul |
| Catalogue local | Ollama **Launch** (×9 : Claude, ChatGPT, Hermes, OpenClaw…) | **WATCH** — 1 à la fois, Mac froid · voir [[ARCHITECTURE_AGORA]] |

La « phase équipe » = **industrialiser** ça (plus d’agents, plus clairs), pas tout réécrire.  
**Schéma :** [[ARCHITECTURE_AGORA]] — oui utile pour fluidifier / vérifier plans de vol + console.

---

## Non-négociables (avant tout multiplexeur)
1. **Mac 8 Go** : 1 agent lourd à la fois en local ; le reste en cold / cloud / séquentiel.  
2. **Champion ACE** intouchable sans GO.  
3. **Coffre = vérité** (coutumes) — pas 5 chats qui divergent.  
4. **BRIEF_IA_SNIFF** vivant = nez commun de la veille.  
5. Pas de herdr / multi-agents **pendant** un run ACE ou Ollama OOM.

---

## Chemin en 4 marches (GO humain à chaque marche)

### Marche 0 — Doctrine (fait / en cours)
- AGORA · COUTUMES · OU_EST_QUOI · BRIEF · Attention · Journal.  
- **Critère :** un nouvel agent lit AGORA + BRIEF + CONSOLE et sait quoi faire.

### Marche 1 — Bus + rôles écrits (`GO equipe-1`)
- Fiche rôles figée (qui écrit où, qui a le droit de `say`, qui ne touche jamais `runs/`).  
- 1 template « brief de session » pour Gemini/Kimi (copier BRIEF + CONSOLE).  
- **Critère :** 2 IA externes sans se marcher sur les notes.

### Marche 2 — Orchestration légère (`GO equipe-2`)
- File de jobs froids : veille → note Attention → (option) Cursor.  
- Punk `suivi` / journal déjà là ; éventuellement daemon **seulement** si Mac froid.  
- **Critère :** un post → une note → une ligne mémoire, sans que tu redises le process.

### Marche 3 — Multiplexeur optionnel (`GO equipe-3` / herdr ou équivalent)
- Tester **herdr** (ou tmux+scripts) : 1–2 panes max, detach OK.  
- Plugins / marketplace = curiosité ; **zéro** plugin trading.  
- **Critère :** tu attaches/détaches sans tuer ACE ; RAM reste ≥ ~400 Mo hors run.

### Marche 4 — Équipe nombreuse (`GO equipe-4`) — plus tard
- Agents spécialisés : Judge, Sniff, Hygiène, Journal…  
- State sur disque (S6) + judge PASS/FAIL (M3).  
- Cloud / machine distante si le Mac Air sature.  
- **Critère :** N agents, **1** coffre, **1** BRIEF, **0** champion touché.

---

## herdr — place dans le chemin
| | |
|--|--|
| Utile ? | Oui **en marche 3**, comme terminal pour la meute |
| Urgent ? | Non — marches 0–2 d’abord (presque gratuits en RAM) |
| Risque | Trop d’agents locaux = OOM / chaleur alpage |

---

## Mot magique
| Mot | Effet |
|-----|--------|
| `GO equipe-1` | Rôles + template brief session |
| `GO equipe-2` | File jobs froids / durcir bus |
| `GO equipe-3` | Essai herdr (froid, 1–2 agents) |
| `GO equipe-4` | Spécialisation agents + state |

Pas de `GO equipe` global : **une marche à la fois**.

---

## Lien plan de vol
Cette phase vient **après** (ou en parallèle soft de) : Mac propre · sync · Hulk/ACE si GO · **pas** à la place de l’hygiène RAM.
