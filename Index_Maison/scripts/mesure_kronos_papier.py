#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesure_kronos_papier.py — GO 24/10 @laobaishare (Kronos, 0 ordre).
But : mesurer une baseline directionnelle papier sur caches BTC 1h,
en attendant Kronos-mini (torch absent sur ce Mac, donc pas d'inférence lourde).
Méthode honnête : persistance + croisement MM (proxy documenté, PAS Kronos),
scorée comme la justesse maison (HIT/MISS directionnel).
Sortie : thermo/kronos_mesure_<ts>.json (hors git).
IA=Buffy (Muse Spark 1.3, Freebuff). 0 ordre, lecture seule.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

BTC = Path("/Users/christophe/ace777-test-day1/hulk-mexc/runs/replay_cache/BTCUSDT_1h_45j.json")
JUSTESSE = Path(__file__).resolve().parent / "justesse_cockpit.json"
THERMO = Path(__file__).resolve().parent.parent / "thermo"

def mm(xs, n):
    return sum(xs[-n:]) / n if len(xs) >= n else None

def main():
    kl = json.load(open(BTC, encoding="utf-8"))
    closes = [float(b["c"]) for b in kl if b.get("c")]
    # fenêtres : toutes les 24h sur les 30 derniers jours, horizon +24h
    hits, total, lignes = 0, 0, []
    for i in range(len(closes) - 24 - 30 * 24, len(closes) - 24, 24):
        if i < 50:
            continue
        passe = closes[:i]
        m7, m25 = mm(passe, 7), mm(passe, 25)
        if m7 is None or m25 is None:
            continue
        pred = "LONG" if m7 > m25 else "SHORT"
        reel = "LONG" if closes[i + 24] > closes[i] else "SHORT"
        hit = pred == reel
        hits += hit
        total += 1
        lignes.append({"i": i, "pred": pred, "reel": reel, "hit": hit})
    pct = round(hits / total * 100, 1) if total else 0.0
    try:
        j = json.load(open(JUSTESSE, encoding="utf-8"))
        maison = {"global_pct": j.get("pct"), "n": j.get("total_scored"),
                  "directionnel_pct": (j.get("directionnel") or {}).get("pct")}
    except Exception as e:
        maison = {"erreur": str(e)}
    out = {"ts": datetime.now(timezone.utc).isoformat(),
           "fenetres": total, "hits": hits, "pct": pct,
           "methode": "proxy MM7/MM25 (PAS Kronos — torch absent, mesure d'attente honnête)",
           "kronos_protocole": "quand torch dispo : Kronos-mini (4.1M) lookback 400 / pred 120 sur mêmes fenêtres, même score HIT/MISS",
           "maison_justesse": maison,
           "verdict": ("baseline au niveau du hasard — Kronos reste à mesurer pour de vrai"
                        if pct < 55 else "baseline étonnamment haute — à confirmer avec Kronos"),
           "detail": lignes[-5:]}
    f = THERMO / f"kronos_mesure_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"-> {f} : {hits}/{total} = {pct}% | maison {maison}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
