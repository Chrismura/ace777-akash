# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T02:06Z — 70376 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_020555.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 148 | 481642.3 | 876977.29 | 447833.94 | 0 (0.0%) | 5 |
| BTCUSDT | 1476 | 420648.57 | 1924444.32 | 487976.55 | 49 (3.32%) | 124 |
| ETHUSDT | 1123 | 179403.7 | 1966688.05 | 175004.46 | 13 (1.16%) | 56 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8219 | 91438.93 | 606419.6 | 94880.05 | 357 (4.34%) | 1073 |
| XLMUSDT | 140 | 72651.0 | 210677.64 | 67430.84 | 0 (0.0%) | 0 |
| ALGOUSDT | 140 | 53725.3 | 92198.5 | 49918.93 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6908 | 30056.24 | 63738.72 | 26179.82 | 245 (3.55%) | 643 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 141 | 27184.99 | 87814.07 | 28184.85 | 0 (0.0%) | 8 |
| JASMYUSDT | 141 | 21676.01 | 227011.04 | 8830.21 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 70376 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1754 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3666 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
