# SPEC v2 — Correction panne ALPHA rc=1 (mort silencieuse par helpers ruby)

**Date :** 2026-08-14 · **Auteur :** Buffy (superviseur) · **Circuit :** famille 6/6 (cible tranchée) → codeur → grille → famille (validation patch) → GO Christophe → retest
**Décision famille 6/6 (`AUDIT_CIBLE_CORRECTION_2026-08-14/`) : Option A** — ajout minimal dans `genesis_manifest.txt` + **re-scellement du champion** (précédent du trap ligne 90 → `af307996`, validé 6/6).

---

## 1. La panne (faits vérifiés — 2 rounds famille)

- ALPHA meurt en rc=1 à **07:49:10Z** (~8 min après départ, juste après le fill #42), 14/08. Pattern identique au 13/08. BETA survit. FATAL_RC1 **VIDE** (le trap ERR ligne 90 ne se propage pas dans les sous-shells / substitutions `$(…)`).
- **Mécanisme (unanimité famille, confirmé superviseur)** : `public_get`/`curl_with_retry` sont DÉJÀ protégés (retournent 0, `|| true` présent). Le tueur = **helpers ruby non protégés dans des substitutions imbriquées** qui sortent en rc≠0 (TypeError ruby sur JSON vide/invalide, clé absente, argument vide) → sous `set -e`, la substitution échoue → mort silencieuse du sous-shell.
- Structure : tout le code moteur est dans `genesis_manifest.txt` (2517 lignes, INTANGIBLE — mais re-scellable, précédent validé). Le lanceur (269 lignes) ne fait que `tail -n +85 genesis | bash -s`.

## 2. Correctif demandé (borné — Option A famille, re-scellement)

**Ajout minimal dans `genesis_manifest.txt`** (champion → re-scellé après patch, backups datés AVANT toute modif) :

1. **Helper unique** `safe_call` (ou `safe_eval`) injecté dans la section helpers (~ligne 690, à côté de `curl_with_retry`) :
```bash
# ANTI-MORT SILENCIEUSE (14/08, SPEC v2 famille 6/6) : neutralise l'échec d'un
# helper ruby dans une substitution sous set -e. Log + repli 0. Bash 3.2.
safe_call() {
  local rc=0
  "$@" 2>>/tmp/ace777_stderr_debug.log || rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "[WARN safe_call rc=$rc] $*" >> /tmp/ace777_fatal_rc1.log 2>/dev/null || true
  fi
  return 0
}
```
2. **Encapsuler UNIQUEMENT les helpers ruby** dans les substitutions (PAS les simples lectures locales — réserve JUGE) — les N zones :
   - Lignes **1600, 1614, 1734, 1735** (`p1`, `p2`, `bid_px`, `ask_px`)
   - Lignes **2057, 2061, 2071, 2109, 2142** (entry / px / px_confirm)
   - Ligne **2431** (`exit_price`)
   - `trend_bps_from_klines` (781) + `vortex_radar_clamp`/`bps_change`/`abs_num` si utilisés en substitution non protégée dans la boucle
   - `llm_raw` (1992) — vérifier la couverture
   - Transformation type : `p1="$(as_num "$(json_get "$p1_resp" "price")")"` → `p1="$(safe_call as_num "$(safe_call json_get "$p1_resp" "price")")"` (ou `|| echo "0"` simple si le helper est le dernier maillon).
3. **RE-SCELLEMENT** : après patch, mettre à jour les références md5 champion dans `preflight_ace777.sh`, `verif_pre_run_3x.sh`, `verif_setup_champion.sh`, `GO_VORTEX_V2.sh` (comme fait pour `af307996`).

**Contraintes :** bash 3.2 macOS (pas de `mapfile`, pas de `${var^^}`) · zéro changement du comportement nominal (helper OK → aucune trace) · commentaires concis en français · **backup daté de genesis AVANT modif** (`cp genesis_manifest.txt genesis_manifest.txt.BAK_avant_safe_call_<ts>`).

## 3. CLAUSE PERMANENTE — PROUVER LA MEILLEURE LOGIQUE (Christophe, 14/08)

> « Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible. »

Le codeur doit **prouver** que ce correctif est la meilleure logique (vs alternatives : `|| true` brut, sous-shell `(…)`, injection lanceur/Option B rejetée) — et peut proposer UNE amélioration **prouvée** (mesurable, bornée, sans effet de bord). Rien au-delà de la SPEC.

## 4. Grille de test (tiers, pas le codeur)

| # | Test | Résultat attendu |
|---|------|------------------|
| 1 | `bash -n genesis_manifest.txt` | 0 erreur syntaxe |
| 2 | `safe_call false` en CLI | rc 0, warning loggé, pas de mort |
| 3 | `safe_call json_get "" "price"` (JSON vide) | rc 0, repli, run continue |
| 4 | Retest (GEMINI_TEST + crash dump) | **ALPHA survit > 10 min / passe le fill #50** (indicateur GROK) |
| 5 | Vérif : champion re-scellé, md5 affiché | Nouveau md5 = référence mise à jour |

## 5. Contrat de sortie
1. Patch complet (helper + N zones) dans genesis, backups `.BAK_avant_safe_call_<ts>`.
2. Preuve « meilleure logique » (section obligatoire).
3. Grille 1-3 passée en machine.
4. **Re-scellement** : nouveau md5 affiché + listé (le champion change, prévenir Christophe).

**Documents liés :** `AUDIT_PANNE_2026-08-14/` · `AUDIT_CIBLE_CORRECTION_2026-08-14/` (6 avis) · `CODE_correction_panne_alpha.md` (patch inapplicable, placement corrigé) · `runs/CRASH_DUMP_ALPHA_X13_BURST13_20260814_074910.log`
