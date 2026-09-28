#!/usr/bin/env python3
# AUDIT GROS COUPS — lecture seule, zéro contact moteur, zéro conclusion anticipée.
# RÈGLES FIGÉES AVANT L'ANALYSE :
#   GROS COUP := trade clôturé avec pnl >= 15 $ (seuil posé avant d'avoir vu la distribution)
#   NET      := gross − fees
#                si feeUsdt/pnlNet sont dans le CSV -> on utilise CE QUE LE MOTEUR A ENREGISTRÉ (source > modèle)
#                sinon -> fees = (entryPrice+exitPrice)*qty*0.0004  (4 bps/aller = 8 bps aller-retour, modèle famille R30)
# Sortie : 1) chronologie frais  2) table des gros coups toutes sessions  3) caractérisation sniper  4) calibration Binance réelle
import csv, glob, os, sys
from datetime import datetime, timezone

RUNS = os.path.expanduser('~/ace777-test-day1/runs')
SEUIL = 15.0
BPS_RT = 8.0  # bps aller-retour (modèle famille)

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
    for fmt in ('%Y%m%d_%H%M%SZ', '%Y%m%d_%H%M%S', '%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%SZ'):
        try: return datetime.strptime(s.replace('Z','Z'), fmt).replace(tzinfo=timezone.utc) if fmt.endswith('Z') else datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError: continue
    return None

rows_all = []           # tous les trades clôturés ALPHA (sniper) de toutes les sessions
files_fee, files_nofee = [], []

for path in sorted(glob.glob(os.path.join(RUNS, '*.csv'))):
    base = os.path.basename(path)
    if 'OBSERVATION' in base or 'SHADOW' in base: continue
    if not ('ALPHA' in base.upper() or 'CHAMPION' in base.upper()): continue
    try:
        with open(path, newline='', errors='replace') as f:
            rdr = csv.DictReader(f)
            if not rdr.fieldnames or 'pnl' not in rdr.fieldnames: continue
            has_fee = 'feeUsdt' in rdr.fieldnames and 'pnlNet' in rdr.fieldnames
            (files_fee if has_fee else files_nofee).append(base)
            for r in rdr:
                pnl = to_f(r.get('pnl'))
                if pnl is None: continue  # lignes ouvertes/vides
                ep, xp = to_f(r.get('entryPrice')), to_f(r.get('exitPrice'))
                q = to_f(r.get('qty'))
                if has_fee:
                    fee = to_f(r.get('feeUsdt'))
                    net = to_f(r.get('pnlNet'))
                else:
                    fee = (ep + xp) * q * (BPS_RT / 10000.0) if (ep and xp and q) else None
                    net = (pnl - fee) if fee is not None else None
                hold = to_f(r.get('holdSec'))
                ts = parse_ts(r.get('ts'))
                side = (r.get('side') or '?').strip().upper()
                rows_all.append(dict(file=base, has_fee=has_fee, ts=ts, tsraw=(r.get('ts') or '').strip(),
                                     side=side, pnl=pnl, fee=fee, net=net, hold=hold, q=q, ep=ep, xp=xp))
    except Exception as e:
        print(f'!! {base}: {e}', file=sys.stderr)

# ---- 1) CHRONOLOGIE FRAIS : à partir de quand les CSV enregistrent les frais ?
print('=== 1) CHRONOLOGIE DE L\'ENREGISTREMENT DES FRAIS (ta mémoire : mi-août) ===')
print(f'fichiers AVEC colonnes feeUsdt/pnlNet : {len(files_fee)}')
for b in files_fee: print('   +', b)
print(f'fichiers SANS (brut only)            : {len(files_nofee)}')
for b in sorted(files_nofee)[:12]: print('   -', b)
if len(files_nofee) > 12: print(f'   ... et {len(files_nofee)-12} autres')

