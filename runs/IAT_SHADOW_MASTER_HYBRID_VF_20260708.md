# IAT SHADOW (Malanga) — simulation replay

> Tag: `MASTER_HYBRID_VF_20260708` | Formule: Cortana `quantum::malanga` | Shadow: **SKIP si IAT ≥ 80**
> Généré: `2026-07-08T16:47:27Z`

## Formule rappel

```
Énergie  = funding saturé (|f|>0.05%) + OI > +20% vs moy 24h
Temps    = cycle Fourier majeur (>24h) proche extremum
Espace   = mur carnet (proxy bid_drop/ask_drop du CSV)
IAT      = (E + T + S) / 3  →  alerte si > 80
```

## Résultat

| | Réel | Avec IAT shadow |
|---|------|-----------------|
| Trades | 5 | 5 (+ 0 filtrés) |
| PnL | **3.1337 USDT** | **3.1337 USDT** |
| Delta | — | **+0.0000 USDT** |

- Pertes évitées: **0.0000 USDT**
- Gains manqués: **0.0000 USDT**

## Détail par trade

| TS | Unité | Side | PnL | IAT | E | T | S | Funding% | OI× | Verdict |
|----|-------|------|-----|-----|---|---|---|----------|-----|---------|
| 2026-07-08T16:27:35Z | ALPHA | BUY | 3.7800 | 48.6 | 0 | 59 | 87 | +0.0072 | 1.02 | ALLOW |
| 2026-07-08T16:28:28Z | BETA | SELL | -0.0722 | 42.8 | 0 | 59 | 69 | +0.0072 | 1.02 | ALLOW |
| 2026-07-08T16:31:34Z | ALPHA | BUY | -0.5542 | 48.6 | 0 | 59 | 87 | +0.0072 | 1.02 | ALLOW |
| 2026-07-08T16:33:55Z | BETA | SELL | -0.0000 | 48.6 | 0 | 59 | 87 | +0.0072 | 1.02 | ALLOW |
| 2026-07-08T16:41:50Z | BETA | SELL | -0.0200 | 48.6 | 0 | 59 | 87 | +0.0072 | 1.02 | ALLOW |

**Verdict : neutre** — impact marginal sur ce cycle (+0.00 USDT).

_Données live Binance (funding, OI, klines 1h) + proxy spatial depuis CSV (bid_drop/ask_drop)._
