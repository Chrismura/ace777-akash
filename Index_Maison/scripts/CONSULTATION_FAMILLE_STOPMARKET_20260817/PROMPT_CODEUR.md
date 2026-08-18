# 👨‍💻 CONSULTATION CODEUR — PATCH FILET DE SÉCURITÉ PHYSIQUE (STOP_MARKET + CANCEL) — 17/08/2026

**Rôle :** Tu es le codeur de la famille ACE777. On te demande une revue critique du patch ci-dessous.
**Règle famille :** Ne te contente PAS de corriger — si tu vois une MEILLEURE façon de faire, propose-la.
Tu réponds en français, structuré, honnête. Termine par : VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X%.

---

## 📋 CONTEXTE MOTEUR (vérifié, à respecter à la lettre)

- Le moteur est `genesis_manifest.txt`, **bash pur** (pas de Python/ccxt)
- `private_post()` (ligne 734) : `local path="$1" q="$2"; sig="$(sign "$q")"; curl_with_retry -X POST ...` — **POST codé en dur, ne supporte PAS DELETE**
- `sign()` et `curl_with_retry()` existent déjà et sont réutilisables
- `curl_with_retry` : `-sS --connect-timeout 10 --max-time 25`, retry max 3, pause 5s
- **Aucun `clientOrderId` n'est utilisé aujourd'hui dans le moteur** (zéro occurrence)
- **Aucune fonction d'annulation n'existe** (zéro cancel/DELETE)
- Mode hedge actif : `BINANCE_HEDGE_MODE=TRUE`, `POSITION_SIDE_STRICT=TRUE`, `POSITION_SIDE=LONG/SHORT`
- La sortie de position se fait dans le bloc commun (lignes 2431-2437) :
  ```bash
  q_exit="symbol=$SYMBOL&side=$close_side&type=MARKET&quantity=$qty${trade_position_side_param}&timestamp=$ts&recvWindow=$RECV_WINDOW"
  exit_resp="$(private_post "/fapi/v1/order" "$q_exit" || true)"
  ```
  **TOUS les chemins de sortie passent par ce bloc** (stop_loss, trailing, shockwave, fluid_exit_inversion, fluid_exit_brake, timeout, target, phase_shift)
- Le numéro de cycle est `$i` (ex: 157) — dispo dans la boucle
- Décision famille : STOP_MARKET physique à **8-10 bps** (filet anti-crash), stop logiciel à **7 bps** (scalpel), `DUO_HUNTER_HARD_STOP_MULT=2.0` gardé
- Le `clientOrderId` Binance Futures est **alphanumérique uniquement** (pas d'underscore)

## 🔧 LE PATCH PROPOSÉ (à challenger)

### Étape 1 — Nouvelle fonction `private_delete()` (à côté de private_post)
```bash
private_delete() {
  local path="$1" q="$2" sig
  sig="$(sign "$q")"
  curl_with_retry -X DELETE -H "X-MBX-APIKEY: $BINANCE_API_KEY" "$BASE_URL$path?$q&signature=$sig"
}
```

### Étape 2 — Fonction de nettoyage ciblé du stop
```bash
private_delete_order_sniper() {
  local symbol="$1" cycle_id="$2"
  local client_order_id="ACESTOP${cycle_id}"   # alphanumérique, pas d'underscore
  local query_params="symbol=${symbol}&origClientOrderId=${client_order_id}"
  echo "🧹 [NETTOYAGE] Suppression du STOP_MARKET : ${client_order_id}"
  local response
  response="$(private_delete "/fapi/v1/order" "${query_params}" || true)"
  if [ -z "$response" ]; then
    echo "⚠️ [ATTENTION] Réponse vide (réseau ?) — l'annulation n'est PAS confirmée, à vérifier"
  elif echo "$response" | grep -q '"code":'; then
    echo "⚠️ [ATTENTION] Ordre déjà exécuté ou introuvable : $(echo "$response" | head -c 200)"
  else
    echo "✅ [NETTOYAGE] Filet physique annulé proprement."
  fi
}
```

### Étape 3 — À l'ENTRÉE : poser le STOP_MARKET physique
- Après l'ordre d'entrée réussi, placer : `type=STOP_MARKET`, `side=$close_side`, `quantity=$qty`,
  `stopPrice=<entrée réelle × (1 ∓ 0.0008/0.001)>`, `reduceOnly=true`, `positionSide=LONG/SHORT`,
  `newClientOrderId=ACESTOP${i}`, `timeInForce=GTE_GTC`
- **stopPrice en PRIX ABSOLU** (pas en bps) : 8-10 bps ≈ ×(1−0.0008) à ×(1−0.001) selon le sens
- Convertir le bps → prix, et arrondir selon le tickSize de la paire

### Étape 4 — À la SORTIE (bloc commun, après exit_resp réussi) : nettoyer le stop
```bash
# Après le MARKET de sortie réussi (exit_resp sans code d'erreur) :
private_delete_order_sniper "$SYMBOL" "$i"
```
- Intégrer DANS le bloc commun (lignes 2431-2437) pour couvrir les 8 chemins de sortie
- Ne JAMAIS annuler avant la sortie (fenêtre sans protection interdite)
- Si le STOP_MARKET a déjà déclenché (position fermée par Binance), la sortie MARKET reduceOnly
  échouera en douceur et le cancel trouvera l'ordre déjà exécuté → géré par le grep '"code":'

## ❓ QUESTIONS AU CODEUR

1. **Le patch est-il correct et complet ?** Pièges cachés : mode hedge + positionSide sur le STOP_MARKET,
   tickSize/arrondi du stopPrice, timeInForce, ordre STOP_MARKET accepté sans position ouverte en hedge ?

2. **Le placement à l'entrée** : faut-il poser le STOP_MARKET AVANT ou APRÈS l'ordre MARKET d'entrée ?
   Y a-t-il une fenêtre sans protection entre les deux ? (Ex: ordre batch atomique
   `fapiPrivatePostBatchOrders` pour ouvrir + stop en un seul appel ?)

3. **La gestion d'erreur du cancel** : la détection (vide / "code": / succès) est-elle robuste ?
   Que faire si le cancel échoue mais que la sortie a réussi (stop orphelin) ?

4. **Ta MEILLEURE amélioration** : pas juste corriger. (Ex: TRAILING_STOP_MARKET natif à la place du
   STOP_MARKET fixe ? STOP_LIMIT avec price ×0.998 pour réduire le slippage ? heartbeat anti-zombie ?)

---

**Rappel :** ne touche à rien — tu donnes ton avis et ta proposition. C'est le binôme Buffy + Christophe
qui validera l'implémentation finale.
