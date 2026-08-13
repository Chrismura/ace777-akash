# DIAGNOSTIC ALPHA — MASTER_VORTEX_V2_COLLAB_4H

> Généré: `2026-08-13T16:44:48Z` | Verdict: **ALERTE — ALPHA quasi dormante**

## Résumé

| Métrique | ALPHA | BETA (référence) |
|----------|-------|------------------|
| FILLED | 4 | 21 |
| PnL net | 2.3134 USDT | -0.3269 USDT |
| SKIP total | 149 | 154 |
| duo_wait | 18 (12.1% des SKIP ALPHA) | 0 |

## Entonnoir des gates — ALPHA

Ordre dans `genesis_manifest.txt` : radar → tension/vacuum → tactic → stase → **duo** → qty → llm_gate → execute

- `radar_block` — **109**
- `impulse_resonance_wait` — **19**
- `duo_wait` — **18**
- `tactic_mismatch` — **3**

## duo_wait — sous-raisons (cause #2 après radar)

- `no_trigger` — **17** (94.4% des duo_wait)
- `no_state` — **1** (5.6% des duo_wait)

### Lecture technique

| Sous-raison | Signification |
|-------------|---------------|
| `stale_state` | `duo_state.json` trop vieux (> `DUO_EVENT_TTL_SEC=60s`) |
| `no_trigger` | SCOUT pas en mode suffer/revenge/vacuum_strike |
| `no_state` | fichier `duo_state.json` absent ou illisible |
| `no_true_vacuum` | `DUO_HUNTER_REQUIRE_TRUE_VACUUM=TRUE` non satisfait |

## Cause racine probable

### 1. `DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE` (actif — revenge élargi)

Revenge autorisé au-delà de `stop_loss` (shock / fluid / sentinel).
Sorties BETA observées :

- `shock_inversion_stop` — 17 trades
- `fluid_exit_inversion` — 3 trades
- `fluid_exit_brake` — 1 trades

- Sorties `shock_inversion_stop` : **17**
- Sorties `stop_loss` : **0**


### 2. `DUO_EVENT_TTL_SEC=60` (stale_state)

Quand le SCOUT ne rafraîchit pas `duo_state.json` dans les 60s, le HUNTER skip avec `stale_state`.
Observé : **0** fois (0.0% des duo_wait).

### 3. radar_block en amont (109 SKIP)

Même si le duo était parfait, 73.2% des cycles ALPHA meurent au radar avant d'atteindre le HUNTER.

## Paramètres duo actifs (config)

| Variable | Valeur |
|----------|--------|
| DUO_EVENT_TTL_SEC | `60` |
| DUO_HUNTER_REQUIRE_STOP_LOSS | `FALSE` |
| DUO_SCOUT_SUFFER_BPS | `-5` |
| DUO_SCOUT_SUFFER_USDT | `-0.50` |
| DUO_HUNTER_REQUIRE_TRUE_VACUUM | `FALSE` |

## Recommandations (NON APPLIQUÉES — ordre requis)

| Priorité | Action | Impact attendu |
|----------|--------|----------------|
| **P0** | `DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE` ou accepter `shock_inversion_stop` en revenge | Débloque revenge sur sorties BETA réelles |
| **P1** | `DUO_EVENT_TTL_SEC=60` (ou 120) | Réduit `stale_state` |
| **P2** | Rafraîchir `ts_ms` dans `duo_state.json` à chaque cycle SCOUT (même SKIP) | Élimine stale_state structurel |
| **P3** | Revoir seuils radar ALPHA (`VACUUM_TENSION_THRESHOLD_ALPHA`) | Réduit radar_block en amont |

## Fichiers analysés

- `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
- `runs/duo_state.json` (état live au moment du diag)

---
_Généré par `scripts/diagnostic_alpha.sh` — aucune constante modifiée._
