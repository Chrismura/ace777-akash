# RÉPONSE CODEUR (task code.ia · Puter Grok (gratuit)) — 2026-08-14T08:09:47.498269Z

**Code patch (prêt à insérer dans `genesis_manifest.txt`)**

```bash
# ANTI-MORT SILENCIEUSE (14/08, SPEC v2) — helper unique
safe_call() {
  local rc=0
  "$@" 2>>/tmp/ace777_stderr_debug.log || rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "[WARN safe_call rc=$rc] $*" >> /tmp/ace777_fatal_rc1.log 2>/dev/null || true
  fi
  return 0
}
```

**Encapsulations (zones listées) — transformations exactes :**

```bash
# Lignes ~1600/1614
p1="$(safe_call as_num "$(safe_call json_get "$p1_resp" "price")")"
p2="$(safe_call as_num "$(safe_call json_get "$p2_resp" "price")")"

# Lignes ~1734/1735
bid_px="$(safe_call as_num "$(safe_call json_get "$book" "bid")")"
ask_px="$(safe_call as_num "$(safe_call json_get "$book" "ask")")"

# Lignes ~2057/2061/2071/2109/2142
entry="$(safe_call calc_entry "$(safe_call json_get "$resp" "price")")"
px="$(safe_call as_num "$(safe_call json_get "$tick" "price")")"
px_confirm="$(safe_call as_num "$(safe_call json_get "$confirm" "price")")"

# Ligne 2431
exit_price="$(safe_call as_num "$(safe_call json_get "$exit_resp" "price")")"

# Ligne 781 + radar helpers (si substitution directe)
trend="$(safe_call trend_bps_from_klines "$klines")"
vortex="$(safe_call vortex_radar_clamp "$val")"
bps="$(safe_call bps_change "$a" "$b")"
absv="$(safe_call abs_num "$x")"

# Ligne 1992
raw="$(safe_call llm_raw "$prompt")"
```

**Backup avant modification (à exécuter manuellement) :**
```bash
cp genesis_manifest.txt genesis_manifest.txt.BAK_avant_safe_call_$(date +%s)
```

---

**PREUVE — Meilleure logique (vs alternatives)**

`|| true` brut sur la substitution entière masque l’erreur sans log ni distinction, rendant le débogage impossible et violant la traçabilité exigée. Le sous-shell `(…)` crée un nouveau contexte qui ne propage pas correctement les variables locales ni les `set -e` attendus dans le shell parent. L’injection dans le lanceur (Option B) a été rejetée car le moteur est dans `genesis_manifest.txt` (2517 lignes intangibles).  

`safe_call` est la seule solution qui :
- force rc=0 pour `set -e` (survie du sous-shell),
- logge uniquement les échecs (zéro trace en nominal),
- reste compatible bash 3.2 (pas de `mapfile`, pas de tableaux associatifs),
- n’altère aucun comportement quand le helper ruby réussit.

C’est donc la correction minimale et la plus sûre.

**Amélioration prouvée (UNE, mesurable, sans effet de bord)**

Ajout d’un compteur atomique optionnel dans `safe_call` (seulement si `SAFE_CALL_COUNT=1`) :

```bash
[ -n "${SAFE_CALL_COUNT:-}" ] && echo "1" >> /tmp/ace777_safe_call.count || true
```

Mesurable : `wc -l /tmp/ace777_safe_call.count` donne le nombre exact d’appels après run. Zéro impact nominal (variable non positionnée par défaut). Borné à cette fonction.
