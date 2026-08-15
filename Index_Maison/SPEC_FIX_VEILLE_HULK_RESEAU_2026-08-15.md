# SPEC — Veille Hulk robuste au réseau (fix anti-pend) — 15/08/2026

**Cible** : `hulk-mexc/scripts/digest_watch.py` (+ 1 ligne `hulk-mexc/config/defaults.env`)
**Nature** : HORS genesis (outil paper uniquement). Réversible via backup. Ne touche PAS au moteur ACE ni à `paper_diprip.py`.
**Motif** : la veille (`digest_watch.py`) se pend sur le réseau WiFi/alpage (contrainte PERMANENTE) → plus de digest depuis 2,5 jours → positions Hulk gelées. Cause racine = aucune borne temporelle : `timeout=40s × 3 retries` par appel HTTP, ~18 paires × 4 appels = un scan peut durer des heures sous réseau dégradé.

## Objectif du fix (4 mécanismes, validés famille + Cortana)
1. **Timeout strict** : 40s → 12s par appel.
2. **Back-off exponentiel** : sleep linéaire 1s/2s → exponentiel 1→2→4s (plafonné 8s).
3. **Circuit-breaker par host** : 3 échecs réseau consécutifs sur un host (api.mexc.com / api.llama.fi) → ouverture 60s (fast-fail au lieu de marteler). Un 4xx/5xx HTTP (le serveur RÉPOND) ne compte PAS comme panne réseau.
4. **Deadline de scan globale** : 90s max par scan → si dépassée, les paires restantes passent en `scan_deadline` et le digest est marqué `degraded: true` (bandeau d'alerte dans DIGEST_LATEST.md).

## DIFF EXACT (appliquer au caractère près)

### 1. Imports — ajouter `import urllib.error`
OLD:
```
import urllib.parse
import urllib.request
```
NEW:
```
import urllib.error
import urllib.parse
import urllib.request
```

### 2. Remplacer toute la fonction `http_json` (et ajouter les helpers circuit-breaker juste avant)
OLD (fonction complète, à remplacer intégralement):
```
def http_json(url: str, timeout: float = 40.0, retries: int = 3) -> Any:
    last: Optional[Exception] = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-digest/0.1"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            last = e
            time.sleep(1.0 * (i + 1))
    raise last  # type: ignore[misc]
```
NEW:
```
# ─── Robustesse réseau (WiFi/alpage) : timeout strict + back-off + circuit-breaker ───
_CB: dict[str, dict[str, float]] = {}


def _host_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc


def _circuit_open(host: str, failures: int, cooldown_sec: float) -> bool:
    st = _CB.get(host)
    if not st:
        return False
    if st["fails"] >= failures:
        if time.time() - st["opened_at"] < cooldown_sec:
            return True
        _CB.pop(host, None)  # cooldown écoulé → on réessaie
    return False


def _record_failure(host: str) -> None:
    st = _CB.setdefault(host, {"fails": 0, "opened_at": 0.0})
    st["fails"] += 1
    st["opened_at"] = time.time()


def _record_success(host: str) -> None:
    _CB.pop(host, None)


def http_json(
    url: str,
    timeout: float = 12.0,
    retries: int = 3,
    *,
    failures: int = 3,
    cooldown_sec: float = 60.0,
) -> Any:
    host = _host_of(url)
    last: Optional[Exception] = None
    for i in range(retries):
        if _circuit_open(host, failures, cooldown_sec):
            raise TimeoutError(
                f"circuit-open {host} (réseau dégradé, pause {int(cooldown_sec)}s)"
            )
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hulk-digest/0.1"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                _record_success(host)
                return json.loads(r.read().decode())
        except Exception as e:
            last = e
            # 4xx/5xx = le serveur répond → PAS une panne réseau (ne compte pas pour le circuit)
            if not isinstance(e, urllib.error.HTTPError):
                _record_failure(host)
            time.sleep(min(2.0 ** i, 8.0))  # back-off exponentiel 1→2→4s (plafonné 8s)
    raise last  # type: ignore[misc]
```

### 3. `build_digest` — signature + deadline + flag degraded
OLD (signature + début de boucle):
```
def build_digest(cfg: dict, *, with_llama: bool = True) -> dict:
    pairs = pairs_from_cfg(cfg)
    mexc_meta = load_env(MEXC_ENV)
    has_keys = bool(mexc_meta.get("MEXC_API_KEY") and mexc_meta.get("MEXC_API_SECRET"))
    rows = []
    for pair in pairs:
        try:
```
NEW:
```
def build_digest(
    cfg: dict, *, with_llama: bool = True, deadline_sec: float = 90.0
) -> dict:
    pairs = pairs_from_cfg(cfg)
    mexc_meta = load_env(MEXC_ENV)
    has_keys = bool(mexc_meta.get("MEXC_API_KEY") and mexc_meta.get("MEXC_API_SECRET"))
    rows = []
    degraded = False
    t0 = time.time()
    for pair in pairs:
        if time.time() - t0 > deadline_sec:
            degraded = True
            rows.append(
                {"pair": pair, "error": "scan_deadline", "priority": -1, "hint": "ERR"}
            )
            continue
        try:
```

OLD (return dict — début):
```
    return {
        "ts": utc_now(),
        "mexc_keys_loaded": has_keys,
```
NEW:
```
    return {
        "ts": utc_now(),
        "degraded": degraded,
        "mexc_keys_loaded": has_keys,
```

### 4. `run_once` — lire la deadline depuis cfg + log dégradé
OLD:
```
    dig = build_digest(cfg, with_llama=with_llama)
```
NEW:
```
    deadline = float(cfg.get("SCAN_DEADLINE_SEC", "90") or 90)
    dig = build_digest(cfg, with_llama=with_llama, deadline_sec=deadline)
    if dig.get("degraded"):
        print(
            f"[{utc_now()}] ⚠ scan dégradé (deadline {deadline:.0f}s atteinte) — réseau lent, "
            f"données partielles"
        )
```

### 5. `to_markdown` — bandeau dégradé
OLD:
```
    lines = [
        f"# Hulk DIGEST — {dig['ts']}",
        "",
        f"- **Piste :** VEILLE (séparée du paper Hulk)",
```
NEW:
```
    lines = [
        f"# Hulk DIGEST — {dig['ts']}",
        "",
    ]
    if dig.get("degraded"):
        lines += [
            "> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.",
            "",
        ]
    lines += [
        f"- **Piste :** VEILLE (séparée du paper Hulk)",
```

### 6. `defaults.env` — ajouter la deadline (seule valeur lue depuis cfg)
OLD:
```
# Dédup : 1 écriture max / paire:type de hint par heure (VEILLE_CALLS / notes)
HINT_COOLDOWN_SEC=3600
```
NEW:
```
# Dédup : 1 écriture max / paire:type de hint par heure (VEILLE_CALLS / notes)
HINT_COOLDOWN_SEC=3600
# Veille robuste au réseau (WiFi/alpage) — deadline max d'un scan complet (fix 15/08)
# (timeout HTTP 12s + back-off + circuit-breaker 3 échecs/60s sont codés en dur dans digest_watch.py)
SCAN_DEADLINE_SEC=90
```

## VÉRIFICATIONS ATTENDUES (à faire après application)
1. `python3 -m py_compile scripts/digest_watch.py` → OK.
2. Test one-shot : `python3 scripts/digest_watch.py` se termine en < ~90s et écrit `runs/DIGEST_LATEST.md` (frais, pas un hang).
3. Test circuit-breaker isolé : appeler `http_json` sur un host mort (ex. `http://127.0.0.1:1/x`) → échoue en fast-fail après 3 échecs (pas 40s×3).
4. Aucun impact sur `paper_diprip.py` / genesis ACE (non touchés).

## CONTRAINTES
- Ne rien changer d'autre. Ne pas toucher à `defillama_hint` (timeout 20s/retries 2 = best-effort, déjà correct).
- `paper_diprip.py` lit `.veille_status.json` en fail-open (absent/corrompu → n'agit pas) : comportement prudent conservé, non modifié.
