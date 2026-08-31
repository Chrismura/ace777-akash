# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T07:09Z — 71727 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_070902.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 158 | 478081.89 | 876977.29 | 451542.44 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8472 | 91490.42 | 606419.6 | 94862.85 | 367 (4.33%) | 1100 |
| XLMUSDT | 150 | 72240.85 | 210677.64 | 67549.4 | 0 (0.0%) | 0 |
| ALGOUSDT | 150 | 53714.23 | 92198.5 | 50104.29 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7160 | 30433.45 | 63738.72 | 26090.24 | 255 (3.56%) | 661 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 151 | 27399.57 | 87814.07 | 28071.07 | 0 (0.0%) | 9 |
| JASMYUSDT | 151 | 20848.67 | 227011.04 | 8856.45 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 71727 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1799 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3746 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
