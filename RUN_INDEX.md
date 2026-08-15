# RUN INDEX

Ce fichier sert de table des runs ACE777 pour retrouver vite les tests.

## Format

- Date UTC
- Profil
- Script
- Log
- Parametres cle
- Resultat
- Verdict / Notes

---

## 2026-02-27 - Validation r095 (sans watchdog)

- Profil: `sniper_v1_500_r095_nowd`
- Script: `mini_run_live_smart.sh`
- Logs:
  - `run_sniper_v1_500_r095_bis_nowd.csv`
  - `run_sniper_v1_500_r095_ter_nowd.csv`
- Parametres cle:
  - `BUY_USDT=500`
  - `RADAR_MIN_CONF=0.95`
  - `MIN_PROFIT_BPS=45`
  - `STOP_LOSS_BPS=20`
  - `TRAIL_ARM_BPS=30`
  - `TRAIL_GIVEBACK_BPS=10`
  - `WATCHDOG_ENABLED=FALSE`
  - `CRASH_WATCHDOG_ENABLED=FALSE`
- Resultat:
  - BIS: `-0.26357920 USDT`
  - TER: `-0.26399030 USDT`
  - Total: `-0.52756950 USDT`
- Verdict:
  - Non valide en reproductibilite (faible nombre de trades + sorties `exit_stall` dominantes).

---

## 2026-02-27 - B300 (sans watchdog)

- Profil: `b300_nowd`
- Script: `mini_run_live_smart.sh`
- Log: `run_b300_nowd_01.csv`
- Parametres cle:
  - `BUY_USDT=300`
  - `MIN_PROFIT_BPS=30`
  - `STOP_LOSS_BPS=20`
  - `TRAIL_ARM_BPS=20`
  - `TRAIL_GIVEBACK_BPS=8`
  - `WATCHDOG_ENABLED=FALSE`
  - `CRASH_WATCHDOG_ENABLED=FALSE`
- Resultat:
  - `+0.03969000 USDT`
- Verdict:
  - Marche tres plat, echantillon faible (1 trade), run propre mais non concluant statistiquement.

---

## 2026-02-27 - Harmonique 550

- Profil: `ace777_harmonic_550`
- Script: `mini_run_live_smart.sh`
- Log: `run_ace777_harmonic_550.csv`
- Parametres cle:
  - `BUY_USDT=550`
  - `MIN_PROFIT_BPS=33`
  - `STOP_LOSS_BPS=11`
  - `TRAIL_ARM_BPS=22`
  - `TRAIL_GIVEBACK_BPS=7`
  - `T_BASE=360`
  - `K_ENTROPY=0.015`
  - `MIN_HOLD=45s`
  - `STALL_CONFIRMATIONS=8`
  - `RADAR_MIN_CONF=0.92`
- Resultat (dernier resume):
  - `-0.47057570 USDT` (15 cycles, 2 trades)
- Verdict:
  - Non adapte au regime range/chute observe, forte dominance des `SKIP`, pertes sur rares entrees.

---

## Session en cours - Contre-predation

- Profil: `ace777_predator_550`
- Script: `mini_run_live_smart.sh`
- Log cible: `run_ace777_predator_550.csv`
- Parametres cibles:
  - `BUY_USDT=550`
  - `MIN_PROFIT_BPS=40`
  - `STOP_LOSS_BPS=22`
  - `TRAIL_ARM_BPS=15`
  - `TRAIL_GIVEBACK_BPS=3`
  - `T_BASE=300`
  - `K_ENTROPY=0.03`
  - `STALL_CONFIRMATIONS=5`
  - `RADAR_MIN_CONF=0.88`
- Statut:
  - A lancer / en evaluation.

---

## 2026-02-27 - Contre-predation V1 (range hostile)

- Profil: `ace777_predator_550`
- Script: `mini_run_live_smart.sh`
- Log: `run_ace777_predator_550.csv`
- Parametres cle:
  - `BUY_USDT=550`
  - `MIN_PROFIT_BPS=40`
  - `STOP_LOSS_BPS=22`
  - `TRAIL_ARM_BPS=15`
  - `TRAIL_GIVEBACK_BPS=3`
  - `T_BASE=300`
  - `K_ENTROPY=0.03`
  - `STALL_CONFIRMATIONS=5`
  - `RADAR_MIN_CONF=0.88`
  - `WATCHDOG_ENABLED=FALSE`
- Contexte marche:
  - Range estime ~200 USD avec impulsions courtes.
- Resultat:
  - `Requested=20`, `Successful=9`, `PnL=-0.42950240 USDT`
- Verdict:
  - Non valide sur ce regime (faux departs + sorties `exit_stall` dominantes).
  - Next step validee: **Option B** (`RADAR_MIN_CONF=0.90`, masse 550 inchangee).

---

## 2026-07-08 — MASTER_BASE_V8_5_IMPACT_8H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08`
- Tag: `MASTER_BASE_V8_5_IMPACT_8H00`
- Période: `2026-03-12T11:46:21Z` → `2026-03-13T10:05:55Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_8H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_8H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.6115 USDT` (393 trades)
  - ALPHA: `+1.0716 USDT` (2 trades)
  - Total: `+0.4601 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_052046.md`
- Verdict: `POSITIF`


---

## 2026-07-08 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-03-10T11:09:28Z` → `2026-07-08T09:41:42Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+14.9432 USDT` (365 trades)
  - ALPHA: `-8.4943 USDT` (60 trades)
  - Total: `+6.4489 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_094144.md`
- Verdict: `POSITIF`


---

## 2026-07-08 — MASTER_BASE_V8_5_IMPACT_C2 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_C2`
- Période: `2026-07-08T09:54:43Z` → `2026-07-08T16:04:54Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_C2_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_C2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5816 USDT` (16 trades)
  - ALPHA: `-3.9473 USDT` (21 trades)
  - Total: `-4.5289 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_160457.md`
- Verdict: `NEGATIF`


---

## 2026-07-08 — MASTER_BASE_V8_5_IMPACT_C2 (auto)

- Profil: `non_charge` v`?`
- Tag: `MASTER_BASE_V8_5_IMPACT_C2`
- Période: `2026-07-08T09:54:43Z` → `2026-07-08T16:17:55Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_C2_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_C2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.4741 USDT` (19 trades)
  - ALPHA: `-0.8033 USDT` (23 trades)
  - Total: `-1.2774 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_161759.md`
- Verdict: `NEGATIF`


---

## 2026-07-08 — MASTER_BASE_V8_5_IMPACT_C2 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_C2`
- Période: `2026-07-08T09:54:43Z` → `2026-07-08T16:23:27Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_C2_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_C2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.6751 USDT` (20 trades)
  - ALPHA: `+0.5082 USDT` (24 trades)
  - Total: `-0.1669 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_162333.md`
- Verdict: `NEGATIF`


---

## 2026-07-08 — MASTER_HYBRID_VF_20260708 (auto)

- Profil: `non_charge` v`?`
- Tag: `MASTER_HYBRID_VF_20260708`
- Période: `2026-07-08T16:25:36Z` → `2026-07-08T20:25:13Z`
- Logs:
  - `MASTER_HYBRID_VF_20260708_BETA_X5.csv`
  - `MASTER_HYBRID_VF_20260708_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-1.4941 USDT` (55 trades)
  - ALPHA: `-3.5764 USDT` (31 trades)
  - Total: `-5.0705 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_202705.md`
- Verdict: `NEGATIF`


---

## 2026-07-08 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-08-gemini-cursor-v2`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-08T20:52:31Z` → `2026-07-08T21:05:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_210515.md`
- Verdict: `NEUTRE`


---

## 2026-07-08 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-08T21:07:57Z` → `2026-07-08T21:31:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0318 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0318 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260708_213117.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-08-gemini-cursor-v2`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-08T21:31:33Z` → `2026-07-09T01:31:24Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5790 USDT` (41 trades)
  - ALPHA: `-1.3616 USDT` (20 trades)
  - Total: `+0.2174 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_013126.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-08-gemini-cursor-v2`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T06:46:23Z` → `2026-07-09T10:48:15Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.2534 USDT` (152 trades)
  - ALPHA: `+10.8490 USDT` (57 trades)
  - Total: `+13.1023 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_104817.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T11:23:27Z` → `2026-07-09T11:31:01Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1562 USDT` (9 trades)
  - ALPHA: `+0.3856 USDT` (3 trades)
  - Total: `+0.5418 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_113110.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-08-gemini-cursor-v2`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T11:33:40Z` → `2026-07-09T16:40:06Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4124 USDT` (233 trades)
  - ALPHA: `+1.6356 USDT` (6 trades)
  - Total: `+2.0480 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_164009.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T11:33:40Z` → `2026-07-09T16:40:06Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4124 USDT` (233 trades)
  - ALPHA: `+1.6356 USDT` (6 trades)
  - Total: `+2.0480 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_165903.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T17:00:27Z` → `2026-07-09T17:10:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4952 USDT` (6 trades)
  - ALPHA: `+0.0794 USDT` (3 trades)
  - Total: `-0.4158 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_181251.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T17:00:27Z` → `2026-07-09T17:10:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4952 USDT` (6 trades)
  - ALPHA: `+0.0794 USDT` (3 trades)
  - Total: `-0.4158 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_181312.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T17:00:27Z` → `2026-07-09T17:10:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4952 USDT` (6 trades)
  - ALPHA: `+0.0794 USDT` (3 trades)
  - Total: `-0.4158 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_181506.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T18:15:20Z` → `2026-07-09T18:17:16Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_181718.md`
