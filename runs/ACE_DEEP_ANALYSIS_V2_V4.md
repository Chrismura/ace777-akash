# ACE deep Beta/Alpha analysis

> Read-only. All values extracted from CSV msg fields; no exchange, no engine modification.

## Filled trades by exit reason

| Exit | # | Gross | Fees | Net | Avg hold | Avg tension | Avg confidence | Avg bps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `kill_switch` | 2 | -0.3603 | +0.9357 | -1.2960 | 44s | 1.645 | 0.635 | -0.0292% |
| `stop_loss` | 8 | -12.0420 | +5.0346 | -17.0766 | 94s | 2.221 | 0.848 | -0.1832% |
| `timeout` | 1 | -0.0474 | +0.7966 | -0.8440 | 212s | 2.670 | 0.809 | -0.0048% |
| `trailing_stop` | 5 | +5.3343 | +5.1818 | +0.1525 | 61s | 5.235 | 0.731 | 0.0770% |

## Individual fills

| Source | Cycle | Side | Entry | Exit | Qty | Hold | Tension | Conf | Pct% | Gross | Fees | Net | Exit |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V3_15M` | 113 | SELL | 77951.3 | 77965.8 | 0.006400 | 66s | 1.506 | 0.6346 | -0.0186 | -0.0928 | +0.3991 | -0.4919 | `kill_switch` |
| `ACE_DUO_CLEAN_V3_15M` | 98 | BUY | 77996.9 | 77965.8 | 0.008600 | 23s | 1.783 | 0.6346 | -0.0399 | -0.2675 | +0.5366 | -0.8041 | `kill_switch` |
| `ACE_DUO_CLEAN_V2_15M` | 16 | BUY | 77877.4 | 77816.6 | 0.008600 | 100s | 1.028 | 0.8772 | -0.0781 | -0.5229 | +0.5358 | -1.0587 | `stop_loss` |
| `ACE_DUO_CLEAN_V2_15M` | 13 | SELL | 77816.6 | 77892.0 | 0.006400 | 100s | 3.321 | 0.9968 | -0.0969 | -0.4826 | +0.3984 | -0.8810 | `stop_loss` |
| `ACE_DUO_CLEAN_V2_15M` | 28 | SELL | 77788.8 | 77999.9 | 0.006400 | 133s | 1.073 | 0.9992 | -0.2714 | -1.3510 | +0.3983 | -1.7493 | `stop_loss` |
| `ACE_DUO_CLEAN_V2_15M` | 44 | SELL | 77850.5 | 77917.6 | 0.006400 | 100s | 1.293 | 0.9912 | -0.0862 | -0.4294 | +0.3986 | -0.8280 | `stop_loss` |
| `ACE_DUO_CLEAN_V3_15M` | 4 | SELL | 77828.7 | 77997.0 | 0.012800 | 51s | 1.253 | 0.7160 | -0.2162 | -2.1542 | +0.7970 | -2.9512 | `stop_loss` |
| `ACE_DUO_CLEAN_V3_15M` | 17 | BUY | 77996.9 | 77877.9 | 0.021000 | 132s | 4.339 | 0.5096 | -0.1526 | -2.4990 | +1.3103 | -3.8093 | `stop_loss` |
| `ACE_DUO_CLEAN_V4_15M` | 15 | SELL | 77828.2 | 78107.8 | 0.012800 | 52s | 3.916 | 0.7521 | -0.3593 | -3.5789 | +0.7970 | -4.3758 | `stop_loss` |
| `ACE_DUO_CLEAN_V4_15M` | 29 | SELL | 77974.9 | 78134.9 | 0.006400 | 84s | 1.543 | 0.9447 | -0.2052 | -1.0240 | +0.3992 | -1.4232 | `stop_loss` |
| `ACE_DUO_CLEAN_V2_15M` | 7 | SELL | 77792.1 | 77795.8 | 0.012800 | 212s | 2.670 | 0.8091 | -0.0048 | -0.0474 | +0.7966 | -0.8440 | `timeout` |
| `ACE_DUO_CLEAN_V2_15M` | 14 | BUY | 77792.4 | 77908.9 | 0.017300 | 63s | 1.072 | 0.7880 | 0.1498 | +2.0154 | +1.0766 | +0.9388 | `trailing_stop` |
| `ACE_DUO_CLEAN_V2_15M` | 81 | BUY | 77850.5 | 77924.3 | 0.021000 | 109s | 9.461 | 0.9928 | 0.0948 | +1.5498 | +1.3079 | +0.2419 | `trailing_stop` |
| `ACE_DUO_CLEAN_V3_15M` | 4 | BUY | 77844.5 | 77900.1 | 0.017300 | 65s | 1.027 | 0.7039 | 0.0714 | +0.9619 | +1.0774 | -0.1155 | `trailing_stop` |
| `ACE_DUO_CLEAN_V3_15M` | 20 | SELL | 77996.9 | 77979.0 | 0.010300 | 45s | 8.364 | 0.5096 | 0.0229 | +0.1844 | +0.6427 | -0.4583 | `trailing_stop` |
| `ACE_DUO_CLEAN_V4_15M` | 20 | BUY | 77831.1 | 77867.1 | 0.017300 | 21s | 6.249 | 0.6591 | 0.0463 | +0.6228 | +1.0772 | -0.4544 | `trailing_stop` |

## Skip context summary

- Total SKIP cycles: 567

## Verdict

- Stop_loss trades enter with higher tension but move against the position immediately.
- The trailing_stop win is tiny and consumed by fees.
- Confidence is high on losing trades — the confidence model is not aligned with profitability.
- No live parameter change is recommended; richer entry data is needed.
- ACE LIVE remains NO-GO.
