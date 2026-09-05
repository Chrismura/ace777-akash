# ACE tension by unit

> Read-only analysis of tension embedded in engine logs.

| Run | Unit | N | Min | P50 | P90 | Max | Decisions |
|---|---|---:|---:|---:|---:|---:|---|
| `ACE_DUO_CLEAN_V2_15M` | ALPHA | 85 | 0.000 | 0.006 | 3.101 | 6.819 | SKIP=85 |
| `ACE_DUO_CLEAN_V2_15M` | BETA | 49 | 0.000 | 0.001 | 2.148 | 4.812 | SKIP=49 |
| `ACE_DUO_CLEAN_V3_15M` | ALPHA | 95 | 0.000 | 0.014 | 1.506 | 9.458 | SKIP=95 |
| `ACE_DUO_CLEAN_V3_15M` | BETA | 110 | 0.000 | 0.000 | 1.981 | 11.549 | SKIP=110 |
| `ACE_DUO_CLEAN_V4_15M` | ALPHA | 124 | 0.000 | 0.010 | 2.651 | 8.300 | SKIP=124 |
| `ACE_DUO_CLEAN_V4_15M` | BETA | 104 | 0.000 | 0.018 | 2.492 | 8.095 | SKIP=104 |

## Verdict

- Tension is now measurable from the historical logs.
- The available logs contain SKIP decisions only; they do not prove what would have happened after allowing a blocked cycle.
- No gate threshold change is justified without complete structured observations and replay data.
- ACE LIVE remains NO-GO.
