# ⚖️ VERDICT FAMILLE — PATCH STOP_MARKET V2 (validation finale)

**Date :** 17/08/2026 — Règle d'économie : 2 membres + le juge (plus jamais 6)
**Consultés :** gemini (78%) · groq (88%) · **JUGE (92% — décision finale)**

---

## 🎯 DÉCISION FINALE : GO-AVEC-RÉSERVE (unanime 3/3)

Le patch V2 est **validé pour intégration**, avec des réserves. **Aucun membre ne bloque.** Le juge tranche à 92%.

## Ce que la famille valide sans réserve

- Le **principe du filet physique** chez Binance : « laisser la sécurité aux mains de l'exchange est une nécessité vitale vu la latence (889 ms, pic 5,4 s) » — c'est le standard minimal d'un bot sérieux.
- `workingType=MARK_PRICE` : « critique et salvatrice » (évite les déclenchements sur mèches du last price).
- L'arrondi directionnel floor/ceil : « mathématiquement propre ».
- L'ordre sortie → puis cancel : « la bonne séquence ».
- `ACE_STOP_MARKET_ENABLED=FALSE` par défaut : « excellente sage précaution ».

## ⚠️ Le point commun des 3 avis : le heartbeat `allOpenOrders`

**Les 3 membres convergent sur le même point de vigilance** : le morceau 5 rase TOUS les ordres ouverts au début de chaque cycle. Aujourd'hui c'est sûr (seuls les ACESTOP dorment), mais :
- c'est une « méthode de bûcheron » qui pourrait tuer un ordre légitime si l'architecture évolue (autre stratégie, multi-jambes) ;
- ça consomme du rate-limit API (risque d'erreurs 429).

**La recommandation famille** : préférer un **DELETE ciblé par clientOrderId ACESTOP** plutôt que le rasage aveugle — sauf si les erreurs 429 apparaissent en test.

## 📌 Les 2 conditions du JUGE (exigées, pas suggérées)

1. **Valider la signature `private_delete()` sur un ordre factice en testnet AVANT toute activation** — les DELETE de l'API Futures Binance sont piégeux (HMAC-SHA256). Premier micro-test obligatoire.
2. **Garder `ACE_STOP_MARKET_ENABLED=FALSE` jusqu'au redémarrage propre du cycle d'intégration** — l'activation ne se fait jamais à l'aveugle.

## Décision binôme (Buffy + utilisateur) — à entériner

| Point | Décision famille | À valider par le binôme |
|---|---|---|
| Patch V2 global | ✅ GO-AVEC-RÉSERVE | à entériner |
| Heartbeat `allOpenOrders` | ⚠️ à remplacer par cancel ciblé ACESTOP si possible | **décision à prendre** |
| Condition juge n°1 (test signature DELETE) | obligatoire | à planifier au test |
| Condition juge n°2 (ENABLED=FALSE jusqu'à redémarrage propre) | obligatoire | à respecter |

**Statut : rien n'est intégré au moteur. Le patch V2 est prêt, la famille a donné son feu vert conditionnel.**
