# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T23:04Z — 69587 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_230400.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 142 | 479846.82 | 876977.29 | 446938.31 | 0 (0.0%) | 3 |
| BTCUSDT | 1419 | 426652.54 | 1924444.32 | 489302.07 | 44 (3.1%) | 110 |
| ETHUSDT | 976 | 183547.03 | 1966688.05 | 176713.16 | 10 (1.02%) | 39 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8072 | 91404.47 | 606419.6 | 95047.09 | 349 (4.32%) | 1052 |
| XLMUSDT | 134 | 72649.82 | 210677.64 | 67593.58 | 0 (0.0%) | 0 |
| ALGOUSDT | 134 | 53930.21 | 92198.5 | 49760.81 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6761 | 29915.79 | 63738.72 | 26210.78 | 239 (3.53%) | 634 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 135 | 27222.39 | 87814.07 | 28017.03 | 0 (0.0%) | 7 |
| JASMYUSDT | 135 | 22225.13 | 227011.04 | 8910.38 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 69587 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1726 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3591 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
