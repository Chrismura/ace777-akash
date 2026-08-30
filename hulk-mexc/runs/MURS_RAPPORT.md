# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T17:30Z — 68140 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_172938.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 131 | 480565.85 | 876977.29 | 449247.57 | 0 (0.0%) | 3 |
| BTCUSDT | 1150 | 456005.44 | 1924444.32 | 472953.5 | 29 (2.52%) | 72 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7803 | 91504.86 | 606419.6 | 95493.41 | 331 (4.24%) | 1026 |
| XLMUSDT | 123 | 71907.58 | 210677.64 | 67237.28 | 0 (0.0%) | 0 |
| ALGOUSDT | 123 | 54495.89 | 92198.5 | 50546.8 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6491 | 29588.43 | 63738.72 | 26180.17 | 226 (3.48%) | 616 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 124 | 27653.57 | 87814.07 | 28258.55 | 0 (0.0%) | 6 |
| JASMYUSDT | 124 | 22808.17 | 227011.04 | 9003.53 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 68140 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1649 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3486 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
