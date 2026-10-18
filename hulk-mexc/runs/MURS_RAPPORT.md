# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-10-18T03:17Z — 90492 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20261018_031650.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 2095 | 459212.91 | 2078362.86 | 444704.05 | 0 (0.0%) | 92 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 2087 | 85447.14 | 312328.07 | 72146.02 | 0 (0.0%) | 72 |
| ALGOUSDT | 2088 | 49049.75 | 180103.2 | 44473.0 | 0 (0.0%) | 66 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| GOLD(PAXG)USDT | 2089 | 29713.46 | 191387.78 | 29070.99 | 0 (0.0%) | 163 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| JASMYUSDT | 2087 | 15686.88 | 239378.61 | 11651.5 | 0 (0.0%) | 16 |

## Synthèse
- **Total mesures** : 90492 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.0% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 4631 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
