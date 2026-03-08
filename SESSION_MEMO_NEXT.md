# Session Memo - Next Resume Point

Date: 2026-02-27

## Decision validated now

- Keep current profile unchanged for confirmation.
- Run 2 additional identical tests before any new tuning:
  - `run_sniper_v1_500_r095_bis.csv`
  - `run_sniper_v1_500_r095_ter.csv`

## Current active profile (kept as-is)

- `BUY_USDT=500`
- `MIN_PROFIT_BPS=45`
- `STOP_LOSS_BPS=20`
- `TRAIL_ARM_BPS=30`
- `TRAIL_GIVEBACK_BPS=10`
- `T_BASE=400`
- `K_ENTROPY=0.01`
- `MIN_HOLD=60s`
- `RADAR_MIN_CONF=0.95`
- `RADAR_GATE=TRUE`
- `Index mode ON`
- `Anomaly soft mode ON`

## Watchdog state

- Watchdog v2 integrated (skip streak + cycle cap).
- Crash watchdog integrated as optional (OFF by default):
  - `CRASH_WATCHDOG_ENABLED`
  - `CRASH_ALERT_BPS` (default 18)
  - `CRASH_CHECK_MS` (default 500)
  - action: cancel open orders then market exit.

## Items intentionally deferred (do not change during current tests)

- Further radar relaxation to `0.90` (only if confirmation runs are weak).
- Any change to SKIP hierarchy logic.
- Arbitrage execution layer (`arbitrage/README.md`) postponed until base coherence is confirmed.
- Advanced watchdog policy tuning after confirmation sample is complete.

## Post-test decision rule

- If both confirmation runs stay coherent and net positive/near-flat: keep profile.
- If unstable or net negative with low trade count: lower radar confidence to `0.90` and retest.
