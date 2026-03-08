ACE777 - Base validee (snapshot)
================================

Objectif
--------
Ce dossier regroupe une base claire des elements valides pour eviter le melange
entre essais, archives et runs actifs.

Structure
---------
- scripts/
  - ACE777_STRICT_CLONE_FUTURES.sh
  - ACE777_STRICT_CLONE_FUTURES_V2.sh
- launchers/
  - SOUVERAIN_START_ELITE_STYLE.sh
- runs_reference/
  - ALPHA_SNIPER_9H.csv
  - BETA_LOURD_RAPIDE_9H.csv
  - ACE777_V2_STABLE_1H.csv
  - ACE777_SYNCHRO_REEL_7H_NUIT_ROOT.csv
  - ACE777_SYNCHRO_REEL_7H_NUIT_RUNS.csv
- master_reference/
  - MASTER_REFERENCE_9H_HEDGE.sh
  - MASTER_LOW_LIQUIDITE_250_4H.sh
- TEST_MASTER/
  - README_TEST_MASTER.md
  - inbox_runs/
  - candidats/
  - reports/PNL_LATEST_MASTER.txt

Notes importantes
-----------------
- C'est une copie de reference (snapshot), pas la source vivante.
- Les scripts vivants restent dans la racine du projet.
- Les nouveaux runs doivent continuer a aller dans:
  runs/ACE777_SYNCHRO_REEL_7H/
- Tous les scripts MASTER de cette base utilisent la version BASE timestamped
  (heure UTC en debut de chaque ligne live).

Validation hedge (reference)
----------------------------
- ALPHA_SNIPER_9H.csv: pnl_net +3.15950000 USDT
- BETA_LOURD_RAPIDE_9H.csv: pnl_net +2.01600000 USDT
- Total hedge: +5.17550000 USDT

Note strategie validee (low liquidite)
--------------------------------------
- Profil: BUY_USDT=250
- Usage: marche en range / liquidite faible
- Intention: viser des gains progressifs avec risque contenu

Reference nuit 7H (validee)
---------------------------
- Snapshot principal copie: ACE777_SYNCHRO_REEL_7H_NUIT_ROOT.csv
- Snapshot runs copie: ACE777_SYNCHRO_REEL_7H_NUIT_RUNS.csv

