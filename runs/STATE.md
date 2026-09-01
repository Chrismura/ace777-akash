# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-01T13:22:31Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `ACE_DUO_PREFLIGHT_10M` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Net USDT | SKIP |
|-------|--------|-----|------|------|----------|------|
| BETA | 2 | 1 | 1 | 50.0% | 0.0691 | 51 |
| ALPHA | 1 | 0 | 1 | 0.0% | -0.1868 | 59 |
| **TOTAL** | **3** | — | — | — | **-0.1177** | **110** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-1.12573747` USDT
- HUNTER PnL: `-1.26350619` USDT
- Total session: `-2.38924366` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `-1.3884782` |
| pnl_usdt | `-0.46736896` |
| reason | `kill_switch` |
| cycle | `53` |
| hold_sec | `90` |

## Top SKIP — BETA

1. `regime_gate` — 40
2. `radar_block` — 11

## Top SKIP — ALPHA

1. `regime_gate` — 44
2. `radar_block` — 9
3. `impulse_resonance_wait` — 3
4. `duo_wait` — 3

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `ACE_DUO_PREFLIGHT_10M_BETA_X5.csv` (ok)
- ALPHA CSV: `ACE_DUO_PREFLIGHT_10M_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
