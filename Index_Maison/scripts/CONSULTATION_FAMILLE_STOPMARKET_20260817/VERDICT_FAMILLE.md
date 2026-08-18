# ⚖️ VERDICT FAMILLE — FILET DE SÉCURITÉ PHYSIQUE (STOP_MARKET BINANCE) — 17/08/2026

**Consultation :** 5 modèles consultés (gemini 6,8s · groq 8,2s [via Gemini fallback] · mistral 10,2s ·
huggingface 22,1s · nara 116s [via Gemini fallback]). NVIDIA : **timeout** (trop lent ce soir, non
rejoué). OpenRouter juge/ultra : non ciblés (fallback).
**Statut :** ✅ **GO-AVEC-RÉSERVE sur le PRINCIPE (5/5)** — mais **le seuil 5,1 bps est REJETÉ par
consensus (5/5)** et **le CANCEL est un pré-requis impératif (5/5)**.

## Le consensus famille (5/5, sans ambiguïté)

| # | Question | Consensus famille | Décision retenue |
|---|---|---|---|
| 1 | STOP_MARKET = la bonne solution ? | **OUI, indispensable** (5/5) — « déporter la sécurité sur l'exchange est la seule vraie façon de survivre si la boucle tousse » | **STOP_MARKET : GO** — mais SEULEMENT après avoir codé le CANCEL |
| 2 | Seuil 5,1 bps (~5,3 $) ? | **TROP SERRÉ (5/5)** — le bruit max mesuré est 5,10 $, le stop serait chassé en boucle (whipsaw) | **Stop physique à 8-10 bps (~8,3-10,4 $)** — filet anti-crash, pas coupure nominale |
| 3 | HARD_STOP_MULT=2.0 ? | **Partagé** : groq = cohérent avec le duo · mistral = réduire à 1,5 · gemini/nara = contradiction logique avec un stop physique fixe · huggingface = acceptable si filet secondaire | **À clarifier** : le stop exchange doit être ≥ au stop doublé, ou on sépare les 2 rôles |
| 4 | Amélioration ? | **Filet en cascade / séparation des rôles** (5/5 convergent) | Voir architecture retenue ci-dessous |

## 🎯 LA LEÇON MAJEURE DE LA FAMILLE (la vraie trouvaille)

**Ne mélange pas les deux rôles du stop.** La famille est unanime :

- **Le stop logiciel (rapide, intelligent)** = gérer le risque TACTIQUE : couper proprement à ~7 bps quand la boucle tourne bien (trailing, shockwave, fluid_exit).
- **Le STOP_MARKET Binance (physique, lent à modifier, sans cerveau)** = parer le risque SYSTÉMIQUE : le cygne noir, le flash crash, la boucle qui meurt. Il doit être **plus large** (8-12 bps) pour ne JAMAIS être déclenché par le bruit, et servir de **dernier recours absolu**.

Si tu mets le stop physique au même niveau que le stop logiciel (5,1 bps) → le bruit le déclenche en permanence, tu paies des frais pour rien, et tu casses la stratégie. **C'est le piège que la famille a vu en 5/5.**

## Architecture retenue (fusion des 5 avis)

### Phase 1 — PRÉ-REQUIS (avant tout STOP_MARKET)
1. **Coder `private_delete_order()` (CANCEL)** — la famille est formelle : « Pas de CANCEL = pas de STOP_MARKET. Point final. » (gemini, nara, groq, huggingface)
2. L'intégrer à TOUTES les branches de sortie (timeout, shockwave, fluid_exit, trailing, target) : annuler le stop d'abord, puis sortir.
3. Mode hedge : le STOP_MARKET doit porter `positionSide=LONG/SHORT` explicite (groq) sinon rejet ou exécution à l'envers.

### Phase 2 — LE FILET PHYSIQUE (ce qu'on code)
4. **`STOP_MARKET` à l'entrée avec `reduceOnly=true` + `positionSide`** à **8-10 bps** (~8,3-10,4 $) — décision famille (5/5).
   - Option famille (huggingface, mistral) : **`STOP_LIMIT`** avec price légèrement meilleur (×0,998) pour réduire le slippage — à tester côte à côte.
5. **Le stop logiciel reste le coupeur principal** à ~7 bps (intelligent, réagit au contexte) — le physique n'intervient que si le logiciel meurt ou est trop lent.

### Phase 3 — AMÉLIORATIONS (à débattre après le test)
6. **Trailing stop natif côté Binance** (`TRAILING_STOP_MARKET` avec callbackRate) — proposé par groq + mistral + huggingface : dès que la position est en profit, le stop suit côté exchange sans latence.
7. **Heartbeat anti-ordres-zombie** (huggingface) : alerte si un cancel n'est pas confirmé en X ms.
8. **Batch order atomique** (huggingface) : `fapiPrivatePostBatchOrders` pour ouvrir + stop en UN appel (zéro fenêtre sans protection).

## Décisions chiffrées après famille

| Paramètre | Proposition initiale | **Décision famille** |
|---|---|---|
| `DUO_HUNTER_STOP_LOSS_BPS` | 5,1 | **7 bps** (~7,3 $) — coupeur logiciel |
| `STOP_LOSS_BPS` / `SOFT_STOP_LOSS_BPS` | 5,1 | **7 bps** (~7,3 $) |
| **STOP_MARKET physique Binance** | 5,1 | **8-10 bps** (~8,3-10,4 $) — filet anti-crash |
| `DUO_HUNTER_HARD_STOP_MULT` | 2,0 | **GARDÉ à 2,0** (le duo soutient le scout) — mais le stop physique ≥ 10,2 bps max autorisé |
| CANCEL à chaque sortie | à coder | **PRÉ-REQUIS ABSOLU** |

## Réserves notées (suivi)

- **Nara (le plus dur)** : NO-GO sur les paramètres chiffrés — « 5,1 bps trop serré face au bruit 5,10 $ → whipsaw + ordres orphelins » → corrigé par la décision famille (7 bps logiciel / 8-10 physique).
- **Gemini** : « coder et tester le CANCEL AVANT d'écrire la moindre ligne de STOP_MARKET ».
- **Tous** : le spread testnet (1,70 $) fausse les mesures — valider le seuil réel en mainnet (0,10 $) avant la mise en prod.
- **Mistral** : proposait HARD_STOP_MULT=1,5 — retenu 2,0 (décision de Christophe + groq : cohérent avec l'ADN duo), à surveiller.

## SYNTHÈSE

Le principe (STOP_MARKET Binance) est **validé à l'unanimité** : c'est LA réponse à la latence (889 ms → 5,3 s) et au cas #157. MAIS la famille corrige deux choses : (1) **le seuil 5,1 bps est trop serré** — le stop physique doit être un filet large (8-10 bps), pas un scalpel ; le scalpel reste la boucle logicielle à 7 bps. (2) **le CANCEL est le pré-requis n°1** — sans lui, on crée des ordres orphelins pires que le problème initial. HARD_STOP_MULT=2,0 conservé (décision Christophe), cohérent si le stop physique est ≥ 10,2 bps max.

## ⚠️ NOTE ÉCONOMIE (décision Christophe, gravée dans REGLES_FAMILLE.md)

Ce round table a consulté **6 cerveaux — c'était EXCEPTIONNEL, ne plus refaire**. Règle n°1 :
**la consultation famille = 2 membres + le juge**, puis **Buffy + Christophe** décident ensemble.
