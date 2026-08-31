# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T09:10Z — 72472 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_091025.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 162 | 479003.73 | 876977.29 | 452046.07 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8613 | 91566.6 | 606419.6 | 94498.98 | 371 (4.31%) | 1117 |
| XLMUSDT | 154 | 72169.2 | 210677.64 | 67691.53 | 0 (0.0%) | 0 |
| ALGOUSDT | 154 | 53614.17 | 92198.5 | 50240.22 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7302 | 30636.41 | 63738.72 | 26114.65 | 262 (3.59%) | 668 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 155 | 27482.65 | 87814.07 | 27916.31 | 0 (0.0%) | 9 |
| JASMYUSDT | 155 | 24445.24 | 227011.04 | 8906.54 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 72472 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1819 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3781 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
