# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T07:39Z — 71915 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_073926.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 159 | 478483.94 | 876977.29 | 451601.02 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8507 | 91501.03 | 606419.6 | 94784.35 | 367 (4.31%) | 1104 |
| XLMUSDT | 151 | 72232.61 | 210677.64 | 67609.08 | 0 (0.0%) | 0 |
| ALGOUSDT | 151 | 53675.5 | 92198.5 | 50138.65 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7196 | 30492.02 | 63738.72 | 26097.99 | 257 (3.57%) | 664 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 152 | 27337.2 | 87814.07 | 28032.28 | 0 (0.0%) | 9 |
| JASMYUSDT | 152 | 21851.39 | 227011.04 | 8868.92 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 71915 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1805 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3759 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
