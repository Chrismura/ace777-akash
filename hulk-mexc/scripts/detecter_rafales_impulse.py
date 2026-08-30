#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""detecter_rafales_impulse.py — Détecteur d'allumages IMPULSE (lecture seule).

Rejoue croisement_contexte.jsonl et liste CHAQUE allumage de régime IMPULSE
par paire : prix d'allumage, durée, prix 30min/60min après, verdict.

C'est la donnée qui manque pour valider le set-up « régime » d'EDEL :
l'accumulation des allumages jour après jour (avec ce qu'a fait le prix
après) prouvera ou réfutera le pattern. Rien n'est modifié dans Hulk.

Usage : python3 detecter_rafales_impulse.py [PAIRE ...]   (défaut : EDELUSDT)
Sortie : runs/rafales_impulse/<PAIRE>.md + .json
"""
import json
import os
import statistics
import sys
import datetime

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
OUT = os.path.join(RUNS, "rafales_impulse")
os.makedirs(OUT, exist_ok=True)


def load(pair):
    pts = []
    for line in open(CROIS, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("pair") == pair:
            pts.append(d)
    pts.sort(key=lambda x: x["ts"])
    return pts


def detecter(pts, gap_max=600):
    """Blocs consécutifs en régime IMPULSE (écart < gap_max s)."""
    blocks = []
    cur = None
    prev_ts = None
    for d in pts:
        if d.get("regime") == "IMPULSE":
            if cur is None or (prev_ts is not None and d["ts"] - prev_ts > gap_max):
                cur = [d]
            else:
                cur.append(d)
        else:
            if cur is not None:
                blocks.append(cur)
                cur = None
        prev_ts = d["ts"]
    if cur is not None:
        blocks.append(cur)
    return blocks


def price_after(pts, ts, delay):
    for d in pts:
        if d["ts"] >= ts + delay:
            return d["price"]
    return None


def main(pairs):
    for pair in pairs:
        pts = load(pair)
        blocks = detecter(pts)
        rows = []
        for b in blocks:
            t0 = b[0]["ts"]
            p0 = b[0]["price"]
            dt = datetime.datetime.fromtimestamp(t0, datetime.timezone.utc)
            p30 = price_after(pts, t0, 1800)
            p60 = price_after(pts, t0, 3600)
            # pic atteint pendant la rafale
            peak = max(x["price"] for x in b)
            rows.append({
                "ts": t0, "utc": dt.strftime("%Y-%m-%d %H:%MZ"),
                "dur_pts": len(b), "px_allumage": p0,
                "px_30min": p30, "ret_30min_pct": round((p30 / p0 - 1) * 100, 2) if p30 else None,
                "px_60min": p60, "ret_60min_pct": round((p60 / p0 - 1) * 100, 2) if p60 else None,
                "pic_rafale": peak, "ret_pic_pct": round((peak / p0 - 1) * 100, 2),
            })

        lines = [f"# ⚡ RAFALES IMPULSE — {pair} (rejouées depuis croisement_contexte.jsonl)",
                 "",
                 f"Fenêtre : {pts[0]['utc']} → {pts[-1]['utc']} · {len(pts)} points · "
                 f"**{len(blocks)} allumages IMPULSE détectés**",
                 "",
                 "| # | Allumage (UTC) | Durée (pts) | Prix allumage | Pic rafale | +30min | +60min |",
                 "|---|---|---|---|---|---|---|"]
        for i, r in enumerate(rows, 1):
            r30 = f"{r['ret_30min_pct']:+.2f}%" if r["ret_30min_pct"] is not None else "n/a"
            r60 = f"{r['ret_60min_pct']:+.2f}%" if r["ret_60min_pct"] is not None else "n/a"
            lines.append(f"| {i} | {r['utc']} | {r['dur_pts']} | {r['px_allumage']:.5f} | "
                         f"{r['pic_rafale']:.5f} ({r['ret_pic_pct']:+.2f}%) | {r30} | {r60} |")

        # stats globales
        g30 = [r["ret_30min_pct"] for r in rows if r["ret_30min_pct"] is not None]
        g60 = [r["ret_60min_pct"] for r in rows if r["ret_60min_pct"] is not None]
        lines += ["", "## 📊 Statistiques", ""]
        if g30:
            lines.append(f"- **+30min** : moy {statistics.mean(g30):+.2f}% · médiane {statistics.median(g30):+.2f}% · "
                         f"{sum(1 for g in g30 if g > 0)} up / {sum(1 for g in g30 if g <= 0)} down (n={len(g30)})")
        if g60:
            lines.append(f"- **+60min** : moy {statistics.mean(g60):+.2f}% · médiane {statistics.median(g60):+.2f}% · "
                         f"{sum(1 for g in g60 if g > 0)} up / {sum(1 for g in g60 if g <= 0)} down (n={len(g60)})")
        lines.append("")
        lines.append("_⚠️ n faible = à confirmer par l'accumulation des prochains jours (doctrine : jamais statique)._")

        with open(os.path.join(OUT, f"{pair}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        with open(os.path.join(OUT, f"{pair}.json"), "w", encoding="utf-8") as f:
            json.dump({"pair": pair, "n_rafales": len(rows), "rafales": rows}, f, ensure_ascii=False, indent=1)
        print(f"[OK] {pair}: {len(blocks)} rafales → {os.path.join(OUT, f'{pair}.md')}")
        for r in rows:
            r30 = f"{r['ret_30min_pct']:+.2f}%" if r["ret_30min_pct"] is not None else "n/a"
            r60 = f"{r['ret_60min_pct']:+.2f}%" if r["ret_60min_pct"] is not None else "n/a"
            print(f"  {r['utc']} · dur {r['dur_pts']}pts · px {r['px_allumage']:.5f} · "
                  f"pic {r['ret_pic_pct']:+.2f}% · 30min {r30} · 60min {r60}")


if __name__ == "__main__":
    args = sys.argv[1:] or ["EDELUSDT"]
    main([a.upper() if a.upper().endswith("USDT") else a.upper() + "USDT" for a in args])
