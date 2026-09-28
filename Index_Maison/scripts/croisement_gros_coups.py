#!/usr/bin/env python3
# CROISEMENT 13 GROS COUPS × KLINES 1m — lecture seule (+ fetch public Binance si manquant, zéro clé, zéro ordre).
# HYPOTHÈSE FIGÉE AVANT ANALYSE (philosophie HUNTER du vault, 28/08) :
#   « On n'achète pas la pompe, on est censé être déjà dedans » -> les gros coups sont entrés PENDANT
#   une impulsion déjà en cours, pas avant. Test : le prix bougeait-il déjà dans le sens du trade
#   dans les minutes AVANT l'entrée ?
import csv, glob, os, json, statistics, urllib.request, time
from datetime import datetime, timezone, timedelta

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
def to_f(x):
    try: return float(x)
    except (TypeError, ValueError): return None

# --- 1) Extraire les 13 gros coups (ts, side, ep, q, pnl)
wins = []
for path in sorted(glob.glob(os.path.join(RUNS, '*.csv'))):
    base = os.path.basename(path)
    if 'OBSERVATION' in base or 'SHADOW' in base: continue
    if not ('ALPHA' in base.upper() or 'CHAMPION' in base.upper()): continue
    try:
        with open(path, newline='', errors='replace') as f:
            for r in csv.DictReader(f):
                p = to_f(r.get('pnl'))
                if p is None or p < 15: continue
                ep, q = to_f(r.get('entryPrice')), to_f(r.get('qty'))
                ts = (r.get('ts') or '').strip()
                wins.append(dict(ts=ts, side=(r.get('side') or '').upper(), ep=ep, q=q, pnl=p, file=base[:40]))
    except Exception: pass

def parse_ts(s):
    s = str(s).strip()
    try:
        v = float(s)
        if v > 1e12: v /= 1000.0
        if v > 1e9: return datetime.fromtimestamp(v, tz=timezone.utc)
    except ValueError: pass
    for fmt in ('%Y%m%d_%H%M%SZ', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S'):
        try: return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError: continue
    return None

for w in wins: w['dt'] = parse_ts(w['ts'])
wins = sorted([w for w in wins if w['dt']], key=lambda w: w['dt'])
print(f'--- 13 GROS COUPS : {len(wins)} datés')
for w in wins:
    print(f"  {w['dt'].strftime('%d/%m %H:%M')} {w['side']:<5} pnl={w['pnl']:>7.2f}  ep={w['ep']}  {w['file'][:34]}")

# --- 2) Couverture des klines en cache
print('\n--- COUVERTURE KLINES EN CACHE ---')
cover = {}
for path in glob.glob(os.path.join(RUNS, 'KLINES_1M_*.csv')):
    base = os.path.basename(path)
    tss = []
    with open(path, newline='', errors='replace') as f:
        rdr = csv.DictReader(f)
        col = 'ts' if rdr.fieldnames and 'ts' in rdr.fieldnames else (rdr.fieldnames[0] if rdr.fieldnames else None)
        for r in rdr:
            v = parse_ts(r.get(col)) if col else None
            if v: tss.append(v)
    if tss:
        cover[base] = (min(tss), max(tss), len(tss))
        print(f'  {base:<28} {min(tss).strftime("%d/%m %H:%M")} -> {max(tss).strftime("%d/%m %H:%M")}  ({len(tss)} barres)')

# --- 3) Fetch public des klines manquants (fenêtre ±90 min autour de chaque gros coup)
def fetch_klines(start, end):
    url = (f'https://fapi.binance.com/fapi/v1/klines?symbol=BTCUSDT&interval=1m&startTime={int(start.timestamp()*1000)}'
           f'&endTime={int(end.timestamp()*1000)}&limit=200')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                return json.load(resp)
        except Exception as e:
            if attempt == 2: print(f'  fetch KO {start:%d/%m %H:%M}: {e}')
            time.sleep(1.5)
    return []

print('\n--- CONTEXTE DE MARCHÉ (klines ±90 min, public BTCUSDT) ---')
print(f'{"date":<12}{"sens":<6}{"pnl":>7} | {"ret60 AVANT":>11}{"ret5 AVANT":>11}{"vol5/vol60":>11}{"move capturé":>13} | déjà dedans ?')
for w in wins:
    start, end = w['dt'] - timedelta(minutes=90), w['dt'] + timedelta(minutes=10)
    ks = fetch_klines(start, end)
    if not ks:
        print(f"{w['dt'].strftime('%d/%m %H:%M'):<12}{w['side']:<6}{w['pnl']:>7.2f} | klines indisponibles")
        continue
    closes = [(int(k[0]), float(k[4])) for k in ks]
    entry_ms = int(w['dt'].timestamp() * 1000)
    hist = [c for t, c in closes if t <= entry_ms]
    if len(hist) < 20:
        print(f"{w['dt'].strftime('%d/%m %H:%M'):<12}{w['side']:<6}{w['pnl']:>7.2f} | historique insuffisant ({len(hist)})")
        continue
    e = hist[-1]
    sgn = 1 if w['side'] == 'BUY' else -1
    ret60 = (e / hist[-61] - 1) * 100 * sgn if len(hist) >= 61 else None   # % dans le sens du trade
    ret5 = (e / hist[-6] - 1) * 100 * sgn
    rets = [hist[i] / hist[i-1] - 1 for i in range(max(1, len(hist)-60), len(hist))]
    vol60 = statistics.pstdev(rets) * 100 if len(rets) > 2 else None
    rets5 = [hist[i] / hist[i-1] - 1 for i in range(max(1, len(hist)-5), len(hist))]
    vol5 = statistics.pstdev(rets5) * 100 if len(rets5) > 1 else None
    ratio = (vol5 / vol60) if (vol5 is not None and vol60 and vol60 > 0) else None
    move = w['pnl'] / (w['ep'] * w['q']) * 10000 if (w['ep'] and w['q']) else None  # bps
    verdict = 'OUI déjà dedans' if (ret5 is not None and ret5 > 0.05) else 'NON (entrée avant/silence)'
    print(f"{w['dt'].strftime('%d/%m %H:%M'):<12}{w['side']:<6}{w['pnl']:>7.2f} | "
          f"{(f'{ret60:+.2f}%' if ret60 is not None else '—'):>11}"
          f"{(f'{ret5:+.2f}%' if ret5 is not None else '—'):>11}"
          f"{(f'{ratio:.1f}x' if ratio is not None else '—'):>11}"
          f"{(f'{move:.0f}bps' if move is not None else '—'):>13} | {verdict}")
    time.sleep(0.35)
