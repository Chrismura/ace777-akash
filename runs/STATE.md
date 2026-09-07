# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-07T22:30:18Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `MASTER_BASE_V8_6_FORTRESS_1H30` |
| run_id | `MASTER_BASE_V8_6_FORTRESS_1H30_20260907T210011Z_9797` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 18 | 2 | 16 | 11.1% | 2.1619 | 9.5209 | -7.3590 | 499 |
| ALPHA | 6 | 0 | 6 | 0.0% | -3.0685 | 6.4615 | -9.5300 | 831 |
| **TOTAL** | **24** | — | — | — | **-0.9066** | **15.9824** | **-16.8890** | **1330** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-7.359033050000001` USDT
- HUNTER PnL: `-9.52997152` USDT
- Total session: `-16.88900457` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `0.25270297` |
| pnl_usdt | `-0.38628727` |
| reason | `kill_switch` |
| cycle | `524` |
| hold_sec | `86` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 170
2. `reason=COMPRESSE tension=0.00001169 threshold=0.05` — 4
3. `reason=COMPRESSE tension=0.00001998 threshold=0.05` — 4
4. `reason=COMPRESSE tension=0.00001608 threshold=0.05` — 3
5. `reason=COMPRESSE tension=0.00002095 threshold=0.05` — 3

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 309
2. `reason=no_trigger mode=none` — 38
3. `reason=COMPRESSE tension=0.00001608 threshold=0.05` — 3
4. `reason=COMPRESSE tension=0.00001391 threshold=0.05` — 2
5. `reason=COMPRESSE tension=0.00002143 threshold=0.05` — 2

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `MASTER_BASE_V8_6_FORTRESS_1H30_BETA_X5.csv` (ok)
- ALPHA CSV: `MASTER_BASE_V8_6_FORTRESS_1H30_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
