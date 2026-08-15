# VERDICT FAMILLE — Diagnostic moteur (revenge + shock_stop + tension stale)

**Date :** 2026-08-15 · **Avis :** 4/4 (gemini 85%, nvidia 78%, juge 78%, ultra 85%)

## Consensus (convergence 4/4)

1. **Infra d'abord** — E-STALE 1032 (`tension_stale age>800ms` = feed NUAGE qui lag 8-12s) + E-PROC 75 (workers qui meurent) **faussent les données et les décisions**. Le bot décide sur des prix « fantômes » → `shock_inversion_stop` artificiels → revenge déclenchés sur du bruit de latence. Corriger le revenge maintenant = optimiser sur données corrompues.
2. **Revenge = churn structurel probablement sans edge** — le %revenge monte (58→89%) alors que le marché est plus calme ; le PnL revenge est ultra-volatil (+51 le 14, −3.6 le 13, +0.9 le 15), le +51 du 14 masque une espérance non démontrée.
3. **Mesurer avant de toucher** — il manque : PnL net par **séquence complète** scout→hunter (frais inclus), hold moyen revenge vs normal, côté (long/short) du revenge vs scout, corrélation E-STALE/revenge.

## Améliorations convergentes (stacking functions)

- **Freeze/plafonner revenge** (`revenge_enabled=false` ou max 1x) le temps de corriger l'infra.
- **`latency_guard`** : bloquer toute entrée si `tension_stale_age > 500ms` ou `E-PROC > 10`.
- **`sequence_id`** (UUID partagé BETA→ALPHA) pour mesurer le PnL net séquentiel.
- **Superviseur process** : restart auto des workers + alerte latence > 800ms.
- **Compteur frais cumulés** dans les CSV (taker ×2/cycle, ~15-20% du PnL brut).

## Verdict

> **OUVRIR CHANTIER INFRA EN PREMIER** (stabiliser feed + workers), puis **audit des séquences BETA+ALPHA frais inclus**, **avant** toute modification de `revenge_mult` / `revenge_reasons`. Le revenge n'est pas prouvé perdant, mais il n'est pas prouvé gagnant non plus — il faut d'abord des données propres.

## Fichiers
- Avis : `AVIS_{gemini,nvidia,openrouter-juge,openrouter-ultra}.md` (ce dossier)
- Chiffres source : `Index_Maison/scripts/enquete_endormie_20260815.py`
