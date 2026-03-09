ACE777 - TEST_MASTER
====================

Objectif
--------
Centraliser tous les tests avant validation dans la base MASTER.

Organisation
------------
- inbox_runs/
  - Deposer ici les CSV bruts d'un test en cours (avant tri).
- candidats/
  - Scripts/profils candidats a valider (avant promotion en MASTER).
  - DUO_1_TEST.sh (hedge test 4h, horodate UTC en live)
- reports/
  - Rapports PnL et observations par session de test.

Regle simple
------------
1) Tester dans TEST_MASTER.
2) Mesurer le PnL et la stabilite.
3) Promouvoir dans VALIDATION_ACE777_BASE uniquement si valide.

Commande unique (fin de run)
----------------------------
Exemple:

  bash ./VALIDATION_ACE777_BASE/TEST_MASTER/finalize_test.sh \
    /app/runs/ACE777_SYNCHRO_REEL_7H/ACE777_ESCALIER_4H.csv

Cette commande:
- copie le CSV dans inbox_runs/ (snapshot timestamped),
- genere un rapport PnL dans reports/.
- ajoute automatiquement debut, fin et duree du test.

Lancement DUO 1 test
--------------------

  bash ./VALIDATION_ACE777_BASE/TEST_MASTER/candidats/DUO_1_TEST.sh

Sorties:
- runs/ACE777_SYNCHRO_REEL_7H/DUO1_ALPHA_TEST.csv
- runs/ACE777_SYNCHRO_REEL_7H/DUO1_BETA_TEST.csv
