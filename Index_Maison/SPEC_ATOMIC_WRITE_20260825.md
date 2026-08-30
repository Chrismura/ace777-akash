# SPEC — ÉTAPE 1 : ÉCRITURE ATOMIQUE live.json
> Buffy (superviseur), 25/08/2026

## CONTEXTE
3 scripts écrivent dans `thermo/live.json` à des cycles différents :
- `thermo_quotidien_free.py` (market data) — cycle 5 min
- `pont_onchain.py` (whales, cpfp, dust) — cycle 5 min
- D'autres scripts indirectement

36 scripts lisent `live.json`. Problème : quand un écrit pendant qu'un autre lit → JSON tronqué → données NULL → Cortana/Ada prennent des décisions sur du vide.

## OBJECTIF
Éliminer la race condition en rendant l'écriture de `live.json` **atomique** : un lecteur ne voit JAMAIS un fichier à moitié écrit.

## CONTRAINTES
- **macOS** (pas Linux, pas `/dev/shm`)
- **Zéro modification des 36 scripts lecteurs** — ils continuent de lire `live.json` normalement
- **stdlib seule** (pas Redis, pas LMDB pour l'instant)
- **Rétrocompatibilité totale** — même structure JSON, même chemin

## ARCHITECTURE CIBLE

```
Script A (thermo)     ──→ [verrou + tmp + os.replace] ──→ live.json ←── [verrou + tmp + os.replace] ──── Script B (pont)
                                                                                        ↑
                                                                        36 scripts lisent ICI (sans锁)
```

## SPÉCIFICATION TECHNIQUE

### 1. Module `atomic_write.py` (nouveau fichier)

Chemin : `Index_Maison/scripts/atomic_write.py`

```python
class SafeLiveWriter:
    def __init__(self, target_path: str = "live.json"):
        # Crée les chemins target, .tmp, .lock dans le MÊME répertoire
    
    def write(self, data: dict) -> None:
        # 1. json.dumps EN MÉMOIRE d'abord (fail-fast si pas sérialisable)
        # 2. fcntl.flock(LOCK_EX) sur .lock
        # 3. Écriture dans .tmp + fsync
        # 4. os.replace(.tmp, target) — atomique POSIX
        # 5. fcntl.flock(LOCK_UN)
        # Nettoyage .tmp en cas d'erreur
    
    def read(self) -> dict:
        # 1. fcntl.flock(LOCK_SH) sur .lock (non-bloquant si possible)
        # 2. json.load(target)
        # 3. Fallback {} en cas d'erreur
        # 4. fcntl.flock(LOCK_UN)
```

### 2. Intégration dans `thermo_quotidien_free.py`

- Remplacer l'écriture directe `live_json.write_text(...)` par `SafeLiveWriter.write(payload)`
- Le writer est instancié une fois au début de `main()`
- Le reste du script inchangé

### 3. Intégration dans `pont_onchain.py`

- Même principe : remplacer l'écriture par `SafeLiveWriter.write(payload)`
- pont_onchain lit d'abord le live.json existant (via `SafeLiveWriter.read()`), y injecte la section onchain, puis réécrit atomiquement

### 4. Tests obligatoires

- `py_compile` sur les 3 fichiers
- Test de concurrence : 10 processus écrivent en boucle pendant que 20 lisent → zéro `JSONDecodeError`
- Vérifier que les 36 scripts existants lisent correctement le nouveau format

## FICHIERS À MODIFIER
1. `Index_Maison/scripts/atomic_write.py` — **NOUVEAU**
2. `Index_Maison/scripts/thermo_quotidien_free.py` — remplacer l'écriture
3. `Index_Maison/scripts/pont_onchain.py` — remplacer l'écriture

## CE QU'ON NE TOUCHE PAS
- La structure du JSON (mêmes clés)
- Les 36 scripts lecteurs
- Les plists
- Les indices/formules
