# AVIS INFERX (task inferx.analyse, morceau M3_serveur_final)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT INFERX — M3_serveur_final (lignes 381-540)

### CRITIQUE (bloquant)

**C1. Filet de sécurité dernier recours : `call_provider` re-blackliste immédiatement**
Lignes 505-520 : le filet de sécurité appelle `call_provider(prov, ...)` qui commence par `_is_blacklisted(prov)`. Or, si `tried == 0`, TOUS les providers sont blacklistés. Le filet va donc lever `BlacklistedProvider` immédiatement pour chaque provider, sans jamais tenter l'appel réel. Le filet est **inopérant** — il ne fait que re-échouer en boucle.

**Correctif proposé :**
```python
if tried == 0 and providers:
    log_event("failover", "Tous blacklistes - tentative de dernier recours sans blacklist", "")
    for prov in providers:
        try:
            _t0 = time.time()
            # Appel direct _raw_call, PAS call_provider (qui re-blackliste)
            content = _raw_call(prov, messages, temperature, max_tokens, prov.get("timeout", 600))
            _register_result(prov, True)
            log_event("message", "« " + prov["name"] + " » a repondu (dernier recours)", "")
            log_usage(task or only_model or "auto", prov.get("id", "?"), prov.get("model", "?"), prov.get("kind", "?"), duration=time.time() - _t0)
            return {"content": content, "provider": prov["name"], "attempts": attempts}
        except Exception as e:
            last_err = str(e)[:300]
            attempts.append(prov["name"] + ": " + last_err)
            log_event("failover", "Bascule depuis " + prov["name"], last_err)
```

---

### MAJEUR

**M1. Logique "coupure" incohérente — `target_ids = [pid for pid in target_ids]` est un no-op**
Ligne 448 : quand budget atteint et aucun gratuit dans `target_ids`, on fait `target_ids = [pid for pid in target_ids]` — c'est une copie identique. Le log dit "coupure" mais on continue avec les payants. Soit on coupe vraiment (vider `target_ids`), soit on change le message. Actuellement, c'est trompeur et viole la règle "gratuits jamais coupés" (on utilise des payants en budget épuisé).

**M2. `_mode_tempete_actif()` : chemins absolus codés en dur**
Ligne 397 : `os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")` — ce chemin est spécifique à la machine de Christophe. Si le hub tourne ailleurs, la détection tempête échoue silencieusement (retourne False). Devrait être relatif à `ROOT` ou configurable.

**M3. `_read_body()` : pas de limite de taille**
Ligne 465 : `int(self.headers.get("Content-Length", 0))` — un client malveillant peut envoyer un payload de plusieurs Go, le hub va tout lire en mémoire. Devrait avoir une limite (ex: 1 Mo) et renvoyer 413.

---

### MINEUR

**m1. `threshold = int(threshold) if isinstance(threshold, int) else 600`**
Ligne 384 : si `complexity_threshold` est un string numérique (ex: "600" dans routing.json), `isinstance(threshold, int)` est False → on prend 600 par défaut. Mais si c'est un float (600.0), `isinstance(600.0, int)` est False aussi → 600 par défaut. Le cast devrait être `int(threshold)` avec try/except.

**m2. `log_event("failover", "Saute (blacklist) depuis ...", "0 attente")`**
Ligne 493 : le détail "0 attente" est trompeur — le backoff peut être de 15min à 4h. Devrait afficher la durée restante.

**m3. `Handler._json` : pas de gestion des erreurs d'écriture**
Ligne 456 : `self.wfile.write(body)` peut lever `BrokenPipeError` si le client se déconnecte. Devrait être dans un try/except pour éviter un crash du thread.

**m4. `do_GET /events` et `/usage` : lecture non protégée**
Lignes 475-490 : si un autre thread écrit dans `EVENTS_PATH`/`USAGE_PATH` pendant la lecture, `readlines()` peut lever une exception. Devrait être protégé par un lock ou un try/except.

---

### COHÉRENCE AVEC LE RESTE DU HUB

**Cohérent :**
- Utilisation de `_blacklock` pour les structures partagées ✓
- `_gratuits_actifs()` dynamique depuis providers.json ✓
- Logique tempête avec réserve storm ✓
- PATIENCE (retry x3) correctement implémentée ✓

**Incohérent :**
- Le filet de sécurité (C1) est censé être le "dernier recours" mais ne fonctionne pas
- La logique "coupure" (M1) ne coupe rien en pratique

---

### VERDICT

**STATUT : REFUSÉ** — le filet de sécurité (C1) est inopérant, ce qui viole le principe "zéro défaut, on ne doit plus y revenir". En cas de panne générale blacklistant tous les providers, le hub lèvera une erreur au lieu de tenter le dernier recours.

**Priorité de correction :**
1. C1 (bloquant) : appeler `_raw_call` directement dans le filet
2. M1 (majeur) : clarifier la logique "coupure" (soit couper vraiment, soit changer le message)
3. M2 (majeur) : rendre le chemin tempête relatif à ROOT
4. M3 (majeur) : limiter la taille du body
5. Mineurs : à corriger dans une passe ultérieure