# ---- 2) TABLE DES GROS COUPS (>= 15 $) toutes sessions
big = sorted([r for r in rows_all if r['pnl'] >= SEUIL], key=lambda r: -(r['pnl']))
print(f'\n=== 2) GROS COUPS (pnl >= {SEUIL:.0f}$) — {len(big)} trades sur {len(rows_all)} clôturés (toutes sessions) ===')
tot_gross = sum(r['pnl'] for r in rows_all)
big_gross = sum(r['pnl'] for r in big)
big_net   = sum((r['net'] or 0) for r in big)
print(f'{"date":<17}{"session":<46}{"side":<6}{"hold":>7}{"brut":>9}{"net":>9}')
for r in big:
    d = r['ts'].strftime('%d/%m %H:%M') if r['ts'] else r['tsraw'][:16]
    h = f"{r['hold']/60:.0f}m" if r['hold'] else '?'
    print(f'{d:<17}{r["file"][:45]:<46}{r["side"][:5]:<6}{h:>7}{r["pnl"]:>9.2f}{(r["net"] or 0):>9.2f}')
print(f'\nBrut total toutes sessions : {tot_gross:+.2f}$')
print(f'Brut des {len(big)} gros coups : {big_gross:+.2f}$  soit {100*big_gross/tot_gross if tot_gross else 0:.0f}% du brut total')
print(f'Net de ces {len(big)} gros coups (modèle/source) : {big_net:+.2f}$')

# ---- 3) CARACTÉRISATION SNIPER (sur les gros coups)
if big:
    print('\n=== 3) CARACTÉRISATION DES GROS COUPS (ce que le "sniper seul" doit reconnaître) ===')
    import collections
    hrs = collections.Counter((r['ts'].hour if r['ts'] else None) for r in big)
    sides = collections.Counter(r['side'] for r in big)
    holds = [r['hold']/60 for r in big if r['hold']]
    sess = collections.Counter(r['file'].split('_ALPHA')[0].split('_CHAMPION')[0] for r in big)
    print('heures (UTC) :', dict(sorted((k or -1, v) for k, v in hrs.items())))
    print('sens        :', dict(sides))
    if holds: print(f'hold moyen  : {sum(holds)/len(holds):.0f} min  (min {min(holds):.0f} / max {max(holds):.0f})')
    print('sessions    :', dict(sess.most_common(8)))
    filt = [r for r in big if r['hold'] and r['hold'] <= 3600]
    print(f'gros coups tenus <= 60 min : {len(filt)}/{len(big)}')

# ---- 4) CALIBRATION SUR DONNÉES BINANCE RÉELLES
rec = os.path.join(RUNS, 'BINANCE_RECONCILED_20260821.csv')
if os.path.exists(rec):
    print('\n=== 4) CALIBRATION FRAIS RÉELS — BINANCE_RECONCILED_20260821.csv (commissions vraies) ===')
    n = tot_pnl = tot_comm = 0.0; w = l = 0; top = []
    with open(rec, newline='', errors='replace') as f:
        for r in csv.DictReader(f):
            p, c = to_f(r.get('realized_pnl')), to_f(r.get('commission'))
            if p is None: continue
            n += 1; tot_pnl += p; tot_comm += abs(c or 0)
            if p >= SEUIL: top.append((r.get('ts','')[:16], p, c))
            if p > 0: w += 1
            elif p < 0: l += 1
    print(f'trades : {n}   wins/losses : {w}/{l}   realized_pnl brut : {tot_pnl:+.2f}$   commissions vraies : {tot_comm:.2f}$')
    print(f'NET Binance réel : {tot_pnl - tot_comm:+.2f}$')
    print(f'Commission moyenne / trade : {tot_comm/max(n,1):.3f}$  (à comparer au modèle famille)')
    if top:
        print(f'gros coups dans ce fichier ({len(top)}) :')
        for t, p, c in sorted(top, key=lambda x: -x[1])[:10]:
            print(f'   {t}  +{p:.2f}$  (comm {c:.3f})')
