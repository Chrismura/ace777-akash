#!/usr/bin/env python3
# FILTRE EX-ANTE OUTCOME-BLIND + CORRECTIONS FINALES — lecture seule.
# RÈGLE FIGÉE AVANT TOUTE ÉVALUATION (déclarée ici, ne pas retoucher après) :
#   BUY  si ask_drop >= p95(ask_drop des BUY)  ET conf >= 0.90
#   SELL si bid_drop >= p95(bid_drop des SELL) ET conf >= 0.90
# Justification : physique L2 (le carnet opposé s'effondre = burst dans notre sens, enquete_franchi :
# évaporation -> traversée en 5 s médian) + sélectivité (les 61-82 % historiques = ultra-sélectivité).
# Les seuils p95/0.90 viennent des DISTRIBUTIONS DES SIGNAUX et de la CONVENTION, jamais des pnl.
import csv, glob, os, re
from datetime import datetime, timezone

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
def to_f(x):
    try: return float(x)
    except (TypeError, ValueError): return None
def parse_ts(s):
    if not s: return None
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

trades = []
for path in sorted(glob.glob(os.path.join(RUNS, '*.csv'))):
    base = os.path.basename(path)
    if 'OBSERVATION' in base or 'SHADOW' in base: continue
    if not ('ALPHA' in base.upper() or 'CHAMPION' in base.upper()): continue
    try:
        with open(path, newline='', errors='replace') as f:
            rdr = csv.DictReader(f)
            if not rdr.fieldnames or 'pnl' not in rdr.fieldnames: continue
            has_fee = 'feeUsdt' in rdr.fieldnames
            for r in rdr:
                p = to_f(r.get('pnl'))
                if p is None or p == 0: continue  # skips les lignes-wait (status SKIPPED)
                ep, xp, q = to_f(r.get('entryPrice')), to_f(r.get('exitPrice')), to_f(r.get('qty'))
                fee = to_f(r.get('feeUsdt')) if has_fee else None
                if fee is None and ep and xp and q: fee = (ep + xp) * q * 0.0004
                m = r.get('msg') or ''
                def grab(k):
                    mm = re.search(k + r'=([^\s]+)', m)
                    return to_f(mm.group(1)) if mm else None
                trades.append(dict(file=base, ts=parse_ts(r.get('ts')), side=(r.get('side') or '').upper(),
                                   pnl=p, fee=fee, net=(p - fee) if fee is not None else None,
                                   ask_drop=grab('ask_drop'), bid_drop=grab('bid_drop'), conf=grab('conf')))
    except Exception as e:
        print(f'!! {base}: {e}')

# --- Winrate par ère + frais réels (vrais trades uniquement)
print('=== CORRECTIONS FINALES (vrais trades, pnl != 0) ===')
tot_fees = sum((t['fee'] or 0) for t in trades)
print(f'n={len(trades)}  brut={sum(t["pnl"] for t in trades):+.2f}$  fees={tot_fees:.2f}$  '
      f'net={sum(t["net"] or 0 for t in trades):+.2f}$  fee moyen/trade={tot_fees/len(trades):.2f}$')
for lbl, lo, hi in [('avant 01/08', None, '2026-08-01'), ('août', '2026-08-01', None)]:
    sub = [t for t in trades if t['ts'] and (not lo or str(t['ts'].date()) >= lo) and (not hi or str(t['ts'].date()) < hi)]
    if sub:
        w = sum(1 for t in sub if t['pnl'] > 0)
        f = sum((t['fee'] or 0) for t in sub)
        print(f'  {lbl:<12} n={len(sub):<6} winrate={100*w/len(sub):.1f}%  brut={sum(t["pnl"] for t in sub):+9.2f}$  fees={f:8.2f}$  net={sum(t["net"] or 0 for t in sub):+9.2f}$')

