# SNIFFER DU VRAI — méthode (19/08/2026)

> Théorie de Christophe, validée : **le narratif (Twitter/news) = « ce qu'on veut
> que tu saches »**, c'est de la manipulation d'information (filtrée, retardée,
> orientée). **Le brut (mempool, blocs, ordres, code, usage réel) = la vérité.**
> Le signal = **la divergence** entre les deux.
> Étalon de la méthode : **la formule de la poussière** (CPFP + accumulation de
> poussière < 2 sat/vB + blocs privatisés) — on lit le mempool brut, pas les tweets.

## Les 3 couches

```
COUCHE 3 — NARRATIF   (Twitter, news, influenceurs)
          → « ce qu'on veut que tu saches » → jamais la vérité seule
COUCHE 2 — MESURABLE  (métriques calculées sur le brut : dust, CPFP, SOPR, whales)
          → objectif mais interprétable
COUCHE 1 — BRUT       (mempool, blocs, ordres, code, usage réel, papiers)
          → la source, ça ne ment pas
```

**Règle d'or** : toujours séparer les 3 couches, chercher la **divergence**.
Le narratif dit A, le brut dit B → c'est là qu'est le signal.

## Taxonomie des sources (par domaine)

| Domaine | Couche 1 (brut) | Couche 2 (mesurable) | Couche 3 (narratif) |
|---|---|---|---|
| Trading | mempool, blocs, ordres, flux whales | dust, CPFP, blocs privatisés, SOPR | Twitter, news, influenceurs |
| Hub IA | `usage.jsonl`, `hub_events.jsonl` | dispo, latence, justesse | catalogues, marketing providers |
| Dev | le code, les commits | tests, diff, typecheck | README, articles de blog |
| Veille | papiers arXiv, données officielles | benchmarks, métriques | articles de blog qui racontent |

## La poussière comme étalon (+ 2 améliorations à intégrer)

1. **Normaliser par le régime de frais** : la poussière n'apparaît que quand les
   frais sont bas. « Accumulation de poussière » doit se lire RELATIVE aux frais
   du moment, pas en absolu (sinon on confond accumulation et frais bas).
2. **Fondre les 3 cartes en un seul score** (comme la voilure ADA) : CPFP +
   dust + blocs privatisés → un indice « onchain » lisible, plutôt que 3
   observations séparées.

## Le prompt canon

`identity/prompts/divergence.json` — à injecter quand on sniffe un sujet.
Il force la famille à répondre en 4 temps : FAITS BRUTS → NARRATIF → DIVERGENCE
→ VERDICT. Priorité au brut, jamais recopier le narratif.
