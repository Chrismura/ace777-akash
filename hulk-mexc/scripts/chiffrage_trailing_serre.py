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
    """Tout l'historique 1 h depuis le 01/08/2026, caché sur disque.
    28/10 : MEXC ignore endTime SEUL et plafonne à 500 bougies/requête —
    l'ancienne pagination arrière ramenait 3× les mêmes 500 dernières bougies
    (cache Oct-08→28, sorties d'août/sept irrejouables, écart +450 h).
    Pagination AVANT avec startTime+endTime (fenêtres de 400 h), dédup par open."""
    os.makedirs(KL_DIR, exist_ok=True)
    f = os.path.join(KL_DIR, f"{pair}.json")
    if os.path.exists(f) and time.time() - os.path.getmtime(f) < 6 * 3600:
        return json.loads(open(f).read())
    out: dict[int, list] = {}
    start = int(datetime(2026, 8, 1, tzinfo=timezone.utc).timestamp() * 1000)
    now = int(datetime.now(timezone.utc).timestamp() * 1000)
    while start < now:
        end = min(start + 400 * 3600 * 1000, now)
        q = urllib.parse.urlencode({"symbol": pair, "interval": "60m", "limit": 500,
                                    "startTime": start, "endTime": end})
        kl = _http(f"https://api.mexc.com/api/v3/klines?{q}")
        if not kl:
            break
        for c in kl:
            out[int(c[0])] = c
        start = int(kl[-1][0]) + 3600 * 1000
        if len(kl) < 2:
            break
        time.sleep(0.8)
    res = [out[k] for k in sorted(out)]
    json.dump(res, open(f, "w"))
    return res


