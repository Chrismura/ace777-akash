#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_seellfull_guard.py — Test isolé de la garde SELL full (SPEC v2, copie de test).

Construit un bot FACTICE via object.__new__ (aucun __init__ → aucun réseau) et
vérifie les 3 branches de decide/exit du stop dans manage_open :

  A) amplitude forte (> guard) SANS invalidation  → SELL_PARTIAL 50% (qty réduit, pos reste ouverte)
  B) amplitude forte AVEC invalidation (dd15<-5)  → SELL full (100%)
  C) amplitude faible                             → SELL full (100%) [comportement historique]

Lit le module de la COPIE de test (paper_diprip_SELLFULL_TEST.py), jamais le moteur réel.
"""
import importlib
import shutil
import sys
from pathlib import Path

# Cache la copie d'origine puis importe-la via importlib (pour que __file__ existe)
SRC = Path(__file__).resolve().parent
TMP = SRC / "_sci_test_module"
TMP.mkdir(exist_ok=True)
shutil.copy(SRC / "paper_diprip_SELLFULL_TEST.py", TMP / "paper_diprip_SELLFULL_TEST.py")
sys.path.insert(0, str(TMP))
PaperBot = importlib.import_module("paper_diprip_SELLFULL_TEST").PaperBot


def make_bot(sc: dict, pos_qty: float = 10.0):
    bot = object.__new__(PaperBot)
    # attrs conf (SPEC v2)
    bot.sell_full_amplitude_guard = 12.0
    bot.sell_full_require_invalidation = 1
    bot.sell_full_guard_degraded = 1
    bot.dust_sweep_min_notional = 1.0
    # infra
    bot.scores = {"TESTUSDT": dict(sc)}
    bot.pos = {
        "TESTUSDT": {
            "entry": 1.0, "qty": pos_qty,
            "stop": 6.0,            # config req par manage_open (stop %)
            "rip_step": 0, "high": 1.0,
            "stake": 1.0 * pos_qty,
            "regime": "COOLING", "cadence": "",
        }
    }
    bot.lot_cache = {"TESTUSDT": (0.0001, 1.0)}
    bot.double_mult = 2.0
    bot.bag_no_tech_stop = False
    bot.bags = {}
    bot.bag_dca = {}
    bot.pair_cash = {}
    bot.pnl_total = 0.0
    bot.trades = 0
    bot.reentry_count = {}
    bot.inv = {}
    return bot


def run(bot, price=1.0):
    """Appelle la branche de gestion du stop via manage_open (mock des sorties)."""
    results = {"sells": []}

    def fake_sell(pair, price, reason, qty=None):
        p = bot.pos[pair]
        full = p["qty"]
        sq = qty if qty is not None else full
        results["sells"].append((reason, round(sq, 6)))
        left = full - sq
        if left <= full * 0.001:
            del bot.pos[pair]
        else:
            p["qty"] = left
        return price * sq

    def fake_add(pair, proceeds):
        bot.pair_cash[pair] = bot.pair_cash.get(pair, 0.0) + proceeds

    bot.sell_trade = fake_sell
    bot.add_pair_cash = fake_add
    bot.lot_filter = lambda pair: bot.lot_cache.get(pair, (None, None))
    bot.is_bag = lambda pair: pair in bot.bags
    bot.arm_reentry = lambda *a, **k: None
    # meta requises par sell_trade sur d'autres chemins
    bot.stop_cooldown_h = 24
    bot.log = lambda *a, **k: None

    # prix en baisse de 10% sous entry pour déclencher le stop (-10% < -6%)
    pb = dict(bot.scores["TESTUSDT"])
    pb["price"] = 0.90
    bot.scores["TESTUSDT"] = pb
    bot.manage_open("TESTUSDT", 0.90)
    return results

ok = 0
fails = []

# ---- CAS A : amplitude forte, PAS d'invalidation → SELL_PARTIAL 50%
b = make_bot({"move24_pct": 15.0, "vol_spike": 2.0, "dd15_pct": -1.0})
r = run(b, 0.90)
assert b.pos.get("TESTUSDT"), "la position doit rester ouverte (partiel)"
assert abs(b.pos["TESTUSDT"]["qty"] - 5.0) < 1e-6, f"qty restant attendu 5.0, got {b.pos['TESTUSDT']['qty']}"
assert r["sells"] and r["sells"][0][0].endswith("guard_partial_50"), r["sells"]
print(f"[OK]   A forte amp, pas d'invalidation → SELL_PARTIAL 50% | qty restant={b.pos['TESTUSDT']['qty']}")
ok += 1

# ---- CAS B : amplitude forte AVEC invalidation (dd15<-5) → SELL full
b = make_bot({"move24_pct": 15.0, "vol_spike": 2.0, "dd15_pct": -8.0})
r = run(b, 0.90)
assert "TESTUSDT" not in b.pos, "la position doit être fermée (SELL full)"
assert r["sells"] and "_avant_2x" in r["sells"][0][0], r["sells"]
print(f"[OK]   B forte amp + invalidation → SELL full (position fermée)")
ok += 1

# ---- CAS C : amplitude faible (< guard) → SELL full (historique)
b = make_bot({"move24_pct": 8.0, "vol_spike": 2.0, "dd15_pct": -1.0})
r = run(b, 0.90)
assert "TESTUSDT" not in b.pos, "amplitude faible → SELL full"
assert r["sells"] and "_avant_2x" in r["sells"][0][0], r["sells"]
print(f"[OK]   C amplitude faible → SELL full (comportement historique)")
ok += 1

# ---- CAS D : mode dégradé (vol_spike absent) → fallback SELL full (sûr)
b = make_bot({"move24_pct": 15.0, "vol_spike": None, "dd15_pct": -1.0})
r = run(b, 0.90)
assert "TESTUSDT" not in b.pos, "mode dégradé → jamais de partiel (sûr), position fermée"
assert r["sells"] and "_avant_2x" in r["sells"][0][0], r["sells"]
print(f"[OK]   D mode dégradé → fallback SELL full (sûr)")
ok += 1

print(f"\n=== {ok} tests OK, {len(fails)} échecs ===")
sys.exit(0 if not fails else 1)