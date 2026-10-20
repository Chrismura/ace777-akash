#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CHIFFRAGE ATTRIBUTION."""
import csv, glob, json, os, sys
from collections import defaultdict, deque
from datetime import datetime
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(SCRIPTS, "..", "runs")
FEE = 0.0005 + float(os.environ.get("REPLAY_SLIP_BPS", "0")) / 10000.0
def ts(s):
    try: return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except: return None
def dernier_csv():
    return sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)[-1]
def fam(reason, ev):
    r = reason or ""
    if ev == "BUY":
        if r.startswith("SEED"): return "SEED"
        if "impulse" in r: return "impulse"
        if "reentry" in r: return "reentry_dump"
        if "cooling" in r: return "cooling"
        if "cash_redeploy" in r: return "cash_redeploy"
        if "gbag_entree" in r: return "gbag_entree"
        return "buy_autre:" + r[:30]
    if ev in ("SELL", "SELL_PARTIAL"):
        if "trailing_peak" in r: return "trailing"
        if r.startswith("stop"): return "stop"
        if "dust_sweep" in r: return "dust_sweep"
        if "stake_out" in r: return "stake_out"
        if "trend_stop" in r: return "trend_stop"
        if "trend_palier" in r: return "trend_palier"
        if "trend_trail" in r: return "trend_trail"
        if "gbag_sortie" in r: return "gbag_sortie"
        return "sell_autre:" + r[:30]
    if ev in ("BAG_SELL", "BAG_CRASH"):
        if "crash" in r: return "bag_crash"
        if "slow" in r: return "bag_slow"
        return "bag_autre:" + r[:30]
    return ev
