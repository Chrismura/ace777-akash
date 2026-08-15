# SPEC — FLÉAU TIMEOUT HUB EN DÉBUT DE SESSION (v1, 13/08)

## Problème (confirmé par les logs du 13/08, boot machine 08:29 après coupure batterie)

Au début de session, le hub (launchd RunAtLoad) démarre AVANT que le réseau soit prêt.
Les premiers appels échouent en DNS (`Errno 8 nodename nor servname provided, or not known`)
et timeouts SSL. Enchaînement du fléau :

1. Erreur DNS = le réseau n'est pas encore up, PAS le provider qui est mort.
2. `call_provider` traite ça comme une « lenteur » : `sleep(2)` + **retry avec timeout x3
   (plafonné 900s)**. Une requête peut durer 12-25 min par provider.
3. Le filet de dernier recours appelle `_raw_call` avec `timeout=600` sur CHAQUE provider :
   jusqu'à 80 min par requête si tout est down.
4. Les clients (boot.sh max-time 3, scripts timeout 600) abandonnent -> BrokenPipeError.
5. 3 échecs consécutifs -> blacklist backoff (15min, 30min, 1h...). Les providers sont
   blacklistés à cause d'une panne RÉSEAU -> « Toutes les IA ont échoué » même quand le
   réseau revient. Il fallait redémarrer le hub (vider le blacklist mémoire) = « avant
   bidouillage, timeout ».

## Objectif (3 coups une pierre : logique + performance + stabilité)

Une requête hub ne doit JAMAIS dépasser ~2 min. Une panne réseau ne doit ni blacklister
les providers, ni déclencher de PATIENCE x3. Le hub doit détecter « réseau pas prêt » et
répondre vite avec une erreur claire.

## Corrections demandées (fichier : hub_prise_ia.py, uniquement)

### C1 — Distinguer erreur RÉSEAU de l'erreur PROVIDER

Dans `call_provider`, la PATIENCE (sleep + retry x3) et `_register_result(False)` ne doivent
s'appliquer qu'aux erreurs PROVIDER (HTTP 429/5xx, quota, timeout d'une API qui répond).
Une erreur RÉSEAU (résolution DNS, connexion refusée, timeout de connexion SSL) doit :
- basculer immédiatement (pas de sleep(2), pas de retry x3)
- NE PAS compter comme échec du provider (`_register_result(False)` interdit) — sinon
  3 erreurs réseau blacklistent un provider sain.

Implémentation : nouvelle exception interne `ReseauIndisponible(Exception)` levée dans
`_raw_call` quand l'erreur est une erreur de connectivité (gaierror, Errno 8, timeout de
connexion avant réponse HTTP). `call_provider` capture `ReseauIndisponible` SÉPARÉMENT :
retour d'échec immédiat sans retry ni comptage blacklist.

### C2 — Budget temps global par requête

Nouveau plafond `REQUEST_MAX_SECONDS` (constante module, défaut 120 s, lisible via
`routing.json` clé `request_max_seconds` si présente). Dans `chat_completions` :
- `t0 = time.time()` au début
- chaque `call_provider` reçoit un timeout borné : `min(prov_timeout, budget_restant)`
  où `budget_restant = REQUEST_MAX_SECONDS - (time.time() - t0)`
- le filet de dernier recours utilise aussi ce budget restant (jamais 600 brut)
- si `budget_restant <= 0` : lever `RuntimeError("Budget temps requete depasse")` -> le
  client reçoit une réponse 502 rapide au lieu d'attendre 80 min

Signature : `call_provider(prov, messages, temperature, max_tokens, timeout_budget)` et
`_raw_call` garde son paramètre `timeout` (déjà présent), on passe le budget borné.

### C3 — Détection « réseau pas prêt » (mode boot)

Au début de `chat_completions`, une fonction `_reseau_disponible()` :
- résout le DNS d'un hôte de référence (ex. `api.openai.com`) avec un timeout court (~2s)
- si KO : on tente QUAND MÊME les providers (le réseau peut revenir entre-temps) MAIS
  sans PATIENCE ni filet long : chaque `_raw_call` timeout <= 15s, et on log un événement
  `network` « Reseau pas pret — mode degrade »
