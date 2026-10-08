# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-10-08T22:13Z — 87135 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20261008_221300.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 1722 | 474597.83 | 2078362.86 | 460065.03 | 0 (0.0%) | 65 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 1714 | 84362.67 | 312328.07 | 72565.9 | 0 (0.0%) | 65 |
| ALGOUSDT | 1715 | 49377.7 | 180103.2 | 46909.54 | 0 (0.0%) | 53 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| GOLD(PAXG)USDT | 1716 | 29992.42 | 191387.78 | 29122.91 | 0 (0.0%) | 139 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| JASMYUSDT | 1714 | 16688.25 | 239378.61 | 11748.42 | 0 (0.0%) | 12 |

## Synthèse
- **Total mesures** : 87135 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.1% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 4452 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