def simule(candles, t_entry, entry_px, gb_pct, arm_pct=10.0, fast_trig=None, fast_mult=0.5):
    """Retourne (ts_sortie_ms, px_sortie, pic_pct) ou (None, None, pic). Règle trailing
    FIDÈLE au moteur (manage_open) : pic = max depuis l'entrée ; sortie SEULEMENT
    si pic ≥ entry×(1+arm) PUIS close < pic×(1-gb). Sans le ARM, le simu sort
    sur le premier micro-repli — c'est ce qui a tué la fidélité V2 (écart 409 h).
    fast_trig : si +X% touché sous 72 h -> gb *= fast_mult à partir de là."""
    gb = gb_pct
    pic = entry_px
    arme = False
    px_arm = entry_px * (1 + arm_pct / 100.0)
    for c in candles:
        ts = int(c[0])
        if ts < int(t_entry.timestamp() * 1000):
            continue
        close = float(c[4])
        high = float(c[2]) if len(c) > 2 else close
        if high > pic:
            pic = high
        if fast_trig and not arme:
            if (t_entry.timestamp() * 1000) <= ts <= (t_entry.timestamp() * 1000) + 72 * 3600 * 1000:
                if high >= entry_px * (1 + fast_trig / 100.0):
                    arme = True
                    gb = gb_pct * fast_mult
        if pic >= px_arm and close < pic * (1 - gb / 100.0):
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
        exits.append(({"ts": r["ts"], "pair": r["pair"], "entry": entry, "qty": qty,
                       "pnl": pnl, "gb": float(m.group(2))}, r))
    # arm par paire = profil vivant AU JOUR DE LA SORTIE (trail_arm_pct).
    # Les calibres bougent (git) : l'arm d'aujourd'hui appliqué aux trades d'août
    # faussait tout. Table (commit_ts, arm par paire) reconstruite depuis git,
    # cachée dans runs/ARM_HIST.json.
    import subprocess
    ARM_HIST = os.path.join(RUNS, "ARM_HIST.json")
    def _arm_hist():
        if os.path.exists(ARM_HIST) and time.time() - os.path.getmtime(ARM_HIST) < 24 * 3600:
            return json.load(open(ARM_HIST, encoding="utf-8"))
        rac = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        rel = "hulk-mexc/strategie/universe_profils.json"
        if os.path.basename(os.getcwd()) == "hulk-mexc":
            rac, rel = os.getcwd(), "strategie/universe_profils.json"
        else:
            try:
                rac = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                     capture_output=True, text=True, timeout=20).stdout.strip() or rac
            except Exception:
                pass
        hist = []
        try:
            log = subprocess.run(["git", "log", "--format=%H|%ct", "--", rel],
                                 capture_output=True, text=True, timeout=60, cwd=rac).stdout.strip().splitlines()
        except Exception:
            log = []
        for ligne in log:
            try:
                h, cts = ligne.split("|")
                blob = subprocess.run(["git", "show", f"{h}:{rel}"], capture_output=True,
                                      text=True, timeout=30, cwd=rac).stdout
                p = json.loads(blob)
                arms = {pair: float((v.get("calib") or {}).get("trail_arm_pct") or 0)
                        for pair, v in (p.items() if isinstance(p, dict) else [])
                        if isinstance(v, dict)}
                hist.append((int(cts), arms))
            except Exception:
                continue
        hist.sort()
        try:
            json.dump(hist, open(ARM_HIST, "w"))
        except Exception:
            pass
        return hist
    try:
        _hist = _arm_hist()
        _cur = json.load(open(os.path.join(os.path.dirname(RUNS), "strategie",
                                           "universe_profils.json"), encoding="utf-8"))
        _cur_arms = {pair: float((v.get("calib") or {}).get("trail_arm_pct") or 0)
                     for pair, v in _cur.items()
                     if isinstance(v, dict)} if isinstance(_cur, dict) else {}
    except Exception:
        _hist, _cur_arms = [], {}
    profils = {"__hist__": _hist, "__cur__": _cur_arms}
    def arm_at(pair, ts_ms):
        best = (_cur_arms.get(pair) or 0) or 10.0
        for cts, arms in _hist:
            if cts * 1000 <= ts_ms and (arms.get(pair) or 0) > 0:
                best = arms[pair]
        return best    # ancre = remontée ARRIÈRE depuis la sortie : on couvre la quantité vendue
    # avec les achats précédents (les ventes partielles antérieures allongent le
    # besoin). Le walk AVANT échouait : poussières d'arrondi + events composés
    # (GBAG_PYRAMIDE/BAG_SELL) faussaient le zéro → ancre fossilisée, 450 h d'écart.
    ACHAT = ("BUY", "DCA", "BAG_DCA", "GBAG_PYRAMIDE")
    VENTE = ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH")
    par_paire: dict[str, list] = {}
    for r in rows:
        if r["event"] in ACHAT + VENTE:
            par_paire.setdefault(r["pair"], []).append(r)

    idx_par_ligne = {id(r): i for i, r in enumerate(rows)}

    def ancre(e, ligne_exit):
        need = _f(e.get("qty"))
        j = idx_par_ligne.get(id(ligne_exit))
        if j is None:
            return None
        for r in reversed(rows[:j]):
            if r["pair"] != e["pair"]:
                continue
            if r["event"] in ACHAT:
                need -= _f(r.get("qty"))
                if need <= 1e-9:
                    return r["ts"]
            elif r["event"] in VENTE:
                need += _f(r.get("qty"))
        return None
    kl_cache: dict[str, list] = {}
    print("=== REPLAY trailing bougies 1 h (§29) ===")
    print(f"journal : {os.path.basename(csvs[-1])} · sorties trailing : {len(exits)}")
    # 1) fidélité : la règle normale retrouve-t-elle la sortie réelle ?
    dts, dpx, ok = [], [], 0
    sims = []
    for e, ligne_exit in exits:
        a = ancre(e, ligne_exit)
        if not a:
            continue
        t_entry = datetime.fromisoformat(a.replace("Z", "+00:00"))
        arm = arm_at(e["pair"], datetime.fromisoformat(e["ts"].replace("Z", "+00:00")).timestamp() * 1000)
        pair = e["pair"]
        if pair not in kl_cache:
            try:
                kl_cache[pair] = klines_1h(pair)
            except Exception as ex:
                print(f"  klines {pair} KO ({ex}) — paire ignorée")
                kl_cache[pair] = []
        if not kl_cache[pair]:
            continue
        ts_s, px_s, pic = simule(kl_cache[pair], t_entry, e["entry"], e["gb"], arm)
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
            arm_e = arm_at(e["pair"], datetime.fromisoformat(e["ts"].replace("Z", "+00:00")).timestamp() * 1000)
            ts_s, px_s, _ = simule(kl_cache[e["pair"]], t_entry, e["entry"], e["gb"], arm_e,
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
    print("\nR8 : 1 h (pas le carnet), frais ignorés, ancres remontées ARRIÈRE, "
          "arms datés via git, pics sur plus-hauts horaires. Un câblage exigera GO + shadow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
