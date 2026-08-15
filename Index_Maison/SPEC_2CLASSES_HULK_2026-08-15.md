# SPEC — 2 classes de paires Hulk (core liquides vs small caps bag) — 15/08/2026

**Cible** : `hulk-mexc/scripts/paper_diprip.py` + `hulk-mexc/config/defaults.env`
**Nature** : HORS genesis. Réversible. Famille consultée (gemini 70% / nvidia 72%, GO-AVEC-RÉSERVE sur le concept — cette spec l'implémente fidèlement).
**Sécurité** : `BAG_PAIRS` **vide par défaut** → comportement INCHANGÉ tant qu'on ne déclare aucune paire bag. Premier bag proposé : CCUSDT (Canton, vérifié ce jour).

## Principe
- **Classe A (core liquides)** : XRP, HBAR + tout le reste — règles actuelles (filtres stricts, stop technique, taille pleine).
- **Classe B (small caps bag)** : paires listées dans `BAG_PAIRS` — règles d'exception famille :
  - taille par position = `BAG_POSITION_MULT` × notionnel normal ;
  - plafond `BAG_MAX_POSITIONS` positions bag simultanées ;
  - **PAS de stop technique** (illiquide → chassé) : le bag tient (stake-out 2× conservé) ;
  - filtres volume (`vol_ok_for_entry`) et spread (`sense_ok`) ASSOUPLIS (on accepte DEAD/DRY et spreads larges).

## DIFF EXACT

### 1. `paper_diprip.py` — config `__init__` (après `self.veille_stale_h = ...`)
OLD :
```
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
```
NEW :
```
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
        # === 2 classes de paires (famille 15/08) ===
        self.bag_pairs = {
            p.strip().upper() for p in (cfg.get("BAG_PAIRS") or "").split(",") if p.strip()
        }
        self.bag_max_positions = max(1, int(float(cfg.get("BAG_MAX_POSITIONS", "5"))))
        self.bag_position_mult = float(cfg.get("BAG_POSITION_MULT", "0.5"))
        self.bag_no_tech_stop = cfg.get("BAG_NO_TECH_STOP", "1").strip() not in ("0", "false", "False")
```

### 2. `paper_diprip.py` — helper `is_bag` (juste après `def tier`)
OLD :
```
    def tier(self, pair: str) -> str:
        return (self.inv.get(pair) or {}).get("tier", "A")
```
NEW :
```
    def tier(self, pair: str) -> str:
        return (self.inv.get(pair) or {}).get("tier", "A")

    def is_bag(self, pair: str) -> bool:
        """Classe B (small caps bag) : règles d'exception."""
        return pair in self.bag_pairs
```

### 3. `paper_diprip.py` — `sense_ok` : assouplir le spread pour les bags
OLD :
```
        tier = self.tier(pair)
        allow_wide = tier == "B" or "IMPULSE" in regime
```
NEW :
```
        tier = self.tier(pair)
        allow_wide = tier == "B" or "IMPULSE" in regime or self.is_bag(pair)
```

### 4. `paper_diprip.py` — `vol_ok_for_entry` : pas de filtre volume pour les bags
OLD :
```
    def vol_ok_for_entry(self, sc: dict, regime: str) -> tuple[bool, str]:
        if not sc.get("is_small_cap"):
            return True, "vol_ok_liq"
```
NEW :
```
    def vol_ok_for_entry(self, sc: dict, regime: str) -> tuple[bool, str]:
        if sc.get("pair") and self.is_bag(str(sc.get("pair"))):
            return True, "vol_ok_bag"  # Classe B : pas de filtre volume (accumulation sur périodes sèches)
        if not sc.get("is_small_cap"):
            return True, "vol_ok_liq"
```

### 5. `paper_diprip.py` — `buy` : plafond positions bag + taille réduite
OLD :
```
        ok, why = self.sense_ok(pair, sc, regime)
        if not ok:
            say("warn", f"[{utc_now()}] BUY skip {pair} sense={why}")
            return
        trade_n = float(notion) if notion is not None else self.current_notional()
        if trade_n < 1.0:
            return
```
NEW :
```
        ok, why = self.sense_ok(pair, sc, regime)
        if not ok:
            say("warn", f"[{utc_now()}] BUY skip {pair} sense={why}")
            return
        if self.is_bag(pair):
            bag_open = sum(1 for p in self.pos if self.is_bag(p))
            if bag_open >= self.bag_max_positions:
                say("warn", f"[{utc_now()}] BAG MAX {pair} ({bag_open}/{self.bag_max_positions})")
                self.log(
                    pair, "SKIP", regime, price, price, 0.0, 0.0,
                    sc.get("cadence_pct"), f"BAG_MAX:{bag_open}",
                )
                return
        trade_n = float(notion) if notion is not None else self.current_notional()
        if self.is_bag(pair):
            trade_n = trade_n * self.bag_position_mult
        if trade_n < 1.0:
            return
```

### 6. `paper_diprip.py` — `manage_open` : pas de stop technique pour les bags
OLD :
```
        if chg <= -float(p.get("stop") or 6):
            proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
            self.add_pair_cash(pair, proceeds)
```
NEW :
```
        if not (self.is_bag(pair) and self.bag_no_tech_stop):
            if chg <= -float(p.get("stop") or 6):
                proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
                self.add_pair_cash(pair, proceeds)
```

### 7. `paper_diprip.py` — heartbeat : compter les bags ouverts
OLD :
```
                _stale, _sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
                standby = f" | STANDBY({_sreason})" if _stale else ""
```
NEW :
```
                _stale, _sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
                standby = f" | STANDBY({_sreason})" if _stale else ""
                _bag_open = sum(1 for p in self.pos if self.is_bag(p))
```
OLD :
```
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby} "
                    f"cortana={len(self.cortana_pending)}",
```
NEW :
```
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby} "
                    f"cortana={len(self.cortana_pending)} bag={_bag_open}/{self.bag_max_positions}",
```

### 8. `defaults.env` — config (après `CORTANA_PILOT_FILE=...`)
OLD :
```
# Contrat Cortana ↔ moteur : ADVISORY = propositions loggées, JAMAIS appliquées tant que justesse < 60%
CORTANA_MODE=ADVISORY
CORTANA_PILOT_FILE=strategie/cortana_pilot.json
```
NEW :
```
# Contrat Cortana ↔ moteur : ADVISORY = propositions loggées, JAMAIS appliquées tant que justesse < 60%
CORTANA_MODE=ADVISORY
CORTANA_PILOT_FILE=strategie/cortana_pilot.json
# === 2 classes de paires (famille 15/08) ===
# Classe B = small caps bag (institutionnel sous-radar) : taille réduite, PAS de stop technique, filtres assouplis
# (BAG_PAIRS vide par défaut = comportement inchangé ; premier bag proposé : CCUSDT)
BAG_PAIRS=
BAG_MAX_POSITIONS=5
BAG_POSITION_MULT=0.5
BAG_NO_TECH_STOP=1
```

## VÉRIFICATIONS ATTENDUES
1. `python3 -m py_compile paper_diprip.py` → OK.
2. Test isolé : `BAG_PAIRS=` → `is_bag("CCUSDT")==False`, comportement inchangé ; avec `BAG_PAIRS=CCUSDT` → `is_bag==True`, `vol_ok_for_entry` sur un sc bag DEAD/vol_spike 0.1 → `(True,"vol_ok_bag")`, `manage_open` n'applique pas le stop.
3. Aucun impact sur les ventes/stops des classes A, ni sur le kill-switch / contrat Cortana.

## CONTRAINTES
- `BAG_PAIRS` vide par défaut (aucun changement tant qu'on ne déclare rien).
- Ne rien changer d'autre. Le stop « fondamental » (départ d'un partenaire / delist / volume mort 3 mois) reste un suivi humain pour l'instant (documenté).
