# SPEC — Relance 4H : reset d'harmonie duo + STOP sur double mort

**Date :** 2026-08-14 · **Auteur :** Buffy (superviseur) · **Circuit :** famille 6/6 (diagnostic) → JUGE valide → codeur → grille → famille → GO Christophe → retest
**Règle d'or :** champion genesis **INTANGIBLE** — on ne modifie QUE les lanceurs (wrapper). Backups datés avant chaque modif. 1 GO = 1 vol.

---

## 1. La constatation (faits vérifiés — famille 6/6, `AUDIT_RUN_DUO_2026-08-14/`)

- **Correctif anti-mort (safe_call, genesis `d6977337`) : VALIDÉ** — plus aucun crash silencieux technique. Les arrêts sont des **sorties métier propres** (rc=1 volontaire) : BETA `shock_inversion_stop` (ligne 2287 genesis) → ALPHA `duo stale_state` (TTL 20s) → mort en chaîne **relationnelle**, pas technique.
- **Nouveau problème (5/6, thèse Christophe « la relance n'a pas l'harmonie »)** : la relance auto 4H (`launch_vortex_v2_collab_4h_binance.sh`, boucle `while true` + `sleep 5`) redémarre les bots **sans resynchroniser le contrat duo**. Preuve : session #2, ALPHA voit des tensions 1.5-6.03 mais bloque en `no_trigger`/`no_state` pendant 130+ cycles, zéro fill ; BETA micro-trades plats (`exit=62861.20` = même prix).
- Le simple `rm -f duo_state.json duo_session.json` (GEMINI_TEST ligne 66) laisse une **fenêtre de race** : le nouveau ALPHA peut lire un état résiduel / TTL périmé du SCOUT mort → désynchronisation dès le boot.

## 2. Correctif demandé (borné — lanceurs UNIQUEMENT, JAMAIS genesis)

