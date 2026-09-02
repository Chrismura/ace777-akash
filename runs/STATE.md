# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-02T01:04:31Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `ACE_RADAR_ALIGNED_V4_60M` |
| run_id | `ACE_RADAR_ALIGNED_V4_60M_20260902T000420Z_41201` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 9 | 2 | 7 | 22.2% | -5.8093 | 4.7056 | -10.5149 | 339 |
| ALPHA | 5 | 0 | 5 | 0.0% | -3.3131 | 4.9776 | -8.2907 | 366 |
| **TOTAL** | **14** | — | — | — | **-9.1224** | **9.6832** | **-18.8056** | **705** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-10.514915449999998` USDT
- HUNTER PnL: `-8.290707959999999` USDT
- Total session: `-18.805623409999995` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `-13.73163717` |
| pnl_usdt | `-1.07363328` |
| reason | `stop_loss` |
| cycle | `345` |
| hold_sec | `36` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 152
2. `reason=COMPRESSE tension=0.00000613 threshold=0.05` — 2
3. `reason=COMPRESSE tension=0.01680238 threshold=0.05` — 1
4. `reason=COMPRESSE tension=0.00101623 threshold=0.05` — 1
5. `reason=COMPRESSE tension=0.00001931 threshold=0.05` — 1

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 176
2. `reason=no_trigger mode=none` — 5
3. `reason=no_state mode=none` — 4
4. `reason=COMPRESSE tension=0.00057525 threshold=0.05` — 1
5. `reason=COMPRESSE tension=0.00000855 threshold=0.05` — 1

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `ACE_RADAR_ALIGNED_V4_60M_BETA_X5.csv` (ok)
- ALPHA CSV: `ACE_RADAR_ALIGNED_V4_60M_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
