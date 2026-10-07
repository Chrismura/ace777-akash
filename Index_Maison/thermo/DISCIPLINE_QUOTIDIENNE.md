# DISCIPLINE QUOTIDIENNE — 2026-10-07T07:34:31Z

## ALERTES
- 🔴 CORTANA sous 50% (33.0%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 SEUIL NON RANGÉ : 5 clé(s) décident sans être classées (STOP_AMPLITUDE_MULT, RUNNER_CONSERVATION_FRAC, RUNNER_TRAIL_ARM_MULT, RUNNER_GIVEBACK_FRAC, RUNNER_STOP_MULT) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 33.0%
- Analyses notées : 117/355
- Par indice : altSeason 1/5; bassine 4/8; btc 3/14; chg24 1/4; croisements 15/46; etfBtcM 1/6; etfEthM 2/6; etfXrpM 2/6; fearGreed 32/80; geopol 7/39; gexPutCall 4/7; indice_onchain 1/6; liq24Usd 3/6; longShort 1/6; oi 0/8; onchain 2/7; pipeline_health 0/3; radar 33/75; rbf 0/3; score 0/6; sdi 2/6; verre 3/8

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
- 128 clés de config · **29 seuils DÉCIDENT sans mesure** · non classés : 5
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
