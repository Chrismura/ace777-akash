# VERDICT FAMILLE — Bug heartbeat → TTL revenge neutralisé

**Date :** 2026-08-15 · **Avis :** 4/4 GO-AVEC-RÉSERVE (gemini 95%, nvidia 82%, juge 85%, ultra 92%)

## Le bug (confirmé 4/4 + vérifié dans le code)

`duo_touch_heartbeat` (L1545, à chaque cycle SCOUT) rafraîchit `ts_ms`. La décision revenge
(L1027) désarme le revenge si `age = now − ts_ms > 20s` (`stale_state`). Comme `ts_ms` est
rafraîchi en continu, `age` reste ~0 → `stale_state` ne se déclenche JAMAIS → **revenge armé en
permanence** (TTL 20s inopérant). Cause racine du %revenge 58→89% et du PnL ALPHA ultra-volatil.

## Fix recommandé (convergent 4/4)

Conditionner `duo_touch_heartbeat_force` : ne PAS rafraîchir `ts_ms` si le dernier événement
scout est une **perte close** (`status=="CLOSED" && pnl<0`). Effet : `ts_ms` fige à l'instant de
la perte → TTL 20s redevient opérant → revenge auto-désarmé après 20s sans gain scout.

## Vérification croisée (faite par Buffy, pour fermer la réserve nvidia)

- **L1091 `cooldown_revenge`** : utilise `burst_file["last_burst_ms"]` (fichier séparé), **pas** `ts_ms` → ✅ intact.
- **L1094 `boost`** : lit bien `age` (= `ts_ms`) via `age <= boost_ttl_sec*1000` (40s) → ⚠️
  **ultra s'est trompé** en disant que boost ne lit jamais ts_ms. MAIS : le fix est quand même
  sûr, car en figeant ts_ms sur perte, la fenêtre boost (40s) est naturellement plafonnée à la
  fenêtre revenge (20s), ce qui est le comportement voulu (le boost ne s'applique qu'à un revenge
  encore armé). Aucune régression.

## Priorité (légère divergence, arbitrée)

- Le bot est **ARRÊTÉ** → l'urgence « gel revenge immédiat » est caduque.
- Ordre retenu : **1) fix TTL/heartbeat** (le bug structurant, 3/4 priorité 1), **2) infra**
  (E-STALE 1032 + E-PROC 75), **3)** mesurer le %revenge post-fix (<10% attendu en shadow).

## Améliorations (stacking functions)

1. Ajouter `revenge_ttl_expired_count` (métrique de validation du fix).
2. Compteur de revenge consécutif plafonné (max ~3) en ceinture de sécurité.
3. Kill-switch `REVENGE_ENABLED` (env var) pour geler sans redéploiement.
4. Logger `age` + `reason` à chaque décision revenge.

## Verdict

> **GO-AVEC-RÉSERVE** — ouvrir un chantier correctif TTL/heartbeat. Changement du genesis scellé
> = majeur → GO humain + spec/diff exact au codeur + smoke test + re-scellement. Infra (E-STALE/E-PROC)
> traitée ensuite.
