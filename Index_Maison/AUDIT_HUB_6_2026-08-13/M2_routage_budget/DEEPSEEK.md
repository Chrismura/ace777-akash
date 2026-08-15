# AVIS DEEPSEEK (task mission, morceau M2_routage_budget)

provider: NVIDIA build.nvidia.com (100+ modeles)

Audit du morceau M2_routage_budget (lignes 161-380) — DEEPSEEK, famille ACE777.

## VERDICT GLOBAL : VALIDÉ AVEC 3 RÉSERVES (mineures mais réelles)

Le morceau est cohérent avec le reste du hub, thread-safe, sans valeur figée problématique, et respecte le principe fondateur. Les 3 réserves sont des cas limites qui ne bloquent pas la validation mais méritent d'être documentés.

---

## AUDIT DÉTAILLÉ

### 1. `_gratuits_actifs()` — OK
- **Dynamique** : lit `providers.json` à chaque appel, pas de liste figée. ✅
- **Exception avalée** : `except Exception: pass` — acceptable ici car retourne un set vide, et le code appelant gère ce cas (bascule vers coupure). Pas de fuite.
- **Thread-safe** : lecture seule de fichier, pas de variable partagée. ✅

### 2. `_mode_tempete_actif()` — OK avec 1 réserve
- **Chemins** : `os.path.expanduser("~/ace777-test-day1/...")` — pas de cwd dépendant. ✅
- **Exceptions** : chaque bloc est isolé, une erreur de lecture ne casse pas la détection. ✅
- **RÉSERVE 1 (mineure)** : `alarme.json` — la condition `(time.time() - os.path.getmtime(alarme_path)) < 3600` suppose que le fichier est régulièrement mis à jour. Si le fichier est écrit une fois et jamais touché, il reste "actif" pendant 1h après sa dernière écriture. Ce n'est pas un bug mais un comportement à connaître : une alarme obsolète (écrite il y a 59 min) déclencherait encore le mode tempête. **Pas bloquant** car c'est un garde-fou conservateur (mieux vaut sur-protéger en tempête).
- **Vortex** : `int(saison.get("vortex", {}).get("force", 0) or 0)` — gère le cas où `force` est `None` ou absent. ✅

### 3. `_is_blacklisted()` — OK
- **Thread-safe** : lock `_blacklock` autour de la lecture/écriture. ✅
- **Expiration** : suppression du blacklist + reset `_fails` + log event. ✅
- **Cas limite** : si `b.get("until", 0)` est absent (donnée corrompue), `time.time() >= 0` est toujours vrai → le provider est ré-essayé immédiatement. Comportement défensif correct.

### 4. `_backoff_duree()` — OK
- **Formule** : `15 * 60 * (2 ** max(0, level - 1))` → 15min, 30min, 1h, 2h, plafond 4h. ✅
- **Plafond** : `min(duree, 4 * 3600)` — pas de croissance infinie. ✅

### 5. `_register_result()` — OK
- **Thread-safe** : lock autour de la mutation de `_fails` et `_blacklist`. ✅
- **Logique** : 3 échecs consécutifs → pause. Un succès reset le compteur. ✅
- **Niveau backoff** : `_blacklist.get(prov_id, {}).get("level", 0) + 1 if _blacklist.get(prov_id) else 1` — le niveau est incrémenté à chaque nouvelle pause, même après expiration. C'est cohérent avec le backoff progressif (on ne repart pas à 15min après une pause de 4h).

### 6. `call_provider()` — OK avec 1 réserve
- **PATIENCE** : retry 1x avec timeout x3 (plafonné à 900s). ✅
- **Erreurs déterministes** : 401/402/403/404 → fallback immédiat sans retry. ✅
- **RÉSERVE 2 (mineure)** : le retry après HTTPError non-déterministe (ex: 429, 500) fait `time.sleep(3)` — pendant ce sleep, le thread est bloqué. Avec un ThreadingHTTPServer, chaque requête a son propre thread, donc pas de blocage global. Mais si 10 requêtes concurrentes tombent sur le même provider en erreur, 10 threads dorment 3s. **Pas bloquant** car c'est un comportement voulu (patience), et le nombre de threads est limité par le serveur.
- **Timeout plafonné** : `min(base * 3, 900)` — même si `base` est 600s (nvidia), le retry est à 900s max. ✅