**Cible : `launch_vortex_v2_collab_4h_binance.sh` (boucle de relance, lignes 53-82) et `GO_VORTEX_V2.sh` (point d'entrée).** Aucune modif de genesis, aucun changement du comportement nominal (session #1 = identique).

### 2.1 — Reset d'harmonie ATOMIQUE avant chaque session (remplace le `rm -f` seul)

Créer une fonction `reset_duo_harmony()` dans `GO_VORTEX_V2.sh` (avant `exec launch_vortex_v2_collab_4h_binance.sh`) et l'appeler **au début de CHAQUE itération de la boucle** (`launch_vortex_v2_collab_4h_binance.sh` ligne 55, juste après `attempt=$((attempt + 1))`) :

```bash
# RESET HARMONIE DUO (14/08, SPEC famille 6/6) : état INIT/RESET explicite
# au lieu d'un rm -f seul -> élimine la race window (ALPHA lisant un état
# SCOUT résiduel / TTL périmé). Bash 3.2. Zéro impact session propre.
reset_duo_harmony() {
  local sd="${RUN_DIR:-runs}/duo_state.json"
  local ss="${RUN_DIR:-runs}/duo_session.json"
  rm -f "$sd" "$ss" 2>/dev/null || true
  # état neutre écrit AVANT spawn : ALPHA ne peut plus lire un résidu
  mkdir -p "${RUN_DIR:-runs}" 2>/dev/null || true
  echo '{"role":"INIT","status":"RESET","ts_ms":0}' > "$sd" 2>/dev/null || true
  echo '{"run_state":{"current_tier":13,"start_ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","last_cycle":0,"total_pnl_snapshot":0.0},"roles":{},"total_pnl":0.0}' > "$ss" 2>/dev/null || true
  sync 2>/dev/null || true
}
```

### 2.2 — STOP si double mort en chaîne (ne pas relancer sur un marché mort)

Dans la boucle (`launch_vortex_v2_collab_4h_binance.sh`, après la ligne 66 `rc=$?`) : détecter la **signature de mort duo** et poser un STOP au lieu de relancer :

```bash
# DOUBLE MORT DUO (14/08, SPEC famille) : si la session est morte avec la
# signature duo (BETA shock + ALPHA stale dans la même session), on NE relance
# PAS en boucle sur un marché sans harmonie -> STOP propre + rapport.
if [ -f "$RUN_DIR/PROCESS_EXIT.log" ] && \
   grep -q "BETA_X5.*rc=1" "$RUN_DIR/PROCESS_EXIT.log" && \
   grep -q "ALPHA_X13_BURST13.*rc=1" "$RUN_DIR/PROCESS_EXIT.log"; then
  last_beta="$(grep "BETA_X5" "$RUN_DIR/PROCESS_EXIT.log" | tail -1)"
  last_alpha="$(grep "ALPHA_X13_BURST13" "$RUN_DIR/PROCESS_EXIT.log" | tail -1)"
  if [ -n "$last_beta" ] && [ -n "$last_alpha" ]; then
    tb="$(echo "$last_beta" | awk '{print $1}')"
    ta="$(echo "$last_alpha" | awk '{print $1}')"      # si les 2 morts sont dans les 300 dernières secondes -> double mort duo
      # (reserve JUGE 14/08 : rescue + repli si format ISO inattendu)
      if [ "$(ruby -rtime -e 'begin; a=Time.parse(ARGV[0]); b=Time.parse(ARGV[1]); puts ((a-b).abs<=300 ? "1" : "0"); rescue; puts "0"; end' -- "$tb" "$ta" 2>/dev/null || echo "0")" = "1" ]; then
      echo "=== DOUBLE MORT DUO détectée ($tb / $ta) — STOP, pas de relance. ==="
      touch STOP STOP_ALPHA STOP_BETA 2>/dev/null || true
      break
    fi
  fi
fi
```

**Contraintes :** bash 3.2 macOS (pas de `mapfile`, pas de `${var^^}`, pas de `date -d`) · `ruby` dispo (déjà utilisé dans le script) · zéro changement du comportement nominal (session qui se termine bien / STOP manuel = inchangé) · commentaires concis en français · ne toucher **que** ces 2 lanceurs, **jamais** `genesis_manifest.txt`.

## 3. CLAUSE PERMANENTE — PROUVER LA MEILLEURE LOGIQUE (Christophe, 14/08)

> « Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible. »

Le codeur doit **prouver** que ce correctif est la meilleure logique (vs alternatives : `rm -f` seul / état vide `{}` / sleep avant spawn / désactiver l'auto-relance) — et peut proposer UNE amélioration **prouvée** (mesurable, bornée, sans effet de bord). Rien au-delà de la SPEC.

## 4. Grille de test (tiers, pas le codeur)

| # | Test | Résultat attendu |
|---|------|------------------|
| 1 | `bash -n` sur les 2 lanceurs modifiés | 0 erreur |
| 2 | `reset_duo_harmony` en CLI | duo_state.json = `{"role":"INIT","status":"RESET","ts_ms":0}`, duo_session = vierge, sync OK |
| 3 | Signature double mort (simulation : 2 lignes PROCESS_EXIT proches) | STOP posé, pas de relance |
| 4 | Session propre se termine (rc=0) | PAS de STOP (comportement nominal intact) |
| 5 | Retest réel | ALPHA trigger dès tension > 2 (1 fill) OU double mort → STOP propre (pas de boucle stérile) |

## 5. Contrat de sortie
1. Patch complet (fonction + 2 points d'insertion) dans `GO_VORTEX_V2.sh` + `launch_vortex_v2_collab_4h_binance.sh`, backups `.BAK_avant_reset_duo_<ts>`.
2. Preuve « meilleure logique » (section obligatoire).
3. Grille 1-4 passée en machine.
4. Rien d'autre — pas de réécriture, pas de feature, genesis intouché.

**Documents liés :** `AUDIT_RUN_DUO_2026-08-14/` (6 avis) · `SPEC_correction_panne_alpha_v3.md` (correctif anti-mort validé) · `runs/CRASH_DUMP_*_20260814_*.log` (preuves) · `runs/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log` (cycles réels)
