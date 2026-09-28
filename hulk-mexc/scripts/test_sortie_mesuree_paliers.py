#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_sortie_mesuree_paliers.py — R17, paliers de sortie relus dans l'unité de la paire.

Ce que ce test PROUVE, sur le code RÉEL (`paper_diprip.py`, pas une copie) :
  1. PLANCHER : si la paire bouge MOINS que la cadence de référence, le palier est
     EXACTEMENT celui d'avant → aucune protection retirée (assertion dure).
  2. MESURE  : si la paire bouge PLUS que la référence, le palier s'élargit dans son
     rapport mesuré → le moteur vend PLUS TARD que l'ancien réglage, et on le voit
     à l'exécution (l'ancien réglage vend à +3 %, le nouveau ne vend pas).
  3. cadence absente/vide → comportement d'avant, à l'identique (fail-safe).

Isolation déclarée : `_profils()` est neutralisé pour atteindre le ladder RIP (les paires
à profil TRAILING sortent AVANT ce bloc, par conception — le test le dit et ne le cache pas).
Lecture seule : on ne vend RIEN (sell_trade est un stub qui enregistre).
"""
import importlib
import os
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS not in sys.path:
    sys.path.insert(0, SCRIPTS)

pd = importlib.import_module("paper_diprip")
PaperBot = pd.PaperBot
pd._profils = lambda: {}          # isolation déclarée : on cible le ladder RIP


def faire_bot(cadence, on, ref=7.30, early=True):
    """Bot minimal, branché sur le VRAI manage_open.

    `early=True` → la paire est dans RIP_EARLY_PAIRS : ladder 2 %/6 % (le cas du chiffrage).
    `early=False` → ladder LATE 6 %/8 % (small caps), testé séparément.
    """
    b = object.__new__(PaperBot)
    b.pos = {"TESTUSDT": {"entry": 100.0, "qty": 10.0, "stake": 1000.0, "high": 100.0,
                          "stop": 6.0, "cadence": cadence, "rip_step": 0,
                          "qty_init": 10.0}}
    b.scores = {}
    b.bags, b.bag_dca, b.pair_cash = {}, {}, {}
    b.inv, b.lot_cache = {}, {}
    b.pnl_total, b.trades, b.double_mult = 0.0, 0, 2.0
    b.bag_no_tech_stop = True
    b.rip_early_pairs = {"TESTUSDT"} if early else set()
    b.rip_early_p1, b.rip_early_p2 = 2.0, 6.0
    b.rip_late_p1, b.rip_late_p2 = 6.0, 8.0
    b.rip_scaleout_frac = 0.25
    b.rip_cadence_on = on
    b.rip_cadence_ref = ref
    b.tier_b_spread_max, b.tier_b_position_mult = 100.0, 0.25
    b.sell_full_amplitude_guard, b.sell_full_require_invalidation = 12.0, 1
    b.sell_full_guard_degraded, b.dust_sweep_min_notional = 1, 1.0
    b.sell_partial_cascade = 1
    b.stop_cooldown_h = 24
    b.vendu = []
    b.log = lambda *a, **k: None
    b.sell_trade = lambda pair, price, reason, qty=None: (b.vendu.append((reason, qty)), 0.0)[1]
    b.add_pair_cash = lambda *a, **k: None
    b.lot_filter = lambda p: (None, None)
    b.is_bag = lambda p: False
    b.arm_reentry = lambda *a, **k: None
    b.tier = lambda p: "A"
    return b


def palier_reel(cadence, on, pct, ref=7.30, early=True):
    """Fait tourner manage_open à entry×(1+pct/100) et dit si un palier RIP a été vendu."""
    b = faire_bot(cadence, on, ref, early)
    b.manage_open("TESTUSDT", 100.0 * (1 + pct / 100.0))
    return [r for r, _ in b.vendu if r.startswith("rip_")]


ok = True


def verifier(libelle, condition, detail=""):
    global ok
    ok = ok and condition
    print(f"  {'✅' if condition else '❌'} {libelle}{(' — ' + detail) if detail else ''}")


print("TEST — palier de sortie piloté par la MESURE (R17) sur le code réel\n")

# 1. PLANCHER — cadence 3 %/j (<< référence 7,30) : le palier NE BOUGE PAS.
off = palier_reel(3.0, False, 2.05)
on = palier_reel(3.0, True, 2.05)
verifier("cadence faible : le palier d'avant est CONSERVÉ (+2,05 % vend)",
         bool(off) and bool(on), f"off={off} on={on}")

# 2. PLANCHER strict — au niveau exact d'avant +2 %, les deux vendent (aucune protection retirée).
verifier("palier exact (+2,00 %) vend dans les deux cas",
         bool(palier_reel(3.0, False, 2.0)) and bool(palier_reel(3.0, True, 2.0)))

# 3. MESURE — cadence 20 %/j (2,7× la référence) : le palier s'élargit, donc à +3 %
#    l'ANCIEN réglage vend et le NOUVEAU NE VEND PAS. C'est la preuve d'exécution.
off20 = palier_reel(20.0, False, 3.0)
on20 = palier_reel(20.0, True, 3.0)
verifier("cadence forte : l'ancien réglage vend à +3 %", bool(off20), f"off={off20}")
verifier("cadence forte : le nouveau NE vend PAS à +3 % (palier élargi à sa mesure)",
         not on20, f"on={on20}")

# 4. La mesure exacte : cadence 20 / réf 7,30 = 2,7397 → palier1 = 2 % × 2,7397 = 5,4795 %.
b = faire_bot(20.0, True)
b.manage_open("TESTUSDT", 100.0 * (1 + 5.40 / 100.0))
verifier("à +5,40 % (< 5,4795 % mesuré) le nouveau palier ne vend pas encore",
         not [r for r, _ in b.vendu if r.startswith("rip_")])
b2 = faire_bot(20.0, True)
b2.manage_open("TESTUSDT", 100.0 * (1 + 5.55 / 100.0))
verifier("à +5,55 % (> 5,4795 %) il vend", any(r.startswith("rip_") for r, _ in b2.vendu))
# 4c. RIEN DE SILENCIEUX (#6) : la raison de vente écrit le palier ET la mesure qui l'a produit,
#     donc le journal prouve à lui seul que la décision vient de la mesure.
_raison = next((r for r, _ in b2.vendu if r.startswith("rip_")), "")
verifier("la raison de vente écrit le palier effectif + la cadence mesurée",
         "niv5.5pct" in _raison and "cad20.0" in _raison and "rel2.74" in _raison, _raison)

# 4b. LADDER LATE (small caps 6 %/8 %) — même règle, mesurée de la même façon.
#     cadence 20/7,30 = 2,7397 → palier1 = 6 % × 2,7397 = 16,44 % : à +10 % l'ancien
#     réglage vend, le nouveau NE vend PAS → le moteur vend plus tard, à sa mesure.
verifier("ladder LATE : l'ancien vend à +10 %, le nouveau non",
         bool(palier_reel(20.0, False, 10.0, early=False)) and
         not palier_reel(20.0, True, 10.0, early=False),
         f"off={palier_reel(20.0, False, 10.0, early=False)} "
         f"on={palier_reel(20.0, True, 10.0, early=False)}")
verifier("ladder LATE : vend bien au-delà de 16,44 % (+17 %)",
         bool(palier_reel(20.0, True, 17.0, early=False)))

# 5. CADENCE ABSENTE — comportement d'avant, à l'identique (fail-safe).
auc = palier_reel(0.0, True, 2.05)
verifier("cadence absente : comportement d'avant conservé", bool(auc), f"on={auc}")

# 6. L'échelle vient bien de la CONFIG (aucun multiplicateur caché dans le code).
_env = open(os.path.join(SCRIPTS, "..", "config", "defaults.env"), encoding="utf-8").read()
verifier("l'échelle est déclarée dans la config (RIP_CADENCE_REF_PCT=7.30)",
         "RIP_CADENCE_REF_PCT=7.30" in _env and "RIP_CADENCE_MESURE_ON=1" in _env)
ref_haute = bool(palier_reel(20.0, True, 3.0, ref=40.0))   # rel=0,5 → plancher 1 → palier 2 % : vend
ref_basse = bool(palier_reel(20.0, True, 3.0, ref=1.0))    # rel=20  → palier 40 % : ne vend pas
verifier("changer la référence change le palier (la mesure pilote vraiment)",
         ref_haute is True and ref_basse is False,
         f"réf 40 → vend={ref_haute} (plancher 1) · réf 1 → vend={ref_basse} (palier 40 %)")

print(f"\n{'✅ TOUS LES TESTS PASSENT' if ok else '❌ ÉCHEC — ne pas câbler'}")
sys.exit(0 if ok else 1)
