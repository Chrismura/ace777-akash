# HULK — Schéma Technique Complet & Document d'Audit

> **Système** : HULK — bot de trading algorithmique paper (dip & rip + bags) sur MEXC spot
> **Version audité** : `paper_diprip.py` — 2108 lignes · module `PaperBot` · 39 méthodes
> **Date de l'audit** : 2026-08-27
> **Nature** : Document de présentation pour due diligence technique (standards institutionnels)
> **Statut du système au moment de l'audit** : process PID 8886 vivant · 17 paires suivies · 11 positions · veilleuse STABLE · sante_index 12/12

---

## 0. Résumé exécutif

HULK est un système de trading **100% mécanique** (aucune décision humaine en boucle) qui
opère en **paper trading** (simulation, aucun ordre réel) sur **MEXC spot**. Il exécute une
stratégie **dip & rip** : acheter des petites capitalisations en zone de reflux, vendre en
paliers de profit, conserver un « bag » (position de long terme) après la première prise de
profit, et recycler le cash récupéré.

**Gouvernance en 6 couches** (de la donnée brute à l'exécution) :
1. **Données** — MEXC public REST (klines 60m×15j, ticker 24h, carnet d'ordres), corrélation BTC, GEX Deribit (via live.json), veille maison.
2. **Indices** — 5 régimes de marché par paire (QUIET/WATCH/IMPULSE/IMPULSE_WAIT/COOLING) calculés sur la physique des bougies, pas sur des indicateurs classiques.
3. **Gates d'entrée** — 9 contrôles séquentiels dont 3 dédiés à l'intégrité des données (circuits breaker), 2 aux murs de liquidité, 1 à la veille, 1 au cooldown post-stop.
4. **Exécution** — taille de position adaptative (murs, profil par paire, tier), filtre lots MEXC (stepSize/minNotional), arrondi côté achat ET vente.
5. **Sorties** — stop, rip scale-out 2 paliers, stake-out 50% à 2×, bag crash, DCA.
6. **Surveillance** — watchdog (2 min), veilleuse md5 (10 min), sante_index (12 chaînes), circuits breaker, kill-switch global.

**Principes d'ingénierie appliqués** (alignés standards du secteur) :
- **Séparation des préoccupations** : modules distincts — `ace_sense_mexc` (sonde), `veille_gates` (veille/cooldown), `circuit_breaker`, `cortana_contract` (conseils IA), `pipeline_health` (score de confiance des données).
- **Fail-safe defaults** : si une donnée est incertaine → pas d'entrée (jamais de pari sur une donnée douteuse) ; les sorties ne sont JAMAIS bloquées.
- **Déterminisme & reproductibilité** : état complet persisté à chaque cycle (state.json), CSV append-only, resume `--resume` après coupure.

---

## 1. Architecture globale (vue d'ensemble)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         ENVIRONNEMENT EXTERNE                              │
│  MEXC API (REST public)         Deribit (via live.json)   Veille maison     │
│  · klines 60m × 15j             · GEX call/put walls      · DIGEST_LATEST   │
│  · ticker/24hr                  · tsUnix fraîcheur        · .veille_status  │
│  · ticker/price                 │                        · cache cooldown  │
│  · exchangeInfo (stepSize)      │                        │                  │
│  · depth (carnet)               │                        │                  │
└──────────────┬──────────────────┴────────────────────────┴────────┬─────────┘
               │ GET (http_json, SIGALRM anti-black-hole)            │ lecture
┌──────────────▼─────────────────────────────────────────────────────▼─────────┐
│                         paper_diprip.py — PaperBot                          │
│                                                                              │
│  ┌──────────────┐   ┌──────────────────┐   ┌─────────────────────────────┐  │
│  │ DATA LAYER   │   │ SCORING          │   │ ENTRY GATES (ordre)          │  │
│  │ http_json    │──▶│ score_pair()     │──▶│ 1. circuits (btc+gex) is_ok  │  │
│  │ last_price   │   │   → 5 régimes    │   │ 2. cash_redeploy (si cash)   │  │
│  │ ticker_24h   │   │   → dip/rip/stop │   │ 3. régime ∈ COOLING|IMPULSE  │  │
│  │ klines       │   │   → cadence      │   │ 4. pas déjà en position      │  │
│  │ sniff_volume │   │   → vol spike    │   │ 5. MUR-SPOOF (façade)        │  │
│  │ aspiration_  │   └──────────────────┘   │ 6. MUR-CASSE (drop ≥15%/s)   │  │
│  │  sense       │                          │ 7. MUR-FAIBLE (score<0.2)     │  │
│  └──────────────┘                          │ 8. vol_ok_for_entry (small)  │  │
│                                            │ 9. (dans buy) veille+cooldown │  │
│  ┌──────────────────┐   ┌──────────────┐   └──────────────┬──────────────┘  │
│  │ RISK LAYER       │   │ SIZING       │                  │                 │
│  │ cb_btc (TTL 10s) │   │ notional     │◀─────────────────┘                 │
│  │ cb_gex (TTL 2h)  │   │  × wall_mult │   ┌─────────────────────────────┐  │
│  │ pipeline_health  │   │  × tier mult │   │ EXECUTION                   │  │
│  │  mult (0-1)      │   │  × bag mult  │   │ lot_filter (stepSize)       │  │
│  │ STOP_PAPER       │   │  ≤ mur×2%    │   │ _floor_step → qty au pas    │  │
│  │ STOP_ALL (global)│   └──────────────┘   │ minNotional check           │  │
│  └──────────────────┘                      │ pos[pair] = {...}           │  │
│                                             └──────────────┬──────────────┘  │
│  ┌──────────────────┐   ┌──────────────┐   ┌──────────────▼──────────────┐  │
│  │ EXITS            │   │ BAGS         │   │ PERSISTENCE                 │  │
│  │ stop ≤ -stop%    │   │ stake-out    │   │ save_state (atomic)         │  │
│  │ rip 2 paliers    │   │  50% à 2×    │   │ resume_state (--resume)     │  │
│  │ stake-out 50%    │   │ bag crash    │   │ CSV append-only (11 col)    │  │
│  │ 2×               │   │ DCA rebuy    │   │ lock anti-double-run        │  │
│  └──────────────────┘   └──────────────┘   └─────────────────────────────┘  │
└──────────────┬──────────────────────────────────────────────────────────────┘
               │ écrit
┌──────────────▼──────────────────────────────────────────────────────────────┐
│  SORTIES (fichiers)                                                         │
│  runs/PAPER_V1_<ts>.csv        (journal append-only, 11 colonnes)           │
│  runs/PAPER_V1_<ts>_state.json (état complet : pos/bags/cash/scores/...)    │
│  runs/ASPIRATION_CALIB_<ts>.csv(sonde : 18 colonnes, calibration murs)      │
│  runs/.paper_diprip.lock       (verrou fcntl anti-double-run)               │
│  strategie/cortana_pilot.json  (conseils IA Cortana, mode ADVISORY)         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Modules et responsabilités (séparation des préoccupations)

| Module | Rôle | Lignes | Dépend de |
|---|---|---|---|
| `paper_diprip.py` | Orchestrateur : boucle, gates, exécution, sorties, persistance | 2108 | tous ci-dessous |
| `ace_sense_mexc.py` | Sonde carnet : `book_sense`, `aspiration_sense`, `tension_score`, `entry_gate` | — | MEXC depth API |
| `veille_gates.py` | `entry_gate_check` (cooldown + skip RED), `veille_stale` (kill-switch veille), `record_stop` | — | fichiers runs/ |
| `circuit_breaker.py` | `TradeCircuitBreaker` : hystérésis CLOSED→OPEN→HALF-OPEN | 148 | stdlib |
| `cortana_contract.py` | `process_pilot` : applique les propositions IA (mode ADVISORY) | — | cortana_pilot.json |
| `pipeline_health.py` | Score de confiance 7 sources de données (via `Index_Maison/data/pipeline_health.json`) | — | live.json |
| `universe_profils.json` | Profils comportementaux par paire (murs, spoof, spread, fenêtres) | 11985 o | 53 465 mesures |
| `config/defaults.env` | Tous les paramètres (voir §5) | — | — |
| `data/universe_mexc_inventory.csv` | Inventaire MEXC : tiers A/B, spread, volume | — | — |

---

## 2. Infrastructure de données (Data Layer)

### 2.1 Sources et endpoints

| Donnée | Endpoint MEXC | Usage | Fréquence |
|---|---|---|---|
| Bougies 1h | `GET /api/v3/klines?symbol=X&interval=60m&limit=360` | 15 jours d'historique → régimes, cadence, drawdowns | refresh_scores (tous les 3 cycles) |
| Prix spot | `GET /api/v3/ticker/price` | prix courant par paire | chaque tick (20s) |
| Volume 24h | `GET /api/v3/ticker/24hr` | vol24, lastPrice, change | refresh_scores |
| Spécifications lots | `GET /api/v3/exchangeInfo` | `baseSizePrecision`→stepSize, `quoteAmountPrecision`→minNotional | lot_filter (cache) |
| Carnet d'ordres | `GET /api/v3/depth` (via `aspiration_sense`) | murs bid/ask, spoof, drops | probe aspiration |
| GEX Deribit | `Index_Maison/thermo/live.json` → `gex.*` | call/put walls, fraîcheur | probe (1×) |
| Corrélation BTC | `ticker/price BTCUSDT` | btc_price, btc_delta_pct par mesure | probe (1×) |

### 2.2 Robustesse réseau — `http_json()` (ligne 134)

- **Retries** : 4 tentatives avec backoff linéaire (1.2s, 2.4s, 3.6s, 4.8s).
- **Ceinture SIGALRM** (leçon du black-hole 23/08) : `signal.alarm(timeout+2)` coupe à
  coup sûr un `connect()` bloqué en SYN_SENT — un timeout socket d'urllib ne se
  déclenche PAS sur un black-hole (process vu bloqué 5 min en réel).
- **Fail-open au niveau boucle** (précis, vérifié en test 27/08) : `http_json` retry
  4× puis **lève** l'exception (ligne 166 `raise last_err`). Le système ne meurt JAMAIS
  grâce aux appelants : `run()` enveloppe chaque `tick_pair` d'un `try/except` (ligne
  2024) — une erreur réseau saute le tick de la paire concernée et conserve les
  lectures précédentes en mémoire. **Preuve production** : 27/08 10:08Z, erreurs DNS
  attrapées (`ERR KITEUSDT: nodename nor servname`), Hulk a continué avec ses positions.
  Le circuit breaker compte l'échec (voir §3.1).
- Timeout par défaut : 40s (réduit à 12-15s pour les appels critiques).

### 2.3 Scoring — `score_pair()` (ligne 309)

Un **seul fetch** 60m×15j par paire (anti double-timeout), puis :

| Indice calculé | Définition | Usage |
|---|---|---|
| `price` | close dernière bougie (corrigé par ticker/24hr) | mark |
| `range15_pct` | (max15/min15 − 1) × 100 — amplitude 15j | détection spike |
| `dd15 / dd24 / dd6` | drawdown du prix vs pic sur 15j/24h/6h | entrées COOLING/IMPULSE |
| `cadence_pct` | **médiane** des ranges journaliers (blocs 24h) | seuils dip/rip/stop adaptatifs |
| `move6 / move24` | amplitude 6h/24h | détection impulse |
| `vol_spike` (vx) | vol 6h récent / médiane des fenêtres 6h (~15j) | filtre volume small-caps |
| `vol_flag` | HOT ≥2.0 / OK ≥1.3 / DRY ≥0.8 / DEAD | blocage entrée |
| `is_small_cap` | vol24 < 400k$ OU cadence ≥ 12 | application du filtre volume |
| `dip / rip / stop` | max(plancher, cadence × mult) — **seuils adaptés à la volatilité de la paire** | entrée/sortie |
| `cool_entry / impulse_entry` | pullback minimum requis | entrée COOLING/IMPULSE |

### 2.4 Régimes de marché (5 états)

```
                    range15 ≥ 25%  ou  move24 ≥ 8%
                              │
              ┌───────────────┴───────────────┐
              │                               │
         move6 ≥ 8% ou move24 ≥ 9.6%     spike + dd15 ≥ 8%
              │          │                    │
        dd6 ≥ entrée │   sinon           impulse_now ?
              │          │                    │
         IMPULSE     IMPULSE_WAIT         oui → COOLING
                                                non → WATCH
   (range15 < 8% et move24 < 4.8%) → QUIET
```

| Régime | Définition | Comportement |
|---|---|---|
| `QUIET` | range15 < 8% et move24 < 4.8% | **aucune entrée** |
| `WATCH` | aucun signal | **aucune entrée** |
| `IMPULSE_WAIT` | impulse détecté mais pullback insuffisant | **aucune entrée** (attente) |
| `IMPULSE` | impulse + dd6 ≥ impulse_entry | **entrée** sur pullback |
| `COOLING` | vrai spike 15j + dd15 ≥ 8% | **entrée** sur pullback profond |

---

## 3. Gestion du risque (Risk Management)

### 3.1 Circuits breaker — `TradeCircuitBreaker` (hystérésis)

| Circuit | TTL | Seuil échecs | Cooldown | Donnée validée |
|---|---|---|---|---|
| `cb_btc` | **10 s** | 3 | 30 s | prix BTC fetché à chaque probe |
| `cb_gex` | **7200 s** (2 h) | 2 | 60 s | `live.json` gex `tsUnix` (cadence réelle ~1h, marge ×2) |

- **CLOSED** → données fraîches → trading autorisé.
- Échec (stale, prix ≤ 0, pas de timestamp) → compté ; **3 échecs (btc) / 2 (gex)** → **OPEN**.
- **OPEN** → `is_ok() == False` → `maybe_enter()` **refuse toute entrée nouvelle** (FIX 27/08 :
  les circuits étaient décoratifs, `is_ok()` jamais appelé — corrigé).
- Cooldown passé → **HALF-OPEN** → succès → CLOSED ; échec → re-OPEN immédiat.
- **Les sorties ne sont jamais bloquées** (on ne bloque jamais une sortie).

### 3.2 Pipeline health — multiplicateur de taille (0-1)

`Index_Maison/data/pipeline_health.json` — score de confiance de 7 sources
(binance, mempool, deribit, alternative, blockchain, google_news, sdi_ipt) :

| Mode | Score | `position_multiplier` |
|---|---|---|
| Nominal | ≥ 0.85 | × 1.0 |
| Dégradé | 0.60–0.85 | × 0.5 |
| Kill switch | < 0.60 | × 0.0 (aucun trade) |

Appliqué dans `current_notional()` : `notional *= health_mult`. Fail-open : fichier
absent → 1.0 (mais le skip RED + circuits protègent déjà).

### 3.3 Kill-switches (2 niveaux)

| Fichier | Portée | Sémantique |
|---|---|---|
| `hulk-mexc/STOP_PAPER` | Hulk seul | arrêt propre à la prochaine itération de boucle |
| `Index_Maison/STOP_ALL` | **tous les bots** | kill-switch global (vérifié à chaque cycle) |
| `veille_stale()` | Hulk | veille muette > 6h → **STANDBY** : plus de nouvel achat (l'existant est géré) |

### 3.4 Verrou anti-double-run

`fcntl.flock(LOCK_EX | LOCK_NB)` sur `runs/.paper_diprip.lock` au boot — une 2e
instance (watchdog pendant qu'un zombie traîne) **échoue immédiatement (exit 3)**
au lieu de doubler les ordres. **Testé en audit : 2e instance bloquée ✅**

---

## 4. Stratégie (Strategy Engine)

### 4.1 Boucle principale (`run()`, ligne 1981)

```
while alive:
  STOP_PAPER? STOP_ALL? → break
  tous les score_every (3) cycles → refresh_scores() + refresh_cortana_pilot()
  probe_aspiration(n)                    # sonde + circuits btc/gex
  pour chaque paire: check_wall_melt()   # murs qui fondent post-choc BTC
  pour chaque paire: check_gex_wall()    # squeeze imminent
  pour chaque paire: tick_pair(pair)     # score→gates→décision
  tous les 3 cycles → heartbeat + save_state()
  sleep(poll=20s)
```

### 4.2 Taille de position — `current_notional()` (ligne 642)

```
base = NOTIONAL_USDT (20$)
si compound ON :
  grown = base + max(0, pnl) × 0.5        (réinvestit 50% des gains)
  si pnl < 0 : grown = max(base×0.5, base + pnl×0.25)
  notional = min(max(grown, base×0.5), base × 3.0)   (cap ×3)
notional ×= pipeline_health_mult          (§3.2)
```

Puis dans `buy()` — **multiplicateurs empilés** :
```
notion = current_notional()
si paire BAG        → × BAG_POSITION_MULT (0.5)
si tier B           → × TIER_B_POSITION_MULT (0.25)   (illiquides : taille microscopique)
si pas cash_redeploy → × wall_mult(pair)               (murs : ×1.2 solide / ×0.6 fragile)
PLAFOND PROFONDEUR  → ≤ mur_bid_med × mise_max_pct_mur (2%)  [27/08]
si < 1$             → skip
```

### 4.3 Gates d'entrée — séquence complète (9 contrôles)

| # | Gate | Réf | Bloque si |
|---|---|---|---|
| 1 | **Circuits** | `maybe_enter` | `cb_btc.is_ok()` ou `cb_gex.is_ok()` False (données stale) |
| 2 | **Cash redeploy** | `maybe_enter` | cash paire ≥ 2$ + régime COOLING/IMPULSE + pullback OK → réinvestit 100% |
| 3 | **Régime** | `maybe_enter` | QUIET / WATCH / IMPULSE_WAIT → skip |
| 4 | **Déjà en position** | `maybe_enter` | pair ∈ pos ou bags |
| 5 | **MUR-SPOOF** | `maybe_enter` | sonde aspiration : façade détectée (mur fondu puis reconstruit) |
| 6 | **MUR-CASSE** | `maybe_enter` | drop mur ≥ 15%/s (bid ou ask) |
| 7 | **MUR-FAIBLE** | `maybe_enter` | `wall_strength(pair) < 0.2` (pas de support) |
| 8 | **Volume** | `maybe_enter` | small-cap et `vol_spike < 1.5` (ou DRY/DEAD en IMPULSE) |
| 9 | **Veille + cooldown** | `buy()` | veille muette (STANDBY) · cooldown post-stop · veille RED · spread > 100bps · reentry_max |

**wall_strength** (relatif, FIX 27/08) : mur actuel vs **SA médiane** (profil) plutôt
que l'absolu 30k$ — XRP 84k$ est normal pour XRP, EDEL 909$ est normal pour EDEL.
Pénalité spoof (max −50%) + bonus drop (max +20%).

### 4.4 Exécution — `buy()` (ligne 1299)

1. Vérifie tous les garde-fous (§4.3 #9).
2. `trade_qty = trade_n / price` → **`lot_filter(pair)`** (stepSize/minNotional MEXC réels).
3. `_floor_step(qty, step)` → arrondi **vers le bas** au pas du carnet.
4. `trade_n = qty × price` → **notional recalculé honnête** (pas de promesse virtuelle).
5. Skip si `trade_n < minNotional` (1$).
6. `pos[pair] = {entry, qty, qty_init, stake, ts, regime, rip, stop, cadence, notional, high, tension, sense_spread}`.
7. Journal CSV (ligne `BUY` avec raison complète — ex. `cooling_dd15=20.3>=12.3 wall=0.91🛡️`).

### 4.5 Sorties — `manage_open()` (ligne 1649)

Ordre de priorité :
1. **Stake-out** : `valeur ≥ stake × 2` → `stake_out_half()` — vend **50%** → devient bag.
2. **Stop** : `chg ≤ −stop%` → vente totale (sauf classe BAG avec `bag_no_tech_stop`).
3. **Rip scale-out 2 paliers** (16/08, « une pierre trois coups ») :

| Paire | Palier 1 | Palier 2 | Fraction vendue (de qty_init) |
|---|---|---|---|
| XRP/HBAR (liquides) | +2% | +6% | 25% ×2 |
| Small caps | +6% | +8% | 25% ×2 |

   → le « runner » garde 50% pour le gros mouvement. Tier B : rip refusé si spread > 100bps.

### 4.6 Bags, DCA, reentry — `manage_bag()`, `stake_out_half()` (lignes 1536, 1491)

| Mécanisme | Déclencheur | Action |
|---|---|---|
| Bag (post stake-out) | valeur ≥ 2× | garde 50% en bag, 50% cash |
| DCA rebuy | bag en baisse ≥ `BAG_DCA_DD_PCT` (6%) depuis le high | rachat (TTL 24h) |
| Bag slow | baisse lente ≥ 8% | DCA lent |
| Bag crash | baisse ≥ 20% | vente 90% (protection) |
| Reentry | après stop, prix redescend ≥ 6% | re-entry (max `REENTRY_MAX`=1, TTL 2h) |
| Cash redeploy | cash paire ≥ 2$ + dip | réinvestit 100% du cash de la paire |

---

## 5. Paramètres (config/defaults.env) — référence complète

### 5.1 Univers & sélection
| Param | Valeur | Rôle |
|---|---|---|
| `PAPER_PAIRS` | 17 paires (BTC, ETH + 15 small caps) | univers tradé |
| `PAPER_WATCH_PAIRS` | QNT/FLUID/RWA | univers observé |
| `PAPER_MAX_PAIRS` | 15 | max simultanées |
| `MIN_QUOTE_VOL_USDT` | 50 000 | volume min inventaire |
| `MAX_SPREAD_BPS` | 80 | spread max inventaire |
| `BUY_SPREAD_MAX_BPS` | 100 | garde spread au buy |
| `TIER_B_SPREAD_MAX_BPS` | 100 | rip refusé tier B au-delà |

### 5.2 Boucle & timing
| Param | Valeur | Rôle |
|---|---|---|
| `POLL_SEC` | 20 | période de tick |
| `SCORE_EVERY` | 3 | refresh scores tous les 3 cycles |
| `SCAN_DEADLINE_SEC` | 90 | deadline scan |
| `HINT_COOLDOWN_SEC` | 3600 | cooldown messages |

### 5.3 Capital & compound
| Param | Valeur | Rôle |
|---|---|---|
| `NOTIONAL_USDT` | 20 | mise de base |
| `COMPOUND_ON` | 1 | réinvestissement |
| `COMPOUND_FRAC` | 0.50 | part des gains réinvestie |
| `COMPOUND_MAX_MULT` | 3.0 | plafond ×3 |
| `STAKE_DOUBLE_MULT` | 2.0 | cible 2× → stake-out |
| `STAKE_SELL_FRAC` | 0.50 | fraction vendue au stake-out |
| `TIER_B_POSITION_MULT` | 0.25 | taille tier B |

### 5.4 Seuils stratégiques (adaptés à la cadence)
| Param | Valeur | Rôle |
|---|---|---|
| `DIP_FLOOR_PCT` | 4.0 | plancher dip |
| `RIP_FLOOR_PCT` | 2.0 | plancher rip |
| `STOP_FLOOR_PCT` | 6.0 | plancher stop |
| `DIP_CADENCE_MULT` | 0.50 | dip = cadence × 0.5 |
| `RIP_CADENCE_MULT` | 0.35 | rip = cadence × 0.35 |
| `STOP_CADENCE_MULT` | 0.80 | stop = cadence × 0.8 |
| `QUIET_RANGE_PCT` | 8 | seuil QUIET |
| `SPIKE_15D_PCT` | 25 | seuil spike 15j |
| `IMPULSE_PCT` | 8 | seuil impulse |
| `COOLING_DD_MIN_PCT` | 8 | dd min COOLING |
| `COOLING_PULLBACK_FRAC` | 0.28 | pullback COOLING |
| `IMPULSE_PULLBACK_MIN_PCT` | 5 | pullback min IMPULSE |
| `IMPULSE_PULLBACK_FRAC` | 0.30 | pullback IMPULSE |

### 5.5 Volume small-caps
| Param | Valeur | Rôle |
|---|---|---|
| `VOL_SMALL_CAP_USDT` | 400 000 | seuil small-cap |
| `VOL_SMALL_CADENCE` | 12 | seuil cadence small-cap |
| `VOL_SPIKE_MIN_SMALL` | 1.5 | vx min entrée small-cap |
| `VOL_HOT_SPIKE` | 2.0 | flag HOT |
| `VOL_OK_SPIKE` | 1.3 | flag OK |
| `VOL_DRY_SPIKE` | 0.8 | flag DRY |

### 5.6 Rip scale-out
| Param | Valeur | Rôle |
|---|---|---|
| `RIP_EARLY_PAIRS` | XRP, HBAR | paires à rip précoce |
| `RIP_EARLY_P1/P2_PCT` | 2.0 / 6.0 | paliers liquides |
| `RIP_LATE_P1/P2_PCT` | 6.0 / 8.0 | paliers small caps |
| `RIP_SCALEOUT_FRAC` | 0.25 | fraction par palier |
| `RIP_SELL_FRAC` | 0.50 | fraction vente rip simple |

### 5.7 Bags & DCA
| Param | Valeur | Rôle |
|---|---|---|
| `BAG_PAIRS` | CC, EDEL | classe BAG |
| `BAG_MAX_POSITIONS` | 5 | max bags |
| `BAG_POSITION_MULT` | 0.5 | taille bag |
| `BAG_NO_TECH_STOP` | 1 | pas de stop technique bag |
| `BAG_DCA_ON` | 1 | DCA activé |
| `BAG_DCA_DD_PCT` | 6 | dd déclencheur DCA |
| `BAG_SLOW_DD_PCT` | 8 | dd lent |
| `BAG_DCA_TTL_SEC` | 86 400 | TTL DCA 24h |
| `BAG_CRASH_DD_PCT` | 20 | seuil crash |
| `BAG_CRASH_SELL_FRAC` | 0.90 | vente au crash |
| `CASH_REDEPLOY_ON` | 1 | recyclage cash |

### 5.8 Reentry & cooldown
| Param | Valeur | Rôle |
|---|---|---|
| `REENTRY_ON` | 1 | reentry activé |
| `REENTRY_DD_PCT` | 6 | dd de reentry |
| `REENTRY_TTL_SEC` | 7 200 | TTL 2h |
| `REENTRY_MAX` | 1 | max reentry par paire |
| `STOP_COOLDOWN_HOURS` | 4 | cooldown post-stop |

### 5.9 Veille
| Param | Valeur | Rôle |
|---|---|---|
| `VEILLE_STALE_HOURS` | 6 | STANDBY si veille muette > 6h |
| `VEILLE_SKIP_RED_ON` | 1 | skip entrée si veille RED |
| `VEILLE_STATUS_MAX_AGE_MIN` | 30 | fenêtre RED |
| `VEILLE_STATUS_REFRESH_SEC` | 60 | refresh statut |

### 5.10 Sonde aspiration (calibration, ZÉRO effet moteur)
| Param | Valeur | Rôle |
|---|---|---|
| `ASPIRATION_ON` | 1 | sonde active |
| `ASPIRATION_DELAY_S` | 0.5 | délai entre lectures |
| `ASPIRATION_MIN_NOTIONAL_USDT` | 0 | notional min mesure |
| `ASPIRATION_PROBE_EVERY` | 1 | probe tous les cycles |
| `ASPIRATION_MAX_PAIRS` | 5 | max paires par probe |
| `ASPIRATION_SPOOF_DROP_PCT_S` | 15 | seuil spoof/drop %/s |
| `ASPIRATION_BTC_ON` | 1 | corrélation BTC active |

### 5.11 Filtre lots MEXC (FIX 27/08)
| Élément | Source | Exemple (vérifié API réelle) |
|---|---|---|
| stepSize | `baseSizePrecision` (ou dérivé `baseAssetPrecision`) | XRP **0.1** · HBAR/ZBCN/QAIT/CHIP/TEL **0.01** · BTC **0.000001** |
| minNotional | `quoteAmountPrecision` | 1.0 $ partout (vérifié) |
| Arrondi | `_floor_step` vers le bas | buy ET sell |
| Fail-open | API down → (None, None) | on trade comme avant (paper) |

---

## 6. Persistance & reproductibilité

| Fichier | Écriture | Contenu | Usage |
|---|---|---|---|
| `PAPER_V1_<ts>.csv` | append à chaque opération | ts, pair, event, regime, price, entry, qty, pnl, pnl_total, cadence, reason | journal complet des trades + skips (audit trail) |
| `PAPER_V1_<ts>_state.json` | tous les 3 cycles (atomic) | ts, pnl, notional, trades, positions, bags, bag_dca, pair_cash, reentry, scores, pairs, wall_melt_events | reprise `--resume` |
| `ASPIRATION_CALIB_<ts>.csv` | chaque probe | 18 colonnes (ts, pair, regime, asp_side, drops, spread, walls, spoof, btc, …) | calibration des murs 48h |
| `.paper_diprip.lock` | boot | PID | verrou anti-double-run |

- **Écriture atomique** du state : `tempfile.mkstemp` + `os.replace` (24/08, codeur) —
  jamais d'état à moitié écrit si le Mac coupe.
- **Resume** (`--resume`) : recharge positions/bags/cash/scores/pnl/trades du dernier
  state → tient les positions pendant les coupures (24/08, Christophe).

---

## 7. Surveillance & opérations (Monitoring)

| Brique | Cadence | Rôle |
|---|---|---|
| **watchdog_hulk_ghost.sh** (plist 120s) | 2 min | relance Hulk si mort (avec `--resume`) ; vérifie veille + digest + state |
| **Veilleuse synapses** (plist 10 min) | 10 min | intégrité md5 des fichiers surveillés + fraîcheur → INTRUSION détectée |
| **sante_index** (plist 5 min) | 5 min | 12 chaînes complètes (HULK inclus : process, CSV, analyzer, pilot, analyses) |
| **Heartbeat Hulk** | 60 s | open/bags/cash/mise/pnl/régimes/cb/gex/Cortana/health |
| **DIGEST_LATEST** | chaque cycle digest_watch | veille : signaux → skip RED |
| **Registre v1.4.6** | md5 | 35 fichiers déclarés + fraîcheurs (pilot, live.json, whales, cpfp, regime_couleur) |

**Boucles externes consommées par Hulk** :
- **Cortana analyzer** (plist 300s) → `cortana_analysis.json` → recommandation la **plus sévère** (TTL 30 min, sinon niveau `stale`) → affichée au heartbeat.
- **Cortana pilot** (07:45/jour) → `cortana_pilot.json` → propositions de paramètres, mode **ADVISORY** (jamais exécuté par Hulk).
- **Pipeline health** → multiplicateur de taille.
- **live.json (thermo)** → GEX walls + fraîcheur.

---

## 8. Limites & zones d'observation (transparence)

1. **Paper trading** — aucun ordre réel. Les frais estimés (0.05% taker) sont calculés
   dans le feed cockpit, pas déduits du PnL moteur.
2. **Sonde aspiration en OBSERVATION** — collecte + affichage + gates murs actives
   (spoof/drop), mais calibration complète en cours (CSV 18 colonnes).
3. **Profils BTC/ETH en collecte** — ajoutés 27/08 comme banc de preuve des indices
   onchain ; leurs murs n'ont pas encore 50 échantillons (wall_strength → neutre 0.5).
4. **Cortana ADVISORY** — ses propositions ne sont PAS appliquées (justesse 54.3% <
   60% → prudence ; mode pas encore ENFORCED).
5. **Une seule bourse** (MEXC) — pas de routage multi-venue, pas de frais maker.

---

## 8bis. Matrice de vérification — preuve par preuve (audit 27/08, test à l'appui)

Légende : **TEST** = exécuté en direct le 27/08 (unit test ou données réelles MEXC) ·
**LU** = code vérifié ligne à ligne · **LOG** = extrait des fichiers de production.

| Composant | Type | Preuve | Résultat |
|---|---|---|---|
| `score_pair` (régimes + seuils) | TEST | 4 paires réelles MEXC (XRP/RIZE/BTC/EDEL) | XRP=COOLING (dd15 15%≥8) · RIZE=IMPULSE · BTC=WATCH (dd15 1.6%<8) · EDEL=IMPULSE — diagramme §2.4 exact |
| Seuil `COOLING_DD_MIN_PCT`=8 | TEST | XRP dd15=14.99% → COOLING / BTC dd15=1.57% → WATCH | seuil 8 validé en réel (pas 6) |
| `current_notional` (compound) | TEST | 7 scénarios (pnl ±, plafond, plancher, health) | 7/7 exacts : 20→35→60 (cap ×3) →15→10 (plancher ×0.5) →×0.5 health →0.0 kill |
| `http_json` normal | TEST | appel réel MEXC | OK 0.22s (BTC 79 960) |
| `http_json` échec | TEST | 404 forcé | **lève après retries** (ligne 166) — fail-open assuré par la boucle, pas par http_json (nuance documentée §2.2) |
| Fail-open boucle | LOG | 27/08 10:08Z `ERR KITEUSDT: nodename nor servname` | Hulk a continué (positions vivantes) — preuve production |
| Gate G1 circuits | TEST | `maybe_enter` + cb ouvert | skip `CB ouvert (btc=OPEN gex=OPEN)` ✅ |
| Gate G3 régime QUIET | TEST | `maybe_enter` + sc QUIET | skip ✅ |
| Gate G4 déjà en position | TEST | `maybe_enter` + pair ∈ pos | skip ✅ |
| Gate G5 MUR-SPOOF | TEST | `maybe_enter` + aspiration.spoof | skip `MUR-SPOOF (façade détectée)` ✅ |
| Gate G6 MUR-CASSE | TEST | `maybe_enter` + drop 22%/s ≥ 15 | skip `MUR-CASSE (drop 22.0%/s ≥ 15)` ✅ |
| Gate G7 MUR-FAIBLE | TEST | `maybe_enter` + ws=0.1 < 0.2 | skip `MUR-FAIBLE (score=0.10)` ✅ |
| Gate G8 volume dry | TEST | `maybe_enter` + vx=0.9<1.27 DRY small-cap | skip `vol_dry_vx=0.90<1.27_DRY` ✅ |
| Gate G2 cash redeploy | TEST | `maybe_redeploy_cash` + cash 3.5$ COOLING | `CASH REDEPLOY 3.50$ → buy(cash_redeploy_3.50, notion=3.5)` ✅ (cash<2$ → non · en position → non) |
| Gate G9 cooldown | TEST | `entry_gate_check` + stop simulé | `SKIP_COOLDOWN: stop@18:00Z left≈201m` ✅ (aucun cooldown → OK) |
| Gate G9 veille RED | LOG | 18:21Z `SKIP_VEILLE_RED \| RIZEUSDT` | skip réel en production ✅ |
| Gate murs en prod | LOG | `MUR-CASSE (drop 22%/s)` XRP · `MUR-SPOOF` QAIT | skip réels 18:21Z ✅ |
| Circuit breaker | TEST | unit test 11 scénarios (CLOSED→OPEN→HALF-OPEN→CLOSED) | 11/11 ✅ |
| Verrou anti-double-run | TEST | 2e instance lancée | bloquée (fcntl LOCK_EX\|LOCK_NB) ✅ |
| `lot_filter` stepSize | TEST | API réelle exchangeInfo | XRP 0.1 · HBAR/ZBCN/QAIT/CHIP/TEL 0.01 · BTC 0.000001 · minNotional 1.0 ✅ |
| Pipeline health | LU+LOG | `global_score 0.95 · position_multiplier 1.0` (10.9 min) | nominal ✅ |
| `wall_strength` relatif | LU | SA médiane profil vs absolu 30k$ | fix 27/08 confirmé ligne à ligne ✅ |
| Plafond de mise ≤ mur×2% | LU | code `buy()` | cap confirmé ✅ |
| Entrée réelle (boucle complète) | LOG | CSV 27/08 `RWAINCUSDT BUY ... cooling_dd15=20.3>=12.3 wall=0.91🛡️` | boucle gates→buy prouvée en prod ✅ |
| Sorties (stop/rip/stake) | LOG | CSV stops -6%/-8.37%/-14.58% · rip paliers 1+2 PYTH/KITE/CHIP | exécution réelle ✅ |
| Watchdog | LOG | `PAPER: OK pid=8886 · CHECK_DONE` (2 min) | sain ✅ |
| sante_index | LOG | 12/12 chaînes OK | sain ✅ |
| Veilleuse | LOG | `✅ STABLE` (18:25Z) | sain ✅ |

**Ce qui reste LU (non exécuté) :** `manage_open` (sorties) et `manage_bag`/`stake_out_half`
sont vérifiés ligne à ligne + prouvés par les logs de production (stops/rips/stake-out réels),
mais pas rejoués en isolation — l'exécution en production de ces mêmes chemins est la preuve.

---

## 9. Preuves de fonctionnement (extraits réels au moment de l'audit)

| Preuve | Extrait |
|---|---|
| Heartbeat | `open=11 bags=0 dca=0 cash_pairs=7(39.0$) mise=19.89$ trades=22 pnl=-0.4494$ \| cb:CLOSED gex=$82K` |
| Gate murs | `BUY skip XRPUSDT MUR-CASSE (drop 22.0%/s ≥ 15)` |
| Gate spoof | `BUY skip QAITUSDT MUR-SPOOF (façade détectée)` |
| Gate veille | `SKIP_VEILLE_RED \| RIZEUSDT \| WATCH_PULLBACK` |
| Entrée réelle | `RWAINCUSDT BUY ... cooling_dd15=20.3>=12.3 wall=0.91🛡️` |
| Stop exécuté | `RIZEUSDT SELL ... stop-14.58%_avant_2x tier=B spread=58.9bps` |
| Rip scale-out | `PYTHUSDT SELL_PARTIAL ... rip_8.2pct_palier2_sell_25pct tier=A spread=0.0bps` |
| Watchdog | `PAPER: OK pid=8886 · PAPER_STATE age=2s · CHECK_DONE` (toutes les 2 min) |
| sante_index | `12/12 chaînes OK · état OK` |
| Veilleuse | `✅ STABLE — tout est en ordre` |
| Circuit breaker | test unitaire 11 scénarios : CLOSED→OPEN→HALF-OPEN→CLOSED ✅ |
| Verrou | 2e instance bloquée (fcntl LOCK_EX\|LOCK_NB) ✅ |

---

## 10. Registre des risques & mitigations

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| R1 | API MEXC down / black-hole | moyenne | élevée | http_json retries + SIGALRM + circuits (3 échecs → OPEN) + fail-open lectures précédentes |
| R2 | Données stale (live.json figé) | faible | élevée | cb_gex TTL 2h (cadence réelle 1h, marge ×2) + pipeline_health |
| R3 | Mur de façade (spoof) | moyenne | moyenne | gate MUR-SPOOF (sonde 2 lectures) + wall_strength pénalité |
| R4 | Mur qui s'effondre | moyenne | moyenne | gate MUR-CASSE (drop ≥15%/s) + check_wall_melt post-choc BTC |
| R5 | Slippage sur mur fin | élevée (small caps) | moyenne | plafond de mise ≤ 2% du mur médian (profil) + tier B ×0.25 |
| R6 | Double instance (zombie + watchdog) | faible | élevée | verrou fcntl → exit 3 |
| R7 | Veille morte (muette) | faible | moyenne | veille_stale → STANDBY (plus d'achat) |
| R8 | Ordre invalide (quantité hors pas) | faible | élevée (réel) | lot_filter stepSize/minNotional au buy ET au sell |
| R9 | Marché imprévisible (small caps) | certaine | — | stops adaptés à la cadence, bags no-tech-stop, DCA, crash-sell 90% |
| R10 | Perte d'état (coupure) | faible | élevée | save_state atomique tous les 3 cycles + resume |

---

*Document généré pour audit technique — standards de présentation institutionnelle
(architecture → données → stratégie → risque → exécution → portefeuille → surveillance).
Chaque affirmation du §9 est un extrait réel des fichiers de production au 27/08 18:25Z.*
