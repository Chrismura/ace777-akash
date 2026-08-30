# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T16:59Z — 68004 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_165923.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 130 | 480133.23 | 876977.29 | 449765.22 | 0 (0.0%) | 3 |
| BTCUSDT | 1124 | 460259.46 | 1924444.32 | 471668.98 | 28 (2.49%) | 64 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7777 | 91396.66 | 606419.6 | 95528.54 | 331 (4.26%) | 1026 |
| XLMUSDT | 122 | 71891.94 | 210677.64 | 67221.16 | 0 (0.0%) | 0 |
| ALGOUSDT | 122 | 54474.17 | 92198.5 | 50499.91 | 0 (0.0%) | 2 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6466 | 29567.73 | 63738.72 | 26165.46 | 225 (3.48%) | 615 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 123 | 27641.35 | 87814.07 | 28216.7 | 0 (0.0%) | 6 |
| JASMYUSDT | 123 | 22802.98 | 227011.04 | 9003.42 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 68004 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1644 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3476 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
