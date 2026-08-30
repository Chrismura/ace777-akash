#!/usr/bin/env python3
"""
Backtest comparatif — 3 stratégies côte à côte sur 5 jours de klines 15m réels.

Rejoue le comportement du prix (open→high→low→close) bougie par bougie et
applique, en parallèle, 3 gestionnaires différents sur le MÊME capital initial.
But : montrer ce que "attraper le couteau + sortie au pump" donne vs ce que fait
Hulk actuellement (dip/rip/stop), et vs un simple hold.

Stratégies :
  1. VANILLE  — la logique actuelle (dip → achat, rip 6/8% en 2 paliers, stop −6%)
  2. COUTEAU  — le set-up proposé : acheter au creux (pente qui se calme),
     lots croissants en descente, sortie partielle au pump moyen, runner gardé.
  3. HOLD     — acheter au prix de départ et tenir (la thèse longue).

Les 3 partent du MÊME capital (CAPITAL_USDT) et se comparent en PnL % du capital.

Ce script est un OUTIL DE RECHERCHE : il n'exécute rien sur le live.
Dépendance : /tmp/klines_5d.json (série 15m collectée via API MEXC).
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field

CAPITAL_USDT = 100.0  # capital identique pour les 3 stratégies
# Exposition initiale identique partout : on compare à capital risqué égal.
# VANILLE engage ~40% du capital à l'entrée (stake_frac) — on donne le MÊME 40%
# au HOLD pour que battre HOLD signifie vraiment "mieux que tenir", pas "plus exposé".
HOLD_STAKE = 0.40


# ---------------------------------------------------------------------------
# Modèles de marché
# ---------------------------------------------------------------------------
@dataclass
class Candle:
    t: int          # openTime ms
    o: float        # open
    h: float        # high
    l: float        # low
    c: float        # close
    v: float        # volume


def load_pairs(path="/tmp/klines_5d.json") -> dict[str, list[Candle]]:
    """Charge les klines. Si un fichier 30j Binance existe, il prend le dessus
    sur les paires qu'il couvre (fenêtre 6× plus longue)."""
    raw = json.load(open(path))
    out = {}
    for pair, arr in raw.items():
        cs = [Candle(t=int(k[0]), o=float(k[1]), h=float(k[2]),
                     l=float(k[3]), c=float(k[4]), v=float(k[5])) for k in arr]
        out[pair] = cs
    bn = None
    try:
        bn = json.load(open("/tmp/klines_binance_30d.json"))
    except FileNotFoundError:
        pass
    if bn:
        for pair, arr in bn.items():
            if len(arr) > len(out.get(pair, [])):
                out[pair] = [Candle(t=int(k[0]), o=float(k[1]), h=float(k[2]),
                                    l=float(k[3]), c=float(k[4]), v=float(k[5])) for k in arr]
    return out


# ---------------------------------------------------------------------------
# Cœur du backtest : rejoue la série et laisse le gestionnaire décider
# ---------------------------------------------------------------------------
class Backtest:
    def __init__(self, candles: list[Candle], capital: float, ema_period: int = 48):
        self.candles = candles
        self.capital0 = capital
        self.cash = capital
        self.qty = 0.0
        self.ema_period = ema_period
        self.state = {}          # dict libre pour la stratégie
        self.ema = 0.0
        self.ema_n = 0
        # registre des trades (pour la lecture)
        self.trades: list[dict] = []

    def equity(self, price: float) -> float:
        return self.cash + self.qty * price

    def buy(self, price: float, usdt: float, note: str):
        usdt = min(usdt, self.cash)
        if usdt < 0.1:
            return
        self.cash -= usdt
        self.qty += usdt / price
        self.trades.append({"t": self.candles[self.i].t, "side": "BUY",
                            "px": round(price, 6), "usdt": round(usdt, 2), "note": note})

    def sell(self, price: float, frac: float, note: str):
        q = self.qty * frac
        if q <= 0:
            return
        self.qty -= q
        self.cash += q * price
        self.trades.append({"t": self.candles[self.i].t, "side": "SELL",
                            "px": round(price, 6), "qty": round(q, 3), "note": note})

    def run(self):
        cs = self.candles
        n = len(cs)
        # état de base : prix moyen glissant lent (support estimé du couteau)
        self.state["ema"] = cs[0].c
        for i in range(n):
            self.i = i
            c = cs[i]
            if self.ema == 0:
                self.ema = c.c
                self.ema_n = 1
            else:
                alpha = 2 / (self.ema_period + 1)
                self.ema = self.ema + alpha * (c.c - self.ema)
                self.ema_n += 1
            self.decide(i, c)

    def decide(self, i: int, c: Candle):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# 1. VANILLE — la logique Hulk actuelle (simplifiée, fidèle aux CSV du run)
