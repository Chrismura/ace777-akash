#!/usr/bin/env python3
"""
BACKTEST — Couleur TSMOM (prix_dir) : validation sur 300 jours BTC réels.

Rejoue le signal "prix_dir = TSMOM 30j" comme couleur_regime.py le ferait et
mesure la JUSTESSE avec la même métrique que couleur_regime.py --score :
  - HIT  : la couleur disait la bonne direction (marché a monté dans les X jours)
  - MISS : la couleur se trompait
  - prédiction 24h (comme le score actuel) ET 7 jours (le vrai horizon de la couleur)

On compare aussi :
  - TSMOM 30j seul
  - TSMOM 60j
  - TSMOM 90j
  - MA200 (le classique)
  - TSMOM30 + MA200 (le combo proposé : réactivité + confirmation)

Sortie : table de justesse par méthode, et le HIT-rate 24h/7j.
OUTIL DE RECHERCHE — n'exécute rien sur le live.
"""
from __future__ import annotations
import json


def load() -> list[float]:
    raw = json.load(open("/tmp/btc_daily.json"))
    return [float(k[4]) for k in raw]


def sma(closes: list[float], n: int, i: int) -> float:
    if i < n - 1:
        return float("nan")
    return sum(closes[i - n + 1:i + 1]) / n


def tsmom(closes: list[float], n: int) -> list[bool]:
    """True = haussier (prix > prix d'il y a n jours)."""
    return [False] * n + [closes[i] > closes[i - n] for i in range(n, len(closes))]


def ma200_sig(closes: list[float]) -> list[bool]:
    return [False] * 200 + [closes[i] > sma(closes, 200, i) for i in range(200, len(closes))]


def justesse(closes: list[float], sig: list[bool], horizon: int) -> dict:
    """HIT/MISS : le signal disait long et le marché a monté sur `horizon` jours ?"""
    n = len(closes)
    hits = miss = 0
    # on ne juge que quand le signal est établi (pas les 200 premiers jours de warmup)
    start = max(200, horizon)
    for i in range(start, n - horizon):
        up = closes[i + horizon] > closes[i]
        if sig[i]:
            hits += 1 if up else 0
            miss += 0 if up else 1
    tot = hits + miss
    return {
        "hits": hits, "miss": miss, "n": tot,
        "hit_rate": hits / tot * 100 if tot else 0,
    }


def main():
    closes = load()
    n = len(closes)
    print(f"BTC — {n} jours. Backtest de la couleur TSMOM (signal → marché a monté ?)")
    print("=" * 92)

    sigs = {
        "TSMOM 30j": tsmom(closes, 30),
        "TSMOM 60j": tsmom(closes, 60),
        "TSMOM 90j": tsmom(closes, 90),
        "MA200 seul": ma200_sig(closes),
        "TSMOM30 + MA200 (combo)": [a and b for a, b in zip(tsmom(closes, 30), ma200_sig(closes))],
        "TSMOM30 OU MA200 (ou)": [a or b for a, b in zip(tsmom(closes, 30), ma200_sig(closes))],
    }

    print(f"{'MÉTHODE':<26}{'%j long':>8}{'HIT 24h':>10}{'HIT 7j':>9}"
          f"{'MISS 7j':>9}{'n 7j':>6}")
    print("-" * 92)
    for name, sig in sigs.items():
        pct = sum(1 for s in sig if s) / len(sig) * 100
        j24 = justesse(closes, sig, 1)
        j7 = justesse(closes, sig, 7)
        print(f"{name:<26}{pct:>7.1f}%{j24['hit_rate']:>9.1f}%{j7['hit_rate']:>8.1f}%"
              f"{j7['miss']:>8}{j7['n']:>6}")

    print("=" * 92)
    print("LECTURE : HIT = le signal disait 'haussier' et le marché a monté (24h et 7j).")
    print("Un bon détecteur de trend : HIT 7j nettement > 50% et % long adapté au marché.")
    print()
    # Comparaison avec le vrai comportement : combien de jours le marché a monté au total ?
    up_days = sum(1 for i in range(1, n) if closes[i] > closes[i - 1])
    print(f"Référence : le marché a monté {up_days}/{n - 1} jours = {up_days/(n-1)*100:.1f}% du temps.")
    print("(Un signal doit battre cette base, sinon il n'apporte rien.)")

    # Le verdict 7j de TSMOM 30j en détail : par mois
    print()
    print("Détail TSMOM 30j — justesse 7j par période (~15 jours) :")
    raw = json.load(open("/tmp/btc_daily.json"))
    import datetime
    sig = tsmom(closes, 30)
    for i in range(210, n - 7, 15):
        d = datetime.datetime.utcfromtimestamp(raw[i][0] / 1000).strftime("%m-%d")
        state = "HAUSSIER 🟢" if sig[i] else "BAISSIER 🔴"
        r7 = (closes[i + 7] / closes[i] - 1) * 100
        ok = "HIT ✅" if (sig[i] and r7 > 0) or (not sig[i] and r7 <= 0) else "MISS ❌"
        print(f"  {d}  {state}  →  marché 7j: {r7:+.1f}%  {ok}")


if __name__ == "__main__":
    main()
