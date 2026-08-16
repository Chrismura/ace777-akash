# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-15T21:53:12Z → 2026-08-16T06:03:13Z (8h10m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-16T06:03:23Z UTC
**Filtre session:** `ts >= 2026-08-15T21:52:47Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.3553 USDT** |
| **PNL ALPHA** | **-0.0755 USDT** |
| **PNL SESSION TOTAL** | **+0.2798 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 160 |
| Gagnants | 46 |
| Perdants | 45 |
| Flat (0) | 69 |
| Win rate | **28.8%** |
| Gains totaux | +1.3351 USDT |
| Pertes totales | -0.9798 USDT |
| **PNL net** | **+0.3553 USDT** |
| BPS moyen | 0.01 |

**Meilleur trade:** +0.1869 USDT
**Pire trade:** -0.1217 USDT

**Direction:** SELL (160)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 121 |
| fluid_exit_brake | 29 |
| fluid_exit_inversion | 10 |

**Cycles SKIP:** 2066
| Raison | Nb |
|--------|-----|
| radar_block | 1738 |
| impulse_resonance_wait | 237 |
| gap_guard_pause | 87 |
| tactic_mismatch | 4 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 12 |
| Gagnants | 3 |
| Perdants | 4 |
| Flat (0) | 5 |
| Win rate | **25.0%** |
| Gains totaux | +0.1300 USDT |
| Pertes totales | -0.2054 USDT |
| **PNL net** | **-0.0755 USDT** |
| BPS moyen | -0.03 |

**Meilleur trade:** +0.1236 USDT
**Pire trade:** -0.1928 USDT

**Direction:** BUY (12)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 10 |
| fluid_exit_brake | 2 |

**Cycles SKIP:** 2201
| Raison | Nb |
|--------|-----|
| radar_block | 1791 |
| impulse_resonance_wait | 271 |
| duo_wait | 137 |
| tactic_mismatch | 2 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 160 | 12 | 172 |
| PnL | +0.3553 | -0.0755 | **+0.2798** |
| Win rate | 28.8% | 25.0% | 28.5% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 1743 | 78.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 324 | 14.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 160 | 7.2% | 160 | +0.3553 |

- Fenêtre: `2026-08-15T21:53:12Z` → `2026-08-16T06:03:07Z` (2227 cycles) · μ(tension)=0.2643 · σ=0.9205 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`

## Engle — couches évolutives (hors moteur)

- Plan: `engle/PLAN_COUCHES_B1_B3.md`
- Journal B1: `engle/journal/ENGLE_JOURNAL_DERNIER.md` (généré via `engle_journal.rb` / `update_state_md.sh`)
- Adapt B2: `ENGLE_ADAPT=0` (défaut OFF = usine pure ; `log` = posture JSON only)
- Dernière posture log: `WAIT_COLD` · régime `COMPRESSE` · applied=`false`

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `0.70` | ALPHA: `0.50`
- SHOCK_EXIT: `16` bps
- VOLATILITY_FILTER: `16`
- STASE: spread=`16` vol=`16`
- POLL_SEC: `0.064`

---

*Rapport auto — CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*
