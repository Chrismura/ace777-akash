# ACE consolidated run facts

> Local read-only consolidation. Gross/net values come from trade CSVs; no Binance reconciliation is implied.

| Run | Unit | Obs rows | SKIP | ALLOW | Fills | Gross | Fees | Net | Exit reasons |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V2_15M` | ALPHA | 88 | 85 | 3 | 3 | +3.0424 | +2.9203 | +0.1220 | stop_loss=1, trailing_stop=2 |
| `ACE_DUO_CLEAN_V2_15M` | BETA | 53 | 49 | 4 | 4 | -2.3104 | +1.9919 | -4.3023 | stop_loss=3, timeout=1 |
| `ACE_DUO_CLEAN_V3_15M` | ALPHA | 98 | 95 | 3 | 3 | -1.8046 | +2.9243 | -4.7289 | kill_switch=1, stop_loss=1, trailing_stop=1 |
| `ACE_DUO_CLEAN_V3_15M` | BETA | 113 | 110 | 3 | 3 | -2.0627 | +1.8388 | -3.9014 | kill_switch=1, stop_loss=1, trailing_stop=1 |
| `ACE_DUO_CLEAN_V4_15M` | ALPHA | 125 | 124 | 1 | 1 | +0.6228 | +1.0772 | -0.4544 | trailing_stop=1 |
| `ACE_DUO_CLEAN_V4_15M` | BETA | 106 | 104 | 2 | 2 | -4.6029 | +1.1962 | -5.7991 | stop_loss=2 |

## Strict verdict

- The recent runs are technically complete and locally accounted for.
- Observation coverage is sufficient to describe decisions, not to estimate missed-trade outcomes.
- Net performance remains a local engine result until exchange commissions are reconciled by run_id.
- Do not alter gates or enable LIVE based on this report alone.