# ---------------------------------------------------------------------------
class Vanille(Backtest):
    def __init__(self, candles, capital, dip_pct=4.0, rip1=6.0, rip2=8.0, stop=6.0, stake_frac=0.40):
        super().__init__(candles, capital)
        self.dip_pct = dip_pct          # entrée : creux 15m ≥ dip derrière
        self.rip1, self.rip2 = rip1, rip2
        self.stop = stop
        self.stake_frac = stake_frac    # part du capital engagé à l'entrée
        self.entry = 0.0
        self.p1done = False

    def decide(self, i, c):
        if self.qty == 0:
            # entrée sur creux profond : dd depuis pic récent ≥ dip
            look = self.candles[max(0, i - 4):i]  # ~1h de contexte
            if look:
                peak = max(x.h for x in look)
                dd = (1 - c.c / peak) * 100 if peak else 0
                if dd >= self.dip_pct:
                    self.buy(c.c, self.capital0 * self.stake_frac, f"dip dd={dd:.1f}%")
                    self.entry = c.c
                    self.p1done = False
        else:
            chg = (c.c - self.entry) / self.entry * 100
            if not self.p1done and chg >= self.rip1:
                self.sell(c.c, 0.25, f"rip1 +{chg:.1f}%")
                self.p1done = True
            elif self.p1done and chg >= self.rip2:
                self.sell(c.c, 0.25, f"rip2 +{chg:.1f}%")
            if chg <= -self.stop:
                self.sell(c.c, 1.0, f"stop -{chg:.1f}%")
                self.state["cooldown"] = i + 8  # ~2h de neutralité


# ---------------------------------------------------------------------------
# 2. COUTEAU — le set-up proposé
# ---------------------------------------------------------------------------
class Couteau(Backtest):
    def __init__(self, candles, capital, ema_period=16,
                 pente_seuil=0.8,        # %/bougie max de descente encore active
                 max_cout=3.0,           # cumul de baisse sous l'EMA (vente panique)
                 lot1=0.20, lot2=0.25, lot3=0.30,  # mises décroissantes en accumulation
                 pump_seuil=7.0,         # % de rebond déclenchant une sortie partielle
                 giveback=-8.0,          # % sous pic déclenchant la sortie du runner
                 stop_large=30.0,        # stop de sécurité très large (hold, pas scalp)
                 cooldown=24):           # bougies (6h) sans ré-entrée après sortie complète
        super().__init__(candles, capital)
        self.ema_period = ema_period
        self.pente_seuil = pente_seuil
        self.max_cout = max_cout
        self.lots = [lot1, lot2, lot3]
        self.pump_seuil = pump_seuil
        self.giveback = giveback
        self.stop_large = stop_large
        self.cooldown = cooldown
        self.entry0 = 0.0
        self.batches = 0
        self.peakb = 0.0
        self.second_entry = 0.0
        self.sold_at = 0
        self.sold_half = False
        self.final = False

    def pente(self, i):
        # vitesse de baisse sur 3 bougies (~45 min) en %/bougie
        look = self.candles[max(0, i - 3):i + 1]
        c0, c1 = look[0].c, look[-1].c
        if c0 <= 0:
            return 0.0
        return (c1 / c0 - 1) * 100

    def max_cout_from_ema(self, c):
        return (1 - c.c / self.ema) * 100 if self.ema else 0

    def decide(self, i, c):
        if self.qty == 0:
            # ré-entrée interdite juste après une sortie complète (patience)
            if i < self.sold_at + self.cooldown:
                return
            if self.final:
                return
            self.batches = 0
            self.peakb = 0.0
            self.entry0 = 0.0
            self.second_entry = 0.0
            # 1) on attend une vente panique (fort dépassement sous la moyenne)
            panique = self.max_cout_from_ema(c) <= -self.max_cout
            # 2) ET que la pente se calme (le couteau ralentit = proche du sol)
            pente = self.pente(i)
            ralentit = pente > -self.pente_seuil  # pas en pleine cascade
            if panique and ralentit:
                self.buy(c.c, self.capital0 * self.lots[0], f"couteau pente={pente:.1f}%")
                self.entry0 = c.c
                self.peakb = c.c
                self.batches = 1
        else:
            # suivi du pic pour le trailing
            self.peakb = max(self.peakb, c.c)
            # accumuler sur la descente : lots 2 et 3 en dessous de l'entrée
            below = (1 - c.c / self.entry0) * 100
            if self.batches == 1 and below >= 6:
                self.buy(c.c, self.capital0 * self.lots[1], f"lot2 -{below:.1f}%")
                self.batches = 2
            elif self.batches == 2 and below >= 12:
                self.buy(c.c, self.capital0 * self.lots[2], f"lot3 -{below:.1f}%")
                self.batches = 3
            # sorties partielles RESTANTES (une seule sortie 50% au rebond)
            if self.qty > 0 and not self.sold_half:
                chg = (c.c - self.entry0) / self.entry0 * 100
                if chg >= self.pump_seuil:
                    self.sell(c.c, 0.5, f"pump +{chg:.1f}% sortie 50%")
                    self.sold_half = True
            # runner : sortir le reste si le prix redonne trop sous le pic
            giveback = (c.c - self.peakb) / self.peakb * 100 if self.peakb else 0
            if self.qty > 0 and giveback <= self.giveback:
                self.sell(c.c, 1.0, f"giveback {giveback:.1f}% sortie runner")
                self.sold_at = i
                self.sold_half = True
                self.final = True
            # stop de sécurité (effondrement réel, pas le scalp)
            if self.qty > 0 and (c.c - self.entry0) / self.entry0 * 100 <= -self.stop_large:
                self.sell(c.c, 1.0, f"stop large")
                self.sold_at = i
                self.sold_half = True
                self.final = True


