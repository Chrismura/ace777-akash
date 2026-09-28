#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tester_solutions_alternatives.py — 3 SOLUTIONS TESTÉES PAPIER
(GO direct C. 14/09 : « trouve-moi des solutions » · 0 ordre · 0 euro · specs figées AVANT le run)

T1 SUR-RÉACTION (fade le dépassement) — même données que le test du retard :
   Après |ret BTC 1min| ≥ 0,04%, si le prix PM Up a déjà dépassé 0,75 (mouvement haussier)
   ou glissé sous 0,25 (baissier) → le marché a SUR-agi. On achète le côté CONTRAIRE
   bon marché (~0,25) et on sort à la 1ère remontée vers 0,40, sinon 10 min, friction 1 ¢.
   Logique : mes 3 403 événements montraient que le prix PM REVIENT en arrière 90 % du temps.

T2 ETH et SOL Up/Down — les mêmes marchés sur des actifs MOINS regardés par les bots :
   slugs « ethereum-up-or-down-on-<mois>-<jour> » / « solana-... ». Si le retard existe
   quelque part, c'est là (moins de liquidité = moins de collets).

T3 LECTURE DE LA ZONE : pour chaque actif (BTC/ETH/SOL), distribution des prix d'équilibre
   et amplitude moyenne des oscillations — l'actif où le prix oscillle le plus est celui
   où le market making naïf rapporte le plus.
