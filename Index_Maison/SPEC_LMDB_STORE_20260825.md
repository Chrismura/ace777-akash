# SPEC — ÉTAPE 3 : STORE TEMPOREL LMDB + DEAD MAN'S SWITCH
> Buffy (superviseur), 25/08/2026

## CONTEXTE
Étape 1 (atomicité) et Étape 2 (circuit breaker) sont en place.
Maintenant on structure les données par temporalité pour que Hulk ait
les bonnes données au bon moment.

## CE QU'ON A DÉJÀ
- `atomic_write.py` : SafeLiveWriter (fcntl + tmp + os.replace)
- `circuit_breaker.py` : TradeCircuitBreaker (TTL + hystérésis)
- `paper_diprip.py` : Hulk lit live.json pour GEX, aspire l'orderbook MEXC directement

## OBJECTIF
Créer un store temporel LMDB qui :
1. Isole les données par temporalité (Hot/Warm/Cold)
2. Gère le Dead Man's Switch (si un writer meurt, alerte)
3. Reste compatible avec live.json (les 36 scripts lisent toujours ça)

## CONTRAINTES
- **macOS** (pas `/dev/shm`)
- **`pip install lmdb`** (seule dépendance externe)
- **Rétrocompatibilité** : LMDB est un STORE SUPPLÉMENTAIRE, pas un remplacement de live.json
- Les 36 scripts continuent de lire live.json
- Hulk peut éventuellement lire LMDB directement (Étape 4, pas maintenant)

## ARCHITECTURE CIBLE

```
[thermo_quotidien] ──→ SafeLiveWriter ──→ live.json ←── SafeLiveWriter ←── [pont_onchain]
                                         (36 scripts lisent ICI)
                                              │
                                              ▼
                                    [LMDB Temporal Store]
                                    ├── HOT:  prix, spread, liquidations (TTL 10s)
                                    ├── WARM: funding, corrélations, score (TTL 1h)
                                    └── COLD: baleines, ETF, macro (TTL 24h)
                                              │
                                              ▼
                                    [Dead Man's Switch]
                                    Si aucun writer ne bouge pendant 15s → alerte
```

## SPÉCIFICATION TECHNIQUE

### 1. Module `temporal_store.py` (nouveau fichier)

Chemin : `Index_Maison/scripts/temporal_store.py`

```python
class TemporalStore:
    def __init__(self, db_path: str = "data/temporal_bus.lmdb"):
        # LMDB avec sub-databases pour Hot/Warm/Cold
        # + METADATA pour DMS
    
    def write(self, tier: str, key: str, data: dict) -> None:
        # tier: "hot", "warm", "cold"
        # Écrit avec timestamp automatique
        # Met à jour le heartbeat du DMS
    
    def read(self, tier: str, key: str) -> dict | None:
        # Lit une donnée
        # Retourne None si absent ou TTL dépassé
    
    def read_fresh(self, tier: str, key: str, max_age_seconds: float) -> dict | None:
        # Lit seulement si la donnée est fraîche (< max_age)
        # Sinon retourne None
    
    def dead_man_check(self, writer_name: str, max_silence: float = 15.0) -> bool:
        # True si le writer est mort (pas de heartbeat depuis max_silence)
    
    def heartbeat(self, writer_name: str) -> None:
        # Met à jour le heartbeat d'un writer
```

### 2. Intégration dans `thermo_quotidien_free.py`

Ajouter après l'écriture atomique de live.json :
```python
# Écriture dans le store temporel (en parallèle, ne bloque pas)
try:
    store = TemporalStore()
    store.write("hot", "btc_price", {"price": mark, "ts": time.time()})
    store.write("hot", "funding", {"rate": funding, "ts": time.time()})
    store.write("warm", "gex", gex_data)
    store.write("cold", "etf", etf_data)
    store.heartbeat("thermo")
except Exception:
    pass  # fail-open, ne bloque jamais le pipeline
```

### 3. Intégration dans `pont_onchain.py`

Ajouter après l'écriture atomique :
```python
try:
    store = TemporalStore()
    store.write("hot", "cpfp", {"zscore": z, "dust": dust})
    store.write("cold", "whales", {"dir": whale_dir, "blocs": n})
    store.heartbeat("pont")
except Exception:
    pass
```

### 4. Watchdog DMS (nouveau fichier optionnel)

Chemin : `Index_Maison/scripts/dms_watchdog.py`

Script léger qui vérifie le DMS toutes les minutes :
```python
store = TemporalStore()
if store.dead_man_check("thermo", max_silence=120):
    # Alerte + tentative de relance
    send_alert("thermo est mort depuis 2 min")
    restart_thermo()
if store.dead_man_check("pont", max_silence=120):
    send_alert("pont est mort depuis 2 min")
    restart_pont()
```

## EDGE CASES À TESTER
1. LMDB MapFullError (taille dépasse map_size) → prévoir 200MB
2. Coupure de courant → LMDB ACID protège les données
3. Deux process écrivent en même temps → LMDB gère le verrouillage
4. Lecture pendant écriture → LMDB autorise les lectures concurrentes (WAL mode)

## FICHIERS À CRÉER/MODIFIER
1. `Index_Maison/scripts/temporal_store.py` — **NOUVEAU**
2. `Index_Maison/scripts/thermo_quotidien_free.py` — ajouter écriture LMDB
3. `Index_Maison/scripts/pont_onchain.py` — ajouter écriture LMDB

## CE QU'ON NE TOUCHE PAS
- `live.json` et les 36 scripts lecteurs
- Les plists existantes
- Les indices/formules de la poussière
- Le circuit breaker (déjà en place)
