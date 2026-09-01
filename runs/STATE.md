# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-01T16:17:19Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `ACE_DUO_CLEAN_V4_15M` |
| run_id | `ACE_DUO_CLEAN_V4_15M_20260901T160208Z_34195` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 2 | 0 | 2 | 0.0% | -4.6029 | 1.1962 | -5.7991 | 104 |
| ALPHA | 1 | 0 | 1 | 0.0% | 0.6228 | 1.0772 | -0.4544 | 124 |
| **TOTAL** | **3** | — | — | — | **-3.9801** | **2.2734** | **-6.2535** | **228** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-5.79907226` USDT
- HUNTER PnL: `-0.45438242` USDT
- Total session: `-6.25345468` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `-20.51942356` |
| pnl_usdt | `-1.42323149` |
| reason | `stop_loss` |
| cycle | `29` |
| hold_sec | `84` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 34
2. `reason=spread_too_wide conf=0.5 mom_sig=1.06849918 raw_mom_bps=0.00000000 spread_bps=41.50140000 tension=1.06849918 bid_drop=6.94524466 ask_drop=0.26761617 swarm=0` — 1
3. `mom=long structure=short` — 1
4. `reason=spread_too_wide conf=0.5 mom_sig=2.84403454 raw_mom_bps=0.00000000 spread_bps=10.40030000 tension=2.84403454 bid_drop=18.48622452 ask_drop=0.16780662 swarm=0` — 1
5. `reason=spread_too_wide conf=0.5 mom_sig=2.13510629 raw_mom_bps=0.00000000 spread_bps=40.96460000 tension=2.13510629 bid_drop=13.87819090 ask_drop=0.00000000 swarm=0` — 1

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 40
2. `reason=no_state mode=none` — 2
3. `reason=COMPRESSE tension=0.00092633 threshold=0.05` — 1
4. `reason=COMPRESSE tension=0.00000083 threshold=0.05` — 1
5. `reason=COMPRESSE tension=0.01041051 threshold=0.05` — 1

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv` (ok)
- ALPHA CSV: `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
