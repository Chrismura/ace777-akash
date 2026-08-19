# SPEC — HULK : RESPECTER TIER + RIP (garde-fous typologie) — 16/08/2026

**Statut :** à consulter famille · **Fichier cible :** `hulk-mexc/scripts/paper_diprip.py` + `config/defaults.env`
**Constat terrain :** 13→16/08 : pnl −7.02$ en **4 stops, 0 gain** (RIZE −2.48, EDEL −1.82 + −1.49, ZBCN −1.22).
Campagne 22-26/07 : −8.36$ en 5 stops (même pattern, `docs/CONFRONTATION.md`).

## La double distinction (rappel typologie, verrouillée 15/08)

| Axe | Définition | Source | A/B |
|---|---|---|---|
| **TIER** | Liquidité du marché (exécutable ?) | `data/universe_mexc_inventory.csv` (inventaire MEXC) | A = liquide · B = spike illiquide (« paper ou taille microscopique », PLAN.md) · C = skip |
| **CLASSE** | Stratégie d'investissement (comment gérer ?) | famille 15/08 (verdict smallcaps) | A = core liquides (stop technique) · B = small caps bag institutionnel (pas de stop technique, taille ×0.5, horizon 12 mois) |

**Ce qui cloche :** le moteur mélange les deux axes.
- `pick_pairs()` (l.155) filtre bien `tier=="A"`… mais `PAPER_PAIRS` en dur (15 paires dans `defaults.env`)
  **contourne le filtre** → QAIT (tier B, spread 327 bps !), RIZE (tier B, 59 bps), EDEL (tier B, 22 bps) sont tradés.
- `buy()` (l.756-758) ne réduit la taille que si `is_bag()` (classe B → ×0.5) : **un tier B illiquide reçoit la
  pleine mise 20$ comme un tier A** → stop chassé/gapé (RIZE −12.25% au lieu de −6%).
- `rip_pct` est calculé (l.353) et stocké (l.768) mais **jamais utilisé pour vendre** : `manage_open()` (l.994)
  ne fait que 2× → stake_out ou stop. PLAN.md prévoit pourtant « Sell rip/spike : rebond ≥ RIP_PCT depuis entry ».
- Re-entry : EDEL acheté **3×** (cooldown 2h trop court pour une paire en chute → −3.31$ sur une seule paire).

## Le fix (4 blocs)

### 1. Sizing par TIER dans `buy()` (après le sizing classe B existant, l.756-758)

```python
        trade_n = float(notion) if notion is not None else self.current_notional()
        if self.is_bag(pair):
            trade_n = trade_n * self.bag_position_mult
        if self.tier(pair) == "B":
            trade_n = trade_n * self.tier_b_position_mult   # NOUVEAU : tier B = taille microscopique
        if trade_n < 1.0:
            return
```

Config (defaults.env, à côté de BAG_POSITION_MULT) :
```bash
# Tier B (illiquide, PLAN.md : « paper ou taille microscopique ») — taille réduite
TIER_B_POSITION_MULT=0.25
```

### 2. `pick_pairs()` : les tier B ne passent QUE si explicitement demandés

Règle : quand `PAPER_PAIRS` est défini, chaque paire est vérifiée contre l'inventaire —
**si tier B et pas dans `PAPER_EXTRA_PAIRS` (watch explicite) → exclue** (log une fois au boot).

```python
def pick_pairs(cfg: dict, inv: dict[str, dict]) -> list[str]:
    raw = cfg.get("PAPER_PAIRS", "").strip()
    if raw:
        extra = {p.strip().upper() for p in cfg.get("PAPER_EXTRA_PAIRS", "").split(",") if p.strip()}
        out = []
        for p in raw.split(","):
            p = p.strip().upper()
            if not p:
                continue
            t = (inv.get(p) or {}).get("tier", "A")
            if t == "B" and p not in extra:
                print(f"[TIER] exclue {p} (tier B illiquide — watch via PAPER_EXTRA_PAIRS si voulu)")
                continue
            out.append(p)
        return out
    # ... (comportement actuel inchangé)
```

