#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moteur_paternes_btc.py — P1 du chantier CORTANA_ANALYSTE (GO Christophe 11/09)
Rôle : mesurer en continu les paterne BTC validés au corpus de leçons :
  1) 50w x 200w + RSI hebdo        (LECON-032 : régime de fond)
  2) MACD 12/26/9 daily            (LECON-035 : FILTRE, pas déclencheur)
  3) tops de cycle / halving->top  (LECON-036 : contexte de cycle ~4 ans)
  4) cycle lunaire                 (LECON-037 : testé NUL — documenté, jamais signal)
Produit : Index_Maison/data/paternes_btc_hist.jsonl (append-only, 1 ligne/run)
          Index_Maison/data/paternes_btc_etat.json (anti-figage 3 cycles, [C4] zéro alarme)
Convention maison : stdlib uniquement, lecture seule des APIs, aucune écriture moteur.
"""
import json, hashlib, urllib.request
from pathlib import Path
from datetime import datetime, timezone, date

BASE = Path.home() / "ace777-test-day1"
HIST = BASE / "Index_Maison/data/paternes_btc_hist.jsonl"
ETAT = BASE / "Index_Maison/data/paternes_btc_etat.json"

SYNODIQUE = 29.530588853          # jours
REF_NOUVELLE_LUNE = 947145240     # 06/01/2000 18:14 UTC
HALVINGS = ["2012-11-28", "2016-07-09", "2020-05-11", "2024-04-19"]
TOPS = [("2013-04-10", 231), ("2013-12-05", 1137), ("2017-12-17", 19280),
        ("2021-04-14", 63554), ("2021-11-09", 67562), ("2025-10-07", 124777)]  # LECON-036

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ACE777-lecture-seule"})
    return json.load(urllib.request.urlopen(req, timeout=25))

def sma(a, n):
    return [sum(a[i-n+1:i+1])/n if i >= n-1 else None for i in range(len(a))]

def rsi(c, n=14):
    out = [None]*len(c)
    for i in range(n, len(c)):
        g = l = 0.0
        for k in range(i-n+1, i+1):
            ch = c[k]-c[k-1]
            if ch > 0: g += ch
            else: l -= ch
        out[i] = 100 - 100/(1+(g/l if l > 0 else 1e9))
    return out

def ema(p, per):
    k = 2/(per+1); out = [None]*len(p)
    for i in range(per-1, len(p)):
        out[i] = sum(p[:per])/per if i == per-1 else p[i]*k + out[i-1]*(1-k)
    return out

def d(iso): return date.fromisoformat(iso)

def main():
    brut = fetch("https://api.blockchain.info/charts/market-price?timespan=all&format=json&sampled=false")
    vals = [(p["x"], p["y"]) for p in brut["values"] if p["y"] > 0]
    ts = [v[0] for v in vals]; px = [v[1] for v in vals]; n = len(px)

    # ---- 1) hebdo : 50w x 200w + RSIw ----
    semaines = {}
    for t, v in vals:
        semaines[t - (t % 604800)] = v
    wks = sorted(semaines); wc = [semaines[w] for w in wks]
    s50, s200 = sma(wc, 50), sma(wc, 200)
    rsiw = rsi(wc)
    ecart_50_200 = (s50[-1]/s200[-1]-1)*100 if s50[-1] and s200[-1] else None
    regime = "HAUSSIER" if s50[-1] > s200[-1] else "BAISSIER"

    # ---- 2) MACD 12/26/9 daily (filtre) ----
    e12, e26 = ema(px, 12), ema(px, 26)
    macd = [e12[i]-e26[i] if e12[i] is not None and e26[i] is not None else None for i in range(n)]
    start = next(i for i, x in enumerate(macd) if x is not None)
    sig = [None]*n; k9 = 2/10
    sig[start+8] = sum(macd[start:start+9])/9
    for i in range(start+9, n): sig[i] = macd[i]*k9 + sig[i-1]*(1-k9)
    hist = [macd[i]-sig[i] if sig[i] is not None else None for i in range(n)]
    dernier_crois = None
    for i in range(start+9, n):
        if hist[i] is None or hist[i-1] is None: continue
        if (hist[i-1] <= 0 < hist[i]) or (hist[i-1] >= 0 > hist[i]):
            dernier_crois = {"date": datetime.utcfromtimestamp(ts[i]).date().isoformat(),
                             "type": "HAUSSIER" if hist[i] > 0 else "BAISSIER",
                             "jours_depuis": n-1-i}
    macd_filtre = None
    if dernier_crois and s50[-1] and s200[-1]:
        macd_filtre = (dernier_crois["type"] == "HAUSSIER" and regime == "HAUSSIER")

    # ---- 3) contexte de cycle (LECON-036) ----
    auj = datetime.utcfromtimestamp(ts[-1]).date()
    h4 = d("2024-04-19")
    jours_halving = (auj - h4).days
    top2025 = d("2025-10-07")
    jours_depuis_top = (auj - top2025).days
    pct_du_top = (px[-1]/TOPS[-1][1]-1)*100
    cycle = {"jours_depuis_halving_2024": jours_halving,
             "jours_depuis_top_2025": jours_depuis_top,
             "pct_vs_top_2025": round(pct_du_top, 1),
             "reference_halving_top_jours": {"2012": 133, "2016": 526, "2020": 338, "2024": 536}}

    # ---- 4) lunaire : phase du jour + rappel du nul (LECON-037) ----
    phase_pct = ((ts[-1]-REF_NOUVELLE_LUNE)/SYNODIQUE) % 1.0
    lunaire = {"phase_pct": round(phase_pct*100, 1),
               "statut": "TESTE_NUL (LECON-037 : 199 lunations, ecart pleine/nouvelle 0,002 pt/j) — DOCUMENTATION, pas un signal"}

    resume = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "prix_dernier": round(px[-1], 2),
        "regime_fond": {"sma50w": round(s50[-1]), "sma200w": round(s200[-1]),
                        "ecart_pct": round(ecart_50_200, 1), "rsi_w": round(rsiw[-1], 1),
                        "regime": regime},
        "macd_filtre": {"dernier_croisement": dernier_crois,
                        "histogramme": round(hist[-1]) if hist[-1] is not None else None,
                        "filtre_actif": macd_filtre,
                        "note": "LECON-035 : filtre, pas declencheur"},
        "cycle": cycle,
        "lunaire": lunaire,
        "sources": {"prix": "api.blockchain.info charts/market-price (lecture seule)"},
        "lecons": ["LECON-032", "LECON-035", "LECON-036", "LECON-037"],
    }

    payload = json.dumps({k: v for k, v in resume.items() if k != "ts"}, sort_keys=True, ensure_ascii=False)
    md5 = hashlib.md5(payload.encode()).hexdigest()

    etat = json.loads(ETAT.read_text(encoding="utf-8")) if ETAT.exists() else {}
    if etat.get("md5_payload") == md5:
        fige = etat.get("fige_consecutifs", 0) + 1
    else:
        fige = 0
    etat.update({"ts": resume["ts"], "md5_payload": md5, "fige_consecutifs": fige,
                 "alerte_figee": fige >= 3,   # [C4] flag d'état SEUL — aucune alarme.json en phase 1
                 "note": "fige_consecutifs = payload identique sur cycles consécutifs (3 = source potentiellement morte); lu à l'analyse, jamais de sirène"})
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")

    with open(HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(resume, ensure_ascii=False) + "\n")

    r = resume["regime_fond"]
    print(f"OK {resume['ts']} | prix {resume['prix_dernier']}$ | fond {r['regime']} "
          f"(50w {'+' if r['ecart_pct']>=0 else ''}{r['ecart_pct']}% vs 200w, RSIw {r['rsi_w']}) | "
          f"MACD {dernier_crois['type'] if dernier_crois else '?'} il y a {dernier_crois['jours_depuis'] if dernier_crois else '?'} j, filtre actif: {macd_filtre} | "
          f"cycle: {jours_halving} j post-halving, {pct_du_top:.0f}% du top 2025 | fige {fige}/3")

if __name__ == "__main__":
    main()
