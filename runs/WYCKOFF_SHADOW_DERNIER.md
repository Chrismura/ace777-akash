# Wyckoff SHADOW — simulation replay

> Tag: `MASTER_HYBRID_VF_20260708` | Filtre: `2026-07-08T16:25:07Z` | Mode: **lecture seule** (pas appliqué au live)
> Généré: `2026-07-08T16:38:24Z`

## Résultat global

| Métrique | Sans Wyckoff (réel) | Avec Wyckoff shadow |
|----------|---------------------|---------------------|
| Trades FILLED | 4 | 4 exécutés, 0 filtrés |
| PnL net | **3.1536 USDT** | **3.1536 USDT** |
| Delta | — | **+0.0000 USDT** |

- Pertes évitées (trades filtrés perdants): **0.0000 USDT**
- Gains manqués (trades filtrés gagnants): **0.0000 USDT**

## Détail des trades FILLED

| TS | Unité | Side | PnL | Wyckoff | Phase | Raisons |
|----|-------|------|-----|---------|-------|---------|
| 2026-07-08T16:27:35Z | ALPHA | BUY | 3.7800 | ALLOW | unknown |  |
| 2026-07-08T16:28:28Z | BETA | SELL | -0.0722 | BOOST | unknown | upthrust_short |
| 2026-07-08T16:31:34Z | ALPHA | BUY | -0.5542 | ALLOW | unknown |  |
| 2026-07-08T16:33:55Z | BETA | SELL | -0.0000 | BOOST | unknown | upthrust_short |

## Lecture

**Verdict simulation : neutre** — impact marginal (+0.00 USDT). À valider sur 2–3 cycles.

_Règles shadow : effort/résultat, spring/upthrust, filtre phase markup/markdown, chop sélectif._
