# DISCIPLINE QUOTIDIENNE — 2026-09-05T05:15:07Z

## ALERTES
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice CRITIQUE — voir DERIVE_MEMOIRE.md

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 54.8%
- Analyses notées : 57/104
- Par indice : altSeason 0/1; bassine 3/3; btc 3/7; chg24 0/1; etfEthM 0/1; etfXrpM 0/1; fearGreed 21/36; gexPutCall 1/1; indice_onchain 0/1; liq24Usd 3/3; oi 0/1; onchain 1/1; radar 22/43; sdi 1/1; verre 2/3

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
