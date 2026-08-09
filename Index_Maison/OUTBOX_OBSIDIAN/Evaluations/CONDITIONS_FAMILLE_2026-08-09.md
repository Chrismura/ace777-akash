# 🛡️ LES 6 CONDITIONS FAMILLE — APPLIQUÉES — 2026-08-09 16:50Z

> GO Christophe après jugement famille (GARDER AVEC GARDE-FOUS RENFORCÉS).
> Processus 1quinquies respecté : Ada SPECIFIE → GEMINI écrit (4 scripts) → Ada checker (3 bugs macOS corrigés) → AUDIT TIERS = OK AVEC RÉSERVES → réserves appliquées.

## État final vérifié (verif_conditions.py)

| Condition | État | Preuve réelle |
|---|---|---|
| **C1** — Ada sans droits d'écriture | ✅ APPLIQUÉE | 20 fichiers critiques en **chmod 444** ; test : écriture directe → `Permission denied` |
| **C2** — Journal WORM immuable | ✅ APPLIQUÉE | `WORM_JOURNAL.log` **append-only (chflags uappnd)** ; 11 entrées ; append direct vérifié |
| **C3** — Preuve obligatoire | ✅ APPLIQUÉE | `preuve.py exiger --affirmation --cmd` → PREUVE OK journalisée (2 tests) |
| **C4** — Double signature | ✅ APPLIQUÉE | `gardien.py apply` REFUSE sans signature (test : « Erreur C4 signature manquante ») |
| **C5** — Sanction automatique | ✅ APPLIQUÉE | 0 violation ; ≥3 violations/7j → `PAUSE_ORCHESTRATRICE` auto |
| **C6** — Mode probatoire | ✅ APPLIQUÉE | `PROBATOIRE.json` (début 09/08, max 1 action/jour les 7 premiers jours) |

## La preuve que ça MARCHE (test d'intrusion volontaire)
J'ai modifié `integrite.py` **sans trace** → `integrite.py check` a détecté la modif → **VIOLATION journalisée**. Le harnais m'a attrapé moi-même. C'est exactement le comportement demandé.

## Réserves de l'audit tiers (documentées, pas cachées)
1. **Contournement possible si root** : `chmod +w` / `chflags nouappnd` par root contournerait la protection (limite macOS mono-utilisateur — pas de séparation OS réelle).
2. **La double signature repose sur la confiance dans le mécanisme de signature** (pas de crypto externe).
3. **Red teaming** : recommandé un test d'intrusion régulier (simuler une compromission).

## Fichiers livrés
- `scripts/gardien.py` — wrapper central (C1, C2, C4)
- `scripts/integrite.py` — base hash sha256 + détection modifs non tracées
- `scripts/preuve.py` — preuve machine obligatoire (C3)
- `scripts/verif_conditions.py` — état 6 conditions + sanctions (C5) + probatoire (C6)
- `FICHIERS_CRITIQUES.txt` — 20 fichiers protégés
- `WORM_JOURNAL.log` — journal append-only
- `PROBATOIRE.json` — mode probatoire
- `INTEGRITE_BASE.json` — base de référence

## Vérification par Christophe (10 secondes)
```
cd ~/ace777-test-day1/Index_Maison && python3 scripts/verif_conditions.py
→ 6 lignes APPLIQUEE + « Aucune sanction nécessaire »
```
