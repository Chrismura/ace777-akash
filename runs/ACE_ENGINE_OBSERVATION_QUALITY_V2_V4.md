# ACE engine observation quality

> Read-only analysis of parsed historical logs. Missing values are not inferred.

| File | Rows | SKIP | ALLOW | Tension values | Tension avg | Spread field | Momentum field | Confidence field | Units | run_id |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `ACE_DUO_CLEAN_V2_15M_ENGINE_OBSERVATIONS.csv` | 268 | 268 | 0 | 134 | 0.680 | 0 | 0 | 82 | ALPHA,BETA | ACE_DUO_CLEAN_V2_15M |
| `ACE_DUO_CLEAN_V3_15M_ENGINE_OBSERVATIONS.csv` | 410 | 410 | 0 | 205 | 0.713 | 0 | 0 | 132 | ALPHA,BETA | ACE_DUO_CLEAN_V3_15M |
| `ACE_DUO_CLEAN_V4_15M_ENGINE_OBSERVATIONS.csv` | 456 | 456 | 0 | 228 | 0.851 | 0 | 0 | 166 | ALPHA,BETA | ACE_DUO_CLEAN_V4_15M |

## Verdict

- The current log parser captures decisions and units reliably.
- Historical logs do not provide complete spread/momentum fields per cycle.
- No gate threshold should be changed based on incomplete telemetry.
- The next engine instrumentation should emit one structured observation before every decision.
- ACE LIVE remains NO-GO.
