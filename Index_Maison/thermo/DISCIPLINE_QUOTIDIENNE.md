# DISCIPLINE QUOTIDIENNE — 2026-10-31T06:15:02Z

## ALERTES
- 🔴 CORTANA sous 50% (12.9%) — discipline NEUTRE active, à surveiller
- 🔴 SEUIL NON RANGÉ : 8 clé(s) décident sans être classées (ETANCHE_MISE_MAX, STOP_POST_PARTIEL_TRAIL, TIERS_P1_PCT, TIERS_P2_PCT, GBAG_EXIT_FIRST_FRAC, REDEPLOY_CONFIRM_BUF_PCT) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 12.9%
- Analyses notées : 4/31
- Par indice : altSeason 0/1; bassine 0/1; chat 3/4; croisements 0/7; etfEthM 0/1; etfXrpM 0/1; fearGreed 0/4; geopol 0/4; gexPutCall 0/1; indice_onchain 0/1; pipeline_health 0/1; radar 1/3; rbf 0/1; verre 0/1

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 16 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## ERREURS (6ᵉ partie du cycle — post-mortem branché, R15/R17.5)
- Registre : 30 classes d'erreur · non branché : 0 · récidives depuis la correction : 0
- REGISTRE_ECHECS_ET_ERREURS.md : consulté AVANT de proposer une garde (sinon on repaie).

## SEUILS FIXES (R17 — la mesure doit décider)
- 183 clés de config · **46 seuils DÉCIDENT sans mesure** · non classés : 8
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
