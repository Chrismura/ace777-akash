# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T16:29Z — 67860 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_162842.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 129 | 479763.88 | 876977.29 | 449700.95 | 0 (0.0%) | 3 |
| BTCUSDT | 1097 | 460667.03 | 1924444.32 | 472066.86 | 28 (2.55%) | 61 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7750 | 91330.93 | 606419.6 | 95579.2 | 330 (4.26%) | 1024 |
| XLMUSDT | 121 | 71798.84 | 210677.64 | 67160.36 | 0 (0.0%) | 0 |
| ALGOUSDT | 121 | 54534.35 | 92198.5 | 50527.37 | 0 (0.0%) | 2 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6439 | 29525.56 | 63738.72 | 26132.7 | 222 (3.45%) | 612 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 122 | 27532.06 | 87814.07 | 28204.77 | 0 (0.0%) | 6 |
| JASMYUSDT | 122 | 22913.15 | 227011.04 | 9022.99 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 67860 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1637 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3468 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
