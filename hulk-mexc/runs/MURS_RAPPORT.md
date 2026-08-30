# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T20:02Z — 68808 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_200206.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 136 | 481984.16 | 876977.29 | 449456.44 | 0 (0.0%) | 3 |
| BTCUSDT | 1274 | 438305.4 | 1924444.32 | 483889.71 | 34 (2.67%) | 91 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7927 | 91434.81 | 606419.6 | 95343.98 | 336 (4.24%) | 1038 |
| XLMUSDT | 128 | 72191.86 | 210677.64 | 67107.04 | 0 (0.0%) | 0 |
| ALGOUSDT | 128 | 54311.33 | 92198.5 | 50552.95 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6616 | 29744.42 | 63738.72 | 26224.43 | 232 (3.51%) | 621 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 129 | 27360.31 | 87814.07 | 28190.73 | 0 (0.0%) | 6 |
| JASMYUSDT | 129 | 22756.53 | 227011.04 | 8983.64 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 68808 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1682 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3529 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
