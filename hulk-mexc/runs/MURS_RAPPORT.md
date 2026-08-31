# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T03:06Z — 70654 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_030626.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 150 | 480609.47 | 876977.29 | 448437.18 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1175 | 178542.14 | 1966688.05 | 174285.2 | 13 (1.11%) | 58 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8271 | 91392.56 | 606419.6 | 94801.66 | 360 (4.35%) | 1077 |
| XLMUSDT | 142 | 72371.44 | 210677.64 | 67495.78 | 0 (0.0%) | 0 |
| ALGOUSDT | 142 | 53718.84 | 92198.5 | 49979.95 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6960 | 30132.93 | 63738.72 | 26162.89 | 248 (3.56%) | 650 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 143 | 27230.21 | 87814.07 | 28138.1 | 0 (0.0%) | 9 |
| JASMYUSDT | 143 | 21482.09 | 227011.04 | 8799.54 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 70654 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1768 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3686 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
