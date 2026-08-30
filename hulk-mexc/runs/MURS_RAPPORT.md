# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T19:01Z — 68530 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_190130.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 134 | 481097.62 | 876977.29 | 449548.0 | 0 (0.0%) | 3 |
| BTCUSDT | 1222 | 448135.77 | 1924444.32 | 476720.98 | 33 (2.7%) | 82 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7875 | 91466.82 | 606419.6 | 95449.12 | 335 (4.25%) | 1035 |
| XLMUSDT | 126 | 72056.68 | 210677.64 | 67142.08 | 0 (0.0%) | 0 |
| ALGOUSDT | 126 | 54422.94 | 92198.5 | 50507.75 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6564 | 29682.42 | 63738.72 | 26233.43 | 229 (3.49%) | 618 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 127 | 27459.41 | 87814.07 | 28243.41 | 0 (0.0%) | 6 |
| JASMYUSDT | 127 | 22779.94 | 227011.04 | 8955.09 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 68530 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1671 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3510 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
