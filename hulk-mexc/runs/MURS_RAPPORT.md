# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T15:58Z — 67730 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_155812.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 128 | 478705.06 | 876977.29 | 449129.18 | 0 (0.0%) | 3 |
| BTCUSDT | 1072 | 464481.48 | 1924444.32 | 473144.98 | 27 (2.52%) | 53 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7726 | 91426.76 | 606419.6 | 95442.51 | 329 (4.26%) | 1018 |
| XLMUSDT | 120 | 71805.1 | 210677.64 | 67113.31 | 0 (0.0%) | 0 |
| ALGOUSDT | 120 | 54593.79 | 92198.5 | 50611.98 | 0 (0.0%) | 2 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6415 | 29490.63 | 63738.72 | 26116.03 | 220 (3.43%) | 609 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 121 | 27068.37 | 87814.07 | 28266.5 | 0 (0.0%) | 6 |
| JASMYUSDT | 121 | 22948.48 | 227011.04 | 9012.25 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 67730 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1631 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3447 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
