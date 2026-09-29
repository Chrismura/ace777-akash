# DISCIPLINE QUOTIDIENNE — 2026-09-29T05:15:09Z

## ALERTES
- ✅ Rien à signaler

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 88.7%
- Analyses notées : 196/221
- Par indice : altSeason 3/4; bassine 7/7; btc 7/11; chg24 1/1; croisements 18/18; etfBtcM 2/2; etfEthM 3/4; etfXrpM 3/4; fearGreed 39/46; geopol 26/26; gexPutCall 5/5; indice_onchain 4/4; liq24Usd 6/6; longShort 3/3; oi 5/6; onchain 4/4; pipeline_health 2/2; radar 43/52; rbf 2/2; score 4/4; sdi 3/3; verre 6/7

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
- Registre : 25 classes d'erreur · non branché : 0 · récidives depuis la correction : 0
- REGISTRE_ECHECS_ET_ERREURS.md : consulté AVANT de proposer une garde (sinon on repaie).

## SEUILS FIXES (R17 — la mesure doit décider)
- 121 clés de config · **29 seuils DÉCIDENT sans mesure** · non classés : 0
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 1 (anomalies 0) · avant câblage : 32
- 1 sortie(s) par palier depuis le câblage — toutes conformes

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
