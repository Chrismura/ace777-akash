# Vérification — Version nuit 9–10 mars 2026 + Qwen Tween

## 1. Version identique à la nuit

| Élément | Nuit (user paste) | Actuel | Statut |
|--------|-------------------|--------|--------|
| Lanceur | `launch_test_master_base_v8_6_fortress.sh` | idem | OK |
| LLM | `LLM_GATE_ENABLED=TRUE` + `qwen2.5-coder:1.5b` | idem (fortress L82-83) | OK |
| Duration | `--duration 04:00:00` | supporté | OK |
| MOM | 0.96 | 0.96 | OK |
| WALL_DROP | 6.5% | 6.5% | OK |
| GLOBAL_STOP | -45.00 | -45.00 | OK |
| BETA | x5, Leverage=3, BuyUSDT=200, SHORT | idem (impact L71-94) | OK |
| ALPHA | x13, Leverage ramp 5→13, BuyUSDT=800, LONG, BURST | idem (impact L98-125) | OK |
| Préfixes | [BETA_X5] jaune, [ALPHA_X13_BURST13] cyan | idem (impact L62-66) | OK |

**Conclusion :** La version actuelle correspond à celle de la nuit.

---

## 2. Couleurs sur les lignes de cycle

| Segment | Couleur | Code | Lignes genesis |
|---------|---------|------|-----------------|
| Cycle N | Bleu | C_B | toutes les lignes cycle |
| SKIP | Jaune | C_Y | hashrate, radar, impulse, vacuum, tactic, duo, qty, llm_gate |
| ORDER | Vert | C_G | ligne ORDER + hedge fallback |
| OBSERVE | Cyan | C_C | ligne OBSERVE |
| Détails (après \|) | Cyan | C_C | partout |
| Erreurs | Rouge | C_R | ENTRY error, EXIT error, LEVERAGE error |
| SOFT anomaly | Magenta | C_M | détection + pnl |
| SENTINEL / LAGRANGE / PHASE_SHIFT | Magenta | C_M | événements spéciaux |

**Conclusion :** Les couleurs sont bien appliquées sur les segments (Cycle bleu, SKIP jaune, ORDER vert, etc.).

---

## 3. Mode standard pour tests de cycle

Pour désactiver les couleurs (sortie standard) :

```bash
CYCLE_COLORS=FALSE ./launch_test_master_base_v8_6_fortress.sh --duration 00:05:00
```

Ou dans v8_7 :

```bash
CYCLE_COLORS=FALSE LLM_MODEL=qwen2.5-coder:1.5b ./launch_test_master_base_v8_7_qwen_tween.sh --duration 00:05:00
```

---

## 4. Qwen Tween (Ollama qwen2.5-coder:1.5b)

- **Modèle Ollama :** `qwen2.5-coder:1.5b` (après `ollama pull qwen2.5-coder:1.5b`)
- **v8_6 fortress :** `LLM_MODEL=qwen2.5-coder:1.5b` (déjà correct)
- **v8_7 qwen_tween :** était `QWEN_TWEEN` → corrigé en `qwen2.5-coder:1.5b`

---

## 5. Commande de lancement (identique à la nuit)

```bash
ollama pull qwen2.5-coder:1.5b
LLM_GATE_ENABLED=TRUE ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
```

Ou via v8_7 (même config + tag distinct) :

```bash
ollama pull qwen2.5-coder:1.5b
./launch_test_master_base_v8_7_qwen_tween.sh --duration 04:00:00
```
