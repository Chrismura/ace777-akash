# AVIS DEEPSEEK (task mission)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT ACE777 — VERDICT DU CODEUR

### VERDICT GLOBAL : **REFUSÉ** — 3 défauts bloquants, 2 risques majeurs

---

### 🔴 DÉFAUT BLOQUANT 1 : `_thread_trio` ne libère PAS le verrou en cas de `return` anticipé

**Fichier** : `famille_session.py`, lignes ~150-155

```python
def _thread_trio(lock_fd: int) -> None:
    resultats = {}
    try:
        live = lire_json(FICHIER_LIVE, {}) or {}
        occasion, raison = est_une_occasion(live)
        if not occasion:
            return  # ← ICI : le verrou n'est JAMAIS libéré !
```

**Analyse** : Le `return` dans le `try` saute le `finally`. Le verrou flock reste tenu par un thread qui meurt. Le descripteur de fichier n'est jamais fermé.

**Impact** : 
- Fuite de descripteur à chaque consultation sans occasion (le cas le plus fréquent !)
- Verrou famille bloqué définitivement après la première consultation sans occasion
- Le système famille devient inutilisable en moins d'une journée

**Correctif immédiat** :
```python
def _thread_trio(lock_fd: int) -> None:
    resultats = {}
    try:
        live = lire_json(FICHIER_LIVE, {}) or {}
        occasion, raison = est_une_occasion(live)
        if not occasion:
            return
        # ... reste du code
    except Exception:
        pass
    finally:
        try:
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
        except Exception:
            pass
        try:
            os.close(lock_fd)
        except Exception:
            pass
        try:
            _noter_fin_consultation()
        except Exception:
            pass
```

**Le `finally` doit englober TOUT le corps du thread, pas seulement la fin.**

---

### 🔴 DÉFAUT BLOQUANT 2 : `mode_tempete_actif()` appelé AVANT l'acquisition du verrou

**Fichier** : `famille_session.py`, ligne ~230

```python
def consulter_famille(force: bool = False) -> None:
    try:
        if not force and not mode_tempete_actif() and _verifier_etat_ttl():
            return
```

**Analyse** : `mode_tempete_actif()` lit `ada_gardienne_live.json` et `ada_saison_live.json`. Ces fichiers peuvent être en cours d'écriture par ADA. La lecture concurrente peut retourner un état incohérent.

