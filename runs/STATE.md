# ACE777 — STATE

> Généré automatiquement — ne pas éditer à la main
> Phase: `ended` | Statut: `ENDED` | MAJ: `2026-09-08T03:13:58Z`

## Config active

| Paramètre | Valeur |
|-----------|--------|
| Profil | `vide_froid_binance` v`2026-07-08-setup-ready` |
| Masse BETA / ALPHA | `200` / `800` USDT |
| LLM gate | enabled=`TRUE` fail_closed=`TRUE` |
| Modèle LLM | `qwen2.5-coder:1.5b` |
| Tag session | `MASTER_BASE_V8_6_FORTRESS_6H00` |
| run_id | `MASTER_BASE_V8_6_FORTRESS_6H00_20260907T233636Z_64326` |
| Frais Binance | `UNMATCHED_BINANCE_FEES` |

## PnL session

| Unité | FILLED | Win | Loss | Win% | Brut | Frais | Net USDT | SKIP |
|-------|--------|-----|------|------|------|------|----------|------|
| BETA | 46 | 4 | 42 | 8.7% | 0.2709 | 23.6631 | -23.3921 | 986 |
| ALPHA | 17 | 1 | 16 | 5.9% | -1.2512 | 20.5696 | -21.8208 | 1903 |
| **TOTAL** | **63** | — | — | — | **-0.9802** | **44.2327** | **-45.2129** | **2889** |

## Duo session (`duo_session.json`)

- SCOUT PnL: `-23.392132439999997` USDT
- HUNTER PnL: `-21.82080095` USDT
- Total session: `-45.212933389999996` USDT

## Duo live (`duo_state.json`)

| Champ | Valeur |
|-------|--------|
| role | `SCOUT` |
| status | `CLOSED` |
| side | `SELL` |
| bps | `0.17730182` |
| pnl_usdt | `-0.38914546` |
| reason | `exit_fatigue` |
| cycle | `1072` |
| hold_sec | `104` |

## Top SKIP — BETA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 272
2. `reason=COMPRESSE tension=0.00000680 threshold=0.05` — 4
3. `reason=COMPRESSE tension=0.00000984 threshold=0.05` — 4
4. `mom=short structure=long` — 3
5. `reason=COMPRESSE tension=0.00000682 threshold=0.05` — 2

## Top SKIP — ALPHA

1. `reason=COMPRESSE tension=0.00000000 threshold=0.05` — 570
2. `reason=no_trigger mode=none` — 152
3. `mom=short structure=long` — 5
4. `reason=COMPRESSE tension=0.00000380 threshold=0.05` — 4
5. `reason=COMPRESSE tension=0.00000834 threshold=0.05` — 4

## Vortex (`vortex_control.json`)

- Mode: `CHOP`
- Message: `v2_swarm_wind_chop`
- TS: `2026-08-27T08:04:41Z`

## Processus

- master.pid: `stopped`
- beta.pid: `stopped`
- alpha.pid: `stopped`

## Fichiers

- BETA CSV: `MASTER_BASE_V8_6_FORTRESS_6H00_BETA_X5.csv` (ok)
- ALPHA CSV: `MASTER_BASE_V8_6_FORTRESS_6H00_ALPHA_X13_BURST13.csv` (ok)

## Dernière leçon ERREURS_AI

- Fichier: `RAPPORT_INCIDENT_VIE_PRIVEE_CURSOR_BAN_20260812.md`
- Titre: # RAPPORT D'INCIDENT — VIE PRIVÉE · QUOTA · BAN CURSOR

---
_Généré par `scripts/update_state_md.sh`_
