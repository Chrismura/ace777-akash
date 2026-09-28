#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tester_polymarket_phase_b.py — TEST PAPIER du set up Polymarket BTC Up/Down
(GO direct Christophe 14/09 : "c'est MOI la loi" en mode test — 0 ordre, 0 euro, lecture seule).

SPEC FIGÉE AVANT LE RUN (anti data-snooping) :
  Marchés : série quotidienne "Bitcoin Up or Down on <mois>-<jour>" (Polymarket gamma-api).
  Données : trades réels (data-api) du jour J-30 à J-1 + résolution (Up/Down à 1/0).
  Prix d'entrée simulé : prix de la 1ère transaction du marché + 0,02 $ de glissement.
  Frais : 0 (Polymarket), mais on compte 0,02 de slippage + 0,01 de marge d'incertitude.
  Règles testées (figées maintenant, une seule passe) :
    R1 SUIVEUR  : acheter le côté gagnant de la VEILLE.
    R2 MOMENTUM : acheter Up si BTC spot (Binance 1j) a monté > +1 % la veille, Down si < -1 %,
                  sinon pas de trade (sélectivité type HUNTER).
    R3 CONTRE   : acheter le côté PERDANT de la veille (retour à la moyenne).
    R0 HASARD   : pile ou face (la base de comparaison).
  Verdict honnête : EV net par trade = p_gagnant×(1−prix) − (1−p_gagnant)×prix − frictions.
  Échantillon : ~30 jours. Petit par nature — c'est un DÉTECTEUR de piste, pas une preuve.
Sortie : print tableau + JSON thermo/polymarket_phaseb_resultat.json. Aucun ordre envoyé.
"""
import json, time, urllib.request
from pathlib import Path
from datetime import datetime, timezone, timedelta

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
OUT = BASE / "thermo" / "polymarket_phaseb_resultat.json"
J = 30  # jours d'historique
SLIP, MARGE = 0.02, 0.01

MOIS = ["january","february","march","april","may","june","july",
        "august","september","october","november","december"]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-test/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=15).read())

def jour_slug(d):
    return f"bitcoin-up-or-down-on-{MOIS[d.month-1]}-{d.day}"

# ---- 1. récolte : pour chaque jour, résolution + prix d'entrée (1er trade) ----
jours = []
today = datetime.now(timezone.utc).date()
for k in range(1, J + 1):
    d = today - timedelta(days=k)
    slug = jour_slug(d)
    try:
        evs = get(f"https://gamma-api.polymarket.com/events?slug={slug}")
        if not evs:
            continue
        m = evs[0]["markets"][0]
        outcomes = m.get("outcomes") or []
        if isinstance(outcomes, str): outcomes = json.loads(outcomes)
        prices = m.get("outcomePrices") or []
        if isinstance(prices, str): prices = json.loads(prices)
        gagnant = outcomes[prices.index("1")] if "1" in prices else None
        if not gagnant:
            continue
        cid = m.get("conditionId")
        trades = get(f"https://data-api.polymarket.com/trades?market={cid}&limit=500")
        if not trades:
            continue
        trades.sort(key=lambda t: t["timestamp"])
        premier = trades[0]
        # prix d'entrée = 1er trade du côté qu'on achète (Up ou Down), sinon prix Up + spread ~
        prix = {o: None for o in outcomes}
        for t in trades:
            o = t["outcome"]
            if prix[o] is None:
                prix[o] = float(t["price"])
        jours.append({
            "date": str(d), "gagnant": gagnant,
            "prix_up": prix.get("Up"), "prix_down": prix.get("Down"),
        })
    except Exception as e:
        jours.append({"date": str(d), "err": str(e)[:80]})
    time.sleep(0.15)

ok = [j for j in jours if "gagnant" in j]

# ---- 2. momentum Binance (veille) pour R2 ----
try:
    kl = get("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=40")
    momo = {}
    for row in kl:
        dt = datetime.fromtimestamp(row[0] / 1000, timezone.utc).date()
        o, c = float(row[1]), float(row[4])
        momo[str(dt)] = (c / o - 1) * 100
except Exception:
    momo = {}

# ---- 3. les 4 règles, une seule passe ----
def ev(p, bon):
    # p = prix payé (+frictions) ; bon = 1 si on gagne
    cout = p + SLIP + MARGE
    return (1 - cout) if bon else -cout

res = {"R1_suiveur": [], "R2_momentum": [], "R3_contre": [], "R0_hasard": []}
for i, j in enumerate(ok):
    if i == 0: continue
    veille = ok[i - 1]
    cote_r1 = veille["gagnant"]
    cote_r3 = "Down" if veille["gagnant"] == "Up" else "Up"
    mm = momo.get(veille["date"])
    cote_r2 = None
    if mm is not None:
        if mm > 1: cote_r2 = "Up"
        elif mm < -1: cote_r2 = "Down"
    import random
    random.seed(42 + i)
    cote_r0 = random.choice(["Up", "Down"])

    for nom, cote in (("R1_suiveur", cote_r1), ("R2_momentum", cote_r2),
                      ("R3_contre", cote_r3), ("R0_hasard", cote_r0)):
        if cote is None: continue
        p = j["prix_up"] if cote == "Up" else j["prix_down"]
        if p is None: continue
        bon = (cote == j["gagnant"])
        res[nom].append({"ev": ev(p, bon), "bon": bon})

# ---- 4. tableau final ----
print(f"\n═══ POLYMARKET PHASE B — TEST PAPIER sur {len(ok)} marchés quotidiens (J-30 → J-1) ═══\n")
print(f"{'Règle':<14}{'n':>4}{'WR':>9}{'EV/trade':>11}{'total':>9}")
ligne_finale = {}
for nom in ("R0_hasard", "R1_suiveur", "R2_momentum", "R3_contre"):
    tr = res[nom]
    if not tr:
        print(f"{nom:<14}{'0':>4}")
        continue
    n = len(tr)
    wr = 100 * sum(1 for t in tr if t["bon"]) / n
    evm = sum(t["ev"] for t in tr) / n
    tot = sum(t["ev"] for t in tr)
    print(f"{nom:<14}{n:>4}{wr:>8.1f}%{evm:>+10.3f}${tot:>+8.2f}$")
    ligne_finale[nom] = {"n": n, "wr_pct": round(wr, 1), "ev_par_trade": round(evm, 3),
                         "total_30j": round(tot, 2)}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "ts": datetime.now(timezone.utc).isoformat(),
    "spec": "figée en docstring AVANT le run — une seule passe, 0 ordre",
    "marches": len(ok), "resultats": ligne_finale,
}, ensure_ascii=False, indent=1))
print(f"\nrésultat : {OUT}")
