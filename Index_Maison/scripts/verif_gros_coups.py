#!/usr/bin/env python3
# VÉRIFICATIONS POINTUES sur l'audit gros coups — lecture seule, zéro contact moteur.
# A) détail brut des lignes suspectes (net négatif sur gros coups, hold=0, date 04/03)
# B) résumé par session (brut / net / winrate) pour vérifier le total +229,77
# C) calibration bps RÉELS : commissions Binance vraies (21/08) + feeUsdt enregistrés par le moteur
import csv, glob, os, statistics
from datetime import datetime, timezone

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
def to_f(x):
    try: return float(x)
    except (TypeError, ValueError): return None

print('=== A) LIGNES SUSPECTES — lecture brute du CSV ===')
checks = [
    ('NUAGE_PROD_4H_ALPHA_X13_BURST13.csv', 32.07),
    ('MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv', 24.28),
    ('MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv', 23.34),
    ('TEST_DUO_HARMONIC_5813_12H30_ALPHA_X13_BURST13.csv', 34.05),
]
for fname, target in checks:
    path = os.path.join(RUNS, fname)
    if not os.path.exists(path):
        print(f'{fname}: ABSENT'); continue
    with open(path, newline='', errors='replace') as f:
        for r in csv.DictReader(f):
            if to_f(r.get('pnl')) == target:
                keep = {k: v for k, v in r.items() if v not in (None, '')}
                print(f'{fname} pnl={target}: {keep}')
                break

print('\n=== B) RÉSUMÉ PAR SESSION (toutes sessions ALPHA) ===')
sess = {}
for path in sorted(glob.glob(os.path.join(RUNS, '*.csv'))):
    base = os.path.basename(path)
    if 'OBSERVATION' in base or 'SHADOW' in base: continue
    if not ('ALPHA' in base.upper() or 'CHAMPION' in base.upper()): continue
    try:
        with open(path, newline='', errors='replace') as f:
            rdr = csv.DictReader(f)
            if not rdr.fieldnames or 'pnl' not in rdr.fieldnames: continue
            g = w = n = 0
            for r in rdr:
                p = to_f(r.get('pnl'))
                if p is None: continue
                n += 1; g += p
                if p > 0: w += 1
            if n: sess[base] = (n, w, g)
    except Exception as e:
        print(f'!! {base}: {e}')
tot = sum(s[2] for s in sess.values())
for b, (n, w, g) in sorted(sess.items(), key=lambda kv: -kv[1][2])[:8]:
    print(f'{b[:55]:<55} fills={n:>6}  winrate={100*w/n if n else 0:>5.1f}%  brut={g:+9.2f}$')
print('   ...')
worst = sorted(sess.items(), key=lambda kv: kv[1][2])[:5]
for b, (n, w, g) in worst:
    print(f'{b[:55]:<55} fills={n:>6}  winrate={100*w/n if n else 0:>5.1f}%  brut={g:+9.2f}$')
print(f'TOTAL {len(sess)} sessions : brut = {tot:+.2f}$')

print('\n=== C) CALIBRATION BPS RÉELS ===')
rec = os.path.join(RUNS, 'BINANCE_RECONCILED_20260821.csv')
if os.path.exists(rec):
    bps_list, notional_list = [], []
    tp = tc = 0.0
    with open(rec, newline='', errors='replace') as f:
        for r in csv.DictReader(f):
            p, c = to_f(r.get('realized_pnl')), to_f(r.get('commission'))
            q, pr = to_f(r.get('qty')), to_f(r.get('price'))
            if p is None: continue
            tp += p; tc += abs(c or 0)
            if q and pr:
                notional = q * pr
                notional_list.append(notional)
                if c is not None and notional > 0: bps_list.append(abs(c) / notional * 10000)
    print(f'BINANCE_RECONCILED (21/08, données vraies Binance) :')
    if bps_list:
        print(f'  bps commission médian : {statistics.median(bps_list):.2f}   (p25 {sorted(bps_list)[len(bps_list)//4]:.2f} / p75 {sorted(bps_list)[3*len(bps_list)//4]:.2f})')
    if notional_list:
        print(f'  notional médian : {statistics.median(notional_list):.0f}$   total : {sum(notional_list):,.0f}$')
    print(f'  brut {tp:+.2f}$  commissions {tc:.2f}$  NET {tp-tc:+.2f}$')

print('\nFichiers avec feeUsdt enregistrés par le moteur :')
for path in sorted(glob.glob(os.path.join(RUNS, '*ALPHA*.csv'))):
    base = os.path.basename(path)
    with open(path, newline='', errors='replace') as f:
        rdr = csv.DictReader(f)
        if not rdr.fieldnames or 'feeUsdt' not in rdr.fieldnames: continue
        g = tf = tn = n = 0
        for r in rdr:
            p, fee, net = to_f(r.get('pnl')), to_f(r.get('feeUsdt')), to_f(r.get('pnlNet'))
            if p is None: continue
            n += 1; g += p
            if fee is not None: tf += abs(fee)
            if net is not None: tn += net
        print(f'  {base[:60]:<60} fills={n:>6} brut={g:+9.2f} fees={tf:8.2f} net={tn:+9.2f}')
