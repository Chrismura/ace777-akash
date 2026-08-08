# Éval #10 — @undefinedKi « Graph Engineering / Anthropic method » + `judge.sh`

- **Date :** 2026-07-28
- **Compte :** [@undefinedKi](https://x.com/undefinedKi)
- **Post / article :** *Graph Engineering: an Agent That Reviews Its Own Work. The Anthropic Method (Full Guide)*  
  https://x.com/undefinedKi/status/2080992300893675775
- **Snippet collé :** `judge.sh` — PASS/FAIL machine avant tout le reste

## Idée centrale

L’agent n’est pas « bête » — le **shape** du travail est faux.  
Boucle (modèle pilote) → dérive. **Graphe** (nœuds + state disque + gates) → visible, résumable, branches, checks déterministes.

Principe Anthropic cité : **ne pas patcher le code ; patcher le process** (rulebook) qui l’a produit.

## `judge.sh` (Step 1 — le plus important)

```bash
#!/bin/bash
# judge.sh <file>
FILE=$1
[ -s "$FILE" ] || { echo "FAIL: empty"; exit 1; }
grep -q "required_section" "$FILE" || { echo "FAIL: missing section"; exit 1; }
echo "PASS"; exit 0
```

| | |
|--|--|
| Job | Exit 0/1 **sans** que tu ouvres le fichier |
| Contenu démo | Non-vide + section requise |
| Vrai usage | Wrap tests / schema / patterns interdits ; fuzzy → modèle oui/non |
| Step 2 article | **Casser** le judge exprès — s’il passe encore, il est aveugle |

### Vulgarisé
Avant de laisser l’IA écrire 40 fichiers : **comment une machine sait que c’est OK ?**  
Sinon l’agent s’arrête quand il « sent » que c’est fini = humeur, pas condition.

## Suite article (lu via API)

| Step | Contenu |
|------|---------|
| 3 | `rulebook.md` — croît ; jamais bypass main |
| 4 | Stress 3 items → diff → fixer règles → **delete** le travail |
| 5 | Queue/state **sur disque** (pas contexte) → kill/resume |
| 6 | 2 reviewers isolés + citation règle |
| 7 | Checks chers hors boucle ; cheap dedans |

Anecdotes packaging : Bun Zig→Rust, Python→TS, $ tokens — **SEMI** (récits Anthropic/Sumner/Krieger via article) ; principe graphe/gates = **VRAI**.

## Pour ACE / swarm / Punk

| Prendre | Laisser |
|---------|---------|
| **Judge avant worker** (CSV fills, paper gates, Punk check) | Remplacer champion ACE par graphe LLM |
| State disque / queue (style `state.json`, out/) | Croire migration Bun $165k = ton playbook demain |
| Rulebook qui grandit sur erreurs répétées | Hand-patch outputs agents en silence |
| 2 reviewers froid | Tout vérifier au LLM |

Aligné éval #5 (@0xSomni graphes) + culture ACE : **fills = vérité** = déjà un judge.

### `daemon.sh` (batch queue — aussi lu)

```bash
# while true: si queue/rebuild_requests non vide
#   → mv processing → rebuild.sh (1× pour le batch)
#   → test_affected.sh → logs/results.txt → rm processing
#   sleep 10
```

| | |
|--|--|
| Job | File d’attente **disque** : les reviewers demandent un rebuild ; un daemon traite le **lot** une fois |
| Vulgarisé | Pas 50 agents qui recompilent en même temps — une cloche, un passage, des tests, on range |
| Solide | Batch = coût check cher hors boucle (Step 7) · state visible · resume possible |
| Piège | Pas de lock/crash mid-`processing` dans le snippet · `sleep 10` = polling basique |

**Mindset / cold path :** OUI. Hot path champion : NON.

## Décision

- **VRAI (cadre)** — judge + rulebook + state disque = harness sérieux.  
- `judge.sh` démo = jouet ; pattern = **or**.  
- Pas de code ACE ; inspiration Punk / Index / paper Poly sniper (width = judge).
