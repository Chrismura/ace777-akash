# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T01:05Z — 70118 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_010528.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 146 | 482094.48 | 876977.29 | 446971.95 | 0 (0.0%) | 5 |
| BTCUSDT | 1476 | 420648.57 | 1924444.32 | 487976.55 | 49 (3.32%) | 124 |
| ETHUSDT | 1075 | 180062.77 | 1966688.05 | 174881.43 | 13 (1.21%) | 52 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8171 | 91372.67 | 606419.6 | 94899.84 | 356 (4.36%) | 1066 |
| XLMUSDT | 138 | 72643.29 | 210677.64 | 67420.81 | 0 (0.0%) | 0 |
| ALGOUSDT | 138 | 53706.18 | 92198.5 | 49851.65 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6860 | 29992.75 | 63738.72 | 26173.38 | 242 (3.53%) | 640 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 139 | 27173.34 | 87814.07 | 28280.92 | 0 (0.0%) | 8 |
| JASMYUSDT | 139 | 21869.48 | 227011.04 | 8850.03 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 70118 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1748 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3645 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
