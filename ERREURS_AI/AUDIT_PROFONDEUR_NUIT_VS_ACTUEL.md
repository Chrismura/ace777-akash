# Audit en profondeur — Setup nuit vs actuel (Qwen, configs, pertes)

**Date :** 27 février 2026

---

## 1. Chaîne d'exécution

| Lanceur | Appelle | Variables clés |
|---------|---------|----------------|
| **launch_250_4h.sh** | fortress | BUY_USDT_BETA=250, ALPHA=250, LLM_GATE=TRUE |
| **launch_test_master_base_v8_6_fortress.sh** | impact | STOP_LOSS=16, BUY_USDT=200/800 (defaults) |
| **launch_test_master_base_v8_5_impact.sh** | genesis (tail +85) | BETA/ALPHA configs |
| **launch_test_master_base_v8_7_qwen_tween.sh** | fortress | Même config, tag différent |

**Problème :** `launch_250_4h` n'appelle **jamais** `config_nuit.env`. Les valeurs de la nuit ne sont jamais chargées.

---

## 2. Config nuit vs actuel (détail)

### 2.1 config_nuit.env (jamais chargé par launch_250_4h)

```bash
BUY_USDT_BETA=200
BUY_USDT_ALPHA=800
STOP_LOSS_BPS=16
MOMENTUM_THRESHOLD=0.96
```

### 2.2 Ce que lance réellement launch_250_4h

| Variable | Valeur | Source |
|----------|--------|--------|
| BUY_USDT_BETA | 250 | launch_250_4h (override) |
| BUY_USDT_ALPHA | 250 | launch_250_4h (override) |
| STOP_LOSS_BPS | 16 | fortress (défaut, pas config_nuit) |
| MOMENTUM_THRESHOLD | 0.96 | fortress |

---

## 3. LLM Gate (Qwen) — Points critiques

### 3.1 Prompt envoyé à Qwen

```
Side=SELL px=69700 bps=-5.2. Trade?
```

- **Très minimal** : pas de contexte marché, pas de system prompt
- **Variable** : Qwen peut répondre différemment selon charge, température, etc.

### 3.2 Logique de skip

```bash
if echo "$llm_out" | grep -qiE "skip|non|no|stop|pas"; then
  # SKIP
else
  # TRADE (passe)
fi
```

### 3.3 Comportement en cas d'erreur (bug potentiel)

- Si **curl échoue** (timeout 15s, réseau, Ollama down) → `llm_out=""`
- `echo "" | grep "skip"` → **aucun match**
- **Conséquence : le trade PASSE** (fail-open)

Quand Binance ou le réseau pose problème, Ollama peut être lent. Si le curl timeout, plus de trades passent sans filtrage Qwen.

### 3.4 Différence nuit vs actuel

- **Même modèle** : qwen2.5-coder:1.5b
- **Même prompt**
- **Différence possible** : charge machine, latence Ollama, réponses plus/moins conservatrices selon le moment

---

## 4. Fichiers .1437 — Configs non utilisées

### anomaly_soft.1437 (non chargé par genesis)

```
ANOMALY_TICK_BPS=20        # genesis default: 40
ANOMALY_PNL_USDT=0.02     # genesis default: 0.05
SOFT_STOP_LOSS_BPS=6      # genesis default: 7
```

Ces valeurs sont **plus strictes** (anomalie déclenchée plus tôt) mais **genesis_manifest ne charge pas ce fichier**. Elles ne s'appliquent pas.

### radar_gate.1437 (non chargé par genesis)

```
RADAR_MIN_CONF=0.88       # genesis default: 0.30
RADAR_MAX_SPREAD_BPS=2    # genesis default: 8
```

Config plus stricte (moins de trades) mais **jamais utilisée** par le flux actuel.

---

## 5. Duo BETA/ALPHA — Comportement différent

### Run actuel (launch_250_4h)

- **BETA** : 12 FILLED, beaucoup de SKIP (spread_too_wide, llm_skip, etc.)
- **ALPHA** : 0 FILLED, quasi tout en duo stale_state / duo no_trigger

### Run nuit (MASTER_BASE_V8_5_IMPACT_4H)

- **BETA** : 194 FILLED
- **ALPHA** : 7 FILLED

ALPHA ne trade plus dans le run actuel. Causes possibles :
- BETA ne publie pas correctement l’état (duo_state)
- Conditions marché différentes (spread, tension)
- Config duo (stale_state, no_trigger) plus restrictive

---

## 6. Synthèse des écarts

| Élément | Nuit | Actuel | Impact |
|---------|------|--------|--------|
| **Masse BETA** | 200 | 250 | +25 % perte par trade |
| **Masse ALPHA** | 800 | 250 | ALPHA moins actif |
| **config_nuit** | Chargée (si utilisée) | Jamais chargée | STOP_LOSS, etc. ignorés |
| **LLM gate** | Idem | Idem | Mais fail-open si Ollama timeout |
| **anomaly_soft.1437** | Non chargé | Non chargé | Valeurs strictes inutilisées |
| **radar_gate.1437** | Non chargé | Non chargé | Valeurs strictes inutilisées |
| **ALPHA trades** | 7 | 0 | Duo moins déclenché |

---

## 7. Recommandations

### 7.1 Revenir au setup nuit

```bash
source config_backup_nuit_20260310/config_nuit.env
./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
```

### 7.2 Ou modifier launch_250_4h pour charger config_nuit

```bash
# En tête de launch_250_4h.sh
[ -f config_backup_nuit_20260310/config_nuit.env ] && source config_backup_nuit_20260310/config_nuit.env
# Puis override masse si souhaité
export BUY_USDT_BETA="${BUY_USDT_BETA:-200}"
export BUY_USDT_ALPHA="${BUY_USDT_ALPHA:-800}"
```

### 7.3 LLM gate : fail-closed

En cas d’erreur/timeout Ollama, faire un SKIP au lieu de laisser passer :

```bash
if [ -z "$llm_out" ]; then
  # Ollama unreachable → SKIP (fail-closed)
  echo "SKIP | llm_gate timeout/error"
  continue
fi
```

### 7.4 Charger anomaly_soft.1437 dans genesis

Si le fichier existe, le sourcer pour appliquer des seuils plus stricts.

---

## 8. Conclusion

La différence ne vient pas uniquement de la masse. S’y ajoutent :

1. **config_nuit.env jamais chargée** par launch_250_4h
2. **LLM gate fail-open** quand Ollama timeout
3. **Fichiers .1437** (anomaly_soft, radar_gate) non utilisés
4. **ALPHA** qui ne trade plus (duo stale_state)
5. **Masse** 250 vs 200/800

Pour limiter les pertes comme la nuit : charger `config_nuit.env`, revenir à 200/800, et corriger le fail-open du LLM gate.