# --- Trades porteurs de msg (août+) et distributions des SIGNAUX (outcome-blind)
msg_t = [t for t in trades if t['ask_drop'] is not None or t['bid_drop'] is not None]
print(f'\n=== SIGNAUX MSG : {len(msg_t)} trades porteurs ===')
def pct(vals, p):
    v = sorted(vals); return v[min(int(p*len(v)), len(v)-1)]
buy_d = [t['ask_drop'] for t in msg_t if t['side'] == 'BUY' and t['ask_drop'] is not None]
sell_d = [t['bid_drop'] for t in msg_t if t['side'] == 'SELL' and t['bid_drop'] is not None]
confs = [t['conf'] for t in msg_t if t['conf'] is not None]
if buy_d: print(f'BUY  ask_drop : p50={pct(buy_d,.5):.6g} p90={pct(buy_d,.9):.6g} p95={pct(buy_d,.95):.6g} p99={pct(buy_d,.99):.6g} n={len(buy_d)}')
if sell_d: print(f'SELL bid_drop : p50={pct(sell_d,.5):.6g} p90={pct(sell_d,.9):.6g} p95={pct(sell_d,.95):.6g} p99={pct(sell_d,.99):.6g} n={len(sell_d)}')
if confs: print(f'conf         : p50={pct(confs,.5):.6g} p90={pct(confs,.9):.6g} p95={pct(confs,.95):.6g} n={len(confs)}')

# --- RÈGLE FIGÉE : évaluation (une seule fois)
T_ASK = pct(buy_d, .95) if buy_d else None
T_BID = pct(sell_d, .95) if sell_d else None
print(f'\n=== RÈGLE FIGÉE : dominant_drop >= p95 ET conf >= 0.90 ===')
print(f'seuils figés : ask>={T_ASK:.6g} (BUY)' + (f' · bid>={T_BID:.6g} (SELL)' if T_BID is not None else ' · (aucun SELL avec bid_drop : règle BUY seule)'))
kept = [t for t in msg_t if ((t['side'] == 'BUY' and t['ask_drop'] is not None and T_ASK is not None and t['ask_drop'] >= T_ASK) or
                             (t['side'] == 'SELL' and t['bid_drop'] is not None and T_BID is not None and t['bid_drop'] >= T_BID))
        and (t['conf'] is None or t['conf'] >= 0.90)]
if kept:
    w = sum(1 for t in kept if t['pnl'] > 0)
    g = sum(t['pnl'] for t in kept); f = sum((t['fee'] or 0) for t in kept)
    print(f'gardés : {len(kept)}/{len(msg_t)}  winrate={100*w/len(kept):.1f}%  brut={g:+.2f}$  fees={f:.2f}$  NET={g-f:+.2f}$')
    big = [t for t in kept if t['pnl'] >= 15]
    print(f'gros coups (>=15$) capturés : {len(big)} -> ' + ', '.join(f'{t["pnl"]:+.2f}' for t in sorted(big, key=lambda x: -x["pnl"])))
    print(f'comparaison : TOUS les {len(msg_t)} trades msg : NET={sum(t["net"] or 0 for t in msg_t):+.2f}$')
# variante stricte p99 (robustesse, décidée MAINTENANT aussi)
if buy_d and sell_d:
    kept99 = [t for t in msg_t if ((t['side'] == 'BUY' and t['ask_drop'] is not None and t['ask_drop'] >= pct(buy_d, .99)) or
                                    (t['side'] == 'SELL' and t['bid_drop'] is not None and t['bid_drop'] >= pct(sell_d, .99)))
              and (t['conf'] is None or t['conf'] >= 0.90)]
    if kept99:
        w = sum(1 for t in kept99 if t['pnl'] > 0)
        print(f'variante p99 : gardés={len(kept99)}  winrate={100*w/len(kept99):.1f}%  NET={sum(t["net"] or 0 for t in kept99):+.2f}$  '
              f'gros coups={sum(1 for t in kept99 if t["pnl"]>=15)}')
