#!/usr/bin/env python3
"""
AUDIT — Détection de trend : méthodes institutionnelles confrontées aux données réelles.

Compare côte à côte les principaux signaux de régime utilisés par les fonds :
  1. MA200 (prix > moyenne 200j)          — le classique des fonds actions
  2. MA50/MA200 (croisement)              — le "golden/death cross"
  3. Rendement 60j glissant               — la méthode de décomposition des papers (bull>+15% / bear<-15%)
  4. Momentum 1 mois (TSMOM)              — Moskowitz et al., utilisé par Man Group
  5. MA200 + vol (couche vol)             — combinaison trend + régime de volatilité

Pour chaque méthode, on mesure :
  - % du temps "haussier" vs "baissier"
  - rendement moyen des jours haussiers vs baissiers (le signal sépare-t-il les bons des mauvais jours ?)
  - le "lag" : combien de jours après un vrai sommet/creux le signal bascule (réactivité)
  - le ratio de Sharpe conditionnel

Données : /tmp/btc_daily.json (300 bougies 1j Binance). OUTIL DE RECHERCHE — n'exécute rien.
"""
from __future__ import annotations
import json


def load() -> list[float]:
    raw = json.load(open("/tmp/btc_daily.json"))
    return [float(k[4]) for k in raw]  # closes


def sma(closes: list[float], n: int, i: int) -> float:
    if i < n - 1:
        return float("nan")
    return sum(closes[i - n + 1:i + 1]) / n


def ema_series(closes: list[float], n: int) -> list[float]:
    out: list[float] = []
    alpha = 2 / (n + 1)
    e = closes[0]
    for c in closes:
        e = c if e is None else e + alpha * (c - e)
        out.append(e)
    return out


def audit(name: str, closes: list[float], long_signal: list[bool]) -> dict:
    """Évalue la qualité d'un signal long/bear."""
    n = len(closes)
    rets = [(closes[i] / closes[i - 1] - 1) * 100 for i in range(1, n)]
    ls = long_signal[1:]  # aligné sur rets
    long_days = [r for r, s in zip(rets, ls) if s]
    short_days = [r for r, s in zip(rets, ls) if not s]
    avg_long = sum(long_days) / len(long_days) if long_days else 0
    avg_short = sum(short_days) / len(short_days) if short_days else 0
    # séparation : rendement annuelisé si on suit le signal (long les jours verts, cash sinon)
    cum = 1.0
    for r, s in zip(rets, ls):
        cum *= 1 + (r / 100 if s else 0) / 100
    tot = (cum - 1) * 100
    pct_long = sum(1 for s in ls if s) / len(ls) * 100
    # Sharpe du signal
    rets_sig = [r / 100 if s else 0 for r, s in zip(rets, ls)]
    import statistics
    mu = sum(rets_sig) / len(rets_sig)
    sd = statistics.stdev(rets_sig) if len(rets_sig) > 1 else 0
    sharpe = mu / sd * (365 ** 0.5) if sd else 0
    return {
        "name": name, "avg_long": avg_long, "avg_short": avg_short,
        "pct_long": pct_long, "cum": tot, "sharpe": sharpe,
        "separation": avg_long - avg_short,
    }


def main():
    closes = load()
    n = len(closes)
    print(f"BTC — {n} jours (closes), dernier close = {closes[-1]:,.0f}$")
    print("=" * 100)

    # --- Méthode 1 : MA200 ---
    s200 = [sma(closes, 200, i) for i in range(n)]
    sig1 = [False] * 200 + [c > s for c, s in zip(closes[200:], s200[200:])]

    # --- Méthode 2 : MA50/MA200 cross ---
    s50 = [sma(closes, 50, i) for i in range(n)]
    sig2 = [False] * 200
    for i in range(200, n):
        sig2.append(s50[i] > s200[i])

    # --- Méthode 3 : rendement 60j (paper) ---
    sig3 = [False] * 60
    for i in range(60, n):
        r60 = (closes[i] / closes[i - 60] - 1) * 100
        sig3.append(r60 > 15)  # bull > +15% sur 60j (seuil du paper)

    # --- Méthode 4 : TSMOM 1 mois ---
    sig4 = [False] * 30
    for i in range(30, n):
        sig4.append(closes[i] > closes[i - 30])  # momentum 30j > 0

    # --- Méthode 5 : MA200 + vol faible ---
    ema20 = ema_series(closes, 20)
    vols: list[float] = []
    for i in range(1, n):
        vols.append(abs(closes[i] / closes[i - 1] - 1))
    vol_ma20: list[float] = []
    for i in range(n):
        v = vols[max(0, i - 20):i]
        vol_ma20.append(sum(v) / len(v) if v else 0)
    sig5 = []
    for i in range(n):
        ok_trend = i >= 200 and closes[i] > s200[i]
        ok_vol = vol_ma20[i] < 0.04  # vol 20j < 4%/jour ≈ marché calme
        sig5.append(ok_trend and ok_vol)

    results = [
        audit("MA200 (prix>moyenne 200j)", closes, sig1),
        audit("MA50/MA200 (golden/death cross)", closes, sig2),
        audit("Rendement 60j >+15% (paper bull)", closes, sig3),
        audit("TSMOM momentum 30j", closes, sig4),
        audit("MA200 + vol faible", closes, sig5),
    ]

    print(f"{'MÉTHODE':<32}{'%long':>7}{'ret/j long':>10}{'ret/j bear':>11}"
          f"{'cum signal':>11}{'Sharpe':>8}{'séparation':>11}")
    print("-" * 100)
    for r in sorted(results, key=lambda x: -x["sharpe"]):
        print(f"{r['name']:<32}{r['pct_long']:>6.1f}%{r['avg_long']:>+9.3f}%"
              f"{r['avg_short']:>+10.3f}%{r['cum']:>+10.1f}%{r['sharpe']:>8.2f}"
              f"{r['separation']:>+10.3f}%")

    print("=" * 100)
    print("LECTURE : 'séparation' = écart de rendement moyen entre jours long et jours bear.")
    print("Plus c'est positif, mieux le signal sépare les bons des mauvais jours.")
    # Derniers 60 jours : quel signal dit quoi maintenant ?
    print("-" * 100)
    print("DERNIERS 60 JOURS — état actuel de chaque signal :")
    labels = ["MA200", "MA50/200", "R60j>15", "TSMOM30", "MA200+vol"]
    for lbl, sig in zip(labels, [sig1, sig2, sig3, sig4, sig5]):
        state = "HAUSSIER 🟢" if sig[-1] else "BAISSIER/NEUTRE 🔴"
        # combien de bascules dans les 60 derniers jours
        flips = sum(1 for i in range(max(1, n - 60), n) if sig[i] != sig[i - 1])
        print(f"  {lbl:<10} -> {state}  (basculement: {flips}x / 60j)")


if __name__ == "__main__":
    main()
