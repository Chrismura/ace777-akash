# Éval #5 — @0xSomni « agents = graphes pas giant prompts »

- **Date :** 2026-07-28
- **Compte :** [@0xSomni](https://x.com/0xSomni) — petit compte (~67 followers), format répétitif « this paper is f*cking brilliant »
- **Post :** production AI agents = **graphs** (état typé, nœuds, arêtes, checkpoints) ; le modèle ne pilote plus le workflow

## Analyse classique (archi agents)

| | |
|--|--|
| Idée technique | **VRAIE / mature** — LangGraph & co : StateGraph, conditional edges, Postgres checkpointer |
| Packaging tweet | **Hype** (« fucking brilliant ») — l’idée n’est pas nouvelle en 2026 |
| Lien leopardracer « graphes > boucles » | **Même famille** — on l’avait déjà classé SEMI-VRAI |

### Vulgarisé
- **Boucle / giant prompt** = un LLM qui improvise la suite (« encore un tool… »). Fragile.
- **Graphe** = plan fixé : cases (nœuds) + flèches (qui décide la suite). L’IA juge *parfois* ; les outils déterministes font le travail.
- **Checkpoint** = sauvegarde à chaque case → crash Mac / restart → on reprend (très « alpage »).

## Pour ACE777 / swarm

| | |
|--|--|
| Hot path champion | **Déjà déterministe** — ne pas remplacer par LangGraph |
| Cold path (Punk, veille, Index, Cortana) | **Oui inspiration forte** — graphe : digest → score → note Obsidian → gate |
| Swarm ACE/Hulk/Cortana/Punk | **Oui** — jambes = nœuds ; bus / STOP = arêtes ; state.json = checkpoint soft |

**Règle d’or déjà vôtre :** le modèle ne contrôle pas le workflow fills. Le tweet dit la même chose avec du jargon CS.

## Autres posts du compte (coup d’œil)

| Post | Verdict |
|------|---------|
| 4 agents LLaMA trade TSLA/BTC « +55% » | **Sceptique** — paper marketing, pas edge ACE |
| PCA pairs Pologne / LSTM | Leçon utile : **simple > fancy** en régime shift |
| DL 50–100 stocks Chine 9j max | Curiosité quant, hors scope |
| Desk 6 agents quant research | Idée org cold path OK |
| Cours Google / Anthropic agents | Formation OK |

→ Compte = **agrégateur hype papers** ; on pêche l’idée graphe, on jette les PnL miracles.

## Décision

- **Garder :** graphe + checkpoints + outils déterministes aux nœuds (archi swarm / Punk / Index).
- **Guillemets piste :** « Agent graph / harness » (avec Polymarket, Index).
- **Ne pas :** réécrire ACE en LangGraph demain.