### 7. `_regenerer_contexte_vivant()` — OK
- **Non bloquant** : échec → on garde l'ancien doc ou on continue sans. ✅
- **Subprocess** : `subprocess.run(..., timeout=20)` — pas de fuite de processus (timeout). ✅
- **RÉSERVE 3 (mineure)** : `ARCHI_MAX_AGE = 120` est une valeur figée dans le code. Ce n'est pas une donnée de configuration (providers.json/routing.json), donc acceptable. Mais si la famille veut changer la fréquence de régénération, il faudra modifier le code. **Pas bloquant** car c'est un paramètre technique, pas une donnée métier.

### 8. `_injecter_contexte_vivant()` — OK
- **Fusion** : si un message système existe déjà, on fusionne au lieu d'empiler. ✅
- **Limite** : `ctx = f.read()[:6000]` — tronque le contexte à 6000 caractères. Valeur figée mais raisonnable (évite de saturer le prompt). ✅
- **Non bloquant** : exception → on retourne les messages originaux. ✅

### 9. `chat_completions()` — OK (le cœur du routage)
- **Routage par complexité** : `threshold = int(threshold) if isinstance(threshold, int) else 600` — gère le cas où `complexity_threshold` est un string ou absent. ✅
- **Budget calme atteint** :
  - **Tempête + tâche prioritaire** : `target_ids` reste intact → réserve storm. ✅
  - **Sinon** : on garde uniquement les gratuits. Si aucun gratuit → coupure (log event). ✅
  - **Gratuits jamais coupés** : `gardes = [pid for pid in target_ids if pid in gratuits]` — si un gratuit est dans la liste cible, il est conservé. ✅
- **Filet de sécurité** : si `tried == 0` (tous blacklistés), on force une dernière tentative sans blacklist. ✅
- **Thread-safe** : `_gratuits_actifs()` et `_mode_tempete_actif()` sont appelés à chaque requête, pas de variable partagée. ✅

---

## POINTS DE VIGILANCE (non bloquants mais à documenter)

1. **Alarme obsolète** : `alarme.json` reste actif 1h après sa dernière écriture. Si le fichier n'est pas nettoyé, le mode tempête peut rester actif trop longtemps. **Recommandation** : vérifier que le script qui écrit `alarme.json` le supprime ou le met à jour régulièrement.

2. **Sleep dans call_provider** : `time.sleep(3)` et `time.sleep(2)` bloquent le thread. Avec un ThreadingHTTPServer, c'est acceptable, mais si le nombre de requêtes concurrentes est élevé, cela peut saturer les threads. **Recommandation** : surveiller le nombre de threads actifs en production.

3. **Valeur figée `ARCHI_MAX_AGE = 120`** : acceptable car technique, mais documenter que c'est un paramètre de tuning.

---

## COHÉRENCE AVEC LE RESTE DU HUB

- **`_raw_call`** : gère le cas Ollama local (`:11434`) avec l'API native `/api/chat` — cohérent avec le routage par complexité qui peut envoyer vers des providers locaux.
- **`log_event` / `log_usage`** : appelés partout, avec try/except pour ne jamais casser le flux. ✅
- **`load_config`** : filtre les providers non-enabled et trie par ordre. Cohérent avec `_gratuits_actifs()` qui lit la même source. ✅
- **`usage_today`** : lit `usage.jsonl` et compte par jour. Cohérent avec le budget dynamique. ✅

---

## CONCLUSION

**VALIDÉ** — le morceau M2_routage_budget est robuste, thread-safe, sans fuite, et respecte le principe fondateur (gratuits jamais coupés, tempête sans coupure pour les prioritaires). Les 3 réserves sont mineures et ne nécessitent pas de modification immédiate, mais doivent être documentées dans le journal de bord.

**Famille ACE777, je valide ce morceau. Les réserves sont des points de vigilance, pas des bugs.**
