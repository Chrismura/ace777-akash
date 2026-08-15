# BILAN — RUN TEST CHAMPION 9fe9f105 (12/08)

- Généré le : 2026-08-12 23:14:13 UTC
- Durée observée : 26 min

- master.pid: ARRETE
- alpha.pid: ARRETE
- beta.pid: ARRETE
- supervisor_v9_v2.pid: ARRETE

## Symbiose (la question critique)

| Métrique | Valeur | Attendu |
|---|---|---|
| BARRIER_TIMEOUT | 0 | 0 (champion sans barrière) |
| duo no_trigger (ALPHA muette) | 4 | 0 |
| duo no_state (clone) | 1 | 0 |
| revenge | 0 | faible |

## Performance

- Fills (entrées) : 16
- PnL cumulé (session) : -1.8794 USDT
- Trades gagnants : 5 | Perdants : 6
- Meilleur trade : +1.1685 | Pire : -1.8942

## Derniers cycles ALPHA

```[ALPHA_X13_BURST13] Successful order-cycles: 7```
```[ALPHA_X13_BURST13] Dernier cycle #87: pnl=0.00000000 bps=0.00000000 pct=0.00000000%```
```[ALPHA_X13_BURST13] 2026-08-12T23:12:27Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_0 rc=0```

## Derniers cycles BETA

```[BETA_X5] Successful order-cycles: 9```
```[BETA_X5] Dernier cycle #89: pnl=-0.00000000 bps=-0.00000000 pct=-0.00000000%```
```[BETA_X5] 2026-08-12T23:12:28Z PROCESS_EXIT unit=BETA_X5 how=pipe_run_unit why=rc_0 rc=0```

