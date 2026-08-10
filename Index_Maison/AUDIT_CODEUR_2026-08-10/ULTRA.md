# AVIS ULTRA (task ultra.analyse)

provider: OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte

**VERDICT : GO AVEC RESERVES**

**Réserves concrètes :**

1. `soumettre_hub_illimite.py` ~L110-120 : `except Exception` attrape `JSONDecodeError`/`KeyError` (réponse 200 invalide) comme erreur réseau → 3 retries inutiles (90s) avant échec. *Correction : distinguer erreurs parsing (exit 1 direct) des erreurs réseau.*

2. `deleguer_codeur.py` ~L50-65 + L85-90 : double lecture du fichier spec (`getsize` puis `read`). *Correction : `verifier_spec` retourne le contenu lu, `main` le réutilise.*

3. `lancer_detache.py` ~L25 : nom de log `ace777_detache_<PID_parent>.log` — collision possible si relance immédiate même PID. *Correction : inclure timestamp ou `uuid4()` dans le nom.*
