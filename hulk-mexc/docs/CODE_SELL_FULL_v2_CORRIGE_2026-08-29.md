# Réponse codeur — 2e passe SELL FULL corrigée (provider Google Gemini, 5.0s, 2026-08-29T11:35:02.343113+00:00)

Corrections intégrées. Voici le diff exact, complet et applicable intégrant la correction critique 1 (`sc` dans `manage_open`), la correction majeure 2 (chargement des variables de configuration dans `__init__`), ainsi que la sécurisation de l'ordre d'évaluation de l'invalidation (`dd15 < -5.0` en premier).

```diff
--- hulk-mexc/scripts/paper_diprip.py
+++ hulk-mexc/scripts/paper_diprip.py
@@ -529,6 +529,11 @@
         self.rip_late_p2 = float(cfg.get("RIP_LATE_P2_PCT", "8.0"))
         self.rip_scaleout_frac = float(cfg.get("RIP_SCALEOUT_FRAC", "0.25"))
+        self.sell_full_amplitude_guard = float(cfg.get("SELL_FULL_AMPLITUDE_GUARD", "12.0"))
+        self.sell_full_require_invalidation = int(cfg.get("SELL_FULL_REQUIRE_INVALIDATION", "1"))
+        self.sell_full_guard_degraded = int(cfg.get("SELL_FULL_GUARD_DEGRADED", "1"))
+        self.dust_sweep_min_notional = float(cfg.get("DUST_SWEEP_MIN_NOTIONAL", "1.0"))
+        self.sell_partial_cascade = int(cfg.get("SELL_PARTIAL_CASCADE", "1"))
         self.reentry_max = max(1, int(float(cfg.get("REENTRY_MAX", "1"))))
         self.reentry_count: dict[str, int] = {}
@@ -1875,6 +1880,7 @@
         sortie quand le prix redonne giveback sous le pic. Zéro 2× / zéro rip
         paliers (ils contrediraient le « laisser courir »)."""
         p = self.pos[pair]
+        sc = self.scores.get(pair) or {}
         t_arm = float(p.get("trail_arm_pct") or 0)
         t_gb = float(p.get("trail_giveback_pct") or 0)
         chg = float(p.get("chg_pct") or 0)
@@ -1885,8 +1891,32 @@
         if t_arm > 0 and t_gb > 0:
             # backstop dur : le stop fixe reste (protection)
             if chg <= -float(p.get("stop") or 6):
-                proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
-                self.add_pair_cash(pair, proceeds)
+                # SPEC v2 — Verrous 1 & 2 & Bloc 1/2 : Garde-fou SELL full en forte amplitude
+                move24 = float(sc.get("move24_pct") or 0.0)
+                vol_spike = sc.get("vol_spike")
+                dd15 = float(sc.get("dd15_pct") or 0.0)
+                
+                is_degraded = (vol_spike is None)
+                invalidation_valid = (not self.sell_full_require_invalidation) or is_degraded or (dd15 < -5.0 or vol_spike == 0)
+                
+                if move24 > self.sell_full_amplitude_guard and not invalidation_valid and not (is_degraded and not self.sell_full_guard_degraded):
+                    # Bascule en vente partielle 50% + Verrou 1 (Dust Sweeper)
+                    part_qty = p["qty"] * 0.5
+                    step, _mn = self.lot_filter(pair)
+                    rem_qty = p["qty"] - part_qty
+                    rem_val = rem_qty * price
+                    min_q = step if step else 0.0
+                    
+                    if rem_qty < min_q or rem_val < self.dust_sweep_min_notional:
+                        proceeds = self.sell_trade(pair, price, f"dust_sweep_stop_guard_{pair}")
+                        guard_tag = "DUST_SWEEP"
+                    else:
+                        proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_guard_partial_50", qty=part_qty)
+                        guard_tag = "SELL_PARTIAL"
+                    self.add_pair_cash(pair, proceeds)
+                    p["guard_last"] = guard_tag
+                else:
+                    proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
+                    self.add_pair_cash(pair, proceeds)
                 return
             # trailing : armé quand le pic ≥ arm, sortie si le prix redonne
@@ -1914,8 +1944,32 @@
         if not (self.is_bag(pair) and self.bag_no_tech_stop):
             if chg <= -float(p.get("stop") or 6):
-                proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
-                self.add_pair_cash(pair, proceeds)
+                # SPEC v2 — Verrous 1 & 2 & Bloc 1/2 : Garde-fou SELL full en forte amplitude (branche 2)
+                move24 = float(sc.get("move24_pct") or 0.0)
+                vol_spike = sc.get("vol_spike")
+                dd15 = float(sc.get("dd15_pct") or 0.0)
+                
+                is_degraded = (vol_spike is None)
+                invalidation_valid = (not self.sell_full_require_invalidation) or is_degraded or (dd15 < -5.0 or vol_spike == 0)
+                
+                if move24 > self.sell_full_amplitude_guard and not invalidation_valid and not (is_degraded and not self.sell_full_guard_degraded):
+                    part_qty = p["qty"] * 0.5
+                    step, _mn = self.lot_filter(pair)
+                    rem_qty = p["qty"] - part_qty
+                    rem_val = rem_qty * price
+                    min_q = step if step else 0.0
+                    
+                    if rem_qty < min_q or rem_val < self.dust_sweep_min_notional:
+                        proceeds = self.sell_trade(pair, price, f"dust_sweep_stop_guard_{pair}")
+                        guard_tag = "DUST_SWEEP"
+                    else:
+                        proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_guard_partial_50", qty=part_qty)
+                        guard_tag = "SELL_PARTIAL"
+                    self.add_pair_cash(pair, proceeds)
+                    p["guard_last"] = guard_tag
+                else:
+                    proceeds = self.sell_trade(pair, price, f"stop-{p['stop']}%_avant_2x")
+                    self.add_pair_cash(pair, proceeds)
                 return
 
             # 16/08 soir (Christophe) : RIP scale-out 2 paliers
--- hulk-mexc/defaults.env
+++ hulk-mexc/defaults.env
@@ -45,2 +45,9 @@
 REENTRY_MAX=1
 SEED_BAGS_ON=1
+
+# Garde-fou SELL full en forte amplitude (SPEC v2 29/08)
+SELL_FULL_AMPLITUDE_GUARD=12
+SELL_FULL_REQUIRE_INVALIDATION=1
+SELL_PARTIAL_CASCADE=1
+DUST_SWEEP_MIN_NOTIONAL=1.0
+SELL_FULL_GUARD_DEGRADED=1
```
