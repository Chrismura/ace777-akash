ACE777 - Analyse session tests
==============================

Perimetre analyse
-----------------
- ACE777_ESCALIER_4H.csv
- BETA_LOURD_4H.csv
- DUO1_ALPHA_TEST.csv
- DUO1_BETA_TEST.csv

Resultats PnL
-------------
- ACE777_ESCALIER_4H.csv
  - trades=113 | wins=63 | losses=50
  - pnl_net=+10.51910000 USDT
  - profit_factor=1.5131
  - exit_errors=0 | entry_errors=0

- BETA_LOURD_4H.csv (run coupe tot)
  - trades=3 | wins=2 | losses=1
  - pnl_net=-0.03780000 USDT
  - profit_factor=0.9380
  - exit_errors=0 | entry_errors=0

- DUO1_ALPHA_TEST.csv
  - trades=22 | wins=13 | losses=9
  - pnl_net=+2.51910000 USDT
  - profit_factor=1.7420
  - exit_errors=20 | entry_errors=0

- DUO1_BETA_TEST.csv
  - trades=26 | wins=19 | losses=7
  - pnl_net=+3.67380000 USDT
  - profit_factor=2.1737
  - exit_errors=17 | entry_errors=0

- DUO1 total (ALPHA+BETA)
  - trades=48 | wins=32 | losses=16
  - pnl_net=+6.19290000 USDT
  - profit_factor=1.9491
  - exit_errors=37

Durees observees
----------------
- ACE777_ESCALIER_4H.csv
  - start=2026-02-28T17:21:17Z
  - end=2026-03-01T08:51:28Z
  - duree=15h30m11s

- BETA_LOURD_4H.csv
  - start=2026-03-01T09:39:05Z
  - end=2026-03-01T09:42:53Z
  - duree=0h3m48s

- DUO1_ALPHA_TEST.csv
  - start=2026-03-01T09:46:52Z
  - end=2026-03-01T11:35:48Z
  - duree=1h48m56s

- DUO1_BETA_TEST.csv
  - start=2026-03-01T09:44:39Z
  - end=2026-03-01T11:35:47Z
  - duree=1h51m8s

Lecture et avis
---------------
- Point fort: la logique filtre/radar reste rentable en session test.
- Point fort: DUO1 est positif et assez solide sur cet echantillon.
- Point faible: trop d'erreurs EXIT (-2022), ce qui pollue l'execution et la lecture.
- Point de vigilance: la session a ete interrompue manuellement, donc la stat est partielle.
- Point technique: le script BASE a ete revalide (`bash -n` OK) apres le message de syntax error.

Recommandations
---------------
1) Priorite: patch anti -2022 (verif position ouverte avant reduceOnly).
2) Continuer DUO1 en session complete (4h pleine) pour confirmer la stabilite.
3) Valider un seuil de promotion MASTER:
   - pnl_net > 0
   - profit_factor > 1.20
   - exit_errors reduits de maniere nette.
