# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T06:08Z — 71420 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_060828.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 156 | 477924.13 | 876977.29 | 450325.44 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8414 | 91445.54 | 606419.6 | 94995.62 | 366 (4.35%) | 1094 |
| XLMUSDT | 148 | 72183.43 | 210677.64 | 67544.8 | 0 (0.0%) | 0 |
| ALGOUSDT | 148 | 53703.94 | 92198.5 | 50014.06 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7103 | 30339.63 | 63738.72 | 26115.95 | 253 (3.56%) | 658 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 149 | 27449.6 | 87814.07 | 28114.72 | 0 (0.0%) | 9 |
| JASMYUSDT | 149 | 20903.83 | 227011.04 | 8814.74 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 71420 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1791 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3731 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
