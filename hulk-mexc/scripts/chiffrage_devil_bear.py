#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_devil_bear.py — PHASE 1 (GO Christophe « gère la cadence », 23/10).

Question : un AVOCAT DU DIABLE (2e avis bear avant chaque BUY, inspiré G5
TradingAgents) aurait-il évité de mauvais trades sans tuer l'amplitude ?

BEAR-CONTEXTE (pré-enregistré AVANT mesure, champs stables de history.jsonl
30/07->now — pas de taker/whales, ajoutés trop tard) : BEAR si >= 2 vrais sur :
  (1) longShort >= 2.0 (longs bondés = purge probable),
  (2) funding > 1.5x fundingAvg30 (portage cher),
  (3) chg24 <= -1.0 % (vent contre),
  (4) climate == 'hot' (score haut).
Outcome par BUY : FIFO lots par paire (SEED/BUY/DCA/GBAG_PYRAMIDE/BAG_DCA/
GBAG_SOUCHE poussent ; SELL*/STOP/BAG_SELL/BAG_CRASH consomment ; BAG_ARM
neutre/transfert). Positions encore ouvertes : valorisées au mark DIGEST live.
RÈGLE DE DÉCISION (pré-enregistrée) : on CÂBLE le diviseur ÷2 si ET SEULEMENT SI
  bear_mean < calm_mean - 0.10 $ ET part_bear < 40 % ET n_bear >= 20.
Sinon on PARQUE (pas de câblage). Réversible de toute façon.
Lecture seule moteur. 0 €, 0 ordre.
"""
import csv
import json
from collections import deque, defaultdict
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = ROOT + "/hulk-mexc/runs"
HIST = ROOT + "/Index_Maison/thermo/history.jsonl"
JOURNAL = RUNS + "/PAPER_V1_20261018_100103.csv"


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


hist = []
for ln in open(HIST, encoding="utf-8"):
    ln = ln.strip()
    if not ln:
        continue
    try:
        d = json.loads(ln)
    except Exception:
        continue
    t = parse_ts(d.get("ts"))
    if t is None:
        continue
    hist.append((t, d))
hist.sort(key=lambda x: x[0])
print(f"history : {len(hist)} pts ({hist[0][0].isoformat()} -> {hist[-1][0].isoformat()})")


def bear_ctx(t):
    best = None
    for ht, d in hist:
        if ht <= t:
            best = d
        else:
            break
    if best is None:
        return None, "pas d'historique"
    votes, why = 0, []
    try:
        ls = float(best.get("longShort") or 0)
    except Exception:
        ls = 0.0
    if ls >= 2.0:
        votes += 1; why.append(f"L/S {ls:.2f}>=2")
    try:
        f = float(best.get("funding") or 0); fa = float(best.get("fundingAvg30") or 0)
    except Exception:
        f, fa = 0.0, 0.0
    if fa > 0 and f > 1.5 * fa:
        votes += 1; why.append(f"fund {f:.1e}>1.5x{fa:.1e}")
    try:
        c24 = float(best.get("chg24") or 0)
    except Exception:
        c24 = 0.0
    if c24 <= -1.0:
        votes += 1; why.append(f"chg24 {c24:.2f}<=-1")
    if (best.get("climate") or "") == "hot":
        votes += 1; why.append("climat hot")
    return (votes >= 2), ("+".join(why) if why else "calme")


rows = list(csv.DictReader(open(JOURNAL, newline="", encoding="utf-8-sig")))
lots = defaultdict(deque)   # pair -> deque([qty, px])
buys = []                   # (pair, ts, qty, px, bear, why)
for r in rows:
    ts = parse_ts(r.get("ts") or "")
    if ts is None:
        continue
    p = r.get("pair") or ""
    ev = (r.get("event") or "").upper()
    try:
        q = float(r.get("qty") or 0.0); px = float(r.get("price") or 0.0)
    except Exception:
        continue
    if q <= 0 or px <= 0 or not p:
        continue
    if ev == "BAG_ARM":
        continue
    if ev in ("BUY", "DCA", "GBAG_PYRAMIDE", "BAG_DCA", "GBAG_SOUCHE"):
        lots[p].append([q, px])
        if ev != "GBAG_SOUCHE" or True:
            b, w = bear_ctx(ts)
            buys.append({"pair": p, "ts": ts, "qty": q, "px": px,
                         "bear": bool(b) if b is not None else None, "why": w,
                         "real": 0.0, "closed": 0.0})
    elif ev.startswith(("SELL", "STOP", "BAG")):
        rest = q
        while rest > 1e-12 and lots[p]:
            lq, lpx = lots[p][0]
            use = min(lq, rest)
            # attribue au prorata aux BUYs encore ouverts de cette paire (FIFO)
            need = use
            for b in buys:
                if b["pair"] != p or b["closed"] >= b["qty"] - 1e-12:
                    continue
                take = min(b["qty"] - b["closed"], need)
                b["real"] += (px - b["px"]) * take
                b["closed"] += take
                need -= take
                if need <= 1e-12:
                    break
            if lq <= rest + 1e-12:
                lots[p].popleft(); rest -= lq
            else:
                lots[p][0][0] = lq - rest; rest = 0.0

# marks live (DIGEST le plus récent) pour l'ouvert restant
live = {}
import glob as _glob
for f in sorted(_glob.glob(RUNS + "/DIGEST_202610*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for e in (d.get("pairs") or []):
        try:
            if e.get("pair") and float(e.get("last") or 0) > 0:
                live[e["pair"]] = float(e["last"])
        except Exception:
            pass

bear_r, calm_r, na_r = [], [], []
for b in buys:
    ouvert = b["qty"] - b["closed"]
    tot = b["real"] + ouvert * ((live.get(b["pair"], b["px"]) or b["px"]) - b["px"])
    b["total"] = tot
    (bear_r if b["bear"] is True else (calm_r if b["bear"] is False else na_r)).append(tot)

import statistics as st
def resume(xs):
    return (len(xs), round(st.mean(xs), 3) if xs else 0.0,
            round(100.0 * sum(1 for x in xs if x > 0) / len(xs), 1) if xs else 0.0,
            round(sum(xs), 2) if xs else 0.0)

nb, mb, wb, sb = resume(bear_r)
nc, mc, wc, sc_ = resume(calm_r)
print(f"\nBUY avec contexte : bear n={nb} moy={mb}$ win={wb}% somme={sb}$")
print(f"BUY contexte calme : n={nc} moy={mc}$ win={wc}% somme={sc_}$")
print(f"BUY sans contexte  : n={len(na_r)} (avant 30/07, ignores)")
part = nb / max(1, nb + nc)
print(f"part bear = {part:.1%} (seuil <40 %)")
print(f"\nDÉCISION pré-enregistrée : bear_moy({mb}) < calm_moy({mc}) - 0.10"
      f" ? {mb < mc - 0.10} | part<40% ? {part < 0.40} | n>=20 ? {nb >= 20}")
if mb < mc - 0.10 and part < 0.40 and nb >= 20:
    print("=> CÂBLER le diviseur devil ÷2 (1 flag, réversible)")
else:
    print("=> PARQUER (pas de câblage)")
