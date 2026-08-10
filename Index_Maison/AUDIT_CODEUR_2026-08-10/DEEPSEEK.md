# AVIS DEEPSEEK (task mission)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT FLUX CODEUR — LOI 1QUINQUIES

### VERDICT : GO AVEC RÉSERVES

---

### CONFORMITÉ LOI 1QUINQUIES : ✅ CONFORME

Le flux respecte strictement la séparation des rôles :
- **Ada** : spécifie (SPEC_revue_scripts_timeout_v2.md), intègre, teste
- **Codeur du hub** : écrit le code (via `deleguer_codeur.py` → `soumettre_hub_illimite.py`)
- **Ada** : n'écrit AUCUN code dans ce flux, uniquement des specs et de l'orchestration

---

### ROBUSTESSE : ✅ SOLIDE (avec réserves)

| Point | État | Analyse |
|-------|------|---------|
| Timeout illimité | ✅ | `timeout=None` dans `urlopen` (soumettre_hub_illimite.py:97) |
| Retries différenciés | ✅ | 429/5xx retryables, 4xx non-retryables (lignes 104-118) |
| Détachement macOS | ✅ | `start_new_session=True` (lancer_detache.py:29) |
| Garde spec vide | ✅ | `verifier_spec()` vérifie taille source > 20 octets (deleguer_codeur.py:38-51) |
| Garde mission | ✅ | Existence + non-vide avant lecture (soumettre_hub_illimite.py:48-62) |
| Requête reconstruite | ✅ | `req` créée dans la boucle (ligne 88) |
| Logs détaché | ✅ | stdout/stderr → fichier log (lancer_detache.py:27-29) |
| Timeout lancement 60s | ✅ | `subprocess.run(timeout=60)` (deleguer_codeur.py:89) |

---

### RÉSERVES CONCRÈTES (3 points)

#### R1 : `deleguer_codeur.py:89` — TimeoutExpired ne tue pas le processus enfant

**Problème** : Si `subprocess.run(timeout=60)` expire, le processus `lancer_detache.py` est tué, MAIS le processus détaché (`soumettre_hub_illimite.py`) a déjà été lancé par `Popen` et **survit** (c'est le but). Le message d'erreur "timeout lancement détaché" est **trompeur** : le codeur tourne peut-être déjà.

**Impact** : Perte de temps à diagnostiquer un "échec" qui n'en est pas un.

**Correction suggérée** :
```python
except subprocess.TimeoutExpired:
    # Le lanceur a expiré, mais le processus détaché peut être vivant
    print("[ATTENTION] timeout lancement (60s) — vérifier si le codeur tourne", file=sys.stderr)
    print("[INFO] poller %s pour la réponse" % out_path)
    sys.exit(0)  # Pas un échec : le détaché est peut-être parti
```

---

#### R2 : `soumettre_hub_illimite.py:97` — `urlopen(timeout=None)` peut bloquer indéfiniment

**Problème** : `timeout=None` signifie "attendre indéfiniment". Si le hub se fige (pas de réponse, pas d'erreur), le script reste bloqué **pour toujours**. Les retries ne servent à rien si la connexion ne se ferme jamais.

**Impact** : Un appel IA qui ne répond pas = processus zombie qui consomme des ressources sans fin.

**Correction suggérée** :
```python
# timeout=None est dangereux si le hub se fige sans erreur
# Utiliser un timeout très long (ex: 3600s = 1h) plutôt que None
with urllib.request.urlopen(req, timeout=3600) as resp:
```
Ou mieux : garder `timeout=None` mais ajouter un watchdog externe qui vérifie la fraîcheur du fichier de sortie.

---

#### R3 : `soumettre_hub_illimite.py:104-118` — Pas de retry sur erreurs réseau `URLError`

**Problème** : Le `except Exception` (ligne 120) capture les `URLError` (connexion refusée, DNS, etc.) et retry, MAIS le message dit "erreur réseau" alors que ça peut être une erreur de parsing JSON, un timeout de lecture, etc. La distinction est floue.

**Impact** : Une erreur applicative (JSON invalide) sera retryée 3 fois avec 30s d'attente = 90s perdues.

**Correction suggérée** :
```python
except urllib.error.URLError as e:
    # Erreur réseau pure : retryable
    print("[essai %d/%d] erreur réseau: %s" % (attempt, RETRIES, e.reason))
    time.sleep(RETRY_DELAY)
except (json.JSONDecodeError, KeyError) as e:
    # Erreur applicative : pas de retry
    print("[ECHEC] réponse hub invalide: %s" % e, file=sys.stderr)
    with open(out_path, "a", encoding="utf-8") as f:
        f.write("\n\n## ERREUR RÉPONSE INVALIDE\n\n%s\n" % e)
    return 1
except Exception as e:
    # Autres erreurs : retry
    print("[essai %d/%d] erreur inattendue: %s" % (attempt, RETRIES, e))
    time.sleep(RETRY_DELAY)
```

---

### ABSENCE DE FAILLE COÛTEUSE : ✅ (avec R1 comme point de vigilance)

Le problème du 10/08 (timeouts tuant les appels IA) est **réglé** :
- `timeout=None` élimine les coupures
- `start_new_session=True` garantit la survie
- Les gardes d'entrée empêchent les lancements inutiles

**MAIS** : R1 peut créer une fausse alerte (le codeur tourne alors qu'on croit qu'il a échoué). C'est un coût de diagnostic, pas un coût de crédits.

---

### TESTS RÉELS : ✅ VALIDÉS

Les 3 cas d'échec propres + flux valide OK sont cohérents avec le code. Les messages sont clairs, sans traceback.

---

### CONCLUSION

**GO AVEC RÉSERVES** — Le flux est fonctionnel et conforme. Les 3 réserves sont des améliorations de robustesse, pas des failles bloquantes. R1 est la plus importante (fausse alerte possible). R2 et R3 sont des cas limites.

**Priorité de correction** : R1 > R3 > R2 (R2 est acceptable si le hub est fiable).
