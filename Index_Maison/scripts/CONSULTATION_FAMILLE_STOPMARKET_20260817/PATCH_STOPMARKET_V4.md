# PATCH STOP_MARKET V4 — Migration Algo Order API Binance

**Date :** 17/08/2026 — **V4** (correction découverte en TEST RÉEL : Binance a migré les ordres conditionnels)
**Cible :** `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.SETUP_D_stopmarket_20260817` (md5 `5a0a6797`)
**Validations :** famille V2 (GO-AVEC-RÉSERVE 3/3) · codeur V2 (GO 90%) · **tests réels testnet 17/08 (ci-dessous)**

---

## 🔴 Pourquoi une V4 ? La vérité découverte en test réel

Le premier test réel (setup D V3) a révélé que **Binance a migré les ordres conditionnels vers la nouvelle Algo Order API** (décembre 2025) :

- Ancien endpoint `POST /fapi/v1/order` avec `STOP_MARKET` → **refusé** `-4120 "Order type not supported for this endpoint. Please use the Algo Order API endpoints instead."`
- Le paramètre `reduceOnly` → **interdit en mode Hedge** `-1106 "Parameter 'reduceonly' sent when not required."`

## ✅ Tests réels concluants (testnet, 17/08, ordres fantômes annulés)

| Test | Résultat |
|---|---|
| **A1** : `algoType=CONDITIONAL` + `triggerPrice` + `positionSide=LONG` + `quantity` (SANS reduceOnly) | ✅ **ACCEPTÉ** — Binance applique `reduceOnly:true` automatiquement (`"reduceOnly":true` dans la réponse) |
| A2 : `closePosition=true` | ❌ `-4509` — exige une position ouverte au moment du placement (inadapté) |
| A3 : sans `positionSide` | ❌ `-4061` — compte en mode hedge, `positionSide` obligatoire |
| **Annulation** : `DELETE /fapi/v1/algoOrder?clientAlgoId=` | ✅ **`code=200 success`** |

**La clé** : en mode hedge, Binance applique `reduceOnly` automatiquement quand `positionSide` est envoyé — le filet anti-short-surprise est **intégré par Binance lui-même**.

## Δ V3 → V4 (les changements)

| Paramètre | V3 (obsolète) | V4 (Algo Order API) |
|---|---|---|
| Endpoint placement | `POST /fapi/v1/order` | **`POST /fapi/v1/algoOrder`** |
| Préfixe requis | — | **`algoType=CONDITIONAL`** |
| Prix déclencheur | `stopPrice` | **`triggerPrice`** |
| ID client | `newClientOrderId` | **`clientAlgoId`** |
| `reduceOnly=true` | envoyé | **SUPPRIMÉ** (interdit en hedge ; automatique via positionSide) |
| Endpoint annulation | `DELETE /fapi/v1/order?origClientOrderId=` | **`DELETE /fapi/v1/algoOrder?clientAlgoId=`** |

## Les morceaux modifiés (2 seulement — le reste du V3 est inchangé)

### Morceau 2 (modifié) : `private_delete_order_sniper()` — annulation Algo Order API

```bash
private_delete_order_sniper() {
  local symbol="$1" cycle_id="$2"
  local client_order_id="ACESTOP${cycle_id}"
  local query_params="clientAlgoId=${client_order_id}"
  echo "🧹 [NETTOYAGE] Suppression du STOP_MARKET physique : ${client_order_id}"
  local response
  response="$(private_delete "/fapi/v1/algoOrder" "$query_params" || true)"
  if [ -z "$response" ]; then
    echo "⚠️ [NETTOYAGE] Réponse vide (réseau ?) — statut du filet INCONNU, à vérifier manuellement."
  elif echo "$response" | grep -q '"code":'; then
    echo "⚠️ [NETTOYAGE] Ordre déjà exécuté par Binance ou introuvable. On passe en douceur."
  else
    echo "✅ [NETTOYAGE] Filet physique annulé proprement."
  fi
}
```

### Morceau 3 (modifié) : placement STOP_MARKET — Algo Order API

```bash
    ts="$(now_ms)"
    # V4 : Algo Order API — triggerPrice au lieu de stopPrice, clientAlgoId au lieu de newClientOrderId,
    # PAS de reduceOnly (interdit en hedge ; Binance l'applique automatiquement avec positionSide)
    q_stop="algoType=CONDITIONAL&symbol=$SYMBOL&side=$close_side&type=STOP_MARKET&quantity=$qty&triggerPrice=$stop_price&workingType=MARK_PRICE${stop_position_side_param}&clientAlgoId=ACESTOP${i}&timestamp=$ts&recvWindow=$RECV_WINDOW"
    stop_resp="$(private_post "/fapi/v1/algoOrder" "$q_stop" || true)"
```

**Le reste du V3 est inchangé** : heartbeat ciblé ACESTOP (morceau 5), cancel dans le bloc de sortie commun (morceau 4), cancel phase_shift (4bis), config `ACE_STOP_MARKET_ENABLED=FALSE` par défaut (morceau 6), arrondi directionnel floor/ceil.

## Réversibilité (inchangée)

| Mécanisme | Action |
|---|---|
| **Bascule instantanée** | `bash scripts/basculer_setup.sh A` → retour setup actuel, backup auto |
| **Runtime** | `ACE_STOP_MARKET_ENABLED=FALSE` → filet désactivé sans toucher au code |
| **Profondeur** | BAK horodaté + git auto-sync |

## Conditions JUGE (rappel)

1. ✅ **Signature DELETE validée** (test 17/08 : `-2011` sur ordre inexistant = HMAC OK, puis `code=200` sur annulation réelle)
2. `ACE_STOP_MARKET_ENABLED=FALSE` jusqu'au redémarrage propre — **respectée : le run en cours tourne en V3, la V4 attend le prochain lancement**
