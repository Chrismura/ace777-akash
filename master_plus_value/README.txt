MASTER PLUS VALUE

Ce sous-dossier est reserve aux configurations/tests avec plus-value validee.

Structure:
- setups/: launchers/scripts retenus
- logs/: logs CSV gagnants de reference

Setups copies:
- setups/MASTER_REFERENCE_9H_HEDGE.sh
- setups/MASTER_LOW_LIQUIDITE_250_4H.sh
- setups/launch_modele_14_v63_30m.sh

Logs copies:
- logs/ALPHA_SNIPER_9H.csv
- logs/BETA_LOURD_RAPIDE_9H.csv
- logs/ACE777_ESCALIER_4H.csv
- logs/TEST_DUO_MINIPATCH_X7_ALPHA_HUNTER_X7.csv
- logs/TEST_DUO_MINIPATCH_X7_BETA_SCOUT_X7.csv

PnL references:
- MASTER nuit (ALPHA_SNIPER_9H + BETA_LOURD_RAPIDE_9H): +5.1755 USDT
- ESCALIER_4H: +10.5191 USDT
- TEST_DUO_MINIPATCH_X7 (ALPHA + BETA): +10.7021 USDT
- MASTER_BASE_V8_5_IMPACT_7H30 (BETA actif): +4.5376 USDT

MODELE 14 (memoire):
- Trade reference detecte dans logs historiques:
  ALPHA_HUNTER.csv -> pnl max unitaire: +14.8008 USDT
- Signature: hunter revenge 1.5x + leverage x10
- Setup associe (avec dernieres mises a jour V6.3):
  setups/launch_modele_14_v63_30m.sh
