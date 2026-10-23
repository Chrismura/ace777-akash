#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_recup_full30.py — trajectoire de l'ecart vs HOLD-FULL30 (19/10 -> now).

Question Christophe : depuis l'introduction du benchmark full-30 (GO 20/10),
combien a-t-on recupere ? Impression : +70/80 $.

Methode (memes regles comptables que le feed cockpit_mission_feed.py) :
- cash init par paire = budget mission (seed_val + 20) ; rejeu du journal
  (BUY/DCA/GBAG_PYRAMIDE -> cash -= notional+fee ; GBAG_SOUCHE -> tout le cash
  converti ; SELL/STOP/BAG* -> cash += notional-fee ; BAG_ARM ignore ;
  feeRate 0.0005) jusqu'a T ; positions = +-qty du journal.
- MARKS(T) = prix DIGEST (vrai prix live par paire, pas le dernier prix du
  journal qui est stale : QNT +35 %, PYTH +23 % le 23/10).
- seed/sp/budget = constantes mission (seedPx lu, pas devine) ; full30(T) =
  meme formule + memes replis que le feed.
VALIDATION integree : a T=now, l'ecart recalcule doit coller au fichier (+-2 $).
Sinon STOP (methode fausse, chiffres historiques non publies).
Lecture seule, 0 ordre.
"""
import csv
import glob
import json
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
RUNS = ROOT + "/hulk-mexc/runs"
MISSION = ROOT + "/Index_Maison/cockpit/mission.json"
FEE = 0.0005
MARGE = 20.0


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


def digest_marks():
    idx = {}
    for f in sorted(glob.glob(RUNS + "/DIGEST_202610*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        t = parse_ts(d.get("ts"))
        if t is None:
            continue
        px = {}
        for e in (d.get("pairs") or []):
            try:
                if e.get("pair") and float(e.get("last") or 0) > 0:
                    px[e["pair"]] = float(e["last"])
            except Exception:
                continue
        if px:
            idx[t] = px
    return idx


_MARKS = digest_marks()
print(f"index DIGEST : {len(_MARKS)} points "
      f"({min(_MARKS).isoformat() if _MARKS else '?'} -> "
      f"{max(_MARKS).isoformat() if _MARKS else '?'})")


def marks_at(t_lim):
    best, out = None, {}
    for t in sorted(_MARKS):
        if t <= t_lim:
            best = t
        else:
            break
    return dict(_MARKS.get(best, {}))


def snapshot(t_lim):
    mission = json.load(open(MISSION, encoding="utf-8"))
    hv = mission["hulk"]["hulkVsHold"]
    consts = {p["pair"]: p for p in hv["pairs"]}
    rows = list(csv.DictReader(open(RUNS + "/PAPER_V1_20261018_100103.csv",
                                    newline="", encoding="utf-8-sig")))
    cash, hold_qty = {}, {}
    for p, c in consts.items():
        cash[p] = float(c.get("budget") or 0.0)
        hold_qty[p] = 0.0
    for r in rows:
        ts = parse_ts(r.get("ts") or "")
        if ts is None or ts > t_lim:
            continue
        p = r.get("pair") or ""
        if p not in cash:
            continue
        ev = (r.get("event") or "").upper()
        if ev == "BAG_ARM":
            continue
        if (ev not in ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE")
                and not ev.startswith(("SELL", "STOP", "BAG"))):
            continue
        try:
            q = float(r.get("qty") or 0.0)
            px = float(r.get("price") or 0.0)
        except Exception:
            continue
        if q <= 0 or px <= 0:
            continue
        notion = q * px
        fee = notion * FEE
        if ev == "GBAG_SOUCHE":
            cash[p] -= max(0.0, cash[p])
            hold_qty[p] += q
        elif ev in ("BUY", "DCA", "GBAG_PYRAMIDE", "BAG_DCA"):
            # BAG_DCA = RACHAT (feed ligne ~861, traite comme BUY, pas comme vente)
            cash[p] -= notion + fee
            hold_qty[p] += q
        else:
            cash[p] += notion - fee
            hold_qty[p] -= q
    marks = marks_at(t_lim)
    reel, hold, full = {}, {}, {}
    for p, c in consts.items():
        budget = float(c.get("budget") or 0.0)
        mk = marks.get(p, 0.0)
        reel[p] = cash[p] + max(0.0, hold_qty[p]) * mk
        # seedQty mission = jetons du seed ; seed = 10 $ -> sp = 10/seedQty.
        # full30 = (budget/sp)*mark = budget*seedQty*mark/10 (feed, meme formule).
        try:
            sq = float(c.get("seedQty") or 0.0)
            su = float(c.get("seed") or 0.0)
        except Exception:
            sq, su = 0.0, 0.0
        hold[p] = sq * mk + MARGE if (mk and sq) else budget
        full[p] = (budget * sq * mk / su) if (mk and sq and su and budget) else budget
    return reel, hold, full


now = datetime.now(timezone.utc)
etapes = [
    ("19/10 00:00Z (avant GO full30)", datetime(2026, 10, 19, tzinfo=timezone.utc)),
    ("20/10 12:00Z (GO full30 ~midi)", datetime(2026, 10, 20, 12, tzinfo=timezone.utc)),
    ("21/10 00:00Z (GO seuils+short)", datetime(2026, 10, 21, tzinfo=timezone.utc)),
    ("22/10 00:00Z", datetime(2026, 10, 22, tzinfo=timezone.utc)),
    ("23/10 now", now),
]
print(f"{'etape':28s} {'reel':>10s} {'full30':>10s} {'ecart':>10s}")
res = []
for nom, t in etapes:
    r, h, f = snapshot(t)
    e = round(sum(r.values()) - sum(f.values()), 2)
    res.append((nom, sum(r.values()), sum(f.values()), e))
    print(f"{nom:28s} {sum(r.values()):10.2f} {sum(f.values()):10.2f} {e:10.2f}")
print()
print(f"VALIDATION now vs fichier : recalcule={res[-1][3]} fichier=-3.53 (20:34Z)")
if abs(res[-1][3] - (-3.53)) > 2.0:
    print("ECART TROP GRAND — methode non valide, chiffres historiques NON publies.")
else:
    print(f"RECUP depuis le 19/10 : {round(res[-1][3] - res[0][3], 2):+.2f} $ "
          f"({res[0][3]} -> {res[-1][3]})")
    print(f"RECUP depuis le 20/10 (GO) : {round(res[-1][3] - res[1][3], 2):+.2f} $")
    print(f"RECUP depuis le 21/10 : {round(res[-1][3] - res[2][3], 2):+.2f} $")
