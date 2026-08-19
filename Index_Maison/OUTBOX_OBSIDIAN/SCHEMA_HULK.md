# 🗺️ SCHEMA HULK — référence rapide (mise à jour 16/08/2026)

> **But** : comprendre HULK en 2 minutes, sans relire tous les docs. À tenir à jour à chaque chantier.

## 1. En une phrase

**HULK = paper trading "dip & rip" sur MEXC spot** : achète les descentes de ~15 paires small
caps (watchlist CMC « The Hulk Portfolio Picks »), revend les remontées. 20$ par trade, **argent
fictif** (paper), jamais live. Dossier : `~/ace777-test-day1/hulk-mexc/` — **ne touche pas ACE/genesis**.

## 2. Les 2 axes (LA clé de lecture — typologie verrouillée 15/08)

| Axe | Question | Source | A | B |
|---|---|---|---|---|
| **TIER** | *Le marché peut-il exécuter ?* (liquidité) | `data/universe_mexc_inventory.csv` (inventaire MEXC) | liquide → pleine mise | illiquide/spike → **×0.25** (watch) |
| **CLASSE** | *Comment on gère ?* (stratégie) | `BAG_PAIRS` (config) | core → stop technique 6% | bag institutionnel → **pas de stop**, taille ×0.5, horizon 12 mois |

**Règle d'or** : un bag (classe B) = UNIQUEMENT institutionnel vérifié (≥3 participants officiels,
no pre-mine, burn-mint). **CCUSDT (Canton) = seul bag actif.** Les autres small caps = trading
tactique (classe A) avec les filtres tier.

## 3. Les 2 pistes (séparées volontairement — docs/TRACKS_SEPARES.md)

```
PISTE A (exécution)          PISTE B (veille / anticipation)
paper_diprip.py              digest_watch.py --live
règles froides, trade        scans MEXC en boucle, écrit DIGEST_LATEST.md
runs/PAPER_V1_*.csv          pour Qwen/Cortana (ne trade PAS)
└── confrontation en fin de campagne : docs/CONFRONTATION.md
```

## 4. Arborescence (où est quoi)

```
hulk-mexc/
├── SCHEMA_HULK.md            ← CE FICHIER
├── README.md                 ← vision + commandes de base
├── STOP_PAPER / STOP_DIGEST  ← garde-fous (toucher = arrêt, ghost ne relance pas)
├── config/defaults.env       ← TOUTE la config (136 lignes, commentée)
├── data/
│   ├── universe_hulk_seed.csv        ← watchlist CMC brute
│   └── universe_mexc_inventory.csv   ← inventaire MEXC + TIERS (A/B) ← référence liquidité
├── docs/
│   ├── PLAN.md               ← stratégie v0 (dip/rip, tiers)
│   ├── TRACKS_SEPARES.md     ← pourquoi 2 pistes
│   ├── CONFRONTATION.md      ← bilan paper vs veille (22-26/07 : −8.36$)
│   ├── PROTOCOLE_GHOST.md    ← watchdog (fix AbandonProcessGroup 16/08)
│   └── SPEC/CHANTIER_FIX_TIER_RIP_2026-08-16.md ← fix du 16/08
├── scripts/
│   ├── paper_diprip.py       ← PISTE A : le bot (boucle 20s)
│   ├── digest_watch.py       ← PISTE B : la veille
│   ├── inventory_mexc.py     ← rafraîchit l'inventaire (tiers)
│   ├── watchdog_hulk_ghost.sh← gardien launchd (relance si mort, 2 min)
│   ├── veille_gates.py       ← kill-switch veille (STANDBY si DIGEST vieux >6h)
│   ├── cortana_contract.py   ← contrat Cortana (ADVISORY, n'applique rien <60%)
│   └── consulter_famille_*.py← consultations famille (protocole maison)
├── strategie/
│   ├── cortana_pilot.json    ← propositions Cortana (ADVISORY)
│   └── kelly_ombre.json      ← sizing Kelly (ombre : n'applique rien, 0/4 win → 0$)
└── runs/                     ← PREUVES : CSV + state.json + DIGEST_LATEST.md + logs
```

## 5. Flux de décision du bot (paper_diprip.py)

