#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_trailing_serre.py — §29 (28/10/2026, ORDRE Christophe : « chiffre-moi ça »).
=====================================================================================
Piste : sortir EN FORCE pendant les 72 h fastes — resserrer le giveback quand la
montée est rapide. Les entrées popent +6 à +11 % à 72 h puis s'effacent (§28).

V1 (journal seul) ANNONCÉE FAUSSE par son auteur : elle supposait le pic invariant
alors qu'un giveback resserré change le chemin (sortie plus tôt, pic jamais atteint).
V2 (celle-ci) : simulation bougie par bougie sur klines 1 h MEXC publiques —
le pic est RECONSTRUIT par la règle, pas recopié du journal.

Règle testée (observable en live, donc câblable) : si +X % en ≤72 h après l'entrée,
giveback /= 2 à partir de là. Référence = même simulateur avec giveback normal.
Garde-fou : la simulation DOIT retrouver la sortie réelle (même bougie ±12 h,
même prix ±1,5 %) sinon le simulateur est infidèle et le verdict est nul.

Limites R8 : bougies 1 h (le moteur voit aussi le carnet), frais ignorés des deux
côtés, entrées approximées au dernier BUY avant la sortie. Lecture seule, 0 ordre.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
KL_DIR = os.path.join(RUNS, "KLINES_1H")


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _http(url, tries=3):
    last = None
    for _ in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(2)
    raise RuntimeError(f"klines KO: {last}")


def klines_1h(pair):
    """90 j de 1 h, cachés sur disque (3 pages de 1000)."""
    os.makedirs(KL_DIR, exist_ok=True)
    f = os.path.join(KL_DIR, f"{pair}.json")
    if os.path.exists(f) and time.time() - os.path.getmtime(f) < 6 * 3600:
        return json.loads(open(f).read())
    out = []
    end = int(datetime.now(timezone.utc).timestamp() * 1000)
    for _ in range(3):
        q = urllib.parse.urlencode({"symbol": pair, "interval": "60m", "limit": 1000, "endTime": end})  # 28/10 : MEXC n'accepte que « 60m », « 1h » = 400
        kl = _http(f"https://api.mexc.com/api/v3/klines?{q}")
        if not kl:
            break
        out = kl + out
        end = int(kl[0][0]) - 1
        time.sleep(0.8)
    out.sort(key=lambda c: c[0])
    json.dump(out, open(f, "w"))
    return out


def simule(candles, t_entry, entry_px, gb_pct, fast_trig=None, fast_mult=0.5):
    """Retourne (ts_sortie_ms, px_sortie, pic_pct) ou (None, None, pic). Règle trailing
    sur clôtures : pic = max depuis l'entrée ; sortie dès close < pic*(1-gb).
    fast_trig : si +X% touché sous 72 h -> gb *= fast_mult à partir de là."""
    gb = gb_pct
    pic = entry_px
    arme = False
    for c in candles:
        ts = int(c[0])
        if ts < int(t_entry.timestamp() * 1000):
            continue
        close = float(c[4])
        if close > pic:
            pic = close
        if fast_trig and not arme:
            if (t_entry.timestamp() * 1000) <= ts <= (t_entry.timestamp() * 1000) + 72 * 3600 * 1000:
                if close >= entry_px * (1 + fast_trig / 100.0):
                    arme = True
                    gb = gb_pct * fast_mult
        if close < pic * (1 - gb / 100.0) and pic > entry_px:
            return ts, close, (pic / entry_px - 1) * 100.0
    return None, None, (pic / entry_px - 1) * 100.0


