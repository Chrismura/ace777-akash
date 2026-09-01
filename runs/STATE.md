# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `unknown` | Statut: `IDLE` | MAJ: `2026-09-01T20:20:38Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `non_charge` v`?` |
| Masse BETA / ALPHA | `?` / `?` USDT |
| LLM gate | enabled=`?` fail_closed=`?` |
| Modèle LLM | `?` |
| Tag session | `ACE_DUO_CLEAN_V1_15M` |
| run_id | `ACE_DUO_CLEAN_V1_15M_20260901T141030Z_60190` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 2 | 0 | 2 | 0.0% | -2.9614 | 1.1910 | -4.1524 | 104 |
| ALPHA | 0 | 0 | 0 | 0.00% | 0.0000 | 0.0000 | 0.0000 | 121 |
| **TOTAL** | **2** | — | — | — | **-2.9614** | **1.1910** | **-4.1524** | **225** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-3.2266249` USDT
- HUNTER PnL: `-1.3594556800000002` USDT
- Total session: `-4.58608058` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `-0.0` |
| pnl_usdt | `-0.3956864` |
| reason | `kill_switch` |
| cycle | `47` |
| hold_sec | `11` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 33
2. `mom=long structure=short` — 2
3. `reason=COMPRESSE tension=0.00000669 threshold=0.05` — 2
4. `reason=COMPRESSE tension=0.01396506 threshold=0.05` — 1
5. `reason=low_confidence conf=0.2574 mom_sig=0.21095842 raw_mom_bps=19.45105096 spread_bps=4.28570000 tension=0.21095842 bid_drop=1.37122974 ask_drop=0.12078468 swarm=0` — 1

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 39
2. `reason=no_trigger mode=none` — 4
3. `reason=spread_too_wide conf=0.5 mom_sig=3.08238450 raw_mom_bps=0.00000000 spread_bps=35.50470000 tension=3.08238450 bid_drop=20.03549927 ask_drop=0.00000000 swarm=0` — 1
4. `reason=COMPRESSE tension=0.00128574 threshold=0.05` — 1
5. `reason=low_confidence conf=0.2082 mom_sig=0.24238380 raw_mom_bps=0.00000000 spread_bps=7.75510000 tension=0.24238380 bid_drop=1.57549471 ask_drop=0.00000000 swarm=0` — 1

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `ACE_DUO_CLEAN_V1_15M_BETA_X5.csv` (ok)
- ALPHA CSV: `ACE_DUO_CLEAN_V1_15M_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
