# SPEC — CORRECTIONS HUB (audit famille 6, 13/08) — objectif ZÉRO hedge fund suisse

## Contexte

Audit famille COMPLETE (6 cerveaux × 3 morceaux = 18 avis) du `hub_prise_ia.py`.
Verdicts : M1 🟢🟢🟢🟡🟡🔴, M2 🟢🟢🟢🟡🟡🔴, M3 🟡🟡🔴🔴 (les 🔴 sont
DEEPSEEK et INFERX). Le superviseur a VÉRIFIÉ chaque point dans le code réel.
Cette spec ne contient QUE les points réels convergents. Les points faux ont été
écartés (le finally englobe le return, l'ordre TTL/tempête est équivalent, la
race _register_result est sous _blacklock).

## Corrections demandées (classées par priorité)

### C1 — 🔴 Filet de sécurité INOPÉRANT (DEEPSEEK + INFERX convergents, vérifié)

**Problème** : dans `chat_completions()`, le filet de dernier recours (quand
`tried == 0`, c'est-à-dire TOUS les providers blacklistés) appelle
`call_provider()`, qui COMMENCE par `_is_blacklisted(prov)` → lève
`BlacklistedProvider` immédiatement → le filet ne tente JAMAIS un appel réel.
Il re-échoue en boucle. Pire : les providers en backoff court peuvent être
réessayés et re-blacklistés en boucle.

**Correctif** : dans le filet, appeler `_raw_call()` DIRECTEMENT (contourne le
blacklist — c'est le but du dernier recours) :
```python
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
```

### C2 — 🔴 Coupure no-op : le budget est contourné (INFERX, vérifié)

**Problème** : quand budget calme atteint et aucun gratuit dans la chaîne cible :
```python
target_ids = [pid for pid in target_ids]   # copie IDENTIQUE — no-op !
log_event("quota", "... -> coupure", task)
```
Le log dit « coupure » mais `target_ids` est inchangé → le hub CONTINUE avec les
payants en budget épuisé. La dépense n'est jamais coupée.

**Correctif** : couper VRAIMENT (vider la liste → aucune requête payante ne part,
le hub répond une erreur propre). OU chercher parmi TOUS les gratuits du système
(pas seulement ceux de la chaîne). Le plus conforme au principe
« gratuits jamais coupés » : élargir aux gratuits de tout providers.json d'abord,
puis couper si vraiment rien de gratuit :
```python
else:
    tous_gratuits = [p for p in providers if p.get("id") in gratuits]
    if tous_gratuits:
        target_ids = [p["id"] for p in tous_gratuits]
        log_event("quota", "Budget calme atteint -> bascule famille (tous gratuits)", task)
    else:
        target_ids = []
        log_event("quota", "Budget calme atteint, aucun gratuit dispo -> coupure reelle", task)
```

### C3 — 🟡 Chemins tempête + tâches prioritaires en dur (INFERX + GROK)

**Problème** :
- `_mode_tempete_actif()` utilise `os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")` — chemin machine en dur. Si le hub est déplacé, la détection tempête échoue silencieusement → tâches prioritaires coupées en tempête.
- `taches_prio = {"signets.juge", ...}` est un set en dur dans le code — devrait vivre dans routing.json (principe « valeur fixe → on coule »).

**Correctif** :
1. Chemin tempête : construire depuis `ROOT` (le hub est dans `~/prise-ia/`, le projet dans `~/ace777-test-day1/`) OU depuis une constante configurable lue dans routing.json. Le plus robuste : `os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")` remplacé par un chemin dérivé de `ROOT` avec repli.
2. `taches_prio` : lire depuis `routing.json` clé `"priority_tasks"` (liste), défaut au set actuel si absente.

### C4 — 🟡 Robustesse serveur (DEEPSEEK + INFERX + JUGE)

1. **`load_config()` sans try/except** : si providers.json est corrompu → crash du hub. Wrapper try/except → retourne liste vide + log_event.
2. **`_read_body()` sans limite** : `Content-Length` illimité → OOM possible. Limiter à 10 Mo (ou 1 Mo) → 413 si dépassé.
3. **JSON invalide dans `_read_body`** : `json.loads` lève → 502 avec stack trace exposée. Retourner un message d'erreur propre (400).
4. **Écritures logs non verrouillées** (`log_event`, `log_usage`) : ajouter un lock partagé (les appends concurrents peuvent se corrompre).
5. **`/health` recharge `load_config()` à chaque appel** : cache 30s.
6. **`_raw_call` : vérifier `resp.status == 200`** avant de parser (réponse 200 avec corps invalide → crash).
7. **`encoding="utf-8"` explicite** sur tous les `open()` (JUGE) pour éviter UnicodeDecodeError selon la locale.

### C5 — 🟢 Mineurs (si dans la passe, sinon documentés)

- `BrokenPipeError` sur `self.wfile.write` (client déconnecté) → try/except.
- `log_message` : logger les erreurs 4xx/5xx (au lieu de pass total).
- `threshold` cast : `int(threshold)` avec try/except (gère "600" string et 600.0 float).
- Message `"0 attente"` dans le log de blacklist sauté → afficher la durée restante.

## Règles absolues

1. Python 3.9 stdlib, non fatal (jamais de crash), commentaires français.
2. Ne PAS casser : blacklist/backoff, gratuits dynamiques, mode tempête, contexte
   vivant, PATIENCE, réserve storm (déjà validés par la famille).
3. Les corrections C1-C4 sont OBLIGATOIRES. C5 recommandé.
4. Contrat de sortie : le diff complet (blocs avant/après) de `hub_prise_ia.py`,
   prêt à intégrer, avec l'indication des numéros de lignes.
