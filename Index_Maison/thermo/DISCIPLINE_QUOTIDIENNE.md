# DISCIPLINE QUOTIDIENNE — 2026-10-11T08:26:01Z

## ALERTES
- 🔴 CORTANA sous 50% (34.3%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 SEUIL NON RANGÉ : 30 clé(s) décident sans être classées (STOP_AMPLITUDE_MULT, RUNNER_CONSERVATION_FRAC, RUNNER_TRAIL_ARM_MULT, RUNNER_GIVEBACK_FRAC, RUNNER_STOP_MULT, GIVEBACK_AMP_COUPLE_FRAC) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 34.3%
- Analyses notées : 137/399
- Par indice : altSeason 1/5; bassine 4/8; btc 4/15; chg24 1/4; croisements 22/60; etfBtcM 1/7; etfEthM 2/7; etfXrpM 2/7; fearGreed 34/85; geopol 9/44; gexPutCall 4/8; indice_onchain 2/8; liq24Usd 3/6; longShort 1/7; oi 1/10; onchain 3/9; pipeline_health 0/3; radar 36/78; rbf 0/3; score 0/7; sdi 3/8; verre 4/10

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
- 157 clés de config · **29 seuils DÉCIDENT sans mesure** · non classés : 30
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
