# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T04:07Z — 70924 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_040653.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 152 | 479425.59 | 876977.29 | 449015.1 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1223 | 177957.67 | 1966688.05 | 173753.47 | 14 (1.14%) | 59 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8322 | 91462.53 | 606419.6 | 94939.88 | 363 (4.36%) | 1087 |
| XLMUSDT | 144 | 72386.97 | 210677.64 | 67499.33 | 0 (0.0%) | 0 |
| ALGOUSDT | 144 | 53579.21 | 92198.5 | 49979.72 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7010 | 30210.16 | 63738.72 | 26156.93 | 250 (3.57%) | 651 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 145 | 27367.14 | 87814.07 | 28257.08 | 0 (0.0%) | 9 |
| JASMYUSDT | 145 | 21264.11 | 227011.04 | 8781.34 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 70924 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1781 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3706 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
