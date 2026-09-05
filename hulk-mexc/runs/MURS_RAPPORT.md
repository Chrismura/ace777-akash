# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-09-05T15:08Z — 75179 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260905_150820.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 394 | 500469.8 | 1131378.99 | 486764.29 | 0 (0.0%) | 8 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 386 | 73145.64 | 312328.07 | 66115.5 | 0 (0.0%) | 7 |
| ALGOUSDT | 386 | 54958.15 | 93941.7 | 50548.55 | 0 (0.0%) | 10 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 387 | 27614.13 | 87814.07 | 28966.99 | 0 (0.0%) | 25 |
| JASMYUSDT | 386 | 25003.59 | 239378.61 | 10684.76 | 0 (0.0%) | 2 |

## Synthèse
- **Total mesures** : 75179 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3891 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
