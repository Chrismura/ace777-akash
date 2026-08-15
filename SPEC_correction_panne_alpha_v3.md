# SPEC v3 — Correction panne ALPHA rc=1 (diff EXACT, lignes vérifiées)

**Date :** 2026-08-14 · **Auteur :** Buffy (superviseur) · **Circuit :** famille 6/6 (cible A tranchée) → codeur → grille → famille (validation patch) → GO Christophe → retest
**Pourquoi v3 :** les 2 livrables codeur (v1, v2) étaient de la fiction (variables/clés JSON inventées : `$book`, `calc_entry`, `"bid"` au lieu de `"bidPrice"`). Cette SPEC donne les lignes **EXACTES** lues dans `genesis_manifest.txt` (vérifiées superviseur) + la transformation précise. Le codeur ne doit RIEN inventer : il recopie le diff ci-dessous tel quel, sans renommer, sans réécrire.

---

## 1. La panne (résumé)

ALPHA meurt rc=1 ~8-13 min après départ, juste après un fill. FATAL_RC1 vide (trap ERR ne se propage pas dans les substitutions sous set -e). Mécanisme famille 6/6 : helpers ruby dans substitutions `$(…)` qui sortent rc≠0 → mort silencieuse. Cible : Option A (ajout minimal dans genesis + re-scellement).

## 2. Diff EXACT à appliquer (une ligne → une ligne, rien d'autre)

**Étape 1 — Helper unique** (insérer juste après `public_get() { curl_with_retry "$BASE_URL$1"; }`, ligne 717) :
```bash
# ANTI-MORT SILENCIEUSE (14/08, SPEC v3) : neutralise l'echec d'un helper ruby
# dans une substitution sous set -e. Log + repli vide. Bash 3.2. Rien en nominal.
safe_call() {
  local rc=0
  "$@" 2>>/tmp/ace777_stderr_debug.log || rc=$?
  if [ "$rc" -ne 0 ]; then
    echo "[WARN safe_call rc=$rc] $*" >> /tmp/ace777_fatal_rc1.log 2>/dev/null || true
  fi
  return 0
}
```

**Étape 2 — Les 10 lignes (copie EXACTE old → new, vérifiées à l'instant) :**

| Ligne | AVANT (exact) | APRÈS (exact) |
|---|---|---|
| 1600 | `  p1="$(as_num "$(json_get "$p1_resp" "price")")"` | `  p1="$(safe_call as_num "$(safe_call json_get "$p1_resp" "price")")"` |
| 1614 | `  p2="$(as_num "$(json_get "$p2_resp" "price")")"` | `  p2="$(safe_call as_num "$(safe_call json_get "$p2_resp" "price")")"` |
| 1734 | `  bid_px="$(as_num "$(json_get "$book_resp" "bidPrice")")"` | `  bid_px="$(safe_call as_num "$(safe_call json_get "$book_resp" "bidPrice")")"` |
| 1735 | `  ask_px="$(as_num "$(json_get "$book_resp" "askPrice")")"` | `  ask_px="$(safe_call as_num "$(safe_call json_get "$book_resp" "askPrice")")"` |
| 2057 | `    entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"` | `    entry_price="$(safe_call as_num "$(safe_call json_get "$entry_resp" "avgPrice")")"` |
| 2061 | `    px_confirm="$(as_num "$(json_get "$tick_confirm" "price")")"` | `    px_confirm="$(safe_call as_num "$(safe_call json_get "$tick_confirm" "price")")"` |
| 2071 | `          entry_price_2="$(as_num "$(json_get "$entry_resp2" "avgPrice")")"` | `          entry_price_2="$(safe_call as_num "$(safe_call json_get "$entry_resp2" "avgPrice")")"` |
| 2109 | `    entry_price="$(as_num "$(json_get "$entry_resp" "avgPrice")")"` | `    entry_price="$(safe_call as_num "$(safe_call json_get "$entry_resp" "avgPrice")")"` |
| 2142 | `    px="$(as_num "$(json_get "$tick_resp" "price")")"` | `    px="$(safe_call as_num "$(safe_call json_get "$tick_resp" "price")")"` |
| 2431 | `    exit_price="$(as_num "$(json_get "$exit_resp" "avgPrice")")"` | `    exit_price="$(safe_call as_num "$(safe_call json_get "$exit_resp" "avgPrice")")"` |

**Étape 3 — `trend_bps_from_klines` (définition ligne 781)** : la fonction a déjà `exit 0` sur les chemins d'erreur → **PAS de modification** sauf si un appel en substitution directe est trouvé (le codeur doit le vérifier et ne proposer QUE s'il existe, avec la ligne exacte).

**Étape 4 — `llm_raw` (1990-1995)** : DÉJÀ protégé (`|| llm_curl_ok=$?` + `2>/dev/null`) → **PAS de modification**. Ne pas y toucher.

**Étape 5 — `num_*` (675-684) en substitution directe** : vérifier les occurrences `$(num_…` utilisées comme commande d'assignation (hors `if`) ; proposer la protection UNIQUEMENT pour celles-là, avec ligne exacte.

## 3. Règles d'or pour le codeur (obligatoires)

1. **NE RIEN INVENTER** : recopier le diff ci-dessus tel quel. Pas de renommage (`$book_resp` reste `$book_resp`, `"bidPrice"` reste `"bidPrice"`). Pas de nouvelle fonction (`calc_entry` n'existe pas — ne pas la créer).
2. Répondre avec le **bloc final complet prêt à insérer** = helper + les 10 lignes + éventuels ajouts justifiés (avec ligne exacte vérifiée).
3. Vérifier `bash -n` sur la version modifiée avant de répondre (ou au minimum ré-écrire les lignes telles quelles).
4. Backup : `cp genesis_manifest.txt genesis_manifest.txt.BAK_avant_safe_call_$(date +%s)` (exécuté par le superviseur avant insertion, PAS par le codeur).

## 4. Grille de test (tiers)

| # | Test | Résultat attendu |
|---|------|------------------|
| 1 | `bash -n genesis_manifest.txt` (après patch) | 0 erreur |
| 2 | `safe_call false` en CLI | rc 0, warning loggé |
| 3 | `safe_call json_get "" "price"` | rc 0, pas de mort |
| 4 | Retest GEMINI_TEST + crash dump | **ALPHA survit > 10 min / fill #50** (indicateur GROK) |
| 5 | Champion re-scellé, md5 à jour | Nouveau md5 = références mises à jour |

## 5. Contrat de sortie
1. Bloc final complet (helper + diff exact) — **aucune invention**.
2. Confirmation que les lignes 2057/2109 (doublons `entry_price`) sont bien 2 occurrences distinctes à transformer (vérifiées : oui, lignes différentes).
3. Rien d'autre.

**Documents liés :** `AUDIT_CIBLE_CORRECTION_2026-08-14/` · `SPEC_correction_panne_alpha_v2.md` · `CODE_correction_panne_alpha_v2.md` (patch fiction, rejeté)
