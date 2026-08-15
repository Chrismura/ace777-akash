# AVIS INFERX (task inferx.analyse, morceau M1_coeur_reseau)

provider: NVIDIA build.nvidia.com (100+ modeles)

Audit du morceau M1_coeur_reseau (lignes 1-160) — INFERX, famille ACE777.

**Verdict global :** Le morceau est globalement sain, robuste et conforme aux principes fondateurs. Cependant, j'ai identifié **3 incohérences majeures** et **2 points de vigilance** qui doivent être corrigés pour atteindre le niveau "zéro défaut" exigé.

---

### 🔴 INCOHÉRENCE MAJEURE 1 : `load_config()` — Fuite de clé API dans les logs et les réponses

**Localisation :** Lignes 47-58.

**Problème :** La fonction `load_config()` charge les clés API dans le dictionnaire `providers` retourné. Ce dictionnaire est ensuite utilisé dans `chat_completions()` (ligne ~250) pour construire la réponse HTTP `/v1/chat/completions` :
```python
return {"content": content, "provider": prov["name"], "attempts": attempts}
```
Heureusement, la réponse n'inclut pas `prov` entier, mais le dictionnaire `prov` est passé à `_raw_call()` et `call_provider()`. Si une exception est levée et que `last_err` contient des informations sensibles (ex. `str(e)` d'une erreur HTTP avec l'URL complète incluant la clé API), cela pourrait fuiter dans les logs `/events` et dans la réponse d'erreur 502.

**Impact :** Risque de fuite de secrets dans les logs et les réponses HTTP. C'est une faille de sécurité critique pour un "hedge fund suisse".

**Correctif proposé :**
```python
def load_config():
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    providers = []
    for p in data.get("providers", []):
        if not p.get("enabled", True):
            continue
        key = p.get("api_key_env")
        api_key = os.environ.get(key, "") if key else p.get("api_key", "")
        # Ne PAS stocker la clé en clair dans le dictionnaire retourné
        providers.append({**p, "api_key": api_key})
    providers.sort(key=lambda x: x.get("order", 99))
    return providers
```
**Action requise :** Dans `_raw_call()`, ne jamais inclure la clé API dans les messages d'erreur. Utiliser `prov["name"]` au lieu de `prov` dans les logs.

---

### 🔴 INCOHÉRENCE MAJEURE 2 : `_raw_call()` — Détection Ollama fragile et non-conforme

**Localisation :** Lignes 91-120.

**Problème :** La détection d'Ollama repose sur `":11434" in base`. C'est une valeur en dur qui viole le principe "zéro valeur figée". Si le port d'Ollama change (ex. 11435 pour un second Ollama), le hub enverra une requête au format OpenAI à Ollama, qui la rejettera.

**Impact :** En cas de changement de port Ollama, le hub échouera silencieusement ou basculera sur un fallback inutile, violant le principe de robustesse.

**Correctif proposé :**
```python
def _raw_call(prov, messages, temperature, max_tokens, timeout):
    base = prov["base_url"].rstrip("/")
    # Détection Ollama via le champ "kind" ou "api" dans providers.json
    if prov.get("kind") == "local" or prov.get("api") == "ollama":
        url = base.replace("/v1", "") + "/api/chat"
        # ... (reste inchangé)
    else:
        # ... (reste inchangé)
```
**Action requise :** Ajouter un champ `"api": "ollama"` ou `"kind": "local"` dans providers.json pour les providers Ollama, et utiliser ce champ pour la détection.

---

### 🔴 INCOHÉRENCE MAJEURE 3 : `usage_today()` — Lecture non thread-safe et fuite de fichier

**Localisation :** Lignes 70-84.

**Problème :** La fonction `usage_today()` ouvre le fichier `USAGE_PATH` en lecture sans verrou. Comme le hub est un `ThreadingHTTPServer`, plusieurs requêtes concurrentes peuvent appeler `usage_today()` simultanément. Si `log_usage()` écrit dans le même fichier pendant qu'une lecture est en cours, cela peut provoquer une `OSError` (fichier en cours d'utilisation) ou une lecture corrompue.

