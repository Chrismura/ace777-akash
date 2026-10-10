# OBSERVATOIRE DES MURS DE LIQUIDITÉ
> 2026-10-10T14:41Z — 87774 mesures sur 27 paires · CSVs ASPIRATION_CALIB + OBSERVATION_MURS · sonde observation OBSERVATION_MURS_20261010_144057.csv

## Les VRAIS murs (top 12 par mur bid moyen)

| Paire | Mesures | Mur BID moy ($) | Mur BID max ($) | Mur ASK moy ($) | Spoof | Drop ≥15%/s |
|---|---|---|---|---|---|---|
| SOLUSDT | 1793 | 475600.3 | 2078362.86 | 460578.99 | 0 (0.0%) | 67 |
| BTCUSDT | 1481 | 419926.18 | 1924444.32 | 488181.06 | 49 (3.31%) | 124 |
| ETHUSDT | 1264 | 177592.18 | 1966688.05 | 173455.49 | 14 (1.11%) | 63 |
| ADAUSDT | 36 | 102875.08 | 154143.34 | 92656.51 | 0 (0.0%) | 1 |
| XRPUSDT | 8737 | 91589.68 | 606419.6 | 94098.68 | 376 (4.3%) | 1137 |
| XLMUSDT | 1785 | 84666.18 | 312328.07 | 72474.95 | 0 (0.0%) | 68 |
| ALGOUSDT | 1786 | 49385.91 | 180103.2 | 46241.46 | 0 (0.0%) | 53 |
| CHIPUSDT | 828 | 30766.68 | 61779.48 | 27298.12 | 32 (3.86%) | 53 |
| HBARUSDT | 7426 | 30739.91 | 63738.72 | 26144.54 | 268 (3.61%) | 682 |
| GOLD(PAXG)USDT | 1787 | 29841.51 | 191387.78 | 29208.52 | 0 (0.0%) | 140 |
| KITEUSDT | 391 | 28494.55 | 49707.9 | 26254.61 | 10 (2.56%) | 17 |
| JASMYUSDT | 1785 | 16504.08 | 239378.61 | 11722.78 | 0 (0.0%) | 12 |

## Synthèse
- **Total mesures** : 87774 (16-24/08, sonde aspiration)
- **Spoofs détectés** : 1845 (2.1% des mesures) — murs de façade (fond puis se reconstruit)
- **Chutes brutales de mur** (≥ 15%/s) : 4474 — le signal ACE « le mur s'effondre »

## Lecture
- Un mur BID épais = support réel (des acheteurs tiennent le prix)
- Un mur ASK épais = résistance réelle (des vendeurs bloquent la hausse)
- Spoof élevé sur une paire = murs de façade fréquents → méfiance (manipulation)
- Drop ≥ 15%/s = le mur s'effondre → l'aspiration se déclenche (ACE)
