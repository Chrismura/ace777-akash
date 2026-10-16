#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_gbag_mode.py — test isolé du mode GBAG (10/10/2026, GO « go suggestion 1 »).

Construit un bot FACTICE via object.__new__ (aucun __init__ → aucun réseau) et
vérifie les invariants de `_gbag_cycle` sur des bougies 1 h synthétiques.

DISCIPLINE DES BOUGIES : la DERNIÈRE bougie du cache est « en cours » et n'est pas
décidée ; la décision porte sur l'avant-dernière (kl[-2]). Donc : appel N décide la
bougie qui était « en cours » à l'appel N−1. Chaque `pousser()` ajoute une bougie et
rend la précédente décidable.

Invariants :
  1. ENTRÉE   : close > SMA24 ET > plus-haut 24 clôt. ET > SMA240 → 1 tranche.
  2. PYRAMIDE : +8 % du dernier ajout → +1 tranche, JAMAIS au-delà de 3.
  3. SORTIE   : clôture < SMA24 → tout le tradable vendu + rachat armé à 0,5×amp7.
  4. SOUCHE   : clôture ≤ niveau → TOUT le cash converti en bag kind=core.
  5. RÈGLE #8 : amp7 non mesurée → la sortie vend MAIS aucun rachat armé.
  6. FIDÉLITÉ : aucune décision sans NOUVELLE clôture 1 h.

