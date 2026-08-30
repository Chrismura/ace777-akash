# 📚 DOCUMENTATION COMPLÈTE — Session 25 Août 2026

> **Objet** : Refonte du pipeline de données ACE — du cockpit éteint au système incassable
> **Auteur** : Buffy (supervision) + Christophe (direction)
> **Date** : 2026-08-25

---

## 🎯 RÉSUMÉ EN UNE PHRASE

On est passés d'un cockpit éteint avec des données fausses à un pipeline unifié, atomique, auto-réparé, avec détection de baleines silencieuses et 3 modes de sécurité.

---

## 📋 CE QUI A ÉTÉ IMPLÉMENTÉ

### ÉTAPE 1 : Atomicité JSON (45 min)

**Problème** : `live.json` était écrit par 2 scripts (thermo + pont) en même temps → race condition → JSON tronqué → données NULL pour Cortana/Hulk.

**Solution** : Module `atomic_write.py` avec SafeLiveWriter.

**Comment ça marche** :
```
1. Ouvrir un fichier .lock (fcntl.flock) → verrou exclusif
2. Écrire dans .tmp + fsync → données sur disque
3. os.replace(.tmp, live.json) → swap atomique POSIX
4. Libérer le verrou
```

**Fichiers** :
- `Index_Maison/scripts/atomic_write.py` — le module
- `Index_Maison/scripts/thermo_quotidien_free.py` — modifié (SafeLiveWriter)
- `Index_Maison/scripts/pont_onchain.py` — modifié (SafeLiveWriter)

**Test** : 20 readers + 10 writers en parallèle → 0 erreur

**Pour modifier** :
- Si tu veux changer le timeout du lock : modifier `fcntl.flock(lock, LOCK_EX)` → ajouter un timeout
- Si tu veux un backup : ajouter `shutil.copy2(live_json, backup)` avant `os.replace`

---

### ÉTAPE 2 : Circuit Breaker (2h)

**Problème** : Hulk tradeait sur des données stale (Deribit timeout, Blockchain.com 404).

**Solution** : Module `circuit_breaker.py` avec hystérésis.

**Comment ça marche** :
```
Données fraîches → CLOSED → Hulk trade ✅
Données stale ×3 → OPEN → Hulk arrête ⚡
Après cooldown → HALF-OPEN → test de reprise
Données fraîches → CLOSED → Hulk reprend ✅
```

**Fichiers** :
- `hulk-mexc/scripts/circuit_breaker.py` — le module
- `hulk-mexc/scripts/paper_diprip.py` — import + 2 CB (btc + gex) + heartbeat status

**Pour modifier** :
- TTL btc : chercher `TTL 10s` dans paper_diprip.py → changer la valeur
- Nombre d'échecs avant trip : chercher `trip_after=3` → changer
- Cooldown : chercher `cooldown=30` → changer

---

### ÉTAPE 3 : Store Temporel LMDB (4h)

**Problème** : Pas d'historique des données — seulement le dernier cycle.

