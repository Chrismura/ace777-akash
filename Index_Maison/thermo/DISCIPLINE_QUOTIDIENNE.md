# DISCIPLINE QUOTIDIENNE — 2026-10-10T05:15:27Z

## ALERTES
- 🔴 CORTANA sous 50% (33.0%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 SEUIL NON RANGÉ : 25 clé(s) décident sans être classées (STOP_AMPLITUDE_MULT, RUNNER_CONSERVATION_FRAC, RUNNER_TRAIL_ARM_MULT, RUNNER_GIVEBACK_FRAC, RUNNER_STOP_MULT, GIVEBACK_AMP_COUPLE_FRAC) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 33.0%
- Analyses notées : 126/382
- Par indice : altSeason 1/5; bassine 4/8; btc 3/14; chg24 1/4; croisements 18/55; etfBtcM 2/7; etfEthM 2/7; etfXrpM 2/7; fearGreed 33/83; geopol 8/42; gexPutCall 4/8; indice_onchain 1/7; liq24Usd 3/6; longShort 2/7; oi 0/9; onchain 2/8; pipeline_health 0/3; radar 34/76; rbf 0/3; score 1/7; sdi 2/7; verre 3/9

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 19 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## ERREURS (6ᵉ partie du cycle — post-mortem branché, R15/R17.5)
- Registre : 26 classes d'erreur · non branché : 0 · récidives depuis la correction : 0
- REGISTRE_ECHECS_ET_ERREURS.md : consulté AVANT de proposer une garde (sinon on repaie).

## SEUILS FIXES (R17 — la mesure doit décider)
- 150 clés de config · **29 seuils DÉCIDENT sans mesure** · non classés : 25
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
