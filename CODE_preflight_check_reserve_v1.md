# RÉPONSE HUB (task code.ia · via Puter Grok (gratuit)) — 2026-08-13T16:29:58

**Position d'insertion :** juste avant la ligne `# --- Ruby ---` (après le bloc `vortex_control.json`).

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
  mtime=$(stat -f %m ~/prise-ia/prechauffage_reserve.json 2>/dev/null || echo 0)
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
      warn "préchauffage réserve pas OK/récent — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
    fi
  else
    warn "préchauffage réserve pas OK/récent — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
  fi
else
  warn "préchauffage réserve pas OK/récent — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
fi

# R4 — Préchauffage exécutable
if [ -x ~/prise-ia/prechauffage_reserve.py ]; then
  ok "préchauffage prêt"
else
  warn "prechauffage_reserve.py absent"
fi
```