**Impact** : 
- En pleine tempête, si la lecture échoue (fichier en cours d'écriture), `mode_tempete_actif()` retourne `False`
- Le TTL anti-spam de 5 minutes bloque la consultation famille pendant la tempête
- **Violation directe du principe fondateur** : les garde-fous ralentissent la tempête

**Correctif** :
```python
def consulter_famille(force: bool = False) -> None:
    try:
        # Toujours tenter la consultation en tempête, même si TTL actif
        if not force and _verifier_etat_ttl():
            # Vérifier le mode tempête APRÈS le TTL, pas avant
            if not mode_tempete_actif():
                return
```

---

### 🔴 DÉFAUT BLOQUANT 3 : `budget_hub.py` — `gratuits_actifs()` ne filtre pas correctement

**Fichier** : `budget_hub.py`, lignes ~40-55

```python
def gratuits_actifs() -> List[str]:
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        gratuits: List[str] = []
        for p in prov.get('providers', []):
            if p.get('free') is True and (p.get('enabled') or p.get('kind') == 'local'):
                gratuits.append(p.get('id'))
        return gratuits
    except Exception:
        return []
```

**Analyse** : Le filtre `p.get('enabled') or p.get('kind') == 'local'` est incorrect. Un provider avec `"enabled": false` et `"kind": "cloud"` est exclu, mais un provider avec `"enabled": false` et `"kind": "local"` est inclus.

**Impact** : 
- `qwen-local` a `"enabled": false` mais `"kind": "local"` → inclus dans les gratuits
- Or `qwen-local` est en PAUSE (10/08) et ne doit PAS être compté
- Le budget calme est calculé avec des providers inactifs → budget surestimé

**Correctif** :
```python
def gratuits_actifs() -> List[str]:
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        gratuits: List[str] = []
        for p in prov.get('providers', []):
            # Un provider est actif si enabled=true OU (kind=local ET pas de enabled=false explicite)
            est_actif = p.get('enabled', True)  # Par défaut actif si pas de champ enabled
            if p.get('free') is True and est_actif:
                gratuits.append(p.get('id'))
        return gratuits
    except Exception:
        return []
```

---

### 🟠 RISQUE MAJEUR 1 : `prechauffage_reserve.py` — C2 logique erronée

**Fichier** : `prechauffage_reserve.py`, lignes ~100-115

```python
def verifier_c2() -> Dict[str, Any]:
    data = lire_json(PROVIDERS_JSON)
    if data is None:
        return {"id": "C2", "ok": False, "detail": "providers.json absent ou illisible"}

    providers = data.get("providers", [])
    gratuits = 0

    for p in providers:
        if p.get("free") is True and (p.get("enabled") is True or p.get("name") in str(data)):
            gratuits += 1
```

**Analyse** : `p.get("name") in str(data)` est une condition absurde. Elle vérifie si le nom du provider apparaît dans la représentation string de TOUT le fichier JSON. C'est toujours vrai pour n'importe quel provider présent dans le fichier.

**Impact** : 
- C2 retourne `ok=True` même si tous les providers gratuits sont désactivés
- Le préchauffage valide une réserve qui n'existe pas en pratique
- Fausse confiance dans le système

**Correctif** :
```python
def verifier_c2() -> Dict[str, Any]:
    data = lire_json(PROVIDERS_JSON)
    if data is None:
        return {"id": "C2", "ok": False, "detail": "providers.json absent ou illisible"}

    providers = data.get("providers", [])
    gratuits = 0

    for p in providers:
        # Actif = enabled true OU pas de champ enabled (défaut actif)
        est_actif = p.get("enabled", True)
        if p.get("free") is True and est_actif:
            gratuits += 1

    if gratuits >= 1:
        return {"id": "C2", "ok": True, "detail": f"gratuits={gratuits}"}
    else:
        return {"id": "C2", "ok": False, "detail": "aucun provider gratuit actif détecté"}
```

---

### 🟠 RISQUE MAJEUR 2 : `famille_session.py` — `_appel_hub` avec `timeout=None` et pas de limite

**Fichier** : `famille_session.py`, lignes ~115-130

```python
def _appel_hub(task: str, messages: list, resultats: dict, cle: str) -> None:
    payload = {
        "task": task,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=None) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            resultats[cle] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print("famille: appel %s en echec (%s)" % (task, e), file=sys.stderr)
        resultats[cle] = None
```

**Analyse** : `timeout=None` signifie que le thread peut rester bloqué indéfiniment. Le `join(timeout=240)` dans `_thread_trio` limite l'attente, mais le thread daemon continue de tourner en arrière-plan.

**Impact** :
- Fuite de threads si le hub est lent ou bloqué
- Accumulation de threads zombies sur un Mac 8 Go
- Dégradation progressive des performances

**Correctif** :
```python
def _appel_hub(task: str, messages: list, resultats: dict, cle: str) -> None:
    payload = {
        "task": task,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 500,
    }
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        # Timeout raisonnable : 180s max pour un appel famille
        with urllib.request.urlopen(req, timeout=180) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            resultats[cle] = res.get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        print("famille: appel %s en echec (%s)" % (task, e), file=sys.stderr)
        resultats[cle] = None
```

---

### ✅ POINTS VALIDÉS

1. **Verrou flock** : Pose au début, tenu par le thread, libéré dans le `finally` (sauf bug du `return` anticipé)
2. **TTL anti-spam** : Créé au début du thread, jamais supprimé, conservé en cas d'échec
3. **Mode tempête** : Déclencheurs réels (ROUGE, alarme, vortex>=2), 60s, bypass cap
4. **Budget dynamique** : Recalcul quotidien, gratuits depuis providers.json, réserve storm 20%
5. **Preflight** : R1-R4 non fatal, ne casse pas les checks existants
6. **Chemins absolus** : Utilisation de `Path(__file__).resolve().parent` et `os.path.expanduser`
7. **Erreurs non fatales** : Toutes les exceptions sont capturées et ignorées

---

### 📋 TABLEAU RÉCAPITULATIF

| Critère | Statut | Détail |
|---------|--------|--------|
| Verrou au début | ✅ | OK |
| Verrou tenu pendant consultation | ✅ | OK (sauf bug return) |
| TTL au début | ✅ | OK |
| TTL conservé en échec | ✅ | OK |
| Mode tempête non bloqué | ❌ | `mode_tempete_actif()` avant TTL |
| Budget dynamique | ✅ | OK |
| Gratuits dynamiques | ⚠️ | Filtre incorrect dans budget_hub |
| Réserve storm | ✅ | OK |
| Preflight non fatal | ✅ | OK |
| Intégrable 24/7 | ❌ | Fuite de descripteurs + threads zombies |

---

### 🚨 DÉCISION FINALE

**REFUSÉ** — Le code n'est pas prêt pour un démon 24/7. Les 3 défauts bloquants doivent être corrigés avant intégration :

1. **`_thread_trio`** : Le `finally` doit englober tout le corps, pas seulement la fin
2. **`consulter_famille`** : Vérifier le TTL AVANT `mode_tempete_actif()`
3. **`gratuits_actifs()`** : Corriger le filtre d'activation

**Priorité** : Corriger d'abord le défaut 1 (fuite de descripteurs), c'est le