- objectif : au boot, le hub répond en < 30s avec une erreur claire au lieu de 80 min

### C4 — Micro-robustesse (suggestions famille déjà validées, à conserver)

- Ne PAS toucher au mécanisme de blacklist backoff existant (fonctionne pour les vraies
  pannes provider).
- Conserver le filet de dernier recours (C1 audit famille 6) mais avec le budget C2.
- Conserver les locks (_blacklock, _loglock), le cache /health, la limite de payload.

## Tests attendus (fournir avec le code)

1. Syntaxe : `python3 -m py_compile hub_prise_ia.py`
2. Test unitaire simulé (sans vrai réseau) : `_raw_call` vers un hôte DNS inexistant
   (ex. `http://aucun-nom-xyz.invalid`) doit lever `ReseauIndisponible` rapidement
3. Test : `call_provider` avec ce provider ne doit PAS l'ajouter au blacklist après 3
   échecs réseau (vérifier `_fails[id]` reste 0)
4. Test : budget temps — appeler `chat_completions` avec un provider à timeout 600 et
   vérifier que la requête est bornée (~120s max)

## RÈGLE D'OR

Le codeur livre le code COMPLET à insérer (blocs remplaçants précis avec les numéros de
lignes du fichier réel) + les tests. Pas de diff halluciné : le code réel est en annexe.

---

## ANNEXE — CODE RÉEL ACTUEL (loi du brut, extraits concernés)

### `_raw_call` (lignes 118-156)

```python
def _raw_call(prov, messages, temperature, max_tokens, timeout):
    base = prov["base_url"].rstrip("/")
    # Patch 09/08 : les modeles Qwen3.5 locaux (Ollama) sont des reasoning models :
    # /v1/chat/completions leur laisse consommer tout le budget en "thinking" et
    # renvoie content vide -> le hub basculait a tort sur Gemini (fallback).
    # Solution : API native /api/chat + think:false = reponse directe (teste 09/08).
    if ":11434" in base:
        url = base.replace("/v1", "") + "/api/chat"
        body = json.dumps({
            "model": prov["model"],
            "messages": messages,
            "stream": False,
            "think": False,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }).encode()
    else:
        url = base + "/chat/completions"
        body = json.dumps({
            "model": prov["model"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }).encode()
    headers = {"Content-Type": "application/json"}
    if prov.get("api_key"):
        headers["Authorization"] = "Bearer " + prov["api_key"]
    req = urllib_request.Request(url, data=body, headers=headers, method="POST")
    with urllib_request.urlopen(req, timeout=timeout) as resp:
        if getattr(resp, "status", 200) != 200:
            raise RuntimeError("HTTP status " + str(getattr(resp, "status", "?")))
        raw = resp.read().decode("utf-8")
        data = json.loads(raw)
    if ":11434" in base:
        content = data.get("message", {}).get("content", "")
    else:
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    if not content or not content.strip():
        raise RuntimeError("Reponse vide")
    return content
```

### `call_provider` (lignes 283-330)

```python
def call_provider(prov, messages, temperature, max_tokens):
    """PATIENCE (fix definitif 09/08) : un fournisseur LENT mais vivant n'est PAS un echec.
    Retry 1x avec timeout x3 (plafonne a 600s) avant de laisser jouer le fallback.
    Erreurs deterministes (401/402/403/404) -> fallback immediat, sans retry inutile.
    Historique : l'appel d'audit DeepSeek V4 (129s) basculait a tort sur Gemini (timeout 120s)."""
    if _is_blacklisted(prov):
        raise BlacklistedProvider(prov.get("name", prov.get("id", "inconnu")))
    base = prov.get("timeout", 600)
    try:
        content = _raw_call(prov, messages, temperature, max_tokens, base)
        _register_result(prov, True)
        return content
    except urllib_error.HTTPError as e:
        if e.code in NON_RETRYABLE_HTTP:
            _register_result(prov, False)
            raise  # deterministe : cle, credits, modele inconnu
        log_event("timeout", "Patience " + prov["name"] + " (HTTP " + str(e.code) + ")", str(e)[:150])
        time.sleep(3)
        try:
            content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
            _register_result(prov, True)
            return content
        except Exception as e2:
            _register_result(prov, False)
            raise
    except (TimeoutError, socket.timeout, ConnectionError, urllib_error.URLError) as e:
        log_event("timeout", "Patience " + prov["name"] + " (lenteur)", str(e)[:150])
        time.sleep(2)
        try:
            content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
            _register_result(prov, True)
            return content
        except Exception as e2:
            _register_result(prov, False)
            raise
    except RuntimeError as e:
        if "Reponse vide" in str(e):
            log_event("timeout", "Patience " + prov["name"] + " (reponse vide)", str(e)[:150])
            time.sleep(2)
            try:
                content = _raw_call(prov, messages, temperature, max_tokens, min(base * 3, 900))
                _register_result(prov, True)
                return content
            except Exception as e2:
                _register_result(prov, False)
                raise
        _register_result(prov, False)
        raise
```

