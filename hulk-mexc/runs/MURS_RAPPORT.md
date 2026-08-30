# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T21:03Z — 69056 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_210248.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 138 | 482577.37 | 876977.29 | 447494.05 | 0 (0.0%) | 3 |
| BTCUSDT | 1320 | 435972.47 | 1924444.32 | 487532.86 | 41 (3.11%) | 97 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7973 | 91356.1 | 606419.6 | 95173.07 | 340 (4.26%) | 1043 |
| XLMUSDT | 130 | 72462.46 | 210677.64 | 67542.68 | 0 (0.0%) | 0 |
| ALGOUSDT | 130 | 54091.59 | 92198.5 | 50280.63 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6662 | 29796.86 | 63738.72 | 26215.3 | 233 (3.5%) | 624 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 131 | 27331.01 | 87814.07 | 28190.46 | 0 (0.0%) | 6 |
| JASMYUSDT | 131 | 22581.23 | 227011.04 | 8967.56 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 69056 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1699 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3546 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