```
toutes les 20s, par paire :
 1. SCORE     → régime (WATCH/COOLING/IMPULSE/IMPULSE_WAIT) + dip/rip/stop (cadence×mult)
 2. GATES     → veille fraîche (<6h) · tier (B = ×0.25) · spread ≤100 bps · cooldown 4h post-stop
                · REENTRY_MAX=1 · sense (carnet) · bag max 5
 3. BUY       → mise = 20$ (×0.5 si bag B, ×0.25 si tier B)
 4. GESTION   →  +rip_pct (~2%)  → VENDRE 50% (SELL_PARTIAL, 1 seule fois) ← NOUVEAU 16/08
                +100% (2×)       → VENDRE 50% → reste = BAG maison
                −stop_pct (~6%)  → STOP + cooldown 4h + compteur re-entry
 5. BAGS      → lent (−8%) → DCA · crash (−20%) → vendre 90%
 6. CASH      → récupéré → redeploy 100% sur le prochain dip
```

## 6. Config clé (config/defaults.env)

| Param | Valeur | Sens |
|---|---|---|
| `NOTIONAL_USDT` | 20 | mise de base |
| `DIP_FLOOR_PCT` / `RIP_FLOOR_PCT` / `STOP_FLOOR_PCT` | 4 / 2 / 6 | seuils mini dip/rip/stop (%) |
| `TIER_B_POSITION_MULT` | 0.25 | tier B = taille microscopique (16/08) |
| `BUY_SPREAD_MAX_BPS` / `TIER_B_SPREAD_MAX_BPS` | 100 | garde spread (16/08) |
| `RIP_SELL_FRAC` | 0.50 | vente partielle au rip (16/08) |
| `REENTRY_MAX` / `STOP_COOLDOWN_HOURS` | 1 / 4 | re-entry borné (16/08) |
| `BAG_PAIRS` / `BAG_POSITION_MULT` / `BAG_NO_TECH_STOP` | CCUSDT / 0.5 / 1 | classe B (famille 15/08) |
| `CORTANA_MODE` | ADVISORY | Cortana propose, n'applique pas |
| `VEILLE_STALE_HOURS` | 6 | DIGEST vieux >6h → STANDBY (pas de nouvel achat) |
| `SEED_ON` / `COMPOUND_ON` | 1 / 1 | réalisme baissier / compound |

## 7. Commandes

```bash
cd ~/ace777-test-day1/hulk-mexc
# Lancer paper (PISTE A)
rm -f STOP_PAPER STOP_DIGEST && python3 scripts/paper_diprip.py
# Lancer veille (PISTE B, autre terminal)
python3 scripts/digest_watch.py --live
# Arrêter (le ghost ne relancera pas)
touch STOP_PAPER STOP_DIGEST
# Rafraîchir l'inventaire (tiers)
python3 scripts/inventory_mexc.py
# Ghost : launchd com.ace777.hulk-watchdog (toutes les 2 min, relance si mort)
launchctl list | grep hulk
```

## 8. Lire les résultats

- **CSV** : `runs/PAPER_V1_*.csv` → colonnes `ts,pair,event,regime,price,entry,qty,pnl_usdt,pnl_total,cadence,reason`
  (raisons utiles : `rip_*` = take-profit partiel, `stop-*%_avant_2x` = stop, `REENTRY_MAX`, `tier=`, `spread=`)
- **State** : `runs/PAPER_V1_*_state.json` → positions ouvertes, pnl_total, bags
- **Veille** : `runs/DIGEST_LATEST.md` (paires classées par tension/spread)

## 9. État au 16/08 (historique des fixes)

| Date | Chantier | Statut |
|---|---|---|
| 22-26/07 | Campagne 1 : −8.36$ (5 stops) — confrontation veille meilleure | bilan |
| 15/08 | 2 classes A/B (bags) + contrat Cortana + kill-switch veille + fix réseau veille | ✅ |
| 16/08 | **FIX TIER/RIP** : tier B ×0.25, rip partiel 50%, re-entry max 1, spread ≤100 | ✅ (famille 4/4, codeur validé) |
| 16/08 | **Fix ghost** : AbandonProcessGroup (paper mourait en boucle) | ✅ |

## 10. Prochaines améliorations en attente (backlog)

- A/B tier B 0.25 vs watch-only après 2 semaines (réserve deepseek)
- Kelly : passer en actif si win_rate ≥50% sur ≥20 trades (ombre actuellement)
- Cortana : appliquer si justesse ≥60% (44% actuellement)
- Filtre volume dynamique (réserve codestral)