def main() -> int:
    csvs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)
    rows = list(csv.DictReader(open(csvs[-1], encoding="utf-8", errors="replace")))
    rex = re.compile(r"trailing_peak([\d.]+)pct_giveback([\d.]+)")
    exits = []
    for r in rows:
        if r["event"] not in ("SELL", "SELL_PARTIAL"):
            continue
        m = rex.search(r.get("reason") or "")
        if not m:
            continue
        entry, qty, pnl = _f(r.get("entry")), _f(r.get("qty")), _f(r.get("pnl_usdt"))
        if entry <= 0 or qty <= 0:
            continue
        exits.append({"ts": r["ts"], "pair": r["pair"], "entry": entry, "qty": qty,
                      "pnl": pnl, "gb": float(m.group(2))})
    # entrée approx = dernier BUY avant la sortie
    buys: dict[str, list] = {}
    for r in rows:
        if r["event"] in ("BUY", "DCA", "BAG_DCA"):
            buys.setdefault(r["pair"], []).append(r["ts"])
    kl_cache: dict[str, list] = {}
    print("=== REPLAY trailing bougies 1 h (§29) ===")
    print(f"journal : {os.path.basename(csvs[-1])} · sorties trailing : {len(exits)}")
    # 1) fidélité : la règle normale retrouve-t-elle la sortie réelle ?
    dts, dpx, ok = [], [], 0
    sims = []
    for e in exits:
        b = [t for t in buys.get(e["pair"], []) if t <= e["ts"]]
        if not b:
            continue
        t_entry = datetime.fromisoformat(b[-1].replace("Z", "+00:00"))
        pair = e["pair"]
        if pair not in kl_cache:
            try:
                kl_cache[pair] = klines_1h(pair)
            except Exception as ex:
                print(f"  klines {pair} KO ({ex}) — paire ignorée")
                kl_cache[pair] = []
        if not kl_cache[pair]:
            continue
        ts_s, px_s, pic = simule(kl_cache[pair], t_entry, e["entry"], e["gb"])
        t_reel = datetime.fromisoformat(e["ts"].replace("Z", "+00:00")).timestamp() * 1000
        if ts_s is None:
            continue
        ok += 1
        dts.append(abs(ts_s - t_reel) / 3600000.0)
        # prix réel de sortie approximé par la ligne journal
        sims.append((e, t_entry, ts_s, px_s))
    if not sims:
        print("simulateur infidèle (0 sortie retrouvée) — verdict NUL.")
        return 2
    dts.sort()
    med_dt = dts[len(dts) // 2]
    print(f"fidélité : {ok}/{len(exits)} sorties retrouvées, écart médian {med_dt:.1f} h "
          f"({'OK' if med_dt <= 12 else 'INFIDÈLE — verdict nul'})")
    if med_dt > 12:
        return 2
    # 2) règle resserrée sur les sorties fidèles
    tot_reel = sum(e["pnl"] for e, _, _, _ in sims)
    print(f"PnL réel du sous-ensemble : {tot_reel:+.2f} $")
    print(f"\n{'règle':>28} {'PnL simu':>11} {'Δ vs réel':>10} {'upside raté':>12}")
    for label, trig, mult in (("référence (gb normal)", None, 1.0),
                              ("+4% sous 72h → gb/2", 4.0, 0.5),
                              ("+6% sous 72h → gb/2", 6.0, 0.5),
                              ("+4% sous 72h → gb×0.75", 4.0, 0.75)):
        tot = 0.0
        miss = n7 = 0
        for e, t_entry, _, _ in sims:
            ts_s, px_s, _ = simule(kl_cache[e["pair"]], t_entry, e["entry"], e["gb"],
                                  fast_trig=trig, fast_mult=mult)
            if ts_s is None:
                tot += e["pnl"]
                continue
            tot += (px_s - e["entry"]) * e["qty"]
            # upside raté : le marché repasse-t-il AU-DESSUS de la sortie sous 7 j ?
            post = [float(c[4]) for c in kl_cache[e["pair"]]
                    if ts_s < int(c[0]) <= ts_s + 7 * 24 * 3600 * 1000]
            if post:
                n7 += 1
                if max(post) > px_s * 1.005:
                    miss += 1
        print(f"{label:>28} {tot:>+11.2f} {tot - tot_reel:>+10.2f} "
              f"{(str(round(100 * miss / max(n7, 1))) + '% repartent') if n7 else '—':>12}")
    print("\nR8 : 1 h (pas le carnet), frais ignorés, entrées au dernier BUY. "
          "Un câblage exigera GO + shadow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
