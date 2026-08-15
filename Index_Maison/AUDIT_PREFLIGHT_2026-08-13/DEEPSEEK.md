# AVIS DEEPSEEK (task mission)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT PREFLIGHT RÉSERVE STORM — VERDICT : GO AVEC RÉSERVES

### Analyse ligne par ligne

**R1 — Budget/réserve (routing.json)** ✅
- Parseur robuste : try/except, fallback 0, pas de crash si fichier absent
- `head -n1` / `tail -n1` corrects pour extraire les deux valeurs
- Attention : si `cloud_daily_budget` = 0.5, le test `[ "$budget" != "0" ]` passe (0.5 ≠ 0) ✅
- **RÉSERVE** : si `cloud_daily_budget` = 0.0 (float), le test échoue car "0.0" ≠ "0" → warning à tort. Utiliser `[ "$budget" != "0" ] && [ "$budget" != "0.0" ]` ou comparer en float.

**R2 — Gratuits dynamiques (providers.json)** ✅
- Parseur robuste : gère liste ou objet avec clé "providers"
- `is True` strict : un provider avec `"free": 1` ne sera pas compté — acceptable si le format est strict
- **RÉSERVE** : `[ "$count" -gt 0 ] 2>/dev/null` — si count est vide (cas improbable), le test échoue silencieusement. Ajouter `[ -n "$count" ] && [ "$count" -gt 0 ]`.

**R3 — Rapport préchauffage** ✅
- `stat -f %m` macOS correct
- Calcul d'âge correct (86400 s = 24 h)
- **RÉSERVE** : si `mtime` = 0 (stat échoue), `age` = now → warning correct. Mais si le fichier est vieux de plus de 24h, le message "pas OK/récent" est trompeur (le fichier peut être OK mais vieux). Améliorer le message pour distinguer "pas OK" vs "trop vieux".

**R4 — Exécutable** ✅
- `-x` correct, pas de crash si absent

### Intégration avec le script existant

- **Position** : avant `# --- Ruby ---` ✅ conforme à la spec
- **Helpers** : utilise `ok()` / `warn()` ✅
- **Non fatal** : tous les cas KO → warn, pas de fail ✅
- **set -euo pipefail** : 
  - `vals=$(python3 ...)` : si python3 échoue, `2>/dev/null` capture l'erreur, `vals` vide → warning correct, pas de crash ✅
  - `echo "$vals" | head -n1` : pipe avec set -o pipefail — si head échoue (improbable), le script s'arrête. **RÉSERVE** : utiliser `printf '%s\n' "$vals" | head -n1` ou capturer dans une variable avant.

### Points bloquants potentiels

1. **Ligne 14** : `budget=$(echo "$vals" | head -n1)` — avec `set -o pipefail`, si `echo` échoue (improbable mais possible si vals contient des caractères spéciaux), le script s'arrête. Utiliser `printf '%s\n' "$vals" | head -n1` ou `sed -n '1p'`.

2. **Ligne 31** : `[ "$count" -gt 0 ] 2>/dev/null` — si count est vide, `[ "" -gt 0 ]` génère une erreur bash (integer expression expected) mais `2>/dev/null` la masque → le test échoue → warning. Fonctionnel mais pas propre.

3. **Ligne 44** : `date -r "$mtime"` — si mtime = 0 (stat échoue), `date -r 0` donne 1970-01-01 → message trompeur. Ajouter un test `[ "$mtime" -gt 0 ]`.

### Recommandations concrètes

**Modifications à apporter (non bloquantes mais recommandées) :**

```bash
# Ligne 14-15 : remplacer echo par printf
budget=$(printf '%s\n' "$vals" | head -n1)
reserve=$(printf '%s\n' "$vals" | tail -n1)

# Ligne 31 : ajouter test de non-vide
if [ -n "$count" ] && [ "$count" -gt 0 ] 2>/dev/null; then

# Ligne 44 : vérifier mtime > 0 avant date
if [ "$mtime" -gt 0 ] 2>/dev/null; then
  date_str=$(date -r "$mtime" "+%Y-%m-%d %H:%M" 2>/dev/null || echo "récemment")
else
  date_str="date inconnue"
fi
```

**Message R3 amélioré** (distinguer les cas) :
```bash
if [ "$verdict" = "OK" ]; then
  ok "préchauffage réserve OK ($date_str)"
elif [ "$verdict" = "KO" ]; then
  warn "préchauffage réserve KO — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
else
  warn "préchauffage réserve verdict inconnu ($verdict) — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
fi
```

### Verdict final

**GO AVEC RÉSERVES** — le bloc est intégrable tel quel, fonctionnel, non fatal, et respecte la spec. Les réserves sont des améliorations de robustesse (gestion des floats, messages plus précis) qui ne bloquent pas l'intégration. Le risque principal est le `pipefail` avec `echo | head`, mais en pratique `echo` ne devrait pas échouer sur des valeurs numériques.

**Intégration immédiate possible** avec les 3 modifications mineures ci-dessus pour une robustesse maximale.
