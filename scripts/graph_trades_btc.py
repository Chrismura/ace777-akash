#!/usr/bin/env python3
"""Prototype HORS-cockpit : graphique BTC (klines testnet) + points d'entrée/sortie des trades.

Usage:
  python3 scripts/graph_trades_btc.py [--csv runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv] [--out /tmp/btc_trades.html]

Produit un fichier HTML 100% autonome (canvas, stdlib uniquement, aucune lib externe).
Ouvre ensuite le HTML dans le navigateur (double-clic).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
KLINE_URL = "https://testnet.binancefuture.com/fapi/v1/klines"


def fetch_klines(symbol: str, interval: str, start_ms: int, end_ms: int) -> list[list]:
    """Récupère les klines du testnet sur la fenêtre [start_ms, end_ms] (pagination 1000 max)."""
    out: list[list] = []
    cur = start_ms
    while cur < end_ms:
        url = f"{KLINE_URL}?symbol={symbol}&interval={interval}&startTime={cur}&endTime={end_ms}&limit=1000"
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                batch = json.loads(r.read().decode())
        except Exception as e:
            print(f"WARN: échec klines ({e}) — arrêt pagination", file=sys.stderr)
            break
        if not batch:
            break
        out.extend(batch)
        nxt = batch[-1][6] + 1  # openTime de la prochaine bougie
        if nxt <= cur:
            break
        cur = nxt
    return out


def load_trades(csv_path: Path, since: str | None = None) -> list[dict]:
    """Lit les trades FILLED (par défaut : toute la fenêtre ; --since filtre)."""
    since_dt = None
    if since:
        since_dt = dt.datetime.strptime(since, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=dt.timezone.utc)
    trades = []
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "FILLED":
                continue
            try:
                ts = dt.datetime.strptime(row["ts"][:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=dt.timezone.utc)
                if since_dt and ts < since_dt:
                    continue
                trades.append({
                    "ts_ms": int(ts.timestamp() * 1000),
                    "ts": ts,
                    "side": row["side"],
                    "entry": float(row["entryPrice"]),
                    "exit": float(row["exitPrice"]),
                    "qty": float(row["qty"]),
                    "pnl": float(row["pnl"]),
                    "reason": row["exitReason"],
                    "msg": row["msg"],
                })
            except (ValueError, KeyError):
                continue
    return trades


def build_html(klines: list[list], trades: list[dict], title: str) -> str:
    # Séries
    t_axis = [k[0] for k in klines]                       # openTime
    closes = [float(k[4]) for k in klines]                # close
    # Bornes
    all_prices = closes + [t["entry"] for t in trades] + [t["exit"] for t in trades]
    lo, hi = min(all_prices), max(all_prices)
    pad = max((hi - lo) * 0.08, 1.0)
    ymin, ymax = lo - pad, hi + pad

    klines_json = json.dumps({"t": t_axis, "c": closes})
    trades_json = json.dumps(trades, default=lambda o: o.isoformat() if isinstance(o, dt.datetime) else str(o))
    bounds_json = json.dumps({"ymin": ymin, "ymax": ymax, "lo": lo, "hi": hi})

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  body {{ background:#0d1117; color:#c9d1d9; font-family:ui-monospace,Menlo,monospace; margin:0; padding:18px; }}
  h1 {{ font-size:15px; letter-spacing:.08em; color:#58a6ff; }}
  .meta {{ font-size:11px; color:#8b949e; margin-bottom:10px; }}
  #wrap {{ position:relative; width:min(1200px,96vw); }}
  canvas {{ width:100%; height:70vh; background:#0d1117; border:1px solid #30363d; border-radius:6px; display:block; }}
  .legend {{ display:flex; gap:16px; font-size:11px; margin-top:8px; color:#8b949e; }}
  .legend i {{ display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:4px; vertical-align:-1px; }}
  #tip {{ position:fixed; display:none; background:#161b22; border:1px solid #30363d; border-radius:4px;
          padding:6px 9px; font-size:11px; pointer-events:none; z-index:9; max-width:420px; }}
  #tip b {{ color:#58a6ff; }}
</style>
</head>
<body>
<h1>BTCUSDT — testnet · points d'entrée / sortie</h1>
<div class="meta" id="meta"></div>
<div id="wrap">
  <canvas id="cv"></canvas>
</div>
<div class="legend">
  <span><i style="background:#3fb950"></i>Entrée BUY (long)</span>
  <span><i style="background:#f85149"></i>Entrée SELL (short)</span>
  <span><i style="background:#e3b341"></i>Sortie (croix)</span>
  <span><i style="background:#58a6ff"></i>Prix BTC (close 1m)</span>
</div>
<div id="tip"></div>
<script>
const k = {klines_json};
const tr = {trades_json};
const B = {bounds_json};
const cv = document.getElementById('cv');
const tip = document.getElementById('tip');
const dpr = window.devicePixelRatio || 1;
let W = 0, H = 0;

function resize(){{
  const r = cv.getBoundingClientRect();
  W = r.width; H = r.height;
  cv.width = W * dpr; cv.height = H * dpr;
  const ctx = cv.getContext('2d');
  ctx.setTransform(dpr,0,0,dpr,0,0);
  draw(ctx);
}}
window.addEventListener('resize', resize);

function x(ts){{
  const t0 = k.t[0], t1 = k.t[k.t.length-1];
  return 14 + (ts - t0) / (t1 - t0) * (W - 28);
}}
function y(px){{ return 10 + (B.ymax - px) / (B.ymax - B.ymin) * (H - 40); }}

function draw(ctx){{
  ctx.clearRect(0,0,W,H);
  // grille horizontale
  ctx.strokeStyle = '#21262d'; ctx.fillStyle = '#8b949e'; ctx.font = '10px ui-monospace,Menlo';
  for (let i = 0; i <= 5; i++){{
    const px = B.ymin + (B.ymax - B.ymin) * i / 5;
    const yy = y(px);
    ctx.beginPath(); ctx.moveTo(14, yy); ctx.lineTo(W-14, yy); ctx.stroke();
    ctx.fillText(px.toFixed(0), 2, yy - 3);
  }}
  // courbe prix
  ctx.strokeStyle = '#58a6ff'; ctx.lineWidth = 1.4; ctx.beginPath();
  for (let i = 0; i < k.t.length; i++){{
    const xx = x(k.t[i]), yy = y(k.c[i]);
    i === 0 ? ctx.moveTo(xx, yy) : ctx.lineTo(xx, yy);
  }}
  ctx.stroke();
  // points trades
  tr.forEach(t => {{
    const xx = x(t.ts_ms), yy = y(t.entry);
    const green = t.side === 'BUY';
    ctx.beginPath();
    ctx.fillStyle = green ? '#3fb950' : '#f85149';
    ctx.strokeStyle = '#0d1117'; ctx.lineWidth = 1;
    ctx.arc(xx, yy, 4.5, 0, Math.PI*2); ctx.fill(); ctx.stroke();
    // croix sortie
    const yy2 = y(t.exit);
    ctx.strokeStyle = '#e3b341'; ctx.lineWidth = 1.2;
    const s = 4;
    ctx.beginPath();
    ctx.moveTo(xx-s, yy2-s); ctx.lineTo(xx+s, yy2+s);
    ctx.moveTo(xx+s, yy2-s); ctx.lineTo(xx-s, yy2+s);
    ctx.stroke();
  }});
}}

// infobulle
const pos = tr.length ? {{}} : null;
cv.addEventListener('mousemove', e => {{
  const r = cv.getBoundingClientRect();
  const mx = e.clientX - r.left, my = e.clientY - r.top;
  let near = null, best = 14;
  tr.forEach(t => {{
    const d = Math.hypot(x(t.ts_ms) - mx, y(t.entry) - my);
    if (d < best){{ best = d; near = t; }}
  }});
  if (near){{
    const win = near.pnl > 0 ? '#3fb950' : near.pnl < 0 ? '#f85149' : '#8b949e';
    tip.style.display = 'block';
    tip.style.left = (e.clientX + 14) + 'px';
    tip.style.top = (e.clientY - 10) + 'px';
    tip.innerHTML = `<b>${{near.ts.slice(0,19)}}</b> ${{near.side}} qty=${{near.qty.toFixed(4)}}<br>
      entrée <b>${{near.entry.toFixed(1)}}</b> → sortie <b>${{near.exit.toFixed(1)}}</b><br>
      pnl <span style="color:${{win}}"><b>${{near.pnl.toFixed(3)}}</b></span> · ${{near.reason}}<br>
      <span style="color:#8b949e">${{near.msg.slice(0,110)}}</span>`;
  }} else {{
    tip.style.display = 'none';
  }}
}});

document.getElementById('meta').textContent =
  `${{tr.length}} trades FILLED · ${{k.t.length}} bougies 1m · fenêtre ${{new Date(k.t[0]).toISOString().slice(0,19)}}Z → ${{new Date(k.t[k.t.length-1]).toISOString().slice(0,19)}}Z · bas ${{B.lo.toFixed(0)}} / haut ${{B.hi.toFixed(0)}}`;
resize();
</script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=str(ROOT / "runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv"))
    ap.add_argument("--out", default="/tmp/btc_trades.html")
    ap.add_argument("--interval", default="1m")
    ap.add_argument("--since", default=None, help="ne garder que les trades après cette date UTC (ex: 2026-08-14T16:24:00)")
    args = ap.parse_args()

    csv_path = Path(args.csv)
    trades = load_trades(csv_path, args.since)
    if not trades:
        print("Aucun trade FILLED trouvé.", file=sys.stderr)
        return 1

    # Fenêtre : 10 min avant le premier trade → 5 min après le dernier
    t0 = trades[0]["ts_ms"] - 10 * 60_000
    t1 = trades[-1]["ts_ms"] + 5 * 60_000
    klines = fetch_klines("BTCUSDT", args.interval, t0, t1)
    if not klines:
        print("Aucune kline récupérée — graphique sans courbe (points seuls).", file=sys.stderr)

    html = build_html(klines, trades, "BTCUSDT testnet — trades")
    out = Path(args.out)
    out.write_text(html, encoding="utf-8")
    print(f"OK: {out}")
    print(f"  {len(trades)} trades · {len(klines)} bougies · {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
