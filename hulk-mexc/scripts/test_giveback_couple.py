#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_giveback_couple.py — test isolé du GIVEBACK COUPLE A L'AMPLITUDE (09/10/2026, GO « go 1,2,3 »).

Construit un bot FACTICE via object.__new__ (aucun __init__ → aucun réseau) et vérifie,
dans `manage_open` (chemin trailing, hors trend_mode) :

  1. FLAG OFF : le giveback reste celui du profil (comportement HISTORIQUE strict).
  2. FLAG ON  : le giveback monte à max(profil, frac × amp7) → la sortie est PLUS TARDIVE.
  3. FLAG ON  : la raison de vente écrit la valeur COUPLÉE (preuve que la valeur est bien lue).
  4. FLAG ON + amp7 = 0 : on ne décide pas (règle #8) — giveback inchangé.
  5. FLAG ON + profil > frac×amp7 : le max garde le profil (pas de rétrécissement).

Lit le VRAI moteur (paper_diprip.py). 0 €, aucun ordre.
"""
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))
import paper_diprip as pd          # noqa: E402
from paper_diprip import PaperBot  # noqa: E402

# Profil factice : giveback CARNET = 1,33 pt, arm = 3,3 %  (valeurs réelles de WUSDT)
pd._profils = lambda: {"WUSDT": {"calib": {"trail_arm_pct": 3.3, "trail_giveback_pct": 1.33}}}


def make_bot(gb_on=1, frac=0.5, amp7=10.9, entry=1.0, high=1.20):
    bot = object.__new__(PaperBot)
    bot.pos = {"WUSDT": {"entry": entry, "qty": 10.0, "qty_init": 10.0,
                         "stake": entry * 10.0, "high": high, "regime": "COOLING"}}
    bot.scores = {"WUSDT": {"amp7_pct": amp7, "cadence_pct": 10.0, "regime": "COOLING"}}
    bot.pair_cash = {}
    bot.gb_couple_on = gb_on
    bot.gb_couple_frac = frac
    bot.sales = []
    bot.sell_trade = lambda pair, price, reason, qty=None: (
        bot.sales.append((reason, price)) or price * (qty or 10.0))
    bot.add_pair_cash = lambda pair, u: bot.pair_cash.__setitem__(
        pair, bot.pair_cash.get(pair, 0.0) + u)
    bot.lot_filter = lambda pair: (0.0001, 1.0)
    return bot


def _triggers_gb(bot, price):
    bot.manage_open("WUSDT", price)
    if bot.sales:
        r = bot.sales[0][0]
        import re
        m = re.search(r"giveback([0-9.]+)", r)
        return True, (float(m.group(1)) if m else None)
    return False, None


def test_flag_off_gb_profil():
    bot = make_bot(gb_on=0)
    vendu, gb = _triggers_gb(bot, 1.16)          # +16 % vs pic +20 % → marge 4 pt
    return (vendu and gb == 1.33), f"OFF → vendu={vendu} giveback={gb} (attendu 1.33)"


def test_flag_on_sort_tardive():
    bot = make_bot(gb_on=1, amp7=10.9)           # 0,5 × 10,9 = 5,45 pt
    vendu, _ = _triggers_gb(bot, 1.16)           # marge 4 pt < 5,45 → NE sort PAS
    return (not vendu), f"ON → vendu={vendu} (attendu False : giveback élargi à 5,45)"


def test_flag_on_raison_couplee():
    bot = make_bot(gb_on=1, amp7=10.9)
    vendu, gb = _triggers_gb(bot, 1.14)          # marge 6 pt > 5,45 → sort
    return (vendu and gb == 5.45), f"ON → vendu={vendu} giveback={gb} (attendu 5.45)"


def test_flag_on_amp7_nul():
    bot = make_bot(gb_on=1, amp7=0.0)
    vendu, gb = _triggers_gb(bot, 1.16)
    return (vendu and gb == 1.33), f"ON, amp7=0 → vendu={vendu} giveback={gb} (attendu 1.33)"


def test_max_garde_profil():
    bot = make_bot(gb_on=1, amp7=1.0)            # 0,5 × 1,0 = 0,5 pt < 1,33 → garde 1,33
    vendu, gb = _triggers_gb(bot, 1.16)
    return (vendu and gb == 1.33), f"ON, petit amp7 → vendu={vendu} giveback={gb} (attendu 1.33)"


def main():
    tests = [
        ("1 flag OFF → giveback profil", test_flag_off_gb_profil),
        ("2 flag ON → sortie plus tardive", test_flag_on_sort_tardive),
        ("3 flag ON → raison = valeur couplée", test_flag_on_raison_couplee),
        ("4 flag ON, amp7=0 → inchangé", test_flag_on_amp7_nul),
        ("5 flag ON, profil > frac×amp7 → profil", test_max_garde_profil),
    ]
    ok_n = 0
    for nom, fn in tests:
        try:
            ok, detail = fn()
        except Exception as e:
            ok, detail = False, f"EXCEPTION {e!r}"
        print(f"[{'OK ' if ok else 'KO '}] {nom:34s} {detail}")
        ok_n += 1 if ok else 0
    print(f"\n=== {ok_n} tests OK, {len(tests)-ok_n} échecs ===")
    return 0 if ok_n == len(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