# ---------------------------------------------------------------------------
# 3. HOLD — acheter au prix de départ et tenir (la thèse longue)
# ---------------------------------------------------------------------------
class Hold(Backtest):
    def __init__(self, candles, capital, stake_frac=1.0):
        super().__init__(candles, capital)
        self.stake_frac = stake_frac

    def decide(self, i, c):
        if self.qty == 0:
            self.buy(c.c, self.capital0 * self.stake_frac, "hold départ")
            self.entry0 = c.c
            # on ne vend plus jamais


# ---------------------------------------------------------------------------
# Comparateur
# ---------------------------------------------------------------------------
def main():
    pairs = load_pairs()
    print(f"{'PAIR':<11}{'VANILLE%':>10}{'COUTEAU%':>10}{'HOLD%':>8}   "
          f"{'vanille$':>9}{'couteau$':>9}{'hold$':>9}   verdict")
    print("-" * 90)
    tot = {"vanille": 0.0, "couteau": 0.0, "hold": 0.0}
    wins = {"vanille": 0, "couteau": 0, "hold": 0}
    tot_v = tot_c = tot_h = 0.0
    tot_tc = tot_tv = 0
    for pair, cs in pairs.items():
        if len(cs) < 100:
            continue
        last = cs[-1].c
        v = Vanille(cs, CAPITAL_USDT); v.run()
        c = Couteau(cs, CAPITAL_USDT); c.run()
        h = Hold(cs, CAPITAL_USDT, stake_frac=HOLD_STAKE); h.run()
        ev = v.equity(last) / CAPITAL_USDT * 100 - 100
        ec = c.equity(last) / CAPITAL_USDT * 100 - 100
        eh = h.equity(last) / CAPITAL_USDT * 100 - 100
        winner = "vanille" if ev >= ec and ev >= eh else ("couteau" if ec >= eh else "hold")
        wins[winner] += 1
        tv = v.equity(last) - CAPITAL_USDT
        tc = c.equity(last) - CAPITAL_USDT
        th = h.equity(last) - CAPITAL_USDT
        tot_v += tv; tot_c += tc; tot_h += th
        tot_tv += len(v.trades); tot_tc += len(c.trades)
        print(f"{pair:<11}{ev:>9.1f}%{ec:>9.1f}%{eh:>7.1f}%   "
              f"{tv:>+8.1f}{tc:>+8.1f}{th:>+8.1f}   "
              f"{('V' if ev>=ec and ev>=eh else ('C' if ec>=eh else 'H'))}  "
              f"({len(v.trades)}/{len(c.trades)})")
    print("-" * 90)
    print(f"TOTAL ({len(pairs):d} paires, capital {CAPITAL_USDT}$ identique déployé ×3)\n"
          f"  VANILLE : {tot_v:+.2f}$   COUTEAU : {tot_c:+.2f}$   HOLD : {tot_h:+.2f}$\n"
          f"  COUTEAU vs VANILLE : {tot_c - tot_v:+.2f}$   HOLD vs VANILLE : {tot_h - tot_v:+.2f}$\n"
          f"  Victoires par stratégie : {wins}   (trades vanille/couteau : {tot_tv}/{tot_tc})")


if __name__ == "__main__":
    main()