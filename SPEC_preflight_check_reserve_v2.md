# SPEC — PREFLIGHT CHECK RÉSERVE STORM — v2 (micro-robustesse)

## Contexte

La v1 a été auditée par la famille. Verdict : **GO / GO AVEC RÉSERVES mineures** (JUGE = GO sans réserve, DEEPSEEK et ULTRA = GO avec 3 micro-corrections convergentes). Le bloc est intégrable, mais on applique les corrections de robustesse demandées par la famille avant l'intégration.

## Corrections à apporter (3, toutes convergentes DEEPSEEK + ULTRA)

### C1 — Extraction budget/réserve : `printf` au lieu de `echo` (DEEPSEEK)
Avec `set -o pipefail` dans le preflight, `echo "$vals" | head -n1` peut théoriquement planter. Remplacer par :
```bash
budget=$(printf '%s\n' "$vals" | head -n1)
reserve=$(printf '%s\n' "$vals" | tail -n1)
```

### C2 — Test count non-vide (DEEPSEEK)
`[ "$count" -gt 0 ]` échoue si count est vide. Sécuriser :
```bash
if [ -n "$count" ] && [ "$count" -gt 0 ] 2>/dev/null; then
```

### C3 — R3 robuste : stat multi-OS + mtime > 0 + messages distincts (ULTRA)
1. stat macOS avec repli Linux (le bloc doit fonctionner sur macOS ET ne pas crasher ailleurs) :
```bash
mtime=$(stat -f %m ~/prise-ia/prechauffage_reserve.json 2>/dev/null || stat -c %Y ~/prise-ia/prechauffage_reserve.json 2>/dev/null || echo 0)
```
2. Date uniquement si mtime > 0 :
```bash
if [ "$mtime" -gt 0 ] 2>/dev/null; then
  date_str=$(date -r "$mtime" "+%Y-%m-%d %H:%M" 2>/dev/null || echo "récemment")
else
  date_str="date inconnue"
fi
```
3. Distinguer les 3 cas de R3 (verdict != OK / trop ancien / absent) :
```bash
if [ "$verdict" = "OK" ]; then
  ok "préchauffage réserve OK ($date_str)"
else
  warn "préchauffage réserve verdict=$verdict — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
fi
```
et le cas trop ancien (>24h) avec message dédié, et le cas absent avec message dédié.

## RÈGLES ABSOLUES (inchangées)

1. Bash macOS, non fatal (warn ne bloque jamais), helpers `ok()`/`warn()` existants.
2. Position : bloc inséré AVANT `# --- Ruby ---` (ligne 168 de `scripts/preflight_ace777.sh`).
3. Ne pas toucher au reste du preflight.
4. R1, R2, R4 de la v1 restent identiques (seule R3 change + les 2 micro-fixes C1/C2).

## CONTRAT DE SORTIE

Le bloc shell COMPLET à insérer (v1 corrigée), prêt à copier-coller, avec la position d'insertion (avant `# --- Ruby ---`). Commentaires en français.

## ANNEXE — BLOC v1 (base à corriger)

Voir `CODE_preflight_check_reserve_v1.md` (le bloc de référence). Seuls les points C1, C2, C3 changent.
