# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T08:10Z — 72104 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_080947.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 160 | 478841.01 | 876977.29 | 451639.63 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8543 | 91545.92 | 606419.6 | 94758.66 | 368 (4.31%) | 1107 |
| XLMUSDT | 152 | 72174.41 | 210677.64 | 67649.72 | 0 (0.0%) | 0 |
| ALGOUSDT | 152 | 53669.59 | 92198.5 | 50172.43 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7232 | 30547.84 | 63738.72 | 26114.54 | 258 (3.57%) | 665 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 153 | 27298.73 | 87814.07 | 27984.6 | 0 (0.0%) | 9 |
| JASMYUSDT | 153 | 23190.17 | 227011.04 | 8913.02 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 72104 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1810 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3767 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
