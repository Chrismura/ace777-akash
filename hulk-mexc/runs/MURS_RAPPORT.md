# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T16:15Z — 73208 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_161500.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 176 | 480942.12 | 876977.29 | 456721.31 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8735 | 91589.48 | 606419.6 | 94098.44 | 376 (4.3%) | 1136 |
| XLMUSDT | 168 | 71766.87 | 210677.64 | 67759.36 | 0 (0.0%) | 1 |
| ALGOUSDT | 168 | 53651.67 | 92198.5 | 50229.42 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7424 | 30736.92 | 63738.72 | 26142.94 | 268 (3.61%) | 681 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 169 | 27184.43 | 87814.07 | 27749.66 | 0 (0.0%) | 9 |
| JASMYUSDT | 169 | 26515.45 | 239378.61 | 8962.02 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 73208 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3830 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
