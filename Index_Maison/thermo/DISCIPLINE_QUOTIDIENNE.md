# DISCIPLINE QUOTIDIENNE — 2026-08-27T05:15:07Z

## ALERTES
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice CRITIQUE — voir DERIVE_MEMOIRE.md

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 54.3%
- Analyses notées : 51/94
- Par indice : altSeason 0/1; bassine 3/3; btc 3/7; etfEthM 0/1; etfXrpM 0/1; fearGreed 14/22; funding 9/23; gexPutCall 1/1; liq24Usd 3/3; oi 0/1; onchain 1/1; radar 15/27; verre 2/3

## ADA (zone/voilure vs BTC 24h, v1)
- Zone-accuracy : None% (0/0)
- v1 zone/voilure vs BTC 24h

## MÉMOIRE (dérive, chantier 2)
- derive_memoire.py : santé de la mémoire par indice (I1 fréquence / I2 contradiction / I3 âge / I4 calibration).
- Détail : DERIVE_MEMOIRE.md — instables/critiques à revoir (contexte, données, prompt).

## AGORA (leçons apprises, chantier E4)
- Leçons actives : 4 (TTL 7j, namespace cortana) — chaque HIT/MISS nourrit la base.
- lecons_auto.py : scan → staging → validation (discipline 07h15, APRÈS la note).

## Boucle
- score_justesse.py relancé chaque jour (07:15, launchd) → la note fraîche nourrit la cadence 8h30/20h30.
- En cas d'alerte : corriger (contexte, données, prompt) PUIS re-mesurer — jamais de silence.
