ACE777 - Analyse operatoire DUO (session recente)
=================================================

Perimetre cible
---------------
- runs/ALPHA_BOUCLIER_SHORT_7H.csv
- runs/BETA_ECLAIREUR_LONG_7H.csv
- runs/ACE777_SYNCHRO_REEL_7H/DUO1_ALPHA_TEST.csv
- runs/ACE777_SYNCHRO_REEL_7H/DUO1_BETA_TEST.csv

Chiffres cles
-------------
- DUO 7H
  - ALPHA_BOUCLIER_SHORT_7H: pnl_net = -2.52260000 USDT (130 trades)
  - BETA_ECLAIREUR_LONG_7H: pnl_net = +4.21670000 USDT (124 trades)
  - Total DUO 7H: +1.69410000 USDT

- DUO1 TEST
  - DUO1_ALPHA_TEST: pnl_net = +2.51910000 USDT (22 trades)
  - DUO1_BETA_TEST: pnl_net = +3.67380000 USDT (26 trades)
  - Total DUO1: +6.19290000 USDT

Lecture
-------
- Le hedge est positif, mais la jambe ALPHA (short strict) est plus fragile.
- La jambe BETA (long) compense et porte la performance nette.
- Le nombre d'ENTRY_ERROR reste eleve sur certains runs 7H (a surveiller).
- Les EXIT_ERROR (-2022) restent un bruit operationnel recurrent sur certains tests.

Avis
----
- Le systeme est exploitable et rentable sur echantillon recent.
- Priorite technique: reduire les erreurs d'entree/sortie (coherence position mode + controle pre-exit).
- Priorite trading: ajuster ALPHA pour diminuer les pertes en regime de marche contraire.
