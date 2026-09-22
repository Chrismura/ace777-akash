# DISCIPLINE QUOTIDIENNE — 2026-09-22T05:15:14Z

## ALERTES
- 🔴 CORTANA sous 50% (40.1%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 40.1%
- Analyses notées : 87/217
- Par indice : altSeason 0/3; bassine 3/5; btc 3/9; chg24 1/3; croisements 10/20; etfBtcM 1/2; etfEthM 0/3; etfXrpM 0/3; fearGreed 30/62; geopol 3/19; gexPutCall 1/3; indice_onchain 1/3; liq24Usd 3/5; longShort 0/2; oi 0/3; onchain 1/2; pipeline_health 0/2; radar 25/56; rbf 0/2; score 0/2; sdi 2/3; verre 3/5

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 11 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
