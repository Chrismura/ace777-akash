# DISCIPLINE QUOTIDIENNE — 2026-10-29T23:42:55Z

## ALERTES
- 🔴 CORTANA sous 50% (4.8%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 SEUIL NON RANGÉ : 8 clé(s) décident sans être classées (ETANCHE_MISE_MAX, STOP_POST_PARTIEL_TRAIL, TIERS_P1_PCT, TIERS_P2_PCT, GBAG_EXIT_FIRST_FRAC, REDEPLOY_CONFIRM_BUF_PCT) — R17 : toute garde se mesure ou se déclare
- 🔴 Tendance à la baisse : 11% → 4.8%

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 4.8% (11% → 4.8% : baisse ≥ 5 pts)
- Analyses notées : 1/21
- Par indice : altSeason 0/1; bassine 0/1; chat 0/1; croisements 0/5; etfEthM 0/1; etfXrpM 0/1; fearGreed 0/3; geopol 0/3; gexPutCall 0/1; indice_onchain 0/1; radar 1/2; verre 0/1

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 20 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
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
