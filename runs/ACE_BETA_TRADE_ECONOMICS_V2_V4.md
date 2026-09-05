# ACE Beta trade economics

> Read-only analysis of local Beta CSV fills; no strategy or engine change was applied.

| Exit reason | Trades | Gross | Fees | Net |
|---|---:|---:|---:|---:|
| `kill_switch` | 1 | -0.0928 | +0.3991 | -0.4919 |
| `stop_loss` | 6 | -9.0202 | +3.1885 | -12.2086 |
| `timeout` | 1 | -0.0474 | +0.7966 | -0.8440 |
| `trailing_stop` | 1 | +0.1844 | +0.6427 | -0.4583 |

## Individual fills

| Source | Cycle | Entry | Exit | Qty | Gross | Fees | Net | Exit |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V2_15M_BETA_X5.csv` | 7 | 77792.10000000 | 77795.80000000 | 0.01280000 | -0.0474 | +0.7966 | -0.8440 | timeout |
| `ACE_DUO_CLEAN_V2_15M_BETA_X5.csv` | 13 | 77816.60000000 | 77892.00000000 | 0.00640000 | -0.4826 | +0.3984 | -0.8810 | stop_loss |
| `ACE_DUO_CLEAN_V2_15M_BETA_X5.csv` | 28 | 77788.80000000 | 77999.90000000 | 0.00640000 | -1.3510 | +0.3983 | -1.7493 | stop_loss |
| `ACE_DUO_CLEAN_V2_15M_BETA_X5.csv` | 44 | 77850.50000000 | 77917.60000000 | 0.00640000 | -0.4294 | +0.3986 | -0.8280 | stop_loss |
| `ACE_DUO_CLEAN_V3_15M_BETA_X5.csv` | 4 | 77828.70000000 | 77997.00000000 | 0.01280000 | -2.1542 | +0.7970 | -2.9512 | stop_loss |
| `ACE_DUO_CLEAN_V3_15M_BETA_X5.csv` | 20 | 77996.90000000 | 77979.00000000 | 0.01030000 | +0.1844 | +0.6427 | -0.4583 | trailing_stop |
| `ACE_DUO_CLEAN_V3_15M_BETA_X5.csv` | 113 | 77951.30000000 | 77965.80000000 | 0.00640000 | -0.0928 | +0.3991 | -0.4919 | kill_switch |
| `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv` | 15 | 77828.20000000 | 78107.80000000 | 0.01280000 | -3.5789 | +0.7970 | -4.3758 | stop_loss |
| `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv` | 29 | 77974.90000000 | 78134.90000000 | 0.00640000 | -1.0240 | +0.3992 | -1.4232 | stop_loss |

## Strict verdict

- Beta must not be changed based on a small sample alone.
- A stop-loss loss and its fee are separate effects and must remain separate in diagnosis.
- The next safe improvement is richer entry telemetry and replay, not a live parameter change.
- ACE LIVE remains NO-GO.
