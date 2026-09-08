# RAPPORT PNL AUTO — MASTER_BASE_V8_6_FORTRESS_6H00

**Session:** `MASTER_BASE_V8_6_FORTRESS_6H00`
**run_id:** `MASTER_BASE_V8_6_FORTRESS_6H00_20260907T233636Z_64326`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-07T23:36:47Z → 2026-09-08T03:13:56Z (3h37m)
**Setup:** `?` v`?` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-08T03:13:58Z UTC
**Filtre session:** `ts >= 2026-09-07T23:36:39Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | +0.2709 USDT |
| Frais BETA | +23.6631 USDT |
| **PNL net BETA** | **-23.3921 USDT** |
| PNL brut ALPHA | -1.2512 USDT |
| Frais ALPHA | +20.5696 USDT |
| **PNL net ALPHA** | **-21.8208 USDT** |
| **PNL SESSION TOTAL** | **-45.2129 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 46 |
| Gagnants | 4 |
| Perdants | 42 |
| Flat (0) | 0 |
| Win rate | **8.7%** |
| Gains totaux | +0.8858 USDT |
| Pertes totales | -24.2779 USDT |
| PNL brut | +0.2709 USDT |
| Frais | +23.6631 USDT |
| **PNL net** | **-23.3921 USDT** |
| BPS moyen | 0.40 |

**Meilleur trade:** +0.3446 USDT
**Pire trade:** -1.6169 USDT

**Direction:** SELL (46)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| timeout | 38 |
| exit_fatigue | 7 |
| stop_loss | 1 |

**Cycles SKIP:** 986
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 272 |
| reason=COMPRESSE tension=0.00000680 threshold=0.05 | 4 |
| reason=COMPRESSE tension=0.00000984 threshold=0.05 | 4 |
| mom=short structure=long | 3 |
| reason=COMPRESSE tension=0.00000682 threshold=0.05 | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 17 |
| Gagnants | 1 |
| Perdants | 16 |
| Flat (0) | 0 |
| Win rate | **5.9%** |
| Gains totaux | +0.0319 USDT |
| Pertes totales | -21.8527 USDT |
| PNL brut | -1.2512 USDT |
| Frais | +20.5696 USDT |
| **PNL net** | **-21.8208 USDT** |
| BPS moyen | -0.31 |

**Meilleur trade:** +0.0319 USDT
**Pire trade:** -3.1888 USDT

**Direction:** BUY (17)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| timeout | 12 |
| exit_fatigue | 4 |
| trailing_stop | 1 |

**Cycles SKIP:** 1903
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 570 |
| reason=no_trigger mode=none | 152 |
| mom=short structure=long | 5 |
| reason=COMPRESSE tension=0.00000380 threshold=0.05 | 4 |
| reason=COMPRESSE tension=0.00000834 threshold=0.05 | 4 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 46 | 17 | 63 |
| PnL | -23.3921 | -21.8208 | **-45.2129** |
| Win rate | 8.7% | 5.9% | 7.9% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 955 | 89.1% | 46 | +0.2709 |
| TRANSITOIRE (bruit retail) | 112 | 10.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 5 | 0.5% | 0 | +0.0000 |

- Fenêtre: `2026-09-07T23:36:47Z` → `2026-09-08T03:13:54Z` (1072 cycles) · μ(tension)=0.0697 · σ=0.3933 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `MASTER_BASE_V8_6_FORTRESS_6H00_BETA_X5.csv`

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

*Rapport auto — CSV: `MASTER_BASE_V8_6_FORTRESS_6H00_BETA_X5.csv` | `MASTER_BASE_V8_6_FORTRESS_6H00_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*
