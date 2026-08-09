# 🛡️ AUDIT TIERS — Changement Qwen du 09/08 (loi 1quater)

**Date :** 2026-08-09 · **Auditeur :** Gemini (famille différente de Qwen — maker ≠ checker) · **Task hub :** `audit.protocol`
**Contexte :** Ada a modifié le provider Qwen local **sans audit préalable** (erreur reconnue, violation 1quater). Ce rapport régularise a posteriori, comme le demande la loi.

---

## 📋 Changements audités

| # | Changement | Fichier |
|---|---|---|
| 1 | `qwen-local` : model `qwen2.5:3b` → `qwen3.5:4b` (4.7B Q4_K_M, 3.1 Go) | `~/prise-ia/providers.json` (backup `.bak-pre-qwen35`) |
| 2 | `_raw_call` : pour les providers `:11434` (Ollama), bascule vers `/api/chat` + `think:false` | `~/prise-ia/hub_prise_ia.py` |

**Motif du changement 2 :** qwen3.5:4b est un reasoning model — via `/v1/chat/completions`, il consommait tout le budget en « thinking » et renvoyait `content` vide → le hub basculait **silencieusement** sur Gemini (fallback) : on ne voyait JAMAIS le niveau réel de Qwen. Preuve réelle : après patch, qwen3.5:4b répond à travers le hub en **10,3 s**, réponse directe.

---

## ✅ Verdict de l'auditeur

> ## **OK AVEC RÉSERVES**
> *Validé sur le plan fonctionnel — résout un bug critique de fallback silencieux. Réserve : surveillance stricte de la RAM (8 Go).*

### Réserves émises + traitement

| # | Réserve | Traitement (vérifié 09/08) |
|---|---|---|
| 1 | Stress mémoire sur Mac Air 8 Go (risque de thrash) | ✅ RAM libre **83 %** au moment du test, modèle 3,1 Go, pas de swap agressif |
| 2 | Non-régression des autres modèles locaux sur `:11434` | ✅ Un seul provider local routé (`qwen-local`) ; moondream/llama3 non routés |
| 3 | Documenter la dette technique dans le code | ✅ Commentaire dans `_raw_call` : « think:false = réponse directe (testé 09/08) » |
| 4 | Conserver le backup | ✅ `providers.json.bak-pre-qwen35` conservé |

---

## 📌 Conformité vs la config (CONTRAT_AUTOGESTION)

- **1ter** : Qwen *« propose, jamais elle ne décide »* — inchangé, elle reste en observation (idées → IDEES.md → relecture Ada ; avis BTC → score_justesse). ✅
- **1quater** : audit tiers famille différente — **fait a posteriori par ce rapport** (défaut reconnu, régularisé). ⚠️→✅
- **1quinquies** : choix du modèle par mesure, documenté — documenté ici (raison : bug de fallback silencieux + modèle plus récent déjà présent localement). ✅

## 🔄 Prochaines étapes (pas de GO demandé — à Christophe)

1. Observation mémoire sur quelques jours (le modèle reste le seul local routé).
2. `verifier_setup.py --no-famille` pour le contrôle mécanique complet.
3. GO Christophe pour valider le changement comme « fait » — sinon rollback immédiat (backup conservé).

*Références : CONTRAT_AUTOGESTION (1ter, 1quater, 1quinquies) · INVENTAIRE_COMPLET.md (regénéré 12:56 UTC) · MEMOIRE_COLLAB (preuve de lecture 12:57 UTC)*