def main():
    rows = list(csv.DictReader(open(dernier_csv(), newline="", encoding="utf-8-sig")))
    bpx = []
    for r in rows:
        if (r.get("pair") or "").strip() != "BTCUSDT": continue
        t = ts(r.get("ts"))
        try: x = float(r.get("price") or 0)
        except: continue
        if t and x > 0: bpx.append((t, x))
    bpx.sort()
    bclose = {}
    dd = defaultdict(list)
    for t, x in bpx: dd[t.date()].append(x)
    for d, v in dd.items(): bclose[d] = v[-1]
    bdays = sorted(bclose)
    bret = {}
    for i in range(1, len(bdays)):
        if (bdays[i] - bdays[i - 1]).days <= 3:
            bret[bdays[i]] = bclose[bdays[i]] / bclose[bdays[i - 1]] - 1
    pos = defaultdict(deque)
    bag = defaultdict(deque)
    by_entry = defaultdict(lambda: [0.0, 0])
    by_exit = defaultdict(lambda: [0.0, 0])
    by_pair = defaultdict(lambda: [0.0, 0])
    red_clone = [0.0, 0]
    red_indep = [0.0, 0]
    nrm_clone = [0.0, 0]
    nrm_indep = [0.0, 0]
    CLONES = {"ETHUSDT", "ZBCNUSDT", "XRPUSDT", "REDUSDT", "PYTHUSDT", "KITEUSDT", "CCUSDT", "TELUSDT"}
    INDEP = {"RIZEUSDT", "RWAINCUSDT", "BIOUSDT", "CHIPUSDT"}
    csv_pnl = 0.0
    attr_pnl = 0.0
    for r in rows:
        ev = (r.get("event") or "").strip()
        p = (r.get("pair") or "").strip()
        if not p or ev in ("SKIP", "DUST_DROP"): continue
        try:
            q = float(r.get("qty") or 0)
            px = float(r.get("price") or 0)
        except: continue
        note = r.get("reason") or ""
        t = ts(r.get("ts"))
        if ev in ("BUY", "GBAG_PYRAMIDE"):
            pos[p].append([q, px, t, fam(note, "BUY")])
        elif ev == "GBAG_SOUCHE":
            bag[p].append([q, px, t, "gbag_souche"])
        elif ev == "BAG_DCA":
            if "trend_" in note: pos[p].append([q, px, t, "trend_add"])
            else: bag[p] = deque([[q, px, t, "bag_dca"]])
        elif ev == "BAG_ARM":
            if "core_trend" in note:
                mv = min(q, sum(x[0] for x in pos[p]))
                rest = mv
                while rest > 1e-12 and pos[p]:
                    take = min(pos[p][0][0], rest)
                    l = pos[p][0]
                    bag[p].append([take, l[1], l[2], l[3]])
                    l[0] -= take; rest -= take
                    if l[0] <= 1e-12: pos[p].popleft()
            elif "house_half" in note:
                bag[p] = deque([[q, px, t, "stake_keep"]])
                pos[p] = deque()
            elif "conservation_half" in note:
                pos[p] = deque()
        elif ev in ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH"):
            try: pc = float(r.get("pnl_usdt") or 0)
            except: pc = 0.0
            csv_pnl += pc
            book = pos if ev in ("SELL", "SELL_PARTIAL") else bag
            fx = fam(note, ev)
            rest = q
            while rest > 1e-12 and book[p]:
                l = book[p][0]
                take = min(l[0], rest)
                pnl = (px - l[1]) * take - px * take * FEE
                attr_pnl += pnl
                by_entry[l[3]][0] += pnl; by_entry[l[3]][1] += 1
                by_exit[fx][0] += pnl; by_exit[fx][1] += 1
                by_pair[p][0] += pnl; by_pair[p][1] += 1
                bd = bret.get(t.date()) if t else None
                if bd is not None and bd <= -0.02 and l[3] != "SEED":
                    tgt = red_clone if p in CLONES else (red_indep if p in INDEP else None)
                    if tgt is not None: tgt[0] += pnl; tgt[1] += 1
                elif bd is not None and l[3] != "SEED":
                    tgt = nrm_clone if p in CLONES else (nrm_indep if p in INDEP else None)
                    if tgt is not None: tgt[0] += pnl; tgt[1] += 1
                l[0] -= take; rest -= take
                if l[0] <= 1e-12: book[p].popleft()
    print(f"VALIDATION attribue={attr_pnl:.2f} vs csv={csv_pnl:.2f} ecart={attr_pnl-csv_pnl:+.2f}")
    print("\n=== PnL par motif ENTREE (trades adosses FIFO, hors frais achat) ===")
    for k, (v, n) in sorted(by_entry.items(), key=lambda kv: -kv[1][0]):
        print(f"  {k:<22} {v:>+9.2f}$  n={n:<4} /trade={v/max(n,1):+7.3f}")
    print("\n=== PnL par motif SORTIE ===")
    for k, (v, n) in sorted(by_exit.items(), key=lambda kv: -kv[1][0]):
        print(f"  {k:<22} {v:>+9.2f}$  n={n:<4} /trade={v/max(n,1):+7.3f}")
    print("\n=== FILTRE BTC selectif (entrees jours BTC<=-2%, clones vs indep, hors SEED) ===")
    for nom, t in (("clone+rouge", red_clone), ("indep+rouge", red_indep),
                   ("clone+normal", nrm_clone), ("indep+normal", nrm_indep)):
        print(f"  {nom:<14} {t[0]:>+9.2f}$  n={t[1]:<4} /trade={t[0]/max(t[1],1):+7.3f}")
    print("\n=== PnL attribue par paire (realise, hors terminal) ===")
    for k, (v, n) in sorted(by_pair.items(), key=lambda kv: -kv[1][0]):
        print(f"  {k:<12} {v:>+9.2f}$  n={n}")
    json.dump({"csv_pnl": round(csv_pnl, 2), "attr_pnl": round(attr_pnl, 2),
               "by_entry": {k: [round(v[0], 2), v[1]] for k, v in by_entry.items()},
               "by_exit": {k: [round(v[0], 2), v[1]] for k, v in by_exit.items()},
               "btc": {"rc": red_clone, "ri": red_indep, "nc": nrm_clone, "ni": nrm_indep},
               "by_pair": {k: [round(v[0], 2), v[1]] for k, v in by_pair.items()}},
              open(os.path.join(RUNS, "CHIFFRAGE_ATTRIBUTION.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n-> runs/CHIFFRAGE_ATTRIBUTION.json")
    return 0
if __name__ == "__main__":
    sys.exit(main())
