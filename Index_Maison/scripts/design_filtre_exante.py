#!/usr/bin/env python3
# RECOMPTAGE PROPRE + EXPLORATION MSG (design set uniquement) — lecture seule.
# DÉCOUVERTE DU JOUR : les CSV mélangent des lignes TRADE et des lignes WAIT/CYCLE à pnl=0,00
# (ALPHA_HUNTER : 814/832 lignes à 0,00 = les cycles duo_wait). Recomptage sur VRAIS trades.
# SPLIT FIGÉ : DESIGN = trades < 2026-08-01 · HOLDOUT = >= 2026-08-01 (touché au prochain script seulement).
import csv, glob, os, re, statistics
from datetime import datetime, timezone

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
CUT = datetime(2026, 8, 1, tzinfo=timezone.utc)

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

# --- A) Que sont les lignes à 0,00 ? (sonde ALPHA_HUNTER)
print('=== A) LIGNES 0,00 — QUE SONT-ELLES ? (ALPHA_HUNTER) ===')
shown = 0
with open(os.path.join(RUNS, 'ALPHA_HUNTER.csv'), newline='', errors='replace') as f:
    rdr = csv.DictReader(f)
    for r in rdr:
        if to_f(r.get('pnl')) == 0.0 and shown < 2:
            keep = {k: (v or '')[:60] for k, v in r.items() if v}
            print('  ', keep); shown += 1

# --- B) Recomptage toutes sessions ALPHA : vrais trades vs lignes-wait
print('\n=== B) RECOMPTAGE PROPRE (status FILLED & pnl != 0 = VRAI TRADE) ===')
sess, all_trades = {}, []
for path in sorted(glob.glob(os.path.join(RUNS, '*.csv'))):
    base = os.path.basename(path)
    if 'OBSERVATION' in base or 'SHADOW' in base: continue
    if not ('ALPHA' in base.upper() or 'CHAMPION' in base.upper()): continue
    try:
        with open(path, newline='', errors='replace') as f:
            rdr = csv.DictReader(f)
            if not rdr.fieldnames or 'pnl' not in rdr.fieldnames: continue
            nz = z = 0; g = 0.0
            for r in rdr:
                p = to_f(r.get('pnl'))
                if p is None: continue
                if p == 0: z += 1; continue
                nz += 1; g += p
                ep, xp, q = to_f(r.get('entryPrice')), to_f(r.get('exitPrice')), to_f(r.get('qty'))
                fee = to_f(r.get('feeUsdt')) if rdr.fieldnames and 'feeUsdt' in rdr.fieldnames else None
                if fee is None and ep and xp and q: fee = (ep + xp) * q * 0.0004
                m = r.get('msg') or ''
                def grab(k):
                    mm = re.search(k + r'=([^\s]+)', m)
                    return to_f(mm.group(1)) if mm else None
                all_trades.append(dict(file=base, ts=parse_ts(r.get('ts')), side=(r.get('side') or '').upper(),
                                       pnl=p, fee=fee, net=(p - fee) if fee is not None else None,
                                       hold=to_f(r.get('holdSec')), q=q, ep=ep, xp=xp,
                                       tension=grab('tension'), conf=grab('conf'),
                                       bid_drop=grab('bid_drop'), ask_drop=grab('ask_drop'),
                                       radar=(re.search(r'radar=(\w+)', m).group(1) if re.search(r'radar=(\w+)', m) else None),
                                       msg_ok=bool(m)))
            if nz: sess[base] = (nz, z, g)
    except Exception as e:
        print(f'!! {base}: {e}')

tot_t = sum(s[0] for s in sess.values()); tot_z = sum(s[1] for s in sess.values()); tot_g = sum(s[2] for s in sess.values())
wins = sum(1 for t in all_trades if t['pnl'] > 0)
print(f'VRAIS trades : {tot_t}   lignes-wait (pnl=0) : {tot_z}   brut total : {tot_g:+.2f}$   winrate réel : {100*wins/tot_t:.1f}%')

# --- C) DESIGN SET (< 01/08) : exploration des signaux msg sur les VRAIS trades
print('\n=== C) DESIGN SET (trades < 01/08 uniquement) — signaux msg ===')
des = [t for t in all_trades if t['ts'] and t['ts'] < CUT]
hol_n = sum(1 for t in all_trades if t['ts'] and t['ts'] >= CUT)
print(f'design n={len(des)}   holdout n={hol_n}   (msg présent : {sum(1 for t in des if t["msg_ok"])}/{len(des)})')
for lbl, cond in [('winners >=15$', lambda t: t['pnl'] >= 15), ('winners >=8$', lambda t: t['pnl'] >= 8),
                  ('winners >=5$', lambda t: t['pnl'] >= 5), ('TOUS', lambda t: True)]:
    sub = [t for t in des if cond(t)]
    if not sub: continue
    def q(vals, p):
        vals = sorted(v for v in vals if v is not None)
        return vals[min(int(p*len(vals)), len(vals)-1)] if vals else None
    print(f'{lbl:<15} n={len(sub):<6} tension p50={q([t["tension"] for t in sub],.5)} p90={q([t["tension"] for t in sub],.9)}'
          f' | conf p50={q([t["conf"] for t in sub],.5)} | ask_drop p50={q([t["ask_drop"] for t in sub],.5)} p90={q([t["ask_drop"] for t in sub],.9)}'
          f' | bid_drop p90={q([t["bid_drop"] for t in sub],.9)}')
# distribution TOUS (pour seuils outcome-blind)
for k in ('tension', 'conf', 'ask_drop', 'bid_drop'):
    vals = sorted(t[k] for t in des if t[k] is not None)
    if vals:
        print(f'  TOUS {k}: p50={vals[len(vals)//2]:.6g}  p90={vals[int(.9*len(vals))]:.6g}  p95={vals[int(.95*len(vals))]:.6g}  p99={vals[int(.99*len(vals))]:.6g}  max={vals[-1]:.6g}  n={len(vals)}')
# radar
import collections
print('radar :', dict(collections.Counter((t['radar'] or '?') for t in des).most_common(6)))
# winners>=5 : quel côté du drop ?
w5 = [t for t in des if t['pnl'] >= 5 and (t['ask_drop'] is not None or t['bid_drop'] is not None)]
dom = [('ask' if (t['ask_drop'] or 0) > (t['bid_drop'] or 0) else 'bid') for t in w5]
print('winners>=5 n=', len(w5), 'drop dominant :', dict(collections.Counter(dom)))