### Boucle `chat_completions` — appel provider + filet (lignes 474-517)

```python
    attempts, last_err, tried = [], "", 0
    for prov in providers:
        if _is_blacklisted(prov):
            attempts.append(prov.get("name", "?") + ": blacklist du jour (saute)")
            log_event("failover", "Saute (blacklist) depuis " + prov.get("name", "?"), "0 attente")
            continue
        tried += 1
        try:
            _t0 = time.time()
            content = call_provider(prov, messages, temperature, max_tokens)
            log_event("message", "« " + prov["name"] + " » a repondu", "bascule" if attempts else "")
            log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
            return {"content": content, "provider": prov["name"], "attempts": attempts}
        except Exception as e:
            last_err = str(e)[:300]
            attempts.append(prov["name"] + ": " + last_err)
            log_event("failover", "Bascule depuis " + prov["name"], last_err)
    # Filet de securite (reserve audit 09/08) : si TOUS les providers etaient blacklistes
    # (tried == 0), on force UNE derniere tentative sans blacklist pour ne jamais planter
    # silencieusement en cas de panne generale.
    # C1 - Filet de dernier recours : on contourne volontairement le blacklist
    # (but du mecanisme, audit famille 6). On appelle _raw_call directement
    # car call_provider commencerait par _is_blacklisted -> levee immediate.
    if tried == 0 and providers:
        log_event("failover", "Tous blacklistes - tentative de dernier recours sans blacklist", "")
        for prov in providers:
            try:
                _t0 = time.time()
                content = _raw_call(prov, messages, temperature, max_tokens, prov.get("timeout", 600))
                _register_result(prov, True)
                log_event("message", "« " + prov["name"] + " » a repondu (dernier recours)", "")
                log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
                return {"content": content, "provider": prov["name"], "attempts": attempts}
            except Exception as e:
                last_err = str(e)[:300]
                attempts.append(prov["name"] + ": " + last_err)
                log_event("failover", "Bascule depuis " + prov["name"], last_err)
    log_event("error", "Toutes les IA ont echoue", " | ".join(attempts)[:500])
    raise RuntimeError("Toutes les IA branchees ont echoue. Derniere erreur : " + last_err)
```

### Début de `chat_completions` (lignes 377-383) — point d'insertion C2/C3

```python
def chat_completions(payload):
    providers = load_config()
    messages = payload.get("messages", [])
    temperature = payload.get("temperature", 0.7)
    max_tokens = payload.get("max_tokens", 2048)
    task = payload.get("task")
    only_model = payload.get("model")
    messages = _injecter_contexte_vivant(task, messages)
```

### Utilitaires disponibles (déjà en place, NE PAS réécrire)

- `_is_blacklisted(prov)`, `_register_result(prov, ok)`, `_fails`, `_blacklist`, `_blacklock`
- `log_event(kind, title, detail)`, `log_usage(task, provider, model, kind, duration=None)`
- `load_routing()`, `_gratuits_actifs()`, `_mode_tempete_actif()`, `_get_strat_path()`
- imports : `json, os, sys, threading, time, socket, subprocess` + `urllib.request/error`
