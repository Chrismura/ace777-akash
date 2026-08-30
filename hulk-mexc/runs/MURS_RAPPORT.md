# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T22:03Z — 69324 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_220318.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 140 | 480978.8 | 876977.29 | 446433.97 | 0 (0.0%) | 3 |
| BTCUSDT | 1370 | 431107.78 | 1924444.32 | 486233.93 | 43 (3.14%) | 104 |
| ETHUSDT | 937 | 183980.91 | 1966688.05 | 177006.32 | 9 (0.96%) | 34 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8023 | 91386.45 | 606419.6 | 95086.04 | 345 (4.3%) | 1047 |
| XLMUSDT | 132 | 72436.31 | 210677.64 | 67466.47 | 0 (0.0%) | 0 |
| ALGOUSDT | 132 | 53716.62 | 92198.5 | 49785.05 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6712 | 29841.93 | 63738.72 | 26212.25 | 236 (3.52%) | 628 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 133 | 27253.31 | 87814.07 | 28113.02 | 0 (0.0%) | 7 |
| JASMYUSDT | 133 | 22384.57 | 227011.04 | 8932.12 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 69324 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1717 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3569 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
