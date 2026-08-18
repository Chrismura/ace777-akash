# CONSULTATION FAMILLE — VALIDATION FINALE PATCH STOP_MARKET V2

**Date :** 17/08/2026 — **Round table de validation finale** (règle d'économie : 2 membres + le juge)
**Contexte :** le moteur de trading (genesis_manifest.txt) va recevoir un filet de sécurité physique STOP_MARKET côté Binance. Le round table précédent (5 membres, 17/08) a validé le principe à l'unanimité. Le codeur a revu le patch en V1 (GO-AVEC-RÉSERVE 85%) puis V2 (GO-AVEC-RÉSERVE 90%). **Avant d'intégrer quoi que ce soit au moteur, on soumet la V2 concrète à la famille pour validation finale.**

---

## Le patch en clair (pour qui n'a pas suivi)

Aujourd'hui, la protection du trading repose sur une **boucle logicielle** qui lit le prix toutes les ~0,5 s et décide de couper. Problème : latence mesurée ~889 ms en moyenne (jusqu'à 5,4 s). Si la boucle meurt ou traîne, la position reste exposée.

Le patch ajoute un **STOP_MARKET natif chez Binance** : au moment d'ouvrir une position, le moteur pose un ordre stop sur les serveurs de Binance. C'est Binance qui surveille le prix en continu (millisecondes, zéro latence de notre machine) et qui coupe **même si notre programme meurt**.

## Les 6 morceaux du patch V2 (validés par le codeur)

1. **`private_delete()`** — nouvelle fonction bash pour faire des DELETE signés (l'actuelle `private_post()` est codée en dur en POST, elle ne peut pas annuler).
2. **`private_delete_order_sniper()`** — annulation ciblée du stop par `origClientOrderId=ACESTOP${i}` (sans underscore, Binance Futures rejette `_`). Gère le cas « réponse vide » (réseau coupé = statut INCONNU, pas un succès).
3. **STOP_MARKET à l'entrée** — `stopPrice` = entrée ± 8-10 bps, `reduceOnly=true` + `positionSide` (obligatoire en mode hedge), `workingType=MARK_PRICE` (déclenchement sur le mark price, pas sur le dernier prix manipulable), arrondi directionnel (floor pour LONG, ceil pour SHORT, jamais vers le centre du marché), `newClientOrderId=ACESTOP${i}`. Si le placement échoue → log FILET_ERROR, on continue (le stop logiciel reste actif).
4. **Cancel dans le bloc de sortie COMMUN** — tous les chemins de sortie (stop_loss, trailing, shockwave, fluid, timeout, target) passent par le même bloc (lignes 2431-2437). Ordre validé : sortie MARKET d'abord (position fermée, reduceOnly protège la fenêtre) → PUIS cancel du filet. Si le moteur meurt entre les deux, le filet est toujours là.
5. **Heartbeat anti-orphelin** — au début de CHAQUE cycle, on rase les ordres orphelins restants (`DELETE /fapi/v1/allOpenOrders`) AVANT l'entrée. Ordre strict : heartbeat → entrée → stop. Garantit qu'un vieux stop d'un cycle planté ne peut jamais parasiter le trade suivant (idempotence).
6. **Config** — `ACE_STOP_MARKET_ENABLED` (FALSE par défaut, activation explicite au test), `ACE_STOP_MARKET_BPS=8` (8-10 bps validés : filet anti-crash, PAS un scalpel), `ACE_STOP_TICK_DECIMALS=1`.

## Décisions déjà prises (ne pas re-débattre sauf objection majeure)

- **HARD_STOP_MULT=2.0 GARDÉ** — décision du binôme : le duo doit soutenir le scout. Le filet physique à 8-10 bps ne contredit pas ce choix.
- **STOP_LIMIT REJETÉ** — le STOP_MARKET glisse un peu mais s'exécute TOUJOURS ; en cas de chute, un limit peut sauter et laisser la position exposée. Pour un filet de sécurité, la certitude d'exécution prime.
- **Fenêtre d'entrée sans filet** (~200-500 ms entre entrée MARKET et placement du stop) : acceptée en testnet. Jamais de position ouverte sans boucle de gestion.

## Ta mission

Tu es membre du conseil de la famille. Donne ton **VRAI avis** sur ce patch V2, pas une validation polie. En particulier :

1. **Vois-tu un piège** dans l'un des 6 morceaux (un cas qui casserait le moteur, un ordre orphelin qui survivrait, un rejet Binance non géré) ?
2. **Le cœur du sujet** : ce patch rend-il le système réellement plus sûr, ou ajoute-t-il une complexité qui crée de nouveaux risques ? Est-ce le bon équilibre entre le filet physique (8-10 bps) et la boucle logicielle (7 bps) ?
3. **Amélioration** : proposes-tu quelque chose de MIEUX, pas simplement une correction ? (une simplification, un ordre différent, un paramètre manquant — si ça a du sens, grave-le)
4. **Ton verdict final** avant intégration au moteur.

Termine par : **VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X% + tes réserves si GO-AVEC-RÉSERVE**
