# [PARTIE 3] — JALON HISTORIQUE SOUVERAIN — RUN +29 USDT

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

> **Correction date:** jalon certifié = **2026-07-10** (pas juin). Session **204206**, 20:27 UTC.

---

## 3.1. Analyse Forensique du Gain de +29,41 USDT

### Identité session

| Champ | Valeur |
|---|---|
| Session | **204206** |
| Horodatage | **2026-07-10T20:27:00Z → 20:41:52Z** (14 min) |
| Tag CSV | `MASTER_VORTEX_V2_COLLAB_4H` |
| Genesis md5 | **37fca367** (barrière duo OUI, PHI NON) |
| BETA | SCOUT x5 — 200 USDT — 15 FILLED SELL |
| ALPHA | HUNTER x13 fixe — 800 USDT — 14 FILLED BUY |
| PnL certifié | **+29,4095 USDT** (BETA +1,16 / ALPHA +28,25) |
| Meilleur trade ALPHA | **+22,8643 USDT** @ 20:29:56 UTC |

### Chronologie chaîne soir 10/07

| Rapport | PnL | Rôle |
|---------|-----|------|
| 163716 | -0,33 $ | Premier de la chaîne soir |
| 193940 | +13,23 $ | Premier boot x13 identique |
| 202645 | +0,88 $ | Continuation |
| **204206** | **+29,41 $** | **Jalon souverain** |

### Rapport PnL intégral session 204206

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-07-10T20:27:00Z → 2026-07-10T20:41:52Z (0h14m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-07-10T20:42:06Z UTC
**Filtre session:** `ts >= 2026-07-10T20:26:47Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+1.1616 USDT** |
| **PNL ALPHA** | **+28.2480 USDT** |
| **PNL SESSION TOTAL** | **+29.4095 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 15 |
| Gagnants | 4 |
| Perdants | 10 |
| Flat (0) | 1 |
| Win rate | **26.7%** |
| Gains totaux | +1.5846 USDT |
| Pertes totales | -0.4230 USDT |
| **PNL net** | **+1.1616 USDT** |
| BPS moyen | 2.53 |

**Meilleur trade:** +0.7618 USDT
**Pire trade:** -0.1617 USDT

**Direction:** SELL (15)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 9 |
| fluid_exit_inversion | 6 |

**Cycles SKIP:** 36
| Raison | Nb |
|--------|-----|
| radar_block | 32 |
| impulse_resonance_wait | 3 |
| tactic_mismatch | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 14 |
| Gagnants | 12 |
| Perdants | 1 |
| Flat (0) | 1 |
| Win rate | **85.7%** |
| Gains totaux | +29.9640 USDT |
| Pertes totales | -1.7160 USDT |
| **PNL net** | **+28.2480 USDT** |
| BPS moyen | 2.23 |

**Meilleur trade:** +22.8643 USDT
**Pire trade:** -1.7160 USDT

**Direction:** BUY (14)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 13 |
| fluid_exit_inversion | 1 |

**Cycles SKIP:** 63
| Raison | Nb |
|--------|-----|
| radar_block | 48 |
| impulse_resonance_wait | 9 |
| duo_wait | 5 |
| tactic_mismatch | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 15 | 14 | 29 |
| PnL | +1.1616 | +28.2480 | **+29.4095** |
| Win rate | 26.7% | 85.7% | 55.2% |

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `0.70` | ALPHA: `0.50`
- SHOCK_EXIT: `16` bps
- VOLATILITY_FILTER: `16`
- STASE: spread=`16` vol=`16`
- POLL_SEC: `0.064`

---

*Rapport auto — CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

### Meilleur trade ALPHA — log CSV d'origine

```
2026-07-10T20:29:05Z,15,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=0.96978754 raw_mom_bps=0.00000000 spread_bps=10.20630000 tension=0.96978754 bid_drop=6.30361899 ask_drop=0.00000000 swarm=0
2026-07-10T20:29:14Z,16,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0002 mom_sig=0.00021429 raw_mom_bps=0.00000000 spread_bps=11.11460000 tension=0.00021429 bid_drop=0.00000000 ask_drop=0.00139289 swarm=0
2026-07-10T20:29:22Z,17,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0003 mom_sig=0.00040318 raw_mom_bps=-10.20633734 spread_bps=10.36080000 tension=0.00040318 bid_drop=0.00000000 ask_drop=0.00262070 swarm=0
2026-07-10T20:29:31Z,18,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0 mom_sig=0.00000760 raw_mom_bps=0.00000000 spread_bps=10.59610000 tension=0.00000760 bid_drop=0.00000000 ask_drop=0.00004940 swarm=0
2026-07-10T20:29:56Z,19,BUY,FILLED,63718.80000000,63858.90000000,0.16320000,21.98723140,22.86432000,shock_inversion_stop,radar=short conf=0.719 size_note=strong_conf_full+entry_25_75_full soft=0 pct=0.21987231 tension=2.31057925 bid_drop=15.01876511 ask_drop=0.00000000
```

**Paramètres carnet au moment de la frappe (extrait CSV):**
- Entry: **63718.80** → Exit: **63858.90** (+140.10 $ BTC, ~22 bps)
- Tension: **2.31** | conf radar: **0.719** | size: strong_conf_full
- Exit: `shock_inversion_stop` | hold ~cycle court post-revenge BETA

### Alignement couple asynchrone (preuve logique)

1. BETA publie pertes `shock_inversion_stop` (9×) → `duo_state.json` + SWARM
2. ALPHA lit `duo_hunter_signal mode=revenge` → 14 BUY FILLED
3. Win rate ALPHA **85,7%** vs BETA **26,7%** = transfert d'énergie scout→hunter
4. 5 cycles ALPHA `duo_wait` = gate barrière / fraîcheur duo (pas cannibalisation)
5. Meilleur trade **+22,86 USDT** = choc directionnel majeur capturé par HUNTER x13

### Restauration setup identique 204206

```bash
cd /Users/christophe/ace777-test-day1
./LANCER_IDENTIQUE_204206.sh        # vérif
./LANCER_IDENTIQUE_204206.sh lancer # run (utilisateur seul)
```
