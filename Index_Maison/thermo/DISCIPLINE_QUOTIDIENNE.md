# DISCIPLINE QUOTIDIENNE — 2026-09-30T06:12:05Z

## ALERTES
- 🔴 CORTANA sous 50% (33.8%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 Tendance à la baisse : 88% → 33.8%

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 33.8% (88% → 33.8% : baisse ≥ 5 pts)
- Analyses notées : 99/293
- Par indice : altSeason 0/4; bassine 3/7; btc 3/12; chg24 1/3; croisements 13/35; etfBtcM 1/4; etfEthM 0/4; etfXrpM 0/4; fearGreed 30/72; geopol 4/30; gexPutCall 2/5; indice_onchain 1/5; liq24Usd 3/6; longShort 1/4; oi 0/6; onchain 2/5; pipeline_health 0/2; radar 30/67; rbf 0/2; score 0/4; sdi 2/5; verre 3/7

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 22 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
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
