# AVIS DEEPSEEK (task mission, morceau M3_serveur_final)

provider: NVIDIA build.nvidia.com (100+ modeles)

Audit du morceau M3_serveur_final (lignes 381-540) — verdict : **REFUSÉ (2 bugs bloquants, 3 défauts majeurs)**

---

## 🔴 BUGS BLOQUANTS

### 1. **Filet de sécurité dernier recours : boucle infinie potentielle**
**Lignes 481-497** : le filet de sécurité appelle `call_provider()` qui vérifie `_is_blacklisted()`. Si TOUS les providers sont blacklistés, `call_provider()` lève `BlacklistedProvider` immédiatement — le filet ne tente RIEN. Pire : si un provider est blacklisté mais que `_is_blacklisted()` expire pendant la boucle (race condition), le provider est réessayé, échoue, et `_register_result(False)` le re-blackliste. La boucle peut tourner indéfiniment si les providers sont en backoff court.

**Correctif** : le filet doit appeler `_raw_call()` directement (contourne le blacklist), pas `call_provider()`.

### 2. **`_read_body()` : crash sur JSON invalide**
**Ligne 399** : `json.loads(raw or "{}")` lève `json.JSONDecodeError` si le body est malformé. Dans `do_POST`, cette exception est attrapée par le `try` global → réponse 502. MAIS : si le client envoie un body vide avec `Content-Length: 0`, `raw = ""` → `json.loads("{}")` OK. Si le client envoie `Content-Length: 5` avec `"hello"` → crash → 502. Correct mais **le message d'erreur expose le stack trace** (via `str(e)`) — fuite d'info.

---

## 🟠 DÉFAUTS MAJEURS

### 3. **`/health` : charge `load_config()` à chaque requête**
**Ligne 403** : `len(load_config())` relit et parse `providers.json` à CHAQUE health check. Sous charge (monitoring toutes les 5s), c'est du gaspillage I/O. Pire : si le fichier est corrompu, `/health` renvoie 500 au lieu de 200 — le monitoring externe peut déclencher une fausse alerte.

**Correctif** : cache avec TTL (ex: 30s) + fallback sur dernier état connu.

### 4. **`/events` et `/usage` : lecture non atomique**
**Lignes 407-420** : `readlines()[-25:]` lit le fichier entier en mémoire. Si `log_event()` écrit pendant la lecture (concurrence), on peut lire une ligne partielle → `json.loads` échoue → ligne ignorée silencieusement. Pas de crash, mais **perte de données de monitoring**.

**Correctif** : utiliser `seek()` vers la fin + `read()` partiel, ou accepter la perte (documenter).

### 5. **`do_POST` : pas de limite de taille de body**
**Ligne 397** : `int(self.headers.get("Content-Length", 0))` — un client malveillant peut envoyer `Content-Length: 999999999` → le hub lit 1 Go en mémoire → OOM. Le hub est en localhost, mais un process compromis sur la machine peut le tuer.

**Correctif** : `if length > 10_000_000: raise ValueError("Body trop grand")`.

---

## 🟡 DÉFAUTS MINEURS

### 6. **`_json()` : pas de flush explicite**
**Ligne 392** : `self.wfile.write(body)` — sous ThreadingHTTPServer, le buffer peut ne pas être flushé avant la fermeture de connexion. Ajouter `self.wfile.flush()`.

### 7. **`log_message` silencieux**
**Ligne 438** : `pass` — les erreurs HTTP (404, 502) ne sont jamais loggées. En production, impossible de tracer les requêtes échouées.

### 8. **`chat_completions` : `only_model` non validé**
**Ligne 456** : si `payload["model"]` est un dict ou une liste, `only_model not in ("", "auto")` lève `TypeError`. Le payload vient du client → crash 502.

---

## ✅ CE QUI EST BON

- **Filet de sécurité** : loggue correctement avant tentative (ligne 483)
- **Gestion budget** : `gratuits = _gratuits_actifs()` est dynamique (pas de liste figée)
- **Tempête** : `taches_prio` est un set, pas une liste — O(1) lookup
- **`_read_body`** : gère le cas `Content-Length: 0` proprement

---

## 📋 CORRECTIFS OBLIGATOIRES (avant validation)

```python
# 1. Filet de sécurité : utiliser _raw_call directement
if tried == 0 and providers:
    log_event("failover", "Tous blacklistes - tentative de dernier recours sans blacklist", "")
    for prov in providers:
        try:
            _t0 = time.time()
            # Contourne _is_blacklisted() — le filet est le dernier recours
            content = _raw_call(prov, messages, temperature, max_tokens, prov.get("timeout", 600))
            log_event("message", "« " + prov["name"] + " » a repondu (dernier recours)", "")
            log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
            return {"content": content, "provider": prov["name"], "attempts": attempts}
        except Exception as e:
            last_err = str(e)[:300]
            attempts.append(prov["name"] + ": " + last_err)
            log_event("failover", "Bascule depuis " + prov["name"], last_err)

# 2. _read_body : limite de taille + validation
def _read_body(self):
    length = int(self.headers.get("Content-Length", 0))
    if length > 10_000_000:  # 10 Mo max
        raise ValueError("Body trop grand")
    raw = self.rfile.read(length).decode() if length else "{}"
    try:
        return json.loads(raw or "{}")
    except json.JSONDecodeError:
        raise ValueError("JSON invalide")

# 3. /health : cache 30s
_health_cache = {"ts": 0, "count": 0}
def _health_count():
    now = time.time()
    if now - _health_cache["ts"] > 30:
        try:
            _health_cache["count"] = len(load_config())
            _health_cache["ts"] = now
        except Exception:
            pass  # garde l'ancien
    return _health_cache["count"]

# 4. do_POST : catch spécifique pour _read_body
def do_POST(self):
    if self.path == "/v1/chat/completions":
        try:
            payload = self._read_body()
        except ValueError as e:
            self._json(400, {"error": {"message": str(e)}})
            return
        try:
            result = chat_completions(payload)
            # ... (reste inchangé)
```

---

## 🏁 VERDICT FINAL

**Le morceau est refusé en l'état.** Les bugs 1 et 2 sont bloquants (le filet de sécurité ne fonctionne pas comme prévu, et un body malformé peut crasher le handler). Les correctifs ci-dessus sont simples et ne changent pas l'architecture. Une fois appliqués, je revalide.

**Note pour la famille** : le reste du hub (blacklist, budget, tempête) est solide. Ce morceau est le dernier maillon — il doit être aussi robuste que le reste.
