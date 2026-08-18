# PATCH STOP_MARKET V1 — Filet de sécurité physique Binance

**Date :** 17/08/2026 — **Cible :** `genesis_manifest.txt` (setup A, md5 `fe2a7bcc9dc1f31bd524ffc433f9186d` = `genesis_manifest.txt.BAK_avant_fix_heartbeat_20260815-152847`)
**Validé par :** round table famille 17/08 (5/5) + codeur (GO-AVEC-RÉSERVE 85%) + binôme (Buffy + pilote).
**Règle :** rien n'est intégré tant que la famille (2 + juge) n'a pas validé cette V1 concrète.

---

## Ce que fait le patch (en clair)

À chaque entrée de position, on pose un **STOP_MARKET côté Binance** (le filet physique, surveillé par leurs serveurs, zéro dépendance à la boucle logicielle). À chaque sortie logicielle, on **annule ce stop** (anti-orphelin). Au début de chaque cycle, on **rase les stops orphelins** d'un cycle planté. 8-10 bps, garde le stop logiciel comme coupeur principal.

## Les 6 morceaux du patch

### 1. Nouvelle fonction `private_delete()` (après `private_post()`, ligne ~738)

`private_post()` est codé en dur avec `-X POST` — il ne peut PAS faire un DELETE. On crée la fonction dédiée :

```bash
# ============================================================
# DELETE signé (annulation d'ordres) — ajout patch STOP_MARKET
# ============================================================
private_delete() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl_with_retry -X DELETE -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BASE_URL$path?$q&signature=$sig"
}
```

### 2. Routine anti-orphelin `private_delete_order_sniper()` (après `private_delete()`)

Cancel ciblé par `origClientOrderId=ACESTOP${i}` (alphanumérique, sans underscore — Binance Futures rejette `_`). Gère le cas « réponse vide » (réseau coupé = statut INCONNU, pas un succès) :

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

### 3. Placement du STOP_MARKET à l'entrée (après `entry_ts_iso=...`, ligne ~2128)

Point d'ancrage réel : juste après `entry_ts_iso="$(date -u +%FT%TZ)"`, avant `reason="timeout"`. On a `$entry_price`, `$qty`, `$side`, `$close_side`, `$trade_position_side_param` à disposition. stopPrice arrondi au tickSize (ruby printf — le moteur n'a pas de fonction d'arrondi prix, on en ajoute une inline) :

```bash
  entry_ts_iso="$(date -u +%FT%TZ)"

  # ============================================================
  # FILET PHYSIQUE : STOP_MARKET posé chez Binance (patch 17/08)
  # stopPrice = entrée ± stop_bps, arrondi au tickSize
  # ============================================================
  if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
    # positionSide obligatoire en mode hedge — dérivé du sens du trade
    if [ "$side" = "BUY" ]; then
      stop_position_side="LONG"
      stop_price_raw="$(num_sub "$entry_price" "$(num_div "$(num_mul "$entry_price" "$ACE_STOP_MARKET_BPS")" "10000")")"
    else
      stop_position_side="SHORT"
      stop_price_raw="$(num_add "$entry_price" "$(num_div "$(num_mul "$entry_price" "$ACE_STOP_MARKET_BPS")" "10000")")"
    fi
    # Arrondi au tickSize (ex: BTCUSDT testnet = 0.1 → 1 décimale). Configurable.
    stop_price="$(ruby -e 'p=(Float(ARGV[0]) rescue 0.0); d=(Integer(ARGV[1]) rescue 1); d=1 if d < 1; printf("%.#{d}f", p)' -- "$stop_price_raw" "$ACE_STOP_TICK_DECIMALS")"
    ts="$(now_ms)"
    q_stop="symbol=$SYMBOL&side=$close_side&type=STOP_MARKET&quantity=$qty&stopPrice=$stop_price&reduceOnly=true&positionSide=$stop_position_side&newClientOrderId=ACESTOP${i}&timestamp=$ts&recvWindow=$RECV_WINDOW"
    stop_resp="$(private_post "/fapi/v1/order" "$q_stop" || true)"
    stop_code="$(json_get "$stop_resp" "code")"
    if [ -n "$stop_code" ]; then
      stop_msg="$(json_get "$stop_resp" "msg")"
      echo "🔴 [FILET] ÉCHEC placement STOP_MARKET code=$stop_code msg=$stop_msg — position SANS filet physique, stop logiciel seul !"
      echo "$(date -u +%FT%TZ),$i,FILET_ERROR,$side,$entry_price,,$qty,0,0,stop_market_fail,,code=$stop_code msg=$stop_msg" >> "$LOG_FILE"
    else
      echo "🛡️ [FILET] STOP_MARKET ACESTOP${i} posé @ $stop_price (${ACE_STOP_MARKET_BPS} bps) — filet physique armé."
    fi
  fi

  reason="timeout"
```

