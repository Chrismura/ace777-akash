# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

En tant qu'expert de la famille ACE777 (analyse profonde), voici mon audit du bloc preflight proposé pour la réserve storm.

### VERDICT : **GO AVEC RESERVES**

Le code fourni par le codeur du hub est de très bonne facture, élégant, respectueux de la philosophie ACE777 (non bloquant, utilisation intelligente de scripts Python inline pour parser les JSON sans dépendre de structures complexes) et parfaitement aligné avec la spec R1-R4 et le chantier storm du 13/08.

Cependant, **2 réserves mineures d'implémentation** (liées à la robustesse macOS / `stat` et à la sémantique de R3) doivent être ajustées avant l'intégration définitive.

---

### ANALYSE DÉTAILLÉE & RÉSERVES CONCRÈTES

#### 1. R1, R2, R4 : Conforme et robuste
- **R1** : Lecture propre de `routing.json` avec repli à 0 en cas d'erreur. Les helpers `ok()` et `warn()` sont bien utilisés.
- **R2** : Gestion habile du format de `providers.json` (qu'il s'agisse d'une liste directe ou d'un objet contenant une clé `"providers"`).
- **R4** : Vérification correcte de l'exécutabilité (`-x`).

#### 2. Réserve n°1 : La commande `stat` sous macOS (R3)
- **Le problème** : À la ligne `mtime=$(stat -f %m ...)` :
  - Sur **macOS**, `stat -f %m` fonctionne parfaitement.
  - Mais si le script est un jour exécuté ou testé dans un conteneur Linux (CI/CD type Docker), `stat -f %m` plantera (Linux utilise `stat -c %Y`).
  - De plus, sous `set -euo pipefail`, si une commande de substitution échoue ou renvoie du vide, cela peut propager une exception si mal géré.
- **Correction recommandée** : Utiliser une syntaxe multi-OS ou sécuriser la récupération du mtime :
  ```bash
  mtime=$(stat -f %m ~/prise-ia/prechauffage_reserve.json 2>/dev/null || stat -c %Y ~/prise-ia/prechauffage_reserve.json 2>/dev/null || echo 0)
  ```

#### 3. Réserve n°2 : Cohérence du message d'erreur si `verdict != "OK"` (R3)
- **Le problème** : Si le fichier `prechauffage_reserve.json` existe et a moins de 24h, mais que son `verdict` interne est par exemple `"WARN"` ou `"FAIL"`, le script tombe dans le `else` et affiche :
  `warn "préchauffage réserve pas OK/récent — ..."`
  Ce message mélange "pas OK" et "pas récent", alors que le fichier est pourtant récent. 
- **Correction recommandée** (optionnelle mais plus propre) : Distinguer l'âge et le verdict dans les messages de warning pour un déverminage instantané.

---

### CODE CORRIGÉ PRÊT POUR L'INTÉGRATION

Voici le bloc final optimisé (intégration directe juste avant `# --- Ruby ---`) :

```bash
# --- Réserve storm (préchauffage 13/08) ---
# R1 — Budget et réserve présents dans routing.json
if [ -f ~/prise-ia/routing.json ]; then
  vals=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        j = json.load(f)
    print(j.get("cloud_daily_budget", 0) or 0)
    print(j.get("cloud_daily_reserve", 0) or 0)
except Exception:
    print(0)
    print(0)
' ~/prise-ia/routing.json 2>/dev/null)
  budget=$(echo "$vals" | head -n1)
  reserve=$(echo "$vals" | tail -n1)
  if [ "$budget" != "0" ] && [ -n "$budget" ]; then
    ok "budget calme=$budget"
  else
    warn "budget calme absent ou nul"
  fi
  if [ "$reserve" != "0" ] && [ -n "$reserve" ]; then
    ok "réserve storm=$reserve"
  else
    warn "réserve storm absente — lancer : cd ~/prise-ia && python3 budget_hub.py --apply"
  fi
else
  warn "routing.json absent — impossible de vérifier budget/réserve"
fi

# R2 — Gratuits dynamiques détectés dans providers.json
if [ -f ~/prise-ia/providers.json ]; then
  count=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        data = json.load(f)
    providers = data if isinstance(data, list) else data.get("providers", [])
    free_count = sum(1 for p in providers if isinstance(p, dict) and p.get("free") is True)
    print(free_count)
except Exception:
    print(0)
' ~/prise-ia/providers.json 2>/dev/null)
  if [ "$count" -gt 0 ] 2>/dev/null; then
    ok "gratuits dynamiques détectés ($count)"
  else
    warn "aucun provider gratuit détecté — la bascule tempête serait sans filet"
  fi
else
  warn "providers.json absent — impossible de vérifier les gratuits dynamiques"
fi

# R3 — Rapport de préchauffage récent
if [ -f ~/prise-ia/prechauffage_reserve.json ]; then
  now=$(date +%s)
  mtime=$(stat -f %m ~/prise-ia/prechauffage_reserve.json 2>/dev/null || stat -c %Y ~/prise-ia/prechauffage_reserve.json 2>/dev/null || echo 0)
  age=$((now - mtime))
  if [ "$age" -lt 86400 ]; then
    verdict=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        j = json.load(f)
    print(j.get("verdict", ""))
except Exception:
    print("")
' ~/prise-ia/prechauffage_reserve.json 2>/dev/null)
    if [ "$verdict" = "OK" ]; then
      date_str=$(date -r "$mtime" "+%Y-%m-%d %H:%M" 2>/dev/null || echo "récemment")
      ok "préchauffage réserve OK ($date_str)"
    else
      warn "préchauffage réserve verdict != OK — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
    fi
  else
    warn "préchauffage réserve trop ancien (>24h) — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
  fi
else
  warn "rapport préchauffage réserve absent — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
fi

# R4 — Préchauffage exécutable
if [ -x ~/prise-ia/prechauffage_reserve.py ]; then
  ok "préchauffage prêt"
else
  warn "prechauffage_reserve.py absent ou non exécutable"
fi
```

**Intégration validée dès application de ces micropouces de robustesse cross-platform.**
