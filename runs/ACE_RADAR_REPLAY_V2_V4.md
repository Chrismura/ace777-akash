# Beta radar alignment replay

> Local hypothetical: what if Beta had entered in the radar direction?

## Summary

- Aligned trades: 4
- Misaligned trades: 5
- Real gross: -8.9759
- Hypothetical gross (radar-aligned): -0.5101
- Real net: -14.0028
- Hypothetical net: -5.5370
- Delta: +8.4658

## Misaligned trades (would flip PnL)

| Source | Cycle | Side | Radar | Entry | Exit | Real PnL | Hyp PnL | Exit |
|---|---|---|---|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V2_15M` | 13 | SELL | long | 77816.6 | 77892.0 | -0.8810 | +0.0841 | stop_loss |
| `ACE_DUO_CLEAN_V2_15M` | 28 | SELL | long | 77788.8 | 77999.9 | -1.7493 | +0.9528 | stop_loss |
| `ACE_DUO_CLEAN_V2_15M` | 44 | SELL | long | 77850.5 | 77917.6 | -0.8280 | +0.0308 | stop_loss |
| `ACE_DUO_CLEAN_V3_15M` | 4 | SELL | long | 77828.7 | 77997.0 | -2.9512 | +1.3573 | stop_loss |
| `ACE_DUO_CLEAN_V3_15M` | 20 | SELL | long | 77996.9 | 77979.0 | -0.4583 | -0.8271 | trailing_stop |

## Verdict

- This is a local simulation, not proof of profitability.
- It assumes identical exit timing and fees in both scenarios.
- A positive delta does not mean the engine would have been profitable overall.
- ACE LIVE remains NO-GO.
