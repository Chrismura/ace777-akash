#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tester_retard_binance_pm.py — LE TEST DU RETARD Binance → Polymarket (v3 FINALE)
(GO direct Christophe 14/09 · papier · 0 ordre · 0 euro · lecture seule)

CONSTAT DE CALIBRAGE (vérifié à la source avant le run) :
  Les marchés « Bitcoin Up or Down » de Polymarket vivent sur LEUR horloge système
  (dates réelles sept 2025 dans leurs API). On suit LEUR fenêtre, pas la nôtre.

SPEC FIGÉE AVANT LE RUN (une seule passe) :
  Marchés   : les 7 derniers marchés quotidiens « bitcoin-up-or-down-on-<mois>-<jour> »,
              fenêtre = startDate/endDate LUES DANS L'API (jamais supposées).
  Prix PM   : clob prices-history à ~1 min, tokenId du côté "Up".
  BTC       : Binance 1m klines PAGINÉES sur la même fenêtre.
  Événement : minute où |retour BTC 1 min| ≥ 0,04 % ET 0,30 ≤ prix PM ≤ 0,70
              (zone incertaine — on n'achète jamais le quasi-certain, anatomie Grok 37-56 ¢).
  Dérive    : mouvement du prix PM DANS LE SENS du mouvement BTC sur 1/3/5 min.
  PnL papier: entrée minute-événement, sortie ~5 min, friction 1 ¢ aller-retour.
"""
import json, time, urllib.request
from pathlib import Path
from datetime import datetime, timezone, timedelta

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
OUT = BASE / "thermo" / "polymarket_retard_resultat.json"
SEUIL_BTC = 0.0004
FRIC = 0.01
PRIX_MIN, PRIX_MAX = 0.30, 0.70
JOURS = 7
MOIS = ["january","february","march","april","may","june","july",
        "august","september","october","november","december"]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-test/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=25).read())

def binance_1m(start, end):
    out, s, e = {}, start * 1000, end * 1000
    while s < e:
        rows = get(f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m"
                   f"&startTime={s}&endTime={e}&limit=1000")
        if not rows: break
        for r in rows:
            out[int(r[0])//1000] = float(r[4])
        s = int(rows[-1][0]) + 60_000
        if len(rows) < 1000: break
        time.sleep(0.1)
    return out

def iso_ts(s):
    return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp())

drifts = {1: [], 3: [], 5: []}
pnls = []
recap = []
today = datetime.now(timezone.utc).date()

for k in range(1, JOURS + 1):
    d = today - timedelta(days=k)
    slug = f"bitcoin-up-or-down-on-{MOIS[d.month-1]}-{d.day}"
    try:
        evs = get(f"https://gamma-api.polymarket.com/events?slug={slug}")
        if not evs:
            recap.append({"jour": slug, "err": "introuvable"}); continue
        m = evs[0]["markets"][0]
        ids = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
        outcomes = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
        if "Up" not in outcomes:
            recap.append({"jour": slug, "err": "pas de Up"}); continue
        tid = ids[outcomes.index("Up")]
        start, end = iso_ts(m["startDate"]), iso_ts(m["endDate"])

        # points PM à des secondes quelconques → on les met dans le bucket de leur MINUTE
        pm = {}
        for p in get(
            f"https://clob.polymarket.com/prices-history?market={tid}&startTs={start}&endTs={end+3600}&fidelity=1"
        ).get("history", []):
            pm[p["t"] // 60 * 60] = float(p["p"])   # dernier point vu dans la minute
        if len(pm) < 200:
            recap.append({"jour": slug, "err": f"{len(pm)} pts PM"}); continue
        btc = binance_1m(start, end + 600)
        minutes = sorted(set(pm) & set(btc))

        n_ev = 0
        for t in minutes:
            if t - 60 not in btc: continue
            ret = btc[t] / btc[t - 60] - 1
            if abs(ret) < SEUIL_BTC: continue
            sens = 1 if ret > 0 else -1
            prix0 = pm[t]
            if not (PRIX_MIN <= prix0 <= PRIX_MAX): continue
            for lag in (1, 3, 5):
                cible = next((t + dt*60 for dt in range(1, lag + 4) if (t + dt*60) in pm), None)
                if cible is None: continue
                drifts[lag].append((pm[cible] - prix0) if sens > 0 else (prix0 - pm[cible]))
            sortie = next((pm[t + dt*60] for dt in range(5, 9) if (t + dt*60) in pm), None)
            if sortie is None: continue
            pnls.append((sortie - prix0) - FRIC)
            n_ev += 1

        recap.append({"jour": slug,
                      "fenetre": f"{datetime.fromtimestamp(min(pm), timezone.utc):%m-%d %H:%M}→{datetime.fromtimestamp(max(pm), timezone.utc):%m-%d %H:%M}",
                      "pts_pm": len(pm), "bougies_btc": len(btc), "communes": len(minutes), "evenements": n_ev})
        print(f"{slug}: PM {len(pm)} pts · BTC {len(btc)} · communes {len(minutes)} · événements {n_ev}")
        time.sleep(0.2)
    except Exception as e:
        recap.append({"jour": slug, "err": str(e)[:100]})
        print(f"{slug}: ERR {str(e)[:100]}")

print(f"\n═══ DÉRIVE PM DANS LE SENS DU MOUVEMENT BTC (≥0,04 %/min · prix 30-70 ¢) ═══")
for lag in (1, 3, 5):
    v = drifts[lag]
    if not v: continue
    print(f"  après {lag} min : dérive moyenne {sum(v)/len(v)*100:+.2f} ¢ · "
          f"bon sens {100*sum(1 for x in v if x>0)/len(v):.0f}% (n={len(v)})")
if pnls:
    n = len(pnls)
    print(f"\n  STRATÉGIE PAPIER (entrée minute-événement · sortie 5 min · friction 1 ¢) :")
    print(f"  {n} trades · PnL moyen {sum(pnls)/n:+.3f} $/trade · "
          f"réussite {100*sum(1 for p in pnls if p>0)/n:.0f}% · total {sum(pnls):+.2f} $")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "ts": datetime.now(timezone.utc).isoformat(),
    "spec": "v3 figée avant run : fenêtres startDate/endDate de l'API, événement BTC 1m ≥0,04% · prix 30-70¢ · friction 1¢",
    "jours": recap,
    "derive_cents": {str(k): (round(sum(v)/len(v)*100, 2) if v else None) for k, v in drifts.items()},
    "pnl_papier": {"n": len(pnls), "moyen": round(sum(pnls)/len(pnls), 3) if pnls else None,
                   "total": round(sum(pnls), 2) if pnls else None},
}, ensure_ascii=False, indent=1))
print(f"\nrésultat : {OUT}")
