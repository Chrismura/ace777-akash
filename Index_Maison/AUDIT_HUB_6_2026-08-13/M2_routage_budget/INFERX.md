# AVIS INFERX (task inferx.analyse, morceau M2_routage_budget)

provider: NVIDIA build.nvidia.com (100+ modeles)

Audit du morceau M2_routage_budget (lignes 161-380) — **RAPPORT D'AUDIT**

---

## VERDICT GLOBAL : **2 ANOMALIES MAJEURES, 3 MINEURES**

Le morceau est globalement cohérent avec l'architecture, mais présente **2 défauts critiques** qui violent les principes fondateurs.

---

## ANOMALIES MAJEURES

### 🔴 A1 — `_mode_tempete_actif()` : **CHEMIN ABSOLU CÂBLÉ EN DUR** (violation règle 3)
**Ligne 176 :**
```python
strat = os.path.expanduser("~/ace777-test-day1/Index_Maison/strategie")
```
**Problème :** Ce chemin est **câblé en dur** alors que `ROOT` est défini en tête de fichier (ligne 25). Si le hub est déplacé, la détection de tempête échoue silencieusement → **les tâches prioritaires peuvent être coupées en tempête** (violation du principe fondateur).

**Correctif :**
```python
strat = os.path.join(ROOT, "..", "Index_Maison", "strategie")
# ou mieux : définir une constante STRATEGIE_PATH en tête de fichier
```

---

### 🔴 A2 — `_register_result()` : **RACE CONDITION sur `_blacklist`** (violation règle 2)
**Lignes 220-224 :**
```python
with _blacklock:
    if ok:
        _fails[prov_id] = 0
        return
    _fails[prov_id] = _fails.get(prov_id, 0) + 1
    if _fails[prov_id] >= 3:
        level = _blacklist.get(prov_id, {}).get("level", 0) + 1 if _blacklist.get(prov_id) else 1
```
**Problème :** Le calcul de `level` fait **deux lectures** de `_blacklist.get(prov_id)` :
1. `_blacklist.get(prov_id, {}).get("level", 0)` 
2. `_blacklist.get(prov_id)` (test de vérité)

Entre ces deux lectures, un autre thread peut **modifier** `_blacklist[prov_id]` (via `_is_blacklisted` qui fait un `del`). Résultat : `level` peut être calculé sur un état **incohérent** → backoff incorrect.

**Correctif :**
```python
with _blacklock:
    if ok:
        _fails[prov_id] = 0
        return
    _fails[prov_id] = _fails.get(prov_id, 0) + 1
    if _fails[prov_id] >= 3:
        existing = _blacklist.get(prov_id)
        level = (existing.get("level", 0) + 1) if existing else 1
        duree = _backoff_duree(level)
        _blacklist[prov_id] = {"until": time.time() + duree, "level": level}
        _fails[prov_id] = 0
```

---

## ANOMALIES MINEURES

### 🟡 M1 — `_gratuits_actifs()` : **Exception silencieuse sans log** (violation règle 1)
**Lignes 161-166 :**
```python
try:
    for p in load_config():
        if p.get("free"):
            gratuits.add(p.get("id"))
except Exception:
    pass
```
**Problème :** Si `providers.json` est corrompu, on retourne un set **vide** → tous les gratuits sont considérés payants → **coupure des tâches en budget atteint** (violation du principe "gratuit jamais coupé").

**Correctif :** Logger l'erreur et **retourner `None`** pour signaler l'échec, plutôt qu'un set vide trompeur.

---

### 🟡 M2 — `_mode_tempete_actif()` : **Lecture non atomique des fichiers** (violation règle 2)
**Lignes 176-210 :** Les fichiers `ada_gardienne_live.json`, `alarme.json`, etc. sont lus **sans lock**. Si un autre processus écrit pendant la lecture → `json.load` peut lever une exception → tempête non détectée.

**Correctif :** Utiliser un **lock de lecture** (ex: `_storm_lock = threading.Lock()`) autour de chaque lecture, ou au minimum un `try/except` plus granulaire avec log.

---

### 🟡 M3 — `_injecter_contexte_vivant()` : **Fuite de contexte sur messages système multiples**
**Lignes 300-310 :**
```python
if messages and messages[0].get("role") == "system":
    messages = list(messages)
    precedent = messages[0].get("content", "")
    messages[0] = {"role": "system", "content": precedent + "\n\n" + system}
    return messages
```
**Problème :** Si `messages` contient **plusieurs** messages système (ex: un système initial + un système ajouté par un appel précédent), seul le premier est fusionné. Les autres restent → **contexte dupliqué** → le LLM peut être confus.

**Correctif :** Fusionner **tous** les messages système en un seul, ou ne garder que le dernier.

---

## POINTS CONFORMES (validés)

✅ **`_is_blacklisted()`** : Thread-safe, expiration automatique, log correct.

✅ **`_backoff_duree()`** : Progression exponentielle correcte, plafond 4h.

✅ **`call_provider()`** : Patience bien implémentée, retry avec timeout x3, erreurs déterministes gérées.

✅ **`chat_completions()`** : Routage par complexité correct, budget dynamique, réserve storm bien gérée.

✅ **`_regenerer_contexte_vivant()`** : Non-bloquant, timeout 20s, fallback sur ancien doc.

---

## RECOMMANDATIONS PRIORITAIRES

1. **Corriger A1 immédiatement** : remplacer le chemin câblé par `ROOT`-relatif.
2. **Corriger A2** : factoriser la lecture de `_blacklist` dans une variable locale.
3. **Corriger M1** : logger l'erreur et retourner `None` en cas d'échec de `_gratuits_actifs()`.
4. **Ajouter des logs** dans `_mode_tempete_actif()` pour chaque fichier lu (debug).

---

## CONCLUSION

Le morceau est **fonctionnellement correct** dans 95% des cas, mais les 2 anomalies majeures peuvent causer :
- **A1** : coupure des tâches prioritaires en tempête (violation du principe fondateur)
- **A2** : backoff incohérent → provider blacklisté trop longtemps ou pas assez

**Niveau de risque : ÉLEVÉ** — à corriger avant mise en production.
