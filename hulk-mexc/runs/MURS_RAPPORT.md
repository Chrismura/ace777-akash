# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T05:08Z — 71195 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_050734.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 154 | 478151.41 | 876977.29 | 449707.57 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8372 | 91478.44 | 606419.6 | 95033.68 | 365 (4.36%) | 1091 |
| XLMUSDT | 146 | 72397.8 | 210677.64 | 67629.45 | 0 (0.0%) | 0 |
| ALGOUSDT | 146 | 53609.22 | 92198.5 | 50038.45 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7061 | 30274.08 | 63738.72 | 26143.83 | 251 (3.55%) | 655 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 147 | 27428.39 | 87814.07 | 28186.61 | 0 (0.0%) | 9 |
| JASMYUSDT | 147 | 21088.67 | 227011.04 | 8789.58 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 71195 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1786 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3722 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