**Solution** : Module `temporal_store.py` avec LMDB (Hot/Warm/Cold + Dead Man's Switch).

**Comment ça marche** :
```
Hot  (5 min)  → prix, funding, OI → live.json
Warm (30 min) → GEX, fear/greed → live.json
Cold (24h)    → ETF, historique → live.json
DMS  (15s)    → watchdog → si writer ne bouge + → crash + restart
```

**Fichiers** :
- `Index_Maison/scripts/temporal_store.py` — le module LMDB
- `Index_Maison/scripts/thermo_quotidien_free.py` — intégré (Hot/Warm/Cold)
- `Index_Maison/scripts/pont_onchain.py` — intégré (Hot/Cold)

**Pour modifier** :
- Taille LMDB : chercher `map_size=10*1024*1024` → augmenter si besoin
- Fréquences : modifier les constantes `HOT_TTL`, `WARM_TTL`, `COLD_TTL`
- DMS timeout : chercher `DMS_TIMEOUT = 15` → changer

---

### ÉTAPE 4 : SDI + IPT + RBF (3h)

**Problème** : Les baleines bougent en douce, nos scan ne les voyaient pas.

**Solution** : 3 signaux comportementaux dans `silent_drain_index.py`.

**SDI (Silent Drain Index)** :
- Mesure : divergence BTC dormant >1an vs frais payés par adresses <30j
- Source : Blockchain.com (ou alternative.me en proxy) + Mempool.space
- Seuil : SDI > 0.7 = drainage probable

**IPT (Indice de Pression Topologique)** :
- Mesure : ratio micro-tx × z-score frais × entropie scripts
- Source : Mempool.space
- Seuil : IPT > 0.8 = un seul acteur automatisé

**RBF (Replace-By-Fee)** :
- Mesure : proportion de transactions qui se remplacent (urgent)
- Source : Mempool.space
- Seuil : RBF > 0.6 = urgence

**Fichier** :
- `Index_Maison/scripts/silent_drain_index.py`

**Pour modifier** :
- Seuils : modifier `SDI_THRESHOLD`, `IPT_THRESHOLD`, `RBF_THRESHOLD`
- Sources : modifier les URLs dans `get_fee_pressure()`, `get_mempool_entropy()`
- Proxy dormant : Blockchain.com 404 → utiliser alternative.me (déjà en place)

---

### ÉTAPE 5 : Sentinel (2h)

**Problème** : Le sniffer (DeepSeek V4) coûte cher à tourner en continu.

**Solution** : `sentinel.py` — déclencheur z-score qui ne fire DeepSeek V4 QUE quand il y a anomalie.

**Comment ça marche** :
```
live.json → sentinel.py → calcule z-scores (12 métriques)
                         → si z > seuil → fetch Google News → DeepSeek V4
                         → si z < seuil → rien (0 coût)
```

**Coût** :
- Marché calme : 0 appel/heure
- Marché volatile : 12 appels/heure max (rate-limit 30 min/paire)

**Fichier** :
- `Index_Maison/scripts/sentinel.py`

**Pour modifier** :
- Seuils z-score : modifier `ZSCORE_THRESHOLDS` (dict)
- Rate limit : modifier `RATE_LIMIT_SECONDS = 1800`
- Taille historique : modifier `HISTORY_SIZE = 288` (24h à 5 min)

---

### ÉTAPE 6 : Pipeline Health (2h)

**Problème** : Hulk tradeait même quand les données étaient douteuses.

**Solution** : `pipeline_health.py` — score de confiance 3 modes.

**Les 7 sources évaluées** :

| Source | TTL nominal | TTL critique | Poids | Action si bas |
|---|---|---|---|---|
| Binance | <500ms | >1.5s | 25% | Kill Switch |
| Mempool.space | <10s | >30s | 20% | Réduction tailles |
| Deribit | <2s | >5s | 15% | Désactivation GEX |
| Alternative.me | <26h | >48h | 10% | Mode technique pur |
| Blockchain.com | <6h | >24h | 10% | Ignorer dormant |
| Google News | <1h | >4h | 10% | Ignorer narratif |
| SDI/IPT | <10s | >30s | 10% | Réduction mur-fragile |

**Les 3 modes** :
```
Score ≥ 0.85 → ✅ NOMINAL → tailles ×1.0
Score 0.60-0.85 → ⚠️ DÉGRADÉ → tailles ×0.5
Score < 0.60 → 🚨 KILL SWITCH → tailles ×0.0 (gel)
```

**Fichiers** :
- `Index_Maison/scripts/pipeline_health.py` — le module
- `hulk-mexc/scripts/paper_diprip.py` — intégré (get_pipeline_health_mult + heartbeat)

**Pour modifier** :
- Poids des sources : modifier `SOURCE_CONFIG["binance"]["poids"]` etc.
- Seuils mode : modifier `0.85` et `0.60` dans `compute_global_health()`
- Actions : modifier `position_mult` dans les branches if/elif/else

---

## 🏗️ ARCHITECTURE GLOBALE

```
┌─────────────────────────────────────────────────────────────┐
│                    SOURCES DE DONNÉES                        │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│  Binance    │  Mempool    │  Deribit    │  Google News      │
│  (prix)     │  (frais)    │  (GEX)      │  (narratif)       │
│  API publique│  API gratuite│  API publique│  RSS gratuit    │
└──────┬──────┴──────┬──────┴──────┬──────┴────────┬──────────┘
       │             │             │               │
       ▼             ▼             ▼               ▼
┌─────────────────────────────────────────────────────────────┐
│              THERMO + PONT (writers atomiques)               │
│  atomic_write.py → .tmp + fsync + os.replace                 │
│  temporal_store.py → LMDB Hot/Warm/Cold                      │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      live.json                               │
│  (données unifiées, fraîches, atomiques)                     │
└──────────┬──────────────────┬───────────────────────────────┘
           │                  │
           ▼                  ▼
┌──────────────────┐  ┌──────────────────────────────────────┐
│  pipeline_health │  │  sentinel.py                          │
│  (score 0-1)     │  │  (z-scores → déclenche sniffer)       │
│  3 modes         │  │                                       │
└────────┬─────────┘  └──────────────────┬───────────────────┘
         │                               │
         ▼                               ▼
┌──────────────────┐  ┌──────────────────────────────────────┐
│  HULK            │  │  SNIFFER (DeepSeek V4)               │
│  paper_diprip.py │  │  brut vs narratif → divergence        │
│  × health_mult   │  │  → signal à Hulk                      │
└──────────────────┘  └──────────────────────────────────────┘
```

---

## 📁 FICHIERS CRÉÉS/MODIFIÉS

### Nouveaux fichiers
| Fichier | Rôle |
|---|---|
| `Index_Maison/scripts/atomic_write.py` | SafeLiveWriter (fcntl.flock) |
| `Index_Maison/scripts/temporal_store.py` | LMDB Hot/Warm/Cold |
| `Index_Maison/scripts/sentinel.py` | Déclencheur z-score |
| `Index_Maison/scripts/silent_drain_index.py` | SDI + IPT + RBF |
| `Index_Maison/scripts/pipeline_health.py` | Score de confiance 3 modes |
| `hulk-mexc/scripts/circuit_breaker.py` | Circuit Breaker à hystérésis |

### Fichiers modifiés
| Fichier | Modification |
|---|---|
| `Index_Maison/scripts/thermo_quotidien_free.py` | SafeLiveWriter + LMDB + SDI |
| `Index_Maison/scripts/pont_onchain.py` | SafeLiveWriter + LMDB |
| `hulk-mexc/scripts/paper_diprip.py` | Circuit Breaker + wall_strength + pipeline_health |
| `Index_Maison/cockpit/index.html` | Indicateur SDI + pédagogie |

---

## 🔧 COMMENT CORRIGER UN BUG

### Si live.json est corrompu
```bash
# Vérifier le dernier JSON valide
python3 -c "import json; json.load(open('Index_Maison/thermo/live.json'))"

# Si erreur, relancer thermo
cd Index_Maison && python3 scripts/thermo_quotidien_free.py
```

### Si Hulk ne reprend pas ses positions
```bash
# Vérifier le state pointer
cat hulk-mexc/runs/.hulk_resume_pointer

# Forcer le bon state
echo "PAPER_V1_20260825_111542_state.json" > hulk-mexc/runs/.hulk_resume_pointer

# Relancer
cd hulk-mexc && python3 scripts/paper_diprip.py --resume
```

### Si le pipeline_health est en Kill Switch
```bash
# Vérifier quelles sources sont en erreur
python3 -c "
import json
h = json.load(open('Index_Maison/data/pipeline_health.json'))
for s, d in h['sources'].items():
    if d['score'] < 0.8:
        print(f'{s}: {d[\"score\"]} - {d[\"issues\"]}')
"
```

---

## 📊 MD5 REGISTRE (anti-intrusion)

Le fichier `Index_Maison/data/md5_registry.json` contient les empreintes de tous les fichiers critiques. La veilleuse vérifie à chaque cycle.

```json
{
  "Index_Maison/scripts/thermo_quotidien_free.py": {"md5": "06afc161..."},
  "Index_Maison/scripts/pont_onchain.py": {"md5": "c9a52ac5..."},
  "Index_Maison/scripts/atomic_write.py": {"md5": "391309b0..."},
  "Index_Maison/scripts/temporal_store.py": {"md5": "57573990..."},
  "Index_Maison/scripts/sentinel.py": {"md5": "1f57040e..."},
  "Index_Maison/scripts/silent_drain_index.py": {"md5": "a34c5583..."},
  "Index_Maison/scripts/pipeline_health.py": {"md5": "ebf03776..."},
  "Index_Maison/cockpit/index.html": {"md5": "d474e15d..."},
  "hulk-mexc/scripts/paper_diprip.py": {"md5": "de9e5f2d..."},
  "hulk-mexc/scripts/circuit_breaker.py": {"md5": "3240aa49..."}
}
```

**Pour ajouter un fichier** :
```python
import hashlib
md5 = hashlib.md5(open('chemin/fichier.py', 'rb').read()).hexdigest()
# Ajouter au registry
```

---

## 🎯 PROCHAIN CHANTIER

| Priorité | Action | Impact |
|---|---|---|
| **P0** | Valider 72h de prod | Confiance |
| **P1** | WebSocket mempool (upgrade futur) | Latence <100ms |
| **P2** | LMDB export live.json en arrière-plan | Moins de IO |
| **P3** | Consultation "trouve les failles" après 72h | Validation terrain |

---

*Document généré le 2026-08-25. Mis à jour par Buffy.*
