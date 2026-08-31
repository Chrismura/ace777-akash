# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T00:05Z — 69863 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_000445.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 144 | 480312.11 | 876977.29 | 447525.64 | 0 (0.0%) | 4 |
| BTCUSDT | 1470 | 420861.86 | 1924444.32 | 488449.58 | 49 (3.33%) | 122 |
| ETHUSDT | 1028 | 181198.13 | 1966688.05 | 175293.99 | 12 (1.17%) | 47 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8124 | 91377.79 | 606419.6 | 94911.7 | 351 (4.32%) | 1057 |
| XLMUSDT | 136 | 72658.34 | 210677.64 | 67529.87 | 0 (0.0%) | 0 |
| ALGOUSDT | 136 | 53685.45 | 92198.5 | 49816.63 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6813 | 29935.92 | 63738.72 | 26165.57 | 241 (3.54%) | 640 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 137 | 27268.5 | 87814.07 | 27929.62 | 0 (0.0%) | 8 |
| JASMYUSDT | 137 | 22060.78 | 227011.04 | 8874.98 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 69863 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1740 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3628 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
