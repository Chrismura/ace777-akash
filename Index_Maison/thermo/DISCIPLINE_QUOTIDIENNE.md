# DISCIPLINE QUOTIDIENNE — 2026-09-25T05:15:18Z

## ALERTES
- 🔴 CORTANA sous 50% (39.8%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 39.8%
- Analyses notées : 99/249
- Par indice : altSeason 0/3; bassine 3/6; btc 3/10; chg24 1/3; croisements 14/27; etfBtcM 1/3; etfEthM 0/3; etfXrpM 0/3; fearGreed 31/66; geopol 5/24; gexPutCall 2/4; indice_onchain 1/4; liq24Usd 3/5; longShort 1/3; oi 0/4; onchain 1/3; pipeline_health 0/2; radar 28/61; rbf 0/2; score 0/3; sdi 2/4; verre 3/6

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 10 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## ERREURS (6ᵉ partie du cycle — post-mortem branché, R15/R17.5)
- Registre : 25 classes d'erreur · non branché : 0 · récidives depuis la correction : 0
- REGISTRE_ECHECS_ET_ERREURS.md : consulté AVANT de proposer une garde (sinon on repaie).

## SEUILS FIXES (R17 — la mesure doit décider)
- 121 clés de config · **29 seuils DÉCIDENT sans mesure** · non classés : 0
- SEUILS_FIXES_DERNIER.md : la liste chiffrée des seuils à passer à la mesure.

## SORTIE PILOTÉE PAR LA MESURE (GO 3 — suivi en vol)
- Règle armée : **OUI** (référence 7.3 %/jour)
- Sorties par palier au format MESURÉ : 0 (anomalies 0) · avant câblage : 32
- EN ATTENTE — la règle est armée, aucune sortie par palier depuis le câblage

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
