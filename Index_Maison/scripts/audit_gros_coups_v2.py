#!/usr/bin/env python3
# AUDIT GROS COUPS v2 — lecture seule. MODÈLE DE FRAIS CORRIGÉ :
#   réel Binance (calibré 21/08) : 4,00 bps PAR CÔTÉ -> 8 bps aller-retour
#   fee = (ep*q)*4bps + (xp*q)*4bps = (ep+xp)*q*0.0004
#   (la v1 appliquait 8 bps sur la somme = 16 bps RT -> nets deux fois trop pessimistes)
# Validation croisée : bps implicites des feeUsdt enregistrés par le moteur (ACE_*).
import csv, glob, os
from datetime import datetime, timezone

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
SEUIL = 15.0
BPS_SIDE = 4.0  # calibré sur commissions Binance réelles (médiane 4.00)

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

rows, engine_bps = [], []
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
                pnl = to_f(r.get('pnl'))
                if pnl is None: continue
                ep, xp, q = to_f(r.get('entryPrice')), to_f(r.get('exitPrice')), to_f(r.get('qty'))
                if has_fee:
                    fee_rec = to_f(r.get('feeUsdt'))
                    if fee_rec and ep and xp and q and (ep + xp) * q > 0:
                        engine_bps.append(fee_rec / ((ep + xp) * q) * 10000)
                    fee = fee_rec if fee_rec is not None else ((ep + xp) * q * BPS_SIDE / 10000.0 if ep and xp and q else None)
                else:
                    fee = (ep + xp) * q * BPS_SIDE / 10000.0 if ep and xp and q else None
                rows.append(dict(file=base, ts=parse_ts(r.get('ts')), tsraw=(r.get('ts') or '').strip(),
                                 side=(r.get('side') or '?').strip().upper(), pnl=pnl, fee=fee,
                                 net=(pnl - fee) if fee is not None else None, hold=to_f(r.get('holdSec')),
                                 q=q, ep=ep, xp=xp, reason=(r.get('exitReason') or '')))
    except Exception as e:
        print(f'!! {base}: {e}')

tot_gross = sum(r['pnl'] for r in rows)
tot_fees  = sum((r['fee'] or 0) for r in rows)
tot_net   = sum((r['net'] or 0) for r in rows)
big = sorted([r for r in rows if r['pnl'] >= SEUIL], key=lambda r: -r['pnl'])
big_gross = sum(r['pnl'] for r in big); big_fees = sum((r['fee'] or 0) for r in big); big_net = sum((r['net'] or 0) for r in big)
rest_gross = tot_gross - big_gross; rest_fees = tot_fees - big_fees; rest_net = tot_net - big_net

print(f'=== TABLE DES GROS COUPS v2 (fees 4bps/côté calibrés Binance) — {len(big)} trades ===')
print(f'{"date":<17}{"session":<42}{"side":<6}{"hold":>6}{"brut":>9}{"fees":>8}{"net":>9}  exit')
for r in big:
    d = r['ts'].strftime('%d/%m %H:%M') if r['ts'] else r['tsraw'][:16]
    h = f"{r['hold']:.0f}s" if r['hold'] else '?'
    print(f'{d:<17}{r["file"][:41]:<42}{r["side"][:5]:<6}{h:>6}{r["pnl"]:>9.2f}{(r["fee"] or 0):>8.2f}{(r["net"] or 0):>9.2f}  {r["reason"][:30]}')
print(f'\n13 GROS COUPS  : brut {big_gross:+.2f}  fees {big_fees:.2f}  NET {big_net:+.2f}$')
print(f'LE RESTE ({len(rows)-len(big)} trades) : brut {rest_gross:+.2f}  fees {rest_fees:.2f}  NET {rest_net:+.2f}$')
print(f'TOUTES SESSIONS ({len(rows)} trades) : brut {tot_gross:+.2f}  fees {tot_fees:.2f}  NET {tot_net:+.2f}$')
print(f'\nValidation modèle : bps implicites des feeUsdt moteur (médiane) = {sorted(engine_bps)[len(engine_bps)//2]:.2f} bps/côté' if engine_bps else '\nPas de feeUsdt moteur pour validation.')
