#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : mesurer_volatilite_paires.py
Projet       : ACE777 (fusibles par actif — GO Christophe 09/09)
Rôle         : mesure la volatilité RÉELLE de chaque paire de l'universe (klines daily
               MEXC, ~45 jours) et propose le budget-perte par paire :
                 budget_pct = k × sigma_jour   (k = paramètre famille, défaut 1.5)
               + la règle de DÉGEL sur données (pas d'horloge, GO Christophe) :
                 une paire au banc est dégelée si prix > M24h ET dd6 < seuil
                 (rebond mesuré, pas un timer de 24 h).
Stdlib pur. Sortie lisible + JSON (Index_Maison/data/volatilite_paires.json).
Ne trade pas (C3). Lecture seule.
"""
import json
import glob
import time
import urllib.request
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # ace777-test-day1
OUT_JSON = ROOT / "Index_Maison" / "data" / "volatilite_paires.json"
BASE = "https://api.mexc.com/api/v3/klines"
K_DEFAULT = 1.5
MISE_STD = 20.0      # mise standard HULK (USDT)
DELGEL_M24 = True    # dégel : prix > moyenne 24h des closes
DELGEL_DD6_MAX = 3.0 # et dd6 < 3 %


def pairs_universe():
    """Paires : defaults.env UNIVERSE, sinon le dernier DIGEST."""
    env = ROOT / "hulk-mexc" / "config" / "defaults.env"
    try:
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.startswith("UNIVERSE") and "=" in line:
                v = line.split("=", 1)[1].strip()
                if v:
                    return [p.strip().upper() for p in v.split(",") if p.strip()]
    except Exception:
        pass
    digests = sorted(glob.glob(str(ROOT / "hulk-mexc" / "runs" / "DIGEST_*.json")))
    if digests:
        d = json.load(open(digests[-1]))
        return [p["pair"] for p in d.get("pairs", []) if p.get("pair")]
    return []


def klines(sym, interval, limit):
    url = f"{BASE}?symbol={sym}&interval={interval}&limit={limit}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                return json.load(r)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1.5 * (attempt + 1))


def mesure_pair(sym):
    k = klines(sym, "1d", 45)
    if len(k) < 12:
        return None
    closes = [float(r[4]) for r in k]
    highs = [float(r[2]) for r in k]
    lows = [float(r[3]) for r in k]
    rets = [(closes[i] / closes[i - 1] - 1) * 100.0 for i in range(1, len(closes))]
    sigma = st.stdev(rets)                       # vol journalière réalisée %
    adr = st.median((h - l) / c * 100.0 for h, l, c in zip(highs, lows, closes))
    p90 = sorted(abs(r) for r in rets)[int(len(rets) * 0.9)]
    # état courant pour la règle de dégel
    k4 = klines(sym, "4h", 6)                    # 24 h de bougies 4h
    c4 = [float(r[4]) for r in k4]
    m24 = sum(c4) / len(c4)
    prix = c4[-1]
    dd6 = (prix / max(float(r[2]) for r in k4) - 1) * 100.0
    degel = (prix > m24) and (dd6 > -DELGEL_DD6_MAX)
    return {
        "pair": sym, "prix": round(prix, 6),
        "sigma_jour_pct": round(sigma, 2),
        "adr_pct": round(adr, 2),
        "p90_abs_ret_pct": round(p90, 2),
        "m24h": round(m24, 6), "dd6_pct": round(dd6, 2),
        "degel_eligible": bool(degel),
    }


def main():
    pairs = pairs_universe()
    if not pairs:
        print("❌ aucune paire trouvée (defaults.env / DIGEST)")
        return 1
    print(f"═" * 78)
    print(f"VOLATILITÉ RÉELLE DES {len(pairs)} PAIRES — base : daily MEXC ~45 jours")
    print(f"budget_paire = k × sigma_jour (k = {K_DEFAULT}) · mise standard {MISE_STD}$")
    print(f"dégel sur DONNÉES : prix > M24h ET dd6 > -{DELGEL_DD6_MAX}% (jamais d'horloge)")
    print(f"═" * 78)
    rows = []
    for i, p in enumerate(pairs):
        try:
            m = mesure_pair(p)
            if m:
                rows.append(m)
        except Exception as e:
            print(f"  {p}: ERREUR {e}")
        time.sleep(0.25)
    rows.sort(key=lambda r: r["sigma_jour_pct"], reverse=True)
    med_sigma = st.median([r["sigma_jour_pct"] for r in rows]) if rows else 0
    print(f"  {'paire':<12}{'sigma/j':>8}{'ADR':>7}{'p90':>7}{'budget%':>9}{'budget$':>9}"
          f"{'dd6':>7}  dégel?")
    for r in rows:
        budget_pct = K_DEFAULT * r["sigma_jour_pct"]
        tier = "🟥 folle" if r["sigma_jour_pct"] > med_sigma * 1.5 else \
               "🟨 nerveuse" if r["sigma_jour_pct"] > med_sigma else "🟩 sage"
        print(f"  {r['pair']:<12}{r['sigma_jour_pct']:>7.2f}%{r['adr_pct']:>6.2f}%"
              f"{r['p90_abs_ret_pct']:>6.1f}%{budget_pct:>8.1f}%"
              f"{budget_pct/100*MISE_STD:>8.2f}${r['dd6_pct']:>6.1f}%"
              f"  {'OUI' if r['degel_eligible'] else 'non'} {tier}")
    if rows:
        sig = [r["sigma_jour_pct"] for r in rows]
        print(f"\n  médiane sigma : {med_sigma:.2f}%/jour · la plus folle "
              f"{rows[0]['pair']} {rows[0]['sigma_jour_pct']:.2f}% · la plus sage "
              f"{rows[-1]['pair']} {rows[-1]['sigma_jour_pct']:.2f}%")
        print(f"  → rapport folle/sage : {rows[0]['sigma_jour_pct']/max(rows[-1]['sigma_jour_pct'],0.01):.1f}× "
              f"(justification du fusible SUR MESURE : une règle unique surévalue les sages, sous-évalue les folles)")
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps({
        "ts": int(time.time()), "k": K_DEFAULT, "mise_std": MISE_STD,
        "regle_degel": {"prix_sup_m24h": True, "dd6_min_pct": -DELGEL_DD6_MAX},
        "paires": rows,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nsauvé : {OUT_JSON.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
