# CHANTIER — HULK : RESPECTER TIER + RIP — 16/08/2026

**Statut :** ✅ IMPLÉMENTÉ + TESTÉ (6/6) · **Verdict famille :** 4/4 GO-AVEC-RÉSERVE
(`scripts/CONSULTATION_FAMILLE_TIER_RIP_20260816/VERDICT_FAMILLE.md`)

## Contexte

pnl −7.02$ en 4 stops, 0 gain (13→16/08) : RIZE −2.48 (tier B, spread 59 bps, stop gapé −12.25%),
EDEL −3.31 (tier B, acheté 3× dont 2 re-entries), ZBCN −1.22. Même pattern que la campagne
22-26/07 (−8.36$, 5 stops, docs/CONFRONTATION.md). Pendant ce temps RED +32.8% / CHIP +20.7%
non vendus (give-back — cible 2× jamais atteinte).

**Cause racine (double distinction typologie)** : le moteur mélangeait les deux axes —
TIER (liquidité marché, inventaire MEXC) et CLASSE (stratégie, famille 15/08) :
- `PAPER_PAIRS` en dur (15 paires) contournait le filtre `tier=="A"` de `pick_pairs()`
- `buy()` ne réduisait la taille que pour la classe B (bag ×0.5) — un tier B illiquide recevait la pleine mise 20$
- `rip_pct` calculé mais jamais utilisé pour vendre (le PLAN.md prévoyait « Sell rip/spike »)

## Le fix (4 blocs, `scripts/paper_diprip.py` + `config/defaults.env`)

1. **pick_pairs()** : `PAPER_PAIRS` ne contourne plus le filtre tier — tier B exclu sauf watch
   explicite via `PAPER_EXTRA_PAIRS` (log `[TIER] exclue …` au boot).
2. **Sizing tier B** dans `buy()` : × `TIER_B_POSITION_MULT=0.25` (5$ au lieu de 20$).
3. **RIP implémenté** dans `manage_open()` : vente partielle `RIP_SELL_FRAC=0.50` au 1er
   franchissement du `rip_pct` (une seule fois, flag `rip_done`) ; **tier B : pas de rip si
   spread > 100 bps** (slippage). Raisons CSV : `rip_X.Xpct_sell_50pct` + tier/spread loggés.
4. **Re-entry borné** : `REENTRY_MAX=1` + `STOP_COOLDOWN_HOURS=4` (au lieu de 2) — compteur par
   paire incrémenté à chaque fermeture, **reset si gain**.
5. **Garde spread au buy** (réserve famille) : spread inventaire > `BUY_SPREAD_MAX_BPS=100` → SKIP,
   même tier A (protège contre les paires mal classées, ex. QAIT 327 bps).

## Décisions famille intégrées (verdict 16/08)

| Question | Verdict | Décision |
|---|---|---|
| TIER_B_POSITION_MULT | 0.25 OK partout (0.1 trop restrictif) | **0.25** |
| RIP 50% unique ou paliers | 50% unique (3/4) | **RIP_SELL_FRAC=0.50** |
| Rip sur tier B ? | OUI si spread < 100 bps | **condition spread** |
| REENTRY_MAX=1 + 4h | GO (3/4) + reset après gain | **1 / 4h / reset gain** |
| Garde spread au buy | gemini + nvidia + codestral | **BUY_SPREAD_MAX_BPS=100** |

## Validation

- [x] `py_compile` OK
- [x] Test 1 : pick_pairs exclut RIZE/EDEL (tier B), garde QAIT (extra watch)
- [x] Test 2 : comportement auto (sans PAPER_PAIRS) inchangé
- [x] Test 3 : RIP partiel 50% au 1er franchissement (+5% → vend 50%)
- [x] Test 4 : pas de 2e rip (flag `rip_done`)
- [x] Test 5 : tier B spread > 100 → pas de rip (QAIT 327 bps)
- [x] Test 6 : compteur re-entry incrémenté sur perte, reset sur gain
- [x] Smoke boot config réelle : EDEL exclue, QAIT/RIZE en watch ×0.25, 14 paires actives

## Effets attendus (à vérifier sur le prochain run paper)

1. Plus de stop −12% (RIZE) : les tier B sont à ×0.25 → perte max ~0.60$ au lieu de 2.48$.
2. Les spikes gagnants (type RED +32%) : vente partielle 50% au 1er rebond → gains sécurisés.
3. EDEL ×3 impossible (REENTRY_MAX=1 + cooldown 4h).
4. Bags CCUSDT (classe B) inchangés.

## Rollback (1 commande)

```bash
cd ~/ace777-test-day1/hulk-mexc && git checkout -- scripts/paper_diprip.py config/defaults.env
```

## Métriques de validation (après ~10 trades paper)

1. **Stops** : plus aucun stop au-delà de −7% (avant : −12.25% gapé).
2. **%SELL_PARTIAL rip** : les raisons `rip_*` doivent apparaître dans le CSV.
3. **PnL** : tendance vers ≥ 0 (avant : −7.02 sur 3 jours, −8.36 sur 4 jours).
4. **REENTRY_MAX** : plus de `BUY` d'une paire 2× après stop dans la même session.
5. Si les tier B restent négatifs à 0.25 → passer en watch-only (réserve deepseek).

## Réversibilité / sauvegarde

- Backup git : `git checkout --` (les 2 fichiers sont suivis).
- La spec : `docs/SPEC_FIX_TIER_RIP_2026-08-16.md` · verdict : `scripts/CONSULTATION_FAMILLE_TIER_RIP_20260816/`.