**Impact :** Crash potentiel du hub en cas de forte concurrence, ou comptage incorrect du budget cloud.

**Correctif proposé :**
```python
_usage_lock = threading.Lock()

def usage_today():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    counts = {}
    if os.path.exists(USAGE_PATH):
        with _usage_lock:
            with open(USAGE_PATH) as f:
                for line in f:
                    try:
                        ev = json.loads(line)
                    except Exception:
                        continue
                    if ev.get("ts", "")[:10] == today:
                        k = ev.get("kind", "?")
                        counts[k] = counts.get(k, 0) + 1
    return counts
```
**Action requise :** Ajouter un verrou global `_usage_lock` pour protéger toutes les lectures/écritures sur `USAGE_PATH`.

---

### 🟡 POINT DE VIGILANCE 1 : `log_event()` et `log_usage()` — Écritures non thread-safe

**Localisation :** Lignes 60-68 et 86-96.

**Problème :** Les deux fonctions ouvrent le fichier en mode append (`"a"`) sans verrou. En cas de concurrence, deux threads peuvent écrire simultanément, provoquant une corruption de ligne ou une exception `OSError`.

**Impact :** Logs corrompus, perte d'événements, ou crash du hub.

**Correctif proposé :**
```python
_event_lock = threading.Lock()

def log_event(kind, title, detail=""):
    ev = {"ts": datetime.now(timezone.utc).isoformat(), "kind": kind, "title": title, "detail": detail}
    try:
        with _event_lock:
            with open(EVENTS_PATH, "a") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    except Exception:
        pass
    return ev
```
**Action requise :** Ajouter des verrous dédiés pour `EVENTS_PATH` et `USAGE_PATH`.

---

### 🟡 POINT DE VIGILANCE 2 : `load_env()` — Variables d'environnement non thread-safe

**Localisation :** Lignes 30-40.

**Problème :** `os.environ.setdefault()` n'est pas thread-safe. Si deux requêtes concurrentes appellent `load_env()` (via `load_config()`), cela peut provoquer une `RuntimeError` ("dictionary changed size during iteration").

**Impact :** Crash potentiel du hub en cas de forte concurrence.

**Correctif proposé :**
```python
_env_lock = threading.Lock()

def load_env(path):
    if not os.path.exists(path):
        return
    with _env_lock:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
```
**Action requise :** Ajouter un verrou pour protéger `os.environ`.

---

### ✅ POINTS CONFORMES

- **Chemins absolus :** `ROOT = os.path.dirname(os.path.abspath(__file__))` — conforme.
- **Zéro dépendance :** stdlib uniquement — conforme.
- **Blacklist/backoff :** Logique correcte, thread-safe via `_blacklock` — conforme.
- **Gratuits dynamiques :** `_gratuits_actifs()` lit providers.json — conforme.
- **Tempête :** `_mode_tempete_actif()` est non-bloquant et robuste — conforme.
- **Non-fatalité :** Les exceptions dans `log_event`, `log_usage`, `load_routing` sont avalées — conforme.

---

### 📋 RÉSUMÉ DES ACTIONS REQUISES

| # | Sévérité | Problème | Correctif |
|---|----------|----------|-----------|
| 1 | 🔴 Critique | Fuite de clé API dans les logs/réponses | Ne jamais inclure `prov` dans les logs, utiliser `prov["name"]` |
| 2 | 🔴 Critique | Détection Ollama fragile (`:11434` en dur) | Utiliser un champ `"api": "ollama"` dans providers.json |
| 3 | 🔴 Critique | `usage_today()` non thread-safe | Ajouter `_usage_lock` |
| 4 | 🟡 Majeur | `log_event()`/`log_usage()` non thread-safe | Ajouter `_event_lock` et `_usage_lock` |
| 5 | 🟡 Majeur | `load_env()` non thread-safe | Ajouter `_env_lock` |

**Décision :** Le morceau est **REFUSÉ** en l'état. Les 3 incohérences majeures doivent être corrigées avant validation famille. Les points de vigilance sont à traiter dans la même itération pour garantir le niveau "zéro défaut".

**INFERX, prêt à auditer la version corrigée.**
