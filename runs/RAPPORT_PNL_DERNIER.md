# RAPPORT PNL AUTO — ACE_DUO_PREFLIGHT_10M

**Session:** `ACE_DUO_PREFLIGHT_10M`
**Période:** 2026-09-01T13:12:30Z → 2026-09-01T13:22:30Z (0h10m)
**Setup:** `?` v`?` | BETA `?` USDT | ALPHA `?` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-01T13:22:32Z UTC
**Filtre session:** `ts >= 2026-09-01T13:12:21Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.0691 USDT** |
| **PNL ALPHA** | **-0.1868 USDT** |
| **PNL SESSION TOTAL** | **-0.1177 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 2 |
| Gagnants | 1 |
| Perdants | 1 |
| Flat (0) | 0 |
| Win rate | **50.0%** |
| Gains totaux | +0.1382 USDT |
| Pertes totales | -0.0691 USDT |
| **PNL net** | **+0.0691 USDT** |
| BPS moyen | -0.00 |

**Meilleur trade:** +0.1382 USDT
**Pire trade:** -0.0691 USDT

**Direction:** SELL (2)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.79660851 | 1 |
| 0.39824896 | 1 |

**Cycles SKIP:** 51
| Raison | Nb |
|--------|-----|
| regime_gate | 40 |
| radar_block | 11 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 1 |
| Gagnants | 0 |
| Perdants | 1 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -0.1868 USDT |
| **PNL net** | **-0.1868 USDT** |
| BPS moyen | -1.39 |

**Meilleur trade:** -0.1868 USDT
**Pire trade:** -0.1868 USDT

**Direction:** BUY (1)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 1.07666619 | 1 |

**Cycles SKIP:** 59
| Raison | Nb |
|--------|-----|
| regime_gate | 44 |
| radar_block | 9 |
| impulse_resonance_wait | 3 |
| duo_wait | 3 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 2 | 1 | 3 |
| PnL | +0.0691 | -0.1868 | **-0.1177** |
| Win rate | 50.0% | 0.0% | 33.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 42 | 79.2% | 2 | +0.0691 |
| TRANSITOIRE (bruit retail) | 7 | 13.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 4 | 7.5% | 0 | +0.0000 |

- Fenêtre: `2026-09-01T13:12:30Z` → `2026-09-01T13:22:26Z` (53 cycles) · μ(tension)=0.2749 · σ=1.0839 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `ACE_DUO_PREFLIGHT_10M_BETA_X5.csv`

## Engle — couches évolutives (hors moteur)

- Plan: `engle/PLAN_COUCHES_B1_B3.md`
- Journal B1: `engle/journal/ENGLE_JOURNAL_DERNIER.md` (généré via `engle_journal.rb` / `update_state_md.sh`)
- Adapt B2: `ENGLE_ADAPT=0` (défaut OFF = usine pure ; `log` = posture JSON only)
- Dernière posture log: `WAIT_COLD` · régime `COMPRESSE` · applied=`false`

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `?` | ALPHA: `?`
- SHOCK_EXIT: `?` bps
- VOLATILITY_FILTER: `—`
- STASE: spread=`?` vol=`?`
- POLL_SEC: `?`

---

*Rapport auto — CSV: `ACE_DUO_PREFLIGHT_10M_BETA_X5.csv` | `ACE_DUO_PREFLIGHT_10M_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*
