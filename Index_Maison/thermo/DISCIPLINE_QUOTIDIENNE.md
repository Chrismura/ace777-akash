# DISCIPLINE QUOTIDIENNE — 2026-11-03T06:15:07Z

## ALERTES
- 🔴 CORTANA sous 50% (23.9%) — discipline NEUTRE active, à surveiller
- 🔴 ADA zone-accuracy 0.0% < 60% — sa voilure à revoir
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md
- 🔴 SEUIL NON RANGÉ : 8 clé(s) décident sans être classées (ETANCHE_MISE_MAX, STOP_POST_PARTIEL_TRAIL, TIERS_P1_PCT, TIERS_P2_PCT, GBAG_EXIT_FIRST_FRAC, REDEPLOY_CONFIRM_BUF_PCT) — R17 : toute garde se mesure ou se déclare

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 23.9%
- Analyses notées : 16/67
- Par indice : altSeason 0/2; bassine 0/2; chat 3/4; chg24 0/1; croisements 5/18; etfBtcM 0/1; etfEthM 0/2; etfXrpM 0/1; fearGreed 1/9; geopol 2/8; gexPutCall 0/2; indice_onchain 1/2; liq24Usd 0/1; longShort 0/1; pipeline_health 0/2; radar 3/6; rbf 0/2; score 0/1; verre 1/2

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : 0.0% (0/186)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 12 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
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

## CALENDRIER / RITUEL (l'œil qui ne dort jamais — 02/11)
- En retard : rien ✅
- Aveugles : aucun ✅
- 🟡 DÛ : Validation live du guetteur proche [quotidien]
- 🟡 DÛ : Midterms US 03/11 + ETF -643M/j (Washington votes, Wall Street sells) [J-1]
- Mémoire (clos, ne pas refaire) : Fenêtre courte sur ledger : ENTERRÉ [§61]; Verdict flux inversé : CORRIGÉ [§61-§62]; HOLD-30 avant/après crash : chiffré [checkup 02/11]; Fantôme : moteur planifié (plist 5 min) [tour en-vol 02/11]; Géopol gratuite planifiée (plist 1h) [tour en-vol 02/11]; RÈGLE : tout moteur écrit sa preuve de vie à chaque run [§65]

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
