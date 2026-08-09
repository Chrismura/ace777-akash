# 🛡️ GARDE-FOUS MÉCANIQUES BUFFY — 09/08/2026 (implémentation post-jugement)

> **Demande de Christophe (GO 09/08) :** implémenter les 3 garde-fous mécaniques exigés par la famille (jugement : GARDER AVEC GARDE-FOUS).
> **Processus respecté (loi 1quinquies) :** Ada a SPECIFIÉ → **Gemini a écrit le code via le hub** → Ada a vérifié (checker) → **audit tiers famille différente (DeepSeek)** → réserves appliquées → testé.

---

## ✅ Les 3 garde-fous — écrits par Gemini, vérifiés par Ada, audités par DeepSeek

| # | Garde-fou | Fichier | Répond à la faille |
|---|---|---|---|
| 1 | **Gatekeeper bloquant** : preuve de lecture coffre `[LECTURE_COMPLETE_OK]` < 24h obligatoire ; **bloque `verifier_setup.py` (exit 1)** si périmée | `scripts/gatekeeper.py` + intégré à `verifier_setup.py` | « Je réponds sans lire le coffre » (5×) |
| 2 | **Anti code solo** : audite les 40 scripts, traque les en-têtes d'auteur, produit `CODE_AUTHORS.md` ; **exit 1 si des scripts n'ont pas d'auteur** | `scripts/no_solo_code.py` | « Je code en solo avec des bugs » |
| 3 | **Heartbeat 1h** : surveille graph (< 30h), git (< 4h), hub /health, Qwen (ne stagne pas), RAM (< 60% warn, < 15% critique) ; **PAUSE_ORCHESTRATRICE auto si 2 runs critiques** | `scripts/heartbeat.py` + launchd `com.ace777.heartbeat` (1h) | « Chaque "ça ne bouge pas" = maillon manquant » |

---

## 🔍 Corrections du CHECKER (Ada) après le MAKER (Gemini) — 2 bugs réels attrapés
1. **Gatekeeper + no_solo_code** : cherchaient la *dernière ligne* de MEMOIRE_COLLAB au lieu de la *plus récente* (les entrées récentes sont EN HAUT) → corrigé : MAX des timestamps.
2. **no_solo_code** : la regex cherchait l'horodatage en début de ligne, mais les lignes commencent par `|` → corrigé.

**Et mon erreur révélée par le test :** ma propre preuve de lecture du 09/08 12:57Z n'avait PAS le tag machine `[LECTURE_COMPLETE_OK]` — regravée avec le tag exact (13:18Z). Ironie : c'est exactement la loi que je devais respecter.

## 🔍 Réserves de l'audit tiers (DeepSeek, famille ≠ Gemini) — appliquées
| Réserve | Action |
|---|---|
| Seuil RAM 15 % trop laxiste | **60 % = alerte**, 15 % = critique |
| no_solo_code constate sans corriger | **exit 1 si scripts sans auteur** (blocage pipeline) |
| Gatekeeper contournable / passive | **verifier_setup.py s'arrête (exit 1)** si preuve périmée — bloquant, pas signalant |

## 🧪 Tests réels
- `gatekeeper.py` → exit 0, « OK preuve fraîche (0,1h) »
- `verifier_setup.py --no-famille` → **tout vert, exit 0** (gatekeeper en tête)
- `heartbeat.py --status` → graph 1h · git 0,04h · hub OK · RAM 81 % · pause False
- `no_solo_code.py audit` → 3 scripts avec auteur / 37 sans (liste ALERTE) — le rapport `CODE_AUTHORS.md` est créé

---

*Références : RAPPORT_DEFAILLANCES_BUFFY_2026-08-09.md · JUDGEMENT_BUFFY_2026-08-09/ · CONTRAT_AUTOGESTION (1quater, 1quinquies, 1septies) · MEMOIRE_COLLAB (preuves 12:57Z + 13:18Z)*
