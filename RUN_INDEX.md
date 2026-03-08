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