Lit le VRAI moteur (paper_diprip.py). 0 €, aucun ordre.
"""
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))
import paper_diprip as P  # noqa: E402
from paper_diprip import PaperBot  # noqa: E402

H = 3_600_000  # 1 h en ms


def bougie(ts, close):
    return [ts, close, close * 1.01, close * 0.99, close, 1.0]


def bougies(closes):
    """Bougies MEXC-shaped [ts, o, h, l, c, ...] alignées jours UTC (24 h)."""
    return [bougie(i * H, c) for i, c in enumerate(closes)]


def pousser(kl, close):
    """Ajoute une bougie : elle sera « en cours » à cet appel, décidable au suivant."""
    kl.append(bougie(kl[-1][0] + H, close))


def make_bot():
    bot = object.__new__(PaperBot)
    bot.pos = {}
    bot.bags = {}
    bot.bag_dca = {}
    bot.conservation = {}
    bot.pair_cash = {}
    bot.pnl_total = 0.0
    bot.trades = 0
    bot.inv = {}
    bot.scores = {"TESTUSDT": {"regime": "COOLING", "cadence_pct": 10.0}}
    bot.log = lambda *a, **k: None
    bot.gbag_on = True
    bot.gbag_pairs = {"TESTUSDT"}
    bot.gbag_rebuy_frac = 0.5
    bot.gbag_add_step = 0.08
    bot.gbag_sma_e = 24
    bot.gbag_sma_gate = 240
    bot.gbag_check_sec = 0.0
    bot.gbag_pending = {}
    bot.gbag_histo = {}
    # P2/P3 (16/10/2026, GO P1-P4) : défauts prod — porte OFF, cap OFF. Les tests
    # porte/cap les activent explicitement. (Sans ces attributs : AttributeError, la
    # même dérive harnais/moteur que P1 a fermée sur test_seellfull_resume.)
    bot.gbag_gate_amp_on = False
    bot.gbag_min_amp7 = 2.0
    bot.compound_global_cap = 0.0
    bot.deployed_total = lambda: round(sum(float((v or {}).get("stake") or 0.0) for v in bot.pos.values()), 2)
    bot.current_notional = lambda pair=None: 30.0  # signature réelle : pair optionnel (compounding par actif, 14/10)
    bot.lot_filter = lambda pair: (0.0001, 1.0)

    def fake_buy(pair, price, sc, reason, notion=None):
        if pair in bot.pos:
            return
        bot.pos[pair] = {"entry": price, "qty": (notion or 30.0) / price,
                         "qty_init": (notion or 30.0) / price,
                         "stake": notion or 30.0, "high": price,
                         "regime": "COOLING", "stop": 6.0}
        bot.achats.append((reason, notion))

    def fake_sell(pair, price, reason, qty=None):
        p = bot.pos[pair]
        q = p["qty"] if qty is None else min(qty, p["qty"])
        bot.ventes.append((reason, round(q * price, 6)))
        del bot.pos[pair]
        return q * price

    bot.achats = []
    bot.ventes = []
    bot.buy = fake_buy
    bot.sell_trade = fake_sell
    bot.add_pair_cash = lambda pair, u: bot.pair_cash.__setitem__(
        pair, bot.pair_cash.get(pair, 0.0) + u)
    bot.take_pair_cash = lambda pair, u=None: bot.pair_cash.pop(pair, 0.0)
    return bot


def appel(bot, kl, prix):
    """Un passage GBAG (klines mockées sur kl). Rend True si GBAG garde la paire."""
    P.klines = lambda pair, interval, limit: kl
    return bot._gbag_cycle("TESTUSDT", prix, bot.scores["TESTUSDT"])


# 300 bougies à 100 : SMA24=SMA240=hh24=100 ; amp7 = range (101−99)/99 ≈ 2,02 %
BASE = [100.0] * 300


def test_entree_cassure():
    kl = bougies(BASE + [110.0, 105.0])   # décide 110 (105 en cours)
    bot = make_bot()
    appel(bot, kl, 110.0)
    assert "TESTUSDT" in bot.pos, "la cassure doit ouvrir 1 tranche"
    assert bot.pos["TESTUSDT"]["gbag_tranches"] == 1
    assert bot.achats and bot.achats[0][0] == "gbag_entree_sgn"
    assert not bot.bags, "pas de souche à l'entrée (elle ne naît QUE du rachat)"


def test_pyramide_max_3():
    kl = bougies(BASE + [110.0, 119.0])   # décide 110 → entrée (last_add=110)
    bot = make_bot()
    appel(bot, kl, 110.0)
    for close_suivant, decide in ((128.6, 119.0), (139.0, 128.6), (150.0, 139.0)):
        pousser(kl, close_suivant)
        appel(bot, kl, decide)
    p = bot.pos["TESTUSDT"]
    assert p["gbag_tranches"] == 3, f"3 tranches max, obtenu {p['gbag_tranches']}"
    # 1 tranche achetée via buy() + 2 ajouts directs (patron trend_add)
    # tranche = current_notional()/3 = 30/3 = 10 $ (spec mesurée : budget 30 $ → 3×10 $)
    q_attendu = 10.0 / 110.0 + 10.0 / 119.0 + 10.0 / 128.6
    assert abs(p["qty"] - q_attendu) / q_attendu < 0.01, f"qty {p['qty']} != {q_attendu}"
    # 14/10 (GO « si oui branche » — mesuré +39,68 $ vs plat, 44 paires/45 j) : la
    # tranche s'ACHÈTE → base de coût honnête (blend) et stake = coût RÉEL payé
    # (le lot-filter floor donne 29,988 ≤ 30 — c'est l'achat honnête, pas 30 pile).
    # AVANT : les 2 ajouts étaient GRATUITS (qty += q, entry figée) → PnL surévalué.
    assert 29.9 < p["stake"] <= 30.01, f"stake payé {p['stake']} hors tranche — tranche gratuite ?"
    assert abs(p["entry"] * p["qty"] - p["stake"]) < 0.01, \
        f"base de coût entry*qty={p['entry'] * p['qty']} != stake payé {p['stake']}"
    assert p["entry"] > 110.0, f"l'entrée doit monter (blend 119/128.6), obtenu {p['entry']}"


def test_sortie_sma24_arme_rachat():
    kl = bougies(BASE + [110.0, 90.0])    # décide 110 → entrée ; 90 en cours
    bot = make_bot()
    appel(bot, kl, 110.0)
    pousser(kl, 88.0)                      # rend 90 décidable
    appel(bot, kl, 90.0)                   # décide 90 → sortie
    assert bot.ventes and bot.ventes[0][0] == "gbag_sortie_sma24", "sortie SMA24 attendue"
    assert "TESTUSDT" not in bot.pos
    pend = bot.gbag_pending.get("TESTUSDT")
    assert pend, "rachat armé attendu"
    # amp7 ≈ 2,02 % (jours à ±1 % autour de 100) → 0,5×amp7 ≈ 1,01 % sous 90 ≈ 89,09
    assert 88.9 < pend < 89.2, f"rachat attendu ~89,09, obtenu {pend}"


def test_souche_tout_le_cash():
    kl = bougies(BASE + [110.0, 90.0])
    bot = make_bot()
    appel(bot, kl, 110.0)                  # entrée
    pousser(kl, 88.0)
    appel(bot, kl, 90.0)                   # sortie + armement (pend ≈ 89,09)
    pend = bot.gbag_pending["TESTUSDT"]
    bot.pair_cash["TESTUSDT"] = 12.0       # cash de paire connu pour la mesure
    pousser(kl, 88.5)
    appel(bot, kl, 88.0)                   # décide 88 ≤ pend → conversion
    b = bot.bags.get("TESTUSDT")
    assert b, "souche attendue"
    assert b["kind"] == "core", "la souche est kind=core (jamais vendue)"
    assert bot.pair_cash.get("TESTUSDT", 0.0) == 0.0, "TOUT le cash doit être converti"
    assert "TESTUSDT" not in bot.gbag_pending, "l'ordre est consommé après conversion"
    q_attendu = 12.0 / 88.0
    assert abs(b["qty"] - q_attendu) / q_attendu < 0.01, f"souche {b['qty']} != {q_attendu}"


def test_regle8_sans_amp7():
    kl = bougies(BASE + [110.0, 90.0])
    bot = make_bot()
    bot._gbag_amp7 = lambda kl_fermes: None   # mesure absente (règle #8)
    appel(bot, kl, 110.0)                      # entrée
    pousser(kl, 88.0)
    appel(bot, kl, 90.0)                       # sortie
    assert bot.ventes, "la sortie vend quand même"
    assert not bot.gbag_pending, "règle #8 : sans amp7 mesurée, aucun rachat armé"


def test_aucune_decision_sans_nouvelle_cloture():
    kl = bougies(BASE + [110.0, 105.0])
    bot = make_bot()
    appel(bot, kl, 110.0)
    n = len(bot.achats)
    bot.gbag_histo["TESTUSDT"]["next_check"] = 0.0   # force le re-passage
    appel(bot, kl, 110.0)                            # même clôture
    assert len(bot.achats) == n, "pas de décision sans NOUVELLE clôture 1 h"


def test_gate_refuse_chop():
    # P2 : porte ON + amp7 0,5 % (< 2,0) → pas d'entrée, main rendue (False).
    kl = bougies(BASE + [110.0, 105.0])
    bot = make_bot()
    bot.gbag_gate_amp_on = True
    bot._gbag_amp7 = lambda kl_fermes: 0.5
    r = appel(bot, kl, 110.0)
    assert r is False, "chop : GBAG doit rendre la main à la gestion historique"
    assert "TESTUSDT" not in bot.pos, "chop : aucune entrée GBAG"


def test_gate_accepte_trend():
    # P2 : porte ON + amp7 5 % → l'entrée cassure a lieu, GBAG garde (True).
    kl = bougies(BASE + [110.0, 105.0])
    bot = make_bot()
    bot.gbag_gate_amp_on = True
    bot._gbag_amp7 = lambda kl_fermes: 5.0
    r = appel(bot, kl, 110.0)
    assert r is True, "trend : GBAG doit garder la paire"
    assert bot.pos["TESTUSDT"]["gbag_tranches"] == 1


def test_gate_laisse_historique():
    # P2 : position SANS marque (ouverte par la gestion historique) + porte ON →
    # rendue intacte (False), jamais hijackée par GBAG.
    kl = bougies(BASE + [110.0, 105.0])
    bot = make_bot()
    bot.gbag_gate_amp_on = True
    bot.pos["TESTUSDT"] = {"entry": 100.0, "qty": 1.0, "stake": 100.0}
    r = appel(bot, kl, 110.0)
    assert r is False, "position historique : rendre la main"
    assert "gbag_tranches" not in bot.pos["TESTUSDT"], "pas de hijack"
    assert bot.pos["TESTUSDT"]["qty"] == 1.0


def test_global_cap_pyramide():
    # P3 : cap dépassé → la tranche est refusée (loggée), position intacte.
    kl = bougies(BASE + [110.0, 119.0])
    bot = make_bot()
    bot.compound_global_cap = 5.0   # stake d'entrée = 10 $ > cap
    appel(bot, kl, 110.0)           # entrée (fake buy, stake 10)
    assert bot.deployed_total() == 10.0
    pousser(kl, 128.6)
    appel(bot, kl, 119.0)           # +8,06 % ≥ +8 % → palier pyramide...
    p = bot.pos["TESTUSDT"]
    assert p["gbag_tranches"] == 1, "cap : tranche refusée"
    assert abs(p["qty"] - 10.0 / 110.0) < 1e-9, "cap : qty intacte"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    ok = 0
    for t in tests:
        try:
            t()
            print(f"  ✔ {t.__name__}")
            ok += 1
        except AssertionError as e:
            print(f"  ✘ {t.__name__}: {e}")
    print(f"{ok}/{len(tests)} tests OK")
    sys.exit(0 if ok == len(tests) else 1)
