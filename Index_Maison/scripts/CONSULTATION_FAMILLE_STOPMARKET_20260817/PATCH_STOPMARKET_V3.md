# PATCH STOP_MARKET V3 — Filet de sécurité physique Binance (cancel ciblé)

**Date :** 17/08/2026 — **V3** (décision binôme : cancel ciblé direct, PAS la méthode bûcheron)
**Cible :** `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` (setup A, md5 `fe2a7bcc…`) → **nouveau setup D**
**Validations :** famille V2 (GO-AVEC-RÉSERVE 3/3, juge 92%) · conditions juge : test signature DELETE avant activation + ENABLED=FALSE jusqu'à redémarrage propre
**Règle :** réversibilité totale — le patch vit dans le **setup D**, `basculer_setup.sh A` revient à l'identique en 1 commande.

---

## Δ V2 → V3 (décision binôme 17/08)

**Le heartbeat (morceau 5) passe du rasage global `allOpenOrders` au CANCEL CIBLÉ direct :**

- ❌ AVANT (V2) : `DELETE /fapi/v1/allOpenOrders` au début de chaque cycle = « méthode du bûcheron » (rase tout, risque de tuer un ordre légitime, surconsomme le rate-limit, 3 réserves famille).
- ✅ MAINTENANT (V3) : `private_delete_order_sniper "$SYMBOL" "$i"` au début de chaque cycle = annule **uniquement** `ACESTOP${i}` (l'éventuel stop orphelin du cycle précédent). Zéro effet de bord, zéro collision, même fonction que le nettoyage de sortie — **une seule mécanique anti-orphelin partout**.

L'idempotence est préservée : si un cycle planté a laissé `ACESTOP157` vivant, le cycle suivant l'annule **avant** d'en poser un nouveau (ordre strict : heartbeat → entrée → stop).

---

## Les 6 morceaux du patch (V3, ancrés sur le vrai moteur)

### 1. Nouvelle fonction `private_delete()` (après `private_post()`, ligne ~738)

```bash
# ============================================================
# DELETE signé (annulation d'ordres) — patch STOP_MARKET V3
# ============================================================
private_delete() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl_with_retry -X DELETE -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BASE_URL$path?$q&signature=$sig"
}
```

⚠️ **Condition juge n°1** : valider la signature HMAC de ce DELETE sur un ordre factice en testnet AVANT toute activation.

### 2. Routine anti-orphelin `private_delete_order_sniper()` (après `private_delete()`)

```bash
# ============================================================
# Nettoyage chirurgical du filet physique (anti-orphelin)
# ============================================================
private_delete_order_sniper() {
  local symbol="$1" cycle_id="$2"
  local client_order_id="ACESTOP${cycle_id}"
  local query_params="symbol=${symbol}&origClientOrderId=${client_order_id}"
  echo "🧹 [NETTOYAGE] Suppression du STOP_MARKET physique : ${client_order_id}"
  local response
  response="$(private_delete "/fapi/v1/order" "$query_params" || true)"
  if [ -z "$response" ]; then
    # Réponse vide = réseau coupé ou timeout : statut INCONNU, on alerte
    echo "⚠️ [NETTOYAGE] Réponse vide (réseau ?) — statut du filet INCONNU, à vérifier manuellement."
  elif echo "$response" | grep -q '"code":'; then
    # Binance renvoie une erreur si l'ordre est déjà exécuté ou inexistant : passage en douceur
    echo "⚠️ [NETTOYAGE] Ordre déjà exécuté par Binance ou introuvable. On passe en douceur."
  else
    echo "✅ [NETTOYAGE] Filet physique annulé proprement."
  fi
}
```

### 3. Placement du STOP_MARKET à l'entrée (après `entry_ts_iso=...`, ligne ~2127)

Point d'ancrage : entre `entry_ts_iso="$(date -u +%FT%TZ)"` et `reason="timeout"`. On a `$entry_price`, `$qty`, `$side`, `$close_side`, `$SYMBOL` à disposition.

```bash
  entry_ts_iso="$(date -u +%FT%TZ)"

  # ============================================================
  # FILET PHYSIQUE : STOP_MARKET posé chez Binance (patch 17/08 V3)
  # stopPrice = entrée ± stop_bps, arrondi directionnel au tickSize
  # ============================================================
  if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
    # positionSide en mode hedge — dérivé du sens du trade (même logique que l'entrée)
    stop_position_side_param=""
    if [ -n "$trade_position_side_param" ] || [ "$POSITION_SIDE" = "BOTH" ]; then
      stop_position_side="LONG"; [ "$side" = "SELL" ] && stop_position_side="SHORT"
      stop_position_side_param="&positionSide=$stop_position_side"
    fi
    if [ "$side" = "BUY" ]; then
      stop_price_raw="$(num_sub "$entry_price" "$(num_div "$(num_mul "$entry_price" "$ACE_STOP_MARKET_BPS")" "10000")")"
      # Arrondi FLOOR pour un LONG : le stop ne monte JAMAIS vers le marché
      stop_price="$(ruby -e 'p=(Float(ARGV[0]) rescue 0.0); d=(Integer(ARGV[1]) rescue 1); d=1 if d < 1; f=10.0**d; printf("%.#{d}f", (p*f).floor/f)' -- "$stop_price_raw" "$ACE_STOP_TICK_DECIMALS")"
    else
      stop_price_raw="$(num_add "$entry_price" "$(num_div "$(num_mul "$entry_price" "$ACE_STOP_MARKET_BPS")" "10000")")"
      # Arrondi CEIL pour un SHORT : le stop ne descend JAMAIS vers le marché
      stop_price="$(ruby -e 'p=(Float(ARGV[0]) rescue 0.0); d=(Integer(ARGV[1]) rescue 1); d=1 if d < 1; f=10.0**d; printf("%.#{d}f", (p*f).ceil/f)' -- "$stop_price_raw" "$ACE_STOP_TICK_DECIMALS")"
    fi
    ts="$(now_ms)"
    q_stop="symbol=$SYMBOL&side=$close_side&type=STOP_MARKET&quantity=$qty&stopPrice=$stop_price&workingType=MARK_PRICE&reduceOnly=true${stop_position_side_param}&newClientOrderId=ACESTOP${i}&timestamp=$ts&recvWindow=$RECV_WINDOW"
    stop_resp="$(private_post "/fapi/v1/order" "$q_stop" || true)"
    stop_code="$(json_get "$stop_resp" "code")"
    if [ -n "$stop_code" ]; then
      stop_msg="$(json_get "$stop_resp" "msg")"
      echo "🔴 [FILET] ÉCHEC placement STOP_MARKET code=$stop_code msg=$stop_msg — position SANS filet physique, stop logiciel seul !"
      echo "$(date -u +%FT%TZ),$i,FILET_ERROR,$side,$entry_price,,$qty,0,0,stop_market_fail,,code=$stop_code msg=$stop_msg" >> "$LOG_FILE"
    else
      echo "🛡️ [FILET] STOP_MARKET ACESTOP${i} posé @ $stop_price (${ACE_STOP_MARKET_BPS} bps, MARK_PRICE) — filet physique armé."
    fi
  fi

  reason="timeout"
```

⚠️ **Fenêtre d'entrée sans filet** (~200-500 ms) : si le placement échoue → log `FILET_ERROR` et on **continue quand même** (le stop logiciel reste actif) — jamais de position ouverte sans boucle de gestion.

### 4. Cancel dans le bloc de sortie COMMUN (après le bloc `exit_code`, ligne ~2448)

Tous les chemins de sortie (stop_loss, trailing, shockwave, fluid, timeout, target) passent par `exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"`. Ordre validé : **sortie MARKET d'abord → PUIS cancel du filet** (si le moteur meurt entre les deux, le filet est toujours là).

```bash
    exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"
    exit_code="$(json_get "$exit_resp" "code")"
    if [ -n "$exit_code" ]; then
      msg="$(json_get "$exit_resp" "msg")"
      echo "$(date -u +%FT%TZ),$i,EXIT_ERROR,$side,$entry_price,,$qty,$current_bps,0,$reason,,code=$exit_code msg=$msg" >> "$LOG_FILE"
      echo "${C_C}Cycle $i${C_N} ${C_R}EXIT error${C_N} ${C_R}| code=$exit_code msg=$msg${C_N}"
      sleep "$SLEEP_SEC"
      continue
    fi
    # ============================================================
    # ANTI-ORPHELIN : la position est fermée par le moteur →
    # on détruit le filet physique AVANT de continuer (pas de short surprise)
    # ============================================================
    if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
      private_delete_order_sniper "$SYMBOL" "$i"
    fi
    exit_price="$(safe_call as_num "$(safe_call json_get "$exit_resp" "avgPrice")")"
```

### 4bis. Cancel dans le chemin PHASE_SHIFT (avant `[ "$ok_any" -eq 1 ]`, ligne ~1337)

`duo_v63_phase_shift_close()` ferme en 3 étapes (13/8/5) hors du bloc commun. À la fin, position à 0 → le filet doit être détruit là aussi :

```bash
  # SÉCURITÉ PHASE SHIFT (patch 17/08 V3) : position fermée, on nettoie le filet
  if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
    private_delete_order_sniper "$SYMBOL" "$i"
  fi
  [ "$ok_any" -eq 1 ]
```

⚠️ Dans cette fonction, `$i` n'est pas défini localement — reste accessible en global (script unique). À vérifier à l'intégration que `$i` est le cycle courant (sinon passer le cycle_id en argument).

### 5. Heartbeat ANTI-ORPHELIN CIBLÉ (début de CHAQUE cycle, ligne ~1508) — Δ V3

Au début de la boucle `for i in $(seq 1 "$CYCLES"); do`, après les checks `duo_global_stop_hit` / `STOP_FILE`, **avant** toute entrée. **Ordre strict : heartbeat → entrée → stop** (idempotence). **Cancel ciblé, pas de rasage** :

```bash
for i in $(seq 1 "$CYCLES"); do
  dynamic_size_note="na"
  phase_shift_step_override=""
  if duo_global_stop_hit; then
    echo "${C_R}STOP global session detected. Stopping at cycle $i.${C_N}"
    break
  fi
  if [ -f "$STOP_FILE" ]; then
    echo "${C_R}STOP file detected ($STOP_FILE). Stopping safely at cycle $i.${C_N}"
    break
  fi

  # ============================================================
  # HEARTBEAT ANTI-ORPHELIN CIBLÉ (V3) : annule l'éventuel ACESTOP${i}
  # laissé par un cycle planté — JAMAIS de rasage global (méthode bûcheron)
  # ============================================================
  if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
    private_delete_order_sniper "$SYMBOL" "$i"
  fi
```

### 6. Variables de config (après `SOFT_STOP_LOSS_BPS`, ligne ~191)

```bash
# ============================================================
# PATCH STOP_MARKET (17/08 V3) — filet physique Binance
# ============================================================
ACE_STOP_MARKET_ENABLED="${ACE_STOP_MARKET_ENABLED:-FALSE}"   # DÉSACTIVÉ par défaut → activation explicite au test (condition juge n°2)
ACE_STOP_MARKET_BPS="${ACE_STOP_MARKET_BPS:-8}"               # 8-10 bps validés famille (filet anti-crash, PAS un scalpel)
ACE_STOP_TICK_DECIMALS="${ACE_STOP_TICK_DECIMALS:-1}"         # tickSize BTCUSDT testnet = 0.1 → 1 décimale
```

---

## Réversibilité (exigence utilisateur — gravé)

| Mécanisme | Action |
|---|---|
| **Bascule instantanée** | `./scripts/basculer_setup.sh A` → retour au setup actuel (revenge permanent) en 1 commande, backup auto |
| **Backup horodaté** | `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_patch_stopmarket_<timestamp>` créé avant toute modif |
| **Runtime** | `ACE_STOP_MARKET_ENABLED=FALSE` → le filet se désactive sans toucher au code |
| **Profondeur** | git auto-sync + BAK → retour au fichier exact d'avant, même après des cycles |

## Conditions du JUGE (obligatoires avant activation)

1. **Tester la signature `private_delete()`** sur un ordre factice en testnet (les DELETE Futures sont piégeux).
2. **Garder `ACE_STOP_MARKET_ENABLED=FALSE`** jusqu'au redémarrage propre du cycle d'intégration.
