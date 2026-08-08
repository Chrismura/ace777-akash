# Vortex SHADOW V2 — pilotage Radar

> chop_score: **v2** | Hystérésis: 0.65/0.45
> Klines: `BTCUSDT` 1m (15 min) + tension carnet glissante
> Généré: `2026-07-08T20:45:17Z`

## Profils (bornes clampées)

| Mode | BETA mom/conf/spread | ALPHA mom/conf/spread |
|------|----------------------|------------------------|
| BASELINE | 0.01/0.3/8.0 | 0.008/0.25/8.0 |
| TREND | 0.004/0.22/14.0 | 0.003/0.2/14.0 |
| CHOP | 0.015/0.4/5.0 | 0.012/0.35/5.0 |

_Proxy PnL récupéré = PnL du prochain FILLED dans 90s (oracle partiel)._

## chop_score_v2 (formule)

```
trend_chop  = 1 - min(|trend_bps_15m| / 25, 1)     # klines 1m
range_chop  = 1 si range_bps < 10, 0.5 si < 20   # marché en boîte
tension_chop = 1 - min(tension_ma_carnet / 1.0, 1)
vol_chop    = 0.8 si vol faible, 0.2 sinon
score = 0.30*trend + 0.25*range + 0.30*tension + 0.15*vol
CHOP si score > 0.65 | TREND si score < 0.45 (hystérésis)
```

## `MASTER_HYBRID_VF_20260708`

- Lignes: 3355 | FILLED réel: 86 | PnL réel: **-5.0705 USDT**
- `radar_block`: 2423 | Récupérés V2 (baseline block → v2 pass): **7**
- FILLED bloqués en V2 (protection CHOP): 0 | Pertes évitées: 0.0000 | Gains manqués: 0.0000
- Proxy PnL récupéré: -0.5902 USDT
- **Shadow PnL V2 estimé: -5.6607 USDT** | **Delta: -0.5902 USDT**
- Bascules régime: 48 | %TREND: 26.0% | %CHOP: 74.0% | chop_score moy: 0.628
- Mode final: CHOP

### Récupérations par sous-raison radar

- `spread_too_wide`: 7

## `MASTER_BASE_V8_5_IMPACT_4H`

- Lignes: 5906 | FILLED réel: 201 | PnL réel: **4.5053 USDT**
- `radar_block`: 1912 | Récupérés V2 (baseline block → v2 pass): **9**
- FILLED bloqués en V2 (protection CHOP): 0 | Pertes évitées: 0.0000 | Gains manqués: 0.0000
- Proxy PnL récupéré: -0.0096 USDT
- **Shadow PnL V2 estimé: 4.4957 USDT** | **Delta: -0.0096 USDT**
- Bascules régime: 44 | %TREND: 45.1% | %CHOP: 54.9% | chop_score moy: 0.596
- Mode final: CHOP

### Récupérations par sous-raison radar

- `spread_too_wide`: 8
- `low_confidence`: 1

## Synthèse

- Delta moyen V2 vs réel: **-0.2999 USDT**
- chop_score: **v2**
- **Verdict: marginal** — impact faible ; affiner chop_score ou profils avant live.

_Live genesis non modifié — simulation seulement. Prochaine étape si delta > 0 : `cycle_radar_*` dans genesis._
