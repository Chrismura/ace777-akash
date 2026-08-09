# ⚡ BLACKLIST "MORT DU JOUR" — fin du timeout visible — 2026-08-09

## Problème (reproche Christophe 13:00Z)
Le fix PATIENCE évitait les échecs mais pas l'attente : OpenRouter Juge (quota :free épuisé) faisait ~1 min de PATIENCE à chaque appel avant bascule → Christophe voyait « timeout » dans les logs et croyait que rien n'était réglé. 41 timeouts journalisés (27 Juge, 9 Ultra, 2 autres, 2 Qwen locale, 1 NVIDIA).

## Solution implémentée
**Blacklist « mort du jour »** dans `hub_prise_ia.py` :
- Un fournisseur qui **échoue 2 fois de suite** (timeout PATIENCE / quota) est exclu du routage pour le **reste de la journée** → bascule immédiate, **0 attente, 0 timeout visible**.
- La blacklist **expire automatiquement** au changement de jour (UTC).
- **Filet de sécurité** : si TOUS les providers sont blacklistés (panne générale), tentative de dernier recours sans blacklist → jamais de plantage silencieux.

## Processus (loi 1quinquies + 1quater — RESPECTÉ cette fois)
```
Ada SPECIFIE → GEMINI écrit (via hub) → Ada checker + tests unitaires
→ AUDIT TIERS (Gemini famille différente) = OK AVEC RÉSERVES
→ Réserves APPLIQUÉES : filet de sécurité, thread-safety (lock), UTC
→ Compile + 5 tests unitaires passent → hub redémarré, santé OK (9 providers)
```

## Preuves
- Backup : `hub_prise_ia.py.bak-blacklist` (13 Ko)
- Patch spec : `blacklist_patch.py` (écrit par Gemini, 2634 chars)
- Tests unitaires : 5/5 passent (2 échecs→blacklist, expiration jour, reset succès, filet, UTC)
- Hub : `{"status":"ok","providers":9}` après redémarrage
- `log_event("blacklist", ...)` : nouvel événement traçable dans hub_events.jsonl

## Vérification par Christophe
1. `tail -20 ~/prise-ia/hub_events.jsonl` → chercher `kind: blacklist`
2. Plus aucun `timeout` pour les providers morts dans les prochains appels (la bascule est directe)
