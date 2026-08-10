# 🔄 RÉ-INTRODUCTION QWEN-OLLAMA — Mode C6 (après fusion)

> **Décision famille + Christophe — 10/08/2026** : Qwen-Ollama (qwen3.5:4b) mis en **PAUSE RÉVERSIBLE** avant la fusion des services 27→13.
> Raison : le hub (nvidia, grok, gemini) fait ce travail mieux ; on fusionne d'abord, on teste (banc d'essai), on ré-introduit après.
> Verdict famille : **GO avec réserves** — toutes intégrées (voir `FAMILLE_PAUSE_QWEN_2026-08-10/`).

---

## ⏸️ CE QUI A ÉTÉ FAIT LE 10/08 (état actuel)

### 1. Services en pause (plists → DESACTIVES)
| Service | Rôle | État |
|---|---|---|
| `com.ace777.qwen-btc` | Analyse BTC 2×/jour (journalise analyses/ pour score_justesse) | ⏸️ Plist dans `~/Library/LaunchAgents/DESACTIVES_2026-08-10/` — **unloaded** |
| `com.ace777.qwen-elabore` | Élaboration Qwen solo nocturne | ⏸️ Idem — **unloaded** |

### 2. Routing (`~/prise-ia/routing.json`) — fallbacks basculés
| Tâche | Avant | Après |
|---|---|---|
| `cortana.brief` (fallback) | qwen-local | **nvidia** |
| `audit.protocol` (fallback) | qwen-local | **nvidia** |
| `cortana.analyse` (fallback) | qwen-local | **nvidia** |
| `coffre.ask` (fallback) | qwen-local | **nvidia** |
| `qwen.elabore` (provider) | qwen-local | **nvidia** (service en pause) |
| `qwen.btc` (provider) | qwen-local | **nvidia** (service en pause) |

### 3. GARDÉS sur qwen-local (réserve JUGE ① — filet local)
`ada.sanity` · `chat.local` · `signets.synthese` → **inchangés**, Ollama reste actif (17 Mo RAM).

### 4. Sauvegarde
`~/prise-ia/routing.json.bak_avant_pause_qwen_20260810`

---

## 🔄 PROCÉDURE DE RÉ-INTRODUCTION (rollback / mode C6)

> ⚠️ **À faire APRÈS la fusion validée sur banc d'essai** (aucune dégradation latence/taux d'erreur constatée).

### Étape 1 — Restaurer les 2 services
```bash
cp ~/Library/LaunchAgents/DESACTIVES_2026-08-10/com.ace777.qwen-btc.plist ~/Library/LaunchAgents/
cp ~/Library/LaunchAgents/DESACTIVES_2026-08-10/com.ace777.qwen-elabore.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.qwen-btc.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.qwen-elabore.plist
# Vérif : launchctl list | grep qwen
```

### Étape 2 — Restaurer le routing (4 fallbacks + 2 providers → qwen-local)
```bash
cd ~/prise-ia
cp routing.json.bak_avant_pause_qwen_20260810 routing.json   # restauration complète
# OU modification ciblée (python3) : fallback cortana.brief/audit.protocol/cortana.analyse/coffre.ask = qwen-local
#                                     provider qwen.elabore/qwen.btc = qwen-local
chmod u+w routing.json && chmod 444 routing.json   # rétablir la protection
```

### Étape 3 — Vérification (test de bascule délibérée Qwen → hub)
```bash
# 1. Appel local : task ada.sanity doit répondre via qwen-local
curl -s http://127.0.0.1:11435/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"task":"ada.sanity","messages":[{"role":"user","content":"test"}],"max_tokens":20}'
# 2. Appel cloud : task analyse.profonde doit répondre via nvidia (le hub relit routing.json à chaque appel)
# 3. launchctl list | grep qwen  → PIDs présents
# 4. Valider avec la famille (loi 1quinquies) avant de considérer la ré-introduction terminée
```

---

## ✅ TESTS FAITS LE 10/08 (avant poussée)
| Test | Résultat |
|---|---|
| qwen-local répond (ada.sanity) | ✅ OK LOCAL |
| nvidia répond (analyse.profonde = nouveau fallback) | ✅ OK-NVIDIA |
| Hub /health | ✅ 9 providers |
| routing.json relu à chaque appel (pas de restart hub) | ✅ vérifié (`load_routing()` dans `chat_completions`) |
| JSON routing valide + protection 444 restaurée | ✅ |
| Aucun service qwen-btc/elabore chargé | ✅ |

---

## 📌 RÉFÉRENCES
- Avis famille bruts : `Index_Maison/FAMILLE_PAUSE_QWEN_2026-08-10/GEMINI.md` + `JUGE.md`
- Dossier services en pause : `~/Library/LaunchAgents/DESACTIVES_2026-08-10/`
- Sauvegarde routing : `~/prise-ia/routing.json.bak_avant_pause_qwen_20260810`
