# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-01T23:25:55Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `ACE_RADAR_ALIGNED_V3_15M` |
| run_id | `ACE_RADAR_ALIGNED_V3_15M_20260901T231047Z_50145` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 4 | 0 | 4 | 0.0% | 0.7205 | 2.7901 | -2.0696 | 25 |
| ALPHA | 2 | 0 | 2 | 0.0% | -1.0718 | 2.1529 | -3.2247 | 57 |
| **TOTAL** | **6** | — | — | — | **-0.3514** | **4.9430** | **-5.2944** | **82** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-2.0696356` USDT
- HUNTER PnL: `-3.22473643` USDT
- Total session: `-5.29437203` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `-0.01293149` |
| pnl_usdt | `-0.39657267` |
| reason | `timeout` |
| cycle | `15` |
| hold_sec | `164` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 11
2. `reason=low_confidence conf=0.2981 mom_sig=0.27549376 raw_mom_bps=-5.61226007 spread_bps=5.61230000 tension=0.27549376 bid_drop=1.79070945 ask_drop=0.00983674 swarm=0` — 1
3. `reason=COMPRESSE tension=0.00004733 threshold=0.05` — 1
4. `reason=COMPRESSE tension=0.00106266 threshold=0.05` — 1
5. `reason=wall_not_collapsed tension=0.25077269 bid_drop=1.63002248 ask_drop=0.00000000` — 1

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 27
2. `reason=no_trigger mode=none` — 3
3. `reason=COMPRESSE tension=0.00151293 threshold=0.05` — 2
4. `reason=COMPRESSE tension=0.02339481 threshold=0.05` — 1
5. `reason=direction_unclear conf=0.1533 mom_sig=0.14664896 raw_mom_bps=0.00000000 spread_bps=5.96140000 tension=0.14664896 bid_drop=0.95321823 ask_drop=0.00000000 swarm=0` — 1

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `ACE_RADAR_ALIGNED_V3_15M_BETA_X5.csv` (ok)
- ALPHA CSV: `ACE_RADAR_ALIGNED_V3_15M_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
