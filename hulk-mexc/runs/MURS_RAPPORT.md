# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-09-17T23:09Z — 80086 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260917_230846.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 939 | 505602.1 | 2078362.86 | 488280.03 | 0 (0.0%) | 21 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 931 | 74040.52 | 312328.07 | 66408.17 | 0 (0.0%) | 31 |
| ALGOUSDT | 931 | 55115.91 | 102465.26 | 50944.76 | 0 (0.0%) | 28 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 932 | 27378.0 | 98905.04 | 28126.33 | 0 (0.0%) | 74 |
| JASMYUSDT | 931 | 18639.63 | 239378.61 | 10678.04 | 0 (0.0%) | 6 |

## Synthèse
- **Total mesures** : 80086 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.3% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 4056 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
