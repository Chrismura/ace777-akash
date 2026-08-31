# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-31T10:11Z — 73005 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260831_101104.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 164 | 478908.31 | 876977.29 | 452721.98 | 0 (0.0%) | 5 |
| BTCUSDT | 1479 | 419866.72 | 1924444.32 | 488196.4 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8716 | 91587.74 | 606419.6 | 94184.26 | 376 (4.31%) | 1135 |
| XLMUSDT | 156 | 71993.61 | 210677.64 | 67813.81 | 0 (0.0%) | 0 |
| ALGOUSDT | 156 | 53509.92 | 92198.5 | 50207.63 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7405 | 30732.08 | 63738.72 | 26143.11 | 266 (3.59%) | 676 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 157 | 27341.64 | 87814.07 | 27921.27 | 0 (0.0%) | 9 |
| JASMYUSDT | 157 | 24331.41 | 227011.04 | 8922.42 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 73005 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1840 (2.5% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3819 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
