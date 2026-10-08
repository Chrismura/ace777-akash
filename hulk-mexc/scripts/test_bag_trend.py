#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_bag_trend.py — test isolé de la logique BAG PILOTÉ PAR LE TREND (08/10/2026).

Construit un bot FACTICE via object.__new__ (aucun __init__ → aucun réseau) et
vérifie les invariants de `_manage_trend_open` et `manage_bag` :

  1. SOUCHE (core) : un bag kind="core" n'est JAMAIS vendu par manage_bag.
  2. HAUSSIER    : palier 1 (0,6×amp) vend bien la fraction prévue.
  3. TRAILING    : après un pic armé, un repli > giveback sort le reste.
  4. BAISSIER    : au niveau de rachat, le cash RACHÈTE des jetons (bag grossit).
  5. STOP        : sous entry×(1−1,5×amp), la position tradable est soldée.
  6. SANS amp7   : on ne décide pas (règle #8) — aucune vente.

Lit le VRAI moteur (paper_diprip.py). 0 €, aucun ordre.
"""
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))
from paper_diprip import PaperBot  # noqa: E402


def make_bot(amp=10.0, trend="haussier", qty=10.0, entry=1.0):
    bot = object.__new__(PaperBot)
    # infra minimale
    bot.pos = {"TESTUSDT": {
        "entry": entry, "qty": qty, "qty_init": qty, "stake": entry * qty,
        "high": entry, "regime": "COOLING", "cadence": "10.0", "rip_step": 0,
        "trend_mode": 1, "trend_label": trend,
    }}
    bot.bags = {}
    bot.bag_dca = {}
    bot.conservation = {}
    bot.pair_cash = {}
    bot.pnl_total = 0.0
    bot.trades = 0
    bot.inv = {}
    bot.lot_cache = {"TESTUSDT": (0.0001, 1.0)}
    bot.scores = {"TESTUSDT": {"amp7_pct": amp, "cadence_pct": amp,
                               "trend_label": trend, "regime": "COOLING"}}
    bot.log = lambda *a, **k: None
    # config trend-bag
    bot.bt_stop_mult = 1.5
    bot.bt_up_p1, bot.bt_up_p2, bot.bt_up_frac = 0.6, 1.2, 0.15
    bot.bt_up_gb, bot.bt_up_core, bot.bt_up_add = 0.6, 0.30, 0.5
    bot.bt_dn_p1, bot.bt_dn_p2, bot.bt_dn_frac = 0.4, 0.8, 0.25
    bot.bt_dn_gb, bot.bt_dn_core, bot.bt_dn_rebuy = 0.4, 0.15, 1.0
    bot.bt_neu_p1, bot.bt_neu_p2, bot.bt_neu_frac = 0.5, 1.0, 0.20
    bot.bt_neu_gb, bot.bt_neu_core = 0.4, 0.20
    bot.bag_crash_dd = 20.0
    bot.bag_crash_sell_frac = 0.90
    bot.bag_dca_on = True
    bot.bag_slow_dd = 8.0
    bot.bag_dca_dd = 6.0
    bot.bag_dca_ttl = 86400

    def fake_sell(pair, price, reason, qty=None):
        p = bot.pos[pair]
        full = p["qty"]
        sq = full if qty is None else min(qty, full)
        bot.sales.append((reason, round(sq, 6), round(price, 6)))
        left = full - sq
        if left <= full * 0.001:
            del bot.pos[pair]
        else:
            p["qty"] = left
        return price * sq

    bot.sales = []
    bot.sell_trade = fake_sell
    bot.add_pair_cash = lambda pair, u: bot.pair_cash.__setitem__(
        pair, bot.pair_cash.get(pair, 0.0) + u)
    bot.take_pair_cash = lambda pair, u=None: bot.pair_cash.pop(pair, 0.0)
    bot.lot_filter = lambda pair: bot.lot_cache.get(pair, (None, None))
    return bot


def test_core_jamais_vendu():
    bot = make_bot()
    bot.bags["TESTUSDT"] = {"entry": 1.0, "qty": 3.0, "kind": "core", "high": 2.0}
    bot.manage_bag("TESTUSDT", 0.5, bot.scores["TESTUSDT"])   # dd -50%
    ok = bot.sales == [] and bot.bags.get("TESTUSDT", {}).get("qty") == 3.0
    return ok, f"core intact après dd -50% : ventes={bot.sales}"


def test_palier_haussier():
    bot = make_bot(amp=10.0, trend="haussier", qty=10.0)
    # 0.6×amp = +6 % → px 1.06
    bot._manage_trend_open("TESTUSDT", 1.06, bot.scores["TESTUSDT"])
    # palier vend qty_init(10) × 0.15 = 1.5
    ok = len(bot.sales) == 1 and abs(bot.sales[0][1] - 1.5) < 1e-6
    return ok, f"palier1 vendu : {bot.sales}"


def test_trailing():
    bot = make_bot(amp=10.0, trend="haussier", qty=10.0)
    # tick 1 : +6 % → le palier 1 se déclenche (ordre voulu : palier AVANT trailing)
    bot._manage_trend_open("TESTUSDT", 1.06, bot.scores["TESTUSDT"])
    n1 = len(bot.sales)
    # tick 2 : pic +20 % (≥ 1,0×amp → armé), prix 1,10 = -8,3 % sous pic > 0,6×amp(6 %)
    bot.pos["TESTUSDT"]["high"] = 1.20
    bot._manage_trend_open("TESTUSDT", 1.10, bot.scores["TESTUSDT"])
    ok = n1 == 1 and len(bot.sales) == 2 and bot.pos.get("TESTUSDT") is None
    return ok, f"palier puis trailing : {bot.sales}"


def test_rachat_baissier():
    bot = make_bot(amp=10.0, trend="baissier", qty=10.0)
    bot.pair_cash["TESTUSDT"] = 5.0     # 5 $ de cash des paliers
    # rachat à entry×(1-1,0×amp/100) = 0.90 → on passe px 0.89
    bot._manage_trend_open("TESTUSDT", 0.89, bot.scores["TESTUSDT"])
    q = bot.pos["TESTUSDT"]["qty"]
    ok = q > 10.0 and bot.pair_cash.get("TESTUSDT", 0.0) == 0.0
    return ok, f"jetons {10.0} → {q:.4f} (rachat plus bas), cash=0"


def test_stop_amplitude():
    bot = make_bot(amp=10.0, trend="haussier", qty=10.0)
    # stop = entry×(1-1,5×amp/100) = 0.85 → px 0.84
    bot._manage_trend_open("TESTUSDT", 0.84, bot.scores["TESTUSDT"])
    ok = bot.pos.get("TESTUSDT") is None and len(bot.sales) == 1
    return ok, f"stop amplitude solde : {bot.sales}"


def test_sans_amp7():
    bot = make_bot(amp=0.0, trend="haussier", qty=10.0)
    bot.scores["TESTUSDT"]["amp7_pct"] = 0.0
    bot.scores["TESTUSDT"]["cadence_pct"] = 0.0
    bot._manage_trend_open("TESTUSDT", 0.50, bot.scores["TESTUSDT"])
    ok = bot.sales == [] and bot.pos.get("TESTUSDT") is not None
    return ok, "aucune décision sans amp7 (règle #8)"


def main():
    tests = [
        ("1 core jamais vendu", test_core_jamais_vendu),
        ("2 palier haussier", test_palier_haussier),
        ("3 trailing amplitude", test_trailing),
        ("4 rachat baissier", test_rachat_baissier),
        ("5 stop amplitude", test_stop_amplitude),
        ("6 sans amp7 → rien", test_sans_amp7),
    ]
    ok_n = 0
    for nom, fn in tests:
        try:
            ok, detail = fn()
        except Exception as e:
            ok, detail = False, f"EXCEPTION {e!r}"
        print(f"[{'OK ' if ok else 'KO '}] {nom:24s} {detail}")
        ok_n += 1 if ok else 0
    print(f"\n=== {ok_n} tests OK, {len(tests)-ok_n} échecs ===")
    return 0 if ok_n == len(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
