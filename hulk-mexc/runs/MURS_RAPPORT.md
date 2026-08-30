# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-08-30T18:01Z — 68277 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20260830_180017.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 132 | 480970.57 | 876977.29 | 449506.53 | 0 (0.0%) | 3 |
| BTCUSDT | 1175 | 454843.46 | 1924444.32 | 474726.65 | 30 (2.55%) | 76 |
| ETHUSDT | 925 | 184004.23 | 1966688.05 | 177431.06 | 8 (0.86%) | 32 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 7828 | 91536.82 | 606419.6 | 95464.36 | 332 (4.24%) | 1028 |
| XLMUSDT | 124 | 71929.53 | 210677.64 | 67222.86 | 0 (0.0%) | 0 |
| ALGOUSDT | 124 | 54447.85 | 92198.5 | 50510.23 | 0 (0.0%) | 3 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 6517 | 29617.0 | 63738.72 | 26205.84 | 226 (3.47%) | 616 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| GOLD(PAXG)USDT | 125 | 27636.97 | 87814.07 | 28204.1 | 0 (0.0%) | 6 |
| JASMYUSDT | 125 | 22799.43 | 227011.04 | 8984.83 | 0 (0.0%) | 0 |

## Synthèse
- **Total mesures** : 68277 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1654 (2.4% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 3492 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