- Verdict: `NEUTRE`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T18:17:23Z` → `2026-07-09T18:31:05Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1591 USDT` (11 trades)
  - ALPHA: `-0.3154 USDT` (5 trades)
  - Total: `-0.1563 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_183850.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T18:39:02Z` → `2026-07-09T18:53:20Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.7486 USDT` (12 trades)
  - ALPHA: `+3.1748 USDT` (7 trades)
  - Total: `+2.4262 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_185325.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T18:53:57Z` → `2026-07-09T19:04:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0307 USDT` (3 trades)
  - ALPHA: `-0.8256 USDT` (2 trades)
  - Total: `-0.8563 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_190951.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T19:10:03Z` → `2026-07-09T19:24:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0947 USDT` (9 trades)
  - ALPHA: `-1.8108 USDT` (4 trades)
  - Total: `-1.9055 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_194101.md`
- Verdict: `NEGATIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-08-gemini-cursor-v2`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T19:41:12Z` → `2026-07-09T20:37:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6738 USDT` (37 trades)
  - ALPHA: `+1.3080 USDT` (6 trades)
  - Total: `+1.9818 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_203732.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T19:41:12Z` → `2026-07-09T20:37:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6738 USDT` (37 trades)
  - ALPHA: `+1.3080 USDT` (6 trades)
  - Total: `+1.9818 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_212948.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-09-v2.2-swarm-cohesion`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T21:32:47Z` → `2026-07-09T21:38:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0603 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0603 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_213821.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-09-v2.2-swarm-cohesion`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T21:38:58Z` → `2026-07-09T22:02:23Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1606 USDT` (19 trades)
  - ALPHA: `+0.5467 USDT` (6 trades)
  - Total: `+0.7073 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_220226.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-09-v2.2-swarm-cohesion`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T22:03:44Z` → `2026-07-09T22:15:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1213 USDT` (8 trades)
  - ALPHA: `+0.7110 USDT` (2 trades)
  - Total: `+0.5897 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_221559.md`
- Verdict: `POSITIF`


---

## 2026-07-09 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-09-v2.2-swarm-cohesion`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T22:19:28Z` → `2026-07-09T22:40:50Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7684 USDT` (9 trades)
  - ALPHA: `-1.0964 USDT` (2 trades)
  - Total: `-0.3280 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260709_224052.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T22:19:28Z` → `2026-07-09T22:40:50Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7684 USDT` (9 trades)
  - ALPHA: `-1.0964 USDT` (2 trades)
  - Total: `-0.3280 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_060918.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-09T22:19:28Z` → `2026-07-09T22:40:50Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7684 USDT` (9 trades)
  - ALPHA: `-1.0964 USDT` (2 trades)
  - Total: `-0.3280 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_064920.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T06:49:31Z` → `2026-07-10T07:01:05Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0953 USDT` (8 trades)
  - ALPHA: `-0.9570 USDT` (3 trades)
  - Total: `-0.8617 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_073013.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T07:30:33Z` → `2026-07-10T07:35:07Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2678 USDT` (3 trades)
  - ALPHA: `+2.3250 USDT` (1 trades)
  - Total: `+2.5928 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_073509.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T07:30:33Z` → `2026-07-10T07:35:07Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2678 USDT` (3 trades)
  - ALPHA: `+2.3250 USDT` (1 trades)
  - Total: `+2.5928 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_073543.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T07:35:55Z` → `2026-07-10T07:51:46Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0500 USDT` (5 trades)
  - ALPHA: `+0.3145 USDT` (4 trades)
  - Total: `+0.2646 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_075155.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T07:35:55Z` → `2026-07-10T07:51:46Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0500 USDT` (5 trades)
  - ALPHA: `+0.3145 USDT` (4 trades)
  - Total: `+0.2646 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_080954.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T08:10:06Z` → `2026-07-10T08:36:55Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-1.0258 USDT` (17 trades)
  - ALPHA: `+26.8768 USDT` (15 trades)
  - Total: `+25.8509 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_083706.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T08:37:22Z` → `2026-07-10T09:01:12Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1046 USDT` (22 trades)
  - ALPHA: `-2.4814 USDT` (5 trades)
  - Total: `-2.3768 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_090121.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T09:33:31Z` → `2026-07-10T10:09:24Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3700 USDT` (26 trades)
  - ALPHA: `+0.1022 USDT` (15 trades)
  - Total: `-0.2678 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_100929.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T10:10:30Z` → `2026-07-10T10:24:38Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0102 USDT` (8 trades)
  - ALPHA: `+2.2473 USDT` (4 trades)
  - Total: `+2.2371 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_102443.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_101019_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_101019_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_104508.md`
- Verdict: `NEUTRE`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T10:49:52Z` → `2026-07-10T10:52:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_104941_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_104941_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_105208.md`
- Verdict: `NEUTRE`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H_20260710_105208 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H_20260710_105208`
- Période: `2026-07-10T10:52:21Z` → `2026-07-10T11:02:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_105208_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_20260710_105208_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1023 USDT` (4 trades)
  - ALPHA: `-2.9294 USDT` (1 trades)
  - Total: `-3.0317 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_111856.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T11:19:07Z` → `2026-07-10T11:26:02Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0019 USDT` (2 trades)
  - ALPHA: `+0.5312 USDT` (2 trades)
  - Total: `+0.5294 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_112604.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T11:19:07Z` → `2026-07-10T11:26:02Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0019 USDT` (2 trades)
  - ALPHA: `+0.5312 USDT` (2 trades)
  - Total: `+0.5294 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_130257.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T13:04:40Z` → `2026-07-10T13:21:25Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5047 USDT` (15 trades)
  - ALPHA: `+0.2781 USDT` (5 trades)
  - Total: `+0.7828 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_132139.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T13:21:56Z` → `2026-07-10T13:42:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2022 USDT` (14 trades)
  - ALPHA: `-4.3160 USDT` (3 trades)
  - Total: `-4.5183 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_134232.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T13:42:59Z` → `2026-07-10T14:00:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0188 USDT` (4 trades)
  - ALPHA: `-7.3089 USDT` (3 trades)
  - Total: `-7.3277 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_140445.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T14:05:13Z` → `2026-07-10T14:16:43Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7176 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.7176 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_141655.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T14:17:26Z` → `2026-07-10T14:21:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0732 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0732 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_142147.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T14:17:26Z` → `2026-07-10T14:21:52Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0732 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0732 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_142634.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T14:28:21Z` → `2026-07-10T14:49:24Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-1.2222 USDT` (13 trades)
  - ALPHA: `-0.8625 USDT` (9 trades)
  - Total: `-2.0847 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_144932.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T14:17:26Z` → `2026-07-10T14:49:24Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-1.1490 USDT` (15 trades)
  - ALPHA: `-0.8625 USDT` (9 trades)
  - Total: `-2.0115 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_150041.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:00:55Z` → `2026-07-10T15:25:31Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0032 USDT` (27 trades)
  - ALPHA: `+8.6316 USDT` (15 trades)
  - Total: `+9.6347 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_152540.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:26:04Z` → `2026-07-10T15:38:17Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0524 USDT` (9 trades)
  - ALPHA: `-1.8024 USDT` (5 trades)
  - Total: `-1.8548 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_153827.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:38:43Z` → `2026-07-10T15:51:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2935 USDT` (5 trades)
  - ALPHA: `-4.0885 USDT` (5 trades)
  - Total: `-3.7950 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_155135.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:51:52Z` → `2026-07-10T15:57:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2045 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.2045 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_155709.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:57:16Z` → `2026-07-10T15:57:40Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_155745.md`
- Verdict: `NEUTRE`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T15:57:58Z` → `2026-07-10T15:58:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_155830.md`
- Verdict: `NEUTRE`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T16:26:05Z` → `2026-07-10T16:37:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0910 USDT` (9 trades)
  - ALPHA: `-0.2371 USDT` (4 trades)
  - Total: `-0.3281 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_163716.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T16:37:33Z` → `2026-07-10T16:48:23Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.6107 USDT` (11 trades)
  - ALPHA: `+6.3417 USDT` (5 trades)
  - Total: `+5.7310 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_164836.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T16:48:53Z` → `2026-07-10T16:54:33Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.9038 USDT` (7 trades)
  - ALPHA: `+7.5966 USDT` (7 trades)
  - Total: `+6.6929 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_165435.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T16:54:57Z` → `2026-07-10T16:58:21Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0365 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0365 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_165828.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T17:16:01Z` → `2026-07-10T17:51:36Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2042 USDT` (23 trades)
  - ALPHA: `+2.5589 USDT` (9 trades)
  - Total: `+2.3548 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_175145.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T17:52:02Z` → `2026-07-10T18:15:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7329 USDT` (29 trades)
  - ALPHA: `+3.5629 USDT` (5 trades)
  - Total: `+4.2958 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_181511.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T18:15:38Z` → `2026-07-10T19:26:57Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3624 USDT` (54 trades)
  - ALPHA: `+0.8625 USDT` (3 trades)
  - Total: `+1.2249 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_192706.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T19:27:27Z` → `2026-07-10T19:39:30Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.6791 USDT` (9 trades)
  - ALPHA: `+13.9080 USDT` (8 trades)
  - Total: `+13.2290 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_193940.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T19:39:58Z` → `2026-07-10T20:24:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8783 USDT` (34 trades)
  - ALPHA: `+0.0000 USDT` (2 trades)
  - Total: `+0.8783 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_202500.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T19:39:58Z` → `2026-07-10T20:24:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8783 USDT` (34 trades)
  - ALPHA: `+0.0000 USDT` (2 trades)
  - Total: `+0.8783 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_202645.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T20:27:00Z` → `2026-07-10T20:41:52Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.1616 USDT` (15 trades)
  - ALPHA: `+28.2480 USDT` (14 trades)
  - Total: `+29.4095 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_204206.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T20:42:26Z` → `2026-07-10T21:02:14Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0096 USDT` (9 trades)
  - ALPHA: `+1.0274 USDT` (5 trades)
  - Total: `+1.0178 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_210222.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:02:39Z` → `2026-07-10T21:09:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2101 USDT` (7 trades)
  - ALPHA: `+2.8976 USDT` (3 trades)
  - Total: `+2.6875 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_210901.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:11:57Z` → `2026-07-10T21:19:58Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2176 USDT` (6 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `-0.2176 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_212000.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:11:57Z` → `2026-07-10T21:20:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2176 USDT` (6 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `-0.2176 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_212305.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:23:17Z` → `2026-07-10T21:35:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2455 USDT` (6 trades)
  - ALPHA: `+4.7340 USDT` (7 trades)
  - Total: `+4.4884 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_213543.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:36:06Z` → `2026-07-10T21:48:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2968 USDT` (10 trades)
  - ALPHA: `-0.4542 USDT` (4 trades)
  - Total: `-0.7510 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_214818.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:48:37Z` → `2026-07-10T21:51:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0074 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0074 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_215108.md`
- Verdict: `POSITIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T21:55:20Z` → `2026-07-10T22:11:59Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3683 USDT` (15 trades)
  - ALPHA: `+0.0000 USDT` (2 trades)
  - Total: `-0.3683 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_221200.md`
- Verdict: `NEGATIF`


---

## 2026-07-10 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-10T22:12:17Z` → `2026-07-10T22:33:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4759 USDT` (17 trades)
  - ALPHA: `+0.3898 USDT` (1 trades)
  - Total: `-0.0862 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260710_223324.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T07:28:48Z` → `2026-07-11T07:42:33Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2825 USDT` (10 trades)
  - ALPHA: `-0.7925 USDT` (3 trades)
  - Total: `-1.0750 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_074243.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T07:43:01Z` → `2026-07-11T07:57:35Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0474 USDT` (11 trades)
  - ALPHA: `-0.1462 USDT` (3 trades)
  - Total: `-0.0989 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_075740.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T07:43:01Z` → `2026-07-11T07:57:35Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0474 USDT` (11 trades)
  - ALPHA: `-0.1462 USDT` (3 trades)
  - Total: `-0.0989 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_075740.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T07:58:19Z` → `2026-07-11T08:12:25Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2815 USDT` (10 trades)
  - ALPHA: `+0.1868 USDT` (8 trades)
  - Total: `-0.0947 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_081236.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T07:58:19Z` → `2026-07-11T08:12:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2815 USDT` (10 trades)
  - ALPHA: `+0.1868 USDT` (8 trades)
  - Total: `-0.0947 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_081422.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T08:14:35Z` → `2026-07-11T08:33:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0413 USDT` (16 trades)
  - ALPHA: `+0.6375 USDT` (5 trades)
  - Total: `+0.6788 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_083320.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T08:35:05Z` → `2026-07-11T09:01:40Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1288 USDT` (13 trades)
  - ALPHA: `+1.5582 USDT` (4 trades)
  - Total: `+1.4293 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_090143.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T08:35:05Z` → `2026-07-11T09:01:40Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1288 USDT` (13 trades)
  - ALPHA: `+1.5582 USDT` (4 trades)
  - Total: `+1.4293 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_090144.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T09:13:12Z` → `2026-07-11T09:42:23Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5628 USDT` (21 trades)
  - ALPHA: `+3.4461 USDT` (11 trades)
  - Total: `+2.8833 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_094232.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T09:42:50Z` → `2026-07-11T09:53:23Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0977 USDT` (5 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0977 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_095335.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T09:55:38Z` → `2026-07-11T10:11:05Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0321 USDT` (10 trades)
  - ALPHA: `+1.3609 USDT` (9 trades)
  - Total: `+1.3287 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_101107.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T10:11:25Z` → `2026-07-11T11:07:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3361 USDT` (40 trades)
  - ALPHA: `+0.5468 USDT` (9 trades)
  - Total: `+0.8828 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_113323.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T11:56:49Z` → `2026-07-11T11:56:59Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_115659.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T11:56:49Z` → `2026-07-11T11:56:59Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_115722.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T12:04:19Z` → `2026-07-11T12:18:38Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1177 USDT` (8 trades)
  - ALPHA: `+0.0000 USDT` (3 trades)
  - Total: `+0.1177 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_121842.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T12:23:52Z` → `2026-07-11T12:43:52Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0143 USDT` (16 trades)
  - ALPHA: `-2.8953 USDT` (7 trades)
  - Total: `-2.8810 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_124409.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T12:23:52Z` → `2026-07-11T12:43:52Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0143 USDT` (16 trades)
  - ALPHA: `-2.8953 USDT` (7 trades)
  - Total: `-2.8810 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_124510.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T12:52:10Z` → `2026-07-11T12:55:13Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_125520.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T14:11:10Z` → `2026-07-11T14:26:09Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_142617.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T14:29:54Z` → `2026-07-11T14:46:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1783 USDT` (20 trades)
  - ALPHA: `+0.2383 USDT` (8 trades)
  - Total: `+0.0600 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_144635.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T14:48:17Z` → `2026-07-11T14:51:35Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0502 USDT` (5 trades)
  - ALPHA: `-1.9626 USDT` (1 trades)
  - Total: `-1.9125 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_145139.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T14:56:52Z` → `2026-07-11T15:02:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=500`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0269 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0269 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_150259.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T15:38:21Z` → `2026-07-11T15:56:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=500`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2371 USDT` (15 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+1.2371 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_155649.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T15:57:54Z` → `2026-07-11T16:08:15Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=500`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2519 USDT` (9 trades)
  - ALPHA: `-1.5917 USDT` (6 trades)
  - Total: `-1.3398 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_160822.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T16:08:54Z` → `2026-07-11T16:22:21Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=500`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5841 USDT` (12 trades)
  - ALPHA: `-1.9233 USDT` (3 trades)
  - Total: `-1.3392 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_162224.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T16:48:10Z` → `2026-07-11T17:02:33Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0333 USDT` (14 trades)
  - ALPHA: `+2.2928 USDT` (9 trades)
  - Total: `+2.3260 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_170236.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T17:20:37Z` → `2026-07-11T17:29:16Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2135 USDT` (5 trades)
  - ALPHA: `+4.8475 USDT` (2 trades)
  - Total: `+4.6340 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_172917.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T17:20:37Z` → `2026-07-11T17:29:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2135 USDT` (5 trades)
  - ALPHA: `+4.8475 USDT` (2 trades)
  - Total: `+4.6340 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_174059.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T17:43:46Z` → `2026-07-11T17:43:53Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_174359.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T17:43:46Z` → `2026-07-11T17:43:53Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_174659.md`
- Verdict: `NEUTRE`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T17:47:44Z` → `2026-07-11T18:19:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1491 USDT` (15 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+0.1491 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_181947.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T18:20:16Z` → `2026-07-11T18:36:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2590 USDT` (18 trades)
  - ALPHA: `+1.9045 USDT` (11 trades)
  - Total: `+1.6455 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_183651.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T18:37:09Z` → `2026-07-11T19:04:17Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4672 USDT` (21 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.4672 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_190423.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T18:37:09Z` → `2026-07-11T19:04:34Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4672 USDT` (22 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.4672 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_190727.md`
- Verdict: `POSITIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T19:08:09Z` → `2026-07-11T19:41:14Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1031 USDT` (22 trades)
  - ALPHA: `-0.9265 USDT` (3 trades)
  - Total: `-0.8234 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_194118.md`
- Verdict: `NEGATIF`


---

## 2026-07-11 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-11T19:41:43Z` → `2026-07-11T19:45:57Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260711_194559.md`
- Verdict: `NEUTRE`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T06:46:00Z` → `2026-07-12T06:51:34Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2048 USDT` (7 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.2048 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_065140.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T06:51:57Z` → `2026-07-12T06:56:05Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0800 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0800 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_065607.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T06:51:57Z` → `2026-07-12T06:56:05Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0800 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0800 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_065607.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T07:00:36Z` → `2026-07-12T07:14:01Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0679 USDT` (12 trades)
  - ALPHA: `-0.9823 USDT` (2 trades)
  - Total: `-1.0502 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_071403.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T07:21:20Z` → `2026-07-12T07:24:36Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0836 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0836 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_072437.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T07:21:20Z` → `2026-07-12T07:24:36Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0836 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0836 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_072438.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T08:20:00Z` → `2026-07-12T08:28:38Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0381 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `-0.0381 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_082840.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T08:31:57Z` → `2026-07-12T08:43:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0924 USDT` (7 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0924 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_084313.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T08:31:57Z` → `2026-07-12T08:43:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0924 USDT` (7 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0924 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_084313.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T09:12:58Z` → `2026-07-12T09:26:47Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1172 USDT` (10 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+0.1172 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_092655.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T09:12:58Z` → `2026-07-12T09:26:47Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1172 USDT` (10 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+0.1172 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_092655.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T10:15:43Z` → `2026-07-12T10:35:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2051 USDT` (8 trades)
  - ALPHA: `-0.2076 USDT` (2 trades)
  - Total: `-0.4127 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_103529.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T10:54:35Z` → `2026-07-12T11:07:16Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1171 USDT` (7 trades)
  - ALPHA: `+3.6580 USDT` (8 trades)
  - Total: `+3.5409 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_110721.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T10:54:35Z` → `2026-07-12T11:07:16Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1171 USDT` (7 trades)
  - ALPHA: `+3.6580 USDT` (8 trades)
  - Total: `+3.5409 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_110818.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T11:28:23Z` → `2026-07-12T11:32:11Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1575 USDT` (2 trades)
  - ALPHA: `+1.1088 USDT` (3 trades)
  - Total: `+0.9513 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_113220.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T11:44:35Z` → `2026-07-12T11:44:49Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_114454.md`
- Verdict: `NEUTRE`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_114545.md`
- Verdict: `NEUTRE`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T11:47:41Z` → `2026-07-12T11:52:32Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0186 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0186 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_115237.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T11:47:41Z` → `2026-07-12T11:52:32Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0186 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0186 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_115731.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T11:58:02Z` → `2026-07-12T12:04:51Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0316 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0316 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_120451.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:05:36Z` → `2026-07-12T12:12:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0525 USDT` (4 trades)
  - ALPHA: `+0.8293 USDT` (4 trades)
  - Total: `+0.7768 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_121231.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:05:36Z` → `2026-07-12T12:12:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0525 USDT` (4 trades)
  - ALPHA: `+0.8293 USDT` (4 trades)
  - Total: `+0.7768 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_122231.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:22:56Z` → `2026-07-12T12:23:11Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0015 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0015 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_122314.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:22:56Z` → `2026-07-12T12:23:11Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0015 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0015 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_122521.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:25:34Z` → `2026-07-12T12:32:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1509 USDT` (8 trades)
  - ALPHA: `+2.2601 USDT` (2 trades)
  - Total: `+2.4110 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_123202.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:32:34Z` → `2026-07-12T12:32:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1776 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1776 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_123856.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T12:39:23Z` → `2026-07-12T12:39:32Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_123947.md`
- Verdict: `NEUTRE`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T13:02:37Z` → `2026-07-12T13:13:30Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1794 USDT` (10 trades)
  - ALPHA: `+0.4915 USDT` (4 trades)
  - Total: `+0.3121 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_131339.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T13:13:58Z` → `2026-07-12T13:21:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0474 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0474 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_132104.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T13:13:58Z` → `2026-07-12T13:21:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0474 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0474 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_154829.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T13:13:58Z` → `2026-07-12T13:21:04Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0474 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0474 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_154913.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T15:52:48Z` → `2026-07-12T16:10:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_161044.md`
- Verdict: `NEUTRE`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T16:21:02Z` → `2026-07-12T16:33:20Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0792 USDT` (5 trades)
  - ALPHA: `-0.0891 USDT` (6 trades)
  - Total: `-0.1683 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_163434.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T16:35:36Z` → `2026-07-12T16:50:27Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0398 USDT` (13 trades)
  - ALPHA: `-0.9894 USDT` (4 trades)
  - Total: `-0.9497 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_165037.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T16:50:55Z` → `2026-07-12T16:57:47Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1963 USDT` (6 trades)
  - ALPHA: `-2.2028 USDT` (3 trades)
  - Total: `-2.0065 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_165755.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T16:58:13Z` → `2026-07-12T16:59:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0084 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0084 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_165957.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T17:03:54Z` → `2026-07-12T17:18:51Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0758 USDT` (14 trades)
  - ALPHA: `+0.6908 USDT` (4 trades)
  - Total: `+0.6150 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_171902.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T17:19:27Z` → `2026-07-12T18:03:52Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2053 USDT` (35 trades)
  - ALPHA: `+2.5790 USDT` (4 trades)
  - Total: `+2.7843 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_180354.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:10:01Z` → `2026-07-12T20:31:07Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0183 USDT` (18 trades)
  - ALPHA: `+0.5710 USDT` (2 trades)
  - Total: `+0.5528 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_203110.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:36:11Z` → `2026-07-12T20:50:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0306 USDT` (8 trades)
  - ALPHA: `-0.1638 USDT` (5 trades)
  - Total: `-0.1945 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_205013.md`
- Verdict: `NEGATIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:50:30Z` → `2026-07-12T20:59:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0536 USDT` (4 trades)
  - ALPHA: `+2.2599 USDT` (3 trades)
  - Total: `+2.2063 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_205928.md`
- Verdict: `POSITIF`


---

## 2026-07-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:50:30Z` → `2026-07-12T20:59:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0536 USDT` (4 trades)
  - ALPHA: `+2.2599 USDT` (3 trades)
  - Total: `+2.2063 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260712_211449.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:50:30Z` → `2026-07-12T20:59:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0536 USDT` (4 trades)
  - ALPHA: `+2.2599 USDT` (3 trades)
  - Total: `+2.2063 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_131538.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-12T20:50:30Z` → `2026-07-12T20:59:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0536 USDT` (4 trades)
  - ALPHA: `+2.2599 USDT` (3 trades)
  - Total: `+2.2063 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_131734.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T13:24:56Z` → `2026-07-13T13:30:54Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5233 USDT` (3 trades)
  - ALPHA: `-16.8392 USDT` (1 trades)
  - Total: `-16.3159 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_133057.md`
- Verdict: `NEGATIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T13:31:24Z` → `2026-07-13T13:41:30Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1864 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1864 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_134140.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T13:42:57Z` → `2026-07-13T13:50:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4052 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.4052 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_135001.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T14:08:18Z` → `2026-07-13T14:11:32Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_141136.md`
- Verdict: `NEUTRE`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T14:15:21Z` → `2026-07-13T14:31:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1888 USDT` (6 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1888 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_143146.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T15:53:26Z` → `2026-07-13T16:07:58Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0296 USDT` (12 trades)
  - ALPHA: `-2.3950 USDT` (7 trades)
  - Total: `-2.3654 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_160800.md`
- Verdict: `NEGATIF`


---

## 2026-07-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-07-13T15:53:26Z` → `2026-07-13T16:07:58Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0296 USDT` (12 trades)
  - ALPHA: `-2.3950 USDT` (7 trades)
  - Total: `-2.3654 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_161503.md`
- Verdict: `NEGATIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T16:15:19Z` → `2026-07-13T16:29:51Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.3362 USDT` (11 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+1.3362 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_162955.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T16:15:19Z` → `2026-07-13T16:29:51Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.3362 USDT` (11 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+1.3362 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_170955.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T17:10:25Z` → `2026-07-13T18:42:03Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5123 USDT` (93 trades)
  - ALPHA: `+0.0025 USDT` (10 trades)
  - Total: `+1.5148 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_184204.md`
- Verdict: `POSITIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T18:50:27Z` → `2026-07-13T19:17:16Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2248 USDT` (28 trades)
  - ALPHA: `-1.6599 USDT` (2 trades)
  - Total: `-1.4350 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_191721.md`
- Verdict: `NEGATIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T19:27:40Z` → `2026-07-13T19:36:57Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1597 USDT` (11 trades)
  - ALPHA: `-6.8116 USDT` (4 trades)
  - Total: `-6.6520 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_193658.md`
- Verdict: `NEGATIF`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T21:05:19Z` → `2026-07-13T21:13:46Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_211408.md`
- Verdict: `NEUTRE`


---

## 2026-07-13 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T21:05:19Z` → `2026-07-13T21:13:46Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260713_211420.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-13T21:05:19Z` → `2026-07-13T21:13:46Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_035355.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-14T03:54:31Z` → `2026-07-14T03:54:31Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_035435.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — MASTER_BASE_V8_5_IMPACT_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H00`
- Période: `2026-07-14T04:05:50Z` → `2026-07-14T06:49:28Z`
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H00_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0533 USDT` (91 trades)
  - ALPHA: `-11.9994 USDT` (16 trades)
  - Total: `-10.9461 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_064947.md`
- Verdict: `NEGATIF`


---

## 2026-07-14 — NUAGE_SMOKE_15M (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_SMOKE_15M`
- Période: `2026-07-14T06:34:37Z` → `2026-07-14T06:49:29Z`
- Logs:
  - `NUAGE_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2976 USDT` (8 trades)
  - ALPHA: `+1.0120 USDT` (1 trades)
  - Total: `+0.7144 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_065706.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_4H00 (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_4H00`
- Période: `2026-07-14T06:57:38Z` → `2026-07-14T09:07:03Z`
- Logs:
  - `NUAGE_4H00_BETA_X5.csv`
  - `NUAGE_4H00_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.6552 USDT` (90 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+2.6552 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_090705.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2_SMOKE_15M (auto)

- Profil: `vide_froid_binance` v`V2_WATCHDOG`
- Tag: `NUAGE_V2_SMOKE_15M`
- Période: `2026-07-14T10:10:15Z` → `2026-07-14T10:25:06Z`
- Logs:
  - `NUAGE_V2_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2433 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.2433 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_105145.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2_SMOKE_15M (auto)

- Profil: `non_charge` v`V2_WATCHDOG`
- Tag: `NUAGE_V2_SMOKE_15M`
- Période: `2026-07-14T10:10:15Z` → `2026-07-14T10:25:06Z`
- Logs:
  - `NUAGE_V2_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.2433 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.2433 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_112331.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_4H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_112635.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_142848.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_143044.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_144555.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-14T11:26:52Z` → `2026-07-14T14:28:41Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.2479 USDT` (125 trades)
  - ALPHA: `+35.4865 USDT` (7 trades)
  - Total: `+35.2386 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_144633.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_SMOKE_1447Z (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_SMOKE_1447Z`
- Période: `` → ``
- Logs:
  - `NUAGE_SMOKE_1447Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1447Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_144709.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_145310.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_145533.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_SMOKE_1447Z (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_SMOKE_1447Z`
- Période: `2026-07-14T14:47:26Z` → `2026-07-14T14:53:08Z`
- Logs:
  - `NUAGE_SMOKE_1447Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1447Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0720 USDT` (7 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0720 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_145941.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_SMOKE_1503Z (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_SMOKE_1503Z`
- Période: `` → ``
- Logs:
  - `NUAGE_SMOKE_1503Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1503Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_150316.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_151752.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_151849.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_SMOKE_1523Z (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_SMOKE_1523Z`
- Période: `` → ``
- Logs:
  - `NUAGE_SMOKE_1523Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1523Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_152343.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_174656.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_BOOTTEST_1747Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_BOOTTEST_1747Z`
- Période: `2026-07-14T17:48:02Z` → `2026-07-14T17:48:23Z`
- Logs:
  - `NUAGE_BOOTTEST_1747Z_BETA_X5.csv`
  - `NUAGE_BOOTTEST_1747Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_174825.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_174850.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_174902.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_BOOTTEST_1749Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_BOOTTEST_1749Z`
- Période: `2026-07-14T17:49:43Z` → `2026-07-14T17:50:04Z`
- Logs:
  - `NUAGE_BOOTTEST_1749Z_BETA_X5.csv`
  - `NUAGE_BOOTTEST_1749Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_175006.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_SMOKE_1526Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SMOKE_1526Z`
- Période: `2026-07-14T15:26:31Z` → `2026-07-14T15:41:18Z`
- Logs:
  - `NUAGE_SMOKE_1526Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1526Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.6071 USDT` (7 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.6071 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_180655.md`
- Verdict: `NEGATIF`


---

## 2026-07-14 — NUAGE_SMOKE_1807Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SMOKE_1807Z`
- Période: `2026-07-14T18:07:13Z` → `2026-07-14T18:22:12Z`
- Logs:
  - `NUAGE_SMOKE_1807Z_BETA_X5.csv`
  - `NUAGE_SMOKE_1807Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.1156 USDT` (10 trades)
  - ALPHA: `-1.1853 USDT` (1 trades)
  - Total: `-1.3009 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_182922.md`
- Verdict: `NEGATIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_183705.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_PROD_4H_20260714_1829Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H_20260714_1829Z`
- Période: `2026-07-14T18:29:41Z` → `2026-07-14T18:37:03Z`
- Logs:
  - `NUAGE_PROD_4H_20260714_1829Z_BETA_X5.csv`
  - `NUAGE_PROD_4H_20260714_1829Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.0506 USDT` (6 trades)
  - ALPHA: `-4.4516 USDT` (1 trades)
  - Total: `-3.4011 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_183921.md`
- Verdict: `NEGATIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_195127.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_BOOTTEST_2006Z (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_BOOTTEST_2006Z`
- Période: `2026-07-14T20:06:45Z` → `2026-07-14T20:06:45Z`
- Logs:
  - `NUAGE_BOOTTEST_2006Z_BETA_X5.csv`
  - `NUAGE_BOOTTEST_2006Z_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_200657.md`
- Verdict: `NEUTRE`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_204345.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_204838.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-14T20:44:57Z` → `2026-07-14T20:48:33Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.4054 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.4054 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_205004.md`
- Verdict: `NEGATIF`


---

## 2026-07-14 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_221847.md`
- Verdict: `POSITIF`


---

## 2026-07-14 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-14T20:50:25Z` → `2026-07-14T22:04:42Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.5679 USDT` (58 trades)
  - ALPHA: `+1.3856 USDT` (2 trades)
  - Total: `+1.9534 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260714_221939.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_044540.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-14T22:22:13Z` → `2026-07-15T02:22:06Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-2.4376 USDT` (215 trades)
  - ALPHA: `+9.9459 USDT` (2 trades)
  - Total: `+7.5083 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_044733.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_054131.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T05:42:27Z` → `2026-07-15T06:46:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.7210 USDT` (61 trades)
  - ALPHA: `-4.8919 USDT` (1 trades)
  - Total: `-4.1709 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_070715.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T07:08:45Z` → `2026-07-15T08:43:19Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5232 USDT` (80 trades)
  - ALPHA: `+7.3746 USDT` (3 trades)
  - Total: `+7.8978 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_085207.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T08:52:26Z` → `2026-07-15T09:38:15Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.2500 USDT` (29 trades)
  - ALPHA: `-6.3398 USDT` (2 trades)
  - Total: `-6.5898 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_094133.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T09:41:56Z` → `2026-07-15T10:12:29Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-1.7119 USDT` (25 trades)
  - ALPHA: `-0.0261 USDT` (1 trades)
  - Total: `-1.7380 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_105643.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T10:57:02Z` → `2026-07-15T11:48:10Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.1475 USDT` (36 trades)
  - ALPHA: `-0.5624 USDT` (2 trades)
  - Total: `-0.7099 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_121039.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T12:11:00Z` → `2026-07-15T12:36:40Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-1.5777 USDT` (16 trades)
  - ALPHA: `-0.4433 USDT` (1 trades)
  - Total: `-2.0210 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_123840.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T12:39:08Z` → `2026-07-15T13:00:06Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-2.2303 USDT` (20 trades)
  - ALPHA: `-3.0615 USDT` (5 trades)
  - Total: `-5.2918 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_144344.md`
- Verdict: `NEGATIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T14:44:17Z` → `2026-07-15T16:20:30Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.3061 USDT` (86 trades)
  - ALPHA: `+3.1624 USDT` (3 trades)
  - Total: `+4.4685 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_163007.md`
- Verdict: `POSITIF`


---

## 2026-07-15 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T16:30:48Z` → `2026-07-15T20:30:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-6.2442 USDT` (208 trades)
  - ALPHA: `+46.4580 USDT` (11 trades)
  - Total: `+40.2138 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260715_203116.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T20:31:51Z` → `2026-07-15T23:06:05Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+2.1541 USDT` (126 trades)
  - ALPHA: `+3.1963 USDT` (6 trades)
  - Total: `+5.3504 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_004336.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-15T20:31:51Z` → `2026-07-15T23:06:05Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+2.1541 USDT` (126 trades)
  - ALPHA: `+3.1963 USDT` (6 trades)
  - Total: `+5.3504 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_041850.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T04:19:25Z` → `2026-07-16T06:22:44Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.6326 USDT` (91 trades)
  - ALPHA: `+1.0848 USDT` (3 trades)
  - Total: `+0.4522 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_063401.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_080905.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_081600.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_082338.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_082633.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_V2.1_SMOKE_15M (auto)

- Profil: `non_charge` v`V2.1_STROBOSCOPE`
- Tag: `NUAGE_V2.1_SMOKE_15M`
- Période: `2026-07-14T10:53:17Z` → `2026-07-14T11:08:08Z`
- Logs:
  - `NUAGE_V2.1_SMOKE_15M_BETA_X5.csv`
  - `NUAGE_V2.1_SMOKE_15M_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.3299 USDT` (16 trades)
  - ALPHA: `+3.3782 USDT` (2 trades)
  - Total: `+3.0484 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_082951.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_084145.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_084515.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_093358.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_24H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_24H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_24H_BETA_X5.csv`
  - `NUAGE_PROD_24H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_094124.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_094313.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_094456.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_094825.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_095010.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T08:45:37Z` → `2026-07-16T09:07:37Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6502 USDT` (22 trades)
  - ALPHA: `-0.8877 USDT` (1 trades)
  - Total: `-0.2374 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_095305.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_095634.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_100012.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_100151.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_101127.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_101355.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_101831.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_101859.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T10:20:16Z` → `2026-07-16T10:25:24Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (3 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_102529.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T10:28:48Z` → `2026-07-16T11:01:26Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.4807 USDT` (17 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+1.4807 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_110133.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T11:02:52Z` → `2026-07-16T12:06:15Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.3529 USDT` (51 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.3529 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_120620.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:07:03Z` → `2026-07-16T12:08:09Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0356 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0356 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_120812.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:07:03Z` → `2026-07-16T12:08:17Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0356 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0356 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_120825.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:08:43Z` → `2026-07-16T12:09:06Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_120911.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:08:43Z` → `2026-07-16T12:09:14Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_121223.md`
- Verdict: `NEUTRE`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:12:41Z` → `2026-07-16T12:13:23Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.0234 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0234 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_121323.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `?` v`?`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:12:41Z` → `2026-07-16T12:13:25Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-0.0234 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0234 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_121455.md`
- Verdict: `NEGATIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:15:16Z` → `2026-07-16T12:15:55Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1891 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1891 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_121557.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:15:16Z` → `2026-07-16T12:15:55Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.1891 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1891 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_122114.md`
- Verdict: `POSITIF`


---

## 2026-07-16 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:15:16Z` → `2026-07-16T12:15:55Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.1891 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1891 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260716_122448.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:15:16Z` → `2026-07-16T12:15:55Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.1891 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1891 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_062533.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_720H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `NUAGE_PROD_720H`
- Période: `2026-07-16T12:15:16Z` → `2026-07-16T12:15:55Z`
- Logs:
  - `NUAGE_PROD_720H_BETA_X5.csv`
  - `NUAGE_PROD_720H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1891 USDT` (2 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.1891 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_063606.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_063946.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_064527.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_065000.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_070545.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-16T06:34:24Z` → `2026-07-16T07:40:11Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.6607 USDT` (65 trades)
  - ALPHA: `-0.6308 USDT` (1 trades)
  - Total: `+0.0299 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_072715.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T07:30:44Z` → `2026-07-17T08:18:30Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.9942 USDT` (36 trades)
  - ALPHA: `+0.0000 USDT` (5 trades)
  - Total: `+0.9942 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_081848.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H_SYNC (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H_SYNC`
- Période: `2026-07-17T08:20:31Z` → `2026-07-17T08:36:56Z`
- Logs:
  - `NUAGE_PROD_4H_SYNC_BETA_X5.csv`
  - `NUAGE_PROD_4H_SYNC_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.4892 USDT` (16 trades)
  - ALPHA: `-0.9820 USDT` (1 trades)
  - Total: `-0.4928 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_091403.md`
- Verdict: `NEGATIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T09:14:38Z` → `2026-07-17T10:18:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `-2.1654 USDT` (72 trades)
  - ALPHA: `+2.1078 USDT` (5 trades)
  - Total: `-0.0576 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_103144.md`
- Verdict: `NEGATIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_170526.md`
- Verdict: `NEUTRE`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T17:05:45Z` → `2026-07-17T17:11:18Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-2.7531 USDT` (6 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-2.7531 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_171119.md`
- Verdict: `NEGATIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T17:12:19Z` → `2026-07-17T18:36:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.6416 USDT` (71 trades)
  - ALPHA: `+0.9382 USDT` (4 trades)
  - Total: `+2.5798 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_183720.md`
- Verdict: `POSITIF`


---

## 2026-07-17 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T18:38:36Z` → `2026-07-17T19:41:44Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4890 USDT` (42 trades)
  - ALPHA: `-0.0243 USDT` (1 trades)
  - Total: `+0.4646 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260717_194222.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050349.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050354.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050358.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050841.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050842.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-17T19:44:53Z` → `2026-07-17T23:44:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4087 USDT` (153 trades)
  - ALPHA: `+13.1932 USDT` (4 trades)
  - Total: `+13.6019 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_050846.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-18T05:11:11Z` → `2026-07-18T07:05:10Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7088 USDT` (53 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.7088 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_070511.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-18T05:11:11Z` → `2026-07-18T07:17:18Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8984 USDT` (59 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.8984 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_071721.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-18T05:11:11Z` → `2026-07-18T07:17:18Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8984 USDT` (59 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.8984 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_071721.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-18T05:11:11Z` → `2026-07-18T07:17:18Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8984 USDT` (59 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.8984 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_071725.md`
- Verdict: `POSITIF`


---

## 2026-07-18 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-18T05:11:11Z` → `2026-07-18T07:17:18Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.8984 USDT` (59 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.8984 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260718_071734.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T07:19:29Z` → `2026-07-19T08:25:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0033 USDT` (24 trades)
  - ALPHA: `-0.0260 USDT` (1 trades)
  - Total: `+0.9772 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_082603.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T07:19:29Z` → `2026-07-19T08:25:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0033 USDT` (24 trades)
  - ALPHA: `-0.0260 USDT` (1 trades)
  - Total: `+0.9772 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_082603.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T08:28:26Z` → `2026-07-19T12:28:07Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.8032 USDT` (146 trades)
  - ALPHA: `+3.1706 USDT` (5 trades)
  - Total: `+5.9738 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_123224.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T08:28:26Z` → `2026-07-19T12:28:07Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.8032 USDT` (146 trades)
  - ALPHA: `+3.1706 USDT` (5 trades)
  - Total: `+5.9738 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_123604.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T08:28:26Z` → `2026-07-19T12:28:07Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.8032 USDT` (146 trades)
  - ALPHA: `+3.1706 USDT` (5 trades)
  - Total: `+5.9738 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_123604.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T08:28:26Z` → `2026-07-19T12:28:07Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.8032 USDT` (146 trades)
  - ALPHA: `+3.1706 USDT` (5 trades)
  - Total: `+5.9738 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_123608.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_123805.md`
- Verdict: `NEUTRE`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T12:38:14Z` → `2026-07-19T12:52:57Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1345 USDT` (16 trades)
  - ALPHA: `-0.0275 USDT` (3 trades)
  - Total: `+0.1070 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_125306.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T12:38:14Z` → `2026-07-19T12:52:57Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1345 USDT` (16 trades)
  - ALPHA: `-0.0275 USDT` (3 trades)
  - Total: `+0.1070 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_125307.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_125316.md`
- Verdict: `NEUTRE`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T12:53:32Z` → `2026-07-19T13:05:55Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0222 USDT` (11 trades)
  - ALPHA: `-0.1628 USDT` (3 trades)
  - Total: `-0.1849 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_130604.md`
- Verdict: `NEGATIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T12:53:32Z` → `2026-07-19T13:05:55Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0222 USDT` (11 trades)
  - ALPHA: `-0.1628 USDT` (3 trades)
  - Total: `-0.1849 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_130604.md`
- Verdict: `NEGATIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `` → ``
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_130614.md`
- Verdict: `NEUTRE`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135305.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135306.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135310.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135319.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135817.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:06:23Z` → `2026-07-19T13:51:59Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.7054 USDT` (20 trades)
  - ALPHA: `+1.5079 USDT` (5 trades)
  - Total: `+2.2133 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_135817.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:59:51Z` → `2026-07-19T15:38:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0295 USDT` (48 trades)
  - ALPHA: `-0.4312 USDT` (3 trades)
  - Total: `+0.5983 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_153836.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:59:51Z` → `2026-07-19T15:38:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0295 USDT` (48 trades)
  - ALPHA: `-0.4312 USDT` (3 trades)
  - Total: `+0.5983 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_153837.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:59:51Z` → `2026-07-19T15:38:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0295 USDT` (48 trades)
  - ALPHA: `-0.4312 USDT` (3 trades)
  - Total: `+0.5983 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_153841.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:59:51Z` → `2026-07-19T15:38:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0295 USDT` (48 trades)
  - ALPHA: `-0.4312 USDT` (3 trades)
  - Total: `+0.5983 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_153918.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T13:59:51Z` → `2026-07-19T15:38:36Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.0295 USDT` (48 trades)
  - ALPHA: `-0.4312 USDT` (3 trades)
  - Total: `+0.5983 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_153918.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_164927.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_164927.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_164937.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_164937.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_170528.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_170529.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T15:41:17Z` → `2026-07-19T16:49:20Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3914 USDT` (35 trades)
  - ALPHA: `+13.5605 USDT` (4 trades)
  - Total: `+13.9519 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_170533.md`
- Verdict: `POSITIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T17:11:08Z` → `2026-07-19T19:48:42Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6500 USDT` (108 trades)
  - ALPHA: `-6.2972 USDT` (1 trades)
  - Total: `-5.6472 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_194846.md`
- Verdict: `NEGATIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T17:11:08Z` → `2026-07-19T19:48:42Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6500 USDT` (108 trades)
  - ALPHA: `-6.2972 USDT` (1 trades)
  - Total: `-5.6472 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_194847.md`
- Verdict: `NEGATIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T17:11:08Z` → `2026-07-19T19:48:42Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6500 USDT` (108 trades)
  - ALPHA: `-6.2972 USDT` (1 trades)
  - Total: `-5.6472 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_194857.md`
- Verdict: `NEGATIF`


---

## 2026-07-19 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T17:11:08Z` → `2026-07-19T19:48:42Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6500 USDT` (108 trades)
  - ALPHA: `-6.2972 USDT` (1 trades)
  - Total: `-5.6472 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260719_194857.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T19:52:29Z` → `2026-07-19T23:52:19Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4235 USDT` (179 trades)
  - ALPHA: `+8.9146 USDT` (3 trades)
  - Total: `+8.4911 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_044701.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T19:52:29Z` → `2026-07-19T23:52:19Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4235 USDT` (179 trades)
  - ALPHA: `+8.9146 USDT` (3 trades)
  - Total: `+8.4911 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_044920.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-19T19:52:29Z` → `2026-07-19T23:52:19Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4235 USDT` (179 trades)
  - ALPHA: `+8.9146 USDT` (3 trades)
  - Total: `+8.4911 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_044920.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T08:07:55Z` → `2026-07-20T10:18:37Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4063 USDT` (84 trades)
  - ALPHA: `+8.2475 USDT` (4 trades)
  - Total: `+8.6537 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_101840.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T08:07:55Z` → `2026-07-20T10:18:37Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4063 USDT` (84 trades)
  - ALPHA: `+8.2475 USDT` (4 trades)
  - Total: `+8.6537 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_101840.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T08:07:55Z` → `2026-07-20T10:18:37Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4063 USDT` (84 trades)
  - ALPHA: `+8.2475 USDT` (4 trades)
  - Total: `+8.6537 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_102429.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T08:07:55Z` → `2026-07-20T10:18:37Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4063 USDT` (84 trades)
  - ALPHA: `+8.2475 USDT` (4 trades)
  - Total: `+8.6537 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_102430.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T08:07:55Z` → `2026-07-20T10:18:37Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4063 USDT` (84 trades)
  - ALPHA: `+8.2475 USDT` (4 trades)
  - Total: `+8.6537 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_102434.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T10:28:00Z` → `2026-07-20T13:33:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-3.2210 USDT` (120 trades)
  - ALPHA: `-0.7233 USDT` (2 trades)
  - Total: `-3.9443 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_133353.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T10:28:00Z` → `2026-07-20T13:33:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-3.2210 USDT` (120 trades)
  - ALPHA: `-0.7233 USDT` (2 trades)
  - Total: `-3.9443 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_133353.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T10:28:00Z` → `2026-07-20T13:33:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-3.2210 USDT` (120 trades)
  - ALPHA: `-0.7233 USDT` (2 trades)
  - Total: `-3.9443 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_133358.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T13:34:34Z` → `2026-07-20T15:25:23Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2110 USDT` (133 trades)
  - ALPHA: `+4.2744 USDT` (9 trades)
  - Total: `+5.4854 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_165654.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T13:34:34Z` → `2026-07-20T15:25:23Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2110 USDT` (133 trades)
  - ALPHA: `+4.2744 USDT` (9 trades)
  - Total: `+5.4854 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_165654.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T13:34:34Z` → `2026-07-20T15:25:23Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2110 USDT` (133 trades)
  - ALPHA: `+4.2744 USDT` (9 trades)
  - Total: `+5.4854 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_165659.md`
- Verdict: `POSITIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T16:57:53Z` → `2026-07-20T17:25:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5754 USDT` (9 trades)
  - ALPHA: `-2.0494 USDT` (1 trades)
  - Total: `-1.4739 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_172559.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T16:57:53Z` → `2026-07-20T17:25:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5754 USDT` (9 trades)
  - ALPHA: `-2.0494 USDT` (1 trades)
  - Total: `-1.4739 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_172559.md`
- Verdict: `NEGATIF`


---

## 2026-07-20 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-20T16:57:53Z` → `2026-07-20T17:25:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5754 USDT` (9 trades)
  - ALPHA: `-2.0494 USDT` (1 trades)
  - Total: `-1.4739 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260720_172604.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103448.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:43Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103449.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103453.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103838.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103838.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103843.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103954.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103955.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T07:57:20Z` → `2026-07-21T10:34:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3664 USDT` (39 trades)
  - ALPHA: `+0.1057 USDT` (2 trades)
  - Total: `-0.2607 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_103959.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T10:40:16Z` → `2026-07-21T14:40:12Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2726 USDT` (105 trades)
  - ALPHA: `-1.9521 USDT` (2 trades)
  - Total: `-2.2247 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_145008.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T10:40:16Z` → `2026-07-21T14:40:12Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2726 USDT` (105 trades)
  - ALPHA: `-1.9521 USDT` (2 trades)
  - Total: `-2.2247 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_145009.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T10:40:16Z` → `2026-07-21T14:40:12Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.2726 USDT` (105 trades)
  - ALPHA: `-1.9521 USDT` (2 trades)
  - Total: `-2.2247 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_145013.md`
- Verdict: `NEGATIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T14:50:32Z` → `2026-07-21T18:50:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3582 USDT` (94 trades)
  - ALPHA: `+11.4667 USDT` (10 trades)
  - Total: `+11.1085 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_185911.md`
- Verdict: `POSITIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T14:50:32Z` → `2026-07-21T18:50:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3582 USDT` (94 trades)
  - ALPHA: `+11.4667 USDT` (10 trades)
  - Total: `+11.1085 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_185912.md`
- Verdict: `POSITIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T14:50:32Z` → `2026-07-21T18:50:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3582 USDT` (94 trades)
  - ALPHA: `+11.4667 USDT` (10 trades)
  - Total: `+11.1085 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_185917.md`
- Verdict: `POSITIF`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T19:01:34Z` → `2026-07-21T19:02:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_190331.md`
- Verdict: `NEUTRE`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T19:01:34Z` → `2026-07-21T19:02:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_190331.md`
- Verdict: `NEUTRE`


---

## 2026-07-21 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-21T19:01:34Z` → `2026-07-21T19:02:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260721_190336.md`
- Verdict: `NEUTRE`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T06:42:00Z` → `2026-07-22T10:41:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1266 USDT` (66 trades)
  - ALPHA: `-10.5614 USDT` (9 trades)
  - Total: `-10.4348 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_114225.md`
- Verdict: `NEGATIF`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T06:42:00Z` → `2026-07-22T10:41:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1266 USDT` (66 trades)
  - ALPHA: `-10.5614 USDT` (9 trades)
  - Total: `-10.4348 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_114226.md`
- Verdict: `NEGATIF`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T06:42:00Z` → `2026-07-22T10:41:51Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1266 USDT` (66 trades)
  - ALPHA: `-10.5614 USDT` (9 trades)
  - Total: `-10.4348 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_114230.md`
- Verdict: `NEGATIF`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T11:45:04Z` → `2026-07-22T14:22:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.7306 USDT` (51 trades)
  - ALPHA: `+0.1696 USDT` (5 trades)
  - Total: `-0.5609 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_143239.md`
- Verdict: `NEGATIF`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T11:45:04Z` → `2026-07-22T14:22:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.7306 USDT` (51 trades)
  - ALPHA: `+0.1696 USDT` (5 trades)
  - Total: `-0.5609 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_143239.md`
- Verdict: `NEGATIF`


---

## 2026-07-22 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-22T11:45:04Z` → `2026-07-22T14:22:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.7306 USDT` (51 trades)
  - ALPHA: `+0.1696 USDT` (5 trades)
  - Total: `-0.5609 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260722_143244.md`
- Verdict: `NEGATIF`


---

## 2026-07-29 — NUAGE_TEST_4H_0729b (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_4H_0729b`
- Période: `2026-07-29T13:15:21Z` → `2026-07-29T13:15:23Z`
- Logs:
  - `NUAGE_TEST_4H_0729b_BETA_X5.csv`
  - `NUAGE_TEST_4H_0729b_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_131529.md`
- Verdict: `NEUTRE`


---

## 2026-07-29 — NUAGE_TEST_4H_0729b (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_4H_0729b`
- Période: `2026-07-29T13:15:21Z` → `2026-07-29T13:15:23Z`
- Logs:
  - `NUAGE_TEST_4H_0729b_BETA_X5.csv`
  - `NUAGE_TEST_4H_0729b_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_131529.md`
- Verdict: `NEUTRE`


---

## 2026-07-29 — NUAGE_TEST_4H_0729b (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_4H_0729b`
- Période: `2026-07-29T13:15:21Z` → `2026-07-29T13:15:23Z`
- Logs:
  - `NUAGE_TEST_4H_0729b_BETA_X5.csv`
  - `NUAGE_TEST_4H_0729b_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_131536.md`
- Verdict: `NEUTRE`


---

## 2026-07-29 — NUAGE_TEST_4H_0729b (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_4H_0729b`
- Période: `2026-07-29T13:21:46Z` → `2026-07-29T15:08:54Z`
- Logs:
  - `NUAGE_TEST_4H_0729b_BETA_X5.csv`
  - `NUAGE_TEST_4H_0729b_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0119 USDT` (34 trades)
  - ALPHA: `+7.5013 USDT` (5 trades)
  - Total: `+7.4893 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_150857.md`
- Verdict: `POSITIF`


---

## 2026-07-29 — VALIDATION_VOIE_A_PACK_A (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A`
- Tag: `VALIDATION_VOIE_A_PACK_A`
- Période: `` → ``
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_151251.md`
- Verdict: `NEUTRE`


---

## 2026-07-29 — VALIDATION_VOIE_A_PACK_A (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A`
- Tag: `VALIDATION_VOIE_A_PACK_A`
- Période: `2026-07-29T15:12:58Z` → `2026-07-29T20:02:33Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5526 USDT` (253 trades)
  - ALPHA: `+18.2349 USDT` (28 trades)
  - Total: `+19.7876 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_200235.md`
- Verdict: `POSITIF`


---

## 2026-07-29 — VALIDATION_VOIE_A_PACK_A (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A`
- Tag: `VALIDATION_VOIE_A_PACK_A`
- Période: `2026-07-29T15:12:58Z` → `2026-07-29T20:02:33Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.5526 USDT` (253 trades)
  - ALPHA: `+18.2349 USDT` (28 trades)
  - Total: `+19.7876 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_200235.md`
- Verdict: `POSITIF`


---

## 2026-07-29 — VALIDATION_VOIE_A_PACK_B (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_B`
- Tag: `VALIDATION_VOIE_A_PACK_B`
- Période: `` → ``
- Logs:
  - `VALIDATION_VOIE_A_PACK_B_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_B_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260729_201336.md`
- Verdict: `NEUTRE`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_B (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_B`
- Tag: `VALIDATION_VOIE_A_PACK_B`
- Période: `2026-07-29T20:13:44Z` → `2026-07-30T00:13:36Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_B_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_B_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0122 USDT` (110 trades)
  - ALPHA: `-19.1938 USDT` (13 trades)
  - Total: `-19.1817 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_001339.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_B (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_B`
- Tag: `VALIDATION_VOIE_A_PACK_B`
- Période: `2026-07-29T20:13:44Z` → `2026-07-30T00:13:36Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_B_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_B_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.0122 USDT` (110 trades)
  - ALPHA: `-19.1938 USDT` (13 trades)
  - Total: `-19.1817 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_001339.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `` → ``
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_062220.md`
- Verdict: `NEUTRE`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_102243.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_102243.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_151036.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_151036.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_151041.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_155601.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_155601.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — VALIDATION_VOIE_A_PACK_A_P2 (auto)

- Profil: `VALIDATION_VOIE_A` v`pack_A_P2`
- Tag: `VALIDATION_VOIE_A_PACK_A_P2`
- Période: `2026-07-30T06:22:26Z` → `2026-07-30T10:22:24Z`
- Logs:
  - `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv`
  - `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6224 USDT` (202 trades)
  - ALPHA: `-0.8128 USDT` (10 trades)
  - Total: `+0.8096 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_155607.md`
- Verdict: `POSITIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_183255.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `non_charge` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=?`
  - `BUY_USDT_ALPHA=?`
  - `LLM_GATE_ENABLED=?`
  - `LLM_GATE_FAIL_CLOSED=?`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_183256.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_183340.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_184156.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_184156.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T15:58:26Z` → `2026-07-30T17:58:18Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2552 USDT` (26 trades)
  - ALPHA: `-1.5139 USDT` (3 trades)
  - Total: `-1.2587 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_184202.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T18:42:20Z` → `2026-07-30T19:38:57Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5433 USDT` (33 trades)
  - ALPHA: `-0.0804 USDT` (1 trades)
  - Total: `-0.6237 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_203313.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T18:42:20Z` → `2026-07-30T19:38:57Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5433 USDT` (33 trades)
  - ALPHA: `-0.0804 USDT` (1 trades)
  - Total: `-0.6237 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_204257.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T18:42:20Z` → `2026-07-30T19:38:57Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5433 USDT` (33 trades)
  - ALPHA: `-0.0804 USDT` (1 trades)
  - Total: `-0.6237 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_204258.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T18:42:20Z` → `2026-07-30T19:38:57Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.5433 USDT` (33 trades)
  - ALPHA: `-0.0804 USDT` (1 trades)
  - Total: `-0.6237 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_204303.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T20:43:39Z` → `2026-07-30T21:36:35Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.4740 USDT` (48 trades)
  - ALPHA: `-2.7554 USDT` (2 trades)
  - Total: `-1.2814 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_221140.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T20:43:39Z` → `2026-07-30T21:36:35Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.4740 USDT` (48 trades)
  - ALPHA: `-2.7554 USDT` (2 trades)
  - Total: `-1.2814 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_221140.md`
- Verdict: `NEGATIF`


---

## 2026-07-30 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T20:43:39Z` → `2026-07-30T21:36:35Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.4740 USDT` (48 trades)
  - ALPHA: `-2.7554 USDT` (2 trades)
  - Total: `-1.2814 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260730_221145.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T22:13:30Z` → `2026-07-31T00:13:26Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.1944 USDT` (62 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+2.1944 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_043413.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T22:13:30Z` → `2026-07-31T00:13:26Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.1944 USDT` (62 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+2.1944 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_043413.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_SETUP_AVANT (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_SETUP_AVANT`
- Période: `2026-07-30T22:13:30Z` → `2026-07-31T00:13:26Z`
- Logs:
  - `NUAGE_SETUP_AVANT_BETA_X5.csv`
  - `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.1944 USDT` (62 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `+2.1944 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_043419.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T05:16:04Z` → `2026-07-31T09:15:56Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5350 USDT` (47 trades)
  - ALPHA: `-3.3345 USDT` (2 trades)
  - Total: `-1.7995 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_093709.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T05:16:04Z` → `2026-07-31T09:15:56Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5350 USDT` (47 trades)
  - ALPHA: `-3.3345 USDT` (2 trades)
  - Total: `-1.7995 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_093710.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T05:16:04Z` → `2026-07-31T09:15:56Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.5350 USDT` (47 trades)
  - ALPHA: `-3.3345 USDT` (2 trades)
  - Total: `-1.7995 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_093718.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T09:38:15Z` → `2026-07-31T13:01:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6630 USDT` (37 trades)
  - ALPHA: `+8.0032 USDT` (2 trades)
  - Total: `+8.6662 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_135935.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T09:38:15Z` → `2026-07-31T13:01:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6630 USDT` (37 trades)
  - ALPHA: `+8.0032 USDT` (2 trades)
  - Total: `+8.6662 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_135935.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T09:38:15Z` → `2026-07-31T13:01:26Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.6630 USDT` (37 trades)
  - ALPHA: `+8.0032 USDT` (2 trades)
  - Total: `+8.6662 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_135942.md`
- Verdict: `POSITIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T14:07:21Z` → `2026-07-31T18:07:10Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-5.9965 USDT` (161 trades)
  - ALPHA: `+2.8561 USDT` (6 trades)
  - Total: `-3.1405 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_181929.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T14:07:21Z` → `2026-07-31T18:07:10Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-5.9965 USDT` (161 trades)
  - ALPHA: `+2.8561 USDT` (6 trades)
  - Total: `-3.1405 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_181929.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T14:07:21Z` → `2026-07-31T18:07:10Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-5.9965 USDT` (161 trades)
  - ALPHA: `+2.8561 USDT` (6 trades)
  - Total: `-3.1405 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_181938.md`
- Verdict: `NEGATIF`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T18:38:31Z` → `2026-07-31T18:45:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_185840.md`
- Verdict: `NEUTRE`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T18:38:31Z` → `2026-07-31T18:45:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_185841.md`
- Verdict: `NEUTRE`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T18:38:31Z` → `2026-07-31T18:45:03Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_185847.md`
- Verdict: `NEUTRE`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T19:00:17Z` → `2026-07-31T19:06:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_193433.md`
- Verdict: `NEUTRE`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T19:00:17Z` → `2026-07-31T19:06:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_193433.md`
- Verdict: `NEUTRE`


---

## 2026-07-31 — NUAGE_PROD_4H (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_PROD_4H`
- Période: `2026-07-31T19:00:17Z` → `2026-07-31T19:06:52Z`
- Logs:
  - `NUAGE_PROD_4H_BETA_X5.csv`
  - `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260731_193440.md`
- Verdict: `NEUTRE`


---

## 2026-08-04 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260804_145839.md`
- Verdict: `NEGATIF`


---

## 2026-08-04 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260804_145839.md`
- Verdict: `NEGATIF`


---

## 2026-08-04 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260804_145846.md`
- Verdict: `NEGATIF`


---

## 2026-08-10 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260810_212148.md`
- Verdict: `NEGATIF`


---

## 2026-08-10 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260810_212148.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102342.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102343.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102413.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102413.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102454.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — NUAGE_TEST_8H_CMP3 (auto)

- Profil: `vide_froid_binance` v`V2.2.1_NO_SUICIDE`
- Tag: `NUAGE_TEST_8H_CMP3`
- Période: `2026-08-02T18:18:24Z` → `2026-08-02T19:54:01Z`
- Logs:
  - `NUAGE_TEST_8H_CMP3_BETA_X5.csv`
  - `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0047 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0047 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_102454.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_162906.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T16:29:48Z` → `2026-08-12T16:59:06Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0869 USDT` (11 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0869 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_165910.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T16:29:48Z` → `2026-08-12T16:59:06Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0869 USDT` (11 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0869 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_165911.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_165942.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T17:00:07Z` → `2026-08-12T20:59:57Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2569 USDT` (77 trades)
  - ALPHA: `+1.2663 USDT` (1 trades)
  - Total: `+2.5232 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_210002.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T17:00:07Z` → `2026-08-12T20:59:57Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.2569 USDT` (77 trades)
  - ALPHA: `+1.2663 USDT` (1 trades)
  - Total: `+2.5232 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_210003.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_220432.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_221037.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:10:44Z` → `2026-08-12T22:12:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1981 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `-0.1981 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_221206.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:10:44Z` → `2026-08-12T22:12:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1981 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (1 trades)
  - Total: `-0.1981 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_221206.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_221222.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:12:32Z` → `2026-08-12T22:23:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0625 USDT` (4 trades)
  - ALPHA: `+1.3876 USDT` (5 trades)
  - Total: `+1.3251 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_222345.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:12:32Z` → `2026-08-12T22:23:37Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0625 USDT` (4 trades)
  - ALPHA: `+1.3876 USDT` (5 trades)
  - Total: `+1.3251 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_222346.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_222356.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:24:08Z` → `2026-08-12T22:41:01Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0767 USDT` (3 trades)
  - ALPHA: `-5.0264 USDT` (5 trades)
  - Total: `-4.9497 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_224118.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:24:08Z` → `2026-08-12T22:41:01Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0767 USDT` (3 trades)
  - ALPHA: `-5.0264 USDT` (5 trades)
  - Total: `-4.9497 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_224119.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_224135.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:41:56Z` → `2026-08-12T23:12:25Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0600 USDT` (9 trades)
  - ALPHA: `-1.9393 USDT` (7 trades)
  - Total: `-1.8794 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_231229.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T22:41:56Z` → `2026-08-12T23:12:25Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0600 USDT` (9 trades)
  - ALPHA: `-1.9393 USDT` (7 trades)
  - Total: `-1.8794 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_231230.md`
- Verdict: `NEGATIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_232740.md`
- Verdict: `NEUTRE`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T23:28:00Z` → `2026-08-12T23:49:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1175 USDT` (7 trades)
  - ALPHA: `+0.3771 USDT` (5 trades)
  - Total: `+0.2596 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_234917.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T23:28:00Z` → `2026-08-12T23:49:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1175 USDT` (7 trades)
  - ALPHA: `+0.3771 USDT` (5 trades)
  - Total: `+0.2596 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_234918.md`
- Verdict: `POSITIF`


---

## 2026-08-12 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260812_234928.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T23:49:36Z` → `2026-08-13T00:02:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0261 USDT` (9 trades)
  - ALPHA: `+2.1443 USDT` (4 trades)
  - Total: `+2.1182 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_000305.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-12T23:49:36Z` → `2026-08-13T00:02:56Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0261 USDT` (9 trades)
  - ALPHA: `+2.1443 USDT` (4 trades)
  - Total: `+2.1182 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_000306.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_000316.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T00:03:28Z` → `2026-08-13T00:17:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0948 USDT` (5 trades)
  - ALPHA: `+4.7418 USDT` (5 trades)
  - Total: `+4.6470 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_001750.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T00:03:28Z` → `2026-08-13T00:17:42Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0948 USDT` (5 trades)
  - ALPHA: `+4.7418 USDT` (5 trades)
  - Total: `+4.6470 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_001751.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_001802.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T00:18:12Z` → `2026-08-13T00:42:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4116 USDT` (5 trades)
  - ALPHA: `+3.0258 USDT` (7 trades)
  - Total: `+2.6142 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_004253.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T00:18:12Z` → `2026-08-13T00:42:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.4116 USDT` (5 trades)
  - ALPHA: `+3.0258 USDT` (7 trades)
  - Total: `+2.6142 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_004253.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_004303.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_070127.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:01:34Z` → `2026-08-13T07:18:14Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0088 USDT` (10 trades)
  - ALPHA: `+0.4031 USDT` (5 trades)
  - Total: `+0.4119 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_071822.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:01:34Z` → `2026-08-13T07:18:14Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0088 USDT` (10 trades)
  - ALPHA: `+0.4031 USDT` (5 trades)
  - Total: `+0.4119 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_071822.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_071832.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:18:40Z` → `2026-08-13T08:41:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0528 USDT` (34 trades)
  - ALPHA: `+1.6361 USDT` (2 trades)
  - Total: `+1.5833 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_084134.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:18:40Z` → `2026-08-13T08:41:29Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0528 USDT` (34 trades)
  - ALPHA: `+1.6361 USDT` (2 trades)
  - Total: `+1.5833 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_084134.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:18:40Z` → `2026-08-13T08:41:36Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0528 USDT` (34 trades)
  - ALPHA: `+1.6361 USDT` (2 trades)
  - Total: `+1.5833 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_084137.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T07:18:40Z` → `2026-08-13T08:41:36Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0528 USDT` (34 trades)
  - ALPHA: `+1.6361 USDT` (2 trades)
  - Total: `+1.5833 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_084137.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_084459.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T08:45:06Z` → `2026-08-13T12:22:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5060 USDT` (90 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.5060 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_122210.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T08:45:06Z` → `2026-08-13T12:22:08Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5060 USDT` (90 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.5060 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_122210.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_122257.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_BASE_V8_5_IMPACT_4H (auto)

- Profil: `vide_froid_binance` v`2026-07-08-setup-ready`
- Tag: `MASTER_BASE_V8_5_IMPACT_4H`
- Période: `` → ``
- Logs:
  - `MASTER_BASE_V8_5_IMPACT_4H_BETA_X5.csv`
  - `MASTER_BASE_V8_5_IMPACT_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_122613.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_123023.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_123706.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T12:37:12Z` → `2026-08-13T15:45:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0996 USDT` (131 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0996 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_154502.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T12:37:12Z` → `2026-08-13T15:45:00Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0996 USDT` (131 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `-0.0996 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_154502.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_155004.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T15:54:42Z` → `2026-08-13T15:55:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_155520.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T15:54:42Z` → `2026-08-13T15:55:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_155520.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_161624.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T16:16:32Z` → `2026-08-13T16:44:40Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3269 USDT` (21 trades)
  - ALPHA: `+2.3134 USDT` (4 trades)
  - Total: `+1.9866 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_164448.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T16:16:32Z` → `2026-08-13T16:44:40Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.3269 USDT` (21 trades)
  - ALPHA: `+2.3134 USDT` (4 trades)
  - Total: `+1.9866 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_164448.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_164500.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T16:45:07Z` → `2026-08-13T17:16:48Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6350 USDT` (26 trades)
  - ALPHA: `+1.6663 USDT` (14 trades)
  - Total: `+3.3014 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_171657.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T16:45:07Z` → `2026-08-13T17:16:48Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6350 USDT` (26 trades)
  - ALPHA: `+1.6663 USDT` (14 trades)
  - Total: `+3.3014 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_171657.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_171753.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:18:01Z` → `2026-08-13T17:34:13Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0870 USDT` (12 trades)
  - ALPHA: `+3.3333 USDT` (9 trades)
  - Total: `+3.2463 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_173421.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:18:01Z` → `2026-08-13T17:34:13Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.0870 USDT` (12 trades)
  - ALPHA: `+3.3333 USDT` (9 trades)
  - Total: `+3.2463 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_173421.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_173432.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:34:41Z` → `2026-08-13T17:46:31Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1961 USDT` (10 trades)
  - ALPHA: `-6.5615 USDT` (5 trades)
  - Total: `-6.7576 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_174638.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:34:41Z` → `2026-08-13T17:46:31Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1961 USDT` (10 trades)
  - ALPHA: `-6.5615 USDT` (5 trades)
  - Total: `-6.7576 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_174639.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_174651.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:47:00Z` → `2026-08-13T18:12:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4746 USDT` (14 trades)
  - ALPHA: `-12.5039 USDT` (4 trades)
  - Total: `-12.0293 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_181230.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T17:47:00Z` → `2026-08-13T18:12:22Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.4746 USDT` (14 trades)
  - ALPHA: `-12.5039 USDT` (4 trades)
  - Total: `-12.0293 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_181230.md`
- Verdict: `NEGATIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_181241.md`
- Verdict: `NEUTRE`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T18:12:49Z` → `2026-08-13T20:37:07Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5452 USDT` (83 trades)
  - ALPHA: `+0.8266 USDT` (5 trades)
  - Total: `+1.3718 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_203710.md`
- Verdict: `POSITIF`


---

## 2026-08-13 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-13T18:12:49Z` → `2026-08-13T20:37:07Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5452 USDT` (83 trades)
  - ALPHA: `+0.8266 USDT` (5 trades)
  - Total: `+1.3718 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260813_203710.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_074101.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T07:41:10Z` → `2026-08-14T07:56:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1240 USDT` (10 trades)
  - ALPHA: `+2.9474 USDT` (2 trades)
  - Total: `+3.0714 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_075634.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T07:41:10Z` → `2026-08-14T07:56:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1240 USDT` (10 trades)
  - ALPHA: `+2.9474 USDT` (2 trades)
  - Total: `+3.0714 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_075634.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_083126.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T08:31:37Z` → `2026-08-14T08:52:17Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1249 USDT` (19 trades)
  - ALPHA: `+6.6727 USDT` (13 trades)
  - Total: `+6.5478 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_085226.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T08:31:37Z` → `2026-08-14T08:52:17Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `-0.1249 USDT` (19 trades)
  - ALPHA: `+6.6727 USDT` (13 trades)
  - Total: `+6.5478 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_085227.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_085238.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T08:52:47Z` → `2026-08-14T09:29:12Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1764 USDT` (23 trades)
  - ALPHA: `+0.4620 USDT` (3 trades)
  - Total: `+0.6384 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_092920.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T08:52:47Z` → `2026-08-14T09:29:12Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1764 USDT` (23 trades)
  - ALPHA: `+0.4620 USDT` (3 trades)
  - Total: `+0.6384 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_092921.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_092932.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T09:29:42Z` → `2026-08-14T09:31:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0376 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0376 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_093120.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T09:29:42Z` → `2026-08-14T09:31:18Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0376 USDT` (1 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0376 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_093121.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_102448.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_103240.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T10:32:47Z` → `2026-08-14T10:52:20Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5630 USDT` (15 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.5630 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_105222.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T10:32:47Z` → `2026-08-14T10:52:20Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5630 USDT` (15 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.5630 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_105222.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_115709.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T11:57:16Z` → `2026-08-14T12:07:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1379 USDT` (7 trades)
  - ALPHA: `-0.0402 USDT` (2 trades)
  - Total: `+0.0977 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_120728.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T11:57:16Z` → `2026-08-14T12:07:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.1379 USDT` (7 trades)
  - ALPHA: `-0.0402 USDT` (2 trades)
  - Total: `+0.0977 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_120728.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_120739.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:07:46Z` → `2026-08-14T12:17:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0569 USDT` (6 trades)
  - ALPHA: `-8.6278 USDT` (4 trades)
  - Total: `-8.5708 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_121727.md`
- Verdict: `NEGATIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:07:46Z` → `2026-08-14T12:17:19Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0569 USDT` (6 trades)
  - ALPHA: `-8.6278 USDT` (4 trades)
  - Total: `-8.5708 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_121727.md`
- Verdict: `NEGATIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_121739.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:17:45Z` → `2026-08-14T12:40:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0177 USDT` (24 trades)
  - ALPHA: `+3.5478 USDT` (7 trades)
  - Total: `+3.5656 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_124035.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:17:45Z` → `2026-08-14T12:40:26Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0177 USDT` (24 trades)
  - ALPHA: `+3.5478 USDT` (7 trades)
  - Total: `+3.5656 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_124035.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_124046.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_125107.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:51:14Z` → `2026-08-14T15:57:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3956 USDT` (155 trades)
  - ALPHA: `+28.2570 USDT` (65 trades)
  - Total: `+28.6526 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_155705.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T12:51:14Z` → `2026-08-14T15:57:03Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.3956 USDT` (155 trades)
  - ALPHA: `+28.2570 USDT` (65 trades)
  - Total: `+28.6526 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_155706.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_162226.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_162423.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T16:24:30Z` → `2026-08-14T19:35:45Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6846 USDT` (131 trades)
  - ALPHA: `+9.0607 USDT` (26 trades)
  - Total: `+10.7453 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_193548.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T16:24:30Z` → `2026-08-14T19:35:45Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+1.6846 USDT` (131 trades)
  - ALPHA: `+9.0607 USDT` (26 trades)
  - Total: `+10.7453 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_193549.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_193611.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T19:36:21Z` → `2026-08-14T19:53:46Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0033 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0033 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_195348.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T19:36:21Z` → `2026-08-14T19:53:46Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0033 USDT` (4 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0033 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_195349.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_195425.md`
- Verdict: `NEUTRE`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T19:54:34Z` → `2026-08-14T20:24:30Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2811 USDT` (22 trades)
  - ALPHA: `+7.5524 USDT` (11 trades)
  - Total: `+7.8336 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_202433.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T19:54:34Z` → `2026-08-14T20:24:30Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.2811 USDT` (22 trades)
  - ALPHA: `+7.5524 USDT` (11 trades)
  - Total: `+7.8336 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_202433.md`
- Verdict: `POSITIF`


---

## 2026-08-14 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260814_214453.md`
- Verdict: `NEUTRE`


---

## 2026-08-15 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T21:45:03Z` → `2026-08-15T05:44:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.5071 USDT` (205 trades)
  - ALPHA: `+8.6068 USDT` (56 trades)
  - Total: `+11.1140 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260815_054446.md`
- Verdict: `POSITIF`


---

## 2026-08-15 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-14T21:45:03Z` → `2026-08-15T05:44:44Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+2.5071 USDT` (205 trades)
  - ALPHA: `+8.6068 USDT` (56 trades)
  - Total: `+11.1140 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260815_054447.md`
- Verdict: `POSITIF`


---

## 2026-08-15 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `` → ``
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.0000 USDT` (0 trades)
  - ALPHA: `+0.0000 USDT` (0 trades)
  - Total: `+0.0000 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260815_104532.md`
- Verdict: `NEUTRE`


---

## 2026-08-15 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-15T10:45:40Z` → `2026-08-15T12:47:47Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5182 USDT` (66 trades)
  - ALPHA: `-0.3393 USDT` (41 trades)
  - Total: `+0.1789 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260815_124750.md`
- Verdict: `POSITIF`


---

## 2026-08-15 — MASTER_VORTEX_V2_COLLAB_4H (auto)

- Profil: `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt`
- Tag: `MASTER_VORTEX_V2_COLLAB_4H`
- Période: `2026-08-15T10:45:40Z` → `2026-08-15T12:47:47Z`
- Logs:
  - `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Paramètres clé:
  - `BUY_USDT_BETA=200`
  - `BUY_USDT_ALPHA=800`
  - `LLM_GATE_ENABLED=TRUE`
  - `LLM_GATE_FAIL_CLOSED=TRUE`
- Résultat:
  - BETA: `+0.5182 USDT` (66 trades)
  - ALPHA: `-0.3393 USDT` (41 trades)
  - Total: `+0.1789 USDT`
- Rapport: `RAPPORT_PNL_AUTO_20260815_124751.md`
- Verdict: `POSITIF`