⚠️ **Sécurité fenêtre d'entrée** : entre l'entrée MARKET et le placement du stop (~200-500 ms), la position est sans filet. Si le placement échoue → on log `FILET_ERROR` et on **continue quand même** (le stop logiciel reste actif, la boucle de gestion tourne) — jamais de position ouverte sans boucle de gestion. C'est la condition qu'on s'était fixée.

### 4. Cancel dans le bloc de sortie COMMUN (après `exit_resp`, ligne ~2437)

Le point structurel : TOUS les chemins de sortie (stop_loss, trailing, shockwave, fluid, timeout, target, phase_shift) passent par `exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"`. On injecte le cancel juste après la réussite de la sortie MARKET :

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

**Ordre validé** : sortie MARKET d'abord (position fermée, `reduceOnly` protège la fenêtre) → PUIS cancel du filet. Si le moteur meurt entre les deux, le filet est toujours là ✅.

⚠️ **Cas phase_shift** : la sortie `duo_v63_phase_shift_close` (ligne ~2418) est un chemin séparé qui ne passe pas par `exit_resp`. Il faut vérifier où elle retourne et y ajouter le cancel aussi — sinon un cycle sorti par phase_shift laisse son ACESTOP orphelin.

### 5. Heartbeat anti-orphelin (début de CHAQUE cycle, ligne ~1508)

Au début de la boucle `for i in $(seq 1 "$CYCLES"); do`, avant toute entrée — on rase les ACESTOP restants d'un cycle planté :

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
  # HEARTBEAT ANTI-ORPHELIN : rase les ACESTOP restants d'un cycle planté
  # (aucun vieux stop ne peut parasiter le trade suivant)
  # ============================================================
  if [ "$ACE_STOP_MARKET_ENABLED" = "TRUE" ]; then
    ts="$(now_ms)"
    q_scrub="symbol=$SYMBOL&timestamp=$ts&recvWindow=$RECV_WINDOW"
    scrub_resp="$(private_delete "/fapi/v1/allOpenOrders" "$q_scrub" || true)"
    echo "🧹 [HEARTBEAT] Cycle $i — rasage des ordres orphelins $SYMBOL : $(echo "$scrub_resp" | head -c 120)"
  fi
```

⚠️ Le `allOpenOrders` rase TOUT sur la paire — dans ce moteur il n'y a que les ACESTOP qui dorment (entrées/sorties = MARKET immédiats), donc c'est sûr. À confirmer par le codeur qu'aucun autre ordre légitime ne dort jamais sur la paire.

### 6. Variables de config (à côté de `SOFT_STOP_LOSS_BPS`, ligne ~191)

```bash
# ============================================================
# PATCH STOP_MARKET (17/08) — filet physique Binance
# ============================================================
ACE_STOP_MARKET_ENABLED="${ACE_STOP_MARKET_ENABLED:-FALSE}"   # DÉSACTIVÉ par défaut → activation explicite au test
ACE_STOP_MARKET_BPS="${ACE_STOP_MARKET_BPS:-8}"               # 8-10 bps validés famille (filet anti-crash, PAS un scalpel)
ACE_STOP_TICK_DECIMALS="${ACE_STOP_TICK_DECIMALS:-1}"         # tickSize BTCUSDT testnet = 0.1 → 1 décimale
```

---

## Points de vigilance pour le codeur

1. **phase_shift** : la sortie `duo_v63_phase_shift_close` ne passe pas par le bloc commun → il faut trouver le point de retour et y mettre le cancel.
2. **`reduceOnly` + STOP_MARKET** : Binance Futures accepte-t-il `reduceOnly=true` sur un STOP_MARKET ? (normalement oui, à confirmer).
3. **`workingType`** : par défaut `CONTRACT_PRICE` (prix du contrat). Pour un filet anti-crash, `MARK_PRICE` est-il plus robuste (évite les wicks du dernier prix) ? À débattre.
4. **stopPrice arrondi** : `printf` ruby arrondit au plus proche. Pour un stop SELL (long), un arrondi au-dessus du niveau calculé = coupe plus tôt que prévu (OK, protège) ; pour un stop BUY (short), l'inverse. Vérifier que l'arrondi ne déplace jamais le stop du mauvais côté.
5. **Fenêtre d'entrée sans filet** (~200-500 ms) : acceptable en testnet, mais si le placement échoue, on ne doit JAMAIS bloquer la boucle de gestion (position ouverte sans gestion = pire).
6. **Coexistence stop logiciel (7 bps soft / 16 bps hard) + filet (8-10 bps)** : le filet ne se déclenche que si la boucle meurt ou traîne. Aucun conflit attendu — à confirmer que le moteur ne voit pas la position fermée par Binance comme une anomalie.
