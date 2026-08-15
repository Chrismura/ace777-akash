# SPEC — Correction panne ALPHA rc=1 (mort silencieuse par sous-shell)

**Date :** 2026-08-14 · **Auteur :** Buffy (superviseur) · **Circuit :** JUGE valide la SPEC → codeur → grille → famille → GO Christophe → retest
**Règle d'or :** champion genesis **INTANGIBLE** — on ne modifie QUE le lanceur (wrapper). Backups datés avant chaque modif. 1 GO = 1 vol.

---

## 1. La panne (faits vérifiés — famille 6/6 consultée)

- Run test du 14/08 (GEMINI_TEST + crash dump, testnet) : **ALPHA meurt en rc=1 à 07:49:10Z**, ~8 min après le départ, juste après le fill #42. BETA survit. Même pattern que le 13/08.
- Fenêtre de mort : SKIP #43 (07:49:01) → **9 s de silence** → PROCESS_EXIT rc=1 (07:49:10).
- **FATAL_RC1 VIDE** → le trap ERR n'a pas écrit. Cause (unanimité famille) : sous `set -e`, le trap ERR **ne se propage pas** dans les sous-shells / substitutions `$(…)` / pipelines — un échec interne tue l'enfant sans remonter au shell qui porte le trap.
- **Zone fautive (unanimité)** : appels `public_get` / `curl_with_retry` **non protégés** dans des substitutions `$(…)` — lignes 1599-1615 (p1/depth_1/p2/depth_2) et 1733-1745 (book/klines), + helpers `json_get` (454) / `num_*` (677-684). Le timing 9 s = 3 tentatives × 5 s de `curl_with_retry`.

## 2. Correctif demandé (borné — wrapper, JAMAIS genesis)

Créer dans le **lanceur** (`launch_test_master_base_v8_5_impact.sh` et son jumeau `_GEMINI_TEST.sh`) une fonction wrapper qui **neutralise la mort sèche sous set -e** :

```bash
# SÉCURISATION ANTI-MORT SILENCIEUSE (14/08, SPEC validée famille)
# Neutralise l'échec d'un appel externe sous set -e : log + retour 0.
# NE change PAS le comportement nominal (appel réussi = identique).
safe_call() {
  local ec=0
  "$@" 2>>/tmp/ace777_stderr_debug.log || ec=$?
  if [ "$ec" -ne 0 ]; then
    echo "[WARN safe_call rc=$ec] $*" >> /tmp/ace777_fatal_rc1.log
  fi
  return 0
}
```

Puis **encapsuler les appels critiques** par `safe_call` ou suffixer les substitutions par `|| true` / `|| echo "{}"` :
- `p1_resp` / `depth_1` (1599-1601) · `p2_resp` / `depth_2` (1613-1615)
- `book_resp` (1733) · `tr` klines (1745)
- `json_get "$radar_out"` (1385-1388) et autres `json_get`/`num_*` dans la boucle de cycle
- `llm_raw` (1992) — déjà `|| llm_curl_ok=$?`, vérifier la couverture

**Contraintes :** bash 3.2 macOS (pas de `mapfile`, pas de `${var^^}`) · zéro changement du comportement nominal (rc=0 → aucun log de warning) · commentaires concis en français · ne toucher **que** le lanceur + helpers éventuels à côté, **jamais** `genesis_manifest.txt`.

**Réserve JUGE (14/08, validée) :** `safe_call` s'applique **uniquement aux appels réseau** (`curl_with_retry`, `public_get`) — **PAS** aux simples lectures locales de variables / logique pure, pour ne pas masquer une erreur fatale de logique.

## 3. CLAUSE PERMANENTE — PROUVER LA MEILLEURE LOGIQUE (demande Christophe, 14/08)

> **À chaque correction via la chaîne d'approbation (famille ET codeur) :**
> « Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible. »
> Le livreur (codeur) doit montrer QUE sa correction est la meilleure logique (pas juste une rustine),
> et proposer/appliquer une amélioration si elle est **prouvée** (mesurable, bornée, sans effet de bord).
> Rien n'est appliqué au-delà de la SPEC sans re-validation.

**Application dans cette SPEC :** au-delà du correctif de panne, le codeur doit **prouver** que `safe_call` est la meilleure logique (vs alternatives : `|| true` brut, sous-shell `(…)`, wrapper par ligne) — et peut proposer UNE amélioration prouvée (ex. la fenêtre de silence mesurée devient un log `[API durée]`, sans changer le comportement).

## 4. Grille de test (à exécuter AVANT tout retest — par un tiers, pas le codeur)

| # | Test | Résultat attendu |
|---|------|------------------|
| 1 | `bash -n` sur le lanceur modifié | 0 erreur syntaxe |
| 2 | `safe_call false` en CLI | rc global 0, warning loggé, pas de mort |
| 3 | `safe_call curl -sf URL_KO` | rc 0, warning, run continue |
| 4 | Reprise du run test (retest) | ALPHA survit ≥ 30 min OU mort avec **preuve** (ligne + commande) |
| 5 | Vérif : genesis md5 inchangé | `af307996…` toujours (rien touché) |

## 5. Contrat de sortie
1. Code complet du wrapper + zones encapsulées (patch dans le lanceur v8_5 ET GEMINI_TEST), backups `.BAK_avant_safe_call_<ts>`.
2. Preuve « meilleure logique » (section obligatoire dans la réponse).
3. Grille test 1-3 passée en machine.
4. Rien d'autre — pas de réécriture, pas de feature.

**Documents liés :** `AUDIT_PANNE_2026-08-14/` (6 avis) · `runs/CRASH_DUMP_ALPHA_X13_BURST13_20260814_074910.log` · `SPEC_correction_panne_alpha_v1.md`
