# DISCIPLINE QUOTIDIENNE — 2026-09-21T05:15:15Z

## ALERTES
- 🔴 CORTANA sous 50% (43.1%) — discipline NEUTRE active, à surveiller
- 🔴 DÉRIVE MÉMOIRE : au moins 1 indice INSTABLE — voir DERIVE_MEMOIRE.md

## CORTANA (justesse, 44% = pile-ou-face)
- Score global : 43.1%
- Analyses notées : 87/202
- Par indice : altSeason 0/3; bassine 3/5; btc 3/9; chg24 0/2; croisements 8/17; etfBtcM 1/1; etfEthM 1/3; etfXrpM 1/3; fearGreed 30/60; geopol 4/17; gexPutCall 2/3; indice_onchain 1/3; liq24Usd 3/5; longShort 0/1; oi 0/3; onchain 1/2; pipeline_health 0/1; radar 24/54; rbf 0/1; score 0/1; sdi 2/3; verre 3/5

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
