# DISCIPLINE QUOTIDIENNE — 2026-10-27T10:26:09Z

## ALERTES
- 🔴 CORTANA sous 50% (28.8%) — discipline NEUTRE active, à surveiller
- 🔴 SEUIL NON RANGÉ : 3 clé(s) décident sans être classées (ETANCHE_MISE_MAX, TIERS_P1_PCT, TIERS_P2_PCT) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 28.8%
- Analyses notées : 164/570
- Par indice : altSeason 1/8; bassine 5/11; btc 3/18; chat 4/9; chg24 2/6; croisements 36/98; etfBtcM 2/10; etfEthM 2/12; etfXrpM 2/12; fearGreed 33/107; geopol 9/63; gexPutCall 4/13; indice_onchain 1/12; liq24Usd 4/11; longShort 2/11; oi 0/13; onchain 2/11; panierDownPct 0/1; pipeline_health 2/6; radar 44/94; rbf 1/6; score 0/11; sdi 2/12; verre 3/15

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 23 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## ERREURS (6ᵉ partie du cycle — post-mortem branché, R15/R17.5)
- Registre : 26 classes d'erreur · non branché : 0 · récidives depuis la correction : 0
- REGISTRE_ECHECS_ET_ERREURS.md : consulté AVANT de proposer une garde (sinon on repaie).

## SEUILS FIXES (R17 — la mesure doit décider)
- 172 clés de config · **46 seuils DÉCIDENT sans mesure** · non classés : 3
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
