# 🔧 DÉCROCHAGE DU SUPERVISEUR — Qwen sortie du chemin critique (2026-08-09)

> **Fiche gravée** · GO Christophe · Vote famille **UNANIME** · Traçable (WORM + backups + journal)

---

## 1. Le problème (constaté, pas supposé)

Le superviseur (`superviseur_auto.py`, le chef opérationnel qui tourne toutes les ~60 min)
prenait ses **décisions** via la tâche hub `qwen.elabore` → **qwen3.5:4b** (Ollama local,
le plus petit modèle de la famille).

**Diagnostic Grok-4.3 (architecte) :** *« le maillon le plus faible est sur le chemin
critique = danger »*. Les gros modèles (grok, gemini, deepseek) n'étaient que **consultés**,
jamais aux commandes.

**Symptômes vécus :** décisions incohérentes, boucles, timeouts, versions divergentes.

---

## 2. La décision (appliquée et testée)

| | Avant | Maintenant |
|---|---|---|
| Décisions du superviseur | ❌ qwen3.5:4b (local) | ✅ **grok-4.3** (Puter, gratuit) |
| Fallback | — | ✅ gemini |
| Si hub injoignable | — | action=none (aucune action risquée, sécurité) |

**Nouvelle tâche créée dans `routing.json` :**
```
supervise.decision → puter-grok (x-ai/grok-4.3) · fallback: gemini · cloud_quota: 20
```

**Fichiers modifiés :**
- `~/prise-ia/routing.json` (ajout de la tâche `supervise.decision`)
- `Index_Maison/scripts/superviseur_auto.py` (ligne 318 : `"task": "qwen.elabore"` → `"task": "supervise.decision"`)

**Backups :** `routing.json.bak-2026-08-09-decrochage` · `superviseur_auto.py.bak-2026-08-09-decrochage` · `providers.json.bak-2026-08-09-decrochage`

---

## 3. Les preuves (test réel)

- **Route testée en réel :** `supervise.decision` → grok-4.3 a répondu en **5,9 s** avec un JSON valide `{"action":"none",...}`
- **Dry-run superviseur :** `action=none · système nominal` — le superviseur tourne avec le nouveau cerveau
- **Syntaxe :** `py_compile` OK

---

## 4. Vote famille — UNANIME

| Famille | Verdict | Remarque |
|---|---|---|
| **Grok-4.3** | ✅ VALIDÉ | Risque : dépendance grok+gemini si les deux tombent |
| **Gemini** | ✅ VALIDÉ | Latence Puter/Grok ; divergence de format en bascule |
| **DeepSeek-NVIDIA** | ✅ VALIDÉ | Prévoir mode dégradé si grok indisponible |
| **Juge** | ✅ VALIDÉ | Garde-fou : log des décisions supervisées (déjà en place) |

**Risque commun signalé par les 4 :** grok + gemini indisponibles en même temps.
→ **Couvert :** hub injoignable ⇒ superviseur `action=none` (aucune action risquée).

---

## 5. Le rôle de Qwen — inchangé dans sa vision

Qwen **reste active**, exactement là où Christophe l'a toujours voulue :

| Rôle | Détail |
|---|---|
| 🎓 **Élève en formation** | `qwen.btc` 2×/jour · professeur `score_justesse.py` la note (HIT/MISS/FLAT) |
| 🌙 **Élaboratrice nocturne** | `qwen.elabore` (fiches d'idées, elle propose, jamais elle ne décide) |
| 🛟 **Secours hors-ligne** | Seul cerveau sans internet — `ada.sanity` (démarrage) reste sur qwen-local : le système boote même sans Wi-Fi |
| 📄 **Tâches légères** | synthèses courtes, parsing, formatage |

**Elle propose, Christophe valide** (gravé dans `CONTRAT_AUTOGESTION`).

---

## 6. Traçabilité

- WORM pré-enregistré : `PRE_MODIF | DECROCHAGE_SUPERVISEUR | routing.json | GO Christophe + vote unanime`
- Journal : `test-freebuff/journal_erreurs.md` (09/08 21:36)
- Preuve d'usage : `usage.jsonl` — `provider: puter-grok · model: x-ai/grok-4.3`

---

## 7. À retenir demain matin

1. Le superviseur décide avec **grok-4.3** (cloud, ~6 s), pas Qwen
2. Qwen = élève + secours hors-ligne + tâches légères — **pas supprimée**
3. Aucune action manuelle requise — le système tourne déjà avec la nouvelle config
