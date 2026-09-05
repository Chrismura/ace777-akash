# ACE gate analysis

> Read-only analysis of converted CSV observations. No execution or exchange reconciliation.

## Global result

- Rows: **583**
- SKIP: **567** (97.3%)
- ALLOW/FILLED projection: **16** (2.7%)

## By unit/file

| File | Unit | Rows | SKIP | ALLOW | Mid available | Spread available | Momentum available | Confidence available |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `ACE_DUO_CLEAN_V2_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 88 | 85 | 3 | 3 | 0 | 0 | 3 |
| `ACE_DUO_CLEAN_V2_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 53 | 49 | 4 | 4 | 0 | 0 | 4 |
| `ACE_DUO_CLEAN_V3_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 98 | 95 | 3 | 3 | 0 | 0 | 3 |
| `ACE_DUO_CLEAN_V3_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 113 | 110 | 3 | 3 | 0 | 0 | 3 |
| `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 125 | 124 | 1 | 1 | 0 | 0 | 1 |
| `ACE_DUO_CLEAN_V4_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 106 | 104 | 2 | 2 | 0 | 0 | 2 |

## Most frequent recorded reasons

- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 211
- `csv_engine:stop_loss` — 8
- `csv_engine:trailing_stop` — 5
- `csv_engine:reason=no_state mode=none` — 3
- `csv_engine:mom=long structure=short` — 3
- `csv_engine:reason=COMPRESSE tension=0.00012358 threshold=0.05` — 2
- `csv_engine:reason=COMPRESSE tension=0.01396277 threshold=0.05` — 2
- `csv_engine:reason=spread_too_wide conf=0.5 mom_sig=1.24869621 raw_mom_bps=0.00000000 spread_bps=9.57730000 tension=1.24869621 bid_drop=8.11652539 ask_drop=0.11390496 swarm=0` — 2
- `csv_engine:reason=COMPRESSE tension=0.00009458 threshold=0.05` — 2
- `csv_engine:reason=spread_too_wide conf=0.129 mom_sig=0.15478843 raw_mom_bps=0.00000000 spread_bps=11.03890000 tension=0.15478843 bid_drop=1.00612482 ask_drop=0.00000000 swarm=0` — 2

## Strict interpretation

- A high SKIP rate is an observation, not proof that a gate is wrong.
- This projection lacks complete bid/ask history and cannot estimate missed-trade PnL.
- No threshold change is recommended from this report alone.
- ACE LIVE remains NO-GO.
