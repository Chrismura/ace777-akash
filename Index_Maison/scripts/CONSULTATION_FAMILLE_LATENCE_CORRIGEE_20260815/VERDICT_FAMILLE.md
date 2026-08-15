# VERDICT FAMILLE — Robustesse latence (chiffres CORRIGÉS)

**Date :** 2026-08-15 · **Avis :** 4/4 GO-AVEC-RÉSERVE (gemini 85%, nvidia 78%, juge 70%, ultra 85%)

## Ce qui est validé
1. **Le run vortex du 15/08 était sain** (0 tension_stale, 0 process_die) — l'« endormie » = marché
   férié calme, PAS une panne infra. Ma correction de diagnostic est confirmée.
2. **Le fix heartbeat (revenge permanent) reste valide et fait.**

## Le vrai problème (chemin USINE NUAGE)
La gate `NUAGE_TENSION_MAX_AGE_MS=800ms` FIXE est **trop stricte pour WiFi/alpage** : les 1811
`tension_stale` historiques (1-8% des skips) sont des **faux positifs** — la tension est fraîche,
mais le paquet arrive >800ms → le bot skippe par prudence excessive = occasions manquées
(sûr, mais coûteux en marché calme).

## Le chemin VORTEX
Sa garde `VORTEX_JSON_MAX_AGE_SEC` est probablement suffisante (≥1-5s), mais valeur exacte à
vérifier — un avis demande `info insuffisante` sur ce point.

## Recommandation convergente
1. **Corriger le rapport d'erreurs auto** (tag NUAGE_PROD_4H par défaut → run réel) — sinon on
   répète les fausses conclusions. (nvidia, prioritaire)
2. **Gate ADAPTIVE** sur NUAGE : seuil = `max(800ms, EMA latence × facteur)` + logger
   `feed_latency_ms` (percentiles 50/95/99). = dégradation gracieuse : jouer si latence « dans la
   norme du moment », skipper seulement si dérive anormale.
3. **Vérifier/aligner `VORTEX_JSON_MAX_AGE_SEC`** sur la même logique.
4. **Replay historique** NUAGE avec gate adaptative pour quantifier le gain d'occasions.

## Améliorations (stacking functions)
- Timestamp réseau côté serveur dans `vortex_control.json` (mesurer la VRAIE latence).
- Dashboard latence (tension_stale vs spread_too_wide sur 7 jours).
- Fallback « dernière tension connue × confiance décroissante » au lieu du skip sec.

## Verdict
> **GO-AVEC-RÉSERVE** — ouvrir un chantier « robustesse latence » (gate adaptative + métriques),
> MAIS : 1) corriger d'abord le bug du rapport d'erreurs, 2) ne pas toucher la gate avant d'avoir
> des mesures de latence réelles. Pas d'urgence financière (le skip prudent est sûr).