Note : QAIT/RIZE/EDEL restent tradables en watch mais **pas de BUY automatique** (voir §3).

### 3. Implémenter le RIP dans `manage_open()` (l.994) — vente partielle au rebond

Le PLAN prévoit « Sell rip/spike : rebond ≥ RIP_PCT depuis entry ». `sell_trade()` gère déjà les
ventes partielles (`SELL_PARTIAL`). Insertion après le calcul `chg`, AVANT le check 2× :

```python
        if chg >= float(p.get("rip") or 2.0) and not p.get("rip_done"):
            p["rip_done"] = True   # une seule vente rip par position
            sell_qty = qty * self.rip_sell_frac
            if sell_qty >= qty * 0.001:
                proceeds = self.sell_trade(pair, price, f"rip_{chg:.1f}pct_sell_{self.rip_sell_frac*100:.0f}pct", qty=sell_qty)
                self.add_pair_cash(pair, proceeds)
                return
```

Config :
```bash
# Rip (PLAN.md : vendre le rebond) — vente partielle au 1er franchissement du rip_pct
RIP_SELL_FRAC=0.50
```

⚠️ **Interaction à vérifier** : après vente rip, la position continue vers le 2× ou le stop avec
`qty` réduit (sell_trade met déjà `p["qty"] = left`). Le stop −6% s'applique alors au reste — c'est
le comportement voulu (gain partiel sécurisé, reste en course). Le bag maison (2×) n'est pas touché.

### 4. Classe B étanche + re-entry borné

- **Classe B** : AUCUN ajout à `BAG_PAIRS` sans vérification institutionnelle (règle d'or 15/08 —
  documentée, pas de code à changer : `BAG_PAIRS=CCUSDT` reste seul).
- **Re-entry** : cooldown 2h → **4h** (`STOP_COOLDOWN_HOURS=4`) + **max 1 re-entry par paire** :
  dans `buy()`, si la paire a un stop récent en cache (`runs/.hulk_stop_cache.json`) ET a déjà
  été rachetée depuis (compteur local) → SKIP `REENTRY_MAX`.

```python
# __init__ : self.reentry_count: dict[str, int] = {}
# buy() après le cooldown check existant :
if self.reentry_count.get(pair, 0) >= self.reentry_max:
    self.log(pair, "SKIP", regime, price, price, 0.0, 0.0, sc.get("cadence_pct"), f"REENTRY_MAX:{self.reentry_count.get(pair,0)}")
    return
# sell_trade() : quand event == "SELL" (position fermée) → self.reentry_count[pair] = self.reentry_count.get(pair, 0) + 1
```

Config :
```bash
STOP_COOLDOWN_HOURS=4
REENTRY_MAX=1
```

## Contraintes

1. Ne modifier QUE ces 4 blocs + les configs. Aucune autre ligne.
2. Réutiliser `sell_trade()` (gère déjà SELL_PARTIAL + cache stop) — pas de nouvelle fonction de vente.
3. Le kill-switch veille (STANDBY) et le contrat Cortana (ADVISORY) restent intacts.
4. Tout réversible par env (défauts dans defaults.env).

## Effets attendus

- RIZE/EDEL/QAIT (tier B) : plus de pleine mise — ×0.25 max, ou watch only → les stops −12% disparaissent.
- Les spikes gagnants (RED +32%, CHIP +20% du run 13-16/08) : vente partielle 50% au 1er rebond ≥ rip_pct → gains sécurisés au lieu de give-back.
- EDEL ×3 impossible (max 1 re-entry + cooldown 4h).
- Le bag CCUSDT (classe B) : inchangé.

## Questions pour la famille

1. TIER_B_POSITION_MULT=0.25 raisonnable ? (ou 0.1, ou watch-only strict ?)
2. RIP_SELL_FRAC=0.50 au 1er franchissement du rip_pct — ou vente par paliers (ex. 30% à rip, 30% à 2×rip) ?
3. Le rip doit-il s'appliquer aussi aux tier B (qui spikent fort mais illiquides) ?
4. REENTRY_MAX=1 + cooldown 4h : bons ?