"""
import json, time, urllib.request
from pathlib import Path
from datetime import datetime, timezone, timedelta

BASE = Path.home() / "ace777-test-day1" / "Index_Maison"
OUT = BASE / "thermo" / "solutions_alternatives_resultat.json"
SEUIL = 0.0004
FRIC = 0.01
JOURS = 7
MOIS = ["january","february","march","april","may","june","july",
        "august","september","october","november","december"]

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-test/1.0"})
    return json.loads(urllib.request.urlopen(req, timeout=25).read())

def binance_1m(start, end, symbole):
    out, s, e = {}, start * 1000, end * 1000
    while s < e:
        rows = get(f"https://api.binance.com/api/v3/klines?symbol={symbole}&interval=1m"
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

def charger_marche(slug):
    evs = get(f"https://gamma-api.polymarket.com/events?slug={slug}")
    if not evs: return None
    m = evs[0]["markets"][0]
    ids = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    outcomes = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    if "Up" not in outcomes: return None
    tid = ids[outcomes.index("Up")]
    start, end = iso_ts(m["startDate"]), iso_ts(m["endDate"])
    pm = {}
    for p in get(f"https://clob.polymarket.com/prices-history?market={tid}"
                 f"&startTs={start}&endTs={end+3600}&fidelity=1").get("history", []):
        pm[p["t"] // 60 * 60] = float(p["p"])
    return {"tid": tid, "start": start, "end": end, "pm": pm}

# ═══════════════ T1 : SUR-RÉACTION BTC ═══════════════
print("═══ T1 · SUR-RÉACTION (acheter le dépassement, vendre le retour) ═══")
today = datetime.now(timezone.utc).date()
t1_pnls, t1_details = [], {"entrees": 0, "sorties_cible": 0, "sorties_timeout": 0}

for k in range(1, JOURS + 1):
    d = today - timedelta(days=k)
    slug = f"bitcoin-up-or-down-on-{MOIS[d.month-1]}-{d.day}"
    try:
        mk = charger_marche(slug)
        if not mk or len(mk["pm"]) < 200: continue
        btc = binance_1m(mk["start"], mk["end"] + 600, "BTCUSDT")
        minutes = sorted(set(mk["pm"]) & set(btc))
        for t in minutes:
            if t - 60 not in btc: continue
            ret = btc[t] / btc[t - 60] - 1
            if abs(ret) < SEUIL: continue
            p_up = mk["pm"][t]
            # sur-réaction haussière : Up dépassé > 0,75 → on achète DOWN (1 - p_up)
            # sur-réaction baissière : Up sous 0,25 → on achète UP (p_up)
            if ret > 0 and p_up > 0.75:
                prix_achat, cote = 1 - p_up, "Down"
            elif ret < 0 and p_up < 0.25:
                prix_achat, cote = p_up, "Up"
            else:
                continue
            t1_details["entrees"] += 1
            # sortie : prix du côté acheté = 1 - prix Up ; cible 0,40 (achat ~0,25)
            serie_up = mk["pm"]
            sortie = None
            for dt in range(1, 11):
                if (t + dt*60) not in serie_up: continue
                prix_up_apres = serie_up[t + dt*60]
                prix_nous = (1 - prix_up_apres) if cote == "Down" else prix_up_apres
                if prix_nous >= 0.40:
                    sortie, t1_details["sorties_cible"] = prix_nous, t1_details["sorties_cible"] + 1
                    break
            if sortie is None:
                dt = next((dt for dt in range(1, 11) if (t + dt*60) in serie_up), None)
                if dt is None: continue
                prix_up_apres = serie_up[t + dt*60]
                sortie = (1 - prix_up_apres) if cote == "Down" else prix_up_apres
                t1_details["sorties_timeout"] += 1
            t1_pnls.append(sortie - prix_achat - FRIC)
        time.sleep(0.2)
    except Exception as e:
        print(f"  {slug}: ERR {str(e)[:80]}")

if t1_pnls:
    n = len(t1_pnls)
    print(f"  entrées {t1_details['entrees']} · sorties cible 0,40 : {t1_details['sorties_cible']} · timeout : {t1_details['sorties_timeout']}")
    print(f"  PnL moyen {sum(t1_pnls)/n:+.3f} $/trade · réussite {100*sum(1 for p in t1_pnls if p>0)/n:.0f}% · total {sum(t1_pnls):+.2f} $")
else:
    print("  aucun événement éligible")

# ═══════════════ T2 : ETH / SOL UP-DOWN ═══════════════
print("\n═══ T2 · MÊMES MARCHÉS SUR ETH et SOL (moins gardés par les bots) ═══")
t2 = {}
for actif, slug_prefix, sym in (("ETH", "ethereum-up-or-down-on", "ETHUSDT"),
                                 ("SOL", "solana-up-or-down-on", "SOLUSDT")):
    pnls_actif, drifts = [], []
    for k in range(1, JOURS + 1):
        d = today - timedelta(days=k)
        slug = f"{slug_prefix}-{MOIS[d.month-1]}-{d.day}"
        try:
            mk = charger_marche(slug)
            if not mk or len(mk["pm"]) < 200:
                continue
            alt = binance_1m(mk["start"], mk["end"] + 600, sym)
            minutes = sorted(set(mk["pm"]) & set(alt))
            for t in minutes:
                if t - 60 not in alt: continue
                ret = alt[t] / alt[t - 60] - 1
                if abs(ret) < SEUIL: continue
                if not (0.30 <= mk["pm"][t] <= 0.70): continue
                sens = 1 if ret > 0 else -1
                p0 = mk["pm"][t]
                sortie = next(((mk["pm"][t + dt*60]) for dt in range(5, 9) if (t + dt*60) in mk["pm"]), None)
                if sortie is None: continue
                drifts.append((sortie - p0) if sens > 0 else (p0 - sortie))
                pnls_actif.append((sortie - p0) - FRIC)
            time.sleep(0.2)
        except Exception:
            continue
    if pnls_actif:
        n = len(pnls_actif)
        t2[actif] = {"n": n, "derive_moy_cents": round(sum(drifts)/len(drifts)*100, 2),
                     "pnl_moyen": round(sum(pnls_actif)/n, 4),
                     "reussite_pct": round(100*sum(1 for p in pnls_actif if p>0)/n, 1)}
        print(f"  {actif}: {n} événements · dérive {t2[actif]['derive_moy_cents']:+.2f} ¢ · "
              f"PnL {t2[actif]['pnl_moyen']:+.4f} $/trade · réussite {t2[actif]['reussite_pct']}%")
    else:
        t2[actif] = {"n": 0}
        print(f"  {actif}: marchés introuvables ou trop minces")

# ═══════════════ T3 : AMPLITUDE DES OSCILLATIONS PAR ACTIF ═══════════════
print("\n═══ T3 · AMPLITUDE DES OSCILLATIONS (carburant du market making) ═══")
amplitudes = {}
for actif, slug_prefix in (("BTC", "bitcoin-up-or-down-on"),
                            ("ETH", "ethereum-up-or-down-on"),
                            ("SOL", "solana-up-or-down-on")):
    osc = []
    for k in range(1, 4):
        d = today - timedelta(days=k)
        slug = f"{slug_prefix}-{MOIS[d.month-1]}-{d.day}"
        try:
            mk = charger_marche(slug)
            if not mk or len(mk["pm"]) < 200: continue
            vals = list(mk["pm"].values())
            osc.append(max(vals) - min(vals))
            time.sleep(0.2)
        except Exception:
            continue
    if osc:
        amplitudes[actif] = round(sum(osc)/len(osc), 2)
        print(f"  {actif}: amplitude moyenne du prix sur la vie du marché : {amplitudes[actif]:.2f} (0-1)")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "ts": datetime.now(timezone.utc).isoformat(),
    "specs": "figées en docstring avant le run — une seule passe, 0 ordre",
    "T1_surreaction": {"n": len(t1_pnls),
                        "pnl_moyen": round(sum(t1_pnls)/len(t1_pnls), 4) if t1_pnls else None,
                        "total": round(sum(t1_pnls), 2) if t1_pnls else None,
                        "details": t1_details},
    "T2_eth_sol": t2,
    "T3_amplitudes": amplitudes,
}, ensure_ascii=False, indent=1))
print(f"\nrésultat : {OUT}")
