# RETOUR CHEF SCIENTIFIQUE — 2e passe codeur (SPEC v2 SELL FULL)

Date : 2026-08-29 · Source : relecture du diff `CODE_SELL_FULL_2026-08-29.md` sur `paper_diprip.py`

## Verdict : ⛔ REFUSÉ en l'état — 2 corrections obligatoires, puis on reteste

Le fond de ta logique est bon (garde-fou amplitude + invalidation + cascade 50 % + dust sweeper + PREUVE chiffrée ~84,74 $ d'économie). Mais ton diff **plante au premier stop** et **ignore la config** — impossible à merger.

---

## ❌ CORRECTION 1 — CRITIQUE (crash) : `sc` n'existe pas dans `manage_open`

**Le problème** : ton diff utilise `sc.get("move24_pct")` dans `manage_open` (les 2 hunks, lignes ~1885 et ~1914 du fichier). Or la signature est :

```python
def manage_open(self, pair: str, price: float):
```

et l'appel (ligne 2114) est `self.manage_open(pair, price)` — **sans `sc`**. Résultat : `NameError: name 'sc' is not defined` **au premier déclenchement de stop** → crash du moteur.

**La correction (minimale, 1 ligne)** : en tête de `manage_open`, juste après `p = self.pos[pair]`, ajouter :

```python
sc = self.scores.get(pair) or {}
```

Aucun autre appel à changer (un seul appel, ligne 2114). Ne change PAS la signature — trop de surface.

---

## ❌ CORRECTION 2 — MAJEUR (verrou 3 de la SPEC v2) : config jamais chargée

**Le problème** : tu proposes les variables dans `defaults.env` (SELL_FULL_AMPLITUDE_GUARD, etc.) mais ton code les lit avec `getattr(self, "sell_full_amplitude_guard", 12.0)`. Ces attributs **ne sont jamais définis** dans `__init__` → le `getattr` retombe **toujours** sur les défauts et **les valeurs de defaults.env sont ignorées**. C'est exactement le verrou 3 de la SPEC v2 (« paramètres dans defaults.env, rétro-compat ») que le juge a exigé.

**La correction** : charger les 5 attributs dans `__init__` (à côté de `self.rip_scaleout_frac`, ligne ~531, même style `cfg.get`) :

```python
self.sell_full_amplitude_guard = float(cfg.get("SELL_FULL_AMPLITUDE_GUARD", "12.0"))
self.sell_full_require_invalidation = int(cfg.get("SELL_FULL_REQUIRE_INVALIDATION", "1"))
self.sell_full_guard_degraded = int(cfg.get("SELL_FULL_GUARD_DEGRADED", "1"))
self.dust_sweep_min_notional = float(cfg.get("DUST_SWEEP_MIN_NOTIONAL", "1.0"))
```

Puis dans le diff, remplacer les `getattr(self, "x", defaut)` par des lectures directes `self.sell_full_amplitude_guard`, etc.

---

## ✅ Points validés (ne pas y toucher)

| Point | Verdict |
|---|---|
| `lot_filter(pair)` → `(step, min_notional)` (ligne 1476) | ✅ signature OK pour `step, _mn = self.lot_filter(pair)` |
| Logique d'invalidation (`dd15 < -5.0` = vraie cassure → SELL full autorisé) | ✅ cohérent avec la SPEC. Note : `vol_spike == 0` est quasi impossible (ratio vol6/médiane), c'est `dd15` qui porte la décision — OK, mais mets `dd15 < -5.0` en **premier** dans la condition pour la lisibilité |
| Dust sweeper (résidu < min_q ou < 1 $ → vente totale tracée DUST_SWEEP) | ✅ |
| Les 2 zones de stop modifiées | ✅ ce sont bien les bonnes (backstop trailing + stop standard) |
| `return` conservé après chaque branche | ✅ garde le comportement actuel |
| PREUVE : −153,24 $ → ~−68,50 $ (économie ~84,74 $) | ✅ estimation cohérente avec le patron mesuré |

---

## 📋 Ce que j'attends de toi

1. Renvoie le diff **complet et appliquable** (les 2 hunks + le bloc `__init__` + defaults.env) avec la correction 1 (ligne `sc = self.scores.get(pair) or {}`) et la correction 2 (5 attributs chargés).
2. Confirme que tu as lu ce retour (réponse courte : « corrections intégrées »).

⚠️ Rappel : aucune modification n'est faite sur le moteur réel — on travaille en diff + test sur copie. Le moteur tourne en ce moment.
