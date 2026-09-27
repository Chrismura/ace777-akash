# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-09-27T15:54Z — 83620 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260927_155350.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 1332 | 474485.58 | 2078362.86 | 463956.25 | 0 (0.0%) | 48 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 1324 | 80073.29 | 312328.07 | 71683.13 | 0 (0.0%) | 47 |
| ALGOUSDT | 1324 | 52117.67 | 150831.98 | 50288.11 | 0 (0.0%) | 37 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| GOLD(PAXG)USDT | 1325 | 30174.53 | 191387.78 | 28697.95 | 0 (0.0%) | 103 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| JASMYUSDT | 1323 | 17032.15 | 239378.61 | 11716.22 | 0 (0.0%) | 9 |

## Synthèse
- **Total mesures** : 83620 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.2% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 4231 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
