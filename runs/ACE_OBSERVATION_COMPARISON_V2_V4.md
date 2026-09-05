# ACE observation comparison

> Local projection of existing CSVs; no market data or Binance reconciliation is implied.
> Generated: 2026-09-01T17:27:13Z

## Runs

| File | Unit | Rows | SKIP | ALLOW | ALLOW with entry price | run_id |
|---|---:|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V2_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 88 | 85 | 3 | 3 | ACE_DUO_CLEAN_V2_15M |
| `ACE_DUO_CLEAN_V2_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 53 | 49 | 4 | 4 | ACE_DUO_CLEAN_V2_15M |
| `ACE_DUO_CLEAN_V3_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 98 | 95 | 3 | 3 | ACE_DUO_CLEAN_V3_15M |
| `ACE_DUO_CLEAN_V3_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 113 | 110 | 3 | 3 | ACE_DUO_CLEAN_V3_15M |
| `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv` | ALPHA | 125 | 124 | 1 | 1 | ACE_DUO_CLEAN_V4_15M |
| `ACE_DUO_CLEAN_V4_15M_BETA_X5_OBSERVATIONS.csv` | BETA | 106 | 104 | 2 | 2 | ACE_DUO_CLEAN_V4_15M |

## Top decision reasons

### `ACE_DUO_CLEAN_V2_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 31
- `csv_engine:trailing_stop` — 2
- `csv_engine:reason=spread_too_wide conf=0.4288 mom_sig=0.51457537 raw_mom_bps=0.00000000 spread_bps=25.08090000 tension=0.51457537 bid_drop=3.34473989 ask_drop=2.35364478 swarm=0` — 1
- `csv_engine:reason=no_state mode=none` — 1
- `csv_engine:mom=long structure=short` — 1

### `ACE_DUO_CLEAN_V2_15M_BETA_X5_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 20
- `csv_engine:stop_loss` — 3
- `csv_engine:reason=COMPRESSE tension=0.00028178 threshold=0.05` — 1
- `csv_engine:reason=COMPRESSE tension=0.00004812 threshold=0.05` — 1
- `csv_engine:reason=COMPRESSE tension=0.00001200 threshold=0.05` — 1

### `ACE_DUO_CLEAN_V3_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 37
- `csv_engine:reason=no_trigger mode=none` — 2
- `csv_engine:reason=COMPRESSE tension=0.00371356 threshold=0.05` — 1
- `csv_engine:mom=short structure=long` — 1
- `csv_engine:trailing_stop` — 1

### `ACE_DUO_CLEAN_V3_15M_BETA_X5_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 49
- `csv_engine:reason=COMPRESSE tension=0.00011659 threshold=0.05` — 1
- `csv_engine:reason=spread_too_wide conf=0.5 mom_sig=5.36318936 raw_mom_bps=12.15977377 spread_bps=8.13950000 tension=5.36318936 bid_drop=34.86073082 ask_drop=0.00060905 swarm=0` — 1
- `csv_engine:reason=COMPRESSE tension=0.00089004 threshold=0.05` — 1
- `csv_engine:stop_loss` — 1

### `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 40
- `csv_engine:reason=no_state mode=none` — 2
- `csv_engine:reason=spread_too_wide conf=0.5 mom_sig=0.70308789 raw_mom_bps=0.00000000 spread_bps=13.99810000 tension=0.70308789 bid_drop=4.57007126 ask_drop=0.00000000 swarm=0` — 1
- `csv_engine:reason=COMPRESSE tension=0.00092633 threshold=0.05` — 1
- `csv_engine:reason=COMPRESSE tension=0.00000083 threshold=0.05` — 1

### `ACE_DUO_CLEAN_V4_15M_BETA_X5_OBSERVATIONS.csv`
- `csv_engine:reason=COMPRESSE tension=0.00000000 threshold=0.05` — 34
- `csv_engine:stop_loss` — 2
- `csv_engine:reason=spread_too_wide conf=0.5 mom_sig=1.06849918 raw_mom_bps=0.00000000 spread_bps=41.50140000 tension=1.06849918 bid_drop=6.94524466 ask_drop=0.26761617 swarm=0` — 1
- `csv_engine:mom=long structure=short` — 1
- `csv_engine:reason=spread_too_wide conf=0.5 mom_sig=2.84403454 raw_mom_bps=0.00000000 spread_bps=10.40030000 tension=2.84403454 bid_drop=18.48622452 ask_drop=0.16780662 swarm=0` — 1

## Interpretation limits

- This report describes recorded engine decisions only.
- Missing bid/ask/order-book values remain missing.
- It does not establish profitability, slippage, or Binance fee reconciliation.
- It must not be used as permission to launch ACE or LIVE trading.
