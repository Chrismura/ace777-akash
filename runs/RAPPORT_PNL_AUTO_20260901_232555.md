# RAPPORT PNL AUTO — ACE_RADAR_ALIGNED_V3_15M

**Session:** `ACE_RADAR_ALIGNED_V3_15M`
**run_id:** `ACE_RADAR_ALIGNED_V3_15M_20260901T231047Z_50145`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-01T23:10:59Z → 2026-09-01T23:25:52Z (0h14m)
**Setup:** `?` v`?` | BETA `?` USDT | ALPHA `?` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-01T23:25:55Z UTC
**Filtre session:** `ts >= 2026-09-01T23:10:50Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | +0.7205 USDT |
| Frais BETA | +2.7901 USDT |
| **PNL net BETA** | **-2.0696 USDT** |
| PNL brut ALPHA | -1.0718 USDT |
| Frais ALPHA | +2.1529 USDT |
| **PNL net ALPHA** | **-3.2247 USDT** |
| **PNL SESSION TOTAL** | **-5.2944 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 4 |
| Gagnants | 0 |
| Perdants | 4 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -2.0696 USDT |
| PNL brut | +0.7205 USDT |
| Frais | +2.7901 USDT |
| **PNL net** | **-2.0696 USDT** |
| BPS moyen | 1.80 |

**Meilleur trade:** -0.0834 USDT
**Pire trade:** -0.7981 USDT

**Direction:** SELL (4)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| exit_fatigue | 2 |
| timeout | 2 |

**Cycles SKIP:** 25
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 11 |
| reason=low_confidence conf=0.2981 mom_sig=0.27549376 raw_mom_bps=-5.61226007 spread_bps=5.61230000 tension=0.27549376 bid_drop=1.79070945 ask_drop=0.00983674 swarm=0 | 1 |
| reason=COMPRESSE tension=0.00004733 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.00106266 threshold=0.05 | 1 |
| reason=wall_not_collapsed tension=0.25077269 bid_drop=1.63002248 ask_drop=0.00000000 | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 2 |
| Gagnants | 0 |
| Perdants | 2 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -3.2247 USDT |
| PNL brut | -1.0718 USDT |
| Frais | +2.1529 USDT |
| **PNL net** | **-3.2247 USDT** |
| BPS moyen | -3.98 |

**Meilleur trade:** -1.0695 USDT
**Pire trade:** -2.1553 USDT

**Direction:** BUY (2)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| exit_fatigue | 1 |
| timeout | 1 |

**Cycles SKIP:** 57
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 27 |
| reason=no_trigger mode=none | 3 |
| reason=COMPRESSE tension=0.00151293 threshold=0.05 | 2 |
| reason=COMPRESSE tension=0.02339481 threshold=0.05 | 1 |
| reason=direction_unclear conf=0.1533 mom_sig=0.14664896 raw_mom_bps=0.00000000 spread_bps=5.96140000 tension=0.14664896 bid_drop=0.95321823 ask_drop=0.00000000 swarm=0 | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 4 | 2 | 6 |
| PnL | -2.0696 | -3.2247 | **-5.2944** |
| Win rate | 0.0% | 0.0% | 0.0% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 21 | 72.4% | 4 | +0.7205 |
| TRANSITOIRE (bruit retail) | 8 | 27.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-09-01T23:13:26Z` → `2026-09-01T23:25:51Z` (29 cycles) · μ(tension)=0.1265 · σ=0.2360 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `ACE_RADAR_ALIGNED_V3_15M_BETA_X5.csv`

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

*Rapport auto — CSV: `ACE_RADAR_ALIGNED_V3_15M_BETA_X5.csv` | `ACE_RADAR_ALIGNED_V3_15M_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*
